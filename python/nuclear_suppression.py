
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os 

import plotting_functions
import experimental_data

    
plotting_functions.pheno_correction = False

particle = 'jpsi'
# particle = 'upsilon'
plotting_functions.particle = particle
plotting_functions.initialize()

function_of = 'Q2'

reg_scheme_LO = 'decay width'
reg_scheme_NLO = 'NR wave function'
reg_scheme_rel = 'rel wave function'
# NLO_scheme = 'LO(Ydip)'
NLO_scheme = 'squared'

dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/../cpp/output/longitudinal/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/../cpp/output/transverse/'


if particle == 'jpsi':
    alpha_s0 = 0.25
    Mv = 3.0969
    id_string_L = '-jpsi-L-W'
    id_string_T = '-jpsi-T-W'
elif particle == 'upsilon':
    alpha_s0 = 0.18
    Mv = 9.46030
    id_string_L = '-upsilon-L-W'
    id_string_T = '-upsilon-T-W'
else:
    raise Exception('Improper particle!')

Mv2 = Mv**2

Cf = 4/3
# NRQCD_factor = (1-2*Cf*alpha_s0/np.pi)**2

if particle == 'jpsi' and function_of == 'Q2':
    # cs_kcbk_parent_lightq_000_p =    plotting_functions.get_total_cross_section( dir_path_L + r'results-kcbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    # cs_tbk_balsd_lightq_000_p =      plotting_functions.get_total_cross_section( dir_path_L + r'results-tbk-lightq-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    # cs_resumbk_parent_lightq_000_p = plotting_functions.get_total_cross_section( dir_path_L + r'results-resumbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)

    # cs_kcbk_parent_lightq_000_A =    plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-kcbk-lightq-parent-0.00-jpsi-L-W_90.dat',    dir_path_T + r'results-A197-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    # cs_tbk_balsd_lightq_000_A =      plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-L-W_90.dat',     dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    # cs_resumbk_parent_lightq_000_A = plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-resumbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-A197-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)

    # cs_rel_kcbk_parent_lightq_000_p =    plotting_functions.get_total_cross_section( dir_path_L + r'results-kcbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)
    # cs_rel_tbk_balsd_lightq_000_p =      plotting_functions.get_total_cross_section( dir_path_L + r'results-tbk-lightq-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)
    # cs_rel_resumbk_parent_lightq_000_p = plotting_functions.get_total_cross_section( dir_path_L + r'results-resumbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)

    # cs_rel_kcbk_parent_lightq_000_A =    plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-kcbk-lightq-parent-0.00-jpsi-L-W_90.dat',    dir_path_T + r'results-A197-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)
    # cs_rel_tbk_balsd_lightq_000_A =      plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-L-W_90.dat',     dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)
    # cs_rel_resumbk_parent_lightq_000_A = plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-resumbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-A197-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)

    # Longitudinal-only cross sections, Fig. 2 right panel of arXiv:2106.12825 (sigma_L, W=90 GeV, t=0).
    # The paper used KCBK hera bal+sd, Y_{0,BK}=4.61 (2021 config conf-A197-kcbk-hera-bal+sd-4.61.txt, commit f53016e),
    # gold dipoles dipole_kcbk_balsdrc_x0bk0.010000_... and b-grid b<=26 GeV^-1. Reproduces the paper LO (0.72 -> 0.83).
    # TBK gold lines are commented out: the b-dependent code path lacks the target-rapidity shift (b_integral.cpp).
    cs_L_kcbk_hera_balsd_461_p = plotting_functions.get_cross_section_values( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-jpsi-L-W_90_acc3.dat', reg_scheme_NLO, "L", NLO_scheme=NLO_scheme)
    cs_L_kcbk_hera_balsd_461_A = plotting_functions.get_cross_section_values( dir_path_L + r'results-A197-kcbk-hera-bal+sd-4.61-jpsi-L-W_90_acc3.dat', reg_scheme_NLO, "L", NLO_scheme=NLO_scheme)
    cs_L_rel_kcbk_hera_balsd_461_p = plotting_functions.get_cross_section_values( dir_path_L + r'results-kcbk-hera-bal+sd-4.61-jpsi-L-W_90_acc3.dat', reg_scheme_rel, "L", NLO_scheme=NLO_scheme)
    cs_L_rel_kcbk_hera_balsd_461_A = plotting_functions.get_cross_section_values( dir_path_L + r'results-A197-kcbk-hera-bal+sd-4.61-jpsi-L-W_90_acc3.dat', reg_scheme_rel, "L", NLO_scheme=NLO_scheme)

    # cs_L_tbk_parent_lightq_461_p = plotting_functions.get_cross_section_values( dir_path_L + r'results-tbk-lightq-parent-4.61-jpsi-L-W_90.dat', reg_scheme_NLO, "L", NLO_scheme=NLO_scheme)
    # cs_L_tbk_parent_lightq_461_A = plotting_functions.get_cross_section_values( dir_path_L + r'results-A197-tbk-lightq-parent-4.61-jpsi-L-W_90_acc1.dat', reg_scheme_NLO, "L", NLO_scheme=NLO_scheme)
    # cs_L_rel_tbk_parent_lightq_461_p = plotting_functions.get_cross_section_values( dir_path_L + r'results-tbk-lightq-parent-4.61-jpsi-L-W_90.dat', reg_scheme_rel, "L", NLO_scheme=NLO_scheme)
    # cs_L_rel_tbk_parent_lightq_461_A = plotting_functions.get_cross_section_values( dir_path_L + r'results-A197-tbk-lightq-parent-4.61-jpsi-L-W_90_acc1.dat', reg_scheme_rel, "L", NLO_scheme=NLO_scheme)


if particle == 'upsilon' and function_of == 'Q2':
    cs_kcbk_parent_lightq_000_p =    plotting_functions.get_total_cross_section( dir_path_L + r'results-kcbk-lightq-parent-0.00-upsilon-L-W_90.dat',           dir_path_T + r'results-kcbk-lightq-parent-0.00-upsilon-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    cs_tbk_balsd_lightq_000_p =      plotting_functions.get_total_cross_section( dir_path_L + r'results-tbk-lightq-bal+sd-0.00-upsilon-L-W_90.dat',            dir_path_T + r'results-tbk-lightq-bal+sd-0.00-upsilon-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    cs_resumbk_parent_lightq_000_p = plotting_functions.get_total_cross_section( dir_path_L + r'results-resumbk-lightq-parent-0.00-upsilon-L-W_90.dat',        dir_path_T + r'results-resumbk-lightq-parent-0.00-upsilon-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    
    cs_kcbk_parent_lightq_000_A =    plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-kcbk-lightq-parent-0.00-upsilon-L-W_90.dat',    dir_path_T + r'results-A197-kcbk-lightq-parent-0.00-upsilon-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    cs_tbk_balsd_lightq_000_A =      plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-tbk-lightq-bal+sd-0.00-upsilon-L-W_90.dat',     dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00-upsilon-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    cs_resumbk_parent_lightq_000_A = plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-resumbk-lightq-parent-0.00-upsilon-L-W_90.dat', dir_path_T + r'results-A197-resumbk-lightq-parent-0.00-upsilon-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)


if particle == 'jpsi' and function_of == 'W':
    cs_kcbk_parent_lightq_000_p =    plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-lightq-parent-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_tbk_balsd_lightq_000_p =      plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_p = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-lightq-parent-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )

    cs_kcbk_parent_lightq_000_A =    plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-kcbk-lightq-parent-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_tbk_balsd_lightq_000_A =      plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_A = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-resumbk-lightq-parent-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )

    cs_rel_kcbk_parent_lightq_000_p =    plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-lightq-parent-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_rel_tbk_balsd_lightq_000_p =      plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_rel_resumbk_parent_lightq_000_p = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-lightq-parent-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )

    cs_rel_kcbk_parent_lightq_000_A =    plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-kcbk-lightq-parent-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_rel_tbk_balsd_lightq_000_A =      plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_rel_resumbk_parent_lightq_000_A = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-resumbk-lightq-parent-0.00-jpsi-T-Q2_0.01.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )


if particle == 'upsilon' and function_of == 'W':
    cs_kcbk_parent_lightq_000_p =    plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-lightq-parent-0.00-upsilon-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_tbk_balsd_lightq_000_p =      plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-lightq-bal+sd-0.00-upsilon-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_p = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-lightq-parent-0.00-upsilon-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )

    cs_kcbk_parent_lightq_000_A =    plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-kcbk-lightq-parent-0.00-upsilon-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_tbk_balsd_lightq_000_A =      plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00-upsilon-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_A = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-resumbk-lightq-parent-0.00-upsilon-T-Q2_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )



# cs_kcbk_parent_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-kcbk-lightq-parent-0.00' + id_string + '_0.dat', reg_scheme_rel, "T",       NLO_scheme=NLO_scheme )
# cs_tbk_balsd_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-tbk-lightq-bal+sd-0.00' + id_string + '_0.dat', reg_scheme_rel, "T",          NLO_scheme=NLO_scheme )
# cs_resumbk_parent_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-resumbk-lightq-parent-0.00' + id_string + '_0.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )

A = 197


W = 90
C_int = plotting_functions.t_integration_coefficient(W)

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

if function_of == 'Q2' and particle == 'jpsi':
    plots = [15, 18] #plots = [1, 11, 15, 16, 18]
