/*
* Integrands for the longitudinal photon. The common prefactor e*ef*m/(pi)*sqrt(Nc/2)*2*(wavefunction factor) has been left out.
* See the article for the definitions of the functions.
*/

#include <gsl/gsl_math.h>
#include <gsl/gsl_sf_bessel.h>
#include <gsl/gsl_sf_dilog.h>
#include <gsl/gsl_errno.h>
#include <cmath>
#include <iostream>

#include "integrands_T.hpp"
#include "constants.hpp"
#include "dipole_amplitudes.hpp"
using namespace std;

// Heaviside theta
double Transverse::theta(double x) {return (x>0) ? 1:0;}

// Checks that the integrand has the correct number of integration variables.
void Transverse::dimension_error(size_t dim, size_t corr_dim) {
    if (dim != corr_dim)
        {
        cerr << "Error: Integrating over wrong number of dimensions! Correct number: " << corr_dim << ". Got: " << dim <<".\n";
        exit(1);
        }
}

// x10 in terms of x20, x21 and ph = the angle between x20 and x21.
double Transverse::x10_value(double x20, double x21, double ph){
    return sqrt( gsl_pow_2( x20 ) + gsl_pow_2( x21 ) - 2.0 * x20 * x21 * cos(ph) ) + 1.0e-15;
}

// Running alpha_s
double Transverse::alpha_s_run( double r ) {
    return 4.0*M_PI / ( beta_0 * log( pow( pow(mu_0/lambda_QCD, 2.0/c_small ) + pow(2.0*C_big/(r*lambda_QCD), 2.0/c_small), c_small ) ) );
}

double Transverse::alpha_s( double r) {
    if (alpha_s_run_bool)
        return alpha_s_run( r );
    else
        return alpha_s_const;
}

// alpha_s for the qqg-part, where the running alpha_s depends on the sizes of the dipoles.
double Transverse::alpha_s3( double x10, double x20, double x21) {

    if (!alpha_s_run_bool)
        return alpha_s_const;

    double r;
    if( *alpha_s_scheme == "bal+sd" ) {
        r = fmin(x10,  fmin(x20,x21) );        
    }
    else if( *alpha_s_scheme == "parent_dipole" ) {
        r = x10;        
    } else {
        cerr << "Wrong alpha_s scheme: " << *alpha_s_scheme << endl;
        exit(1);
    }
    return alpha_s( r );
}

// Implements delta dependence for the dipole integrals.
double Transverse::delta_factor_qq(double z, double Delta, double x10) {
    return gsl_sf_bessel_J0(x10*Delta*abs(z-0.5) );
}

// Implements delta dependence of the qqg part.
double Transverse::delta_factor_qqg(double z2, double Delta, double x20, double x21, double ph) {
    double bessel_J_argument = Delta * sqrt( gsl_pow_2( (z2-1.0/6.0) * x20 ) + 1.0/36.0 * x21 * x21 - 1.0/3.0*(z2-1.0/6.0)*x20*x21*cos(ph)  );
    return gsl_sf_bessel_J0( bessel_J_argument );
}

//Integrand of J_1. Needs to be integrated over xi to get J_1.
double Transverse::J_1_integrand(double xi, double x10, double m, double Q){
    return 2.0 * ( 1.0/xi * ( -2.0*log(xi)/(1.0-xi) + (1.0+xi)/2.0 ) * ( gsl_sf_bessel_K0( x10 * sqrt(1.0/4.0*Q*Q+m*m) ) - gsl_sf_bessel_K0(x10 * sqrt( 1.0/4.0*Q*Q+m*m + xi*0.5/(1.0-xi)*m*m ) ) ) 
        +1.0/2.0 * (-3.0/(2.0*(1.0-xi)) +1.0/2.0) * gsl_sf_bessel_K0(x10 * sqrt( 1.0/4.0*Q*Q+m*m + xi*0.5/(1.0-xi)*m*m ) ) );
}

