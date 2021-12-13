
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os 

import plotting_functions
import experimental_data

    
plotting_functions.pheno_correction = False
plotting_functions.particle = 'jpsi'
plotting_functions.initialize()

reg_scheme_LO = 'decay width'
reg_scheme_NLO = 'NR wave function'
reg_scheme_rel = 'rel wave function' 
dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_L/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'


R_kcbk_000 =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_NLO)
R_kcbk_461 =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-jpsi-L-W_90.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-jpsi-T-W_90.dat', reg_scheme_NLO)
R_tbk_000 =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_NLO)
R_tbk_461 =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-jpsi-L-W_90.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-jpsi-T-W_90.dat', reg_scheme_NLO)
R_resumbk_000 = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_NLO)
R_resumbk_461 = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-jpsi-L-W_90.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-jpsi-T-W_90.dat', reg_scheme_NLO)
R_lobk_mve =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-LOBK-MVe-jpsi-L-W_90.dat', dir_path_T + r'results-LOBK-MVe-jpsi-T-W_90.dat', reg_scheme_LO)


R_kcbk_000_rel =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_rel)
R_kcbk_461_rel =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-jpsi-L-W_90.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-jpsi-T-W_90.dat', reg_scheme_rel)
R_tbk_000_rel =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_rel)
R_tbk_461_rel =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-jpsi-L-W_90.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-jpsi-T-W_90.dat', reg_scheme_rel)
R_resumbk_000_rel = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_rel)
R_resumbk_461_rel = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-jpsi-L-W_90.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-jpsi-T-W_90.dat', reg_scheme_rel)
R_lobk_mve_rel =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-LOBK-MVe-jpsi-L-W_90.dat', dir_path_T + r'results-LOBK-MVe-jpsi-T-W_90.dat', reg_scheme_rel)


# R_W1000_kcbk_000 =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-L-W_1000.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-T-W_1000.dat', reg_scheme_NLO)
# R_W1000_kcbk_461 =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-L-W_1000.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-T-W_1000.dat', reg_scheme_NLO)
# R_W1000_tbk_000 =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-L-W_1000.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-T-W_1000.dat', reg_scheme_NLO)
# R_W1000_tbk_461 =     plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-L-W_1000.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-T-W_1000.dat', reg_scheme_NLO)
# R_W1000_resumbk_000 = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-L-W_1000.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-T-W_1000.dat', reg_scheme_NLO)
# R_W1000_resumbk_461 = plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-L-W_1000.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-T-W_1000.dat', reg_scheme_NLO)
# R_W1000_lobk_mve =    plotting_functions.get_cross_section_ratio_Q( dir_path_L + r'results-LOBK-MVe-W_1000.dat', dir_path_T + r'results-LOBK-MVe-W_1000.dat', reg_scheme_LO)


R_ZEUS_Q2, R_ZEUS_data =   experimental_data.R_Q2_ZEUS()
R_H1_Q2,   R_H1_data     = experimental_data.R_Q2_H1()

W = 90
C_int = plotting_functions.t_integration_coefficient(W)

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plots = [1,2]

linewidth1 = 1.3*linewidth
linewidth2 = 1.0*linewidth
linewidth3 = 0.7*linewidth


legend_lines = [Line2D([0], [0], color='r', linestyle='-', linewidth=linewidth1),
                Line2D([0], [0], color='g', linestyle='-', linewidth=linewidth2),
                Line2D([0], [0], color='b', linestyle='-', linewidth=linewidth3),
                Line2D([0], [0], color='k', linestyle=':', linewidth=linewidth2),
                Line2D([0], [0], color='k', linestyle='-', linewidth=linewidth1),
                Line2D([0], [0], color='k', linestyle='--', linewidth=linewidth1),
                Line2D([0], [0], color='b', linestyle='None', marker='v'),
                Line2D([0], [0], color='r', linestyle='None', marker='o')
]
                

legend_lines_Y = [
                Line2D([0], [0], color='k', linestyle='-', linewidth=linewidth1),
                Line2D([0], [0], color='k', linestyle='--', linewidth=linewidth1)
                ]

legend_text =  [r'NLO KCBK',
                r'NLO TBK',
                r'NLO ResumBK',
                r'LO LOBK',
                r'$Y_{0,\mathrm{BK}}=4.61$',
                r'$Y_{0,\mathrm{BK}}=0.00$',
                r'H1',
                r'ZEUS'
                ]

legend_text_rel =  [r'NLO+rel KCBK',
                    r'NLO+rel TBK',
                    r'NLO+rel ResumBK',
                    r'LO+rel LOBK',
                    r'$Y_{0,\mathrm{BK}}=4.61$',
                    r'$Y_{0,\mathrm{BK}}=0.00$',
                    r'H1',
                    r'ZEUS'
                    ]

