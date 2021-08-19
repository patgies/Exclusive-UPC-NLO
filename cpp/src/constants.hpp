// File for defining several constants and integration variables.


#ifndef _CONSTANTS_H
#define _CONSTANTS_H


#include <gsl/gsl_math.h>
#include <cmath>
#include <string>
using namespace std;

// Global variables.
extern double Mv;
extern double m ;
extern double Y0_if;
extern double Q0; 
extern double x_max;
extern double m_N;
extern double sigma0;

extern double N_c;
extern double N_F;
extern double beta_0;
extern double C_F;

//Constants for the (running) coupling constant.
extern bool alpha_s_run_bool;
extern double alpha_s_const;
extern double C_big;
extern double lambda_QCD;
extern double c_small;
extern double mu_0;


// Integration limits. May be reset in the config files.
extern double z2_max;
extern double x20_min;
extern double x20_max;
extern double x21_min;
extern double x21_max;
extern double ph_min;
extern double ph_max;
extern double x10_min ;
extern double x10_max;
extern double z_K0_min ;
extern double z_K0_max ;
extern double xi_min ;
extern double xi_max ;
extern double x_J_min;
extern double x_J_max ;
extern double t_min ;
extern double t_max ;
extern double u_min ;
extern double u_max ;


//Evaluation points:
extern int W_points;
extern int Q_points;
extern double Q2_min;
extern double Q2_max;
extern double W_min;
extern double W_max;

// Integration points used in the integration method.
// Low = 1-3 dimensional integrals
// High = 4-dimensional integrals
// dim6 = 6-dimensional integral
extern size_t calls_low;
extern size_t calls_high;
extern size_t calls_dim6;

// Boolean switches for several options.
extern bool integ_points_small_bool;
extern bool eta_bool;
extern bool NLO_x_pom_bool ;
extern bool dipole_file_bool;
extern bool IPsat_bool ;
extern bool rcBK_bool ;

double x_pom_fun(double W, double Q, double Delta);
double x_min_fun(double W, double Q, double Delta);

double Y_0_fun(double W, double Q);
double eta_corr(double r);
double rapidity(double W, double Q, double z2, double r);
double z2_min_fun(double W, double Q);
double z2_min_sub2_fun(double W, double Q, double Delta);


// Constants needed for the nuclear dipole amplitude
extern bool b_dependence_bool;
extern int A;
extern double rho_0;
extern double T_A_b_min_integral;
extern double T_A_squared_b_min_integral;
extern double d_thickness;
extern double R_A_plus;
extern double R_A_minus;
extern double fm_to_inv_gev;

double R_A();




#endif