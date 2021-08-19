
#ifndef _INTEGRANDS_T_H
#define _INTEGRANDS_T_H

#include <gsl/gsl_math.h>

namespace Transverse {

    void dimension_error(size_t dim, size_t corr_dim);

    double alpha_s3(double x, double y, double z);
    double alpha_s(double r);
    double alpha_s_run(double r);
    double x10_value(double x20, double x21, double ph);

    double L_1(double x[], double delta, double m, double Q, double W);
    double M(double x[], double delta, double m, double Q, double W);
    double L_BK(double x[], double delta, double m, double Q, double W);
    double L_rcBK(double x[], double delta, double m, double Q, double W);
    double L_KCBK(double x[], double delta, double m, double Q, double W);


    double qq_LO(double x[], size_t dim, void *params);
    double qq_NLO_1_dim_decay_width(double x[], size_t dim, void *params);
    double qq_NLO_1_dim_wave_function(double x[], size_t dim, void *params);
    double qq_NLO_J_1(double x[], size_t dim, void *params);
    double qq_NLO_J_2(double x[], size_t dim, void *params);
    double qq_NLO_K(double x[], size_t dim, void *params);
    double qqg_dim4_sub(double x[], size_t dim, void *params);
    double qqg_dim4_unsub(double x[], size_t dim, void *params);
    double qqg_dim6(double x[], size_t dim, void *params);
    double qqg_BK(double x[], size_t dim, void *params);
    double qqg_rcBK(double x[], size_t dim, void *params);
    double qqg_KCBK(double x[], size_t dim, void *params);
    double lambda_integrand(double x[], size_t dim, void *params);
    double qq_rel_002_pp(double x[], size_t dim, void *params);
    double qq_rel_200_pp(double x[], size_t dim, void *params);
    double qq_rel_100_pm(double x[], size_t dim, void *params);

    double J_1_integrand(double xi, double x10, double m, double Q);
    double J_2_integrand(double xi, double x, double x10, double m, double Q);
    double K_0_integrand(double z, double x10, double m, double Q);
    double L(double m, double Q);
    double Omega_V(double m, double Q);

    double delta_factor_qq(double z, double Delta, double x10);
    double delta_factor_qqg(double z2, double Delta, double x20, double x21, double ph);

    double theta(double x);
    struct integ_params { double delta; double m; double Q; double x; double W;};

}

#endif