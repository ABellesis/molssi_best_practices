#We need another init file to make sure different parts of the package are communicating smoothly with each other. The init file in the main 
#directory is not enough after we broke up the original functions.py file

from .pdb import open_pdb 
from .xyz import open_xyz, write_xyz

#Hence, anytime anyone tries to import molecool, it should also import the above.
