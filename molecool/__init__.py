"""
molecool
A python package for analyzing and visualizing molecules. For MolSSI Best practices Nov 2019
"""

# Add imports here
from .functions import * #Import all functions; call using molecool.canvas()
#import molecool.functions #Another way to call our functions; call using molecool.functions.canvas()

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
