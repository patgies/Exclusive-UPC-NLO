#!/bin/sh

Y0_if=0.0
Q_0=1.0 
m_N=1.0
sigma_0_half_mb=26.69
C2=1480
lambda_QCD=0.241
c_small=0.2
mu_0=0.6025
dipole_file=../../nlodisfit/data/dipole-resumbk-lightq-parent-0.00.dip
alpha_s_scheme=parent_dipole
A=197
d_fm=0.54
R_A_plus_fm=1.12
R_A_minus_fm=0.86
b_folder="data/au_dipole_amplitudes/dipole_resumbk_pdrc_x0bk1.000000_qs0sqr0.079400_asC^21477.595475_gamma1.920000_sigma0137.071800_impactb%d.000000_A197_ec1.000000_eta00.000000_maxy20.723266_euler0_step0.400000_rpoints100_rminmax0.000001--30.000000_intacc0.010000"

CONF_STRING="-Y0_if $Y0_if -Q_0 $Q_0 -m_N $m_N -sigma_0_half_mb $sigma_0_half_mb -C2 $C2 -c_small $c_small -lambda_QCD $lambda_QCD -mu_0 $mu_0 -dipole_file $dipole_file -alpha_s_scheme $alpha_s_scheme -b_dependent -d_fm $d_fm -R_A_minus_fm $R_A_minus_fm -R_A_plus_fm $R_A_plus_fm -b_folder $b_folder -A $A"