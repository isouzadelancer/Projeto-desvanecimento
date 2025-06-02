import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rice
from gen_rice_va import gen_rice_va

def verify_rice_cdf(omega_c, K, N=100000):
    samples = gen_rice_va(N, omega_c, K)
    v = np.sqrt((K * omega_c) / (K + 1)) / np.sqrt(omega_c / (2 * (K + 1)))
    scale = np.sqrt(omega_c / (2 * (K + 1)))
    x = np.linspace(0, np.max(samples), 1000)
    cdf_teorica = rice.cdf(x, v, scale=scale)
    samples_sorted = np.sort(samples)
    cdf_empirica = np.arange(1, len(samples) + 1) / len(samples)

    plt.figure()
    plt.plot(samples_sorted, cdf_empirica, label='Empírica')
    plt.plot(x, cdf_teorica, 'r--', label='Teórica')
    plt.title(f'CDF Rice - Ωc = {omega_c}, K = {K}')
    plt.xlabel('Valor')
    plt.ylabel('Probabilidade acumulada')
    plt.legend()
    plt.grid()
    plt.savefig(f'graficos/cdf_rice_omega{omega_c}_K{K}.png')
    plt.close()