//Integrand of J_2. Needs to be integrated over xi and x to get J_2.
double Transverse::J_2_integrand(double xi, double x, double x10, double m, double Q) {
    double eta = (1.0-xi)*(1.0-x)* ( x*(1.0-xi) +2.0*xi );
    double nu = sqrt( (0.25*Q*Q+m*m)/(1-x) +xi*m*m*xi/( (1.0-xi)*(1.0-x)*( x* (1.0-xi)+2.0*xi ) ) );
    return 2.0 * ( -1.0/2.0 * gsl_pow_2(1.0-xi)/eta * gsl_sf_bessel_K0(x10*nu) 
        -0.5 *gsl_pow_2(1-xi) * (-x-xi) /(eta * (0.25*Q*Q+m*m-nu*nu)) * 
        (   nu/x10 * ( 2.0*gsl_sf_bessel_K1(x10*nu) - x10*nu*gsl_sf_bessel_Kn(2, x10*nu) )
            -sqrt(0.25*Q*Q+m*m)/x10 * ( 2.0 * gsl_sf_bessel_K1(x10*sqrt(0.25*Q*Q+m*m)) - x10*sqrt(0.25*Q*Q+m*m) * gsl_sf_bessel_Kn(2, x10*sqrt(0.25*Q*Q+m*m))) ) 
        + m*m * x*gsl_pow_2(1-xi)*( 1.0+0.5*xi*xi )/(x*(1.0-xi)+2.0*xi) / (eta * (0.25*Q*Q+m*m-nu*nu)) * (gsl_sf_bessel_K0(x10*nu) - gsl_sf_bessel_K0(x10*sqrt(0.25*Q*Q+m*m))  )  );
}

//Integrand of K_0. Needs to be integrated over z to get K_0.
double Transverse::K_0_integrand(double z, double x10, double m, double Q) {
    double tau = 2.0*m*x10*abs(0.5-z);
    return 1.0/gsl_pow_2(z-0.5) * ( 8.0*z*(1.0-z)*gsl_sf_bessel_K0(x10*sqrt(z*(1.0-z)*Q*Q+m*m)) * ( gsl_sf_bessel_K0(tau) - 1.0/(2.0*(1.0-z)) * ( gsl_sf_bessel_K0(tau)-tau/2.0*gsl_sf_bessel_K1(tau) ) )
    - 2.0*gsl_sf_bessel_K0(x10 * sqrt( 1.0/4.0*Q*Q+m*m )) * (0.5+(z-0.5)*(1.0+2.0*M_EULER + 2.0*log(tau/2.0) ) ) )
            + 4.0*z*x10*sqrt(z*(1.0-z)*Q*Q+m*m) * gsl_sf_bessel_K1(x10*sqrt(z*(1.0-z)*Q*Q+m*m))*gsl_sf_bessel_K0(tau) * ( 1.0+ gsl_pow_2(1.0-2.0*z) );
}

double Transverse::L(double m, double Q) {

    double gamma = sqrt(1.0+4.0*gsl_pow_2(m)/gsl_pow_2(Q));

    return gsl_sf_dilog(1.0/gsl_pow_2(gamma) );

}

double Transverse::Omega_V(double m, double Q) {
    double gamma = sqrt(1.0+4.0*gsl_pow_2(m)/gsl_pow_2(Q));
    return -4.0 * ( log(0.5) + gamma * log( (1+gamma)/gamma ) ) + 2.0 * ( 1.0-gamma+m*m/(Q*Q)) * log( (1.0/4.0*Q*Q+m*m)/(m*m) ) ;
}


double Transverse::g_int(int a, int b, double Qbar, double mf, double x2, double x3, double omega, double lambda, double y) {
    // Integrands of the functions G^(a;b)_(x) that appear in the qqg-part. Here the u-integral has been done, and only one integral remains.
    // The integration varialbe is y = omega * t

    double value = 1.0/pow( y, 0.5*(2.0-a+b) ) * pow( 2.0, a+b-1.0 ) * pow(omega, b-1.0) 
                    * pow(( y*lambda * mf*mf + Qbar*Qbar + mf*mf ) / ( y*x3*x3 + omega*x2*x2 ), 0.5*(a+b-2.0) )
                    * gsl_sf_bessel_Kn( a+b-2, sqrt(1.0/y * ( y*lambda * mf*mf + Qbar*Qbar + mf*mf ) * ( y*x3*x3 + omega*x2*x2 )) ) ;

    return value;
}

