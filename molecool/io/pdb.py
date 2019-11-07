import numpy as np

def open_pdb(file_location):
    # This function reads in a pdb file and returns the atom names and coordinates.
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
