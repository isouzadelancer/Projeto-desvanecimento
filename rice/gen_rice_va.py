import numpy as np

def gen_rice_va(N, omega_c, K):
    s = np.sqrt((K * omega_c) / (K + 1))
    sigma = np.sqrt(omega_c / (2 * (K + 1)))
    X = np.random.normal(s, sigma, N)
    Y = np.random.normal(0, sigma, N)
    rice_samples = np.sqrt(X**2 + Y**2)
    return rice_samples