double Transverse::M(double x[], double delta, double m, double Q, double W) {
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    double t = x[4];
    double u = x[5];

    double x10 = x10_value(x20, x21, ph);
    double Y;
    if (inv_mass_rapidity_bool) {
        Y = invariant_mass_rapidity_qqg( x10, x20, x21, 0.5 - z2, 0.5, z2, W );
    }
    else {
        Y = rapidity(W, Q, z2); 
    }



    if( minus_cutoff_bool == true && z2_min_minus_cutoff( W, Q, x10, x20, x21) > z2 ) return 0.0;


    double omega_j = (1.0/2.0-z2) * z2 * 8.0;
    double lambda_j = 1.0/2.0*z2/(1.0/2.0-z2);
    double Q_j = 0.5 * Q;
    double b_j = sqrt( gsl_pow_2( (1.0 - 2.0*z2) * x20 ) + x21 * x21 - 2.0 * (1.0-2.0*z2) * x20 *x21 * cos( ph ) );
    double r_j = x20;

    double omega_k = 1.0/2.0*z2/(1.0/2.0-z2)/gsl_pow_2(1.0/2.0+z2);
    double lambda_k = 2.0*z2*(1.0/2.0-z2);
    double Q_k = sqrt( (1.0/2.0-z2) * (1.0/2.0+z2)) * Q;
    double b_k = sqrt( gsl_pow_2( 1.0 / (1.0 + 2.0*z2) * x21 ) + x20 * x20 - 2.0 / (1.0 + 2.0*z2) * x20 *x21 * cos( ph ) );
    double r_k = x21;

    double rj_dot_bj = x20*x21*cos(ph)-(1.0-2.0*z2)*x20*x20;
    double rk_dot_bk = -x20*x21*cos(ph) + 1.0/(1.0+2.0*z2)*x21*x21 ;

    double part_j = m/r_j * gsl_sf_bessel_K1(2.0*m*z2*r_j) * ( r_j*r_j/t*( gsl_pow_2(1-z2)+z2*z2 ) * (exp(-t*omega_j*lambda_j*m*m)-1)+z2*z2*(2.0*z2-1.0)*rj_dot_bj/u*exp(-t*omega_j*lambda_j*m*m) )
        - z2*gsl_sf_bessel_K0(2*m*z2*r_j)* ( rj_dot_bj /(u*t)* (2.0*z2-1)/4.0 * (exp(-t*omega_j*lambda_j*m*m)-1)+8.0*m*m*z2*z2*exp(-t*omega_j*lambda_j*m*m) );
    double part_k = m/r_j * gsl_sf_bessel_K1(2.0*m*z2*r_j) * ( r_j*r_k*cos(ph)/(t*(2.0*z2+1.0))* (exp(-t*omega_k*lambda_k*m*m)-1)+z2*z2*gsl_pow_2(2.0*z2-1.0)/gsl_pow_2(1.0+2.0*z2)*rk_dot_bk/u*exp(-t*omega_k*lambda_k*m*m) )
        + z2*gsl_sf_bessel_K0(2*m*z2*r_j)* rk_dot_bk /(u*t)* (2.0*z2+1)/4.0 * (exp(-t*omega_k*lambda_k*m*m)-1);

    return N_xyz(x10,x20,x21,delta,Y)/(M_PI*u*t) * ( theta(u/omega_j-t) * exp( - u*(Q_j*Q_j+m*m) - b_j*b_j/(4.0*u)-r_j*r_j/(4.0*t) ) *part_j
        -   theta(u/omega_k-t) * exp( - u*(Q_k*Q_k+m*m) - b_k*b_k/(4.0*u)-r_k*r_k/(4.0*t) ) *part_k  )
        *  x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);

}


