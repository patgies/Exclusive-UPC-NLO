
from matplotlib.markers import MarkerStyle
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
from scipy import special
import os 

import plotting_functions
import experimental_data


# plotting_functions.pheno_correction = True
plotting_functions.pheno_correction = False

particle = 'jpsi'
# particle = 'upsilon'
plotting_functions.particle = particle
plotting_functions.initialize()

reg_scheme_LO = 'decay width'
# reg_scheme_NLO = 'decay width'
reg_scheme_NLO = 'NR wave function'
reg_scheme_rel = 'rel wave function'
# NLO_scheme='squared'
NLO_scheme='LO(Ydip)'



if particle == 'jpsi':
    plots = [3,4,16, 301, 401]
    # plots = [302, 402, 502]
elif particle == 'upsilon':
    # plots = [14]
    plots = [303, 503]



if particle == 'jpsi':
    id_string = '-jpsi-T-Q2'
    # id_string = "_Q2_0.05" 
    # id_string = "_Q2_0.05-m_1.4" 
elif particle == 'upsilon':
    id_string = '-upsilon-T-Q2'
    # id_string = '-upsilon-T-Q2_0.01_high-W'

dir_path_L = os.path.dirname(os.path.realpath(__file__)) + r'/../cpp/output/longitudinal/'
dir_path_T = os.path.dirname(os.path.realpath(__file__)) + r'/../cpp/output/transverse/'

# cs_kcbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-kcbk-hera-bal+sd-0.00.dat', reg_scheme, "L" )
# cs_kcbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-kcbk-hera-bal+sd-4.61.dat', reg_scheme, "L" )
# cs_tbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-tbk-hera-bal+sd-0.00.dat', reg_scheme, "L"  )
# cs_tbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-tbk-hera-bal+sd-4.61.dat', reg_scheme, "L"  )
# cs_resumbk_000_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-resumbk-hera-bal+sd-0.00.dat', reg_scheme, "L"  )
# cs_resumbk_461_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-resumbk-hera-bal+sd-4.61.dat', reg_scheme, "L"  )

# # cs_ipsat_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-IP_SAT_m1.4.dat', reg_scheme )
# cs_lobk_mve_L = plotting_functions.get_cross_section_values_W( dir_path_L + r'results-LOBK-MVe.dat', reg_scheme, "L"  )

# cs_lobk_mve_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-LOBK-MVe.dat', reg_scheme_rel, "L"  )
# cs_kcbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-kcbk-hera-bal+sd-4.61.dat', reg_scheme_rel, "L"  )
# cs_tbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-tbk-hera-bal+sd-4.61.dat', reg_scheme_rel, "L"  )
# cs_resumbk_461_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-resumbk-hera-bal+sd-4.61.dat', reg_scheme_rel, "L"  )
# cs_kcbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-kcbk-hera-bal+sd-0.00.dat', reg_scheme_rel, "L"  )
# cs_tbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-tbk-hera-bal+sd-0.00.dat', reg_scheme_rel, "L"  )
# cs_resumbk_000_rel_L = plotting_functions.get_distribution_W( dir_path_L + r'results-resumbk-hera-bal+sd-0.00.dat', reg_scheme_rel, "L"  )


cs_kcbk_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_NLO, "T" )
cs_kcbk_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_NLO, "T" )
cs_tbk_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_NLO, "T" )
cs_tbk_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_NLO, "T" )
cs_resumbk_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_NLO, "T" )
cs_resumbk_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_NLO, "T" )

cs_lobk_mve_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-LOBK-MVe' + id_string + '.dat', reg_scheme_LO, "T" )

cs_lobk_mve_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-LOBK-MVe' + id_string + '.dat', reg_scheme_rel, "T" )
cs_kcbk_461_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-kcbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_rel, "T" )
cs_kcbk_000_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-kcbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_rel, "T" )
cs_tbk_461_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-tbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_rel, "T" )
cs_tbk_000_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-tbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_rel, "T" )
cs_resumbk_461_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-resumbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_rel, "T" )
cs_resumbk_000_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-resumbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_rel, "T" )



if particle == 'jpsi':
    cs_kcbk_parent_lightq_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-lightq-parent-4.61' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_kcbk_parent_lightq_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-lightq-parent-0.00' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_tbk_parent_lightq_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-lightq-parent-4.61' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_tbk_parent_lightq_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-lightq-parent-0.00' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-lightq-parent-4.61' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-lightq-parent-0.00' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )

    cs_kcbk_parent_lightq_461_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-kcbk-lightq-parent-4.61' + id_string + '.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_kcbk_parent_lightq_000_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-kcbk-lightq-parent-0.00' + id_string + '.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_tbk_parent_lightq_461_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-tbk-lightq-parent-4.61' + id_string + '.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_tbk_parent_lightq_000_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-tbk-lightq-parent-0.00' + id_string + '.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_461_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-resumbk-lightq-parent-4.61' + id_string + '.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_rel_T = plotting_functions.get_distribution( dir_path_T + r'results-resumbk-lightq-parent-0.00' + id_string + '.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )


    cs_ampsq_kcbk_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme='squared' )
    cs_ampsq_kcbk_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme='squared' )
    cs_ampsq_tbk_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme='squared' )
    cs_ampsq_tbk_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme='squared' )
    cs_ampsq_resumbk_000_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-hera-bal+sd-0.00' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme='squared' )
    cs_ampsq_resumbk_461_T = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-hera-bal+sd-4.61' + id_string + '.dat', reg_scheme_NLO, "T", NLO_scheme='squared' )

    cs_kcbk_parent_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T",       NLO_scheme=NLO_scheme )
    cs_tbk_balsd_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-lightq-bal+sd-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T",          NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-lightq-parent-0.00' + id_string + '_0.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )

    cs_A197_kcbk_parent_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-kcbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T",       NLO_scheme=NLO_scheme )
    cs_A197_tbk_balsd_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T",          NLO_scheme=NLO_scheme )
    cs_A197_resumbk_parent_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-resumbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )

    cs_kcbk_parent_461_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-hera-parent-4.61' + id_string + '_0.01.dat', reg_scheme_NLO, "T",       NLO_scheme=NLO_scheme )
    

    cs_kcbk_parent_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-kcbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_rel, "T",       NLO_scheme=NLO_scheme )
    cs_tbk_balsd_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-tbk-lightq-bal+sd-0.00' + id_string + '_0.01.dat', reg_scheme_rel, "T",          NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-resumbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )

if particle == 'upsilon':
    cs_kcbk_parent_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-kcbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T",       NLO_scheme=NLO_scheme )
    cs_tbk_balsd_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-tbk-lightq-bal+sd-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T",          NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-resumbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )

    cs_A197_kcbk_parent_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-kcbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T",       NLO_scheme=NLO_scheme )
    cs_A197_tbk_balsd_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-tbk-lightq-bal+sd-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T",          NLO_scheme=NLO_scheme )
    cs_A197_resumbk_parent_lightq_000_T_Q0 = plotting_functions.get_cross_section_values( dir_path_T + r'results-A197-resumbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_NLO, "T", NLO_scheme=NLO_scheme )


    cs_kcbk_parent_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-kcbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_rel, "T",       NLO_scheme=NLO_scheme )
    cs_tbk_balsd_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-tbk-lightq-bal+sd-0.00' + id_string + '_0.01.dat', reg_scheme_rel, "T",          NLO_scheme=NLO_scheme )
    cs_resumbk_parent_lightq_000_T_Q0_rel = plotting_functions.get_distribution( dir_path_T + r'results-resumbk-lightq-parent-0.00' + id_string + '_0.01.dat', reg_scheme_rel, "T", NLO_scheme=NLO_scheme )




if particle == 'jpsi':
    alpha_s0 = 0.25
elif particle == 'upsilon':
    alpha_s0 = 0.18
else:
    raise Exception('Improper particle!')

Cf = 4/3
NRQCD_factor = (1-2*Cf*alpha_s0/np.pi)**2

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

