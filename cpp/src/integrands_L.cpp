/*

Integrands for the longitudinal photon. The common prefactor -e*ef*Q/(2*pi)*sqrt(Nc/2)*2*(wavefunction factor) has been left out, as well as the prefactor associated with the wave function.
See the article for the definitions of the functions.
*/

#include <gsl/gsl_math.h>
#include <gsl/gsl_sf_bessel.h>
#include <gsl/gsl_sf_dilog.h>
#include <gsl/gsl_errno.h>
#include <iostream>

#include "dipole_amplitudes.hpp"
#include "integrands_L.hpp"
#include "constants.hpp"
using namespace std;
using namespace Longitudinal;

// Heaviside theta
double Longitudinal::theta(double x) {return (x>0) ? 1:0;}

// Checks that the integrand has the correct number of integration variables.
void Longitudinal::dimension_error(size_t dim, size_t corr_dim) {
    if (dim != corr_dim)
        {
        cerr << "Error: Integrating over wrong number of dimensions! Correct number: " << corr_dim << ". Got: " << dim <<".\n";
        exit(1);
        }
}

// x10 in terms of x20, x21 and ph = the angle between x20 and x21.
double Longitudinal::x10_value(double x20, double x21, double ph){
    return sqrt( gsl_pow_2( x20 ) + gsl_pow_2( x21 ) - 2.0 * x20 * x21 * cos(ph) ) + 1.0e-15;
}

// Running alpha_s
double Longitudinal::alpha_s_run( double r ) {
    return 4.0*M_PI / ( beta_0 * log( pow( pow(mu_0/lambda_QCD, 2.0/c_small ) + pow(2.0*C_big/(r*lambda_QCD), 2.0/c_small), c_small ) ) );
}

double Longitudinal::alpha_s( double r) {
    if (alpha_s_run_bool)
        return alpha_s_run( r );
    else
        return alpha_s_const;
}

// alpha_s for the qqg-part, where the running alpha_s depends on the sizes of the dipoles.
double Longitudinal::alpha_s3( double x10, double x20, double x21) {
    double r = fmin(x10,  fmin(x20,x21) );
    return alpha_s( r );
}

// Implements delta dependence the dipole integrals.
double Longitudinal::delta_factor_qq(double z, double Delta, double x10) {
    return gsl_sf_bessel_J0(x10*Delta*abs(z-0.5) );
}

// Implements delta dependence of the qqg part.
double Longitudinal::delta_factor_qqg(double z2, double Delta, double x20, double x21, double ph) {
    double bessel_J_argument = Delta * sqrt( gsl_pow_2( (z2-1.0/6.0) * x20 ) + 1.0/36.0 * x21 * x21 - 1.0/3.0*(z2-1.0/6.0)*x20*x21*cos(ph)  );
    return gsl_sf_bessel_J0( bessel_J_argument );
}

//Integrand of J_1. Needs to be integrated over xi to get J_1.
double Longitudinal::J_1_integrand(double xi, double x10, double m, double Q){
    return 1.0/xi * ( -2.0*log(xi)/(1.0-xi) + (1.0+xi)/2.0 ) * ( 2.0*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) - 2.0*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+(1.0-xi/2.0)/(1.0-xi)*gsl_pow_2(m) ))  );
}

//Integrand of J_2. Needs to be integrated over xi and x to get J_2.     
double Longitudinal::J_2_integrand(double xi, double x, double x10, double m, double Q) {

    double kappa = m*m * xi*xi / ( (1.0-xi)*(1.0-x) * (x*(1.0-xi)+2.0*xi) );
    double C_Lm = 1.0/2.0*(1.0-xi) * ( -gsl_pow_2(xi) + x*(1.0-xi) * (2.0-gsl_pow_2(xi) ) / ( x*(1.0-xi) + 2.0*xi ) );
    return 2.0*gsl_pow_2(m) * ( gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) - gsl_sf_bessel_K0(x10 * sqrt( (1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m))/(1.0-x) + kappa ))) * C_Lm / ( (1.0-xi)*(1.0-x)*( x*(1.0-xi) + 2.0*xi ) * ( x/(1.0-x)*(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m))+kappa ) );
}

