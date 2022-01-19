#!/bin/sh

Y0_if=0.0
Q_0=1.0 
m_N=1.0
sigma_0_half_mb=8.68
C^2=0.846
lambda_QCD=0.241
c_small=0.2
mu_0=0.6025
int_points_dim_low=500000
int_points_dim_4=5000000
int_points_dim_6=20000000
dipole_file=data/dipole-kcbk-hera-bal+sd-4.61.dip
A=197
d_fm=0.54
R_A_plus_fm=1.12
R_A_minus_fm=0.86
b_folder=data/au_kcbk_y0bk_4605_smallest

CONF_STRING="-Y0_if $Y0_if -Q_0 $Q_0 -m_N $m_N -sigma_0_half_mb $sigma_0_half_mb -C2 $C2 -c_small $c_small -lambda_QCD $lambda_QCD -mu_0 $mu_0 -dipole_file $dipole_file -b_dependent -d_fm=$d_fm -R_A_minus_fm $R_A_minus_fm -R_A_plus_fm $R_A_plus_fm -b_folder $b_folder -A $A"