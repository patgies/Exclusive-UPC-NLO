// Methods for computing the b integral of the dipole amplitude.

#include "b_integral.hpp"
#include "dipole_amplitudes.hpp"
#include "constants.hpp"
#include <cstring>
#include <gsl/gsl_integration.h>


AmplitudeLib *amplitudes [16];
AmplitudeLib *amp_default;

void initialize_amplitudes(string folder,  string default_file) {
    
    // char const *datafile = "data/au_kcbk_y0bk_4605_smallest/au_b_%d";
    // char const *default_file = "data/dipole-kcbk-hera-bal+sd-4.61.dip"; 
    // char const *data_constructor = folder;

    // for(int i=0; i<16; i++) {

    //     char file_0 [256];
    //     sprintf( file_0, data_constructor, 2*i );
    //     string file_path = folder + string(file_0);
    //     amplitudes[i] = new AmplitudeLib(file_path);
    // }




    for(int i=0; i<16; i++) {

        char file_0 [256];
        sprintf( file_0, folder.c_str(), 2*i );
        amplitudes[i] = new AmplitudeLib(file_0);
    }

    // char file_path_def [256];
    // strcpy( file_path_def, folder);
    // strcat( file_path_def, default_file);
    // amp_default = new AmplitudeLib(file_path_def);  
    amp_default = new AmplitudeLib(default_file);    
}


// Wood-Saxon density. Params: b
double rho_A(double x3, void *params)
{   
    double b = ((struct int_params_T_A *) params)->b;
    double r = std::sqrt( x3*x3 + b*b );
    return 1.0 / ( std::exp( (r - R_A() )/d_thickness ) + 1 );
}

// Wood-Saxon density times r^2*4*pi. For calculating \int d^3r T_A(r).
double rho_A_r2(double r, void *params)
{   
    return 1.0 / ( std::exp( (r-R_A())/d_thickness ) + 1 )*r*r*M_PI*4;
}

// Calculates the normalization constant for the Wood-Saxon and normalizes it.
void initialize_rho0() {
    double integ;
    double error;

    // struct int_params_T_A params;
    int n_eval = 200;
    gsl_integration_workspace *w = gsl_integration_workspace_alloc(n_eval);


    // params.b = 0;
    gsl_function F;
    F.function = &rho_A_r2;
    // F.params = &params;
    gsl_integration_qagiu(&F, 0.0, 1e-4, 1e-4, n_eval, w, &integ, &error);
    gsl_integration_workspace_free(w);
    rho_0 = 1.0/integ;
}

// Sets the values for the integral int_{bmin}^inf d^2b T_A(b).
void initialize_T_A() {
    double integ;
    double error;

    // struct int_params_T_A params;
    int n_eval = 200;
    gsl_integration_workspace *w = gsl_integration_workspace_alloc(n_eval);

    double b_min = 26.5;

    // params.b = 0;
    gsl_function F;
    F.function = &T_A_integrand;
    // F.params = &params;
    gsl_integration_qagiu(&F, b_min, 1e-4, 1e-4, n_eval, w, &integ, &error);
    gsl_integration_workspace_free(w);
    T_A_b_min_integral = integ;
}

// Sets the values for the integral int_{bmin}^inf d^2b T_A(b)^2.
void initialize_T_A_squared() {
    double integ;
    double error;

    // struct int_params_T_A params;
    int n_eval = 200;
    gsl_integration_workspace *w = gsl_integration_workspace_alloc(n_eval);


    double b_min = 26.5;
    // params.b = 0;
    gsl_function F;
    F.function = &T_A_squared_integrand;
    // F.params = &params;
    gsl_integration_qagiu(&F, b_min, 1e-4, 1e-4, n_eval, w, &integ, &error);
    gsl_integration_workspace_free(w);
    T_A_squared_b_min_integral = integ;
}

double T_A_integrand(double b, void *params) {
    return 2.0*M_PI*b*T_A(b);
}

double T_A_squared_integrand(double b, void *params) {
    return 2.0*M_PI*b*T_A(b)*T_A(b);
}

double T_A(double b)
{   
    double integ;
    double error;

    struct int_params_T_A params2;
    int n_eval = 200;
    gsl_integration_workspace *w = gsl_integration_workspace_alloc(n_eval);

    // double delta = ((struct int_params_T_A *) params)->delta;
    params2.b = b;
    // params2.delta = delta;
    gsl_function F;
    F.function = &rho_A;
    F.params = &params2;
    gsl_integration_qagi(&F, 1e-4, 1e-4, n_eval, w, &integ, &error);

    gsl_integration_workspace_free(w);

    return integ*rho_0;
}

