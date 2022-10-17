
#ifndef _INTEGRANDS_L_H
#define _INTEGRANDS_L_H

#include <gsl/gsl_math.h>

namespace Longitudinal {

    void dimension_error(size_t dim, size_t corr_dim);

    double alpha_s3(double x, double y, double z);
    double alpha_s(double r);
    double alpha_s_run(double r);
    double x10_value(double x20, double x21, double ph);

    double g_int(int a, int b, double Qbar, double mf, double x2, double x3, double omega, double lambda, double y);


    double Ii_0_integrand(double t, double u, double b, double r, double m, double Qbar, double omega, double lambda);
    double I_integrand(double t, double u, double b, double r, double m, double Qbar, double omega, double lambda);
    double L_5(double x[], double delta, double m, double Q, double W);
    double L_3(double x[], double delta, double m, double Q, double W);
    double L_4(double x[], double delta, double m, double Q, double W);
    double M_1(double x[], double delta, double m, double Q, double W);
    double M_2(double x[], double delta, double m, double Q, double W);
    double L_BK(double x[], double delta, double m, double Q, double W);
    double M_1_fast(double x[], double delta, double m, double Q, double W);
    double M_2_fast(double x[], double delta, double m, double Q, double W);



    double qq_LO(double x[], size_t dim, void *params);
    double qq_NLO_1_dim_decay_width(double x[], size_t dim, void *params);
    double qq_NLO_1_dim_wave_function(double x[], size_t dim, void *params);
    double qq_NLO_J_1(double x[], size_t dim, void *params);
    double qq_NLO_J_2(double x[], size_t dim, void *params);
    double qq_NLO_K0(double x[], size_t dim, void *params);
    double qqg_dim4_sub(double x[], size_t dim, void *params);
    double qqg_dim4_unsub(double x[], size_t dim, void *params);
    double qqg_dim5(double x[], size_t dim, void *params);
    double qqg_dim6(double x[], size_t dim, void *params);
    double qqg_BK(double x[], size_t dim, void *params);
    double lambda_integrand(double x[], size_t dim, void *params);
    double qq_rel_002(double x[], size_t dim, void *params);
    double qq_rel_200(double x[], size_t dim, void *params);

    double J_1_integrand(double xi, double x10, double m, double Q);
    double J_2_integrand(double xi, double x, double x10, double m, double Q);
    double K_0_integrand(double z, double x10, double m, double Q);
    double L(double m, double Q);
    double Gamma_Lm(double m, double Q);

    double delta_factor_qq(double z, double Delta, double x10);
    double delta_factor_qqg(double z2, double Delta, double x20, double x21, double ph);

    double theta(double x);
    struct integ_params { double delta; double m; double Q; double x; double W;};

}

#endif