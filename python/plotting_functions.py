import numpy as np
from scipy import special


pheno_correction = False

def phenomenological_correction(lambda_v):
    """Calculate the factor for phenomenological corrections. Equal to 1 if pheno_correction set to False."""
    if pheno_correction:
        real_part_correction = lambda x: 1+np.tan( np.pi/2 * x )**2
        skewedness_correction = lambda x: 2**(2*x+3)/np.sqrt(np.pi) * special.gamma( x + 5/2 ) / special.gamma( x + 4 )
        return real_part_correction( lambda_v ) * skewedness_correction( lambda_v )**2
    else:
        return 1

def read_file(file):
    """Reads the file and gives the corresponding amplitudes. Returns the value of the constant variable, value for the varying variable the amplitude table. """
    with open(file, "r") as f:
        lines = [line for line in f.readlines() if not line.startswith('#')]
        constant = float( lines[0] )
        variable = np.array([float(x) for x in lines[2].split(' ')[:-1]])
        amplitudes_table = []
        for l in lines[3:]:
            values = l.split(' ')
            amplitudes_vector = [float(x) for x in values[:-1]]
            amplitudes_table += [amplitudes_vector]
    
    return constant, variable, amplitudes_table

def get_total_cross_section_Q(file_L, file_T, bool_decay_width):
    """
    Calculates the total (differential) cross section at t=0, using the files for longitudinal and transverse production.

    Returns(the following are vectors with the same length):
    Q^2, LO, NLO, LO_rel,NLO_rel, LO_pom, LO_rel_pom
    """
    cs_L = get_cross_section_values_Q(file_L, bool_decay_width, "L")
    cs_T = get_cross_section_values_Q(file_T, bool_decay_width, "T")

    if any(cs_L[0] != cs_T[0]):
        raise Exception("Q vectors different: " + str(cs_L[0]) + "\nand\n" + str(cs_T[0]))

    cs_tot = np.array(cs_L) + np.array(cs_T)
    cs_tot[0] = cs_L[0] # Q^2 vector

    return cs_tot


def get_cross_section_ratio_Q(file_L, file_T, bool_decay_width):
    """
    Calculates the ratio of the differential cross sections at t=0: (dsigma_L/dt)/(dsigma_T/dt), using the files for longitudinal and transverse production.

    Returns(the following are vectors with the same length):
    Q^2, LO, NLO, LO_rel,NLO_rel, LO_pom, LO_rel_pom
    """
    cs_L = get_cross_section_values_Q(file_L, bool_decay_width, "L")
    cs_T = get_cross_section_values_Q(file_T, bool_decay_width, "T")

    if any(cs_L[0] != cs_T[0]):
        raise Exception("Q vectors different: " + str(cs_L[0]) + "\nand\n" + str(cs_T[0]))

    cs_tot = np.array(cs_L) / np.array(cs_T)
    cs_tot[0] = cs_L[0] # Q^2 vector

    return cs_tot


def get_total_cross_section_W(file_L, file_T, bool_decay_width):
    """
    Calculates the total (differential) cross section at t=0, using the files for longitudinal and transverse production.

    Returns(the following are vectors with the same length):
    W, LO, NLO, LO_rel,NLO_rel, LO_pom, LO_rel_pom
    """
    cs_L = get_cross_section_values_W(file_L, bool_decay_width, "L")
    cs_T = get_cross_section_values_W(file_T, bool_decay_width, "T")

    if cs_L[0] != cs_T[0]:
        raise Exception("W vectors different: " + str(cs_L[0]) + "\nand\n" + str(cs_T[0]))

    cs_tot = np.array(cs_L) + np.array(cs_T)
    cs_tot[0] = cs_L[0] # W vector

    return cs_tot


