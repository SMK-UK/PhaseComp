from numpy import ndarray, pi, sqrt
from typing import Union

c = 2.99792458E8

def calculate_n(wavelength:ndarray, alphas:list[float], dn_dT:float=0, T:float=20) -> ndarray:
    """
    Calculate the refractive index of a material based on the Sellmeir co-efficient's

    wavelength :
        Wavelength range to determine refractive index (um)
    alphas :
        Sellmeier co-efficients
    dn_dT : float
        change in n with respect to temperature. Default is 0
    T : float
        Temperature at which to calculate n. Default value is room temperature (celsius)
    
    """
    delta_n = delta(dn_dT, T)

    return sqrt(alphas[0]+ alphas[1]/(wavelength**2-alphas[2]) - alphas[3]*wavelength**2) + delta_n

def delta_phi(wavelength:float, L:float, n:float) -> float:
    """
    Evaluate the change in phase of a photon as it propagates through a material
    
    wavelength : float
        Wavelength of the photon
    L : float
        Length of the material
    n : float
        Refractive index of the material 
    """
    return 2*pi*L*n/wavelength

def delta_L(L_0:float, alpha, T:float) -> float:
    """
    Evaluate the change in length of a material with respect to room temperature (20C)

    L_0 : float
        Length at room temperature
    alpha : float
        Co-efficient of thermal expansion
    T : float
        Temperature to determine new length

    """
    return L_0 * delta(alpha, T)

def delta(d:float, T:float) -> float:
    """
    Determine the change of a value based on its difference to room temperature.

    d : float
        Co-efficient of change wrt temperature 
    T : float
        Temperature to evaluate the change at (celsius)

    """
    return (T-20) * d

