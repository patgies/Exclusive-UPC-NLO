
import matplotlib.pyplot as plt
import numpy as np
import os 

import plotting_functions
import experimental_data

    
plotting_functions.pheno_correction = True


bool_decay_width = True
bool_decay_width_rel = False

dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_L/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'

# cs_kcbk_000_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', bool_decay_width, "L" )
# cs_kcbk_461_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', bool_decay_width, "L" )
# cs_tbk_000_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', bool_decay_width, "L"  )
# cs_tbk_461_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', bool_decay_width, "L"  )
# cs_resumbk_000_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', bool_decay_width, "L"  )
# cs_resumbk_461_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', bool_decay_width, "L"  )

# cs_lobk_mve_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-LOBK-MVe-Q.dat', bool_decay_width, "L"  )

# cs_lobk_mve_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-LOBK-MVe-Q.dat', bool_decay_width_rel, "L"  )
# cs_kcbk_461_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel, "L"  )
# cs_tbk_461_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel, "L"  )
# cs_resumbk_461_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel, "L"  )
# cs_kcbk_000_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel, "L"  )
# cs_tbk_000_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel, "L"  )
# cs_resumbk_000_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel, "L"  )

# cs_kcbk_000_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', bool_decay_width, "T" )
# cs_kcbk_461_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', bool_decay_width, "T" )
# cs_tbk_000_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', bool_decay_width, "T" )
# cs_tbk_461_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', bool_decay_width, "T" )
# cs_resumbk_000_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', bool_decay_width, "T" )
# cs_resumbk_461_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', bool_decay_width, "T" )

# cs_lobk_mve_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-LOBK-MVe-Q.dat', bool_decay_width, "T" )

# cs_lobk_mve_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-LOBK-MVe-Q.dat', bool_decay_width_rel, "T" )
# cs_kcbk_461_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel, "T" )
# cs_tbk_461_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel, "T" )
# cs_resumbk_461_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel, "T" )
# cs_kcbk_000_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel, "T" )
# cs_tbk_000_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel, "T" )
# cs_resumbk_000_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel, "T" )

# Q2v = cs_kcbk_000_L[0]

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

Mv = 3.0969
Mv2 = Mv**2



cs_kcbk_000 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', bool_decay_width)
cs_kcbk_461 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', bool_decay_width)
cs_tbk_000 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', bool_decay_width)
cs_tbk_461 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', bool_decay_width)
cs_resumbk_000 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', bool_decay_width)
cs_resumbk_461 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', bool_decay_width)
cs_lobk_mve = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-LOBK-MVe-Q.dat', dir_path_T + r'results-LOBK-MVe-Q.dat', bool_decay_width)


cs_kcbk_000_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel)
cs_kcbk_461_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel)
cs_tbk_000_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel)
cs_tbk_461_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel)
cs_resumbk_000_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel)
cs_resumbk_461_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel)
cs_lobk_mve_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-LOBK-MVe-Q.dat', dir_path_T + r'results-LOBK-MVe-Q.dat', bool_decay_width_rel)

# cs_lobk_mve_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-LOBK-MVe-Q.dat', dir_path_T + r'results-LOBK-MVe-Q.dat', bool_decay_width_rel)
# cs_kcbk_461_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel)
# cs_tbk_461_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel)
# cs_resumbk_461_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', bool_decay_width_rel)
# cs_kcbk_000_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel)
# cs_tbk_000_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel)
# cs_resumbk_000_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', bool_decay_width_rel)

sigma_tot_ZEUS_Q2, sigma_tot_ZEUS_data = experimental_data.sigma_tot_Q2_ZEUS()
sigma_tot_H1_Q2, sigma_tot_H1_data     = experimental_data.sigma_tot_Q2_H1()

W = 90
C_int = plotting_functions.t_integration_coefficient(W)

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plots = [3,4,5,6]