def get_total_cross_section_distribution_Q(file_L, file_T, bool_decay_width):
    """
    Calculates the total (differential) cross section at t=0, using the files for longitudinal and transverse production.
    Samples wave function values and gives the mean/std for various cross sections.
    For consistency, this should be used with bool_decay_width=False.

    Returns(the following are vectors with the same length):
    Q^2, rel_mean, rel_std, rel_pom_mean, rel_pom_std, NLO_rel_mean, NLO_rel_std
    """
    cs_L = get_distribution_Q(file_L, bool_decay_width, "L")
    cs_T = get_distribution_Q(file_T, bool_decay_width, "T")

    if any(cs_L[0] != cs_T[0]):
        raise Exception("Q vectors different: " + str(cs_L[0]) + "\nand\n" + str(cs_T[0]))

    cs_tot = np.zeros( ( 7, len(cs_L[0]) ) )
    cs_tot[0] = cs_L[0] # Q^2 vector
    cs_tot[1] = cs_L[1] + cs_T[1]
    cs_tot[3] = cs_L[3] + cs_T[3]
    cs_tot[5] = cs_L[5] + cs_T[5]
    cs_tot[2] = np.sqrt(cs_L[2]**2 + cs_T[2]**2)
    cs_tot[4] = np.sqrt(cs_L[4]**2 + cs_T[4]**2)
    cs_tot[6] = np.sqrt(cs_L[6]**2 + cs_T[6]**2)

    return cs_tot


def get_total_cross_section_distribution_W(file_L, file_T, bool_decay_width):
    """
    Calculates the total (differential) cross section at t=0, using the files for longitudinal and transverse production.
    Samples wave function values and gives the mean/std for various cross sections.
    For consistency, this should be used with bool_decay_width=False.

    Returns(the following are vectors with the same length):
    W, rel_mean, rel_std, rel_pom_mean, rel_pom_std, NLO_rel_mean, NLO_rel_std
    """
    cs_L = get_distribution_Q(file_L, bool_decay_width, "L")
    cs_T = get_distribution_Q(file_T, bool_decay_width, "T")

    if any(cs_L[0] != cs_T[0]):
        raise Exception("Q vectors different: " + str(cs_L[0]) + "\nand\n" + str(cs_T[0]))

    cs_tot = np.zeros( ( 7, len(cs_L[0]) ) )
    cs_tot[0] = cs_L[0] # W vector
    cs_tot[1] = cs_L[1] + cs_T[1]
    cs_tot[3] = cs_L[3] + cs_T[3]
    cs_tot[5] = cs_L[5] + cs_T[5]
    cs_tot[2] = np.sqrt(cs_L[2]**2 + cs_T[2]**2)
    cs_tot[4] = np.sqrt(cs_L[4]**2 + cs_T[4]**2)
    cs_tot[6] = np.sqrt(cs_L[6]**2 + cs_T[6]**2)

    return cs_tot




