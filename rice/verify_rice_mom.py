import numpy as np
from gen_rice_va import gen_rice_va

def verify_rice_mom(omega_c, K, N=100000):
    samples = gen_rice_va(N, omega_c, K)
    media_empirica = np.mean(samples)
    variancia_empirica = np.var(samples)

    print(f"Ωc = {omega_c}, K = {K}")
    print(f"Média empírica: {media_empirica:.4f}")
    print(f"Variância empírica: {variancia_empirica:.4f}")
    print("-----------------------------------------------------------")
