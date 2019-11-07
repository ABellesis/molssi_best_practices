import numpy as np

def open_pdb(file_location):
    '''
    This function reads in a pdb file and returns the atoms and coordinates.

    The PDB file must specify the atom elements in the last column and follow the conventions outlined in the PDB format specification.
    
    Parameters
    ----------
    file_location: string
        Find the pdb that you want to use
    
    Returns
    -------
    symbols: list 
        The atomic symbols of the pdb file
    coords: numpy array
        Return atomic coordinates of the pdb file
    '''          
    with open(file_location) as f:
        data = f.readlines()

    coordinates = [] #White space around  =, <, >, etc is not required but is best practice.
    symbols = []

    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    return symbols, coords