legend_text_Y = [ r'$Y_{0,\mathrm{BK}}=4.61$',
                  r'$Y_{0,\mathrm{BK}}=0.00$']

if 1 in plots:
    fig1 = plt.figure(1)
    plt.plot(R_kcbk_000[0],    R_kcbk_000[2], 'r--',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(R_kcbk_461[0],    R_kcbk_461[2], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth1)
    plt.plot(R_tbk_000[0],     R_tbk_000[2], 'g--',label=r'NLO TBK 0.00', linewidth=linewidth2)
    plt.plot(R_tbk_461[0],     R_tbk_461[2], 'g-' ,label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(R_resumbk_000[0], R_resumbk_000[2], 'b--',label=r'NLO ResumBK 0.00', linewidth=linewidth3)
    plt.plot(R_resumbk_461[0], R_resumbk_461[2], 'b-',label=r'NLO ResumBK 4.61', linewidth=linewidth3)
    plt.plot(R_lobk_mve[0],    R_lobk_mve[5], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    plt.errorbar(R_ZEUS_Q2[0], R_ZEUS_data[0], xerr=[R_ZEUS_Q2[0]-R_ZEUS_Q2[1], R_ZEUS_Q2[2]-R_ZEUS_Q2[0]] , yerr=[np.sqrt(R_ZEUS_data[1]**2+R_ZEUS_data[2]**2),np.sqrt(R_ZEUS_data[3]**2+R_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    plt.errorbar(R_H1_Q2[0], R_H1_data[0], xerr=[R_H1_Q2[0]-R_H1_Q2[1], R_H1_Q2[2]-R_H1_Q2[0]] , yerr=[np.sqrt(R_H1_data[1]**2+R_H1_data[2]**2),np.sqrt(R_H1_data[3]**2+R_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(legend_lines, legend_text, prop={'size': 17}, frameon=False, labelspacing=0.4,  borderaxespad=0.2)
    plt.xlabel(r'$Q^2$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_L/\sigma_T$', fontsize=20)
    plt.text(0.60, 0.85, r'$W = 90\textrm{ GeV}$', transform=fig1.transFigure, fontsize=20)
    plt.xlim([0, 25])
    plt.ylim([0, 3.5])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 2 in plots:
    fig2 = plt.figure(2)
    plt.plot(R_kcbk_000_rel[0],    R_kcbk_000_rel[4], 'r--',label=r'NLO+rel KCBK 0.00', linewidth=linewidth1)
    plt.plot(R_kcbk_461_rel[0],    R_kcbk_461_rel[4], 'r-' ,label=r'NLO+rel KCBK 4.61', linewidth=linewidth1)
    plt.plot(R_tbk_000_rel[0],     R_tbk_000_rel[4], 'g--',label=r'NLO+rel TBK 0.00', linewidth=linewidth2)
    plt.plot(R_tbk_461_rel[0],     R_tbk_461_rel[4], 'g-' ,label=r'NLO+rel TBK 4.61', linewidth=linewidth2)
    plt.plot(R_resumbk_000_rel[0], R_resumbk_000_rel[4], 'b--',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth3)
    plt.plot(R_resumbk_461_rel[0], R_resumbk_461_rel[4], 'b-',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth3)
    plt.plot(R_lobk_mve_rel[0],    R_lobk_mve_rel[6], 'k:',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.errorbar(R_ZEUS_Q2[0], R_ZEUS_data[0], xerr=[R_ZEUS_Q2[0]-R_ZEUS_Q2[1], R_ZEUS_Q2[2]-R_ZEUS_Q2[0]] , yerr=[np.sqrt(R_ZEUS_data[1]**2+R_ZEUS_data[2]**2),np.sqrt(R_ZEUS_data[3]**2+R_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    plt.errorbar(R_H1_Q2[0], R_H1_data[0], xerr=[R_H1_Q2[0]-R_H1_Q2[1], R_H1_Q2[2]-R_H1_Q2[0]] , yerr=[np.sqrt(R_H1_data[1]**2+R_H1_data[2]**2),np.sqrt(R_H1_data[3]**2+R_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(legend_lines, legend_text_rel, prop={'size': 17}, frameon=False, labelspacing=0.4,  borderaxespad=0.2)
    plt.xlabel(r'$Q^2$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_L/\sigma_T$', fontsize=20)
    plt.text(0.60, 0.85, r'$W = 90\textrm{ GeV}$', transform=fig2.transFigure, fontsize=20)
    plt.xlim([0, 25])
    plt.ylim([0, 3.5])
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
    plt.legend(prop={'size': 11}, frameon=False)
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
    plt.legend(prop={'size': 11}, frameon=False)
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
