
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

dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_L/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'


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
    cs_kcbk_parent_lightq_000_p =    plotting_functions.get_total_cross_section( dir_path_L + r'results-kcbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    cs_tbk_balsd_lightq_000_p =      plotting_functions.get_total_cross_section( dir_path_L + r'results-tbk-lightq-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    cs_resumbk_parent_lightq_000_p = plotting_functions.get_total_cross_section( dir_path_L + r'results-resumbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)

    cs_kcbk_parent_lightq_000_A =    plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-kcbk-lightq-parent-0.00-jpsi-L-W_90.dat',    dir_path_T + r'results-A197-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    cs_tbk_balsd_lightq_000_A =      plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-L-W_90.dat',     dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)
    cs_resumbk_parent_lightq_000_A = plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-resumbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-A197-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_NLO, NLO_scheme=NLO_scheme)

    cs_rel_kcbk_parent_lightq_000_p =    plotting_functions.get_total_cross_section( dir_path_L + r'results-kcbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)
    cs_rel_tbk_balsd_lightq_000_p =      plotting_functions.get_total_cross_section( dir_path_L + r'results-tbk-lightq-bal+sd-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)
    cs_rel_resumbk_parent_lightq_000_p = plotting_functions.get_total_cross_section( dir_path_L + r'results-resumbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)

    cs_rel_kcbk_parent_lightq_000_A =    plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-kcbk-lightq-parent-0.00-jpsi-L-W_90.dat',    dir_path_T + r'results-A197-kcbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)
    cs_rel_tbk_balsd_lightq_000_A =      plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-L-W_90.dat',     dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)
    cs_rel_resumbk_parent_lightq_000_A = plotting_functions.get_total_cross_section( dir_path_L + r'results-A197-resumbk-lightq-parent-0.00-jpsi-L-W_90.dat', dir_path_T + r'results-A197-resumbk-lightq-parent-0.00-jpsi-T-W_90.dat', reg_scheme_rel, NLO_scheme=NLO_scheme)


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
    plots = [1, 11]
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



plt.show()