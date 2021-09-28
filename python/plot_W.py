
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
import os 

import plotting_functions
import experimental_data


plotting_functions.pheno_correction = False


bool_decay_width = True
bool_decay_width_rel = False
id_string = "_Q2_0.05" # Q^2 = 0.05 GeV^2, thus there is no need for L
# id_string = "_Q2_0.05-m_1.4" # Q^2 = 0.05 GeV^2, thus there is no need for L

dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_L/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'

# cs_kcbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-kcbk-hera-bal+sd-0.00.dat', bool_decay_width, "L" )
# cs_kcbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-kcbk-hera-bal+sd-4.61.dat', bool_decay_width, "L" )
# cs_tbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-tbk-hera-bal+sd-0.00.dat', bool_decay_width, "L"  )
# cs_tbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-tbk-hera-bal+sd-4.61.dat', bool_decay_width, "L"  )
# cs_resumbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-resumbk-hera-bal+sd-0.00.dat', bool_decay_width, "L"  )
# cs_resumbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-resumbk-hera-bal+sd-4.61.dat', bool_decay_width, "L"  )

# # cs_ipsat_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-IP_SAT_m1.4.dat', bool_decay_width )
# cs_lobk_mve_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-LOBK-MVe.dat', bool_decay_width, "L"  )

# cs_lobk_mve_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-LOBK-MVe.dat', bool_decay_width_rel, "L"  )
# cs_kcbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-kcbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "L"  )
# cs_tbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-tbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "L"  )
# cs_resumbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-resumbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "L"  )
# cs_kcbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-kcbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "L"  )
# cs_tbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-tbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "L"  )
# cs_resumbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-resumbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "L"  )

cs_kcbk_000_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-kcbk-hera-bal+sd-0.00' + id_string + '.dat', bool_decay_width, "T" )
cs_kcbk_461_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-kcbk-hera-bal+sd-4.61' + id_string + '.dat', bool_decay_width, "T" )
cs_tbk_000_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-tbk-hera-bal+sd-0.00' + id_string + '.dat', bool_decay_width, "T" )
cs_tbk_461_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-tbk-hera-bal+sd-4.61' + id_string + '.dat', bool_decay_width, "T" )
cs_resumbk_000_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-resumbk-hera-bal+sd-0.00' + id_string + '.dat', bool_decay_width, "T" )
cs_resumbk_461_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-resumbk-hera-bal+sd-4.61' + id_string + '.dat', bool_decay_width, "T" )

# cs_ipsat_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-IP_SAT_m1.4.dat', bool_decay_width )
cs_lobk_mve_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-LOBK-MVe' + id_string + '.dat', bool_decay_width, "T" )

cs_lobk_mve_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-LOBK-MVe' + id_string + '.dat', bool_decay_width_rel, "T" )
cs_kcbk_461_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-kcbk-hera-bal+sd-4.61' + id_string + '.dat', bool_decay_width_rel, "T" )
cs_kcbk_000_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-kcbk-hera-bal+sd-0.00' + id_string + '.dat', bool_decay_width_rel, "T" )
cs_tbk_461_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-tbk-hera-bal+sd-4.61' + id_string + '.dat', bool_decay_width_rel, "T" )
cs_tbk_000_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-tbk-hera-bal+sd-0.00' + id_string + '.dat', bool_decay_width_rel, "T" )
cs_resumbk_461_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-resumbk-hera-bal+sd-4.61' + id_string + '.dat', bool_decay_width_rel, "T" )
cs_resumbk_000_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-resumbk-hera-bal+sd-0.00' + id_string + '.dat', bool_decay_width_rel, "T" )


Cf = 4/3
alpha_s0 = 0.25
NRQCD_factor = (1-2*Cf*alpha_s0/np.pi)**2

# cs_kcbk_000 = cs_kcbk_000_L + cs_kcbk_000_T
# cs_kcbk_461 = cs_kcbk_461_L + cs_kcbk_461_T
# cs_tbk_000 = cs_tbk_000_L + cs_tbk_000_T
# cs_tbk_461 = cs_tbk_461_L + cs_tbk_461_T
# cs_resumbk_000 = cs_resumbk_000_L + cs_resumbk_000_T
# cs_resumbk_461 = cs_resumbk_461_L + cs_resumbk_461_T
# cs_lobk_mve = cs_lobk_mve_L + cs_lobk_mve_T

