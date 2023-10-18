import numpy as np
from constants import h, c, quantum_limit
from temperature_effects import black_body_radiation
from materials import get_material_efficiency
from technology import apply_technological_factor


def simulate_photon_flux_density(frequency, temperature, material):
    """
    Integrated simulation to calculate photon flux density considering all factors.
    """
    base_density = black_body_radiation(frequency, temperature)
    quantum_deviation = quantum_limit(frequency)

    # Apply material efficiency
    material_efficiency = get_material_efficiency(material)
    base_density *= material_efficiency

    # Apply technological constraints
    final_density = apply_technological_factor(
        base_density + quantum_deviation)

    return final_density
