"""
For plotting amplitudes.
"""
import matplotlib.pyplot as plt
import numpy as np
import os 
import plotting_functions


# def phenomenological_correction(lambda_v):
#     real_part_correction = lambda x: 1+np.tan( np.pi/2 * x )**2
#     skewedness_correction = lambda x: 2**(2*x+3)/np.sqrt(np.pi) * special.gamma( x + 5/2 ) / special.gamma( x + 4 )
#     # return real_part_correction( lambda_v ) * skewedness_correction( lambda_v )**2
#     return 1


# Order:LO(x_min) 	 LO(x_pom) 	 LO(x_max) 	 qq NLO 1 dim 	 qq NLO J_1 	 qq NLO J_2 	 qq NLO K_0 	 qqg dim 4 no BK 	 qqg dim 4 sub2 BK 	 qqg dim 4 unsub BK 	 qqg dim 6
dir_path = os.path.dirname(os.path.realpath(__file__)) + r'/amplitudes_T/'

# particle = 'jpsi'
particle = 'upsilon' 

if particle == 'jpsi':
    Mv = 3.0969

    amplitude_file1 = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-Q2.dat'
    amplitude_file2 = dir_path + r'results-kcbk-lightq-parent-0.00-jpsi-T-Q2_0.01_minus_cutoff_1-x20x21.dat'
    # amplitude_file1 = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-Q2.dat'
    # amplitude_file2 = dir_path + r'results-resumbk-lightq-parent-0.00-jpsi-T-Q2_0.01_minus_cutoff_1-x20x21.dat'
    # amplitude_file1 = dir_path + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-Q2_0.01.dat'
    # amplitude_file2 = dir_path + r'results-tbk-lightq-bal+sd-0.00-jpsi-T-Q2_0.01_minus_cutoff_1-x20x21.dat'


elif particle == 'upsilon':
    Mv = 9.46

    # amplitude_file1 = dir_path + r'results-kcbk-lightq-parent-0.00-upsilon-T-Q2_0.01.dat'
    # amplitude_file2 = dir_path + r'results-kcbk-lightq-parent-0.00-upsilon-T-Q2_0.01_minus_cutoff_1-x20x21.dat'
    amplitude_file1 = dir_path + r'results-resumbk-lightq-parent-0.00-upsilon-T-Q2_0.01.dat'
    amplitude_file2 = dir_path + r'results-resumbk-lightq-parent-0.00-upsilon-T-Q2_0.01_minus_cutoff_1-x20x21.dat'
    # amplitude_file1 = dir_path + r'results-tbk-lightq-bal+sd-0.00-upsilon-T-Q2_0.01.dat'
    # amplitude_file2 = dir_path + r'results-tbk-lightq-bal+sd-0.00-upsilon-T-Q2_0.01_minus_cutoff_1-x20x21.dat'
else:
    print('Invalid particle')

Wv_1, Q2_1, amplitudes_table_1 = plotting_functions.read_file(amplitude_file1)
Wv_2, Q2_2, amplitudes_table_2 = plotting_functions.read_file(amplitude_file2)


Nc = 3
ef = 2/3
Cf = 4/3
e = np.sqrt(4*np.pi/137)
Gamma_ee = 5.53e-6
m = Mv/2

# TODO: the following should be updated for upsilon
alpha_s = 0.25
O_LDME = 0.440
q_LDME = 0.441


wf_0 = np.sqrt( O_LDME / (2*Nc) )

nabla_wf = -q_LDME * wf_0

reg_scheme = 'NR wave function'

if reg_scheme == 'decay width':
    wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) )  # int dz/(4pi) phi(z,rt=0)
elif reg_scheme == 'NR wave function':
    wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) ) * ( 1 + 2*alpha_s*Cf/np.pi ) # int dz/(4pi) phi(z,rt=0)
elif reg_scheme == 'rel wave function':
    wf_LO = 1/np.sqrt(4*m)*(wf_0 + 1/(6*m**2)*nabla_wf * 7/2)  # int dz/(4pi) phi(z,rt=0)
else:
    raise Exception('Invalid scheme')
# wf_LO = np.sqrt(3*np.pi*Mv*Gamma_ee / (2*Nc*ef**2*e**4) )
nonrel_factor = e*ef*m*Nc/(np.pi)*2*wf_LO / np.sqrt(2*Nc)


