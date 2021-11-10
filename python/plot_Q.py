
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os 

import plotting_functions
import experimental_data

    
plotting_functions.pheno_correction = False

particle = 'jpsi'
plotting_functions.particle = particle
plotting_functions.initialize()

reg_scheme_LO = 'decay width'
reg_scheme_NLO = 'NR wave function'
reg_scheme_rel = 'rel wave function'

dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_L/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'

# cs_kcbk_000_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', reg_scheme, "L" )
# cs_kcbk_461_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', reg_scheme, "L" )
# cs_tbk_000_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', reg_scheme, "L"  )
# cs_tbk_461_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', reg_scheme, "L"  )
# cs_resumbk_000_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', reg_scheme, "L"  )
# cs_resumbk_461_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', reg_scheme, "L"  )

# cs_lobk_mve_L = plotting_functions.get_cross_section_values_Q( dir_path_L + r'results-LOBK-MVe-Q.dat', reg_scheme, "L"  )

# cs_lobk_mve_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-LOBK-MVe-Q.dat', reg_scheme_rel, "L"  )
# cs_kcbk_461_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel, "L"  )
# cs_tbk_461_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel, "L"  )
# cs_resumbk_461_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel, "L"  )
# cs_kcbk_000_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel, "L"  )
# cs_tbk_000_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel, "L"  )
# cs_resumbk_000_rel_L = plotting_functions.get_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel, "L"  )

# cs_kcbk_000_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', reg_scheme, "T" )
# cs_kcbk_461_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', reg_scheme, "T" )
# cs_tbk_000_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', reg_scheme, "T" )
# cs_tbk_461_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', reg_scheme, "T" )
# cs_resumbk_000_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', reg_scheme, "T" )
# cs_resumbk_461_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', reg_scheme, "T" )

# cs_lobk_mve_T = plotting_functions.get_cross_section_values_Q( dir_path_T + r'results-LOBK-MVe-Q.dat', reg_scheme, "T" )

# cs_lobk_mve_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-LOBK-MVe-Q.dat', reg_scheme_rel, "T" )
# cs_kcbk_461_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel, "T" )
# cs_tbk_461_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel, "T" )
# cs_resumbk_461_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel, "T" )
# cs_kcbk_000_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel, "T" )
# cs_tbk_000_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel, "T" )
# cs_resumbk_000_rel_T = plotting_functions.get_distribution_Q( dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel, "T" )

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

if particle == 'jpsi':
    alpha_s0 = 0.25
    Mv = 3.0969
    id_string_L = '-jpsi-L-W_90'
    id_string_T = '-jpsi-T-W_90'
elif particle == 'upsilon':
    alpha_s0 = 0.18
    Mv = 9.46030
    id_string_L = '-upsilon-L-W_90'
    id_string_T = '-upsilon-T-W_90'
else:
    raise Exception('Improper particle!')

Mv2 = Mv**2

Cf = 4/3
NRQCD_factor = (1-2*Cf*alpha_s0/np.pi)**2


cs_kcbk_000 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00' + id_string_L + '.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00' + id_string_T + '.dat', reg_scheme_NLO)
cs_kcbk_461 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61' + id_string_L + '.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61' + id_string_T + '.dat', reg_scheme_NLO)
cs_tbk_000 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00' + id_string_L + '.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00' + id_string_T + '.dat', reg_scheme_NLO)
cs_tbk_461 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61' + id_string_L + '.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61' + id_string_T + '.dat', reg_scheme_NLO)
cs_resumbk_000 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00' + id_string_L + '.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00' + id_string_T + '.dat', reg_scheme_NLO)
cs_resumbk_461 = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61' + id_string_L + '.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61' + id_string_T + '.dat', reg_scheme_NLO)
cs_lobk_mve = plotting_functions.get_total_cross_section_Q( dir_path_L + r'results-LOBK-MVe' + id_string_L + '.dat', dir_path_T + r'results-LOBK-MVe' + id_string_T + '.dat', reg_scheme_LO)


cs_kcbk_000_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00' + id_string_L + '.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00' + id_string_T + '.dat', reg_scheme_rel)
cs_kcbk_461_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61' + id_string_L + '.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61' + id_string_T + '.dat', reg_scheme_rel)
cs_tbk_000_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00' + id_string_L + '.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00' + id_string_T + '.dat', reg_scheme_rel)
cs_tbk_461_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61' + id_string_L + '.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61' + id_string_T + '.dat', reg_scheme_rel)
cs_resumbk_000_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00' + id_string_L + '.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00' + id_string_T + '.dat', reg_scheme_rel)
cs_resumbk_461_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61' + id_string_L + '.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61' + id_string_T + '.dat', reg_scheme_rel)
cs_lobk_mve_rel = plotting_functions.get_total_cross_section_distribution_Q( dir_path_L + r'results-LOBK-MVe' + id_string_L + '.dat', dir_path_T + r'results-LOBK-MVe' + id_string_T + '.dat', reg_scheme_rel)

