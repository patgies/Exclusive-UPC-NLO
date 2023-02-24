// File for defining several constants and integration variables.
// TODO: the rapidities defined here are really complicated. In the future, it might be better to define them more clearly.


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
string* alpha_s_scheme;
double alpha_s_const;
double C_big;
double lambda_QCD;
double c_small;
double mu_0;


// Integration limits. May be reset from the terminal.
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
double y_min = 1.0e-5;
double y_max = 1.0-1.0e-5;


//Number of evaluation points:
int W_length=0;
int Q2_length=0;

// Integration points used in the integration method.
// Low = 1-3 dimensional integrals
// 4 = 4-dimensional integrals
// 6 = 6-dimensional integral
size_t calls_dim_low;
size_t calls_dim_4;
size_t calls_dim_high;

// Boolean switches for several options.
bool eta_bool = false;
bool x_pom_bool = false;
bool dipole_file_bool = true;
bool dim6_bool = false;

bool minus_cutoff_bool = false;
double minus_cutoff_value = 1.0;


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
double rapidity(double W, double Q, double z2) {
    return log(z2) + Y_0_fun(W, Q);
} 

// Target rapidity eta = Y + eta_corr
double target_rapidity(double Y, double r) {
    return Y + eta_corr(r);
} 


// Gives the minimum for the z_2 integral in the unsub scheme.
double z2_min_fun(double W, double Q) {
    if( minus_cutoff_bool == true ) return 0.0;
    return fmin(exp(Y0_if- Y_0_fun(W, Q) ), z2_max);
}

// Gives the minimum for the z_2 integral for the variant of the sub scheme, where LO is evaluated at x_pom.
double z2_min_pom_fun(double W, double Q, double Delta) {
    return z2_min_fun(W, Q) * x_max/x_pom_fun(W, Q, Delta);
}

// Gives the minimum for the z_2 integral when using a cutoff for the minus momentum. 
// This is in addition to the cutoff z2 > 2*Q0*Q0/W*W;
// double z2_min_minus_cutoff(double W, double Q, double x01, double x20, double x21) {
    // double r = min( x20, x21 );
    // return exp(Y0_if) / (W*W+Q*Q-m_N*m_N) / (r*r) * minus_cutoff_value ;
// }

// Gives the minimum for the z_2 integral when using a cutoff for the minus momentum. 
//TODO: minus_cutoff not properly implemented!!! Need to figure out the correct cutoff for z2 and the correct Ydip
double z2_min_minus_cutoff(double W, double Q, double r) {

    // return exp(Y0_if) / (W*W+Q*Q-m_N*m_N) / (fmin(1, Q0*Q0 * r*r )) * minus_cutoff_value ;
    return exp(Y0_if) / (W*W+Q*Q-m_N*m_N) / (r*r ) * minus_cutoff_value ;
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


// A default set of parameters. Meant for debugging only, not to be used in actual calculations.
int read_constants_default() {
    Mv = 3.0969;
    m = Mv / 2.0;
    Y0_if = 0.0;
    Q0 = 1.0; 
    x_max = exp(-Y0_if);
    m_N = 1.0;
    sigma0 = 23.0 / 0.3894;

    C_big = sqrt(exp(-2.0*M_EULER));
    lambda_QCD = 0.241;
    c_small = 0.2;
    mu_0 = 2.5*lambda_QCD;

    z2_max = 0.5-1.0e-8;
    x20_min = 1.0e-5;
    x20_max = 100.0;
    x21_min = 1.0e-5;
    x21_max = 100.0;
    ph_min = 0.0;
    ph_max = 2.0*M_PI-ph_min;
    x10_min = 1.0e-5;
    x10_max = 100.0;
    z_K0_min = 1.0e-5;
    z_K0_max = 0.5-z_K0_min;
    xi_min = 1.0e-5;
    xi_max = 1.0-xi_min;
    x_J_min = 1.0e-5;
    x_J_max = 1.0-x_J_min;
    t_min = 1.0e-5;
    t_max = 1000.0;
    u_min = 1.0e-5;
    u_max = 1000.0;

    alpha_s_scheme = new string("bal+sd");


    calls_dim_low = 1e5;
    calls_dim_4 = 1e5;
    calls_dim_high = 1e5;


    dipole_file_bool = false;
    eta_bool = false;

    return 0;
}

