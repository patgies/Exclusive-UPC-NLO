
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
import os 
import plotting_functions

#TODO:correct, add data


plotting_functions.pheno_correction = True


bool_decay_width = True
bool_decay_width_rel = False

dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_L/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'

cs_kcbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-kcbk-hera-bal+sd-0.00.dat', bool_decay_width, "L" )
cs_kcbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-kcbk-hera-bal+sd-4.61.dat', bool_decay_width, "L" )
cs_tbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-tbk-hera-bal+sd-0.00.dat', bool_decay_width, "L"  )
cs_tbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-tbk-hera-bal+sd-4.61.dat', bool_decay_width, "L"  )
cs_resumbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-resumbk-hera-bal+sd-0.00.dat', bool_decay_width, "L"  )
cs_resumbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-resumbk-hera-bal+sd-4.61.dat', bool_decay_width, "L"  )

# cs_ipsat_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-IP_SAT_m1.4.dat', bool_decay_width )
cs_lobk_mve_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-LOBK-MVe.dat', bool_decay_width, "L"  )

cs_lobk_mve_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-LOBK-MVe.dat', bool_decay_width_rel, "L"  )
cs_kcbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-kcbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "L"  )
cs_tbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-tbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "L"  )
cs_resumbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-resumbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "L"  )
cs_kcbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-kcbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "L"  )
cs_tbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-tbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "L"  )
cs_resumbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-resumbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "L"  )

cs_kcbk_000_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-kcbk-hera-bal+sd-0.00.dat', bool_decay_width, "T" )
cs_kcbk_461_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-kcbk-hera-bal+sd-4.61.dat', bool_decay_width, "T" )
cs_tbk_000_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-tbk-hera-bal+sd-0.00.dat', bool_decay_width, "T" )
cs_tbk_461_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-tbk-hera-bal+sd-4.61.dat', bool_decay_width, "T" )
cs_resumbk_000_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-resumbk-hera-bal+sd-0.00.dat', bool_decay_width, "T" )
cs_resumbk_461_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-resumbk-hera-bal+sd-4.61.dat', bool_decay_width, "T" )

# cs_ipsat_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-IP_SAT_m1.4.dat', bool_decay_width )
cs_lobk_mve_T = plotting_functions.get_cross_section_values_W( dir_path_T + r'results-LOBK-MVe.dat', bool_decay_width, "T" )

cs_lobk_mve_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-LOBK-MVe.dat', bool_decay_width_rel, "T" )
cs_kcbk_461_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-kcbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "T" )
cs_tbk_461_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-tbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "T" )
cs_resumbk_461_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-resumbk-hera-bal+sd-4.61.dat', bool_decay_width_rel, "T" )
cs_kcbk_000_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-kcbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "T" )
cs_tbk_000_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-tbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "T" )
cs_resumbk_000_rel_T = plotting_functions.get_distribution_W( dir_path_T + r'results-resumbk-hera-bal+sd-0.00.dat', bool_decay_width_rel, "T" )



cs_kcbk_000 = cs_kcbk_000_L + cs_kcbk_000_T
cs_kcbk_461 = cs_kcbk_461_L + cs_kcbk_461_T
cs_tbk_000 = cs_tbk_000_L + cs_tbk_000_T
cs_tbk_461 = cs_tbk_461_L + cs_tbk_461_T
cs_resumbk_000 = cs_resumbk_000_L + cs_resumbk_000_T
cs_resumbk_461 = cs_resumbk_461_L + cs_resumbk_461_T
cs_lobk_mve = cs_lobk_mve_L + cs_lobk_mve_T

cs_kcbk_000_rel = cs_kcbk_000_rel_L + cs_kcbk_000_rel_T
cs_kcbk_461_rel = cs_kcbk_461_rel_L + cs_kcbk_461_rel_T
cs_tbk_000_rel = cs_tbk_000_rel_L + cs_tbk_000_rel_T
cs_tbk_461_rel = cs_tbk_461_rel_L + cs_tbk_461_rel_T
cs_resumbk_000_rel = cs_resumbk_000_rel_L + cs_resumbk_000_rel_T
cs_resumbk_461_rel = cs_resumbk_461_rel_L + cs_resumbk_461_rel_T
cs_lobk_mve_rel = cs_lobk_mve_rel_L + cs_lobk_mve_rel_T


linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plots = [1,2,3]

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
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 10$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([50, 1e3])
    plt.ylim([5, 500])
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
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 10$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([50, 1e3])
    plt.ylim([10, 500])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

# if 3 in plots:
#     plt.figure(3)
#     plt.plot(cs_kcbk_000[0], cs_kcbk_000[4], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
#     plt.plot(cs_kcbk_461[0], cs_kcbk_461[4], '--',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
#     plt.plot(cs_tbk_000[0], cs_tbk_000[4], 'r-',label=r'NLO+rel tBK 0.00', linewidth=linewidth)
#     plt.plot(cs_tbk_461[0], cs_tbk_461[4], 'r--',label=r'NLO+rel tBK 4.61', linewidth=linewidth)
#     plt.plot(cs_resumbk_000[0], cs_resumbk_000[4], 'b-',label=r'NLO+rel resumBK 0.00', linewidth=linewidth)
#     plt.plot(cs_resumbk_461[0], cs_resumbk_461[4], 'b--',label=r'NLO+rel resumBK 4.61', linewidth=linewidth)
#     plt.plot(cs_lobk_mve[0], cs_lobk_mve[6], 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
#     plt.legend(prop={'size': 12}, frameon=False)
#     plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 10$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
#     plt.xlabel(r'$W$ [GeV]', fontsize=15)
#     plt.xlim([50, 1e3])
#     plt.ylim([10, 500])
#     plt.xticks(fontsize=15)
#     plt.yticks(fontsize=15)
#     plt.xscale('log')
#     plt.yscale('log')
#     plt.tight_layout()
#     plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
#     plt.tick_params(axis='x', pad=5)


# if 7 in plots:
#     alpha=0.25

#     plt.figure(7)
#     plt.plot(cs_lobk_mve[0], np.ones( len(cs_lobk_mve[0]) ), 'k-',label=r'LO LOBK', linewidth=linewidth)
#     plt.plot(cs_lobk_mve[0], cs_lobk_mve[6]/cs_lobk_mve[5], 'k--',label=r'LO+rel LOBK', linewidth=linewidth)
#     plt.plot(cs_kcbk_461[0], cs_kcbk_461[2]/cs_lobk_mve[5], 'r-',label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth)
#     plt.plot(cs_kcbk_461[0], cs_kcbk_461[4]/cs_lobk_mve[5], 'r--',label=r'NLO+rel KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth)
#     # plt.plot(cs_tbk_461[0], cs_tbk_461[2]/cs_lobk_mve[5], 'b-',label=r'NLO TBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth)
#     # plt.plot(cs_tbk_461[0], cs_tbk_461[4]/cs_lobk_mve[5], 'b--',label=r'NLO+rel TBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth)
#     plt.plot(cs_resumbk_461[0], cs_resumbk_461[2]/cs_lobk_mve[5], 'b-',label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth)
#     plt.plot(cs_resumbk_461[0], cs_resumbk_461[4]/cs_lobk_mve[5], 'b--',label=r'NLO+rel ResumBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth)
#     plt.fill_between(cs_lobk_mve_rel[0], (cs_lobk_mve_rel[3]-cs_lobk_mve_rel[4])/cs_lobk_mve[5], (cs_lobk_mve_rel[3]+cs_lobk_mve_rel[4])/cs_lobk_mve[5], facecolor='k',alpha=alpha)
#     plt.fill_between(cs_kcbk_461_rel[0], (cs_kcbk_461_rel[5]-cs_kcbk_461_rel[6])/cs_lobk_mve[5], (cs_kcbk_461_rel[5]+cs_kcbk_461_rel[6])/cs_lobk_mve[5], facecolor='r',alpha=alpha)
#     plt.fill_between(cs_resumbk_461_rel[0], (cs_resumbk_461_rel[5]-cs_resumbk_461_rel[6])/cs_lobk_mve[5], (cs_resumbk_461_rel[5]+cs_resumbk_461_rel[6])/cs_lobk_mve[5], facecolor='b',alpha=alpha)
#     plt.legend(prop={'size': 10}, frameon=False)
#     plt.ylabel(r'$(d\sigma_T/dt) / (d\sigma_T/dt)_\mathrm{LOBK}(Q^2=10\mathrm{ GeV}^2)$', fontsize=17)
#     plt.xlabel(r'$W$ [GeV]', fontsize=15)
#     plt.xlim([50, 1e3])
#     plt.ylim([0.2, 1.1])
#     plt.xticks(fontsize=15)
#     plt.yticks(fontsize=15)
#     plt.xscale('log')
#     plt.tight_layout()
#     plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
#     plt.tick_params(axis='x', pad=5)

