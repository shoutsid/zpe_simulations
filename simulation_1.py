import numpy as np
import matplotlib.pyplot as plt

# Constants
C = 3e8  # Speed of light in m/s
H_BAR = 1.0545718e-34  # Reduced Planck constant in J.s
E_CUTOFF = 4 * 1.60218e-19  # 4 eV to Joules


# Photon flux density formula
def rho(f):
    return (f**3) / (np.exp(H_BAR * f / E_CUTOFF) - 1)


# Total flux available over a range of frequencies
def total_flux(f_min, f_max):
    freqs = np.linspace(f_min, f_max, 1000)
    integrand = freqs**2 / (np.exp(H_BAR * freqs / E_CUTOFF) - 1)
    return np.trapz(integrand, freqs)


# Simulate the harvest of energy
def harvest_energy(f_min, f_max):
    return H_BAR * total_flux(f_min, f_max)


# Visualization
def plot_simulation(f_min, f_max):
    freqs = np.linspace(f_min, f_max, 1000)
    densities = rho(freqs)

    plt.plot(freqs, densities)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Photon Flux Density")
    plt.title("Photon Flux Density vs. Frequency")
    plt.grid(True)
    plt.show()


# Run the simulation
if __name__ == "__main__":
    f_min, f_max = 1e12, 1e15  # Sample frequency range in Hz (from THz to PHz)
    plot_simulation(f_min, f_max)
    energy_harvested = harvest_energy(f_min, f_max)
    print(f"Total energy harvested: {energy_harvested} Joules")
