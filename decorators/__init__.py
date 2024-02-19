# decorators package

from . import logging_decorators
from . import performance_decorators

# Define the package lever version.
__version__ = "0.01"

__author__ = "Kaleb Soller"

__email__ = "don't email me"

__license__ = "MIT"

__description__ = "Project Decorator descriptions"

__url__ = "www.google.com"


# Perform any other initialization tasks
print("Initializing 'decorators' package...")

__all__ = ["logging_decorators", "performance_decorators"]