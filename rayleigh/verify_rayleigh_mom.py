import numpy as np
from gen_rayleigh_va import gen_rayleigh_va

def verify_rayleigh_mom(omega_c, N=100000):
    samples = gen_rayleigh_va(N, omega_c)
    sigma = np.sqrt(omega_c / 2)
    media_teorica = sigma * np.sqrt(np.pi / 2)
    variancia_teorica = (4 - np.pi) / 2 * sigma**2
    media_empirica = np.mean(samples)
    variancia_empirica = np.var(samples)

    print(f"Ωc = {omega_c}")
    print(f"Média teórica: {media_teorica:.4f} / Média empírica: {media_empirica:.4f}")
    print(f"Variância teórica: {variancia_teorica:.4f} / Variância empírica: {variancia_empirica:.4f}")
    print("-----------------------------------------------------------")
