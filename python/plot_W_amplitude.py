"""
For plotting amplitudes  as function of W, at fixed Q^2. 
"""
import matplotlib.pyplot as plt
import numpy as np
import os 
import plotting_functions

# plots = [52]
plots = [1,2,5]

# def phenomenological_correction(lambda_v):
#     real_part_correction = lambda x: 1+np.tan( np.pi/2 * x )**2
#     skewedness_correction = lambda x: 2**(2*x+3)/np.sqrt(np.pi) * special.gamma( x + 5/2 ) / special.gamma( x + 4 )
#     # return real_part_correction( lambda_v ) * skewedness_correction( lambda_v )**2
#     return 1


# Order:LO(x_min) 	 LO(x_pom) 	 LO(x_max) 	 qq NLO 1 dim 	 qq NLO J_1 	 qq NLO J_2 	 qq NLO K_0 	 qqg dim 4 no BK 	 qqg dim 4 sub2 BK 	 qqg dim 4 unsub BK 	 qqg dim 6
dir_path = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'


alphas_const = False
if alphas_const:
    # amplitude_file = dir_path + r'production_amplitude_W_as_02_fixed_ver_2.0.dat'
    # amplitude_file = dir_path + r'KCBK_Ybk_4.6_as_0.3_W.dat'
    # amplitude_file = dir_path + r'results-LOBK-as-const-jpsi-T-Q2_0.01_high-W.dat'
    # amplitude_file = dir_path + r'results-LOBK-as-const-jpsi-T-Q2_0.01_minus_cutoff.dat'
    amplitude_file = dir_path + r'results-LOBK-as-const-jpsi-T-Q2_0.01_minus_cutoff_1-x20x21.dat'
else:
    # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-Q2.dat'
    # amplitude_file = dir_path + r'results-kcbk-hera-bal+sd-4.61-jpsi-T-Q2.dat'
    # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-Q2.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-Q2_0.01_high-W.dat'
    # amplitude_file = dir_path + r'results-tbk-lightq-bal+sd-0.00-upsilon-T-Q2_0.01_high-W.dat'
    # amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-upsilon-T-Q2_0.01_high-W.dat'
    amplitude_file = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-Q2_0.01_Y0-4.61.dat'
    # amplitude_file = dir_path + r'results-kcbk-lightq-parent-0.00-upsilon-T-Q2_0.01_high-W.dat'
    # amplitude_file = dir_path + r'results-LOBK-MVe-rcBK.dat'
    # amplitude_file = dir_path + r'results-tbk-hera-bal+sd-4.61.dat'
    # amplitude_file = dir_path + r'results-tbk-hera-bal+sd-4.61_Q2_0.05.dat'
    # amplitude_file = dir_path + r'results-IP_SAT_m1.4-lambda-pom.dat'
    # amplitude_file = dir_path + r'production_amplitude_W_m1.2.dat'
    # amplitude_file = dir_path + r'results-A197-kcbk-lightq-parent-0.00-upsilon-T-Q2_0.01.dat'
    # amplitude_file = dir_path + r'results-A197-resumbk-lightq-parent-0.00-upsilon-T-Q2_0.01.dat'
    # amplitude_file = dir_path + r'results-A197-tbk-lightq-bal+sd-0.00-upsilon-T-Q2_0.01.dat'




# with open(amplitude_file, "r") as f:
#     lines = [line for line in f.readlines() if not line.startswith('#')]
#     Wv = [float(x) for x in lines[2].split(' ')[:-1]]
#     amplitudes_table = []
#     for l in lines[3:]:
#         values = l.split(' ')
#         amplitudes_vector = [float(x) for x in values[:-1]]
#         amplitudes_table += [amplitudes_vector]
Wv, Q2, amplitudes_table = plotting_functions.read_file(amplitude_file)

Q = np.sqrt(Q2)
# Q = np.sqrt(10.0)


Nc = 3
ef = 2/3
Cf = 4/3
e = np.sqrt(4*np.pi/137)
Gamma_ee = 5.53e-6
Mv = 3.0969
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



lambda_v = np.array(amplitudes_table)[:,11]
amplitudes = nonrel_factor*np.array(amplitudes_table)[:,:11]
rel_amplitudes = rel_factor*np.array(amplitudes_table)[:,12:]

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')


