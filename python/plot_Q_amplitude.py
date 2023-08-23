"""
For plotting amplitudes.
"""
import matplotlib.pyplot as plt
import numpy as np
import os 
import plotting_functions


# def phenomenological_correction(lambda_v):
#     real_part_correction = lambda x: 1+np.tan( np.pi/2 * x )**2
#     skewedness_correction = lambda x: 2**(2*x+3)/np.sqrt(np.pi) * special.gamma( x + 5/2 ) / special.gamma( x + 4 )
#     # return real_part_correction( lambda_v ) * skewedness_correction( lambda_v )**2
#     return 1


# Order:LO(x_min) 	 LO(x_pom) 	 LO(x_max) 	 qq NLO 1 dim 	 qq NLO J_1 	 qq NLO J_2 	 qq NLO K_0 	 qqg dim 4 no BK 	 qqg dim 4 sub2 BK 	 qqg dim 4 unsub BK 	 qqg dim 6
dir_path = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'

particle = 'jpsi'
# particle = 'upsilon' 

if particle == 'jpsi':
    Mv = 3.0969

    amplitude_file = dir_path + r'results-LOBK-as-const_invariant_mass_rapidity-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'


    # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat'
    # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'
    # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat'
    # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'


    # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff-x20x21.dat'
    # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff-x20x21.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-parent-0.00-jpsi-T-W_90.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90_minus_cutoff-x20x21.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff_1-x20x21-tbkscheme.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-parent-0.00-proj-rapidity-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'
    # amplitude_file = dir_path + r'results-A197-kcbk-hera-bal+sd-4.61-Q.dat'
    # amplitude_file = dir_path + r'results-kcbk-hera-bal+sd-0.00-Q.dat'
    # amplitude_file = dir_path + r'results-kcbk-hera-bal+sd-4.61-jpsi-T-W_90.dat'
    # amplitude_file = dir_path + r'results-IP_SAT_m1.4-Q.dat'
    # amplitude_file = dir_path + r'results-LOBK-MVe-Q.dat'
    # amplitude_file = dir_path + r'production_amplitude_W_m1.2.dat'
    # amplitude_file = dir_path + r'results-A197-tbk-lightq-bal+sd-0.00-upsilon-T-W_90.dat'
    # amplitude_file = dir_path + r'results-A197-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat'
    # amplitude_file = dir_path + r'results-A197-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat'
elif particle == 'upsilon':
    Mv = 9.46

    # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-upsilon-T-W_90.dat'
    amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-upsilon-T-W_90_minus_cutoff_1-x20x21.dat'
    # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-upsilon-T-W_90.dat'
    # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-upsilon-T-W_90_minus_cutoff_1-x20x21.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-upsilon-T-W_90.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-upsilon-T-W_90_minus_cutoff_1-x20x21.dat'
else:
    print('Invalid particle')


# alphas_const = False
# if alphas_const:
#     amplitude_file = dir_path + r'production_amplitude_Q_as_02.dat'
# else:
#     # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat'
#     # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff-x20x21.dat'
#     # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'
#     amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-upsilon-T-W_90.dat'
#     # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-upsilon-T-W_90_minus_cutoff_1-x20x21.dat'
#     # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat'
#     # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff-x20x21.dat'
#     # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-upsilon-T-W_90.dat'
#     # amplitude_file = dir_path + r'results-tbk-lightq-parent-0.00-upsilon-T-W_90.dat'
#     # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90_minus_cutoff-x20x21.dat'
#     # amplitude_file = dir_path + r'results-tbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'
#     # amplitude_file = dir_path + r'results-tbk-lightq-parent-0.00-jpsi-T-W_90_minus_cutoff_1-x20x21-tbkscheme.dat'
#     # amplitude_file = dir_path + r'results-tbk-lightq-parent-0.00-proj-rapidity-jpsi-T-W_90_minus_cutoff_1-x20x21.dat'
#     # amplitude_file = dir_path + r'results-A197-kcbk-hera-bal+sd-4.61-Q.dat'
#     # amplitude_file = dir_path + r'results-kcbk-hera-bal+sd-0.00-Q.dat'
#     # amplitude_file = dir_path + r'results-kcbk-hera-bal+sd-4.61-jpsi-T-W_90.dat'
#     # amplitude_file = dir_path + r'results-IP_SAT_m1.4-Q.dat'
#     # amplitude_file = dir_path + r'results-LOBK-MVe-Q.dat'
#     # amplitude_file = dir_path + r'production_amplitude_W_m1.2.dat'
#     # amplitude_file = dir_path + r'results-A197-tbk-lightq-bal+sd-0.00-upsilon-T-W_90.dat'
#     # amplitude_file = dir_path + r'results-A197-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat'
#     # amplitude_file = dir_path + r'results-A197-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat'



