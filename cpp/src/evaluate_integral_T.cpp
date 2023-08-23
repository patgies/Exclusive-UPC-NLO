// For actually evaluating the integrals needed to calculate the transverse production amplitude.

#include <gsl/gsl_monte_vegas.h>
#include <gsl/gsl_monte.h>
#include <gsl/gsl_math.h>
#include <stdlib.h>
#include <ctime>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <future>

#include "integrands_T.hpp"
#include "constants.hpp"
using namespace std;

namespace Transverse {

    double integral(gsl_monte_function f, double* xl, double* xu, int dimension, size_t calls) {
        double res, err;

        const gsl_rng_type *T;
        gsl_rng *r;

        size_t calls_warm_up = calls / 10;

        gsl_rng_env_setup ();

        T = gsl_rng_default;
        r = gsl_rng_alloc (T);


        clock_t begin = clock();

        {
            gsl_monte_vegas_state *s = gsl_monte_vegas_alloc (dimension);

            gsl_monte_vegas_integrate (&f, xl, xu, dimension, calls_warm_up, r, s,
                                        &res, &err);
            if( calls_dim_high < 200000 || calls_dim_4 < 100000 ){
                gsl_monte_vegas_integrate (&f, xl, xu, dimension, calls, r, s, &res, &err);

            }
            else {
                do
                    {
                    gsl_monte_vegas_integrate (&f, xl, xu, dimension, calls, r, s, &res, &err);
                    }
                while (fabs (gsl_monte_vegas_chisq (s) - 1.0) > 0.5); // Without this the results is unreliable, according to GSL library. But it seems to give correct enough results even without this, so this can be deleted in exchange for speed.
            }

            gsl_monte_vegas_free (s);
        }

        gsl_rng_free (r);


        clock_t end = clock();

        return res;

    }

