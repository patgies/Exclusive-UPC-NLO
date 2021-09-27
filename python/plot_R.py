
import matplotlib.pyplot as plt
import numpy as np
import os 

import plotting_functions
import experimental_data

    
plotting_functions.pheno_correction = False


bool_decay_width = True
bool_decay_width_rel = False

dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_L/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'


R_kcbk_000 =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', bool_decay_width)
R_kcbk_461 =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', bool_decay_width)
R_tbk_000 =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', bool_decay_width)
R_tbk_461 =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', bool_decay_width)
R_resumbk_000 = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', bool_decay_width)
R_resumbk_461 = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', bool_decay_width)
R_lobk_mve =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-LOBK-MVe-W_90.dat', dir_path_T + r'results-LOBK-MVe-W_90.dat', bool_decay_width)


R_W1000_kcbk_000 =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-L-W_1000.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-T-W_1000.dat', bool_decay_width)
R_W1000_kcbk_461 =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-L-W_1000.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-T-W_1000.dat', bool_decay_width)
R_W1000_tbk_000 =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-L-W_1000.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-T-W_1000.dat', bool_decay_width)
R_W1000_tbk_461 =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-L-W_1000.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-T-W_1000.dat', bool_decay_width)
R_W1000_resumbk_000 = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-L-W_1000.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-T-W_1000.dat', bool_decay_width)
R_W1000_resumbk_461 = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-L-W_1000.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-T-W_1000.dat', bool_decay_width)
R_W1000_lobk_mve =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-LOBK-MVe-W_1000.dat', dir_path_T + r'results-LOBK-MVe-W_1000.dat', bool_decay_width)


R_ZEUS_Q2, R_ZEUS_data =   experimental_data.R_Q2_ZEUS()
R_H1_Q2,   R_H1_data     = experimental_data.R_Q2_H1()

W = 90
C_int = plotting_functions.t_integration_coefficient(W)

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plots = [1,2,3,4]


