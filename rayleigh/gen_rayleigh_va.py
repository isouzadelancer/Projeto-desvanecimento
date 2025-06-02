import numpy as np

def gen_rayleigh_va(N, omega_c):
    sigma = np.sqrt(omega_c / 2)
    X = np.random.normal(0, sigma, N)
    Y = np.random.normal(0, sigma, N)
    rayleigh_samples = np.sqrt(X**2 + Y**2)
    return rayleigh_samples
