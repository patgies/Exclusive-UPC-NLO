
#ifndef _B_INTEGRAL_H
#define _B_INTEGRAL_H


#include "amplitudelib.hpp"
#include <string>
using namespace std;


// Impact-parameter grid of the nuclear dipole files (b in GeV^-1).
// File i holds the dipole at b = B_STEP*i, for i = 0, ..., N_B_FILES-1 (b = 0, 2, ..., 30).
// The b-integral uses the files explicitly up to index B_LAST (b = 26) with the trapezoid rule,
// and for b > B_MIN_TAIL = 26.5 the linearised tail A*T_A(b)*sigma0/2*N_proton(r).
const int    N_B_FILES  = 16;
const double B_STEP     = 2.0;
const int    B_LAST     = 13;
const double B_TAIL_GAP = 0.5;                            // distance from the last file to the tail start
const double B_MIN_TAIL = B_STEP*B_LAST + B_TAIL_GAP;     // = 26.5
const double W_LAST     = B_STEP*B_LAST * (B_STEP/2.0 + B_TAIL_GAP);  // trapezoid weight b*db of the last point (= 1.5*26)

extern AmplitudeLib *amplitudes [N_B_FILES];
extern AmplitudeLib *amp_default;

void initialize_amplitudes(string folder, string default_file);
struct int_params_dipole_qq{double r; double Y;};
struct int_params_dipole_qqg{double x10;  double x20; double x21; double Y;};
struct int_params_T_A{double b;};
double rho_A(double x3, void *params);
double rho_A_r2(double r, void *params);
void initialize_rho0();
void initialize_T_A();
void initialize_T_A_squared();
double T_A_integrand(double b, void *params);
double T_A_squared_integrand(double b, void *params);
double T_A(double b);
double qq_dipole_integrated(double r, double Y);
double qqg_dipole_integrated(double x10, double x20, double x21, double Y);
double qqg_dipole_value( double N_10, double N_20, double N_21 );
double qqg_dipole_value_b_independent( double N_10, double N_20, double N_21);
double qq_dipole_value_high_b(double r, double Y, double b);
double qq_dipole_integrand_high_b(double b, void *params);
double qqg_dipole_integrand_high_b(double b, void *params);
double qq_dipole_value_b_independent(double r, double Y);

#endif