if 1 in plots:
    plt.figure(1)
    plt.plot(R_kcbk_000[0],    R_kcbk_000[2], '-',color='tab:green',label=r'NLO KCBK 0.00', linewidth=linewidth)
    plt.plot(R_kcbk_461[0],    R_kcbk_461[2], '--',color='tab:green',label=r'NLO KCBK 4.61', linewidth=linewidth)
    plt.plot(R_tbk_000[0],     R_tbk_000[2], 'r-',label=r'NLO TBK 0.00', linewidth=linewidth)
    plt.plot(R_tbk_461[0],     R_tbk_461[2], 'r--',label=r'NLO TBK 4.61', linewidth=linewidth)
    plt.plot(R_resumbk_000[0], R_resumbk_000[2], 'b-',label=r'NLO ResumBK 0.00', linewidth=linewidth)
    plt.plot(R_resumbk_461[0], R_resumbk_461[2], 'b--',label=r'NLO ResumBK 4.61', linewidth=linewidth)
    plt.plot(R_lobk_mve[0],    R_lobk_mve[5], 'k:',label=r'LO MV$^e$', linewidth=linewidth)
    plt.errorbar(R_ZEUS_Q2[0], R_ZEUS_data[0], xerr=[R_ZEUS_Q2[0]-R_ZEUS_Q2[1], R_ZEUS_Q2[2]-R_ZEUS_Q2[0]] , yerr=[np.sqrt(R_ZEUS_data[1]**2+R_ZEUS_data[2]**2),np.sqrt(R_ZEUS_data[3]**2+R_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    plt.errorbar(R_H1_Q2[0], R_H1_data[0], xerr=[R_H1_Q2[0]-R_H1_Q2[1], R_H1_Q2[2]-R_H1_Q2[0]] , yerr=[np.sqrt(R_H1_data[1]**2+R_H1_data[2]**2),np.sqrt(R_H1_data[3]**2+R_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_L/\sigma_T$, $W= 90$ GeV', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0, 25])
    plt.ylim([0, 4])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 2 in plots:
    plt.figure(2)
    plt.plot(R_kcbk_000[0],    R_kcbk_000[4], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(R_kcbk_461[0],    R_kcbk_461[4], '--',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(R_tbk_000[0],     R_tbk_000[4], 'r-',label=r'NLO+rel TBK 0.00', linewidth=linewidth)
    plt.plot(R_tbk_461[0],     R_tbk_461[4], 'r--',label=r'NLO+rel TBK 4.61', linewidth=linewidth)
    plt.plot(R_resumbk_000[0], R_resumbk_000[4], 'b-',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth)
    plt.plot(R_resumbk_461[0], R_resumbk_461[4], 'b--',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth)
    plt.plot(R_lobk_mve[0],    R_lobk_mve[6], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.errorbar(R_ZEUS_Q2[0], R_ZEUS_data[0], xerr=[R_ZEUS_Q2[0]-R_ZEUS_Q2[1], R_ZEUS_Q2[2]-R_ZEUS_Q2[0]] , yerr=[np.sqrt(R_ZEUS_data[1]**2+R_ZEUS_data[2]**2),np.sqrt(R_ZEUS_data[3]**2+R_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    plt.errorbar(R_H1_Q2[0], R_H1_data[0], xerr=[R_H1_Q2[0]-R_H1_Q2[1], R_H1_Q2[2]-R_H1_Q2[0]] , yerr=[np.sqrt(R_H1_data[1]**2+R_H1_data[2]**2),np.sqrt(R_H1_data[3]**2+R_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_L/\sigma_T$, $W= 90$ GeV', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0, 25])
    plt.ylim([0, 4])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 3 in plots:
    plt.figure(3)
    plt.plot(R_W1000_kcbk_000[0],    R_W1000_kcbk_000[2], '-',color='tab:green',label=r'NLO KCBK 0.00', linewidth=linewidth)
    plt.plot(R_W1000_kcbk_461[0],    R_W1000_kcbk_461[2], '--',color='tab:green',label=r'NLO KCBK 4.61', linewidth=linewidth)
    plt.plot(R_W1000_tbk_000[0],     R_W1000_tbk_000[2], 'r-',label=r'NLO TBK 0.00', linewidth=linewidth)
    plt.plot(R_W1000_tbk_461[0],     R_W1000_tbk_461[2], 'r--',label=r'NLO TBK 4.61', linewidth=linewidth)
    plt.plot(R_W1000_resumbk_000[0], R_W1000_resumbk_000[2], 'b-',label=r'NLO ResumBK 0.00', linewidth=linewidth)
    plt.plot(R_W1000_resumbk_461[0], R_W1000_resumbk_461[2], 'b--',label=r'NLO ResumBK 4.61', linewidth=linewidth)
    plt.plot(R_W1000_lobk_mve[0],    R_W1000_lobk_mve[5], 'k:',label=r'LO MV$^e$', linewidth=linewidth)
    # plt.errorbar(R_ZEUS_Q2[0], R_ZEUS_data[0], xerr=[R_ZEUS_Q2[0]-R_ZEUS_Q2[1], R_ZEUS_Q2[2]-R_ZEUS_Q2[0]] , yerr=[np.sqrt(R_ZEUS_data[1]**2+R_ZEUS_data[2]**2),np.sqrt(R_ZEUS_data[3]**2+R_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    # plt.errorbar(R_H1_Q2[0], R_H1_data[0], xerr=[R_H1_Q2[0]-R_H1_Q2[1], R_H1_Q2[2]-R_H1_Q2[0]] , yerr=[np.sqrt(R_H1_data[1]**2+R_H1_data[2]**2),np.sqrt(R_H1_data[3]**2+R_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_L/\sigma_T$, $W= 1000$ GeV', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0, 25])
    plt.ylim([0, 4])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 4 in plots:
    plt.figure(4)
    plt.plot(R_W1000_kcbk_000[0],    R_W1000_kcbk_000[4], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(R_W1000_kcbk_461[0],    R_W1000_kcbk_461[4], '--',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(R_W1000_tbk_000[0],     R_W1000_tbk_000[4], 'r-',label=r'NLO+rel TBK 0.00', linewidth=linewidth)
    plt.plot(R_W1000_tbk_461[0],     R_W1000_tbk_461[4], 'r--',label=r'NLO+rel TBK 4.61', linewidth=linewidth)
    plt.plot(R_W1000_resumbk_000[0], R_W1000_resumbk_000[4], 'b-',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth)
    plt.plot(R_W1000_resumbk_461[0], R_W1000_resumbk_461[4], 'b--',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth)
    plt.plot(R_W1000_lobk_mve[0],    R_W1000_lobk_mve[6], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    # plt.errorbar(R_ZEUS_Q2[0], R_ZEUS_data[0], xerr=[R_ZEUS_Q2[0]-R_ZEUS_Q2[1], R_ZEUS_Q2[2]-R_ZEUS_Q2[0]] , yerr=[np.sqrt(R_ZEUS_data[1]**2+R_ZEUS_data[2]**2),np.sqrt(R_ZEUS_data[3]**2+R_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    # plt.errorbar(R_H1_Q2[0], R_H1_data[0], xerr=[R_H1_Q2[0]-R_H1_Q2[1], R_H1_Q2[2]-R_H1_Q2[0]] , yerr=[np.sqrt(R_H1_data[1]**2+R_H1_data[2]**2),np.sqrt(R_H1_data[3]**2+R_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_L/\sigma_T$, $W= 1000$ GeV', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0, 25])
    plt.ylim([0, 4])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

plt.show()