# if 8 in plots:
#     linewidth1 = 0.6*linewidth
#     linewidth2 = 1.2*linewidth
#     # plt.figure(num=8, figsize=(6,8))
#     fig, (ax81, ax82) = plt.subplots(2,1, sharex=True, num=8, figsize=(6,8))
#     # plt.suptitle(r'$\mathrm{d}\sigma_L/\mathrm{d}t (t = 0, Q^2= 10\mathrm{ GeV}^2)$ [nb/GeV$^2$]', fontsize=17)
#     ax81.plot(cs_kcbk_000[0], cs_kcbk_000[2], 'r-' ,label=r'NLO KCBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     ax81.plot(cs_kcbk_461[0], cs_kcbk_461[2], 'r-', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax81.plot(cs_tbk_000[0], cs_tbk_000[2], '--' ,color='tab:green',label=r'NLO TBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     ax81.plot(cs_tbk_461[0], cs_tbk_461[2], '--', color='tab:green',label=r'NLO TBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax81.plot(cs_resumbk_000[0], cs_resumbk_000[2], 'b-.', label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     ax81.plot(cs_resumbk_461[0], cs_resumbk_461[2], 'b-.', label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax81.plot(cs_lobk_mve[0], cs_lobk_mve[5], 'k:',label=r'LO LOBK', linewidth=linewidth*1.2)
#     # ax81.plot(cs_ipsat[0], cs_ipsat[5], 'k--',label=r'LO IPSat', linewidth=linewidth*1.2)
#     ax81.set_ylim([5, 300])
#     ax81.set_yscale('log')
#     ax81.set_ylabel(r'$\mathrm{d}\sigma_T/\mathrm{d}t$ [nb/GeV$^2$]', fontsize=20)
#     plt.text(0.05, 0.85, r'$t=0, Q^2 = 10\textrm{ GeV}^2$', transform=ax81.transAxes, fontsize=20)
#     ax81.legend(prop={'size': 11}, frameon=False, handlelength=2.5, loc='lower right')

#     ax82.plot(cs_lobk_mve[0], np.ones( len(cs_lobk_mve[0]) ), 'k:',label=r'LO LOBK', linewidth=linewidth*1.2)
#     ax82.plot(cs_kcbk_000[0], cs_kcbk_000[2]/cs_lobk_mve[5], 'r-', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     ax82.plot(cs_kcbk_461[0], cs_kcbk_461[2]/cs_lobk_mve[5], 'r-', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax82.plot(cs_tbk_000[0], cs_tbk_000[2]/cs_lobk_mve[5], '--', color='tab:green', label=r'NLO TBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     ax82.plot(cs_tbk_461[0], cs_tbk_461[2]/cs_lobk_mve[5], '--', color='tab:green', label=r'NLO TBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax82.plot(cs_resumbk_000[0], cs_resumbk_000[2]/cs_lobk_mve[5], 'b-.' ,label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     ax82.plot(cs_resumbk_461[0], cs_resumbk_461[2]/cs_lobk_mve[5], 'b-.', label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     # ax82.plot(cs_ipsat[0], cs_ipsat[5]/cs_lobk_mve[5], 'k--', label=r'LO IPSat$', linewidth=1.2*linewidth)
#     ax82.set_xlim([50, 1e3])
#     ax82.set_ylim([0.2, 1.2])
#     ax82.set_xscale('log')
#     ax82.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
#     ax82.set_ylabel(r'$(\mathrm{d}\sigma_T/\mathrm{d}t)/(\mathrm{d}\sigma_T/\mathrm{d}t)_\mathrm{LOBK}$', fontsize=20)
#     ax82.set_xlabel(r'$W$ [GeV]', fontsize=20)
#     ax81.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=18)
#     ax82.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=18)
#     ax81.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=18)
#     ax82.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=18)
#     # plt.tick_params(axis='x', pad=5)
#     plt.tight_layout(pad=1.0)
#     plt.subplots_adjust(hspace=0)