# cs_lobk_mve_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-LOBK-MVe-Q.dat', dir_path_T + r'results-LOBK-MVe-Q.dat', reg_scheme_rel)
# cs_kcbk_461_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel)
# cs_tbk_461_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel)
# cs_resumbk_461_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-4.61-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-4.61-Q.dat', reg_scheme_rel)
# cs_kcbk_000_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-kcbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-kcbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel)
# cs_tbk_000_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-tbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-tbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel)
# cs_resumbk_000_rel = plotting_functions.get_distribution_Q( dir_path_L + r'results-resumbk-hera-bal+sd-0.00-Q.dat', dir_path_T + r'results-resumbk-hera-bal+sd-0.00-Q.dat', reg_scheme_rel)

sigma_tot_ZEUS_Q2, sigma_tot_ZEUS_data = experimental_data.sigma_tot_Q2_ZEUS()
sigma_tot_H1_Q2, sigma_tot_H1_data     = experimental_data.sigma_tot_Q2_H1()

W = 90
C_int = plotting_functions.t_integration_coefficient(W)

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plots = [3,4]

linewidth1 = 1.3*linewidth
linewidth2 = 1.0*linewidth
linewidth3 = 0.7*linewidth




legend_lines = [Line2D([0], [0], color='r', linestyle='-', linewidth=linewidth1),
                Line2D([0], [0], color='g', linestyle='-', linewidth=linewidth2),
                Line2D([0], [0], color='b', linestyle='-', linewidth=linewidth3),
                Line2D([0], [0], color='k', linestyle=':', linewidth=linewidth2),
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
                r'H1',
                r'ZEUS'
                ]

legend_text_rel =  [r'NLO+rel KCBK',
                    r'NLO+rel TBK',
                    r'NLO+rel ResumBK',
                    r'LO+rel LOBK',
                    r'H1',
                    r'ZEUS'
                    ]

legend_text_Y = [ r'$Y_{0,\mathrm{BK}}=4.61$',
                  r'$Y_{0,\mathrm{BK}}=0.00$']