//Integrand of K_0. Needs to be integrated over z to get K_0.
double Longitudinal::K_0_integrand(double z, double x10, double m, double Q) {

    double tau = 2.0*m*x10*(1.0/2.0-z);
    return 16.0*z*(1.0-z)*gsl_sf_bessel_K0(x10 * sqrt(z*(1.0-z)*gsl_pow_2(Q)+gsl_pow_2(m)) )*2.0*z*( gsl_sf_bessel_K0(tau)-tau*gsl_sf_bessel_K1(tau) ) 
    +1.0/gsl_pow_2(z-1.0/2.0)*( 16.0*z*(1.0-z)*gsl_sf_bessel_K0(x10 * sqrt(z*(1.0-z)*gsl_pow_2(Q)+gsl_pow_2(m)) )*( 2.0*z*(1.0-z)*gsl_sf_bessel_K0(tau) - z*( gsl_sf_bessel_K0(tau) - tau/2.0*gsl_sf_bessel_K1(tau) ) ) -gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * ( 1.0+ 2.0*(z-1.0/2.0)*( 1.0+2.0*M_EULER+2.0*log(m*x10)+2.0*log(1.0/2.0-z) ) ) );
}


double Longitudinal::L(double m, double Q) {

    double gamma = sqrt(1.0+4.0*gsl_pow_2(m)/gsl_pow_2(Q));

    return gsl_sf_dilog(1.0/gsl_pow_2(gamma) );

}

double Longitudinal::Gamma_Lm(double m, double Q) {
    double gamma = sqrt(1.0+4.0*gsl_pow_2(m)/gsl_pow_2(Q));
    return log(1.0/2.0)*2.0+gamma*log( (1.0+gamma)/gamma )*2.0 + (gamma-1.0+2.0*gsl_pow_2(m)/gsl_pow_2(Q)) * log( (1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) / gsl_pow_2(m) ) ;
}


//Integrand of I^i, except that the factor i*r^i has been pulled out.
//The singular part at r->0 has been factored out of the integrand. This is taken into account in the definition of Ii_0.
double Longitudinal::Ii_0_integrand(double t, double u, double b, double r, double m, double Qbar, double omega, double lambda) {
    return 1.0/2.0/gsl_pow_2(4.0*M_PI) * 1.0/u * exp( -u * ( gsl_pow_2(Qbar) + gsl_pow_2(m) ) - gsl_pow_2(b)/(4.0*u) ) * 1.0/gsl_pow_2(t) * exp(- gsl_pow_2(r)/(4.0*t) ) *  ( exp( -t*omega*lambda*gsl_pow_2(m) ) - 1.0 );
}

double Longitudinal::I_integrand(double t, double u, double b, double r, double m, double Qbar, double omega, double lambda) {

    return 1.0/gsl_pow_2(4.0*M_PI) * 1.0/u * exp( -u * ( Qbar*Qbar + m*m ) - b*b/(4.0*u) ) 
    * 1.0/t * exp( -t*omega*lambda*m*m - r*r/(4.0*t) );

}

double Longitudinal::M_1(double x[], double delta, double m, double Q, double W) {
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    double t = x[4];
    double u = x[5];

    double x10 = x10_value(x20, x21, ph);
    double Y = rapidity(W, Q, z2);

    double omega_f = (1.0/2.0-z2) * z2 * 8.0;
    double lambda_f = 1.0/2.0*z2/(1.0/2.0-z2);
    double Q_f = 0.5 * Q;
    double b_f = sqrt( gsl_pow_2( (1.0 - 2.0*z2) * x20 ) + x21 * x21 - 2.0 * (1.0-2.0*z2) * x20 *x21 * cos( ph ) );
    double r_f = x20;

    double omega_g = 1.0/2.0*z2/(1.0/2.0-z2)/gsl_pow_2(1.0/2.0+z2);
    double lambda_g = 2.0*z2*(1.0/2.0-z2);
    double Q_g = sqrt( (1.0/2.0-z2) * (1.0/2.0+z2)) * Q;
    double b_g = sqrt( gsl_pow_2( 1.0 / (1.0 + 2.0*z2) * x21 ) + x20 * x20 - 2.0 / (1.0 + 2.0*z2) * x20 *x21 * cos( ph ) );
    double r_g = x21;


    return 32.0 * M_PI * m * N_xyz( x10, x20, x21, delta, Y ) * gsl_sf_bessel_K1( 2*m*z2*x20 ) * 
    ( 
        x20 * ((1.0-z2)*(1.0-z2)+z2*z2) * Ii_0_integrand(t, u, b_f, r_f, m, Q_f, omega_f, lambda_f) * theta(u/omega_f-t)
        +x21 * cos(ph) *(2*z2*z2-1) * (1-2*z2) * Ii_0_integrand(t, u, b_g, r_g, m, Q_g, omega_g, lambda_g) * theta(u/omega_g-t)
    ) * x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);

}