sigma_tot_ZEUS_W, sigma_tot_ZEUS_data = experimental_data.sigma_tot_W_ZEUS()
sigma_tot_H1_v1_W, sigma_tot_H1_v1_data, _     = experimental_data.sigma_tot_W_H1_v1()
sigma_tot_H1_v2_W, sigma_tot_H1_v2_data     = experimental_data.sigma_tot_W_H1_v2()
sigma_tot_ALICE_v1_W, sigma_tot_ALICE_v1_data     = experimental_data.sigma_tot_W_ALICE_v1()
sigma_tot_ALICE_v2_W, sigma_tot_ALICE_v2_data     = experimental_data.sigma_tot_W_ALICE_v2()
sigma_tot_ALICE_v3_W, sigma_tot_ALICE_v3_data     = experimental_data.sigma_tot_W_ALICE_v3()
sigma_tot_LHCb7_W, sigma_tot_LHCb7_data     = experimental_data.sigma_tot_LHCb_7()
sigma_tot_LHCb13_W, sigma_tot_LHCb13_data     = experimental_data.sigma_tot_LHCb_13()

sigma_tot_H1_upsilon, sigma_tot_H1_upsilon_data = experimental_data.sigma_tot_Upsilon_H1()
sigma_tot_ZEUS_v1_upsilon, sigma_tot_ZEUS_v1_upsilon_data = experimental_data.sigma_tot_Upsilon_ZEUS_v1()
sigma_tot_ZEUS_v2_upsilon, sigma_tot_ZEUS_v2_upsilon_data = experimental_data.sigma_tot_Upsilon_ZEUS_v2()
sigma_tot_CMS_upsilon, sigma_tot_CMS_upsilon_data = experimental_data.sigma_tot_Upsilon_CMS()
sigma_tot_LHCb_upsilon, sigma_tot_LHCb_upsilon_data     = experimental_data.sigma_tot_Upsilon_LHCb()

if particle == 'jpsi':
    W = cs_kcbk_000_T[0]
if particle == 'upsilon':
    W = cs_kcbk_parent_lightq_000_T_Q0[0]
C_int = plotting_functions.t_integration_coefficient(W) 
C_int_Au = 1/197**(2/3)*C_int # A very rough estimate!

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

linewidth1 = 1.3*linewidth
linewidth2 = 1.0*linewidth
linewidth3 = 0.7*linewidth



legend_lines = [Line2D([0], [0], color='r', linestyle='-', linewidth=linewidth1),
                Line2D([0], [0], color='g', linestyle='-', linewidth=linewidth2),
                Line2D([0], [0], color='b', linestyle='-', linewidth=linewidth3),
                Line2D([0], [0], color='k', linestyle=':', linewidth=linewidth2),
                Line2D([0], [0], color='b', linestyle='None', marker='v'),
                Line2D([0], [0], color='r', linestyle='None', marker='o'),
                Line2D([0], [0], color='g', linestyle='None', marker='s'),
                Line2D([0], [0], color='m', linestyle='None', marker='*', markersize=10),
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
                r'ZEUS',
                r'ALICE',
                r'LHCb'
                ]

legend_text_rel =  [r'NLO+rel KCBK',
                    r'NLO+rel TBK',
                    r'NLO+rel ResumBK',
                    r'LO+rel LOBK',
                    r'H1',
                    r'ZEUS',
                    r'ALICE',
                    r'LHCb'
                    ]

legend_text_Y = [ r'$Y_{0,\mathrm{BK}},\eta_{0,\mathrm{BK}}=4.61$',
                  r'$Y_{0,\mathrm{BK}},\eta_{0,\mathrm{BK}}=0.00$']

legend_lines_upsilon = [Line2D([0], [0], color='k', linestyle='-', linewidth=linewidth2),
                Line2D([0], [0], color='k', linestyle='--', linewidth=linewidth2),
                Line2D([0], [0], color='r', linestyle='-', linewidth=linewidth1),
                Line2D([0], [0], color='r', linestyle='--', linewidth=linewidth1)
                ]

legend_lines_upsilon_exp = [
                Line2D([0], [0], color='b', linestyle='None', marker='v'),
                Line2D([0], [0], color='r', linestyle='None', marker='o'),
                Line2D([0], [0], color='g', linestyle='None', marker='s'),
                Line2D([0], [0], color='m', linestyle='None', marker='*', markersize=10)
                ]

legend_text_upsilon =  [r'LO LOBK',
                r'LO+rel LOBK',
                r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$',
                r'NLO+rel KCBK $Y_{0,\mathrm{BK}}=4.61$'
                ]

legend_text_upsilon_exp =  [
                r'H1',
                r'ZEUS',
                r'CMS',
                r'LHCb'
                ]