    /**
    * Write a string that contains various values for the integrals needed to calculate the production.
    */ 
    string amplitudes_string(double W, double Q, double Delta) {
        // double x_pom = x_pom_fun(W, Q, Delta);
        // double x_min = x_min_fun(W, Q, Delta);
        double z2_min = z2_min_fun(W, Q);
        double z2_min_pom = z2_min_pom_fun(W, Q, Delta);

        struct Transverse::integ_params params_sub = {Delta, m, Q, new string("Y_dip"), W}; 
        struct Transverse::integ_params params_pom = {Delta, m, Q, new string("Y_pom"), W}; 
        struct Transverse::integ_params params_unsub = {Delta, m, Q, new string("Y_0"), W}; 
        struct Transverse::integ_params params_inv_mass = {Delta, m, Q, new string("Y_IM"), W};


        // struct Transverse::integ_params params_sub = {Delta, m, Q, x_min, W};
        // struct Transverse::integ_params params_pom = {Delta, m, Q, x_pom, W}; 
        // struct Transverse::integ_params params_unsub = {Delta, m, Q, x_max, W};

        gsl_monte_function mf_qq_LO_sub = { &Transverse::qq_LO, 1, &params_sub };
        gsl_monte_function mf_qq_LO_sub2 = { &Transverse::qq_LO, 1, &params_pom };
        gsl_monte_function mf_qq_LO_unsub = { &Transverse::qq_LO, 1, &params_unsub };
        gsl_monte_function mf_qq_NLO_1_dim_dw = { &Transverse::qq_NLO_1_dim_decay_width, 1, &params_sub };
        gsl_monte_function mf_qq_NLO_1_dim_wf = { &Transverse::qq_NLO_1_dim_wave_function, 1, &params_sub };
        gsl_monte_function mf_qq_NLO_J_1 = { &Transverse::qq_NLO_J_1, 2, &params_sub };
        gsl_monte_function mf_qq_NLO_J_2 = { &Transverse::qq_NLO_J_2, 3, &params_sub };
        gsl_monte_function mf_qq_NLO_K = { &Transverse::qq_NLO_K, 2, &params_sub };
        gsl_monte_function mf_qqg_dim_4_sub = { &Transverse::qqg_dim4_sub, 4, &params_sub };
        gsl_monte_function mf_qqg_BK = { &Transverse::qqg_BK, 4, &params_sub };
        gsl_monte_function mf_qqg_dim_5 = { &Transverse::qqg_dim5, 5, &params_sub };
        gsl_monte_function mf_qqg_dim_6 = { &Transverse::qqg_dim6, 6, &params_sub };
        gsl_monte_function mf_lambda = { &Transverse::lambda_integrand, 1, &params_sub };
        gsl_monte_function mf_qq_rel_002_pp = { &Transverse::qq_rel_002_pp, 1, &params_sub };
        gsl_monte_function mf_qq_rel_200_pp = { &Transverse::qq_rel_200_pp, 1, &params_sub };
        gsl_monte_function mf_qq_rel_100_pm = { &Transverse::qq_rel_100_pm, 1, &params_sub };
        if(x_pom_bool) {
            mf_qq_NLO_1_dim_dw = { &Transverse::qq_NLO_1_dim_decay_width, 1, &params_pom };
            mf_qq_NLO_1_dim_wf = { &Transverse::qq_NLO_1_dim_wave_function, 1, &params_pom };
            mf_qq_NLO_J_1 = { &Transverse::qq_NLO_J_1, 2, &params_pom };
            mf_qq_NLO_J_2 = { &Transverse::qq_NLO_J_2, 3, &params_pom };
            mf_qq_NLO_K = { &Transverse::qq_NLO_K, 2, &params_pom };
            mf_qq_rel_002_pp = { &Transverse::qq_rel_002_pp, 1, &params_pom };
            mf_qq_rel_200_pp = { &Transverse::qq_rel_200_pp, 1, &params_pom };
            mf_qq_rel_100_pm = { &Transverse::qq_rel_100_pm, 1, &params_pom };  
            mf_lambda = { &Transverse::lambda_integrand, 1, &params_pom };  
        }


        if(inv_mass_rapidity_bool) {
            gsl_monte_function mf_qq_LO_unsub =     { &Transverse::qq_LO, 1, &params_inv_mass };
            gsl_monte_function mf_qq_NLO_1_dim_dw = { &Transverse::qq_NLO_1_dim_decay_width, 1, &params_inv_mass };
            gsl_monte_function mf_qq_NLO_1_dim_wf = { &Transverse::qq_NLO_1_dim_wave_function, 1, &params_inv_mass };
            gsl_monte_function mf_qq_NLO_J_1 = { &Transverse::qq_NLO_J_1, 2, &params_inv_mass };
            gsl_monte_function mf_qq_NLO_J_2 = { &Transverse::qq_NLO_J_2, 3, &params_inv_mass };
            gsl_monte_function mf_qq_NLO_K = { &Transverse::qq_NLO_K, 2, &params_inv_mass };
        gsl_monte_function mf_lambda = { &Transverse::lambda_integrand, 1, &params_inv_mass };
        gsl_monte_function mf_qq_rel_002_pp = { &Transverse::qq_rel_002_pp, 1, &params_inv_mass };
        gsl_monte_function mf_qq_rel_200_pp = { &Transverse::qq_rel_200_pp, 1, &params_inv_mass };
        gsl_monte_function mf_qq_rel_100_pm = { &Transverse::qq_rel_100_pm, 1, &params_inv_mass };
        }

        double xl_qq_LO[] = {x10_min};
        double xl_qq_NLO_1_dim[] = {x10_min};
        double xl_qq_NLO_J_1[] = {x10_min, xi_min};
        double xl_qq_NLO_J_2[] = {x10_min, xi_min, x_J_min };
        double xl_qq_NLO_K[] = {x10_min, z_K0_min};
        double xl_qqg_dim_4[] = {x20_min, x21_min, ph_min, z2_min};
        double xl_qqg_dim_5[] = {x20_min, x21_min, ph_min, z2_min, y_min}; 
        double xl_qqg_dim_6[] = {x20_min, x21_min, ph_min, z2_min, t_min, u_min};

        double xu_qq_LO [] = {x10_max};
        double xu_qq_NLO_1_dim [] = {x10_max};
        double xu_qq_NLO_J_1 [] = {x10_max, xi_max};
        double xu_qq_NLO_J_2 [] = {x10_max, xi_max, x_J_max };
        double xu_qq_NLO_K [] = {x10_max, z_K0_max};
        double xu_qqg_dim_4 [] = {x20_max, x21_max, ph_max, z2_max};
        double xu_qqg_dim_5 [] = {x20_max, x21_max, ph_max, z2_max, y_max};
        double xu_qqg_dim_6 [] = {x20_max, x21_max, ph_max, z2_max, t_max, u_max};

        int n_values = 15;
        double values[n_values];
        values[0] = integral(mf_qq_LO_sub, xl_qq_LO, xu_qq_LO, 1,    calls_dim_low);
        values[1] =  integral(mf_qq_LO_sub2, xl_qq_LO, xu_qq_LO, 1,  calls_dim_low);
        values[2] =  integral(mf_qq_LO_unsub, xl_qq_LO, xu_qq_LO, 1, calls_dim_low);
        values[3] =  integral(mf_qq_NLO_1_dim_dw, xl_qq_NLO_1_dim, xu_qq_NLO_1_dim, 1, calls_dim_low);
        values[4] =  integral(mf_qq_NLO_1_dim_wf, xl_qq_NLO_1_dim, xu_qq_NLO_1_dim, 1, calls_dim_low);
        values[5] =  integral(mf_qq_NLO_J_1, xl_qq_NLO_J_1, xu_qq_NLO_J_1, 2, calls_dim_low);
        values[6] =  integral(mf_qq_NLO_J_2, xl_qq_NLO_J_2, xu_qq_NLO_J_2, 3, calls_dim_low);
        values[7] =  integral(mf_qq_NLO_K, xl_qq_NLO_K, xu_qq_NLO_K, 2, calls_dim_low);
        values[8] =  integral(mf_qqg_dim_4_sub, xl_qqg_dim_4, xu_qqg_dim_4, 4, calls_dim_4);
        values[9] =  integral(mf_qqg_BK, xl_qqg_dim_4, xu_qqg_dim_4, 4, calls_dim_4);
        if( dim6_bool){
            values[10] =  integral(mf_qqg_dim_6, xl_qqg_dim_6, xu_qqg_dim_6, 6, calls_dim_high);
        }
        else {
            values[10] =  integral(mf_qqg_dim_5, xl_qqg_dim_5, xu_qqg_dim_5, 5, calls_dim_high);
        }
        if( !x_pom_bool ) {
            values[11] =  integral(mf_lambda, xl_qq_LO, xu_qq_LO, 1, calls_dim_low)/values[0];
        }
        else {
            values[11] =  integral(mf_lambda, xl_qq_LO, xu_qq_LO, 1, calls_dim_low)/values[1];
        }
        values[12] = integral(mf_qq_rel_002_pp, xl_qq_LO, xu_qq_LO, 1,  calls_dim_low);
        values[13] =  integral(mf_qq_rel_200_pp, xl_qq_LO, xu_qq_LO, 1, calls_dim_low);
        values[14] =  integral(mf_qq_rel_100_pm, xl_qq_LO, xu_qq_LO, 1, calls_dim_low);

        stringstream s;
        for(int i = 0; i< n_values; i++) {
            s <<  std::scientific << std::showpos << std::setprecision(9)<< values[i] << " ";
        }
        return s.str();
        
    }


