MATERIALS = {
    'gold': {
        'efficiency': 0.9,  # made-up value, actual value may vary
        'band_gap': 2.4     # eV, this might affect the energy harvesting process
    },
    'silicon': {
        'efficiency': 0.85,
        'band_gap': 1.1     # eV
    }
    # ... other materials can be added
}


def get_material_efficiency(material_name):
    return MATERIALS.get(material_name, {}).get('efficiency', 1)