double Transverse::M_fast(double x[], double delta, double m, double Q, double W) {
    // Another implementation of M, requires only 5 integrals instead of 6.
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    double y = x[4];

    double x10 = x10_value(x20, x21, ph);
    double Y;
    if (inv_mass_rapidity_bool) {
        Y = invariant_mass_rapidity_qqg( x10, x20, x21, 0.5 - z2, 0.5, z2, W );
    }
    else {
        Y = rapidity(W, Q, z2); 
    }


    if( minus_cutoff_bool == true && z2_min_minus_cutoff( W, Q, x10, x20, x21 ) > z2 ) return 0.0;


    double omega_j = (1.0/2.0-z2) * z2 * 8.0;
    double lambda_j = 1.0/2.0*z2/(1.0/2.0-z2);
    double Q_j = 0.5 * Q;
    double b_j = sqrt( gsl_pow_2( (1.0 - 2.0*z2) * x20 ) + x21 * x21 - 2.0 * (1.0-2.0*z2) * x20 *x21 * cos( ph ) );
    double r_j = x20;

    double omega_k = 1.0/2.0*z2/(1.0/2.0-z2)/gsl_pow_2(1.0/2.0+z2);
    double lambda_k = 2.0*z2*(1.0/2.0-z2);
    double Q_k = sqrt( (1.0/2.0-z2) * (1.0/2.0+z2)) * Q;
    double b_k = sqrt( gsl_pow_2( 1.0 / (1.0 + 2.0*z2) * x21 ) + x20 * x20 - 2.0 / (1.0 + 2.0*z2) * x20 *x21 * cos( ph ) );
    double r_k = x21;

    double rj_dot_bj = x20*x21*cos(ph)-(1.0-2.0*z2)*x20*x20;
    double rk_dot_bk = -x20*x21*cos(ph) + 1.0/(1.0+2.0*z2)*x21*x21 ;

    double g_12_bar_j = g_int(1, 2, Q_j, m, r_j, b_j, omega_j, lambda_j, y)-g_int(1, 2, Q_j, m, r_j, b_j, omega_j, 0.0, y);
    double g_12_bar_k = g_int(1, 2, Q_k, m, r_k, b_k, omega_k, lambda_k, y)-g_int(1, 2, Q_k, m, r_k, b_k, omega_k, 0.0, y);
    double g_22_bar_j = g_int(2, 2, Q_j, m, r_j, b_j, omega_j, lambda_j, y)-g_int(2, 2, Q_j, m, r_j, b_j, omega_j, 0.0, y);
    double g_22_bar_k = g_int(2, 2, Q_k, m, r_k, b_k, omega_k, lambda_k, y)-g_int(2, 2, Q_k, m, r_k, b_k, omega_k, 0.0, y);

    double g_21_j = g_int(2, 1, Q_j, m, r_j, b_j, omega_j, lambda_j, y);
    double g_21_k = g_int(2, 1, Q_k, m, r_k, b_k, omega_k, lambda_k, y);

    double g_11_j = g_int(1, 1, Q_j, m, r_j, b_j, omega_j, lambda_j, y);


    double part_j = m/r_j * gsl_sf_bessel_K1(2.0*m*z2*r_j) * ( r_j*r_j*( gsl_pow_2(1-z2)+z2*z2 ) * (g_12_bar_j)+z2*z2*(2.0*z2-1.0)*rj_dot_bj*g_21_j )
        - z2*gsl_sf_bessel_K0(2*m*z2*r_j)* ( rj_dot_bj * (2.0*z2-1)/4.0 * (g_22_bar_j)+8.0*m*m*z2*z2*g_11_j );
    double part_k = m/r_j * gsl_sf_bessel_K1(2.0*m*z2*r_j) * ( r_j*r_k*cos(ph)/((2.0*z2+1.0))* (g_12_bar_k)+z2*z2*gsl_pow_2(2.0*z2-1.0)/gsl_pow_2(1.0+2.0*z2)*rk_dot_bk*g_21_k )
        + z2*gsl_sf_bessel_K0(2*m*z2*r_j)* rk_dot_bk * (2.0*z2+1)/4.0 * (g_22_bar_k);

    return N_xyz(x10,x20,x21,delta,Y)/(M_PI) * (  part_j -  part_k  )
        *  x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);

}


