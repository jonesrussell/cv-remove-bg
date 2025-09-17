#!/usr/bin/env python3
"""
Background Removal Tool using OpenCV
====================================

This script removes backgrounds from images using the GrabCut algorithm.
It processes all images in the 'images/' folder and saves results with
transparent backgrounds to the 'output/' folder.

Usage:
    python background_removal.py

Requirements:
    - Input images in 'images/' folder (jpg, jpeg, png)
    - Results saved to 'output/' folder as PNG files with transparency
"""

import argparse
import logging
import sys
from pathlib import Path

import cv2
import numpy as np
from tqdm import tqdm

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


class BackgroundRemover:
    """Background removal utility using OpenCV GrabCut algorithm."""

    def __init__(self, input_dir="images", output_dir="output", margin=0.05):
        """
        Initialize the background remover.

        Args:
            input_dir (str): Directory containing input images
            output_dir (str): Directory to save processed images
            margin (float): Margin percentage for GrabCut rectangle (default: 0.05 = 5%)
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.margin = margin
        self.valid_extensions = {".jpg", ".jpeg", ".png", ".bmp", ".tiff"}

        self._validate_directories()

    def _validate_directories(self):
        """Validate and create necessary directories."""
        if not self.input_dir.exists():
            logger.error(f"Input folder '{self.input_dir}' not found.")
            raise FileNotFoundError(f"Missing input folder: {self.input_dir}")

        self.output_dir.mkdir(exist_ok=True)
        logger.info(f"Output directory: {self.output_dir}")

    def process_image(self, image_path):
        """
        Process a single image to remove background.

        Args:
            image_path (Path): Path to the input image

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Read image
            img = cv2.imread(str(image_path))
            if img is None:
                logger.warning(f"Skipping {image_path.name} (unable to read)")
                return False

            # Get image dimensions
            height, width = img.shape[:2]

            # Calculate rectangle for GrabCut (with margin)
            x = int(width * self.margin)
            y = int(height * self.margin)
            rect = (x, y, width - 2 * x, height - 2 * y)

            # Initialize mask and models for GrabCut
            mask = np.zeros(img.shape[:2], np.uint8)
            bgd_model = np.zeros((1, 65), np.float64)
            fgd_model = np.zeros((1, 65), np.float64)

            # Apply GrabCut algorithm
            cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

            # Create binary mask (0 = background, 1 = foreground)
            mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

            # Convert to RGBA and apply mask to alpha channel
            output_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
            output_rgba[:, :, 3] = mask2 * 255  # 0 for background, 255 for foreground

            # Save as PNG to preserve transparency
            output_path = self.output_dir / image_path.with_suffix(".png").name
            cv2.imwrite(str(output_path), output_rgba)
            logger.info(f"✓ Saved: {output_path.name}")
            return True

        except Exception as e:
            logger.error(f"✗ Error processing {image_path.name}: {e}")
            return False

    def process_all_images(self):
        """Process all valid images in the input directory."""
        # Find all valid image files
        image_files = [
            f
            for f in self.input_dir.iterdir()
            if f.suffix.lower() in self.valid_extensions
        ]

        if not image_files:
            logger.warning(f"No valid image files found in '{self.input_dir}' folder.")
            logger.info(f"Supported formats: {', '.join(self.valid_extensions)}")
            return

        logger.info(f"Found {len(image_files)} image(s) to process")

        # Process each image with progress bar
        successful = 0
        for image_path in tqdm(image_files, desc="Processing images", unit="image"):
            if self.process_image(image_path):
                successful += 1

        logger.info(
            f"Processing complete! {successful}/{len(image_files)} images "
            f"processed successfully."
        )

    def process_single_image(self, image_path):
        """Process a single specified image."""
        image_path = Path(image_path)
        if not image_path.exists():
            logger.error(f"Image not found: {image_path}")
            return False

        if image_path.suffix.lower() not in self.valid_extensions:
            logger.error(f"Unsupported file format: {image_path.suffix}")
            logger.info(f"Supported formats: {', '.join(self.valid_extensions)}")
            return False

        logger.info(f"Processing single image: {image_path.name}")
        return self.process_image(image_path)


def main():
    """Main function to run the background removal tool."""
    parser = argparse.ArgumentParser(
        description="Remove backgrounds from images using OpenCV",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python background_removal.py  # Process all images in 'images/' folder
  python background_removal.py --single image.jpg  # Process single image
  python background_removal.py --margin 0.1  # Use 10% margin for GrabCut
        """,
    )

    parser.add_argument(
        "--input",
        "-i",
        default="images",
        help="Input directory containing images (default: images)",
    )

    parser.add_argument(
        "--output",
        "-o",
        default="output",
        help="Output directory for processed images (default: output)",
    )

    parser.add_argument("--single", "-s", help="Process a single image file")

    parser.add_argument(
        "--margin",
        "-m",
        type=float,
        default=0.05,
        help="Margin percentage for GrabCut rectangle (default: 0.05 = 5%%)",
    )

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        # Initialize background remover
        remover = BackgroundRemover(
            input_dir=args.input, output_dir=args.output, margin=args.margin
        )

        # Process images
        if args.single:
            success = remover.process_single_image(args.single)
            sys.exit(0 if success else 1)
        else:
            remover.process_all_images()

    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
