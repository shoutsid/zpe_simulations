import matplotlib.pyplot as plt

def visualize_results(frequencies, densities, title="Photon Flux Density vs. Frequency"):
    plt.plot(frequencies, densities, label="Simulated Density")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Photon Flux Density")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()
