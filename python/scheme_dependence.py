
import matplotlib.pyplot as plt
import numpy as np
from scipy import special
import os 

import plotting_functions


plotting_functions.pheno_correction = False


reg_scheme_dw = 'decay width'
reg_scheme_wf = 'NR wave function'
id_string = "-Q"
# id_string = ""
# id_string = "_Q2_0.05"


pol = 'T'

dir_path = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_' + pol + r'/'

cs_kcbk_000_dw = plotting_functions.get_cross_section_values_W( dir_path + r'results-kcbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_dw, pol )
cs_kcbk_461_dw = plotting_functions.get_cross_section_values_W( dir_path + r'results-kcbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_dw, pol )
cs_tbk_000_dw = plotting_functions.get_cross_section_values_W( dir_path + r'results-tbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_dw, pol )
cs_tbk_461_dw = plotting_functions.get_cross_section_values_W( dir_path + r'results-tbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_dw, pol )
cs_resumbk_000_dw = plotting_functions.get_cross_section_values_W( dir_path + r'results-resumbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_dw, pol )
cs_resumbk_461_dw = plotting_functions.get_cross_section_values_W( dir_path + r'results-resumbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_dw, pol )

cs_kcbk_000_wf = plotting_functions.get_cross_section_values_W( dir_path + r'results-kcbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_wf, pol )
cs_kcbk_461_wf = plotting_functions.get_cross_section_values_W( dir_path + r'results-kcbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_wf, pol )
cs_tbk_000_wf = plotting_functions.get_cross_section_values_W( dir_path + r'results-tbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_wf, pol )
cs_tbk_461_wf = plotting_functions.get_cross_section_values_W( dir_path + r'results-tbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_wf, pol )
cs_resumbk_000_wf = plotting_functions.get_cross_section_values_W( dir_path + r'results-resumbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_wf, pol )
cs_resumbk_461_wf = plotting_functions.get_cross_section_values_W( dir_path + r'results-resumbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_wf, pol )

xaxis = cs_kcbk_000_dw[0]
xmin = xaxis[0]
xmax = xaxis[-1]

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plots = [5]

linewidth1 = 0.8*linewidth
linewidth2 = 1.2*linewidth

if 1 in plots:
    plt.figure(1)
    plt.plot(cs_kcbk_000_dw[0], cs_kcbk_000_dw[2], 'r-',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_dw[0], cs_kcbk_461_dw[2], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth2)
    plt.plot(cs_tbk_000_dw[0], cs_tbk_000_dw[2], '--',color='tab:green',label=r'NLO TBK 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_461_dw[0], cs_tbk_461_dw[2], '--',color='tab:green',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_dw[0], cs_resumbk_000_dw[2], 'b-.',label=r'NLO ResumBK 0.00', linewidth=linewidth1)
    plt.plot(cs_resumbk_461_dw[0], cs_resumbk_461_dw[2], 'b-.',label=r'NLO ResumBK 4.61', linewidth=linewidth1)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$], decay width reg', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([xmin, xmax])
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
    plt.plot(cs_kcbk_000_wf[0],    cs_kcbk_000_wf[2], 'r-',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_wf[0],    cs_kcbk_461_wf[2], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth2)
    plt.plot(cs_tbk_000_wf[0],     cs_tbk_000_wf[2], '--',color='tab:green',label=r'NLO TBK 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_461_wf[0],     cs_tbk_461_wf[2], '--',color='tab:green',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_wf[0], cs_resumbk_000_wf[2], 'b-.',label=r'NLO ResumBK 0.00', linewidth=linewidth1)
    plt.plot(cs_resumbk_461_wf[0], cs_resumbk_461_wf[2], 'b-.',label=r'NLO ResumBK 4.61', linewidth=linewidth1)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$], wave function reg', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)    
    plt.xlim([xmin, xmax])
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
    plt.plot(cs_kcbk_000_dw[0],    cs_kcbk_000_dw[2], 'r-',label=r'NLO KCBK 0.00, decay width', linewidth=linewidth1)
    plt.plot(cs_kcbk_000_wf[0],    cs_kcbk_000_wf[2], 'r-',label=r'NLO KCBK 0.00, wave function', linewidth=linewidth2)
    plt.plot(cs_tbk_000_dw[0],     cs_tbk_000_dw[2], '--',color='tab:green',label=r'NLO TBK 0.00, decay width', linewidth=linewidth1)
    plt.plot(cs_tbk_000_wf[0],     cs_tbk_000_wf[2], '--',color='tab:green',label=r'NLO TBK 0.00, wave function', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_dw[0], cs_resumbk_000_dw[2], 'b-.',label=r'NLO ResumBK 0.00, decay width', linewidth=linewidth1)
    plt.plot(cs_resumbk_000_wf[0], cs_resumbk_000_wf[2], 'b-.',label=r'NLO ResumBK 0.00, wave function', linewidth=linewidth1)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$], wave function reg', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([xmin, xmax])
    plt.ylim([3e1, 4e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 4 in plots:
    plt.figure(4)
    plt.plot(cs_kcbk_461_dw[0],    cs_kcbk_461_dw[2], 'r-',label=r'NLO KCBK 4.61, decay width', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_wf[0],    cs_kcbk_461_wf[2], 'r-',label=r'NLO KCBK 4.61, wave function', linewidth=linewidth2)
    plt.plot(cs_tbk_461_dw[0],     cs_tbk_461_dw[2], '--',color='tab:green',label=r'NLO TBK 4.61, decay width', linewidth=linewidth1)
    plt.plot(cs_tbk_461_wf[0],     cs_tbk_461_wf[2], '--',color='tab:green',label=r'NLO TBK 4.61, wave function', linewidth=linewidth2)
    plt.plot(cs_resumbk_461_dw[0], cs_resumbk_461_dw[2], 'b-.',label=r'NLO ResumBK 4.61, decay width', linewidth=linewidth1)
    plt.plot(cs_resumbk_461_wf[0], cs_resumbk_461_wf[2], 'b-.',label=r'NLO ResumBK 4.61, wave function', linewidth=linewidth1)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$], wave function reg', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([xmin, xmax])
    plt.ylim([3e1, 4e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 5 in plots:
    fig5=plt.figure(5)
    plt.plot(cs_kcbk_000_dw[0],    cs_kcbk_000_dw[2]/cs_kcbk_000_wf[2], 'r-',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_dw[0],    cs_kcbk_461_dw[2]/cs_kcbk_461_wf[2], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth2)
    plt.plot(cs_tbk_000_dw[0],     cs_tbk_000_dw[2]/cs_tbk_000_wf[2], '--',color='tab:green',label=r'NLO TBK 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_461_dw[0],     cs_tbk_461_dw[2]/cs_tbk_461_wf[2], '--',color='tab:green',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_dw[0], cs_resumbk_000_dw[2]/cs_resumbk_000_wf[2], 'b-.',label=r'NLO ResumBK 0.00', linewidth=linewidth1)
    plt.plot(cs_resumbk_461_dw[0], cs_resumbk_461_dw[2]/cs_resumbk_461_wf[2], 'b-.',label=r'NLO ResumBK 4.61', linewidth=linewidth2)
    if pol == 'L':
        plt.title(r'$(d\sigma_L/dt)_\Gamma /(d\sigma_L/dt)_\Psi$', fontsize=17)
    elif pol == 'T':
        plt.title(r'$(d\sigma_T/dt)_\Gamma /(d\sigma_T/dt)_\Psi$', fontsize=17)
    if id_string == '-Q':
        plt.text(0.15, 0.85, r'$W = 90\textrm{ GeV}$, $t=0$', transform=fig5.transFigure, fontsize=14)
        plt.text(0.15, 0.77, r'$\Gamma = $ decay width scheme', transform=fig5.transFigure, fontsize=14)
        plt.text(0.15, 0.69, r'$\Psi = $ wave function scheme', transform=fig5.transFigure, fontsize=14)
        plt.legend(prop={'size': 11}, frameon=False, loc='lower left')
        plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    elif id_string == "_Q2_0.05":
        plt.text(0.50, 0.85, r'$Q^2 = 0.05\textrm{ GeV}^2$, $t=0$', transform=fig5.transFigure, fontsize=14)
        plt.text(0.50, 0.77, r'$\Gamma = $ decay width scheme', transform=fig5.transFigure, fontsize=14)
        plt.text(0.50, 0.69, r'$\Psi = $ wave function scheme', transform=fig5.transFigure, fontsize=14)
        plt.legend(prop={'size': 11}, frameon=False, loc='lower right')
        plt.xlabel(r'$W$ [GeV]', fontsize=15)
    elif id_string == "":
        plt.text(0.50, 0.85, r'$Q^2 = 10\textrm{ GeV}^2$, $t=0$', transform=fig5.transFigure, fontsize=14)
        plt.text(0.50, 0.77, r'$\Gamma = $ decay width scheme', transform=fig5.transFigure, fontsize=14)
        plt.text(0.50, 0.69, r'$\Psi = $ wave function scheme', transform=fig5.transFigure, fontsize=14)
        plt.legend(prop={'size': 11}, frameon=False, loc='lower right')
        plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([xmin, xmax])
    plt.ylim([0, 2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

plt.show()