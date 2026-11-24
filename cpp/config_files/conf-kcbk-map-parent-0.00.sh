#!/bin/sh
# Proton, KCBK + parent-dipole running coupling, MAP parameters of arXiv:2506.00487.
# Dipole from github.com/hejajama/nlobk_dipole_nucleus, 4th header line set to Y0=0 (x0=1).
# Same fit as conf-A208-kcbk-map-parent-0.00.sh, for the ratio sigma_Pb / (A^2 sigma_p).

Y0_if=0.0
Q_0=1.0
m_N=1.0
sigma_0_half_mb=20.7
C2=663
lambda_QCD=0.241
c_small=0.2
mu_0=0.6025
dipole_file=data/kcbk_2506.00487/kcbk_pd/proton.dat
alpha_s_scheme=parent_dipole

CONF_STRING="-Y0_if $Y0_if -Q_0 $Q_0 -m_N $m_N -sigma_0_half_mb $sigma_0_half_mb -C2 $C2 -c_small $c_small -lambda_QCD $lambda_QCD -mu_0 $mu_0 -dipole_file $dipole_file -alpha_s_scheme $alpha_s_scheme"