double Longitudinal::M_2(double x[], double delta, double m, double Q, double W) {
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    double t = x[4];
    double u = x[5];

    double x10 = x10_value(x20, x21, ph);
    double Y = rapidity(W, Q, z2);

    double omega_f = (1.0/2.0-z2) * z2 * 8.0;
    double lambda_f = 1.0/2.0*z2/(1.0/2.0-z2);
    double Q_f = 0.5 * Q;
    double b_f = sqrt( gsl_pow_2( (1.0 - 2.0*z2) * x20 ) + x21 * x21 - 2.0 * (1.0-2.0*z2) * x20 *x21 * cos( ph ) );
    double r_f = x20;

    double omega_g = 1.0/2.0*z2/(1.0/2.0-z2)/gsl_pow_2(1.0/2.0+z2);
    double lambda_g = 2.0*z2*(1.0/2.0-z2);
    double Q_g = sqrt( (1.0/2.0-z2) * (1.0/2.0+z2)) * Q;
    double b_g = sqrt( gsl_pow_2( 1.0 / (1.0 + 2.0*z2) * x21 ) + x20 * x20 - 2.0 / (1.0 + 2.0*z2) * x20 *x21 * cos( ph ) );
    double r_g = x21;


    return  -128.0 * M_PI * m * m * gsl_pow_3(z2) * N_xyz( x10, x20, x21, delta, Y ) * gsl_sf_bessel_K0( 2*m*z2*x20 ) * 
    ( 
        I_integrand( t, u, b_f, r_f, m, Q_f, omega_f, lambda_f ) * theta(u/omega_f-t) 
        - (0.5-z2)/(0.5+z2) * I_integrand(t, u, b_g, r_g, m, Q_g, omega_g, lambda_g) * theta(u/omega_g-t) 
    ) *2.0*M_PI*x20*x21*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);
}

double Longitudinal::L_5(double x[], double delta, double m, double Q, double W){
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];

    double x10 = x10_value(x20, x21, ph);
    double Y = rapidity(W, Q, z2);

    double omega_f = (1.0/2.0-z2) * z2 * 8.0;
    double Q_f = 0.5 * Q;
    double b_f = sqrt( gsl_pow_2( (1.0 - 2.0*z2) * x20 ) + x21 * x21 - 2.0 * (1.0-2.0*z2) * x20 *x21 * cos( ph ) );
    double r_f = x20;

    double omega_g = 1.0/2.0*z2/(1.0/2.0-z2)/gsl_pow_2(1.0/2.0+z2);
    double Q_g = sqrt( (1.0/2.0-z2) * (1.0/2.0+z2)) * Q;
    double b_g = sqrt( gsl_pow_2( 1.0 / (1.0 + 2.0*z2) * x21 ) + x20 * x20 - 2.0 / (1.0 + 2.0*z2) * x20 *x21 * cos( ph ) );
    double r_g = x21;


    return -8.0 / (M_PI * x20) * m * N_xyz( x10, x20, x21, delta, Y ) * gsl_sf_bessel_K1( 2*m*z2*x20 ) * 
        ( ( gsl_pow_2(1.0-z2) +z2*z2 ) * ( gsl_sf_bessel_K0( x10 * sqrt( Q_f*Q_f + m*m ) ) * (1-x20/x21 * cos(ph) ) - gsl_sf_bessel_K0( sqrt( (b_f*b_f+omega_f*r_f*r_f) *(Q_f*Q_f+m*m) ) ) )
         - x20/x21 * cos(ph) * ( 2*z2*z2-1 ) * ( 1-2*z2 ) * gsl_sf_bessel_K0( sqrt( (b_g*b_g+omega_g*r_g*r_g) *(Q_g*Q_g+m*m) ) ) ) 
        * x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);

}

double Longitudinal::L_3(double x[], double delta, double m, double Q, double W){
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    
    double x10 = x10_value(x20, x21, ph);
    double Y = rapidity(W, Q, z2);

    return 8.0*m/(M_PI*x20)* gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * ( gsl_pow_2(1.0-z2) + gsl_pow_2(z2) -1.0 ) * 
    ( gsl_sf_bessel_K1(2.0*m*z2*x20) * ( 1.0- x20/x21 * cos(ph) ) * N_xyz(x10, x20, x21, delta, Y) 
    - 1.0/(2.0*m*z2*x20) *exp(-gsl_pow_2(x20)/gsl_pow_2(x10) / exp(M_EULER) ) *  N_xy(x10, delta, Y)  ) * x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);

}
    