# cs_kcbk_000_rel = cs_kcbk_000_rel_L + cs_kcbk_000_rel_T
# cs_kcbk_461_rel = cs_kcbk_461_rel_L + cs_kcbk_461_rel_T
# cs_tbk_000_rel = cs_tbk_000_rel_L + cs_tbk_000_rel_T
# cs_tbk_461_rel = cs_tbk_461_rel_L + cs_tbk_461_rel_T
# cs_resumbk_000_rel = cs_resumbk_000_rel_L + cs_resumbk_000_rel_T
# cs_resumbk_461_rel = cs_resumbk_461_rel_L + cs_resumbk_461_rel_T
# cs_lobk_mve_rel = cs_lobk_mve_rel_L + cs_lobk_mve_rel_T

sigma_tot_ZEUS_W, sigma_tot_ZEUS_data = experimental_data.sigma_tot_W_ZEUS()
sigma_tot_H1_v1_W, sigma_tot_H1_v1_data, _     = experimental_data.sigma_tot_W_H1_v1()
sigma_tot_H1_v2_W, sigma_tot_H1_v2_data     = experimental_data.sigma_tot_W_H1_v2()
sigma_tot_ALICE_v1_W, sigma_tot_ALICE_v1_data     = experimental_data.sigma_tot_W_ALICE_v1()
sigma_tot_ALICE_v2_W, sigma_tot_ALICE_v2_data     = experimental_data.sigma_tot_W_ALICE_v2()
sigma_tot_ALICE_v3_W, sigma_tot_ALICE_v3_data     = experimental_data.sigma_tot_W_ALICE_v3()

W = cs_kcbk_000_T[0]
C_int = plotting_functions.t_integration_coefficient(W)

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plots = [1,2,3,4,5,6]

