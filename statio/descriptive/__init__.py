"""
Descriptive statistics provided by Statio.

This module exposes the core descriptive statistics functions
available in the Statio library.
"""

from .mean import mean
from .median import median
from .mode import mode
from .variance import variance

__all__ = [
    "mean",
    "median",
    "mode",
    "variance",
]