# with open(amplitude_file, "r") as f:
#     lines = [line for line in f.readlines() if not line.startswith('#')]
#     Qv = np.array([float(x) for x in lines[2].split(' ')[:-1]])
#     amplitudes_table = []
#     for l in lines[3:]:
#         values = l.split(' ')
#         amplitudes_vector = [float(x) for x in values[:-1]]
#         amplitudes_table += [amplitudes_vector]
Wv, Q2, amplitudes_table = plotting_functions.read_file(amplitude_file)

Qv = np.sqrt(Q2)

Nc = 3
ef = 2/3
Cf = 4/3
e = np.sqrt(4*np.pi/137)
Gamma_ee = 5.53e-6
m = Mv/2
alpha_s = 0.25
O_LDME = 0.440
q_LDME = 0.441
wf_0 = np.sqrt( O_LDME / (2*Nc) )

nabla_wf = -q_LDME * wf_0

reg_scheme = 'NR wave function'

if reg_scheme == 'decay width':
    wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) )  # int dz/(4pi) phi(z,rt=0)
elif reg_scheme == 'NR wave function':
    wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) ) * ( 1 + 2*alpha_s*Cf/np.pi ) # int dz/(4pi) phi(z,rt=0)
elif reg_scheme == 'rel wave function':
    wf_LO = 1/np.sqrt(4*m)*(wf_0 + 1/(6*m**2)*nabla_wf * 7/2)  # int dz/(4pi) phi(z,rt=0)
else:
    raise Exception('Invalid scheme')
# wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) )
nonrel_factor = e*ef*m*Nc/(np.pi)*2*wf_LO / np.sqrt(2*Nc)


wf_rel = 1/(6*m**2)/np.sqrt(m) * nabla_wf

rel_factor = e*ef*m*Nc/(np.pi)*2/ np.sqrt(2*Nc) * wf_rel


# Nc = 3
# ef = 2/3
# e = np.sqrt(4*np.pi/137)
# Mv = 3.0969
# Gamma_ee = 5.53e-6
# alpha_s = 0.2
# # m_c = 1.4
# # m_c = Mv/2
# wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) )
# # wf_NLO_factor = (1+2/np.pi*4/3*alpha_s)
# factor = e*ef*Nc/(2*np.pi)*2*wf_LO*Qv / np.sqrt(2*Nc)


# lambda_v = np.array(amplitudes_table)[:,12]
# amplitudes = np.transpose(nonrel_factor*np.transpose(np.array(amplitudes_table)[:,:12]))
# rel_amplitudes = np.transpose(rel_factor*np.transpose(np.array(amplitudes_table)[:,13:]))



lambda_v = np.array(amplitudes_table)[:,11]
amplitudes = nonrel_factor*np.array(amplitudes_table)[:,:11]
rel_amplitudes = rel_factor*np.array(amplitudes_table)[:,12:]


linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plots = [2,21]