def calculate_cross_section_T(Qv, amplitudes_table, bool_decay_width, O_LDME=0.440, q_LDME=0.441):
    """Calculates the cross sections from the production amplitudes. Qv can be a vector or scalar.
    Returns: a dictionary that contains relevant cross sections (in nb)"""

    Nc = 3
    ef = 2/3
    e = np.sqrt(4*np.pi/137)
    Mv = 3.0969
    m = Mv/2
    

    wf_0 = np.sqrt( O_LDME / (2*Nc) ) # phi_RF(0)
    nabla_wf = -q_LDME * wf_0 # nabla phi_RF(0)

    if bool_decay_width:
        Gamma_ee = 5.53e-6
        wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) )  # int dz/(4pi) phi(z,rt=0)
    else:
        wf_LO = 1/np.sqrt(4*m)*(wf_0 + 1/(6*m**2)*nabla_wf * 7/2)  # int dz/(4pi) phi(z,rt=0)

    nonrel_factor = m*e*ef/(np.pi)*2*np.sqrt(Nc/2)*wf_LO

    wf_rel = 1/(6*m**2)/np.sqrt(m) * nabla_wf

    rel_factor = m*e*ef/(np.pi)*2*np.sqrt(Nc/2) * wf_rel

    lambda_v = np.array(amplitudes_table)[:,12]
    amplitudes = np.transpose(nonrel_factor*np.transpose(np.array(amplitudes_table)[:,:12]))
    rel_amplitudes = np.transpose(rel_factor*np.transpose(np.array(amplitudes_table)[:,13:]))

    pheno_factor = phenomenological_correction(lambda_v)
    
    gev_to_nb = 0.389379e6


    LO_prime = amplitudes[:,0]
    LO_pom = amplitudes[:,1]
    LO_0 = amplitudes[:,2]
    LO_BK = amplitudes[:,2] + amplitudes[:,10]
    if bool_decay_width:
        NLO_dip = amplitudes[:,3]+amplitudes[:,5]+amplitudes[:,6]+amplitudes[:,7]
    else:
        NLO_dip = amplitudes[:,4]+amplitudes[:,5]+amplitudes[:,6]+amplitudes[:,7]
    NLO_qqg = amplitudes[:,8]+amplitudes[:,11]
    NLO_BK = amplitudes[:,10]
    NLO = (LO_0 + NLO_BK) + NLO_dip + NLO_qqg
    # NLO2 = LO_prime + NLO_dip + NLO_qqg  #sub scheme
    # NLO3 = (LO_pom + amplitudes[:,9]) + NLO_dip + NLO_qqg # sub scheme with pom (not consistent...)

    rel = rel_amplitudes[:,0] + rel_amplitudes[:,1] + 1/2*rel_amplitudes[:,2]

    
    cs_LO_prime = 1/(16*np.pi)*LO_prime**2                                                  * gev_to_nb * pheno_factor
    cs_LO_pom = 1/(16*np.pi)*LO_pom**2                                                      * gev_to_nb * pheno_factor
    # cs_LO_0 = 1/(16*np.pi)*LO_0**2                                                          * gev_to_nb * pheno_factor
    # cs_NLO_2 = 1/(16*np.pi)*NLO**2                                                          * gev_to_nb * pheno_factor
    cs_NLO = 1/(16*np.pi)*(LO_prime**2+2*LO_prime*(NLO-LO_prime))                           * gev_to_nb * pheno_factor 
    cs_rel = 1/(16*np.pi)*(LO_prime + rel )**2                                              * gev_to_nb * pheno_factor 
    cs_rel_pom = 1/(16*np.pi)*(LO_pom + rel )**2                                            * gev_to_nb * pheno_factor
    cs_NLO_rel = 1/(16*np.pi)*((LO_prime+rel)**2+2*(LO_prime+rel)*(NLO+rel-(LO_prime+rel))) * gev_to_nb * pheno_factor 

    dict_cs = {"LO": cs_LO_prime, "LO_pom": cs_LO_pom, "NLO": cs_NLO, "LO_rel": cs_rel, "NLO_rel": cs_NLO_rel, "LO_rel_pom": cs_rel_pom   }
    return dict_cs

