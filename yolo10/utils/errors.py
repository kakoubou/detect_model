# yolo10 YOLO 🚀, AGPL-3.0 license

from yolo10.utils import emojis


class HUBModelError(Exception):
    """
    Custom exception class for handling errors related to model fetching in yolo10 YOLO.

    This exception is raised when a requested model is not found or cannot be retrieved.
    The message is also processed to include emojis for better user experience.

    Attributes:
        message (str): The error message displayed when the exception is raised.

    Note:
        The message is automatically processed through the 'emojis' function from the 'yolo10.utils' package.
    """

    def __init__(self, message="Model not found. Please check model URL and try again."):
        """Create an exception for when a model is not found."""
        super().__init__(emojis(message))