if 1 in plots:
    plt.figure(1)
    plt.plot(Qv**2, amplitudes[:,0], 'k-',label='LO($x\'$)', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,1], 'b-',label='LO($x_p$)', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,2], 'r-',label='LO($x_0$)', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,3], 'k--',label='NLO 1 dim', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,5], 'b--',label='NLO $J_1$', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,6], 'r--',label='NLO $J_2$', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,7], 'c--',label='NLO $K_0$', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,8], 'g--',label='qqg dim 4 no BK', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,9], 'y--',label='qqg sub2 BK', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,10], 'm--',label='qqg unsub BK', linewidth=linewidth)
    plt.plot(Qv**2, amplitudes[:,11], 'c--',label='qqg dim 6', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'Amplitude [GeV$^{-2}$]', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0.01, 1e2])
    plt.ylim([-0.15, 0.2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    # plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

# LO_prime = amplitudes[:,0]
# LO_pom = amplitudes[:,1]
# LO_0 = amplitudes[:,2]
# LO_BK = amplitudes[:,2] + amplitudes[:,9]
# if reg_scheme == 'decay width':
#     NLO_dip = amplitudes[:,3]+amplitudes[:,5]+amplitudes[:,6]+amplitudes[:,7]
# else:
#     NLO_dip = amplitudes[:,4]+amplitudes[:,5]+amplitudes[:,6]+amplitudes[:,7]
# NLO_qqg = amplitudes[:,8]+amplitudes[:,11]
# NLO_BK = amplitudes[:,10]
# NLO = LO_0 + NLO_BK + NLO_dip + NLO_qqg
# NLO2 = LO_prime + NLO_dip + NLO_qqg
# NLO3 = LO_pom + amplitudes[:,9] + NLO_dip + NLO_qqg

# rel = rel_amplitudes[:,0] + rel_amplitudes[:,1] + 1/2*rel_amplitudes[:,2]



LO_prime = amplitudes[:,0]
LO_pom = amplitudes[:,1]
LO_0 = amplitudes[:,2]
LO_BK = amplitudes[:,2] + amplitudes[:,9]
if reg_scheme == 'decay width':
    NLO_dip = amplitudes[:,3]+amplitudes[:,5]+amplitudes[:,6]+amplitudes[:,7]
else:
    NLO_dip = amplitudes[:,4]+amplitudes[:,5]+amplitudes[:,6]+amplitudes[:,7]
NLO_qqg = amplitudes[:,8]+amplitudes[:,10]
NLO_BK = amplitudes[:,9]
NLO = (LO_0 + NLO_BK) + NLO_dip + NLO_qqg
NLO2 = LO_prime + NLO_dip + NLO_qqg
# NLO3 = (LO_pom + amplitudes[:,9]) + NLO_dip + NLO_qqg


if 2 in plots:
    plt.figure(2)
    plt.plot(Qv**2, NLO, 'k-',label=r'$\textrm{NLO} (=\textrm{LO}(x_0)+ \textrm{NLO}_\textrm{BK} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    plt.plot(Qv**2, LO_prime, 'b--',label=r'$\textrm{LO}(x^\prime$)', linewidth=linewidth)
    plt.plot(Qv**2, LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
    plt.plot(Qv**2, LO_0, 'r--',label=r'$\textrm{LO}(x_0)$', linewidth=linewidth)
    # plt.plot(Qv**2+Mv**2Wv, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
    plt.plot(Qv**2, NLO_dip, 'b:',label=r'$\textrm{NLO}_\textrm{dip}$', linewidth=linewidth)
    plt.plot(Qv**2, NLO_qqg, 'r:',label=r'$\textrm{NLO}_{qqg}$', linewidth=linewidth)
    plt.plot(Qv**2, NLO_BK, 'k:',label=r'$\textrm{NLO}_\textrm{BK}$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'Amplitude at $W =90 \textrm{GeV}$ [GeV$^{-2}$]', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0.01, 1e2])
    plt.ylim([-0.15, 0.2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    # plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)




if 21 in plots:
    plt.figure(21)
    plt.plot(Mv**2 + Qv**2, np.abs(NLO), 'k-',label=r'$\textrm{NLO} (=\textrm{LO}(x_0)+ \textrm{NLO}_\textrm{BK} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    plt.plot(Mv**2 + Qv**2, np.abs(LO_prime), 'b--',label=r'$\textrm{LO}(x^\prime$)', linewidth=linewidth)
    plt.plot(Mv**2 + Qv**2, np.abs(LO_pom), 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
    plt.plot(Mv**2 + Qv**2, np.abs(LO_0), 'r--',label=r'$\textrm{LO}(x_0)$', linewidth=linewidth)
    # plt.plot(Mv**2 + Qv**2, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
    plt.plot(Mv**2 + Qv**2, np.abs(NLO_dip), 'b:',label=r'$\textrm{NLO}_\textrm{dip}$', linewidth=linewidth)
    plt.plot(Mv**2 + Qv**2, np.abs(NLO_qqg), 'r:',label=r'$\textrm{NLO}_{qqg}$', linewidth=linewidth)
    plt.plot(Mv**2 + Qv**2, np.abs(NLO_BK), 'k:',label=r'$\textrm{NLO}_\textrm{BK}$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'Amplitude at $W =90 \textrm{GeV}$ [GeV$^{-2}$]', fontsize=17)
    plt.xlabel(r'$M_V^2+ Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv**2, Mv**2 + 1e2])
    plt.ylim([1e-4, 1e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

gev_to_nb = 0.389379e6


# real_part_correction = lambda x: 1+np.tan( np.pi/2 * x )**2
# skewedness_correction = lambda x: 2**(2*x+3)/np.sqrt(np.pi) * special.gamma( x + 5/2 ) / special.gamma( x + 4 )
# pheno_factor = real_part_correction( lambda_v ) * skewedness_correction( lambda_v )**2
# pheno_factor = plotting_functions.phenomenological_correction(lambda_v)

# cs_LO_prime = 1/(16*np.pi)*LO_prime**2                                                  * gev_to_nb * pheno_factor
# cs_LO_pom = 1/(16*np.pi)*LO_pom**2                                                      * gev_to_nb * pheno_factor
# cs_LO_0 = 1/(16*np.pi)*LO_0**2                                                          * gev_to_nb * pheno_factor
# cs_NLO_2 = 1/(16*np.pi)*NLO**2                                                          * gev_to_nb * pheno_factor
# cs_NLO_3 = 1/(16*np.pi)*(LO_BK**2+2*LO_BK*(NLO-LO_BK))                                  * gev_to_nb * pheno_factor
# cs_NLO = 1/(16*np.pi)*(LO_prime**2+2*LO_prime*(NLO-LO_prime))                           * gev_to_nb * pheno_factor 
# cs_rel = 1/(16*np.pi)*(LO_prime + rel )**2                                              * gev_to_nb * pheno_factor 
# cs_rel_pom = 1/(16*np.pi)*(LO_pom + rel )**2                                            * gev_to_nb * pheno_factor
# cs_NLO_rel = 1/(16*np.pi)*((LO_prime+rel)**2+2*(LO_prime+rel)*(NLO+rel-(LO_prime+rel))) * gev_to_nb * pheno_factor 

# dict_cs = plotting_functions.calculate_cross_section(Qv, amplitudes_table, reg_scheme)

# cs_LO_prime = dict_cs["LO"]
# cs_LO_pom = dict_cs["LO_pom"]
# cs_NLO = dict_cs["NLO"]
# cs_rel = dict_cs["LO_rel"]
# cs_rel_pom = dict_cs["LO_rel_pom"]
# cs_NLO_rel = dict_cs["NLO_rel"]


if 3 in plots:
    plt.figure(3)
    plt.plot(Qv**2, cs_NLO, 'k-',label=r'$\textrm{NLO}$', linewidth=linewidth)
    # plt.plot(Qv**2, cs_NLO_2, 'k--',label=r'$\textrm{(NLO amplitude)}^2$', linewidth=linewidth)
    # plt.plot(Qv**2, cs_NLO_3, 'k:',label=r'NLO, LO=LO($x_0$)+LO BK', linewidth=linewidth)
    plt.plot(Qv**2, cs_LO_prime, 'b--',label=r'$\textrm{LO}(x^\prime$)', linewidth=linewidth)
    # plt.plot(Qv**2, cs_LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
    plt.plot(Qv**2, cs_rel, 'r--',label=r'$\textrm{LO}(x^\prime)$+rel', linewidth=linewidth)
    # plt.plot(Qv**2, cs_rel_pom, 'r--',label=r'$\textrm{LO}(x_\textrm{P})$+rel', linewidth=linewidth)
    plt.plot(Qv**2, cs_NLO_rel, 'r-',label=r'$\textrm{NLO}$+rel', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma/dt)$ at $t = 0$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0.01, 1e2])
    # plt.xlim([1, 1e2])
    plt.ylim([1e-1, 1000])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 5 in plots:
    fig5=plt.figure(5)
    plt.plot(Qv**2, NLO, 'k-',label=r'NLO', linewidth=1.3*linewidth)
    # plt.plot(Wv, NLO, 'r-',label=r'$\textrm{NLO} (=\textrm{LO}(x^\prime)+ \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    # plt.plot(Wv, NLO, 'b-',label=r'$\textrm{NLO} (=\textrm{LO}(x_\textrm{P})+ \textrm{NLO}_\textrm{BK,2} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    plt.plot(Qv**2, LO_prime, 'k--',label=r'LO$(Y_\textrm{dip})$', linewidth=1.3*linewidth)
    # plt.plot(Wv, LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
    plt.plot(Qv**2, LO_0, 'g--',label=r'LO$(Y_0)$', linewidth=linewidth)
    # plt.plot(Wv, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
    plt.plot(Qv**2, NLO_dip, 'b:',label=r'NLO$_\textrm{dip}$', linewidth=linewidth)
    # plt.plot(Qv**2, NLO_qqg+NLO_BK, 'r:',label=r'NLO$_{q \bar q g}$', linewidth=linewidth)
    plt.plot(Qv**2, NLO_qqg, 'r:',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(no BK)', linewidth=linewidth)
    plt.plot(Qv**2, NLO_BK, 'r-.',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(BK)', linewidth=linewidth)
    # plt.plot(Qv**2, NLO_qqg+NLO_BK+LO_0-LO_prime, 'g:',label=r'NLO$_{q \bar q g}$+LO$(x_0)$-LO$(x^\prime)$', linewidth=linewidth)
    plt.legend(prop={'size': 15}, frameon=False, loc='upper right', ncol=2, columnspacing=0.5)
    # plt.title(r'Amplitude at $W =90$GeV [GeV$^{-2}$] (KCBK 4.61)', fontsize=14)
    # plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(m_c = 1.2\textrm{GeV})$', fontsize=17)
    plt.xlabel(r'$Q^2 \textrm{ [GeV}^2]$', fontsize=20)
    # plt.ylabel(r'$i \mathcal{A}_L(t=0,W=90 \textrm{ GeV})$ ', fontsize=20)
    plt.ylabel(r'$-i \mathcal{A}_T$ [GeV$^{-2}$]', fontsize=20)
    plt.text(0.69, 0.58, r'$t=0$', transform=fig5.transFigure, fontsize=18)
    plt.text(0.69, 0.66, r'$W = 90\textrm{ GeV}$', transform=fig5.transFigure, fontsize=18)
    # plt.ylabel(r'$\sigma_L+\sigma_T$ [nb]', fontsize=15)
    # plt.xlim([50, 2e2])
    plt.xlim([0.1,100])
    plt.ylim([-0.4, 0.9])
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18, ticks=[-0.4,-0.2,0,0.2,0.4, 0.6, 0.8])
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 8 in plots:
    # plt.figure(num=8, figsize=(6,8))
    fig, (ax81, ax82) = plt.subplots(2,1, sharex=True, num=8, figsize=(6,8))
    ax81.plot(Qv**2, NLO, 'k-',label=r'NLO', linewidth=linewidth)
    ax81.plot(Qv**2, LO_prime, 'k--',label=r'LO$(x^\prime)$', linewidth=linewidth)
    ax81.plot(Qv**2, LO_0, 'g--',label=r'LO$(x_0)$', linewidth=linewidth)
    ax81.plot(Qv**2, NLO_dip, 'b:',label=r'NLO$_\textrm{dip}$', linewidth=linewidth)
    # ax81.plot(Qv**2, NLO_qqg+NLO_BK, 'r:',label=r'NLO$_{q \bar q g}$', linewidth=linewidth)
    ax81.plot(Qv**2, NLO_qqg, 'r:',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(no BK)', linewidth=linewidth)
    ax81.plot(Qv**2, NLO_BK, 'r-.',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(BK)', linewidth=linewidth)
    # ax81.set_ylim([0, 0.12])
    ax81.set_ylim([-0.1, 0.2])
    plt.text(0.05, 0.9, r'$t=0, W = 90\mathrm{ GeV}$', transform=ax81.transAxes, fontsize=18)
    # ax81.set_yscale('log')
    ax81.set_ylabel(r'$-i\mathcal{A}$', fontsize=20)
    ax81.legend(prop={'size': 12}, frameon=False)

    ax82.plot(Qv**2, NLO/LO_prime, 'k-',label=r'NLO', linewidth=linewidth)
    ax82.plot(Qv**2, LO_prime/LO_prime, 'k--',label=r'LO$(x^\prime)$', linewidth=linewidth)
    ax82.plot(Qv**2, LO_0/LO_prime, 'g--',label=r'LO$(x_0)$', linewidth=linewidth)
    ax82.plot(Qv**2, NLO_dip/LO_prime, 'b:',label=r'NLO$_\textrm{dip}$', linewidth=linewidth)
    # ax82.plot(Qv**2, (NLO_qqg+NLO_BK)/LO_prime, 'r:',label=r'NLO$_{q \bar q g}$', linewidth=linewidth)
    ax82.plot(Qv**2, NLO_qqg/LO_prime, 'r:',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(no BK)', linewidth=linewidth)
    ax82.plot(Qv**2, NLO_BK/LO_prime, 'r-.',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(BK)', linewidth=linewidth)
    ax82.set_xlim([0.1, 100])
    # ax82.set_ylim([0, 2.5])
    ax82.set_ylim([-2, 4])
    ax82.set_xscale('log')
    ax82.set_yticks([ 0.5, 1.0, 1.5, 2.0])
    ax82.set_ylabel(r'$-i\mathcal{A}/i\mathcal{A}_\mathrm{LO}(x^\prime)$', fontsize=20)
    ax82.set_xlabel(r'$Q^2$ [GeV$^2$]', fontsize=20)
    ax81.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=18)
    ax82.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=18)
    ax81.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=18)
    ax82.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=18)
    # plt.tick_params(axis='x', pad=5)
    plt.tight_layout(pad=1.0)
    plt.subplots_adjust(hspace=0)



plt.show()