if 1 in plots:
    plt.figure(1)
    plt.plot(Mv2 + cs_kcbk_000[0], cs_kcbk_000[2], '-',color='tab:green',label=r'NLO KCBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_kcbk_461[0], cs_kcbk_461[2], '--',color='tab:green',label=r'NLO KCBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_000[0], cs_tbk_000[2], 'r-',label=r'NLO tBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_461[0], cs_tbk_461[2], 'r--',label=r'NLO tBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_000[0], cs_resumbk_000[2], 'b-',label=r'NLO resumBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_461[0], cs_resumbk_461[2], 'b--',label=r'NLO resumBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_lobk_mve[0], cs_lobk_mve[5], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, W= 90$ GeV [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.1, 1e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 2 in plots:
    plt.figure(2)
    plt.plot(Mv2 + cs_kcbk_000[0], cs_kcbk_000_rel[5], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_kcbk_461[0], cs_kcbk_461_rel[5], '--',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_000[0], cs_tbk_000_rel[5], 'r-',label=r'NLO+rel tBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_461[0], cs_tbk_461_rel[5], 'r--',label=r'NLO+rel tBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_000[0], cs_resumbk_000_rel[5], 'b-',label=r'NLO+rel resumBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_461[0], cs_resumbk_461_rel[5], 'b--',label=r'NLO+rel resumBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_lobk_mve[0], cs_lobk_mve_rel[3], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, W= 90$ GeV [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.1, 1e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 3 in plots:
    plt.figure(3)
    plt.plot(Mv2 + cs_kcbk_000[0],    C_int * cs_kcbk_000[2], '-',color='tab:green',label=r'NLO KCBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_kcbk_461[0],    C_int * cs_kcbk_461[2], '--',color='tab:green',label=r'NLO KCBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_000[0],     C_int * cs_tbk_000[2], 'r-',label=r'NLO tBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_461[0],     C_int * cs_tbk_461[2], 'r--',label=r'NLO tBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_000[0], C_int * cs_resumbk_000[2], 'b-',label=r'NLO resumBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_461[0], C_int * cs_resumbk_461[2], 'b--',label=r'NLO resumBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_lobk_mve[0],    C_int * cs_lobk_mve[5], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth)
    plt.errorbar(sigma_tot_ZEUS_Q2[0]+Mv**2, sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_Q2[0]-sigma_tot_ZEUS_Q2[1], sigma_tot_ZEUS_Q2[2]-sigma_tot_ZEUS_Q2[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_Q2[0]+Mv**2, sigma_tot_H1_data[0], xerr=[sigma_tot_H1_Q2[0]-sigma_tot_H1_Q2[1], sigma_tot_H1_Q2[2]-sigma_tot_H1_Q2[0]] , yerr=[np.sqrt(sigma_tot_H1_data[1]**2+sigma_tot_H1_data[2]**2),np.sqrt(sigma_tot_H1_data[3]**2+sigma_tot_H1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $W= 90$ GeV [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.1, 1e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 4 in plots:
    plt.figure(4)
    plt.plot(Mv2 + cs_kcbk_000[0],    C_int * cs_kcbk_000_rel[5], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_kcbk_461[0],    C_int * cs_kcbk_461_rel[5], '--',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_000[0],     C_int * cs_tbk_000_rel[5], 'r-',label=r'NLO+rel tBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_461[0],     C_int * cs_tbk_461_rel[5], 'r--',label=r'NLO+rel tBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_000[0], C_int * cs_resumbk_000_rel[5], 'b-',label=r'NLO+rel resumBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_461[0], C_int * cs_resumbk_461_rel[5], 'b--',label=r'NLO+rel resumBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_lobk_mve[0],    C_int * cs_lobk_mve_rel[3], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.errorbar(sigma_tot_ZEUS_Q2[0]+Mv**2, sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_Q2[0]-sigma_tot_ZEUS_Q2[1], sigma_tot_ZEUS_Q2[2]-sigma_tot_ZEUS_Q2[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_Q2[0]+Mv**2, sigma_tot_H1_data[0], xerr=[sigma_tot_H1_Q2[0]-sigma_tot_H1_Q2[1], sigma_tot_H1_Q2[2]-sigma_tot_H1_Q2[0]] , yerr=[np.sqrt(sigma_tot_H1_data[1]**2+sigma_tot_H1_data[2]**2),np.sqrt(sigma_tot_H1_data[3]**2+sigma_tot_H1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $W= 90$ GeV [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.1, 1e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 5 in plots:
    plt.figure(5)
    plt.plot(Mv2 + cs_kcbk_000[0],    C_int * cs_kcbk_000_rel[5], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_000[0],     C_int * cs_tbk_000_rel[5], 'c-',label=r'NLO+rel tBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_000[0], C_int * cs_resumbk_000_rel[5], 'm-',label=r'NLO+rel resumBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_lobk_mve[0],    C_int * cs_lobk_mve_rel[3], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.fill_between(Mv2 + cs_kcbk_000[0], C_int * (cs_kcbk_000_rel[5]-cs_kcbk_000_rel[6]), C_int * (cs_kcbk_000_rel[5]+cs_kcbk_000_rel[6]), facecolor='tab:green',alpha=0.3)
    plt.fill_between(Mv2 + cs_tbk_000[0], C_int * (cs_tbk_000_rel[5]-cs_tbk_000_rel[6]), C_int * (cs_tbk_000_rel[5]+cs_tbk_000_rel[6]), facecolor='c',alpha=0.3)
    plt.fill_between(Mv2 + cs_resumbk_000[0], C_int * (cs_resumbk_000_rel[5]-cs_resumbk_000_rel[6]), C_int * (cs_resumbk_000_rel[5]+cs_resumbk_000_rel[6]), facecolor='m',alpha=0.3)
    plt.fill_between(Mv2 + cs_lobk_mve[0], C_int * (cs_lobk_mve_rel[3]-cs_lobk_mve_rel[4]), C_int * (cs_lobk_mve_rel[3]+cs_lobk_mve_rel[4]), facecolor='k',alpha=0.3)
    plt.errorbar(sigma_tot_ZEUS_Q2[0]+Mv**2, sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_Q2[0]-sigma_tot_ZEUS_Q2[1], sigma_tot_ZEUS_Q2[2]-sigma_tot_ZEUS_Q2[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    plt.errorbar(sigma_tot_H1_Q2[0]+Mv**2, sigma_tot_H1_data[0], xerr=[sigma_tot_H1_Q2[0]-sigma_tot_H1_Q2[1], sigma_tot_H1_Q2[2]-sigma_tot_H1_Q2[0]] , yerr=[np.sqrt(sigma_tot_H1_data[1]**2+sigma_tot_H1_data[2]**2),np.sqrt(sigma_tot_H1_data[3]**2+sigma_tot_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $W= 90$ GeV [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.1, 1e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 6 in plots:
    plt.figure(6)
    plt.plot(Mv2 + cs_kcbk_461[0],    C_int * cs_kcbk_461_rel[5], '-',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_tbk_461[0],     C_int * cs_tbk_461_rel[5], 'c-',label=r'NLO+rel tBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_461[0], C_int * cs_resumbk_461_rel[5], 'm-',label=r'NLO+rel resumBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_lobk_mve[0],    C_int * cs_lobk_mve_rel[3], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.fill_between(Mv2 + cs_kcbk_461[0], C_int * (cs_kcbk_461_rel[5]-cs_kcbk_461_rel[6]), C_int * (cs_kcbk_461_rel[5]+cs_kcbk_461_rel[6]), facecolor='tab:green',alpha=0.3)
    plt.fill_between(Mv2 + cs_tbk_461[0], C_int * (cs_tbk_461_rel[5]-cs_tbk_461_rel[6]), C_int * (cs_tbk_461_rel[5]+cs_tbk_461_rel[6]), facecolor='c',alpha=0.3)
    plt.fill_between(Mv2 + cs_resumbk_461[0], C_int * (cs_resumbk_461_rel[5]-cs_resumbk_461_rel[6]), C_int * (cs_resumbk_461_rel[5]+cs_resumbk_461_rel[6]), facecolor='m',alpha=0.3)
    plt.fill_between(Mv2 + cs_lobk_mve[0], C_int * (cs_lobk_mve_rel[3]-cs_lobk_mve_rel[4]), C_int * (cs_lobk_mve_rel[3]+cs_lobk_mve_rel[4]), facecolor='k',alpha=0.3)
    plt.errorbar(sigma_tot_ZEUS_Q2[0]+Mv**2, sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_Q2[0]-sigma_tot_ZEUS_Q2[1], sigma_tot_ZEUS_Q2[2]-sigma_tot_ZEUS_Q2[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    plt.errorbar(sigma_tot_H1_Q2[0]+Mv**2, sigma_tot_H1_data[0], xerr=[sigma_tot_H1_Q2[0]-sigma_tot_H1_Q2[1], sigma_tot_H1_Q2[2]-sigma_tot_H1_Q2[0]] , yerr=[np.sqrt(sigma_tot_H1_data[1]**2+sigma_tot_H1_data[2]**2),np.sqrt(sigma_tot_H1_data[3]**2+sigma_tot_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $W= 90$ GeV [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.1, 1e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


plt.show()