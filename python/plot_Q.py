
import matplotlib.pyplot as plt
import numpy as np
import plotting_functions
import os 

    
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


linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plots = [1, 2]

if 1 in plots:
    plt.figure(1)
    plt.plot(cs_kcbk_000[0], cs_kcbk_000[2], '-',color='tab:green',label=r'NLO KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_kcbk_461[0], cs_kcbk_461[2], '--',color='tab:green',label=r'NLO KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_000[0], cs_tbk_000[2], 'r-',label=r'NLO tBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_461[0], cs_tbk_461[2], 'r--',label=r'NLO tBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_000[0], cs_resumbk_000[2], 'b-',label=r'NLO resumBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_461[0], cs_resumbk_461[2], 'b--',label=r'NLO resumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve[0], cs_lobk_mve[5], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, W= 90$ GeV [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0.01, 1e2])
    plt.ylim([0.1, 1e4])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 2 in plots:
    plt.figure(2)
    plt.plot(cs_kcbk_000[0], cs_kcbk_000_rel[5], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_kcbk_461[0], cs_kcbk_461_rel[5], '--',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_000[0], cs_tbk_000_rel[5], 'r-',label=r'NLO+rel tBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_461[0], cs_tbk_461_rel[5], 'r--',label=r'NLO+rel tBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_000[0], cs_resumbk_000_rel[5], 'b-',label=r'NLO+rel resumBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_461[0], cs_resumbk_461_rel[5], 'b--',label=r'NLO+rel resumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve[0], cs_lobk_mve_rel[3], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, W= 90$ GeV [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0.01, 1e2])
    plt.ylim([0.1, 1e4])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

plt.show()