double Transverse::L_1(double x[], double delta, double m, double Q, double W){
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];

    double x10 = x10_value(x20, x21, ph);
    double Y;
    if (inv_mass_rapidity_bool) {
        Y = invariant_mass_rapidity_qqg( x10, x20, x21, 0.5 - z2, 0.5, z2, W );
    }
    else {
        Y = rapidity(W, Q, z2); 
    }


    if( minus_cutoff_bool == true && z2_min_minus_cutoff( W, Q, x10, x20, x21 ) > z2 ) return 0.0;


    double omega_j = (1.0/2.0-z2) * z2 * 8.0;
    double lambda_j = 1.0/2.0*z2/(1.0/2.0-z2);
    double Q_j = 0.5 * Q;
    double b_j = sqrt( gsl_pow_2( (1.0 - 2.0*z2) * x20 ) + x21 * x21 - 2.0 * (1.0-2.0*z2) * x20 *x21 * cos( ph ) );
    double r_j = x20;

    double omega_k = 1.0/2.0*z2/(1.0/2.0-z2)/gsl_pow_2(1.0/2.0+z2);
    double Q_k = sqrt( (1.0/2.0-z2) * (1.0/2.0+z2)) * Q;
    double b_k = sqrt( gsl_pow_2( 1.0 / (1.0 + 2.0*z2) * x21 ) + x20 * x20 - 2.0 / (1.0 + 2.0*z2) * x20 *x21 * cos( ph ) );
    double r_k = x21;


    double rj_dot_bj = x20*x21*cos(ph)-(1.0-2.0*z2)*x20*x20;
    double rk_dot_bk = -x20*x21*cos(ph) + 1.0/(1.0+2.0*z2)*x21*x21 ;

    double zeta = x10 * sqrt( 1.0/4.0*Q*Q+m*m );
    double zeta_j = sqrt( ( Q_j*Q_j+m*m )*( b_j*b_j+omega_j*r_j*r_j ) ) ; 
    double zeta_k = sqrt( ( Q_k*Q_k+m*m )*( b_k*b_k+omega_k*r_k*r_k ) );

    double J_l = 1.0/gsl_pow_2(2.0*M_PI) * sqrt( (Q_j*Q_j+m*m+lambda_j*m*m)/(b_j*b_j+omega_j*r_j*r_j) ) 
        *gsl_sf_bessel_K1( sqrt( ( Q_j*Q_j+m*m*(1.0+lambda_j) )*( b_j*b_j+omega_j*r_j*r_j ) )  );

    double part1 = 8.0*m/(M_PI*x20) * N_xyz(x10,x20,x21,delta,Y) * 
                    ( gsl_sf_bessel_K1(2.0*m*z2*x20) * ( gsl_pow_2(1-z2) + z2*z2 ) *gsl_sf_bessel_K0(zeta_j) -1.0/(2.0*m*z2*x20) * gsl_sf_bessel_K0(zeta) 
                    -gsl_sf_bessel_K1(2.0*m*z2*x20)/( 1.0+2.0*z2 ) *gsl_sf_bessel_K0(zeta_k)*x20/x21 * cos(ph) +1.0/(2.0*m*z2*x20) * gsl_sf_bessel_K0(zeta) *x20/x21 * cos(ph) );
    double part2 = gsl_sf_bessel_K0(zeta)*8.0/(M_PI*x20*x20)*(1.0-z2)*exp(-x20*x20/ ( x10*x10*exp(M_EULER) ) ) * N_xy(x10,delta,Y);
    double part3 = -64.0*M_PI * gsl_sf_bessel_K0(2.0*m*z2*x20)*z2*z2*(1.0-2.0*z2)*J_l*N_xyz(x10, x20, x21, delta,Y);
    double part4 = -4.0*z2/M_PI*gsl_sf_bessel_K0(2.0*m*z2*x20)*N_xyz(x10,x20,x21,delta,Y) * (
                    ( -1.0+2.0*z2 ) * rj_dot_bj/(x20*x20) * sqrt( (Q_j*Q_j+m*m)/(b_j*b_j+omega_j*r_j*r_j)) *gsl_sf_bessel_K1(zeta_j) 
                    +(1.0+2.0*z2) * rk_dot_bk/(x21*x21) * sqrt( (Q_k*Q_k+m*m)/(b_k*b_k+omega_k*r_k*r_k)) *gsl_sf_bessel_K1(zeta_k) ) ;

    return (part1+part2+part3+part4)
        * x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);

}