def calculate_cross_section_L(Qv, amplitudes_table, bool_decay_width, O_LDME=0.440, q_LDME=0.441):
    """Calculates the cross sections from the production amplitudes. Qv can be a vector or scalar.
    Returns: a dictionary that contains relevant cross sections (in nb)"""

    Nc = 3
    ef = 2/3
    e = np.sqrt(4*np.pi/137)
    Mv = 3.0969
    m = Mv/2
    

    wf_0 = np.sqrt( O_LDME / (2*Nc) ) # phi_RF(0)
    nabla_wf = -q_LDME * wf_0 # nabla phi_RF(0)

    if bool_decay_width:
        Gamma_ee = 5.53e-6
        wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) )  # int dz/(4pi) phi(z,rt=0)
    else:
        wf_LO = 1/np.sqrt(4*m)*(wf_0 + 1/(6*m**2)*nabla_wf * 5/2)  # int dz/(4pi) phi(z,rt=0)

    nonrel_factor = e*ef*Qv*Nc/(2*np.pi)*2*wf_LO / np.sqrt(2*Nc)

    wf_rel = 1/(6*m**2)/np.sqrt(m) * nabla_wf

    rel_factor = e*ef*Qv*Nc/(2*np.pi)*2/ np.sqrt(2*Nc) * wf_rel

    lambda_v = np.array(amplitudes_table)[:,12]
    amplitudes = np.transpose(nonrel_factor*np.transpose(np.array(amplitudes_table)[:,:12]))
    rel_amplitudes = np.transpose(rel_factor*np.transpose(np.array(amplitudes_table)[:,13:]))

    pheno_factor = phenomenological_correction(lambda_v)
    
    gev_to_nb = 0.389379e6


    LO_prime = amplitudes[:,0]
    LO_pom = amplitudes[:,1]
    LO_0 = amplitudes[:,2]
    LO_BK = amplitudes[:,2] + amplitudes[:,10]
    if bool_decay_width:
        NLO_dip = amplitudes[:,3]+amplitudes[:,5]+amplitudes[:,6]+amplitudes[:,7]
    else:
        NLO_dip = amplitudes[:,4]+amplitudes[:,5]+amplitudes[:,6]+amplitudes[:,7]
    NLO_qqg = amplitudes[:,8]+amplitudes[:,11]
    NLO_BK = amplitudes[:,10]
    NLO = (LO_0 + NLO_BK) + NLO_dip + NLO_qqg
    # NLO2 = LO_prime + NLO_dip + NLO_qqg  #sub scheme
    # NLO3 = (LO_pom + amplitudes[:,9]) + NLO_dip + NLO_qqg # sub scheme with pom (not consistent...)

    rel = rel_amplitudes[:,0] + rel_amplitudes[:,1] 

    
    cs_LO_prime = 1/(16*np.pi)*LO_prime**2                                                  * gev_to_nb * pheno_factor
    cs_LO_pom = 1/(16*np.pi)*LO_pom**2                                                      * gev_to_nb * pheno_factor
    # cs_LO_0 = 1/(16*np.pi)*LO_0**2                                                          * gev_to_nb * pheno_factor
    # cs_NLO_2 = 1/(16*np.pi)*NLO**2                                                          * gev_to_nb * pheno_factor
    cs_NLO = 1/(16*np.pi)*(LO_prime**2+2*LO_prime*(NLO-LO_prime))                           * gev_to_nb * pheno_factor 
    cs_rel = 1/(16*np.pi)*(LO_prime + rel )**2                                              * gev_to_nb * pheno_factor 
    cs_rel_pom = 1/(16*np.pi)*(LO_pom + rel )**2                                            * gev_to_nb * pheno_factor
    cs_NLO_rel = 1/(16*np.pi)*((LO_prime+rel)**2+2*(LO_prime+rel)*(NLO+rel-(LO_prime+rel))) * gev_to_nb * pheno_factor 

    dict_cs = {"LO": cs_LO_prime, "LO_pom": cs_LO_pom, "NLO": cs_NLO, "LO_rel": cs_rel, "NLO_rel": cs_NLO_rel, "LO_rel_pom": cs_rel_pom   }
    return dict_cs

def calculate_cross_section(Qv, amplitudes_table, bool_decay_width, pol, O_LDME=0.440, q_LDME=0.441):
    if pol=='L':
        dict_cs = calculate_cross_section_L(Qv, amplitudes_table, bool_decay_width, O_LDME=O_LDME, q_LDME=q_LDME)
    elif pol=='T':
        dict_cs = calculate_cross_section_T(Qv, amplitudes_table, bool_decay_width, O_LDME=O_LDME, q_LDME=q_LDME)
    else:
        raise Exception("Invalid polarization: " + str(pol))

    return dict_cs

def calculate_rel_error_bands(Qv, amplitudes_table, bool_decay_width, pol):
    """Calculate the distribution of various differential cross sections, in terms of the NRQCD matrix elements."""
    size = 1000
    O_LDME, q_LDME = get_random_LDMEs(size)

    cs_rel_v = []
    cs_rel_pom_v = []
    cs_NLO_rel_v = []
    for i in range(size):
        dict_cs = calculate_cross_section(Qv, amplitudes_table, bool_decay_width, pol, O_LDME=O_LDME[i], q_LDME=q_LDME[i])

        cs_rel_v += [dict_cs["LO_rel"]]
        cs_rel_pom_v += [dict_cs["LO_rel_pom"]]
        cs_NLO_rel_v += [dict_cs["NLO_rel"]]

    dict_rel_error_bands = { 
        "LO_rel_mean": np.mean(np.array(cs_rel_v), axis=0), "LO_rel_std": np.std(np.array(cs_rel_v), axis=0),
        "NLO_rel_mean": np.mean(np.array(cs_NLO_rel_v), axis=0), "NLO_rel_std": np.std(np.array(cs_NLO_rel_v), axis=0),
        "LO_rel_pom_mean": np.mean(np.array(cs_rel_pom_v), axis=0), "LO_rel_pom_std": np.std(np.array(cs_rel_pom_v), axis=0) 
    }

    return dict_rel_error_bands["LO_rel_mean"], dict_rel_error_bands["LO_rel_std"], dict_rel_error_bands["LO_rel_pom_mean"], dict_rel_error_bands["LO_rel_pom_std"], dict_rel_error_bands["NLO_rel_mean"], dict_rel_error_bands["NLO_rel_std"]


