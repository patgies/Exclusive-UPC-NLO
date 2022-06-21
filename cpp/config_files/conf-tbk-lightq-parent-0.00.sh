#!/bin/sh

Y0_if=0.0
Q_0=1.0 
m_N=1.0
sigma_0_half_mb=29.84
C2=8050
lambda_QCD=0.241
c_small=0.2
mu_0=0.6025
dipole_file=../../nlodisfit/data/dipole-tbk-lightq-parent-0.00.dip
alpha_s_scheme=parent_dipole

CONF_STRING="-Y0_if $Y0_if -Q_0 $Q_0 -m_N $m_N -sigma_0_half_mb $sigma_0_half_mb -C2 $C2 -c_small $c_small -lambda_QCD $lambda_QCD -mu_0 $mu_0 -dipole_file $dipole_file -alpha_s_scheme $alpha_s_scheme -use_target_rapidity"