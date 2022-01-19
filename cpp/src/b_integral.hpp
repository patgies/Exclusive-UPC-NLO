
#ifndef _B_INTEGRAL_H
#define _B_INTEGRAL_H


#include <amplitudelib.hpp>
#include <string>
using namespace std;


extern AmplitudeLib *amplitudes [16];
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