double Transverse::L_BK(double x[], double delta, double m, double Q, double W){
    double x20 = x[0];
    double x21 = x[1];
    double ph = x[2];
    double z2 = x[3];
    
    double x10 = x10_value(x20, x21, ph);
    double Y;
    if (inv_mass_rapidity_bool) {
        Y = invariant_mass_rapidity_qqg( x10, x20, x21, 0.5 - z2, 0.5, z2, W );
    }
    else {
        Y = rapidity(W, Q, z2); 
    }


    if( minus_cutoff_bool == true && z2_min_minus_cutoff( W, Q, x10, x20, x21 ) > z2 ) return 0.0;


    return 2.0 / (M_PI*z2) * ( N_xyz(x10, x20, x21, delta, Y) - N_xy(x10, delta, Y) ) * gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * gsl_pow_2(x10) / gsl_pow_2( x20 * x21 )  * x20 *x21 * 2.0 *M_PI*alpha_s3(x10,x20,x21)*2.0/3.0/M_PI * delta_factor_qqg(z2, delta, x20, x21, ph);
}


// Integrand for the LO part of the calculation.
double Transverse::qq_LO(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];


    double W = p->W;
    double Y;
    
    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }


    return N_xy(x10, delta, Y)*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * 2*M_PI * x10 * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the dipole NLO part of the calculation, where only a 1-dimensional integral has to be done. Here it is expected that this is multiplied by the decay width, NOT the wave function. TODO:check when Ivms done by Risto
double Transverse::qq_NLO_1_dim_decay_width(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];

    double W = p->W;
    double Y;
    
    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }

    return N_xy(x10, delta, Y)*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * ( -Omega_V(m,Q)+L(m,Q) -M_PI*M_PI/3.0+13.0/2.0-3.0*log( m*x10/2.0 ) -3.0*M_EULER )
            *2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the dipole NLO part of the calculation, where only a 1-dimensional integral has to be done. Here it is expected that this is multiplied by the wave function, NOT the decay width. TODO:check when Ivms done by Risto
double Transverse::qq_NLO_1_dim_wave_function(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];


    double W = p->W;
    double Y;
    
    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }

    return N_xy(x10, delta, Y)*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * ( -Omega_V(m,Q)+L(m,Q) -M_PI*M_PI/3.0+5.0/2.0-3.0*log( m*x10/2.0 ) -3.0*M_EULER )
            *2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the K part of the dipole NLO integral.
double Transverse::qq_NLO_K(double x[], size_t dim, void *params) {
    dimension_error(dim, 2);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double z = x[1];


    double W = p->W;
    double Y;
    
    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }


    return N_xy(x10, delta, Y)*K_0_integrand(z, x10, m, Q)*2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(z, delta, x10);
}

// Integrand for the J_1 part of the dipole NLO integral.
double Transverse::qq_NLO_J_1(double x[], size_t dim, void *params) {
    dimension_error(dim, 2);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double xi = x[1];


    double W = p->W;
    double Y;
    
    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }

    return N_xy(x10, delta, Y)*J_1_integrand(xi, x10, m, Q)*2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the J_2 part of the dipole NLO integral.
double Transverse::qq_NLO_J_2(double x[], size_t dim, void *params) {
    dimension_error(dim, 3);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];
    double xi = x[1];
    double x_var = x[2];


    double W = p->W;
    double Y;
    
    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }
    
    return N_xy(x10, delta, Y)*J_2_integrand(xi, x_var, x10, m, Q)*2*M_PI*x10*alpha_s(x10)*2.0/3.0/M_PI * delta_factor_qq(0.5, delta, x10);
}