double qq_dipole_integrated(double r, double Y) {
    
    double value = 0.0;

    // Calculate the integral using trapezoid method. Sum 2*pi*N*(delta b)*b
    value += 2.0*M_PI*amplitudes[0]->DipoleAmplitude(r, Y)*0.0;
    value += 2.0*M_PI*amplitudes[13]->DipoleAmplitude(r, Y)*1.5*26.0;
    for(int i=1; i<13; i++) {
        value += 2.0*M_PI*amplitudes[i]->DipoleAmplitude(r, Y)*2.0*(2.0*i);
    }

    value += T_A_b_min_integral * qq_dipole_value_b_independent(r, Y);

    // For the rest, use the proton value.
    // value += T_A0*sigma0/2.0*A*amp_default->DipoleAmplitude(r, Y);
    // double b_min = 26.5; // This values has been tried and seems to work best, N is continuous also in the saturation region.
    
    // // Calculate the integral using trapezoid method, this should be faster. Sum 2*pi*N*(delta b)*b
    
    // struct int_params_dipole_qq params;
    // params.r = r;
    // params.Y = Y;

    // for(int i=0; i<15; i++) {
    //     double b = b_min + 1.0 + 2.0*i;
    //     value += 2.0*qq_dipole_integrand_high_b(b, &params);
    // }


    // double integ;
    // double error;

    // struct int_params_dipole_qq params;
    // int n_eval = 200;
    // gsl_integration_workspace *w = gsl_integration_workspace_alloc(n_eval);

    // // double delta = ((struct int_params_T_A *) params)->delta;
    // params.r = r;
    // params.Y = Y;
    // gsl_function F;
    // F.function = &qq_dipole_integrand_high_b;
    // F.params = &params;
    // gsl_integration_qagiu(&F, b_min, 1e-4, 1e-4, n_eval, w, &integ, &error);

    // gsl_integration_workspace_free(w);


    // For the rest, use the proton value.
    // value += T_A0*sigma0/2.0*A*amp_default->DipoleAmplitude(r, Y);
    // value += integ;
    return value;
}

double qqg_dipole_integrated(double x10, double x20, double x21, double Y) {
    
    double value = 0.0;

    // Calculate the integral using trapezoid method. Sum 2*pi*N*(delta b)*b
    value += 2.0*M_PI*0.0*qqg_dipole_value(amplitudes[0]->DipoleAmplitude(x10, Y), amplitudes[0]->DipoleAmplitude(x20, Y), amplitudes[0]->DipoleAmplitude(x21, Y));
    value += 2.0*M_PI*1.5*26.0*qqg_dipole_value(amplitudes[13]->DipoleAmplitude(x10, Y), amplitudes[13]->DipoleAmplitude(x20, Y), amplitudes[13]->DipoleAmplitude(x21, Y));
    for(int i=1; i<13; i++) {
        value += 2.0*M_PI*(2.0*i)*2.0*qqg_dipole_value(amplitudes[i]->DipoleAmplitude(x10, Y), amplitudes[i]->DipoleAmplitude(x20, Y), amplitudes[i]->DipoleAmplitude(x21, Y));
    }

    value += qqg_dipole_value_b_independent(qq_dipole_value_b_independent(x10, Y), qq_dipole_value_b_independent(x20, Y), qq_dipole_value_b_independent(x21, Y));

    // For the rest, use the proton value.
    // value += T_A0*sigma0/2.0*A*amp_default->DipoleAmplitude(r, Y);
    // For high b, perform an integral.
    // double b_min = 26.5; // This values has been tried and seems to work best, N is continuous also in the saturation region.

    // struct int_params_dipole_qqg params;
    // params.x10 = x10;
    // params.x20 = x20;
    // params.x21 = x21;
    // params.Y = Y;
    
    // for(int i=0; i<15; i++) {
    //     double b = b_min + 1.0 + 2.0*i;
    //     value += 2.0*qqg_dipole_integrand_high_b(b, &params);
    // }

    // double integ;
    // double error;

    // struct int_params_dipole_qqg params;
    // int n_eval = 200;
    // gsl_integration_workspace *w = gsl_integration_workspace_alloc(n_eval);

    // params.x10 = x10;
    // params.x20 = x20;
    // params.x21 = x21;
    // params.Y = Y;
    // gsl_function F;
    // F.function = &qqg_dipole_integrand_high_b;
    // F.params = &params;
    // gsl_integration_qagiu(&F, b_min, 1e-4, 1e-4, n_eval, w, &integ, &error);

    // gsl_integration_workspace_free(w);


    // value += integ;
    return value;
}

double qqg_dipole_value( double N_10, double N_20, double N_21 ) {
    return  N_c/(2.0*C_F) * ( N_20+N_21-N_21*N_20-1/(N_c*N_c)*N_10 );
}

// Here one has to use b-independent values for the dipole amplitudes N_xy!
double qqg_dipole_value_b_independent( double N_10, double N_20, double N_21) {
    return  N_c/(2.0*C_F) * ( (N_20 + N_21-1/(N_c*N_c)*N_10) * T_A_b_min_integral -N_21*N_20*T_A_squared_b_min_integral );
}


double qq_dipole_value_high_b(double r, double Y, double b) {
    return T_A(b) * sigma0/2.0 * A * amp_default->DipoleAmplitude(r, Y);
}

// The value of the dipole amplitude divided by T(b) (should work at high b, doesn't at low b)
double qq_dipole_value_b_independent(double r, double Y) {
    return sigma0/2.0 * A * amp_default->DipoleAmplitude(r, Y);
}


double qq_dipole_integrand_high_b(double b, void *params) {

    double r = ((struct int_params_dipole_qq *) params)->r;
    double Y = ((struct int_params_dipole_qq *) params)->Y;

    return 2.0 * M_PI * b * qq_dipole_value_high_b(r, Y, b);
}

// TODO: correct b-variables to the dipole amplitudes
double qqg_dipole_integrand_high_b(double b, void *params) {

    double x10 = ((struct int_params_dipole_qqg *) params)->x10;
    double x20 = ((struct int_params_dipole_qqg *) params)->x20;
    double x21 = ((struct int_params_dipole_qqg *) params)->x21;
    double Y = ((struct int_params_dipole_qqg *) params)->Y;

    double N_10 = qq_dipole_value_high_b( x10, Y, b);
    double N_20 = qq_dipole_value_high_b( x20, Y, b);
    double N_21 = qq_dipole_value_high_b( x21, Y, b);

    return 2.0 * M_PI * b * qqg_dipole_value( N_10, N_20, N_21)  ;
}

