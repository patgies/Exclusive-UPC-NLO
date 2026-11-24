#!/bin/sh
# Pb (A=208), KCBK + Balitsky/smallest-dipole running coupling, MAP parameters of arXiv:2506.00487.
# Dipoles from github.com/hejajama/nlobk_dipole_nucleus, 4th header line set to Y0=0 (x0=1).

Y0_if=0.0
Q_0=1.0
m_N=1.0
sigma_0_half_mb=9.08
C2=1.74
lambda_QCD=0.241
c_small=0.2
mu_0=0.6025
dipole_file=data/kcbk_2506.00487/kcbk_bal/proton.dat
alpha_s_scheme=bal+sd
A=208
d_fm=0.54
R_A_plus_fm=1.12
R_A_minus_fm=0.86
b_folder="data/kcbk_2506.00487/kcbk_bal/Pb/Pb_b_%d.dat"

CONF_STRING="-Y0_if $Y0_if -Q_0 $Q_0 -m_N $m_N -sigma_0_half_mb $sigma_0_half_mb -C2 $C2 -c_small $c_small -lambda_QCD $lambda_QCD -mu_0 $mu_0 -dipole_file $dipole_file -alpha_s_scheme $alpha_s_scheme -b_dependent -d_fm $d_fm -R_A_minus_fm $R_A_minus_fm -R_A_plus_fm $R_A_plus_fm -b_folder $b_folder -A $A"
