#!/bin/sh

Y0_if=0.0
Q_0=1.0
m_N=1.0
sigma_0_half_mb=8.68
C2=0.846
lambda_QCD=0.241
c_small=0.2
mu_0=0.6025
dipole_file=data/dipole-kcbk-hera-bal+sd-4.61.dip
alpha_s_scheme=bal+sd
A=197
d_fm=0.54
R_A_plus_fm=1.12
R_A_minus_fm=0.86
b_folder="data/au_dipole_amplitudes/dipole_kcbk_balsdrc_x0bk0.010000_qs0sqr0.090500_asC^20.845969_gamma1.210000_sigma044.561200_impactb%d.000000_A197.000000_ec1.000000_eta00.000000_maxy16.118096_euler1_step0.050000_rpoints100_rminmax0.000001--30.000000_intacc0.010000"

CONF_STRING="-Y0_if $Y0_if -Q_0 $Q_0 -m_N $m_N -sigma_0_half_mb $sigma_0_half_mb -C2 $C2 -c_small $c_small -lambda_QCD $lambda_QCD -mu_0 $mu_0 -dipole_file $dipole_file -alpha_s_scheme $alpha_s_scheme -b_dependent -d_fm $d_fm -R_A_minus_fm $R_A_minus_fm -R_A_plus_fm $R_A_plus_fm -b_folder $b_folder -A $A"