    /**
    * Write production amplitude integrals to the file, at a fixed value Delta. W and Q^2 values given as a list. 
    * n_thread=number of threads to evaluate the integration points.
    */
    void write_amplitudes_thread(string file, int n_thread, double* W_list, double* Q2_list, double Delta) {


        ofstream myfile;
        myfile.open(file, ios_base::app);
        myfile << "# Different parts of the longitudinal production amplitude, at different values of W (GeV) and Q^2 (Gev^2)\n";
        myfile << "#Delta value:\n" << std::scientific << std::setprecision(9) << Delta;

        myfile << "\n#Amplitude values:";
        myfile << "\n#W (GeV)[0]      Q^2 (GeV^2)[1]   LO(Y_dip)[2]     LO(Y_pom)[3]     LO(Y_0)[4]       qq_NLO 1D dwS[5] qq_NLO 1D wfS[6] qq_NLO J_1[7]    qq_NLO J_2[8]    qq_NLO K[9]      qqg 4D no BK[10] qqg BK[11]       qqg 5D[12]       lambda[13]       qq_rel 002pp[14] qq_rel 200pp[15] qq_rel 100pm[16]";
    

        for(int i_n = 0;i_n<W_length/n_thread+1; i_n++) {
            future<string> futures[n_thread];
            for(int i_thread = 0; i_thread<n_thread; i_thread++) {
                int i_W = i_thread + n_thread*i_n;
                if(i_W < W_length) {
                    double W = W_list[i_W];
                    double Q2 = Q2_list[i_W];
                    double Q = sqrt(Q2);
            
                    futures[i_thread] = async(amplitudes_string, W, Q, Delta);
                }

            }

            for(int i_thread = 0; i_thread<n_thread; i_thread++) {
                int i_W = i_thread + n_thread*i_n;
                if(i_W < W_length) {
                    double W = W_list[i_W];
                    double Q2 = Q2_list[i_W];

                    myfile << "\n";
                    myfile << std::scientific << std::showpos << std::setprecision(9)<< W << " ";
                    myfile << std::scientific << std::showpos << std::setprecision(9)<< Q2 << " ";
                    myfile << futures[i_thread].get();
                }
            }

        }
        myfile.close();  
    }


}