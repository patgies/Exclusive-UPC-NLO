// Methods for using dipole amplitude.

#include <gsl/gsl_math.h>
#include <iostream>

#include <amplitudelib.hpp>

#include "dipole_amplitudes.hpp"
#include "constants.hpp"
#include "b_integral.hpp"
using namespace std;

AmplitudeLib *N;
bool amp_init_bool = false;

// Read amplitude from a data file so that it can be used later.
void initialize_amplitude(string file) {
    N = new AmplitudeLib(file);
    amp_init_bool = true;
}


// Qs^2 for GBW model.
double Qs2_GBW( double x ) {
    double x0 = 3.0e-4;
    double lambda_GBW = 0.29;
    // double x0 = 4.0e-5;
    // double lambda_GBW = 0.28;
    return pow( x0 / x, lambda_GBW);
}



// Gives the Fourier transform dipole amplitude N_xy = 1-S_xy. Here r is the distance between the quark and antiquark.
// TODO: delta dependence not implemented!
double N_xy(double r, double delta, double Y) {
    if(b_dependence_bool) {
        if( r < 1.0001 * 1.0e-5 ) {
            return 0.0;
        }
        else if( r > 0.9999 * 25.25 ) {
            return 1.0;
        }
        return qq_dipole_integrated( r, Y );
    }
    else return (1-S_xy(r, Y)) * sigma0/2.0; // The case where the dipole amplitude depends only weakly on b. Integrate over b -> sigma0/2.
}

double S_GBW(double r, double Y) {
    // 1 - (GBW dipole amplitude)
    double x = exp( -Y );
    return exp(- gsl_pow_2(r/2.0) * Qs2_GBW(x) );    
}

// Reads S from file and interpolates
double S_file(double r, double Y) {
    if (!amp_init_bool) {
        cerr << "Dipole amplitude not initialized! Cannot evaluate it." << endl;
    }
    if( r < 1.0001 * N->MinR() ) {
        return 1.0;
    }
    else if( r > 0.9999 * N->MaxR() ) {
        return 0.0;
    }
    else {
        return 1.0-N->DipoleAmplitude(r, Y);
    }
}


// S_matrix for the dipole-nucleus scattering.
double S_xy(double r, double Y){
    // double Y_corr = Y + eta_corr(r);
    double Y_corr = target_rapidity(Y,r);
    if(Y_corr<Y0_if) Y_corr = Y0_if;
    if (dipole_file_bool) return S_file(r, Y_corr);
    else return S_GBW(r, Y_corr);
}

/* 
Gives the Fourier transform of the qqg dipole amplitude N_xyz = 1-S_xyz. 
rij = |xi-xj|; x0 = quark, x1 = antiquark, x2 = gluon transverse coordinates
TODO: delta dependence not implemented
*/
double N_xyz(double r10, double r20, double r21, double delta, double Y) {
    if( b_dependence_bool ) {
        // Handle r<r_min and r>r_max.
        double r_min = 1.0e-5;
        double r_max = 25.25;
        if( r10 < r_min ) r10=r_min*1.00001;
        if( r20 < r_min ) r20=r_min*1.00001;
        if( r21 < r_min ) r21=r_min*1.00001;
        if( r10 > r_max ) r10=r_max*0.9999999;
        if( r20 > r_max ) r20=r_max*0.9999999;
        if( r21 > r_max ) r21=r_max*0.9999999;
        return qqg_dipole_integrated( r10, r20, r21, Y);
    }
    else return  sigma0/2.0 * (  1 - N_c/(2.0*C_F) *( S_xy(r20, Y)*S_xy(r21, Y) - 1.0/(N_c*N_c) * S_xy(r10,Y) ));
}

// Derivative of the dipole amplitude. Needed for calculating phenomenological corrections.
double dNdY(double r, double delta, double Y) {
    double epsilon = 5.0e-2;
    return ( N_xy(r, delta, Y+epsilon ) - N_xy(r, delta, Y-epsilon) ) / (2.0*epsilon);
    // return ( -1.0/12.0 * N_xy(r, delta, Y+2.0*epsilon ) +2.0/3.0 * N_xy(r, delta, Y+epsilon) +1.0/12.0 * N_xy(r, delta, Y-2.0*epsilon ) -2.0/3.0 * N_xy(r, delta, Y-epsilon) ) / (epsilon);
        
}