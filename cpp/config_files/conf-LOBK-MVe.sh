#!/bin/sh

Y0_if=0.0
Q_0=1.0 
m_N=1.0
sigma_0_half_mb=16.36
C2=7.2
lambda_QCD=0.241
c_small=0.2
mu_0=0.6025
dipole_file=data/mve.dat

CONF_STRING="-Y0_if $Y0_if -Q_0 $Q_0 -m_N $m_N -sigma_0_half_mb $sigma_0_half_mb -C2 $C2 -c_small $c_small -lambda_QCD $lambda_QCD -mu_0 $mu_0 -dipole_file $dipole_file"