
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os 

import plotting_functions
import experimental_data

    
plots = [3,4,5,6]

plotting_functions.pheno_correction = False

particle = 'jpsi'
plotting_functions.particle = particle
plotting_functions.initialize()

BKeq = 'resumbk'
Y0 = '0.00'

dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'

cs_nlo_LOYdip    = plotting_functions.get_cross_section_values(    dir_path_T + r'results-' + BKeq + r'-hera-bal+sd-' + Y0 + r'-jpsi-T-W.dat', 'decay width', 'T', NLO_scheme='LO(Ydip)')
cs_nlo_sq        = plotting_functions.get_cross_section_values(    dir_path_T + r'results-' + BKeq + r'-hera-bal+sd-' + Y0 + r'-jpsi-T-W.dat', 'decay width', 'T', NLO_scheme='squared')
cs_nlo_LO0_BK    = plotting_functions.get_cross_section_values(    dir_path_T + r'results-' + BKeq + r'-hera-bal+sd-' + Y0 + r'-jpsi-T-W.dat', 'decay width', 'T', NLO_scheme='LO(Y0)+BK')
cs_nlo_LO0_BK    = plotting_functions.get_cross_section_values(    dir_path_T + r'results-' + BKeq + r'-hera-bal+sd-' + Y0 + r'-jpsi-T-W.dat', 'decay width', 'T', NLO_scheme='LO(Y0)+BK')
cs_lo            = plotting_functions.get_cross_section_values(    dir_path_T + r'results-LOBK-MVe-jpsi-T-W.dat', 'decay width', 'T', NLO_scheme='LO(Y0)+BK')


cs_nlo_LOYdip_W    = plotting_functions.get_cross_section_values(    dir_path_T + r'results-' + BKeq +  r'-hera-bal+sd-' + Y0 + r'-jpsi-T-Q2.dat', 'decay width', 'T', NLO_scheme='LO(Ydip)')
cs_nlo_sq_W        = plotting_functions.get_cross_section_values(    dir_path_T + r'results-' + BKeq +  r'-hera-bal+sd-' + Y0 + r'-jpsi-T-Q2.dat', 'decay width', 'T', NLO_scheme='squared')
cs_nlo_LO0_BK_W    = plotting_functions.get_cross_section_values(    dir_path_T + r'results-' + BKeq +  r'-hera-bal+sd-' + Y0 + r'-jpsi-T-Q2.dat', 'decay width', 'T', NLO_scheme='LO(Y0)+BK')
cs_nlo_LO0_BK_W    = plotting_functions.get_cross_section_values(    dir_path_T + r'results-' + BKeq +  r'-hera-bal+sd-' + Y0 + r'-jpsi-T-Q2.dat', 'decay width', 'T', NLO_scheme='LO(Y0)+BK')
cs_lo_W            = plotting_functions.get_cross_section_values(    dir_path_T + r'results-LOBK-MVe-jpsi-T-Q2.dat', 'decay width', 'T', NLO_scheme='LO(Y0)+BK')



linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

linewidth1 = 1.3*linewidth
linewidth2 = 1.0*linewidth
linewidth3 = 0.7*linewidth




if 3 in plots:
    plt.figure(3)
    plt.plot(cs_nlo_LOYdip[1], cs_nlo_LOYdip[3], 'b-', label=r'NLO result, LO=LO(Ydip)', linewidth=linewidth1)
    plt.plot(cs_nlo_LO0_BK[1], cs_nlo_LO0_BK[3], 'r-.', label=r'NLO result, LO=LO(Y0)+BK', linewidth=linewidth1)
    plt.plot(cs_nlo_sq[1],     cs_nlo_sq[3], 'g:', label=r'NLO result, keep $\alpha_s^2$ term', linewidth=linewidth1)
    plt.plot(cs_lo[1],         cs_lo[6], 'k--', label=r'LO', linewidth=linewidth1)
    plt.legend( loc='upper left', frameon=False, prop={'size': 17} )
    plt.title(r'$\sigma_T(\gamma^* + p \rightarrow J/\psi + p)$ [nb]', fontsize=20)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.ylim([1e-2, 5e2 ])

    plt.xlim([0.1, 1e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)




if 4 in plots:
    plt.figure(4)
    plt.plot(cs_nlo_LOYdip[1], cs_nlo_LOYdip[3]/cs_nlo_LOYdip[3], 'b-', label=r'NLO result, LO=LO(Ydip)', linewidth=linewidth1)
    plt.plot(cs_nlo_LO0_BK[1], cs_nlo_LO0_BK[3]/cs_nlo_LOYdip[3], 'r-.', label=r'NLO result, LO=LO(Y0)+BK', linewidth=linewidth1)
    plt.plot(cs_nlo_sq[1], cs_nlo_sq[3]/cs_nlo_LOYdip[3], 'g:', label=r'NLO result, keep $\alpha_s^2$ term', linewidth=linewidth1)
    plt.legend( loc='upper left', frameon=False, prop={'size': 17} )
    plt.title(r'$\sigma_T/\sigma_T(\textrm{LO}=\textrm{LO}(Y_\textrm{dip}))$', fontsize=20)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=20)
    plt.ylim([0, 2])

    plt.xlim([0.1, 100])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)




if 5 in plots:
    plt.figure(5)
    plt.plot(cs_nlo_LOYdip_W[0], cs_nlo_LOYdip_W[3], 'b-', label=r'NLO result, LO=LO(Ydip)', linewidth=linewidth1)
    plt.plot(cs_nlo_LO0_BK_W[0], cs_nlo_LO0_BK_W[3], 'r-.', label=r'NLO result, LO=LO(Y0)+BK', linewidth=linewidth1)
    plt.plot(cs_nlo_sq_W[0],     cs_nlo_sq_W[3], 'g:', label=r'NLO result, keep $\alpha_s^2$ term', linewidth=linewidth1)
    plt.plot(cs_lo_W[0],         cs_lo_W[6], 'k--', label=r'LO', linewidth=linewidth1)
    plt.legend( loc='upper left', frameon=False, prop={'size': 17} )
    plt.title(r'$\sigma_T(\gamma^* + p \rightarrow J/\psi + p)$ [nb]', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.ylim([1e2, 1e5 ])

    plt.xlim([30, 1e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)




if 6 in plots:
    plt.figure(6)
    plt.plot(cs_nlo_LOYdip_W[0], cs_nlo_LOYdip_W[3]/cs_nlo_LOYdip_W[3], 'b-', label=r'NLO result, LO=LO(Ydip)', linewidth=linewidth1)
    plt.plot(cs_nlo_LO0_BK_W[0], cs_nlo_LO0_BK_W[3]/cs_nlo_LOYdip_W[3], 'r-.', label=r'NLO result, LO=LO(Y0)+BK', linewidth=linewidth1)
    plt.plot(cs_nlo_sq_W[0], cs_nlo_sq_W[3]/cs_nlo_LOYdip_W[3], 'g:', label=r'NLO result, keep $\alpha_s^2$ term', linewidth=linewidth1)
    plt.legend( loc='upper left', frameon=False, prop={'size': 17} )
    plt.title(r'$\sigma_T/\sigma_T(\textrm{LO}=\textrm{LO}(Y_\textrm{dip}))$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylim([0, 2])

    plt.xlim([30, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)





plt.show()