double Longitudinal::L_4(double x[], double delta, double m, double Q, double W){
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    
    double x10 = x10_value(x20, x21, ph);
    double Y = rapidity(W, Q, z2);

    return 8.0*m/(M_PI*x20) * N_xyz(x10, x20, x21, delta, Y) * gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * ( 1.0- x20/x21 * cos(ph) ) * ( gsl_sf_bessel_K1(2.0*m*z2*x20) - 1.0/(2.0*m*z2*x20) )  * x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);
}

double Longitudinal::L_BK(double x[], double delta, double m, double Q, double W){
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    
    double x10 = x10_value(x20, x21, ph);
    double Y = rapidity(W, Q, z2);

    // double kernel0 = N_c / (2*Cf) * gsl_pow_2(x10) / gsl_pow_2( x20 * x21 ) ;
    // double kernel0 = N_c / (2*Cf) * (gsl_pow_2(x10) / gsl_pow_2( x20 * x21 )  + 1/(x20*x20) * (alpha_s(x20)/alpha_s(x21)-1) + 1/(x21*x21) * (alpha_s(x21)/alpha_s(x20)-1) );
    // return 2.0 / (M_PI*z2) * kernel0 * sigma0 * ( -S_xy(x20, Y)*S_xy(x21, Y) + S_xy(x10, Y) ) * gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * x20 *x21 * 2.0 *M_PI*gsl_sf_bessel_J0( bessel_J_argument )*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI;

    return 2.0 / (M_PI*z2) * ( N_xyz(x10, x20, x21, delta, Y) - N_xy(x10, delta, Y) ) * gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * gsl_pow_2(x10) / gsl_pow_2( x20 * x21 )  * x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);
}


double Longitudinal::L_rcBK(double x[], double delta, double m, double Q, double W){
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    
    double x10 = x10_value(x20, x21, ph);
    double Y = rapidity(W, Q, z2);

    double kernel =  (gsl_pow_2(x10) / gsl_pow_2( x20 * x21 )  + 1/(x20*x20) * (alpha_s(x20)/alpha_s(x21)-1) + 1/(x21*x21) * (alpha_s(x21)/alpha_s(x20)-1) );

    return 2.0 / (M_PI*z2) * ( N_xyz(x10, x20, x21, delta, Y) - N_xy(x10, delta, Y) ) * gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * kernel  * x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);
}

double Longitudinal::L_KCBK(double x[], double delta, double m, double Q, double W){
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    
    double x10 = x10_value(x20, x21, ph);
    double Y = rapidity(W, Q, z2);


    double delta012 = fmax(0.0, log( fmin(x20*x20,x21*x21)/(x10*x10) ));
    double kernel0 =  (gsl_pow_2(x10) / gsl_pow_2( x20 * x21 )  + 1/(x20*x20) * (alpha_s(x20)/alpha_s(x21)-1) + 1/(x21*x21) * (alpha_s(x21)/alpha_s(x20)-1) );

    if( Y - delta012 - Y0_if > 0 ) {
        return 2.0 / (M_PI*z2) * kernel0 * sigma0 * ( - S_xy(x20, Y-delta012)*S_xy(x21, Y-delta012) + S_xy(x10, Y) ) * gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * x20 *x21 * 2.0 *M_PI*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);
    } else {
        return 0.0;
    }
}

