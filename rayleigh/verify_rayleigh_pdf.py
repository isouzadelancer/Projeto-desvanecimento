import numpy as np
import matplotlib.pyplot as plt
from gen_rayleigh_va import gen_rayleigh_va

def verify_rayleigh_pdf(omega_c, N=100000):
    samples = gen_rayleigh_va(N, omega_c)
    sigma = np.sqrt(omega_c / 2)
    x = np.linspace(0, np.max(samples), 1000)
    pdf_theoretical = (x / (sigma**2)) * np.exp(-x**2 / (2 * sigma**2))

    plt.figure()
    plt.hist(samples, bins=100, density=True, alpha=0.6, label='Empírico')
    plt.plot(x, pdf_theoretical, 'r--', label='Teórico')
    plt.title(f'PDF Rayleigh - Ωc = {omega_c}')
    plt.xlabel('Valor')
    plt.ylabel('Densidade de probabilidade')
    plt.legend()
    plt.grid()
    plt.savefig(f'graficos/pdf_rayleigh_omega{omega_c}.png')
    plt.close()
