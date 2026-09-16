"""
Image preprocessing pipeline.
"""

import numpy as np

def preprocess_image(image: np.ndarray) -> np.ndarray:
    """
    Apply the preprocessing pipeline to a single input image.

    Args:
        image: Raw input image as a numpy array.
    Returns:
        The preprocessed image, ready for character segmentation.
    """
    raise NotImplementedError("Preprocessing pipeline not yet implemented.")


def segment_characters(image: np.ndarray) -> list[np.ndarray]:
    """
    Split a preprocessed expression image into individual characters.

    Args:
        image: A preprocessed image containing a full expression.
    Returns:
        A list of cropped images, one per detected character, ordered
        left to right (ordering logic to be refined for multi-line or
        spatial notation later).
    """
    raise NotImplementedError("Character segmentation not yet implemented.")