elif function_of == 'Q2' and particle == 'upsilon':
    plots = [1]
elif function_of == 'W':
    plots = [2, 21]

linewidth1 = 1.3*linewidth
linewidth2 = 1.0*linewidth
linewidth3 = 0.7*linewidth


data_sqrt = { 
    'x':            np.array([0.042, 0.029, 0.0011, 4.4e-5, 0.00112, 6.17e-4]),
    'R':            np.array([0.90,  0.74,  0.62,   0.48,   0.62,    0.63]),
    'error_min':    np.array([0.10,  0.07,  0.04,   0.10,   0.057,   0.025]),
    'error_max':    np.array([0.10,  0.07,  0.04,   0.10,   0.057,   0.025])
 }

data = {
    'x': data_sqrt['x'],
    'R': data_sqrt['R']**2,
    'error_min': 2 * data_sqrt['R'] * data_sqrt['error_min'],
    'error_max': 2 * data_sqrt['R'] * data_sqrt['error_max']
}


# legend_lines = [
#                 Line2D([0], [0], color='b', linestyle='None', marker='v'),
#                 Line2D([0], [0], color='r', linestyle='None', marker='o'),
#                 Line2D([0], [0], color='r', linestyle='-', linewidth=linewidth1),
#                 Line2D([0], [0], color='g', linestyle='-', linewidth=linewidth2),
#                 Line2D([0], [0], color='b', linestyle='-', linewidth=linewidth3),
#                 Line2D([0], [0], color='k', linestyle=':', linewidth=linewidth2)
#                 ]

# legend_lines_Y = [
#                 Line2D([0], [0], color='k', linestyle='-', linewidth=linewidth1),
#                 Line2D([0], [0], color='k', linestyle='--', linewidth=linewidth1)
#                 ]

# legend_text =  [
#                 r'H1',
#                 r'ZEUS',
#                 r'NLO KCBK',
#                 r'NLO TBK',
#                 r'NLO ResumBK',
#                 r'LO LOBK'
#                 ]

# legend_text_rel =  [
#                     r'H1',
#                     r'ZEUS',
#                     r'NLO+rel KCBK',
#                     r'NLO+rel TBK',
#                     r'NLO+rel ResumBK',
#                     r'LO+rel LOBK'
#                     ]

# legend_text_Y = [ r'$Y_{0,\mathrm{BK}},\eta_{0,\mathrm{BK}}=4.61$',
#                   r'$Y_{0,\mathrm{BK}},\eta_{0,\mathrm{BK}}=0.00$']

