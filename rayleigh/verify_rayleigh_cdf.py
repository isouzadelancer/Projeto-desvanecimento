import numpy as np
import matplotlib.pyplot as plt
from gen_rayleigh_va import gen_rayleigh_va

def verify_rayleigh_cdf(omega_c, N=100000):
    samples = gen_rayleigh_va(N, omega_c)
    sigma = np.sqrt(omega_c / 2)
    x = np.linspace(0, np.max(samples), 1000)
    cdf_teorica = 1 - np.exp(-x**2 / (2 * sigma**2))
    samples_sorted = np.sort(samples)
    cdf_empirica = np.arange(1, len(samples) + 1) / len(samples)

    plt.figure()
    plt.plot(samples_sorted, cdf_empirica, label='Empírica')
    plt.plot(x, cdf_teorica, 'r--', label='Teórica')
    plt.title(f'CDF Rayleigh - Ωc = {omega_c}')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidade acumulada')
    plt.legend()
    plt.grid()
    plt.savefig(f'graficos/cdf_rayleigh_omega{omega_c}.png')
    plt.close()
