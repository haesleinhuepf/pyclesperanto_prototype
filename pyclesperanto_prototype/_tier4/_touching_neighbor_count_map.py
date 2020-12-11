from .._tier0 import plugin_function
from .._tier0 import Image
from .._tier1 import generate_touch_matrix
from .._tier1 import count_touching_neighbors
from .._tier1 import replace_intensities

@plugin_function
def touching_neighbor_count_map(labels : Image, map_destination : Image = None):
    """

    Parameters
    ----------
    labels
    map_destination

    Returns
    -------

    """
    touch_matrix = generate_touch_matrix(labels)
    number_of_touching_neighbors_vector = count_touching_neighbors(touch_matrix)
    replace_intensities(labels, number_of_touching_neighbors_vector, map_destination)
    return map_destination