if 1 in plots:
    fig1=plt.figure(1)
    plt.plot(Mv2 + cs_kcbk_parent_lightq_000_p[1],    1/A**2 * cs_kcbk_parent_lightq_000_A[3]/cs_kcbk_parent_lightq_000_p[3], 'r-',label=r'NLO KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_resumbk_parent_lightq_000_p[1], 1/A**2 * cs_resumbk_parent_lightq_000_A[3]/cs_resumbk_parent_lightq_000_p[3], 'b-.',label=r'NLO ResumBK parent 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_tbk_balsd_lightq_000_p[1],      1/A**2 * cs_tbk_balsd_lightq_000_A[3]/cs_tbk_balsd_lightq_000_p[3], '--' ,color='tab:green',label=r'NLO TBK bal+sd 0.00', linewidth=linewidth1)
    # plt.plot(Mv2 + cs_lobk_mve[1], cs_lobk_mve[6], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth2)
    plt.legend(prop={'size': 15}, frameon=False)
    if particle == 'jpsi':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow J/\psi+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow J/\psi+p})$', fontsize=17)
        plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    elif particle == 'upsilon':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow \Upsilon+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow \Upsilon+p})$', fontsize=17)
        plt.xlabel(r'$M_{\Upsilon}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0, 1])
    # plt.ylim([0, 0.5])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.text(0.15, 0.75, r'$W = 90\textrm{ GeV}$', transform=fig1.transFigure, fontsize=20)
    plt.text(0.15, 0.65, r'$t = 0$', transform=fig1.transFigure, fontsize=20)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 11 in plots:
    fig11=plt.figure(11)
    plt.plot(Mv2 + cs_kcbk_parent_lightq_000_p[1],    1/A**2 * cs_kcbk_parent_lightq_000_A[5]/cs_kcbk_parent_lightq_000_p[5], 'r-',label=r'NLO KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_resumbk_parent_lightq_000_p[1], 1/A**2 * cs_resumbk_parent_lightq_000_A[5]/cs_resumbk_parent_lightq_000_p[5], 'b-.',label=r'NLO ResumBK parent 0.00', linewidth=linewidth1)
    plt.plot(Mv2 + cs_tbk_balsd_lightq_000_p[1],      1/A**2 * cs_tbk_balsd_lightq_000_A[5]/cs_tbk_balsd_lightq_000_p[5], '--' ,color='tab:green',label=r'NLO TBK bal+sd 0.00', linewidth=linewidth1)
    # plt.plot(Mv2 + cs_lobk_mve[1], cs_lobk_mve[6], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth2)
    plt.legend(prop={'size': 15}, frameon=False)
    if particle == 'jpsi':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow J/\psi+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow J/\psi+p})$', fontsize=17)
        plt.xlabel(r'$M_{J/\psi}^2+Q^2$ [GeV$^2$]', fontsize=15)
    elif particle == 'upsilon':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow \Upsilon+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow \Upsilon+p})$', fontsize=17)
        plt.xlabel(r'$M_{\Upsilon}^2+Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Mv2, 1e2])
    plt.ylim([0, 1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.text(0.15, 0.75, r'$W = 90\textrm{ GeV}$', transform=fig11.transFigure, fontsize=20)
    plt.text(0.15, 0.65, r'$t = 0$', transform=fig11.transFigure, fontsize=20)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

# test R Fig.2 in 2106.12825

if 15 in plots:
    fig15 = plt.figure(15, figsize=(8, 7.5))
    fits = [
        ('KCBK hera-bal+sd 4.61', 'r', cs_L_kcbk_hera_balsd_461_p, cs_L_kcbk_hera_balsd_461_A, cs_L_rel_kcbk_hera_balsd_461_p, cs_L_rel_kcbk_hera_balsd_461_A),
        #('TBK lightq-parent 4.61', 'g', cs_L_tbk_parent_lightq_461_p, cs_L_tbk_parent_lightq_461_A, cs_L_rel_tbk_parent_lightq_461_p, cs_L_rel_tbk_parent_lightq_461_A),
    ]
    for label, color, cs_p, cs_A, cs_rel_p, cs_rel_A in fits:
        Q2v = cs_p[1]
        R_LO      = 1/A**2 * cs_A[2]/cs_p[2]
        R_LO_rel  = 1/A**2 * cs_rel_A[4]/cs_rel_p[4]
        R_NLO     = 1/A**2 * cs_A[3]/cs_p[3]
        R_NLO_rel = 1/A**2 * cs_rel_A[5]/cs_rel_p[5]
        plt.plot(Q2v, R_LO,      color='b', linestyle='-',  label=r'LO',      linewidth=linewidth2)
        plt.plot(Q2v, R_LO_rel,  color='b', linestyle='--', label=r'LO+rel',  linewidth=linewidth2)
        plt.plot(Q2v, R_NLO,     color='r', linestyle='-',  label=r'NLO',     linewidth=linewidth1)
        plt.plot(Q2v, R_NLO_rel, color='r', linestyle='--', label=r'NLO+rel', linewidth=linewidth1)
    plt.legend(prop={'size': 15}, frameon=False, ncol=4, loc='upper center', bbox_to_anchor=(0.5, -0.11))
    if particle == 'jpsi':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow J/\psi+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow J/\psi+p})$, $Y_0=4.61$', fontsize=13)
    elif particle == 'upsilon':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow \Upsilon+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow \Upsilon+p})$, $Y_0=4.61$', fontsize=13)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0.1, 100])
    plt.ylim([0.71, 1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.text(0.97, 0.03, r'$W = 90\textrm{ GeV}$, $t = 0$', transform=plt.gca().transAxes, fontsize=17, ha='right', va='bottom')
    scheme_names = {'decay width': 'decay width', 'NR wave function': 'NR wave function', 'rel wave function': 'rel.~wave function'}
    NLO_scheme_names = {'LO(Ydip)': r'linearized, $\sigma \propto \mathcal{A}_\textrm{LO}^2 + 2\mathcal{A}_\textrm{LO}(\mathcal{A}_\textrm{NLO}-\mathcal{A}_\textrm{LO})$',
                        'squared': r'squared, $\sigma \propto \mathcal{A}_\textrm{NLO}^2$',
                        'LO(Y0)+BK': r'linearized around LO$(Y_0)$+BK'}
    plt.text(0.03, 0.97,
             r'KCBK hera bal+sd, $Y_{0,\textrm{BK}}=4.61$, Au ($A=197$)' '\n'
             r'one-loop $q\bar q$ term: ' + scheme_names[reg_scheme_NLO] + r' (NLO), ' + scheme_names[reg_scheme_rel] + r' (+rel)' '\n'
             r'NLO cross section: ' + NLO_scheme_names[NLO_scheme],
             transform=plt.gca().transAxes, fontsize=11, ha='left', va='top', color='k', linespacing=1.6)
    plt.xscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)
    scheme_tags = {'decay width': 'dw', 'NR wave function': 'NRwf', 'rel wave function': 'relwf'}
    NLO_scheme_tags = {'LO(Ydip)': 'linearized', 'squared': 'squared', 'LO(Y0)+BK': 'linearized-LOY0BK'}
    fig15.savefig(os.path.dirname(os.path.realpath(__file__)) + r'/../figures/nuclear_suppression_L_Q2_W90_kcbk-hera-balsd-4.61_'
                  + scheme_tags[reg_scheme_NLO] + '-' + NLO_scheme_tags[NLO_scheme] + '.pdf', bbox_inches='tight')


if 16 in plots:
    fig16 = plt.figure(16, figsize=(8, 7.5))
    fits_000 = [
        ('KCBK parent 0.00',    'r', cs_kcbk_parent_lightq_000_p,    cs_kcbk_parent_lightq_000_A,    cs_rel_kcbk_parent_lightq_000_p,    cs_rel_kcbk_parent_lightq_000_A),
        ('ResumBK parent 0.00', 'b', cs_resumbk_parent_lightq_000_p, cs_resumbk_parent_lightq_000_A, cs_rel_resumbk_parent_lightq_000_p, cs_rel_resumbk_parent_lightq_000_A),
        ('TBK bal+sd 0.00',     'g', cs_tbk_balsd_lightq_000_p,      cs_tbk_balsd_lightq_000_A,      cs_rel_tbk_balsd_lightq_000_p,      cs_rel_tbk_balsd_lightq_000_A),
    ]
    for label, color, cs_p, cs_A, cs_rel_p, cs_rel_A in fits_000:
        Q2v = cs_p[1]
        R_LO      = 1/A**2 * cs_A[2]/cs_p[2]
        R_LO_rel  = 1/A**2 * cs_rel_A[4]/cs_rel_p[4]
        R_NLO     = 1/A**2 * cs_A[3]/cs_p[3]
        R_NLO_rel = 1/A**2 * cs_rel_A[5]/cs_rel_p[5]
        plt.plot(Q2v, R_LO,      color=color, linestyle=':',  label=label+' LO',      linewidth=linewidth2)
        plt.plot(Q2v, R_LO_rel,  color=color, linestyle='-.', label=label+' LO+rel',  linewidth=linewidth2)
        plt.plot(Q2v, R_NLO,     color=color, linestyle='-',  label=label+' NLO',     linewidth=linewidth2)
        plt.plot(Q2v, R_NLO_rel, color=color, linestyle='--', label=label+' NLO+rel', linewidth=linewidth2)
    plt.legend(prop={'size': 10}, frameon=False, ncol=3, loc='upper center', bbox_to_anchor=(0.5, -0.13))
    if particle == 'jpsi':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow J/\psi+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow J/\psi+p})$, $Y_0=0.00$', fontsize=13)
    elif particle == 'upsilon':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow \Upsilon+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow \Upsilon+p})$, $Y_0=0.00$', fontsize=13)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([Q2v.min(), Q2v.max()])
    plt.ylim([0.71, 0.84])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.text(0.65, 0.85, r'$W = 90\textrm{ GeV}$', transform=fig16.transFigure, fontsize=20)
    plt.text(0.65, 0.78, r'$t = 0$', transform=fig16.transFigure, fontsize=20)
    plt.xscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)
    fig16.savefig(os.path.dirname(os.path.realpath(__file__)) + r'/../figures/nuclear_suppression_Q2_fit_comparison_Y0.pdf', bbox_inches='tight')