// Integrand for the LO part of the calculation.
double Longitudinal::qq_LO(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double Y = log(1.0/x_rap);


    return N_xy(x10, delta, Y)*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * 2*M_PI * x10 * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the dipole NLO part of the calculation, where only a 1-dimensional integral has to be done. Uses decay width as the coefficient!
double Longitudinal::qq_NLO_1_dim_dw(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double Y = log(1.0/x_rap);

    return N_xy(x10, delta, Y)*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * ( 6.0-gsl_pow_2(M_PI)/3.0 + Gamma_Lm(m, Q) + L(m, Q) - 3.0*log(x10*m/2.0)-3.0*M_EULER )*2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the dipole NLO part of the calculation, where only a 1-dimensional integral has to be done. Uses renormalized wave function as the coefficient!
double Longitudinal::qq_NLO_1_dim_wf(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double Y = log(1.0/x_rap);

    return N_xy(x10, delta, Y)*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * ( 2.0-gsl_pow_2(M_PI)/3.0 + Gamma_Lm(m, Q) + L(m, Q) - 3.0*log(x10*m/2.0)-3.0*M_EULER )*2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the K_0 part of the dipole NLO integral.
double Longitudinal::qq_NLO_K0(double x[], size_t dim, void *params) {
    dimension_error(dim, 2);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double z = x[1];
    double Y = log(1.0/x_rap);


    return N_xy(x10, delta, Y)*K_0_integrand(z, x10, m, Q)*2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(z, delta, x10);
}

// Integrand for the J_1 part of the dipole NLO integral.
double Longitudinal::qq_NLO_J_1(double x[], size_t dim, void *params) {
    dimension_error(dim, 2);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double xi = x[1];
    double Y = log(1.0/x_rap);

    return N_xy(x10, delta, Y)*J_1_integrand(xi, x10, m, Q)*2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the J_2 part of the dipole NLO integral.
double Longitudinal::qq_NLO_J_2(double x[], size_t dim, void *params) {
    dimension_error(dim, 3);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double xi = x[1];
    double x_var = x[2];
    double Y = log(1.0/x_rap);
    
    return N_xy(x10, delta, Y)*J_2_integrand(xi, x_var, x10, m, Q)*2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the qqg-part in the sub scheme. Meaning: doesn't contain the BK part.
double Longitudinal::qqg_dim4_sub(double x[], size_t dim, void *params) {
    dimension_error(dim, 4);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return L_3(x, delta, m, Q, W)+L_4(x, delta, m, Q, W)+L_5(x, delta, m, Q, W);
}

// Integrand for the qqg-part in the unsub scheme.
double Longitudinal::qqg_dim4_unsub(double x[], size_t dim, void *params) {
    dimension_error(dim, 4);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return L_3(x, delta, m, Q, W)+L_4(x, delta, m, Q, W)+L_5(x, delta, m, Q, W)+L_BK(x, delta, m, Q, W);
    // return L_3(x, delta, m, Q)+L_4(x, delta, m, Q)+L_5(x, delta, m, Q)+L_KCBK(x, delta, m, Q);
}

// Integrand for the BK part of the qqg integral.
double Longitudinal::qqg_BK(double x[], size_t dim, void *params) {
    dimension_error(dim, 4);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return L_BK(x, delta, m, Q, W);
}

// Integrand for the BK part of the qqg integral. Instead of using LO BK, here we use rcBK.
double Longitudinal::qqg_rcBK(double x[], size_t dim, void *params) {
    dimension_error(dim, 4);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return L_rcBK(x, delta, m, Q, W);
}

// KCBK instead of BK for the qqg part.
double Longitudinal::qqg_KCBK(double x[], size_t dim, void *params) {
    dimension_error(dim, 4);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return L_KCBK(x, delta, m, Q, W);
}

// Integrand for the 6-dimensional integral of the qqg part.
double Longitudinal::qqg_dim6(double x[], size_t dim, void *params) {
    dimension_error(dim, 6);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return M_1(x, delta, m, Q, W)+M_2(x, delta, m, Q, W);
}

// Relativistic correction
double Longitudinal::qq_rel_002(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double Y = log(1.0/x_rap);


    return N_xy(x10, delta, Y)* ( gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*Q*Q + m*m )) - Q*Q*x10/(8.0 * sqrt( 1.0/4.0*Q*Q + m*m ) ) * gsl_sf_bessel_K1(x10 * sqrt( 1.0/4.0*Q*Q + m*m ) ) ) * 2*M_PI * x10 * delta_factor_qq(0.5, delta, x10);
}


// Relativistic correction
double Longitudinal::qq_rel_200(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double Y = log(1.0/x_rap);


    return N_xy(x10, delta, Y)* gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*Q*Q + m*m )) * m*m * x10*x10 / 4.0 * 2*M_PI * x10  * delta_factor_qq(0.5, delta, x10);
}


// Integrand for calculating the phenomenological corrections.
// This is simply LO integrand where the substituion N -> dN/dY has been made.
double Longitudinal::lambda_integrand(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double Y = log(1.0/x_rap);

    return dNdY(x10, delta, Y)*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * 2*M_PI * x10 * delta_factor_qq(0.5, delta, x10);
}