if 1 in plots:
    plt.figure(1)
    plt.plot(Wv, amplitudes[:,0], 'k-',label='LO($x\'$)', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,1], 'b-',label='LO($x_p$)', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,2], 'r-',label='LO($x_0$)', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,3], 'k--',label='NLO 1 dim', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,5], 'b--',label='NLO $J_1$', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,6], 'r--',label='NLO $J_2$', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,7], 'c--',label='NLO $K_0$', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,8], 'g:',label='qqg dim 4 no BK', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,9], 'm:',label='qqg unsub BK', linewidth=linewidth)
    plt.plot(Wv, amplitudes[:,10], 'c:',label='qqg dim 6', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'Amplitude [GeV$^{-2}$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([50, 1e3])
    plt.ylim([-1.0, 1.0])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


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

rel = rel_amplitudes[:,0] + rel_amplitudes[:,1] + 1/2*rel_amplitudes[:,2]

if 2 in plots:
    plt.figure(2)
    plt.plot(Wv, NLO, 'k-',label=r'$\textrm{NLO (unsub scheme)}$', linewidth=linewidth)
    # plt.plot(Wv, NLO, 'r-',label=r'$\textrm{NLO} (=\textrm{LO}(x^\prime)+ \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    # plt.plot(Wv, NLO, 'b-',label=r'$\textrm{NLO} (=\textrm{LO}(x_\textrm{P})+ \textrm{NLO}_\textrm{BK,2} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    plt.plot(Wv, LO_prime, 'b--',label=r'$\textrm{LO}(x^\prime$)', linewidth=linewidth)
    plt.plot(Wv, LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
    plt.plot(Wv, LO_0, 'r--',label=r'$\textrm{LO}(x_0)$', linewidth=linewidth)
    # plt.plot(Wv, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
    plt.plot(Wv, NLO_dip, 'b:',label=r'$\textrm{NLO}_\textrm{dip}$', linewidth=linewidth)
    plt.plot(Wv, NLO_qqg, 'r:',label=r'$\textrm{NLO}_{q \bar q g-BK}$', linewidth=linewidth)
    plt.plot(Wv, NLO_BK, 'k:',label=r'$\textrm{NLO}_\textrm{BK}$', linewidth=linewidth)
    plt.legend(prop={'size': 10}, frameon=False)
    if alphas_const:
        plt.title(r'Amplitude at $Q^2 =0 \textrm{GeV}^2$ [GeV$^{-2}$] $(\alpha_s = 0.3)$', fontsize=14)
    else:
        plt.title(r'Amplitude at $Q^2 =0 \textrm{GeV}^2$ [GeV$^{-2}$]', fontsize=14)
    # plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(m_c = 1.2\textrm{GeV})$', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=12)
    # plt.ylabel(r'$\sigma_L+\sigma_T$ [nb]', fontsize=15)
    # plt.xlim([50, 2e2])
    plt.xlim([50, 1e3])
    # plt.ylim([-0.1e1, 1e0])
    plt.ylim([-3e0, 3e0])
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

# gev_to_nb = 0.389379e6

# pheno_factor = plotting_functions.phenomenological_correction(lambda_v)

# cs_LO_prime = 1/(16*np.pi)*LO_prime**2                                                  * gev_to_nb * pheno_factor
# cs_LO_pom = 1/(16*np.pi)*LO_pom**2                                                      * gev_to_nb * pheno_factor
# cs_LO_0 = 1/(16*np.pi)*LO_0**2                                                          * gev_to_nb * pheno_factor
# cs_NLO_2 = 1/(16*np.pi)*NLO**2                                                          * gev_to_nb * pheno_factor
# cs_NLO = 1/(16*np.pi)*(LO_prime**2+2*LO_prime*(NLO-LO_prime))                           * gev_to_nb * pheno_factor 
# cs_rel = 1/(16*np.pi)*(LO_prime + rel )**2                                              * gev_to_nb * pheno_factor 
# cs_rel_pom = 1/(16*np.pi)*(LO_pom + rel )**2                                            * gev_to_nb * pheno_factor
# cs_NLO_rel = 1/(16*np.pi)*((LO_prime+rel)**2+2*(LO_prime+rel)*(NLO+rel-(LO_prime+rel))) * gev_to_nb * pheno_factor 

# dict_cs = plotting_functions.calculate_cross_section(Q, amplitudes_table, reg_scheme)

# cs_LO_prime = dict_cs["LO"]
# cs_LO_pom = dict_cs["LO_pom"]
# cs_NLO = dict_cs["NLO"]
# cs_rel = dict_cs["LO_rel"]
# cs_rel_pom = dict_cs["LO_rel_pom"]
# cs_NLO_rel = dict_cs["NLO_rel"]

# if 3 in plots:
#     plt.figure(3)
#     plt.plot(Wv, cs_NLO, 'k-',label=r'$\textrm{NLO}$', linewidth=linewidth)
#     # plt.plot(Wv, cs_NLO_2, 'k--',label=r'$\textrm{(NLO amplitude)}^2$', linewidth=linewidth)
#     plt.plot(Wv, cs_LO_prime, 'b--',label=r'$\textrm{LO}(x^\prime)$', linewidth=linewidth)
#     # plt.plot(Wv, cs_LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
#     plt.plot(Wv, cs_rel, 'r--',label=r'$\textrm{LO}(x^\prime)$+rel', linewidth=linewidth)
#     # plt.plot(Wv, cs_rel_pom, 'r--',label=r'$\textrm{LO}(x_\textrm{P})$+rel', linewidth=linewidth)
#     plt.plot(Wv, cs_NLO_rel, 'r-',label=r'$\textrm{NLO}$+rel', linewidth=linewidth)
#     plt.legend(prop={'size': 12}, frameon=False)
#     if alphas_const:
#         plt.title(r'$(d\sigma_T/dt)$ at $t = 0$ [nb/GeV$^2$] $(\alpha_s = 0.3)$', fontsize=17)
#     else:
#         plt.title(r'$(d\sigma_T/dt)$ at $t = 0$ [nb/GeV$^2$]', fontsize=17)
#     plt.xlabel(r'$W$ [GeV]', fontsize=15)
#     plt.xlim([50, 1e3])
#     plt.ylim([1, 500])
#     plt.xticks(fontsize=15)
#     plt.yticks(fontsize=15)
#     plt.xscale('log')
#     plt.yscale('log')
#     plt.tight_layout()
#     plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
#     plt.tick_params(axis='x', pad=5)

# if 4 in plots:
#     plt.figure(4)
#     plt.plot(Wv, cs_NLO, 'k-',label=r'NLO', linewidth=linewidth*2)
#     plt.plot(Wv, cs_LO_prime, 'b--',label=r'LO', linewidth=linewidth*2)
#     # plt.plot(Wv, cs_LO_0, 'r--',label=r'$\textrm{LO}(x_0)$', linewidth=linewidth)
#     plt.legend(prop={'size': 20}, frameon=False)
#     plt.title(r'$(d\sigma_T/dt)$ at $t = 0$ [nb/GeV$^2$]', fontsize=30)
#     # plt.title(r'$(d\sigma/dt)$ at $t = 0$ [nb/GeV$^2$] $(m = 1.2\textrm{GeV})$', fontsize=17)
#     plt.xlabel(r'$W$ [GeV]', fontsize=25)
#     # plt.ylabel(r'$\sigma_L+\sigma_T$ [nb]', fontsize=15)
#     # plt.xlim([50, 2e2])
#     plt.xlim([50, 1e3])
#     plt.ylim([0, 100])
#     plt.xticks(fontsize=25)
#     plt.yticks(fontsize=25)
#     plt.xscale('log')
#     # plt.yscale('log')
#     plt.tight_layout()
#     plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
#     plt.tick_params(axis='x', pad=5)


if 5 in plots:
    fig5=plt.figure(5)
    plt.plot(Wv, NLO, 'k-',label=r'NLO', linewidth=1.3*linewidth)
    # plt.plot(Wv, NLO, 'r-',label=r'$\textrm{NLO} (=\textrm{LO}(x^\prime)+ \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    # plt.plot(Wv, NLO, 'b-',label=r'$\textrm{NLO} (=\textrm{LO}(x_\textrm{P})+ \textrm{NLO}_\textrm{BK,2} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    plt.plot(Wv, LO_prime, 'k--',label=r'LO$(Y_\textrm{dip})$', linewidth=1.3*linewidth)
    # plt.plot(Wv, LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
    plt.plot(Wv, LO_0, 'g--',label=r'LO$(Y_0)$', linewidth=linewidth)
    # plt.plot(Wv, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
    plt.plot(Wv, NLO_dip, 'b:',label=r'NLO$_\textrm{dip}$', linewidth=linewidth)
    # plt.plot(Wv, NLO_qqg+NLO_BK, 'r:',label=r'NLO$_{q \bar q g}$', linewidth=linewidth)
    plt.plot(Wv, NLO_qqg, 'r:',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(no BK)', linewidth=linewidth)
    plt.plot(Wv, NLO_BK, 'r-.',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(BK)', linewidth=linewidth)
    # plt.plot(Wv, NLO_qqg+NLO_BK+LO_0-LO_prime, 'g:',label=r'NLO$_{q \bar q g}$+LO$(x_0)$-LO$(x^\prime)$', linewidth=linewidth)
    plt.legend(prop={'size': 15}, frameon=False, ncol=2, loc='upper left', columnspacing=0.5)
    # if alphas_const:
    #     plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(\alpha_s = 0.3)$', fontsize=14)
    # else:
    #     plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] (KCBK 4.61)', fontsize=14)
    # plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(m_c = 1.2\textrm{GeV})$', fontsize=17)
    plt.xlabel(r'$W \textrm{ [GeV]}$', fontsize=20)
    # plt.ylabel(r'$i \mathcal{A}_L(t=0,Q^2=10 \textrm{ GeV}^2)$ ', fontsize=20)
    plt.ylabel(r'$-i \mathcal{A}_T$ [GeV$^{-2}$]', fontsize=20)
    # plt.text(0.5, 0.85, r'$t=0, Q^2 = 10\textrm{ GeV}^2$', transform=fig5.transFigure, fontsize=16)
    plt.text(0.22, 0.59, r'$t=0$', transform=fig5.transFigure, fontsize=18)
    plt.text(0.22, 0.665, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig5.transFigure, fontsize=18)
    # plt.ylabel(r'$\sigma_L+\sigma_T$ [nb]', fontsize=15)
    # plt.xlim([50, 2e2])
    plt.xlim([50, 1e3])
    # plt.xlim([20, 1e3])
    # plt.xlim([20, 3e3])
    # plt.ylim([-0.2, 0.4])
    plt.ylim([-0.6, 1.4])
    # plt.ylim([-0.03, 0.03])
    plt.xticks(fontsize=18)
    # plt.yticks(fontsize=18,ticks=[0,0.05,0.1,0.15,0.2])
    plt.yticks(fontsize=18)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 51 in plots:
    fig5=plt.figure(51)
    plt.plot(Wv, NLO, 'k-',label=r'NLO', linewidth=1.3*linewidth)
    # plt.plot(Wv, NLO, 'r-',label=r'$\textrm{NLO} (=\textrm{LO}(x^\prime)+ \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    # plt.plot(Wv, NLO, 'b-',label=r'$\textrm{NLO} (=\textrm{LO}(x_\textrm{P})+ \textrm{NLO}_\textrm{BK,2} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    plt.plot(Wv, LO_prime, 'k--',label=r'LO$(Y_\textrm{dip})$', linewidth=1.3*linewidth)
    # plt.plot(Wv, LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
    plt.plot(Wv, LO_0, 'g--',label=r'LO$(Y_0)$', linewidth=linewidth)
    # plt.plot(Wv, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
    plt.plot(Wv, NLO_dip, 'b:',label=r'NLO$_\textrm{dip}$', linewidth=linewidth)
    # plt.plot(Wv, NLO_qqg+NLO_BK, 'r:',label=r'NLO$_{q \bar q g}$', linewidth=linewidth)
    plt.plot(Wv, NLO_qqg, 'r:',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(no BK)', linewidth=linewidth)
    plt.plot(Wv, NLO_BK, 'r-.',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(BK)', linewidth=linewidth)
    # plt.plot(Wv, NLO_qqg+NLO_BK+LO_0-LO_prime, 'g:',label=r'NLO$_{q \bar q g}$+LO$(x_0)$-LO$(x^\prime)$', linewidth=linewidth)
    plt.legend(prop={'size': 15}, frameon=False, ncol=2, loc='upper left', columnspacing=0.5)
    # if alphas_const:
    #     plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(\alpha_s = 0.3)$', fontsize=14)
    # else:
    #     plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] (KCBK 4.61)', fontsize=14)
    # plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(m_c = 1.2\textrm{GeV})$', fontsize=17)
    plt.xlabel(r'$W \textrm{ [GeV]}$', fontsize=20)
    # plt.ylabel(r'$i \mathcal{A}_L(t=0,Q^2=10 \textrm{ GeV}^2)$ ', fontsize=20)
    plt.ylabel(r'$-i \mathcal{A}_T$ [GeV$^{-2}$]', fontsize=20)
    # plt.text(0.5, 0.85, r'$t=0, Q^2 = 10\textrm{ GeV}^2$', transform=fig5.transFigure, fontsize=16)
    plt.text(0.22, 0.59, r'$t=0$', transform=fig5.transFigure, fontsize=18)
    plt.text(0.22, 0.665, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig5.transFigure, fontsize=18)
    # plt.ylabel(r'$\sigma_L+\sigma_T$ [nb]', fontsize=15)
    # plt.xlim([50, 2e2])
    # plt.xlim([50, 1e3])
    plt.xlim([30, 1e3])
    # plt.ylim([-0.2, 0.4])
    plt.ylim([-2, 4])
    plt.xticks(fontsize=18)
    # plt.yticks(fontsize=18,ticks=[0,0.05,0.1,0.15,0.2])
    plt.yticks(fontsize=18)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 52 in plots:
    fig52=plt.figure(52)
    # plt.plot(Wv, NLO, 'k-',label=r'NLO', linewidth=1.3*linewidth)
    # # plt.plot(Wv, NLO, 'r-',label=r'$\textrm{NLO} (=\textrm{LO}(x^\prime)+ \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    # # plt.plot(Wv, NLO, 'b-',label=r'$\textrm{NLO} (=\textrm{LO}(x_\textrm{P})+ \textrm{NLO}_\textrm{BK,2} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
    # plt.plot(Wv, LO_prime, 'k--',label=r'LO$(Y_\textrm{dip})$', linewidth=1.3*linewidth)
    # # plt.plot(Wv, LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
    # plt.plot(Wv, LO_0, 'g--',label=r'LO$(Y_0)$', linewidth=linewidth)
    # # plt.plot(Wv, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
    # plt.plot(Wv, NLO_dip, 'b:',label=r'NLO$_\textrm{dip}$', linewidth=linewidth)
    # plt.plot(Wv, NLO_qqg+NLO_BK, 'r:',label=r'NLO$_{q \bar q g}$', linewidth=linewidth)
    # plt.plot(Wv, NLO_qqg, 'r:',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(no BK)', linewidth=linewidth)
    plt.plot(Wv, np.abs(NLO_qqg/NLO_BK), 'r-.',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(no BK)/NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(BK)', linewidth=linewidth)
    # plt.plot(Wv, NLO_qqg+NLO_BK+LO_0-LO_prime, 'g:',label=r'NLO$_{q \bar q g}$+LO$(x_0)$-LO$(x^\prime)$', linewidth=linewidth)
    plt.legend(prop={'size': 15}, frameon=False, ncol=2, loc='lower left', columnspacing=0.5)
    # if alphas_const:
    #     plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(\alpha_s = 0.3)$', fontsize=14)
    # else:
    #     plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] (KCBK 4.61)', fontsize=14)
    # plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(m_c = 1.2\textrm{GeV})$', fontsize=17)
    plt.xlabel(r'$W \textrm{ [GeV]}$', fontsize=20)
    # plt.ylabel(r'$i \mathcal{A}_L(t=0,Q^2=10 \textrm{ GeV}^2)$ ', fontsize=20)
    # plt.ylabel(r'$-i \mathcal{A}_T$ [GeV$^{-2}$]', fontsize=20)
    # plt.text(0.5, 0.85, r'$t=0, Q^2 = 10\textrm{ GeV}^2$', transform=fig5.transFigure, fontsize=16)
    plt.text(0.22, 0.59, r'$t=0$', transform=fig52.transFigure, fontsize=18)
    plt.text(0.22, 0.665, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig52.transFigure, fontsize=18)
    # plt.ylabel(r'$\sigma_L+\sigma_T$ [nb]', fontsize=15)
    # plt.xlim([50, 2e2])
    # plt.xlim([50, 1e3])
    plt.xlim([30, 1e3])
    # plt.ylim([-0.2, 0.4])
    plt.ylim([0, 1])
    plt.xticks(fontsize=18)
    # plt.yticks(fontsize=18,ticks=[0,0.05,0.1,0.15,0.2])
    plt.yticks(fontsize=18)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



# if 6 in plots:
#     fig5=plt.figure(6)
#     plt.plot(Wv, NLO, 'k-',label=r'NLO', linewidth=linewidth)
#     # plt.plot(Wv, NLO, 'r-',label=r'$\textrm{NLO} (=\textrm{LO}(x^\prime)+ \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
#     # plt.plot(Wv, NLO, 'b-',label=r'$\textrm{NLO} (=\textrm{LO}(x_\textrm{P})+ \textrm{NLO}_\textrm{BK,2} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
#     plt.plot(Wv, LO_prime, 'k--',label=r'LO', linewidth=linewidth)
#     # plt.plot(Wv, LO_pom, 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
#     # plt.plot(Wv, LO_0, 'g--',label=r'LO$(Y_0)$', linewidth=linewidth)
#     # plt.plot(Wv, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
#     # plt.plot(Wv, NLO_dip, 'b:',label=r'NLO$_{\textrm{dip}}$', linewidth=linewidth)
#     # plt.plot(Wv, NLO_qqg+NLO_BK, 'r:',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$', linewidth=linewidth)
#     # plt.plot(Wv, NLO_qqg, 'r:',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(no BK)', linewidth=linewidth)
#     # plt.plot(Wv, NLO_BK, 'r-.',label=r'NLO$_{\textrm{q} \overline \textrm{q}\textrm{g}}$(BK)', linewidth=linewidth)
#     # plt.plot(Wv, NLO_qqg+NLO_BK+LO_0-LO_prime, 'g:',label=r'NLO$_{q \bar q g}$+LO$(x_0)$-LO$(x^\prime)$', linewidth=linewidth)
#     # plt.legend(prop={'size': 12}, frameon=False, ncol=2, loc='upper left')
#     plt.legend(prop={'size': 15}, frameon=False, loc='upper left')
#     # if alphas_const:
#     #     plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(\alpha_s = 0.3)$', fontsize=14)
#     # else:
#     #     plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] (KCBK 4.61)', fontsize=14)
#     # plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(m_c = 1.2\textrm{GeV})$', fontsize=17)
#     plt.xlabel(r'$W \textrm{ [GeV]}$', fontsize=20)
#     # plt.ylabel(r'$i \mathcal{A}_L(t=0,Q^2=10 \textrm{ GeV}^2)$ ', fontsize=20)
#     plt.ylabel(r'$i \mathcal{A}_T$ [GeV$^{-2}$]', fontsize=20)
#     # plt.text(0.5, 0.85, r'$t=0, Q^2 = 10\textrm{ GeV}^2$', transform=fig5.transFigure, fontsize=16)
#     plt.text(0.52, 0.27, r'$t=0$', transform=fig5.transFigure, fontsize=16)
#     plt.text(0.66, 0.27, r'$Q^2 = 10\textrm{ GeV}^2$', transform=fig5.transFigure, fontsize=16)
#     # plt.ylabel(r'$\sigma_L+\sigma_T$ [nb]', fontsize=15)
#     # plt.xlim([50, 2e2])
#     plt.xlim([50, 1e3])
#     plt.ylim([0, 0.2])
#     plt.xticks(fontsize=18)
#     # plt.yticks(fontsize=18,ticks=[0,0.05,0.1,0.15,0.2])
#     plt.yticks(fontsize=18)
#     plt.xscale('log')
#     # plt.yscale('log')
#     plt.tight_layout()
#     plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
#     plt.tick_params(axis='x', pad=5)


# if 8 in plots:
#     fig, (ax81, ax82) = plt.subplots(2,1, sharex=True, num=8, figsize=(6,8))
#     ax81.plot(Wv, NLO, 'k-',label=r'NLO', linewidth=linewidth)
#     ax81.plot(Wv, LO_prime, 'k--',label=r'LO$(x^\prime)$', linewidth=linewidth)
#     ax81.plot(Wv, LO_0, 'g--',label=r'LO$(x_0)$', linewidth=linewidth)
#     ax81.plot(Wv, NLO_dip, 'b:',label=r'NLO$_\textrm{dip}$', linewidth=linewidth)
#     ax81.plot(Wv, NLO_qqg+NLO_BK, 'r:',label=r'NLO$_{q \bar q g}$', linewidth=linewidth)
#     ax81.set_ylim([0, 0.2])
#     # ax81.set_yscale('log')
#     ax81.set_ylabel(r'$i\mathcal{A}$', fontsize=20)
#     plt.text(0.4, 0.85, r'$t=0, Q^2 = 10\textrm{ GeV}^2$', transform=ax81.transAxes, fontsize=15)
#     ax81.legend(prop={'size': 12}, frameon=False, handlelength=2.5)

#     ax82.plot(Wv, NLO/LO_prime, 'k-',label=r'NLO', linewidth=linewidth)
#     ax82.plot(Wv, LO_prime/LO_prime, 'k--',label=r'LO$(x^\prime)$', linewidth=linewidth)
#     ax82.plot(Wv, LO_0/LO_prime, 'g--',label=r'LO$(x_0)$', linewidth=linewidth)
#     ax82.plot(Wv, NLO_dip/LO_prime, 'b:',label=r'NLO$_\textrm{dip}$', linewidth=linewidth)
#     ax82.plot(Wv, (NLO_qqg+NLO_BK)/LO_prime, 'r:',label=r'NLO$_{q \bar q g}$', linewidth=linewidth)
#     ax82.set_xlim([50, 1e3])
#     ax82.set_ylim([0, 2])
#     ax82.set_xscale('log')
#     ax82.set_yticks([0.5, 1, 1.5])
#     ax82.set_ylabel(r'$i\mathcal{A}/i\mathcal{A}_\mathrm{LO}(x^\prime)$', fontsize=20)
#     ax82.set_xlabel(r'$W$ [GeV]', fontsize=20)
#     ax81.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=18)
#     ax82.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=18)
#     ax81.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=18)
#     ax82.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=18)
#     # plt.tick_params(axis='x', pad=5)
#     plt.tight_layout(pad=1.0)
#     plt.subplots_adjust(hspace=0)



# if 12 in plots:
#     plt.figure(12)
#     plt.plot(np.log(Wv), np.log(NLO), 'k-',label=r'$\textrm{NLO (unsub scheme)}$', linewidth=linewidth)
#     # plt.plot(Wv, NLO, 'r-',label=r'$\textrm{NLO} (=\textrm{LO}(x^\prime)+ \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
#     # plt.plot(Wv, NLO, 'b-',label=r'$\textrm{NLO} (=\textrm{LO}(x_\textrm{P})+ \textrm{NLO}_\textrm{BK,2} + \textrm{NLO}_\textrm{dip} + \textrm{NLO}_{qqg})$', linewidth=linewidth)
#     plt.plot(np.log(Wv), np.log(LO_prime), 'b--',label=r'$\textrm{LO}(x^\prime$)', linewidth=linewidth)
#     plt.plot(np.log(Wv), np.log(LO_pom), 'g--',label=r'$\textrm{LO}(x_\textrm{P})$', linewidth=linewidth)
#     plt.plot(np.log(Wv), np.log(LO_0), 'r--',label=r'$\textrm{LO}(x_0)$', linewidth=linewidth)
#     # plt.plot(Wv, LO_BK, 'r--',label=r'$\textrm{LO}(x_0)+ L_\textrm{BK}$', linewidth=linewidth)
#     # plt.plot(Wv, NLO_dip, 'b:',label=r'$\textrm{NLO}_\textrm{dip}$', linewidth=linewidth)
#     # plt.plot(Wv, NLO_qqg, 'r:',label=r'$\textrm{NLO}_{q \bar q g-BK}$', linewidth=linewidth)
#     # plt.plot(Wv, NLO_BK, 'k:',label=r'$\textrm{NLO}_\textrm{BK}$', linewidth=linewidth)
#     plt.legend(prop={'size': 10}, frameon=False)
#     if alphas_const:
#         plt.title(r'Log of amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(\alpha_s = 0.3)$', fontsize=14)
#     else:
#         plt.title(r'Log of amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$]', fontsize=14)
#     # plt.title(r'Amplitude at $Q^2 =10 \textrm{GeV}^2$ [GeV$^{-2}$] $(m_c = 1.2\textrm{GeV})$', fontsize=17)
#     plt.xlabel(r'$W$ [GeV]', fontsize=12)
#     # plt.ylabel(r'$\sigma_L+\sigma_T$ [nb]', fontsize=15)
#     # plt.xlim([50, 1e3])
#     # plt.ylim([-0.02e1, 0.4e0])
#     plt.xticks(fontsize=12)
#     plt.yticks(fontsize=12)
#     plt.xscale('log')
#     # plt.yscale('log')
#     plt.tight_layout()
#     plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
#     plt.tick_params(axis='x', pad=5)


plt.show()