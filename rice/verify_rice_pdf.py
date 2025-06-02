import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import rice
from gen_rice_va import gen_rice_va

def verify_rice_pdf(omega_c, K, N=100000):
    samples = gen_rice_va(N, omega_c, K)
    v = np.sqrt((K * omega_c) / (K + 1)) / np.sqrt(omega_c / (2 * (K + 1)))
    scale = np.sqrt(omega_c / (2 * (K + 1)))
    x = np.linspace(0, np.max(samples), 1000)
    pdf_theoretical = rice.pdf(x, v, scale=scale)

    plt.figure()
    plt.hist(samples, bins=100, density=True, alpha=0.6, label='Empírico')
    plt.plot(x, pdf_theoretical, 'r--', label='Teórico')
    plt.title(f'PDF Rice - Ωc = {omega_c}, K = {K}')
    plt.xlabel('Valor')
    plt.ylabel('Densidade de probabilidade')
    plt.legend()
    plt.grid()
    plt.savefig(f'graficos/pdf_rice_omega{omega_c}_K{K}.png')
    plt.close()
