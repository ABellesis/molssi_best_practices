import numpy as np

def calculate_distance(rA, rB): #(rA, rB) are points in space corresponding to atoms
    ''' 
    This function calculates the distance between two points given as numpy arrays. 
    Parameters
    ----------
    rA, rB, rC: type: np.ndarray
	The coordinates of each point. 
 
   Returns
    -------
    distance : float
        The distance between two points.

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([3.0, 0, 0])
    >>> calculate_distance(r1, r2)
    3.0
    '''

    dist_vector = (rA - rB)
    dist=np.linalg.norm(dist_vector)
    return dist

def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta=np.arccos(np.dot(AB, BC)/(np.linalg.norm(AB)*np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return thetaatom_