if 2 in plots:
    fig2=plt.figure(2)
    plt.plot(cs_kcbk_parent_lightq_000_p[0],    1/A**2 * cs_kcbk_parent_lightq_000_A[3]/cs_kcbk_parent_lightq_000_p[3], 'r-',label=r'NLO KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(cs_resumbk_parent_lightq_000_p[0], 1/A**2 * cs_resumbk_parent_lightq_000_A[3]/cs_resumbk_parent_lightq_000_p[3], 'b-.',label=r'NLO ResumBK parent 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_balsd_lightq_000_p[0],      1/A**2 * cs_tbk_balsd_lightq_000_A[3]/cs_tbk_balsd_lightq_000_p[3], '--' ,color='tab:green',label=r'NLO TBK bal+sd 0.00', linewidth=linewidth1)
    # plt.plot(Mv2 + cs_lobk_mve[1], cs_lobk_mve[6], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth2)
    plt.legend(prop={'size': 15}, frameon=False)
    if particle == 'jpsi':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow J/\psi+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow J/\psi+p})$', fontsize=17)
    elif particle == 'upsilon':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow \Upsilon+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow \Upsilon+p})$', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([30, 3e3])
    plt.ylim([0, 1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.text(0.15, 0.75, r'$Q^2 = 0$', transform=fig2.transFigure, fontsize=20)
    plt.text(0.15, 0.65, r'$t = 0$', transform=fig2.transFigure, fontsize=20)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 21 in plots:
    fig21=plt.figure(21)
    plt.plot(Mv**2/cs_kcbk_parent_lightq_000_p[0]**2,    1/A**2 * cs_kcbk_parent_lightq_000_A[3]/cs_kcbk_parent_lightq_000_p[3], 'r-',label=r'NLO KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(Mv**2/cs_resumbk_parent_lightq_000_p[0]**2, 1/A**2 * cs_resumbk_parent_lightq_000_A[3]/cs_resumbk_parent_lightq_000_p[3], 'b-.',label=r'NLO ResumBK parent 0.00', linewidth=linewidth1)
    plt.plot(Mv**2/cs_tbk_balsd_lightq_000_p[0]**2,      1/A**2 * cs_tbk_balsd_lightq_000_A[3]/cs_tbk_balsd_lightq_000_p[3], '--' ,color='tab:green',label=r'NLO TBK bal+sd 0.00', linewidth=linewidth1)
    # plt.plot(Mv2 + cs_lobk_mve[1], cs_lobk_mve[6], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth2)
    if particle == 'jpsi':
        plt.errorbar(data['x'], data['R'],         yerr=[data['error_min'],data['error_max']],label='Data', fmt='ok', capsize=3)
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow J/\psi+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow J/\psi+p})$', fontsize=17)
    elif particle == 'upsilon':
        plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + A \rightarrow \Upsilon+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma^{\gamma^* + p \rightarrow \Upsilon+p})$', fontsize=17)
    plt.xlabel(r'$x$', fontsize=15)
    plt.legend(prop={'size': 15}, frameon=False, loc='upper left')
    plt.xlim([Mv**2/9e6, Mv**2/30**2])
    plt.ylim([0, 1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.text(0.75, 0.75, r'$Q^2 = 0$', transform=fig21.transFigure, fontsize=20)
    plt.text(0.75, 0.65, r'$t = 0$', transform=fig21.transFigure, fontsize=20)
    plt.xscale('log')
    # plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 18 in plots:
    # Reproduction of arXiv:2106.12825 Fig. 2 right with the 2021 plotting scheme (python/plotting_functions.py at commit f53016e,
    # bool_decay_width=True): decay-width one-loop qq column, LO+rel = (LO+rel)^2, NLO = LO^2 + 2 LO (NLO-LO),
    # NLO+rel = (LO+rel)^2 + 2 (LO+rel)(NLO-LO). The last one is not a scheme in calculate_cross_section_L, so it is
    # built here from the LO, linearized NLO and squared LO+rel cross sections (overall factors cancel in the ratio).
    f_p = dir_path_L + r'results-kcbk-hera-bal+sd-4.61-jpsi-L-W_90_acc3.dat'
    f_A = dir_path_L + r'results-A197-kcbk-hera-bal+sd-4.61-jpsi-L-W_90_acc3.dat'
    def paper_cs(f):
        lin = plotting_functions.get_cross_section_values(f, 'decay width', "L", NLO_scheme='LO(Ydip)')
        sq  = plotting_functions.get_cross_section_values(f, 'decay width', "L", NLO_scheme='squared')
        LO, NLO, LO_rel = lin[2], lin[3], sq[4]
        NLO_rel = LO_rel + (NLO - LO) * np.sqrt(LO_rel / LO)
        return lin[1], LO, LO_rel, NLO, NLO_rel
    Q2v, *cs_p = paper_cs(f_p)
    _,   *cs_A = paper_cs(f_A)
    R = [1/A**2 * a/p for a, p in zip(cs_A, cs_p)]

    fig18 = plt.figure(18, figsize=(8, 7.5))
    plt.plot(Q2v, R[0], 'b-',  label=r'LO',      linewidth=linewidth2)
    plt.plot(Q2v, R[1], 'b--', label=r'LO+rel',  linewidth=linewidth2)
    plt.plot(Q2v, R[2], 'r-',  label=r'NLO',     linewidth=linewidth1)
    plt.plot(Q2v, R[3], 'r--', label=r'NLO+rel', linewidth=linewidth1)
    plt.legend(prop={'size': 15}, frameon=False, ncol=4, loc='upper center', bbox_to_anchor=(0.5, -0.11))
    plt.title(r'Nuclear suppression $\frac{\textrm{d}}{\textrm{d}t} \sigma_L^{\gamma^* + A \rightarrow J/\psi+A} / (A^2 \frac{\textrm{d}}{\textrm{d}t} \sigma_L^{\gamma^* + p \rightarrow J/\psi+p})$', fontsize=15)
    plt.xlabel(r'$Q^2$ [GeV$^2$]', fontsize=15)
    plt.xlim([0.1, 100])
    plt.ylim([0.712, 0.842])  # same range as Fig. 2 (right) of arXiv:2106.12825
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.text(0.97, 0.03, r'$W = 90\textrm{ GeV}$, $t = 0$', transform=plt.gca().transAxes, fontsize=17, ha='right', va='bottom')
    plt.text(0.03, 0.97,
             r'Reproduction of arXiv:2106.12825, Fig.~2 (right)' '\n'
             r'KCBK hera bal+sd, $Y_{0,\textrm{BK}}=4.61$, Au ($A=197$)' '\n'
             r'Scheme: decay-width one-loop $q\bar q$ term,' '\n'
             r'linearized NLO $\sigma \propto \mathcal{A}_\textrm{LO}^2 + 2\mathcal{A}_\textrm{LO}(\mathcal{A}_\textrm{NLO}-\mathcal{A}_\textrm{LO})$',
             transform=plt.gca().transAxes, fontsize=11, ha='left', va='top', color='k', linespacing=1.6)
    plt.xscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)
    fig18.savefig(os.path.dirname(os.path.realpath(__file__)) + r'/../figures/nuclear_suppression_L_Q2_W90_kcbk-hera-balsd-4.61_dw-linearized_arXiv2106.12825.pdf', bbox_inches='tight')



#plt.show()