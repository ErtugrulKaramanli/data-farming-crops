"""
This module defines the Corn crop class.
"""

from farm.crop import Crop


class Corn(Crop):
    """
    Represents a corn crop, inheriting basic traits from Crop.
    """

    def water(self):
        """
        Waters the corn crop, increasing its grains by 10.
        """
        self.grains += 10