// Integrand for the qqg-part in the sub scheme. Meaning: doesn't contain the BK part.
double Transverse::qqg_dim4_sub(double x[], size_t dim, void *params) {
    dimension_error(dim, 4);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return L_1(x, delta, m, Q, W);
}

// Integrand for the qqg-part in the unsub scheme.
double Transverse::qqg_dim4_unsub(double x[], size_t dim, void *params) {
    dimension_error(dim, 4);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return L_1(x, delta, m, Q, W)+L_BK(x, delta, m, Q, W);
}

// Integrand for the BK part of the qqg integral.
double Transverse::qqg_BK(double x[], size_t dim, void *params) {
    dimension_error(dim, 4);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return L_BK(x, delta, m, Q, W);
}


// Integrand for the 5-dimensional integral of the qqg part. 
// REPLACES qqg_dim6.
double Transverse::qqg_dim5(double x[], size_t dim, void *params) {
    dimension_error(dim, 5);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return M_fast(x, delta, m, Q, W);
}



// Integrand for the 6-dimensional integral of the qqg part.
double Transverse::qqg_dim6(double x[], size_t dim, void *params) {
    dimension_error(dim, 6);
    struct integ_params *p = (struct integ_params *)params;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double W = p->W;
    return M(x, delta, m, Q, W);
}

// Relativistic correction
double Transverse::qq_rel_002_pp(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];


    double W = p->W;
    double Y;

    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }
    double zeta = x10 * sqrt(0.25*Q*Q+m*m);


    return -x10*x10*Q*Q/( 8.0*zeta ) * gsl_sf_bessel_K1(zeta) * N_xy(x10, delta, Y) * 2*M_PI * x10 * delta_factor_qq(0.5, delta, x10);
}


// Relativistic correction
double Transverse::qq_rel_200_pp(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];


    double W = p->W;
    double Y;
    
    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }


    double zeta = x10 * sqrt(0.25*Q*Q+m*m);

    return 0.5*m*m*x10*x10*gsl_sf_bessel_K0(zeta) *N_xy(x10, delta, Y) * 2*M_PI * x10  * delta_factor_qq(0.5, delta, x10);
}

// Relativistic correction
// Note: the associated wave function factor is i*phi_pm(0,1,0)
double Transverse::qq_rel_100_pm(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];


    double W = p->W;
    double Y;

    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }

    double zeta = x10 * sqrt(0.25*Q*Q+m*m);

    return -zeta*gsl_sf_bessel_K1(zeta) * N_xy(x10, delta, Y)  * 2*M_PI * x10 * delta_factor_qq(0.5, delta, x10);
}




// Integrand for calculating the phenomenological corrections.
// This is simply LO integrand where the substituion N -> dN/dY has been made.
double Transverse::lambda_integrand(double x[], size_t dim, void *params) {
    dimension_error(dim, 1);
    struct integ_params *p = (struct integ_params *)params;
    string *Y_string = p->Y;
    // double x_rap = p->x;
    double delta = p->delta;
    double Q = p->Q;
    double m = p->m;
    double x10 = x[0];


    double W = p->W;
    double Y;
    
    if (*Y_string == "Y_IM" ) {
        Y = invariant_mass_rapidity_qq( x10, 0.5, 0.5, W );
    }
    else if (*Y_string == "Y_pom") {
        double x_pom = x_pom_fun(W, Q, delta);
        Y = log(1.0/x_pom); 
    }
    else if (*Y_string == "Y_0") {
        Y = Y0_if; 
    }
    else if (*Y_string == "Y_dip") {
        double x_min = x_min_fun(W, Q, delta);
        Y = log(1.0/x_min); 
    }

    return dNdY(x10, delta, Y)*gsl_sf_bessel_K0(x10 * sqrt(1.0/4.0*gsl_pow_2(Q)+gsl_pow_2(m)) ) * 2*M_PI * x10 * delta_factor_qq(0.5, delta, x10);
}
