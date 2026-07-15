"""
This module defines the base Crop class for all crops on the farm.
"""

# pylint: disable=too-few-public-methods
class Crop:
    """
    A base class representing a generic crop with growth and ripeness traits.
    """

    def __init__(self):
        """
        Initializes a new crop with zero grains.
        """
        self.grains = 0

    def ripe(self):
        """
        Checks if the crop is ripe. Returns True if grains are at least 15.
        """
        return self.grains >= 15
