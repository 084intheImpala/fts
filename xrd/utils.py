import numpy as np

def lorentzian( x, x0, gam ):
    return gam / np.pi * 1  / ( gam**2 + ( x - x0 )**2)

def gaussian( x, x0, sig ):
    return 1 / np.sqrt(2 * np.pi * sig**2) * np.exp( - ( x - x0 )**2 / (2 * sig**2))

def peak(x, x0, amp, sigma, eta):
    gamma = sigma * np.sqrt(2 * np.log(2))
    return amp * (eta * lorentzian(x, x0, gamma) + (1 - eta) * gaussian(x, x0, sigma))

def sum_peaks(x, x0_a, amp_a, sigma_a, eta_a, x0_b, amp_b, sigma_b, eta_b, noise):
    return peak(x, x0_a, amp_a, sigma_a, eta_a) + peak(x, x0_b, amp_b, sigma_b, eta_b) + noise

def sum_peak(x, x0, amp, sigma, eta, noise):
    return peak(x, x0, amp, sigma, eta) + noise

def fwhm(sigma):
    fg = 2 * sigma * np.sqrt(2 * np.log(2))
    gamma = sigma * np.sqrt(2*np.log(2))
    fl = 2 * gamma
    return (fg**5 + 2.69269 * fg**4 * fl + 2.42843 * fg**3 * fl**2 + 4.47163 * fg**2 * fl**3 + 0.07842 * fg * fl**4 + fl**5)**(0.2)