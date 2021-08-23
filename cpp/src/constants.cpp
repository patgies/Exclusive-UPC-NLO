// File for defining several constants and integration variables.



#include <gsl/gsl_math.h>
#include <cmath>
#include <string>
using namespace std;

// Global variables.
double Mv;
double m ;
double Y0_if;
double Q0; 
double x_max;
double m_N;
double sigma0;

double N_c = 3.0;
double N_F = 3.0;
double beta_0 = (11.0*N_c-2.0*N_F)/3.0;
double C_F = (gsl_pow_2(N_c)-1.0)/(2.0*N_c); // 4/3

//Constants for the (running) coupling constant.
bool alpha_s_run_bool = true;
double alpha_s_const;
double C_big;
double lambda_QCD;
double c_small;
double mu_0;


// Integration limits. May be reset in the config files.
double z2_max = 0.4999999;
double x20_min = 1.0e-5;
double x20_max = 100.0;
double x21_min = 1.0e-5;
double x21_max = 100.0;
double ph_min = 0.0;
double ph_max = 6.28318530718;
double x10_min = 1.0e-5;
double x10_max = 100.0;
double z_K0_min =  1.0e-5;
double z_K0_max = 0.49999;
double xi_min = 1.0e-5;
double xi_max = 0.99999;
double x_J_min = 1.0e-5;
double x_J_max = 0.99999;
double t_min = 1.0e-5;
double t_max = 1000.0;
double u_min = 1.0e-5;
double u_max = 1000.0;


//Evaluation points:
int W_points;
int Q_points;
double Q2_min;
double Q2_max;
double W_min;
double W_max;

// Integration points used in the integration method.
// Low = 1-3 dimensional integrals
// High = 4-dimensional integrals
// dim6 = 6-dimensional integral
size_t calls_low;
size_t calls_high;
size_t calls_dim6;

// Boolean switches for several options.
bool integ_points_small_bool = false;
bool eta_bool = false;
bool NLO_x_pom_bool = false;
bool rel_x_pom_bool = false;
bool dipole_file_bool = true;
bool IPsat_bool = false;
bool rcBK_bool = false;

double x_pom_fun(double W, double Q, double Delta) {
    return (Q*Q+Mv*Mv+Delta*Delta)/(W*W+Q*Q-m_N*m_N);
}

// x', corresponds to Ydip
double x_min_fun(double W, double Q, double Delta) {
    double x_pom = x_pom_fun(W, Q, Delta);
    return x_pom * 2.0*Q0*Q0/(Q*Q+Mv*Mv+Delta*Delta);
}

double Y_0_fun(double W, double Q) {
    return log( (W*W+Q*Q-m_N*m_N) / (Q0*Q0) );
}

// Correction value for calculations with the target rapidity (instead of Y). 
// eta = Y + eta_corr
double eta_corr(double r) {
    
    if(eta_bool) {
        return log( fmin(1, Q0*Q0 * r*r ) );
    }
    else {
        return 0;
    }
}

// Y
double rapidity(double W, double Q, double z2, double r) {
    return log(z2) + Y_0_fun(W, Q) + eta_corr(r);
} 

// Gives the minimum for the z_2 integral in the unsub scheme.
double z2_min_fun(double W, double Q) {
    return fmin(exp(Y0_if- Y_0_fun(W, Q) ),0.5);
}

// Gives the minimum for the z_2 integral for the variant of the sub scheme, where LO is evaluated at x_pom.
double z2_min_sub2_fun(double W, double Q, double Delta) {
    return z2_min_fun(W, Q) * x_max/x_pom_fun(W, Q, Delta);
}


// Constants needed for the nuclear dipole amplitude
bool b_dependence_bool = false;
int A;
double rho_0;
double T_A_b_min_integral; // Integral int_{bmin}^inf d^2b T_A(b)
double T_A_squared_b_min_integral; // Integral int_{bmin}^inf d^2b T_A(b)^2 
double d_thickness; // Note! These are in Gev^-1!
double R_A_plus;
double R_A_minus;
double fm_to_inv_gev = 5.068;

double R_A() {
    return (R_A_plus*std::pow(A,1.0/3.0)-R_A_minus*std::pow(A,-1.0/3.0));
}