if 1 in plots:
    plt.figure(1)
    plt.plot(Mv2 + cs_kcbk_000[0], cs_kcbk_000[2], 'r-',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_kcbk_461[0], cs_kcbk_461[2], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth2)
    plt.plot(Mv2 + cs_tbk_000[0], cs_tbk_000[2], '--' ,color='tab:green',label=r'NLO TBK 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_tbk_461[0], cs_tbk_461[2], '--',color='tab:green',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(Mv2 + cs_resumbk_000[0], cs_resumbk_000[2], 'b-.',label=r'NLO ResumBK 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_resumbk_461[0], cs_resumbk_461[2], 'b-.',label=r'NLO ResumBK 4.61', linewidth=linewidth2)
    plt.plot(Mv2 + cs_lobk_mve[0], cs_lobk_mve[5], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth2)
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
    plt.plot(Mv2 + cs_kcbk_000[0], cs_kcbk_000_rel[5], 'r-',label=r'NLO+rel KCBK 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_kcbk_461[0], cs_kcbk_461_rel[5], 'r-',label=r'NLO+rel KCBK 4.61', linewidth=linewidth2)
    plt.plot(Mv2 + cs_tbk_000[0], cs_tbk_000_rel[5], '--' ,color='tab:green',label=r'NLO+rel TBK 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_tbk_461[0], cs_tbk_461_rel[5], '--',color='tab:green',label=r'NLO+rel TBK 4.61', linewidth=linewidth2)
    plt.plot(Mv2 + cs_resumbk_000[0], cs_resumbk_000_rel[5], 'b-.',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_resumbk_461[0], cs_resumbk_461_rel[5], 'b-.',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth2)
    plt.plot(Mv2 + cs_lobk_mve[0], NRQCD_factor * cs_lobk_mve_rel[3], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth2)
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
    fig3=plt.figure(num=3)
    plt.plot(Mv2 + cs_kcbk_000[0],    C_int * cs_kcbk_000[2], 'r--',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_kcbk_461[0],    C_int * cs_kcbk_461[2], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth1)
    plt.plot(Mv2 + cs_tbk_000[0],     C_int * cs_tbk_000[2], 'g--',label=r'NLO TBK 0.00', linewidth=linewidth2)
    plt.plot(Mv2 + cs_tbk_461[0],     C_int * cs_tbk_461[2], 'g-',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(Mv2 + cs_resumbk_000[0], C_int * cs_resumbk_000[2], 'b--',label=r'NLO ResumBK 0.00', linewidth=linewidth3)
    plt.plot(Mv2 + cs_resumbk_461[0], C_int * cs_resumbk_461[2], 'b-',label=r'NLO ResumBK 4.61', linewidth=linewidth3)
    plt.plot(Mv2 + cs_lobk_mve[0],    C_int * cs_lobk_mve[5], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_Q2[0]+Mv**2, sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_Q2[0]-sigma_tot_ZEUS_Q2[1], sigma_tot_ZEUS_Q2[2]-sigma_tot_ZEUS_Q2[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_Q2[0]+Mv**2, sigma_tot_H1_data[0], xerr=[sigma_tot_H1_Q2[0]-sigma_tot_H1_Q2[1], sigma_tot_H1_Q2[2]-sigma_tot_H1_Q2[0]] , yerr=[np.sqrt(sigma_tot_H1_data[1]**2+sigma_tot_H1_data[2]**2),np.sqrt(sigma_tot_H1_data[3]**2+sigma_tot_H1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    legend1 = plt.legend(legend_lines,   legend_text, prop={'size': 14.5}, frameon=False, loc='lower left')
    legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 14.5}, frameon=False, loc='upper right')
    plt.gca().add_artist(legend1) 
    # plt.title(r'$\sigma_{\textrm{tot}}$, $W= 90$ GeV [nb]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.67, 0.75, r'$W = 90\textrm{ GeV}$', transform=fig3.transFigure, fontsize=20)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.05, 2e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 4 in plots:    
    fig4=plt.figure(num=4)
    plt.plot(Mv2 + cs_kcbk_000[0],    C_int * cs_kcbk_000_rel[5], 'r--',label=r'NLO+rel KCBK 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_kcbk_461[0],    C_int * cs_kcbk_461_rel[5], 'r-',label=r'NLO+rel KCBK 4.61', linewidth=linewidth1)
    plt.plot(Mv2 + cs_tbk_000[0],     C_int * cs_tbk_000_rel[5], 'g--',label=r'NLO+rel TBK 0.00', linewidth=linewidth2)
    plt.plot(Mv2 + cs_tbk_461[0],     C_int * cs_tbk_461_rel[5], 'g-',label=r'NLO+rel TBK 4.61', linewidth=linewidth2)
    plt.plot(Mv2 + cs_resumbk_000[0], C_int * cs_resumbk_000_rel[5], 'b--',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth3)
    plt.plot(Mv2 + cs_resumbk_461[0], C_int * cs_resumbk_461_rel[5], 'b-',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth3)
    plt.plot(Mv2 + cs_lobk_mve[0],    C_int * cs_lobk_mve_rel[3] * NRQCD_factor, 'k:',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_Q2[0]+Mv**2, sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_Q2[0]-sigma_tot_ZEUS_Q2[1], sigma_tot_ZEUS_Q2[2]-sigma_tot_ZEUS_Q2[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_Q2[0]+Mv**2, sigma_tot_H1_data[0], xerr=[sigma_tot_H1_Q2[0]-sigma_tot_H1_Q2[1], sigma_tot_H1_Q2[2]-sigma_tot_H1_Q2[0]] , yerr=[np.sqrt(sigma_tot_H1_data[1]**2+sigma_tot_H1_data[2]**2),np.sqrt(sigma_tot_H1_data[3]**2+sigma_tot_H1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    legend1 = plt.legend(legend_lines, legend_text_rel, prop={'size': 14.5}, frameon=False, loc='lower left')
    legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 14.5}, frameon=False, loc='upper right')
    plt.gca().add_artist(legend1) 
    # plt.title(r'$\sigma_{\textrm{tot}}$, $W= 90$ GeV [nb]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.67, 0.75, r'$W = 90\textrm{ GeV}$', transform=fig4.transFigure, fontsize=20)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.05, 2e2])
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
    plt.plot(Mv2 + cs_tbk_000[0],     C_int * cs_tbk_000_rel[5], 'c-',label=r'NLO+rel TBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_000[0], C_int * cs_resumbk_000_rel[5], 'm-',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth)
    plt.plot(Mv2 + cs_lobk_mve[0],    C_int * cs_lobk_mve_rel[3] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.fill_between(Mv2 + cs_kcbk_000[0], C_int * (cs_kcbk_000_rel[5]-cs_kcbk_000_rel[6]), C_int * (cs_kcbk_000_rel[5]+cs_kcbk_000_rel[6]), facecolor='tab:green',alpha=0.3)
    plt.fill_between(Mv2 + cs_tbk_000[0], C_int * (cs_tbk_000_rel[5]-cs_tbk_000_rel[6]), C_int * (cs_tbk_000_rel[5]+cs_tbk_000_rel[6]), facecolor='c',alpha=0.3)
    plt.fill_between(Mv2 + cs_resumbk_000[0], C_int * (cs_resumbk_000_rel[5]-cs_resumbk_000_rel[6]), C_int * (cs_resumbk_000_rel[5]+cs_resumbk_000_rel[6]), facecolor='m',alpha=0.3)
    plt.fill_between(Mv2 + cs_lobk_mve[0], C_int * NRQCD_factor * (cs_lobk_mve_rel[3]-cs_lobk_mve_rel[4]), C_int * NRQCD_factor * (cs_lobk_mve_rel[3]+cs_lobk_mve_rel[4]), facecolor='k',alpha=0.3)
    plt.errorbar(sigma_tot_ZEUS_Q2[0]+Mv**2, sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_Q2[0]-sigma_tot_ZEUS_Q2[1], sigma_tot_ZEUS_Q2[2]-sigma_tot_ZEUS_Q2[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    plt.errorbar(sigma_tot_H1_Q2[0]+Mv**2, sigma_tot_H1_data[0], xerr=[sigma_tot_H1_Q2[0]-sigma_tot_H1_Q2[1], sigma_tot_H1_Q2[2]-sigma_tot_H1_Q2[0]] , yerr=[np.sqrt(sigma_tot_H1_data[1]**2+sigma_tot_H1_data[2]**2),np.sqrt(sigma_tot_H1_data[3]**2+sigma_tot_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $W= 90$ GeV [nb]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.05, 1e2])
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
    plt.plot(Mv2 + cs_tbk_461[0],     C_int * cs_tbk_461_rel[5], 'c-',label=r'NLO+rel TBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_resumbk_461[0], C_int * cs_resumbk_461_rel[5], 'm-',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth)
    plt.plot(Mv2 + cs_lobk_mve[0],    C_int * cs_lobk_mve_rel[3] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.fill_between(Mv2 + cs_kcbk_461[0], C_int * (cs_kcbk_461_rel[5]-cs_kcbk_461_rel[6]), C_int * (cs_kcbk_461_rel[5]+cs_kcbk_461_rel[6]), facecolor='tab:green',alpha=0.3)
    plt.fill_between(Mv2 + cs_tbk_461[0], C_int * (cs_tbk_461_rel[5]-cs_tbk_461_rel[6]), C_int * (cs_tbk_461_rel[5]+cs_tbk_461_rel[6]), facecolor='c',alpha=0.3)
    plt.fill_between(Mv2 + cs_resumbk_461[0], C_int * (cs_resumbk_461_rel[5]-cs_resumbk_461_rel[6]), C_int * (cs_resumbk_461_rel[5]+cs_resumbk_461_rel[6]), facecolor='m',alpha=0.3)
    plt.fill_between(Mv2 + cs_lobk_mve[0], C_int * NRQCD_factor * (cs_lobk_mve_rel[3]-cs_lobk_mve_rel[4]), C_int * NRQCD_factor * (cs_lobk_mve_rel[3]+cs_lobk_mve_rel[4]), facecolor='k',alpha=0.3)
    plt.errorbar(sigma_tot_ZEUS_Q2[0]+Mv**2, sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_Q2[0]-sigma_tot_ZEUS_Q2[1], sigma_tot_ZEUS_Q2[2]-sigma_tot_ZEUS_Q2[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=100)
    plt.errorbar(sigma_tot_H1_Q2[0]+Mv**2, sigma_tot_H1_data[0], xerr=[sigma_tot_H1_Q2[0]-sigma_tot_H1_Q2[1], sigma_tot_H1_Q2[2]-sigma_tot_H1_Q2[0]] , yerr=[np.sqrt(sigma_tot_H1_data[1]**2+sigma_tot_H1_data[2]**2),np.sqrt(sigma_tot_H1_data[3]**2+sigma_tot_H1_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=100)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $W= 90$ GeV [nb]', fontsize=17)
    plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0.05, 1e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


plt.show()