# if 9 in plots:
#     linewidth1 = linewidth
#     # linewidth1 = 0.6*linewidth
#     linewidth2 = 1.2*linewidth
#     # plt.figure(num=8, figsize=(6,8))
#     fig, (ax91, ax92) = plt.subplots(2,1, sharex=True, num=9, figsize=(6,8))
#     # plt.suptitle(r'$\mathrm{d}\sigma_L/\mathrm{d}t (t = 0, Q^2= 10\mathrm{ GeV}^2)$ [nb/GeV$^2$]', fontsize=17)
#     ax91.plot(cs_kcbk_000[0], cs_kcbk_000[2], 'r-' ,label=r'NLO KCBK', linewidth=linewidth1)
#     # ax91.plot(cs_kcbk_461[0], cs_kcbk_461[2], 'r-', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax91.plot(cs_tbk_000[0], cs_tbk_000[2], '--' ,color='tab:green',label=r'NLO TBK', linewidth=linewidth1)
#     # ax91.plot(cs_tbk_461[0], cs_tbk_461[2], '--', color='tab:green',label=r'NLO TBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax91.plot(cs_resumbk_000[0], cs_resumbk_000[2], 'b-.', label=r'NLO ResumBK', linewidth=linewidth1)
#     # ax91.plot(cs_resumbk_461[0], cs_resumbk_461[2], 'b-.', label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax91.plot(cs_lobk_mve[0], cs_lobk_mve[5], 'k:',label=r'LO LOBK', linewidth=linewidth*1.2)
#     ax91.set_ylim([10, 400])
#     ax91.set_yscale('log')
#     ax91.set_ylabel(r'$\mathrm{d}\sigma_T/\mathrm{d}t$ [nb/GeV$^2$]', fontsize=20)
#     plt.text(0.05, 0.85, r'$t=0, Q^2 = 10\textrm{ GeV}^2$', transform=ax91.transAxes, fontsize=20)
#     ax91.legend(prop={'size': 15}, frameon=False, handlelength=2.5)

#     ax92.plot(cs_lobk_mve[0], np.ones( len(cs_lobk_mve[0]) ), 'k:',label=r'LO BK', linewidth=linewidth*1.2)
#     ax92.plot(cs_kcbk_000[0], cs_kcbk_000[2]/cs_lobk_mve[5], 'r-', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     # ax92.plot(cs_kcbk_461[0], cs_kcbk_461[2]/cs_lobk_mve[5], 'r-', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax92.plot(cs_tbk_000[0], cs_tbk_000[2]/cs_lobk_mve[5], '--', color='tab:green', label=r'NLO TBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     # ax92.plot(cs_tbk_461[0], cs_tbk_461[2]/cs_lobk_mve[5], '--', color='tab:green', label=r'NLO TBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax92.plot(cs_resumbk_000[0], cs_resumbk_000[2]/cs_lobk_mve[5], 'b-.' ,label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
#     # ax92.plot(cs_resumbk_461[0], cs_resumbk_461[2]/cs_lobk_mve[5], 'b-.', label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
#     ax92.set_xlim([50, 1e3])
#     ax92.set_ylim([0.6, 1.4])
#     ax92.set_xscale('log')
#     ax92.set_yticks([0.6, 0.8, 1.0, 1.2])
#     ax92.set_ylabel(r'$(\mathrm{d}\sigma_T/\mathrm{d}t)/(\mathrm{d}\sigma_T/\mathrm{d}t)_\mathrm{LOBK}$', fontsize=20)
#     ax92.set_xlabel(r'$W$ [GeV]', fontsize=20)
#     ax91.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=18)
#     ax92.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=18)
#     ax91.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=18)
#     ax92.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=18)
#     # plt.tick_params(axis='x', pad=5)
#     plt.tight_layout(pad=1.0)
#     plt.subplots_adjust(hspace=0)





plt.show()