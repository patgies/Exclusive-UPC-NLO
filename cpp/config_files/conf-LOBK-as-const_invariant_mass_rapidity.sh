#!/bin/sh

Y0_if=0.0
Q_0=1.0 
m_N=1.0
sigma_0_half_mb=20.00 # A guess, shouldn't matter
dipole_file=data/fixed_as_025_mv_smallerqs.dip
alpha_s=0.25

Y_min=0.0
Y_max=15.19

CONF_STRING="-Y0_if $Y0_if -Q_0 $Q_0 -m_N $m_N -sigma_0_half_mb $sigma_0_half_mb -dipole_file $dipole_file -alphas_const $alpha_s -use_invariant_mass_rapidity -Y_min $Y_min -Y_max $Y_max"