import numpy as np
from constants import h, k, c


def black_body_radiation(frequency, temperature):
    """
    Calculate the photon flux density based on the black body radiation formula.
    This gives the photon flux density emitted by a black body in thermal equilibrium.
    """
    term1 = (8 * np.pi * frequency**2) / c**3
    term2 = h * frequency / (np.exp((h * frequency) / (k * temperature)) - 1)
    return term1 * term2