if 1 in plots:
    plt.figure(1)
    plt.plot(cs_kcbk_000_T[0], cs_kcbk_000_T[3], 'r-',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_T[0], cs_kcbk_461_T[3], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth2)
    plt.plot(cs_tbk_000_T[0], cs_tbk_000_T[3], '--',color='tab:green',label=r'NLO TBK 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_461_T[0], cs_tbk_461_T[3], '--',color='tab:green',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_T[0], cs_resumbk_000_T[3], 'b-.',label=r'NLO ResumBK 0.00', linewidth=linewidth1)
    plt.plot(cs_resumbk_461_T[0], cs_resumbk_461_T[3], 'b-.',label=r'NLO ResumBK 4.61', linewidth=linewidth2)
    plt.plot(cs_lobk_mve_T[0], cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
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
    plt.plot(cs_kcbk_000_T[0], cs_kcbk_000_rel_T[6], 'r-',label=r'NLO+rel KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_T[0], cs_kcbk_461_rel_T[6], 'r-',label=r'NLO+rel KCBK 4.61', linewidth=linewidth2)
    plt.plot(cs_tbk_000_T[0], cs_tbk_000_rel_T[6], '--',color='tab:green',label=r'NLO+rel TBK 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_461_T[0], cs_tbk_461_rel_T[6], '--',color='tab:green',label=r'NLO+rel TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_T[0], cs_resumbk_000_rel_T[6], 'b-.',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth1)
    plt.plot(cs_resumbk_461_T[0], cs_resumbk_461_rel_T[6], 'b-.',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth2)
    plt.plot(cs_lobk_mve_T[0], cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k:',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([3e1, 4e3])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 3 in plots:
    fig3=plt.figure(num=3)
    plt.plot(cs_kcbk_000_T[0],    C_int * cs_kcbk_000_T[3], 'r--',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_T[3], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth1)
    plt.plot(cs_tbk_000_T[0],     C_int * cs_tbk_000_T[3], 'g--',label=r'NLO TBK 0.00', linewidth=linewidth2)
    plt.plot(cs_tbk_461_T[0],     C_int * cs_tbk_461_T[3], 'g-',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_T[0], C_int * cs_resumbk_000_T[3], 'b--',label=r'NLO ResumBK 0.00', linewidth=linewidth3)
    plt.plot(cs_resumbk_461_T[0], C_int * cs_resumbk_461_T[3], 'b-',label=r'NLO ResumBK 4.61', linewidth=linewidth3)
    # plt.plot(cs_kcbk_parent_461_T_Q0[0], C_int * cs_kcbk_parent_461_T_Q0[3], 'm-',label=r'NLO KCBK parent 4.61', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0],         yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0],       yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0],       yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    # plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    # plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    # plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    # plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    # plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    # plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    # plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    # plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    legend1 = plt.legend(legend_lines, legend_text ,    prop={'size': 17}, frameon=False, loc='lower right', ncol=2, columnspacing=0.1, handlelength=0.8, borderaxespad=0.1)
    legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 17}, frameon=False, loc='upper left')
    plt.gca().add_artist(legend1)
    # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'$p+\gamma^* \rightarrow p + \mathrm{J}/\psi$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.66, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig3.transFigure, fontsize=20)
    plt.xlim([2e1, 3e3])
    plt.ylim([1e1, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 300 in plots:
    fig300=plt.figure(num=300)
    plt.plot(cs_ampsq_kcbk_000_T[0],    C_int * cs_ampsq_kcbk_000_T[3], 'r--',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_ampsq_kcbk_461_T[0],    C_int * cs_ampsq_kcbk_461_T[3], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth1)
    plt.plot(cs_ampsq_tbk_000_T[0],     C_int * cs_ampsq_tbk_000_T[3], 'g--',label=r'NLO TBK 0.00', linewidth=linewidth2)
    plt.plot(cs_ampsq_tbk_461_T[0],     C_int * cs_ampsq_tbk_461_T[3], 'g-',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_ampsq_resumbk_000_T[0], C_int * cs_ampsq_resumbk_000_T[3], 'b--',label=r'NLO ResumBK 0.00', linewidth=linewidth3)
    plt.plot(cs_ampsq_resumbk_461_T[0], C_int * cs_ampsq_resumbk_461_T[3], 'b-',label=r'NLO ResumBK 4.61', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0],         yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0],       yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0],       yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    # plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    # plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    # plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    # plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    # plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    # plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    # plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    # plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    legend1 = plt.legend(legend_lines, legend_text ,    prop={'size': 17}, frameon=False, loc='lower right', ncol=2, columnspacing=0.1, handlelength=0.8, borderaxespad=0.1)
    legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 17}, frameon=False, loc='upper left')
    plt.gca().add_artist(legend1)
    # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'$p+\gamma^* \rightarrow p + \mathrm{J}/\psi$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.66, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig300.transFigure, fontsize=20)
    plt.xlim([2e1, 3e3])
    plt.ylim([1e1, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 301 in plots:
    fig301=plt.figure(num=301)
    plt.plot(cs_kcbk_parent_lightq_000_T[0],    C_int * cs_kcbk_parent_lightq_000_T[3], 'r--',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_parent_lightq_461_T[0],    C_int * cs_kcbk_parent_lightq_461_T[3], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth1)
    plt.plot(cs_tbk_parent_lightq_000_T[0],     C_int * cs_tbk_parent_lightq_000_T[3], 'g--',label=r'NLO TBK 0.00', linewidth=linewidth2)
    plt.plot(cs_tbk_parent_lightq_461_T[0],     C_int * cs_tbk_parent_lightq_461_T[3], 'g-',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_parent_lightq_000_T[0], C_int * cs_resumbk_parent_lightq_000_T[3], 'b--',label=r'NLO ResumBK 0.00', linewidth=linewidth3)
    plt.plot(cs_resumbk_parent_lightq_461_T[0], C_int * cs_resumbk_parent_lightq_461_T[3], 'b-',label=r'NLO ResumBK 4.61', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0],         yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0],       yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0],       yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    legend1 = plt.legend(legend_lines, legend_text ,    prop={'size': 17}, frameon=False, loc='lower right', ncol=2, columnspacing=0.1, handlelength=0.8, borderaxespad=0.1)
    legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 17}, frameon=False, loc='upper left')
    plt.gca().add_artist(legend1)
    # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'$p+\gamma^* \rightarrow p + \mathrm{J}/\psi$, parent lightq', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.66, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig301.transFigure, fontsize=20)
    plt.xlim([2e1, 3e3])
    plt.ylim([1e1, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 302 in plots:
    fig302=plt.figure(num=302)
    plt.plot(cs_kcbk_parent_lightq_000_T_Q0[0],    C_int * cs_kcbk_parent_lightq_000_T_Q0[3], 'r--',label=r'NLO KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_balsd_lightq_000_T_Q0[0],     C_int *  cs_tbk_balsd_lightq_000_T_Q0[3], 'g--',label=r'NLO TBK bal+sd 0.00', linewidth=linewidth2)
    plt.plot(cs_resumbk_parent_lightq_000_T_Q0[0], C_int * cs_resumbk_parent_lightq_000_T_Q0[3], 'b--',label=r'NLO ResumBK parent 0.00', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0],         yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0],       yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0],       yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    # legend1 = plt.legend(legend_lines, legend_text ,    prop={'size': 17}, frameon=False, loc='lower right', ncol=2, columnspacing=0.1, handlelength=0.8, borderaxespad=0.1)
    # legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 17}, frameon=False, loc='upper left')
    # plt.gca().add_artist(legend1)
    plt.legend(prop={'size': 12}, frameon=False, ncol=2)
    # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'$p+\gamma^* \rightarrow p + \mathrm{J}/\psi$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.8, r'$Q^2 = 0.01\textrm{ GeV}^2$', transform=fig302.transFigure, fontsize=20)
    plt.xlim([1e2, 3e3])
    plt.ylim([1e1, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 303 in plots:
    fig303=plt.figure(num=303)
    plt.plot(cs_kcbk_parent_lightq_000_T_Q0[0],    C_int * cs_kcbk_parent_lightq_000_T_Q0[3], 'r--',label=r'NLO KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_balsd_lightq_000_T_Q0[0],     C_int *  cs_tbk_balsd_lightq_000_T_Q0[3], 'g--',label=r'NLO TBK bal+sd 0.00', linewidth=linewidth2)
    plt.plot(cs_resumbk_parent_lightq_000_T_Q0[0], C_int * cs_resumbk_parent_lightq_000_T_Q0[3], 'b--',label=r'NLO ResumBK parent 0.00', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_v1_upsilon[0], sigma_tot_ZEUS_v1_upsilon_data[0], xerr=[sigma_tot_ZEUS_v1_upsilon[0]-sigma_tot_ZEUS_v1_upsilon[1], sigma_tot_ZEUS_v1_upsilon[2]-sigma_tot_ZEUS_v1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[1]**2+sigma_tot_ZEUS_v1_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[3]**2+sigma_tot_ZEUS_v1_upsilon_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_ZEUS_v2_upsilon[0], sigma_tot_ZEUS_v2_upsilon_data[0], xerr=[sigma_tot_ZEUS_v2_upsilon[0]-sigma_tot_ZEUS_v2_upsilon[1], sigma_tot_ZEUS_v2_upsilon[2]-sigma_tot_ZEUS_v2_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[1]**2+sigma_tot_ZEUS_v2_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[3]**2+sigma_tot_ZEUS_v2_upsilon_data[4]**2)],fmt='or', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_H1_upsilon[0], sigma_tot_H1_upsilon_data[0], xerr=[sigma_tot_H1_upsilon[0]-sigma_tot_H1_upsilon[1], sigma_tot_H1_upsilon[2]-sigma_tot_H1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_H1_upsilon_data[1]**2+sigma_tot_H1_upsilon_data[2]**2),np.sqrt(sigma_tot_H1_upsilon_data[3]**2+sigma_tot_H1_upsilon_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_CMS_upsilon[0], sigma_tot_CMS_upsilon_data[0], xerr=[sigma_tot_CMS_upsilon[0]-sigma_tot_CMS_upsilon[1], sigma_tot_CMS_upsilon[2]-sigma_tot_CMS_upsilon[0]] , yerr=[np.sqrt(sigma_tot_CMS_upsilon_data[1]**2+sigma_tot_CMS_upsilon_data[2]**2),np.sqrt(sigma_tot_CMS_upsilon_data[3]**2+sigma_tot_CMS_upsilon_data[4]**2)],label='CMS', fmt='sg', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_LHCb_upsilon[0], sigma_tot_LHCb_upsilon_data[0], yerr=[sigma_tot_LHCb_upsilon_data[1],sigma_tot_LHCb_upsilon_data[2]],label='LHCb', fmt='*m', capsize=3, markersize=10, zorder=10)
    # legend1 = plt.legend(legend_lines_upsilon, legend_text_upsilon, prop={'size': 14}, frameon=False, loc='upper left')
    # legend2 = plt.legend(legend_lines_upsilon_exp, legend_text_upsilon_exp, prop={'size': 14}, frameon=False, loc='lower right')
    # plt.gca().add_artist(legend1)
    plt.legend(prop={'size': 11}, frameon=False, ncol=2, loc='upper left')
    plt.title(r'$p+\gamma^* \rightarrow p + \Upsilon$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.71, 0.2, r'$Q^2 = 0.01\textrm{ GeV}^2$', transform=fig303.transFigure, fontsize=15)
    plt.xlim([1e2, 3e3])
    plt.ylim([1e-2, 1e1])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)




if 4 in plots:
    fig4=plt.figure(num=4)
    plt.plot(cs_kcbk_000_T[0],    C_int * cs_kcbk_000_rel_T[6], 'r--',label=r'NLO+rel KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_rel_T[6], 'r-',label=r'NLO+rel KCBK 4.61', linewidth=linewidth1)
    plt.plot(cs_tbk_000_T[0],     C_int * cs_tbk_000_rel_T[6], 'g--',label=r'NLO+rel TBK 0.00', linewidth=linewidth2)
    plt.plot(cs_tbk_461_T[0],     C_int * cs_tbk_461_rel_T[6], 'g-',label=r'NLO+rel TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_T[0], C_int * cs_resumbk_000_rel_T[6], 'b--',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth3)
    plt.plot(cs_resumbk_461_T[0], C_int * cs_resumbk_461_rel_T[6], 'b-',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k:',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0],         yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0],       yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0],       yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE   
    plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    # plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    # plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    # plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    # plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    # plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    # plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE   
    # plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    # plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    legend1 = plt.legend(legend_lines, legend_text_rel, prop={'size': 17}, frameon=False, loc='lower right', ncol=2, columnspacing=0.1, handlelength=0.8, borderaxespad=0.1)
    legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 17}, frameon=False, loc='upper left')
    plt.gca().add_artist(legend1) # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'$p+\gamma^* \rightarrow p + \mathrm{J}/\psi$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.66, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig4.transFigure, fontsize=20)
    plt.xlim([20, 3e3])
    plt.ylim([1e1, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 401 in plots:
    fig401=plt.figure(num=401)
    plt.plot(cs_kcbk_parent_lightq_000_T[0],    C_int * cs_kcbk_parent_lightq_000_rel_T[6], 'r--',label=r'NLO+rel KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_parent_lightq_461_T[0],    C_int * cs_kcbk_parent_lightq_461_rel_T[6], 'r-',label=r'NLO+rel KCBK 4.61', linewidth=linewidth1)
    plt.plot(cs_tbk_parent_lightq_000_T[0],     C_int * cs_tbk_parent_lightq_000_rel_T[6], 'g--',label=r'NLO+rel TBK 0.00', linewidth=linewidth2)
    plt.plot(cs_tbk_parent_lightq_461_T[0],     C_int * cs_tbk_parent_lightq_461_rel_T[6], 'g-',label=r'NLO+rel TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_parent_lightq_000_T[0], C_int * cs_resumbk_parent_lightq_000_rel_T[6], 'b--',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth3)
    plt.plot(cs_resumbk_parent_lightq_461_T[0], C_int * cs_resumbk_parent_lightq_461_rel_T[6], 'b-',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k:',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0],         yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0],       yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0],       yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE   
    plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    legend1 = plt.legend(legend_lines, legend_text_rel, prop={'size': 17}, frameon=False, loc='lower right', ncol=2, columnspacing=0.1, handlelength=0.8, borderaxespad=0.1)
    legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 17}, frameon=False, loc='upper left')
    plt.gca().add_artist(legend1) # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'$p+\gamma^* \rightarrow p + \mathrm{J}/\psi$, parent lightq', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.66, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig401.transFigure, fontsize=20)
    plt.xlim([20, 3e3])
    plt.ylim([1e1, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 402 in plots:
    fig402=plt.figure(num=402)
    plt.plot(cs_kcbk_parent_lightq_000_T_Q0[0],    C_int * cs_kcbk_parent_lightq_000_T_Q0_rel[6], 'r--',label=r'NLO+rel KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_balsd_lightq_000_T_Q0[0],     C_int *  cs_tbk_balsd_lightq_000_T_Q0_rel[6], 'g--',label=r'NLO+rel TBK bal+sd 0.00', linewidth=linewidth2)
    plt.plot(cs_resumbk_parent_lightq_000_T_Q0[0], C_int * cs_resumbk_parent_lightq_000_T_Q0_rel[6], 'b--',label=r'NLO+rel ResumBK parent 0.00', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k:',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0],         yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0],       yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0],       yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    # legend1 = plt.legend(legend_lines, legend_text ,    prop={'size': 17}, frameon=False, loc='lower right', ncol=2, columnspacing=0.1, handlelength=0.8, borderaxespad=0.1)
    # legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 17}, frameon=False, loc='upper left')
    # plt.gca().add_artist(legend1)
    plt.legend(prop={'size': 12}, frameon=False, ncol=2)
    # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'$p+\gamma^* \rightarrow p + \mathrm{J}/\psi$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.8, r'$Q^2 = 0.01\textrm{ GeV}^2$', transform=fig402.transFigure, fontsize=20)
    plt.xlim([1e2, 3e3])
    plt.ylim([1e1, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 403 in plots:
    fig403=plt.figure(num=403)
    plt.plot(cs_kcbk_parent_lightq_000_T_Q0[0],    C_int * cs_kcbk_parent_lightq_000_T_Q0_rel[6], 'r--',label=r'NLO+rel KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_balsd_lightq_000_T_Q0[0],     C_int *  cs_tbk_balsd_lightq_000_T_Q0_rel[6], 'g--',label=r'NLO+rel TBK bal+sd 0.00', linewidth=linewidth2)
    plt.plot(cs_resumbk_parent_lightq_000_T_Q0[0], C_int * cs_resumbk_parent_lightq_000_T_Q0_rel[6], 'b--',label=r'NLO+rel ResumBK parent 0.00', linewidth=linewidth3)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k:',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.errorbar(sigma_tot_ZEUS_v1_upsilon[0], sigma_tot_ZEUS_v1_upsilon_data[0], xerr=[sigma_tot_ZEUS_v1_upsilon[0]-sigma_tot_ZEUS_v1_upsilon[1], sigma_tot_ZEUS_v1_upsilon[2]-sigma_tot_ZEUS_v1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[1]**2+sigma_tot_ZEUS_v1_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[3]**2+sigma_tot_ZEUS_v1_upsilon_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_ZEUS_v2_upsilon[0], sigma_tot_ZEUS_v2_upsilon_data[0], xerr=[sigma_tot_ZEUS_v2_upsilon[0]-sigma_tot_ZEUS_v2_upsilon[1], sigma_tot_ZEUS_v2_upsilon[2]-sigma_tot_ZEUS_v2_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[1]**2+sigma_tot_ZEUS_v2_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[3]**2+sigma_tot_ZEUS_v2_upsilon_data[4]**2)],fmt='or', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_H1_upsilon[0], sigma_tot_H1_upsilon_data[0], xerr=[sigma_tot_H1_upsilon[0]-sigma_tot_H1_upsilon[1], sigma_tot_H1_upsilon[2]-sigma_tot_H1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_H1_upsilon_data[1]**2+sigma_tot_H1_upsilon_data[2]**2),np.sqrt(sigma_tot_H1_upsilon_data[3]**2+sigma_tot_H1_upsilon_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_CMS_upsilon[0], sigma_tot_CMS_upsilon_data[0], xerr=[sigma_tot_CMS_upsilon[0]-sigma_tot_CMS_upsilon[1], sigma_tot_CMS_upsilon[2]-sigma_tot_CMS_upsilon[0]] , yerr=[np.sqrt(sigma_tot_CMS_upsilon_data[1]**2+sigma_tot_CMS_upsilon_data[2]**2),np.sqrt(sigma_tot_CMS_upsilon_data[3]**2+sigma_tot_CMS_upsilon_data[4]**2)],label='CMS', fmt='sg', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_LHCb_upsilon[0], sigma_tot_LHCb_upsilon_data[0], yerr=[sigma_tot_LHCb_upsilon_data[1],sigma_tot_LHCb_upsilon_data[2]],label='LHCb', fmt='*m', capsize=3, markersize=10, zorder=10)
    # legend1 = plt.legend(legend_lines_upsilon, legend_text_upsilon, prop={'size': 14}, frameon=False, loc='upper left')
    # legend2 = plt.legend(legend_lines_upsilon_exp, legend_text_upsilon_exp, prop={'size': 14}, frameon=False, loc='lower right')
    # plt.gca().add_artist(legend1) # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.legend(prop={'size': 12}, frameon=False, ncol=1)
    plt.title(r'$p+\gamma^* \rightarrow p + \Upsilon$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.57, 0.8, r'$Q^2 = 0.01\textrm{ GeV}^2$', transform=fig403.transFigure, fontsize=20)
    plt.xlim([1e2, 3e3])
    plt.ylim([1e-2, 1e1])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)




if 5 in plots:
    plt.figure(5)
    plt.plot(cs_kcbk_000_T[0],    C_int * cs_kcbk_000_rel_T[6], '-',color='tab:green',label=r'NLO+rel KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_000_T[0],     C_int * cs_tbk_000_rel_T[6], 'c-',label=r'NLO+rel TBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_000_T[0], C_int * cs_resumbk_000_rel_T[6], 'm-',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.fill_between(cs_kcbk_000_T[0], C_int * (cs_kcbk_000_rel_T[6]-cs_kcbk_000_rel_T[7]), C_int * (cs_kcbk_000_rel_T[6]+cs_kcbk_000_rel_T[7]), facecolor='tab:green',alpha=0.3)
    plt.fill_between(cs_tbk_000_T[0], C_int * (cs_tbk_000_rel_T[6]-cs_tbk_000_rel_T[7]), C_int * (cs_tbk_000_rel_T[6]+cs_tbk_000_rel_T[7]), facecolor='c',alpha=0.3)
    plt.fill_between(cs_resumbk_000_T[0], C_int * (cs_resumbk_000_rel_T[6]-cs_resumbk_000_rel_T[7]), C_int * (cs_resumbk_000_rel_T[6]+cs_resumbk_000_rel_T[7]), facecolor='m',alpha=0.3)
    plt.fill_between(cs_lobk_mve_T[0], C_int * NRQCD_factor * (cs_lobk_mve_rel_T[4]-cs_lobk_mve_rel_T[5]), C_int * NRQCD_factor * (cs_lobk_mve_rel_T[4]+cs_lobk_mve_rel_T[5]), facecolor='k',alpha=0.3)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.legend(prop={'size': 11}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([1e1, 5e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 502 in plots:
    fig502=plt.figure(num=502)
    plt.plot(cs_A197_kcbk_parent_lightq_000_T_Q0[0],    C_int_Au * cs_A197_kcbk_parent_lightq_000_T_Q0[3], 'r--',label=r'NLO KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(cs_A197_tbk_balsd_lightq_000_T_Q0[0],      C_int_Au * cs_A197_tbk_balsd_lightq_000_T_Q0[3], 'g--',label=r'NLO TBK bal+sd 0.00', linewidth=linewidth2)
    plt.plot(cs_A197_resumbk_parent_lightq_000_T_Q0[0], C_int_Au * cs_A197_resumbk_parent_lightq_000_T_Q0[3], 'b--',label=r'NLO ResumBK parent 0.00', linewidth=linewidth3)
    # plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    # plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0],         yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    # plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0],       yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    # plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0],       yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    # plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    # plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    # plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    # plt.errorbar(sigma_tot_LHCb7_W[0], sigma_tot_LHCb7_data[0],  yerr=[sigma_tot_LHCb7_data[1], sigma_tot_LHCb7_data[1]], label=r'LHCb', fmt='*m', capsize=3, markersize=10) # LHCb 7
    # plt.errorbar(sigma_tot_LHCb13_W[0], sigma_tot_LHCb13_data[0],  yerr=[sigma_tot_LHCb13_data[1], sigma_tot_LHCb13_data[1]], fmt='*m', capsize=3, markersize=10) # LHCb 13
    # legend1 = plt.legend(legend_lines, legend_text ,    prop={'size': 17}, frameon=False, loc='lower right', ncol=2, columnspacing=0.1, handlelength=0.8, borderaxespad=0.1)
    # legend2 = plt.legend(legend_lines_Y, legend_text_Y, prop={'size': 17}, frameon=False, loc='upper left')
    # plt.gca().add_artist(legend1)
    plt.legend(prop={'size': 12}, frameon=False, ncol=1, loc='lower right')
    # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'Au$+\gamma^* \rightarrow $Au$+ \mathrm{J}/\psi$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.8, r'$Q^2 = 0.01\textrm{ GeV}^2$', transform=fig302.transFigure, fontsize=20)
    plt.xlim([3e1, 3e3])
    plt.ylim([1e3, 2e5])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 503 in plots:
    fig503=plt.figure(num=503)
    plt.plot(cs_A197_kcbk_parent_lightq_000_T_Q0[0],    C_int_Au * cs_A197_kcbk_parent_lightq_000_T_Q0[3], 'r--',label=r'NLO KCBK parent 0.00', linewidth=linewidth1)
    plt.plot(cs_A197_tbk_balsd_lightq_000_T_Q0[0],      C_int_Au * cs_A197_tbk_balsd_lightq_000_T_Q0[3], 'g--',label=r'NLO TBK bal+sd 0.00', linewidth=linewidth2)
    plt.plot(cs_A197_resumbk_parent_lightq_000_T_Q0[0], C_int_Au * cs_A197_resumbk_parent_lightq_000_T_Q0[3], 'b--',label=r'NLO ResumBK parent 0.00', linewidth=linewidth3)
    # plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth2)
    # plt.errorbar(sigma_tot_ZEUS_v1_upsilon[0], sigma_tot_ZEUS_v1_upsilon_data[0], xerr=[sigma_tot_ZEUS_v1_upsilon[0]-sigma_tot_ZEUS_v1_upsilon[1], sigma_tot_ZEUS_v1_upsilon[2]-sigma_tot_ZEUS_v1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[1]**2+sigma_tot_ZEUS_v1_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[3]**2+sigma_tot_ZEUS_v1_upsilon_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=10)
    # plt.errorbar(sigma_tot_ZEUS_v2_upsilon[0], sigma_tot_ZEUS_v2_upsilon_data[0], xerr=[sigma_tot_ZEUS_v2_upsilon[0]-sigma_tot_ZEUS_v2_upsilon[1], sigma_tot_ZEUS_v2_upsilon[2]-sigma_tot_ZEUS_v2_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[1]**2+sigma_tot_ZEUS_v2_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[3]**2+sigma_tot_ZEUS_v2_upsilon_data[4]**2)],fmt='or', capsize=3, zorder=10)
    # plt.errorbar(sigma_tot_H1_upsilon[0], sigma_tot_H1_upsilon_data[0], xerr=[sigma_tot_H1_upsilon[0]-sigma_tot_H1_upsilon[1], sigma_tot_H1_upsilon[2]-sigma_tot_H1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_H1_upsilon_data[1]**2+sigma_tot_H1_upsilon_data[2]**2),np.sqrt(sigma_tot_H1_upsilon_data[3]**2+sigma_tot_H1_upsilon_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=10)
    # plt.errorbar(sigma_tot_CMS_upsilon[0], sigma_tot_CMS_upsilon_data[0], xerr=[sigma_tot_CMS_upsilon[0]-sigma_tot_CMS_upsilon[1], sigma_tot_CMS_upsilon[2]-sigma_tot_CMS_upsilon[0]] , yerr=[np.sqrt(sigma_tot_CMS_upsilon_data[1]**2+sigma_tot_CMS_upsilon_data[2]**2),np.sqrt(sigma_tot_CMS_upsilon_data[3]**2+sigma_tot_CMS_upsilon_data[4]**2)],label='CMS', fmt='sg', capsize=3, zorder=10)
    # plt.errorbar(sigma_tot_LHCb_upsilon[0], sigma_tot_LHCb_upsilon_data[0], yerr=[sigma_tot_LHCb_upsilon_data[1],sigma_tot_LHCb_upsilon_data[2]],label='LHCb', fmt='*m', capsize=3, markersize=10, zorder=10)
    # legend1 = plt.legend(legend_lines_upsilon, legend_text_upsilon, prop={'size': 14}, frameon=False, loc='upper left')
    # legend2 = plt.legend(legend_lines_upsilon_exp, legend_text_upsilon_exp, prop={'size': 14}, frameon=False, loc='lower right')
    # plt.gca().add_artist(legend1)
    plt.legend(prop={'size': 11}, frameon=False, ncol=1, loc='lower right')
    plt.title(r'Au$+\gamma^* \rightarrow$Au$+ \Upsilon$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.17, 0.8, r'$Q^2 = 0.01\textrm{ GeV}^2$', transform=fig303.transFigure, fontsize=15)
    plt.xlim([3e1, 3e3])
    plt.ylim([1e0, 1e3])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)




if 6 in plots:
    plt.figure(6)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_rel_T[7], '-',color='tab:green',label=r'NLO+rel KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_461_T[0],     C_int * cs_tbk_461_rel_T[7], 'c-',label=r'NLO+rel TBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_461_T[0], C_int * cs_resumbk_461_rel_T[7], 'm-',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[5] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth)
    plt.fill_between(cs_kcbk_461_T[0], C_int * (cs_kcbk_461_rel_T[6]-cs_kcbk_461_rel_T[7]), C_int * (cs_kcbk_461_rel_T[6]+cs_kcbk_461_rel_T[7]), facecolor='tab:green',alpha=0.3)
    plt.fill_between(cs_tbk_461_T[0], C_int * (cs_tbk_461_rel_T[6]-cs_tbk_461_rel_T[7]), C_int * (cs_tbk_461_rel_T[6]+cs_tbk_461_rel_T[7]), facecolor='c',alpha=0.3)
    plt.fill_between(cs_resumbk_461_T[0], C_int * (cs_resumbk_461_rel_T[6]-cs_resumbk_461_rel_T[7]), C_int * (cs_resumbk_461_rel_T[6]+cs_resumbk_461_rel_T[7]), facecolor='m',alpha=0.3)
    plt.fill_between(cs_lobk_mve_T[0], C_int * NRQCD_factor * (cs_lobk_mve_rel_T[3]-cs_lobk_mve_rel_T[4]), C_int * NRQCD_factor * (cs_lobk_mve_rel_T[3]+cs_lobk_mve_rel_T[4]), facecolor='k',alpha=0.3)
    plt.errorbar(sigma_tot_ZEUS_W[0], sigma_tot_ZEUS_data[0], xerr=[sigma_tot_ZEUS_W[0]-sigma_tot_ZEUS_W[1], sigma_tot_ZEUS_W[2]-sigma_tot_ZEUS_W[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_data[1]**2+sigma_tot_ZEUS_data[2]**2),np.sqrt(sigma_tot_ZEUS_data[3]**2+sigma_tot_ZEUS_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_v1_W[0], sigma_tot_H1_v1_data[0], xerr=[sigma_tot_H1_v1_W[0]-sigma_tot_H1_v1_W[1], sigma_tot_H1_v1_W[2]-sigma_tot_H1_v1_W[0]] , yerr=[np.sqrt(sigma_tot_H1_v1_data[1]**2+sigma_tot_H1_v1_data[2]**2),np.sqrt(sigma_tot_H1_v1_data[3]**2+sigma_tot_H1_v1_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_H1_v2_W[0], sigma_tot_H1_v2_data[0], xerr=[sigma_tot_H1_v2_W[0]-sigma_tot_H1_v2_W[1], sigma_tot_H1_v2_W[2]-sigma_tot_H1_v2_W[0]] , yerr=[sigma_tot_H1_v2_data[1], sigma_tot_H1_v2_data[2]], fmt='vb', capsize=3) # H1
    plt.errorbar(sigma_tot_ALICE_v1_W[0], sigma_tot_ALICE_v1_data[0], xerr=[sigma_tot_ALICE_v1_W[0]-sigma_tot_ALICE_v1_W[1], sigma_tot_ALICE_v1_W[2]-sigma_tot_ALICE_v1_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v1_data[1]**2+sigma_tot_ALICE_v1_data[2]**2+sigma_tot_ALICE_v1_data[3]**2),np.sqrt(sigma_tot_ALICE_v1_data[4]**2+sigma_tot_ALICE_v1_data[5]**2+sigma_tot_ALICE_v1_data[6]**2)],label='ALICE', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_ALICE_v2_W[0], sigma_tot_ALICE_v2_data[0], xerr=[sigma_tot_ALICE_v2_W[0]-sigma_tot_ALICE_v2_W[1], sigma_tot_ALICE_v2_W[2]-sigma_tot_ALICE_v2_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v2_data[1]**2+sigma_tot_ALICE_v2_data[2]**2+sigma_tot_ALICE_v2_data[3]**2),np.sqrt(sigma_tot_ALICE_v2_data[4]**2+sigma_tot_ALICE_v2_data[5]**2+sigma_tot_ALICE_v2_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.errorbar(sigma_tot_ALICE_v3_W[0], sigma_tot_ALICE_v3_data[0], xerr=[sigma_tot_ALICE_v3_W[0]-sigma_tot_ALICE_v3_W[1], sigma_tot_ALICE_v3_W[2]-sigma_tot_ALICE_v3_W[0]] , yerr=[np.sqrt(sigma_tot_ALICE_v3_data[1]**2+sigma_tot_ALICE_v3_data[2]**2+sigma_tot_ALICE_v3_data[3]**2),np.sqrt(sigma_tot_ALICE_v3_data[4]**2+sigma_tot_ALICE_v3_data[5]**2+sigma_tot_ALICE_v3_data[6]**2)], fmt='sg', capsize=3) # ALICE
    plt.legend(prop={'size': 11}, frameon=False)
    plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([1e1, 5e2])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 10 in plots:
    plt.figure(10)
    plt.plot(cs_kcbk_000_T[0], cs_kcbk_000_T[2], '-',color='tab:green',label=r'LO KCBK 0.00', linewidth=linewidth)
    plt.plot(cs_kcbk_461_T[0], cs_kcbk_461_T[2], '--',color='tab:green',label=r'LO KCBK 4.61', linewidth=linewidth)
    plt.plot(cs_tbk_000_T[0], cs_tbk_000_T[2], 'r-',label=r'LO TBK 0.00', linewidth=linewidth)
    plt.plot(cs_tbk_461_T[0], cs_tbk_461_T[2], 'r--',label=r'LO TBK 4.61', linewidth=linewidth)
    plt.plot(cs_resumbk_000_T[0], cs_resumbk_000_T[2], 'b-',label=r'LO ResumBK 0.00', linewidth=linewidth)
    plt.plot(cs_resumbk_461_T[0], cs_resumbk_461_T[2], 'b--',label=r'LO ResumBK 4.61', linewidth=linewidth)
    plt.plot(cs_lobk_mve_T[0], cs_lobk_mve_T[6], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([20, 1e3])
    plt.ylim([3e0, 4e4])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)


if 11 in plots:
    plt.figure(11)
    plt.plot(cs_kcbk_000_T[0], cs_kcbk_000_T[3], 'r-',label=r'NLO KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_T[0], cs_kcbk_461_T[3], 'r-',label=r'NLO KCBK 4.61', linewidth=linewidth2)
    plt.plot(cs_tbk_000_T[0], cs_tbk_000_T[3], '--',color='tab:green',label=r'NLO TBK 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_461_T[0], cs_tbk_461_T[3], '--',color='tab:green',label=r'NLO TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_T[0], cs_resumbk_000_T[3], 'b-.',label=r'NLO ResumBK 0.00', linewidth=linewidth1)
    plt.plot(cs_resumbk_461_T[0], cs_resumbk_461_T[3], 'b-.',label=r'NLO ResumBK 4.61', linewidth=linewidth2)
    plt.plot(cs_lobk_mve_T[0], cs_lobk_mve_T[6], 'k:',label=r'LOBK MV$^e$', linewidth=linewidth2)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([50, 5e3])
    plt.ylim([5e-2, 3e1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 12 in plots:
    plt.figure(12)
    plt.plot(cs_kcbk_000_T[0], cs_kcbk_000_rel_T[6], 'r-',label=r'NLO+rel KCBK 0.00', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_T[0], cs_kcbk_461_rel_T[6], 'r-',label=r'NLO+rel KCBK 4.61', linewidth=linewidth2)
    plt.plot(cs_tbk_000_T[0], cs_tbk_000_rel_T[6], '--',color='tab:green',label=r'NLO+rel TBK 0.00', linewidth=linewidth1)
    plt.plot(cs_tbk_461_T[0], cs_tbk_461_rel_T[6], '--',color='tab:green',label=r'NLO+rel TBK 4.61', linewidth=linewidth2)
    plt.plot(cs_resumbk_000_T[0], cs_resumbk_000_rel_T[6], 'b-.',label=r'NLO+rel ResumBK 0.00', linewidth=linewidth1)
    plt.plot(cs_resumbk_461_T[0], cs_resumbk_461_rel_T[6], 'b-.',label=r'NLO+rel ResumBK 4.61', linewidth=linewidth2)
    plt.plot(cs_lobk_mve_T[0], cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k:',label=r'LO+rel MV$^e$', linewidth=linewidth2)
    plt.legend(prop={'size': 12}, frameon=False)
    plt.title(r'$(d\sigma_{\textrm{tot}}/dt)$ at $t = 0, Q^2= 0.05$ GeV$^2$ [nb/GeV$^2$]', fontsize=17)
    plt.xlabel(r'$W$ [GeV]', fontsize=15)
    plt.xlim([50, 5e3])
    plt.ylim([5e-2, 3e1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 14 in plots:
    fig14=plt.figure(14)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k-',label=r'LO LOBK', linewidth=linewidth2)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k--',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_T[3], 'r-',label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_rel_T[6], 'r--',label=r'NLO+rel KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth1)
    plt.errorbar(sigma_tot_ZEUS_v1_upsilon[0], sigma_tot_ZEUS_v1_upsilon_data[0], xerr=[sigma_tot_ZEUS_v1_upsilon[0]-sigma_tot_ZEUS_v1_upsilon[1], sigma_tot_ZEUS_v1_upsilon[2]-sigma_tot_ZEUS_v1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[1]**2+sigma_tot_ZEUS_v1_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[3]**2+sigma_tot_ZEUS_v1_upsilon_data[4]**2)],label='ZEUS', fmt='or', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_ZEUS_v2_upsilon[0], sigma_tot_ZEUS_v2_upsilon_data[0], xerr=[sigma_tot_ZEUS_v2_upsilon[0]-sigma_tot_ZEUS_v2_upsilon[1], sigma_tot_ZEUS_v2_upsilon[2]-sigma_tot_ZEUS_v2_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[1]**2+sigma_tot_ZEUS_v2_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[3]**2+sigma_tot_ZEUS_v2_upsilon_data[4]**2)],fmt='or', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_H1_upsilon[0], sigma_tot_H1_upsilon_data[0], xerr=[sigma_tot_H1_upsilon[0]-sigma_tot_H1_upsilon[1], sigma_tot_H1_upsilon[2]-sigma_tot_H1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_H1_upsilon_data[1]**2+sigma_tot_H1_upsilon_data[2]**2),np.sqrt(sigma_tot_H1_upsilon_data[3]**2+sigma_tot_H1_upsilon_data[4]**2)],label='H1', fmt='vb', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_CMS_upsilon[0], sigma_tot_CMS_upsilon_data[0], xerr=[sigma_tot_CMS_upsilon[0]-sigma_tot_CMS_upsilon[1], sigma_tot_CMS_upsilon[2]-sigma_tot_CMS_upsilon[0]] , yerr=[np.sqrt(sigma_tot_CMS_upsilon_data[1]**2+sigma_tot_CMS_upsilon_data[2]**2),np.sqrt(sigma_tot_CMS_upsilon_data[3]**2+sigma_tot_CMS_upsilon_data[4]**2)],label='CMS', fmt='sg', capsize=3, zorder=10)
    plt.errorbar(sigma_tot_LHCb_upsilon[0], sigma_tot_LHCb_upsilon_data[0], yerr=[sigma_tot_LHCb_upsilon_data[1],sigma_tot_LHCb_upsilon_data[2]],label='LHCb', fmt='*m', capsize=3, markersize=10, zorder=10)
    legend1 = plt.legend(legend_lines_upsilon, legend_text_upsilon, prop={'size': 14}, frameon=False, loc='upper left')
    legend2 = plt.legend(legend_lines_upsilon_exp, legend_text_upsilon_exp, prop={'size': 14}, frameon=False, loc='lower right')
    plt.gca().add_artist(legend1) # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.title(r'$p+\gamma^* \rightarrow p + \Upsilon$', fontsize=20)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.45, 0.25, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig14.transFigure, fontsize=20)
    plt.xlim([50, 5e3])
    plt.ylim([5e-2, 1e1])
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)

if 15 in plots:
    fig15=plt.figure(15)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_T[6], 'k-',label=r'LO LOBK', linewidth=linewidth2)
    plt.plot(cs_lobk_mve_T[0],    C_int * cs_lobk_mve_rel_T[4] * NRQCD_factor, 'k--',label=r'LO+rel LOBK', linewidth=linewidth2)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_T[3], 'r-',label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth1)
    plt.plot(cs_kcbk_461_T[0],    C_int * cs_kcbk_461_rel_T[6], 'r--',label=r'NLO+rel KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth1)
    plt.plot(cs_kcbk_000_T[0],    C_int * cs_kcbk_000_T[3], 'b-',label=r'NLO KCBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
    plt.plot(cs_kcbk_000_T[0],    C_int * cs_kcbk_000_rel_T[6], 'b--',label=r'NLO+rel KCBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
    plt.errorbar(sigma_tot_ZEUS_v1_upsilon[0], sigma_tot_ZEUS_v1_upsilon_data[0], xerr=[sigma_tot_ZEUS_v1_upsilon[0]-sigma_tot_ZEUS_v1_upsilon[1], sigma_tot_ZEUS_v1_upsilon[2]-sigma_tot_ZEUS_v1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[1]**2+sigma_tot_ZEUS_v1_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v1_upsilon_data[3]**2+sigma_tot_ZEUS_v1_upsilon_data[4]**2)],label='ZEUS', fmt='or', capsize=3)
    plt.errorbar(sigma_tot_ZEUS_v2_upsilon[0], sigma_tot_ZEUS_v2_upsilon_data[0], xerr=[sigma_tot_ZEUS_v2_upsilon[0]-sigma_tot_ZEUS_v2_upsilon[1], sigma_tot_ZEUS_v2_upsilon[2]-sigma_tot_ZEUS_v2_upsilon[0]] , yerr=[np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[1]**2+sigma_tot_ZEUS_v2_upsilon_data[2]**2),np.sqrt(sigma_tot_ZEUS_v2_upsilon_data[3]**2+sigma_tot_ZEUS_v2_upsilon_data[4]**2)],fmt='or', capsize=3)
    plt.errorbar(sigma_tot_H1_upsilon[0], sigma_tot_H1_upsilon_data[0], xerr=[sigma_tot_H1_upsilon[0]-sigma_tot_H1_upsilon[1], sigma_tot_H1_upsilon[2]-sigma_tot_H1_upsilon[0]] , yerr=[np.sqrt(sigma_tot_H1_upsilon_data[1]**2+sigma_tot_H1_upsilon_data[2]**2),np.sqrt(sigma_tot_H1_upsilon_data[3]**2+sigma_tot_H1_upsilon_data[4]**2)],label='H1', fmt='vb', capsize=3)
    plt.errorbar(sigma_tot_CMS_upsilon[0], sigma_tot_CMS_upsilon_data[0], xerr=[sigma_tot_CMS_upsilon[0]-sigma_tot_CMS_upsilon[1], sigma_tot_CMS_upsilon[2]-sigma_tot_CMS_upsilon[0]] , yerr=[np.sqrt(sigma_tot_CMS_upsilon_data[1]**2+sigma_tot_CMS_upsilon_data[2]**2),np.sqrt(sigma_tot_CMS_upsilon_data[3]**2+sigma_tot_CMS_upsilon_data[4]**2)],label='CMS', fmt='sg', capsize=3)
    plt.errorbar(sigma_tot_LHCb_upsilon[0], sigma_tot_LHCb_upsilon_data[0], yerr=[sigma_tot_LHCb_upsilon_data[1],sigma_tot_LHCb_upsilon_data[2]],label='LHCb', fmt='*m', capsize=3, markersize=10)
    # legend1 = plt.legend(legend_lines_upsilon, legend_text_upsilon, prop={'size': 14}, frameon=False, loc='upper left')
    # legend2 = plt.legend(legend_lines_upsilon_exp, legend_text_upsilon_exp, prop={'size': 14}, frameon=False, loc='lower right')
    # plt.gca().add_artist(legend1) # plt.title(r'$\sigma_{\textrm{tot}}$, $Q^2= 0.05$ GeV$^2$ [nb]', fontsize=17)
    plt.legend(prop={'size': 10}, frameon=False)
    plt.xlabel(r'$W$ [GeV]', fontsize=20)
    plt.ylabel(r'$\sigma_{\textrm{tot}}$ [nb]', fontsize=20)
    plt.text(0.25, 0.25, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig15.transFigure, fontsize=20)
    plt.xlim([50, 5e3])
    plt.ylim([1e-2, 1e1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)



if 16 in plots:


    legend_lines_16 = [Line2D([0], [0], color='r', linestyle='-', linewidth=linewidth1),
                    Line2D([0], [0], color='g', linestyle='-', linewidth=linewidth2),
                    Line2D([0], [0], color='b', linestyle='-', linewidth=linewidth3),
                    Line2D([0], [0], color='k', linestyle='-', linewidth=linewidth1),
                    Line2D([0], [0], color='k', linestyle='--', linewidth=linewidth1),
                    Line2D([0], [0], color='k', linestyle=':', linewidth=linewidth2)
                    ]

    legend_text_16 =  [r'NLO KCBK',
                    r'NLO TBK',
                    r'NLO ResumBK',
                    r'$Y_{0,\mathrm{BK}},\eta_{0,\mathrm{BK}}=4.61$',
                    r'$Y_{0,\mathrm{BK}},\eta_{0,\mathrm{BK}}=0.00$',
                    r'LO LOBK'
                    ]

    # plt.figure(num=8, figsize=(6,8))
    fig16, (ax161, ax162) = plt.subplots(2,1, sharex=True, num=16, figsize=(6,8))
    # plt.suptitle(r'$\mathrm{d}\sigma_L/\mathrm{d}t (t = 0, Q^2= 10\mathrm{ GeV}^2)$ [nb/GeV$^2$]', fontsize=17)
    ax161.plot(cs_kcbk_000_T[0], cs_kcbk_000_T[3], 'r--' ,label=r'NLO KCBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
    ax161.plot(cs_kcbk_461_T[0], cs_kcbk_461_T[3], 'r-', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth1)
    ax161.plot(cs_tbk_000_T[0], cs_tbk_000_T[3], 'g--',label=r'NLO TBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth2)
    ax161.plot(cs_tbk_461_T[0], cs_tbk_461_T[3], 'g-',label=r'NLO TBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
    ax161.plot(cs_resumbk_000_T[0], cs_resumbk_000_T[3], 'b--', label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth3)
    ax161.plot(cs_resumbk_461_T[0], cs_resumbk_461_T[3], 'b-', label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth3)
    ax161.plot(cs_lobk_mve_T[0], cs_lobk_mve_T[6], 'k:',label=r'LO LOBK', linewidth=linewidth*1.2)
    # ax81.plot(cs_ipsat[0], cs_ipsat[5], 'k--',label=r'LO IPSat', linewidth=linewidth*1.2)
    ax161.set_ylim([1e2, 4e3])
    ax161.set_yscale('log')
    ax161.set_ylabel(r'$\mathrm{d}\sigma_T/\mathrm{d}t$ [nb/GeV$^2$]', fontsize=20)
    plt.text(0.05, 0.85, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=ax161.transAxes, fontsize=20)
    plt.text(0.50, 0.85, r'$t=0$', transform=ax161.transAxes, fontsize=20)
    ax161.legend(legend_lines_16, legend_text_16, prop={'size': 15}, frameon=False, handlelength=1.7, loc='lower right')
    fig16.suptitle(r'$p+\gamma^* \rightarrow p + \mathrm{J}/\psi$', fontsize=20)

    ax162.plot(cs_lobk_mve_T[0], np.ones( len(cs_lobk_mve_T[0]) ), 'k:',label=r'LO LOBK', linewidth=linewidth*1.2)
    ax162.plot(cs_kcbk_000_T[0], cs_kcbk_000_T[3]/cs_lobk_mve_T[6], 'r--', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth1)
    ax162.plot(cs_kcbk_461_T[0], cs_kcbk_461_T[3]/cs_lobk_mve_T[6], 'r-', label=r'NLO KCBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth1)
    ax162.plot(cs_tbk_000_T[0], cs_tbk_000_T[3]/cs_lobk_mve_T[6], 'g--', label=r'NLO TBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth2)
    ax162.plot(cs_tbk_461_T[0], cs_tbk_461_T[3]/cs_lobk_mve_T[6], 'g-', label=r'NLO TBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth2)
    ax162.plot(cs_resumbk_000_T[0], cs_resumbk_000_T[3]/cs_lobk_mve_T[6], 'b--' ,label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=0.00$', linewidth=linewidth3)
    ax162.plot(cs_resumbk_461_T[0], cs_resumbk_461_T[3]/cs_lobk_mve_T[6], 'b-', label=r'NLO ResumBK $Y_{0,\mathrm{BK}}=4.61$', linewidth=linewidth3)
    # ax82.plot(cs_ipsat[0], cs_ipsat[5]/cs_lobk_mve[5], 'k--', label=r'LO IPSat$', linewidth=1.2*linewidth)
    ax162.set_xlim([50, 1e3])
    ax162.set_ylim([0.6, 1.2])
    ax162.set_xscale('log')
    ax162.set_yticks([0.6, 0.8, 1.0])
    ax162.set_ylabel(r'$(\mathrm{d}\sigma_T/\mathrm{d}t)/(\mathrm{d}\sigma_T/\mathrm{d}t)_\mathrm{LOBK}$', fontsize=20)
    ax162.set_xlabel(r'$W$ [GeV]', fontsize=20)
    ax161.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=20)
    ax162.tick_params(direction='in', which='both', left=True, right=True, axis='y', labelsize=20)
    ax161.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=20)
    ax162.tick_params(direction='in', which='both', bottom=True, top=True, axis='x', labelsize=20)
    # plt.tick_params(axis='x', pad=5)
    plt.tight_layout(pad=1.0)
    plt.subplots_adjust(hspace=0)



plt.show()