def get_random_LDMEs(size):
    """Get the LDME coefficients by sampling from the correlation matrix. Parameters from the J/psi decay width paper."""

    mean = [0.440, 0.441]
    cov = [[3.63e-3, 1.93e-4] ,[1.93e-4, 1.96e-2]]
    O_LDME, q_LDME = np.random.multivariate_normal(mean, cov, size).T
    return O_LDME, q_LDME

def get_distribution_Q(file, bool_decay_width, pol):
    """Calculate the distribution of various differential cross sections, in terms of the NRQCD matrix elements.
    This is the correct implementation, though slower than the other one."""
    W, Qv, amplitudes_table = read_file(file)
        
    Q2v = Qv**2

    rel_mean, rel_std, rel_pom_mean, rel_pom_std, NLO_rel_mean, NLO_rel_std = calculate_rel_error_bands(Qv, amplitudes_table, bool_decay_width, pol)

    return Q2v, rel_mean, rel_std, rel_pom_mean, rel_pom_std, NLO_rel_mean, NLO_rel_std

def get_distribution_W(file, bool_decay_width, pol):
    """Calculate the distribution of various differential cross sections, in terms of the NRQCD matrix elements."""
    Q2, Wv, amplitudes_table = read_file(file)

    Q = np.sqrt(Q2)

    rel_mean, rel_std, rel_pom_mean, rel_pom_std, NLO_rel_mean, NLO_rel_std = calculate_rel_error_bands(Q, amplitudes_table, bool_decay_width, pol)

    return Wv, rel_mean, rel_std, rel_pom_mean, rel_pom_std, NLO_rel_mean, NLO_rel_std


def get_cross_section_values_Q(file, bool_decay_width, pol):
    """Reads off the LO, NLO, rel and NLO+rel values for the section from the file. The bool_decay_width indicates whether one should use decay width or the wave function as the coefficient: True for decay width, False for wave function """

    W, Qv, amplitudes_table = read_file(file)
            
    Q2v = Qv**2
    
    dict_cs = calculate_cross_section(Qv, amplitudes_table, bool_decay_width, pol)

    return Q2v, dict_cs["LO"], dict_cs["NLO"], dict_cs["LO_rel"], dict_cs["NLO_rel"], dict_cs["LO_pom"], dict_cs["LO_rel_pom"]





def get_cross_section_values_W(file, bool_decay_width, pol):
    """Reads off the LO, NLO, rel and NLO+rel values for the section from the file. The bool_decay_width indicates whether one should use decay width or the wave function as the coefficient: True for decay width, False for wave function """
    
    Q2, Wv, amplitudes_table = read_file(file)

    Q = np.sqrt(Q2)

    dict_cs = calculate_cross_section(Q, amplitudes_table, bool_decay_width, pol)

    return Wv, dict_cs["LO"], dict_cs["NLO"], dict_cs["LO_rel"], dict_cs["NLO_rel"], dict_cs["LO_pom"], dict_cs["LO_rel_pom"]


def nabla_phi():
    """Calculates the mean and std for nabla_phi, using the parameters from the J/psi decay width paper."""
    size = 10000
    O_LDME, q_LDME = get_random_LDMEs(size)
    Nc = 3
    wf_0 = np.sqrt( O_LDME / (2*Nc) )
    nabla_wf = -q_LDME * wf_0

    return np.mean(nabla_wf), np.std(nabla_wf)
    
def t_integration_coefficient(Wv):
    W_0 = 90
    b_0 = 4.15
    alpha_pom = 0.116

    return 1 / ( b_0 + 4 * alpha_pom * np.log( Wv/W_0 ) )