import numpy as np

def transform(sequence):
    '''Transforms a DNA sequence into a series of coordinates for 2D visualization.

    Args:
        sequence (str): The DNA sequence to transform.

    Returns:
        tuple: A tuple containing two lists: one for the x coordinates and one for the y coodinates.

    Example:
        >>> transform("ATG")
        ([0, 0.5, 1, 1, 1.5, 2, 2, 2.5, 3], [0, 1, 0, -1, -2, -1, 0])

    '''
    running_value = 0
    x, y = np.linspace(0, len(sequence), 2 * len(sequence) + 1), [0]
    for i, character in enumerate(sequence.upper()):
        if character == "A":
            y.extend([running_value + 1, running_value])
        elif character == "C":
            y.extend([running_value - 1, running_value])
        elif character == "T":
            y.extend([running_value - 1, running_value - 2])
            running_value -= 2
        elif character == "G":
            y.extend([running_value + 1, running_value + 2])
            running_value += 2
        else:
            y.extend([running_value] * 2)
    return list(x), y