if 1 in plots:
    plt.figure(1)
    plt.plot(cs_kcbk_000_T[0], cs_kcbk_000_T[2], '-',color='tab:green',label=r'NLO KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_kcbk_461_T[0], cs_kcbk_461_T[2], '--',color='tab:green',label=r'NLO KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_000_T[0], cs_tbk_000_T[2], 'r-',label=r'NLO TBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_461_T[0], cs_tbk_461_T[2], 'r--',label=r'NLO TBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_000_T[0], cs_resumbk_000_T[2], 'b-',label=r'NLO ResumBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_461_T[0], cs_resumbk_461_T[2], 'b--',label=r'NLO ResumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0], cs_lobk_mve_T[5], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([3e1, 4e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 2 in plots:
    plt.figure(2)
    plt.plot(cs_kcbk_000_T[0], cs_kcbk_000_rel_T[5], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_kcbk_461_T[0], cs_kcbk_461_rel_T[5], '--',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_000_T[0], cs_tbk_000_rel_T[5], 'r-',label=r'NLO+rel TBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_461_T[0], cs_tbk_461_rel_T[5], 'r--',label=r'NLO+rel TBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_000_T[0], cs_resumbk_000_rel_T[5], 'b-',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_461_T[0], cs_resumbk_461_rel_T[5], 'b--',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0], cs_lobk_mve_rel_T[3] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([3e1, 4e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 3 in plots:
    plt.figure(3)
    plt.plot(cs_kcbk_000_T[0],    C_int * cs_kcbk_000_T[2], '-',color='tab:green',label=r'NLO KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_T[2], '--',color='tab:green',label=r'NLO KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_000_T[0],     C_int * cs_tbk_000_T[2], 'r-',label=r'NLO TBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_461_T[0],     C_int * cs_tbk_461_T[2], 'r--',label=r'NLO TBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_000_T[0], C_int * cs_resumbk_000_T[2], 'b-',label=r'NLO ResumBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_461_T[0], C_int * cs_resumbk_461_T[2], 'b--',label=r'NLO ResumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[5], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.legend(prop={'size': 10}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([2e1, 1e3])
    plt.ylim([1e1, 1e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 4 in plots:
    plt.figure(4)
    plt.plot(cs_kcbk_000_T[0],    C_int * cs_kcbk_000_rel_T[5], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_rel_T[5], '--',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_000_T[0],     C_int * cs_tbk_000_rel_T[5], 'r-',label=r'NLO+rel TBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_461_T[0],     C_int * cs_tbk_461_rel_T[5], 'r--',label=r'NLO+rel TBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_000_T[0], C_int * cs_resumbk_000_rel_T[5], 'b-',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_461_T[0], C_int * cs_resumbk_461_rel_T[5], 'b--',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[3] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.legend(prop={'size': 10}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([1e1, 5e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 5 in plots:
    plt.figure(5)
    plt.plot(cs_kcbk_000_T[0],    C_int * cs_kcbk_000_rel_T[5], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_000_T[0],     C_int * cs_tbk_000_rel_T[5], 'c-',label=r'NLO+rel TBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_000_T[0], C_int * cs_resumbk_000_rel_T[5], 'm-',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[3] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.fill_between(cs_kcbk_000_T[0], C_int * (cs_kcbk_000_rel_T[5]-cs_kcbk_000_rel_T[6]), C_int * (cs_kcbk_000_rel_T[5]+cs_kcbk_000_rel_T[6]), facecolor='tab:green',alpha=0.3)
    plt.fill_between(cs_tbk_000_T[0], C_int * (cs_tbk_000_rel_T[5]-cs_tbk_000_rel_T[6]), C_int * (cs_tbk_000_rel_T[5]+cs_tbk_000_rel_T[6]), facecolor='c',alpha=0.3)
    plt.fill_between(cs_resumbk_000_T[0], C_int * (cs_resumbk_000_rel_T[5]-cs_resumbk_000_rel_T[6]), C_int * (cs_resumbk_000_rel_T[5]+cs_resumbk_000_rel_T[6]), facecolor='m',alpha=0.3)
    plt.fill_between(cs_lobk_mve_T[0], C_int * NRQCD_factor * (cs_lobk_mve_rel_T[3]-cs_lobk_mve_rel_T[4]), C_int * NRQCD_factor * (cs_lobk_mve_rel_T[3]+cs_lobk_mve_rel_T[4]), facecolor='k',alpha=0.3)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.legend(prop={'size': 11}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([1e1, 5e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 6 in plots:
    plt.figure(6)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_rel_T[5], '-',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_461_T[0],     C_int * cs_tbk_461_rel_T[5], 'c-',label=r'NLO+rel TBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_461_T[0], C_int * cs_resumbk_461_rel_T[5], 'm-',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[3] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.fill_between(cs_kcbk_461_T[0], C_int * (cs_kcbk_461_rel_T[5]-cs_kcbk_461_rel_T[6]), C_int * (cs_kcbk_461_rel_T[5]+cs_kcbk_461_rel_T[6]), facecolor='tab:green',alpha=0.3)
    plt.fill_between(cs_tbk_461_T[0], C_int * (cs_tbk_461_rel_T[5]-cs_tbk_461_rel_T[6]), C_int * (cs_tbk_461_rel_T[5]+cs_tbk_461_rel_T[6]), facecolor='c',alpha=0.3)
    plt.fill_between(cs_resumbk_461_T[0], C_int * (cs_resumbk_461_rel_T[5]-cs_resumbk_461_rel_T[6]), C_int * (cs_resumbk_461_rel_T[5]+cs_resumbk_461_rel_T[6]), facecolor='m',alpha=0.3)
    plt.fill_between(cs_lobk_mve_T[0], C_int * NRQCD_factor * (cs_lobk_mve_rel_T[3]-cs_lobk_mve_rel_T[4]), C_int * NRQCD_factor * (cs_lobk_mve_rel_T[3]+cs_lobk_mve_rel_T[4]), facecolor='k',alpha=0.3)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.legend(prop={'size': 11}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([1e1, 5e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 10 in plots:
    plt.figure(10)
    plt.plot(cs_kcbk_000_T[0], cs_kcbk_000_T[1], '-',color='tab:green',label=r'LO KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_kcbk_461_T[0], cs_kcbk_461_T[1], '--',color='tab:green',label=r'LO KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_000_T[0], cs_tbk_000_T[1], 'r-',label=r'LO TBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_461_T[0], cs_tbk_461_T[1], 'r--',label=r'LO TBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_000_T[0], cs_resumbk_000_T[1], 'b-',label=r'LO ResumBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_461_T[0], cs_resumbk_461_T[1], 'b--',label=r'LO ResumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0], cs_lobk_mve_T[5], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([3e1, 4e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

plt.show()