wf_rel = 1/(6*m**2)/np.sqrt(m) * nabla_wf

rel_factor = e*ef*m*Nc/(np.pi)*2/ np.sqrt(2*Nc) * wf_rel

lambda_v_1 = np.array(amplitudes_table_1)[:,11]
amplitudes_1 = nonrel_factor*np.array(amplitudes_table_1)[:,:11]
rel_amplitudes_1 = rel_factor*np.array(amplitudes_table_1)[:,12:]

lambda_v_2 = np.array(amplitudes_table_2)[:,11]
amplitudes_2 = nonrel_factor*np.array(amplitudes_table_2)[:,:11]
rel_amplitudes_2 = rel_factor*np.array(amplitudes_table_2)[:,12:]


def extract_parts(amplitudes_list):

    LO_prime = amplitudes_list[:,0]
    LO_pom = amplitudes_list[:,1]
    LO_0 = amplitudes_list[:,2]
    LO_BK = amplitudes_list[:,2] + amplitudes_list[:,9]
    if reg_scheme == 'decay width': # TODO:???
        NLO_dip = amplitudes_list[:,3]+amplitudes_list[:,5]+amplitudes_list[:,6]+amplitudes_list[:,7]
    else:
        NLO_dip = amplitudes_list[:,4]+amplitudes_list[:,5]+amplitudes_list[:,6]+amplitudes_list[:,7]
    NLO_qqg = amplitudes_list[:,8]+amplitudes_list[:,10]
    NLO_BK = amplitudes_list[:,9]
    NLO = (LO_0 + NLO_BK) + NLO_dip + NLO_qqg
    NLO2 = LO_prime + NLO_dip + NLO_qqg

    dict_amp = {}
    dict_amp['LO_prime'] = LO_prime
    dict_amp['LO_pom'] = LO_pom
    dict_amp['LO_0'] = LO_0
    dict_amp['LO_BK'] = LO_BK
    dict_amp['NLO_dip'] = NLO_dip
    dict_amp['NLO_qqg'] = NLO_qqg
    dict_amp['NLO_BK'] = NLO_BK
    dict_amp['NLO_unsub'] = NLO
    dict_amp['NLO_sub'] = NLO2

    return dict_amp

dict_amp_1 = extract_parts(amplitudes_1)
dict_amp_2 = extract_parts(amplitudes_2)

linewidth = 2.5
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plots = [5]



if 5 in plots:
    fig5=plt.figure(5)
    plt.plot(Wv_1, dict_amp_1['NLO_unsub'], 'k-',label=r'NLO without KC', linewidth=1*linewidth)
    plt.plot(Wv_2, dict_amp_2['NLO_unsub'], 'b-',label=r'NLO with KC', linewidth=1*linewidth)
    plt.plot(Wv_1, dict_amp_1['LO_prime'], 'm--',label=r'LO$(Y_\textrm{dip})$', linewidth=1.3*linewidth)
    plt.plot(Wv_1, dict_amp_1['LO_pom'], 'r--',label=r'$\textrm{LO}(Y_\textrm{P})$', linewidth=1.3*linewidth)
    plt.legend(prop={'size': 15}, frameon=False, ncol=2, loc='upper left', columnspacing=0.5)
    plt.xlabel(r'$W \textrm{ [GeV]}$', fontsize=20)
    plt.ylabel(r'$-i \mathcal{A}_T$ [GeV$^{-2}$]', fontsize=20)
    plt.text(0.52, 0.19, r'$t=0$', transform=fig5.transFigure, fontsize=18)
    plt.text(0.52, 0.265, r'$Q^2 = 0.05\textrm{ GeV}^2$', transform=fig5.transFigure, fontsize=18)
    plt.xlim([30, 3e3])
    if particle == 'jpsi':
        plt.ylim([0.1, 1])
    elif particle == 'upsilon':
        plt.ylim([0.001, 0.3])
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=18)
    plt.xscale('log')
    plt.yscale('log')
    plt.tight_layout()
    plt.tick_params(direction='in', which='both', left=True, right=True, axis='y')
    plt.tick_params(axis='x', pad=5)





plt.show()