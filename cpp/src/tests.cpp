/**
 * For testing the main code.
 **/

#define BOOST_TEST_MAIN
#include <boost/test/unit_test.hpp>
#include <iostream>


#include "dipole_amplitudes.hpp"
#include "read_constants.cpp"
#include "integrands_T.hpp"
#include "integrands_L.hpp"

namespace tt = boost::test_tools;


// Just to get the code to initialize the constants... this is actually pretty stupid
int initiliaze = read_constants_default();

double rdef = 0.8;
double Ydef = 2.3;
double Qdef = 9.8;
double xidef = 0.3;
double xdef = 0.6;
double zdef = 0.35;
double z2def = 0.2;
double x20def = 1.1;
double x21def = 1.9;
double phidef = 0.17;
double Wdef = 90.0;
double tdef = 0.12;
double udef = 0.15;

double tol = 0.0001;

BOOST_AUTO_TEST_CASE( test_alphas_T )
{
    BOOST_TEST( Transverse::alpha_s(rdef) == 0.396203, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_alphas3_T )
{
    double r1 = 1.0;
    double r2 = 2.0;
    double r3 = 3.0;
    BOOST_TEST( Transverse::alpha_s3(r1, r2, r3) == Transverse::alpha_s(r1), tt::tolerance(tol) );
    BOOST_TEST( Transverse::alpha_s3(r2, r1, r3) == Transverse::alpha_s(r1), tt::tolerance(tol) );
    BOOST_TEST( Transverse::alpha_s3(r3, r2, r1) == Transverse::alpha_s(r1), tt::tolerance(tol) );
}


BOOST_AUTO_TEST_CASE( test_x10_T )
{
    BOOST_TEST( Transverse::x10_value(x20def, x21def, phidef) == 0.836813, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_GBW_dipole )
{
    BOOST_TEST( N_xy(rdef, 0.0, Ydef) == 0.863052, tt::tolerance(tol) );
}



BOOST_AUTO_TEST_CASE( test_int_lo_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Transverse::qq_LO( x, 1,  &params) == 0.0427634, tt::tolerance(tol) );
}


BOOST_AUTO_TEST_CASE( test_omega_T )
{
    BOOST_TEST( Transverse::Omega_V(m, Qdef) == -0.1506, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_L_T )
{
    BOOST_TEST( Transverse::L(m, Qdef) == 1.32363, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_1dim_dw_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Transverse::qq_NLO_1_dim_decay_width( x, 1,  &params) == 0.0157832, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_1dim_wf_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Transverse::qq_NLO_1_dim_wave_function( x, 1,  &params) == 0.00140157, tt::tolerance(tol) );
}


BOOST_AUTO_TEST_CASE( test_int_J1_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef, xidef};
    BOOST_TEST( Transverse::qq_NLO_J_1( x, 2,  &params) == -0.00704528, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_J2_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef, xidef, xdef};
    BOOST_TEST( Transverse::qq_NLO_J_2( x, 3,  &params) == -0.00299998, tt::tolerance(tol) );
}



BOOST_AUTO_TEST_CASE( test_int_K_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef, zdef};
    BOOST_TEST( Transverse::qq_NLO_K( x, 2,  &params) == 0.0327568, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_lambda_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Transverse::lambda_integrand( x, 1,  &params) == 0.0122184, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_rel_002_pp_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Transverse::qq_rel_002_pp( x, 1,  &params) == -0.0891563, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_rel_200_pp_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Transverse::qq_rel_200_pp( x, 1,  &params) == 0.0328108, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_rel_100_pm_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Transverse::qq_rel_100_pm( x, 1,  &params) == -0.196119, tt::tolerance(tol) );
}



BOOST_AUTO_TEST_CASE( test_int_BK_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {x20def, x21def, phidef, z2def};
    BOOST_TEST( Transverse::qqg_BK( x, 4,  &params) == 0.0754996, tt::tolerance(tol) );
}


BOOST_AUTO_TEST_CASE( test_int_dim4_unsub_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {x20def, x21def, phidef, z2def};
    BOOST_TEST( Transverse::qqg_dim4_unsub( x, 4,  &params) == -0.309625, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_dim4_sub_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {x20def, x21def, phidef, z2def};
    BOOST_TEST( Transverse::qqg_dim4_sub( x, 4,  &params) == -0.385125, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_dim6_T )
{
    struct Transverse::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {x20def, x21def, phidef, z2def, tdef, udef};
    BOOST_TEST( Transverse::qqg_dim6( x, 6,  &params) == -0.040435, tt::tolerance(tol) );
}






BOOST_AUTO_TEST_CASE( test_alphas_L )
{
    BOOST_TEST( Longitudinal::alpha_s(rdef) == 0.396203, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_alphas3_L )
{
    double r1 = 1.0;
    double r2 = 2.0;
    double r3 = 3.0;
    BOOST_TEST( Longitudinal::alpha_s3(r1, r2, r3) == Longitudinal::alpha_s(r1), tt::tolerance(tol) );
    BOOST_TEST( Longitudinal::alpha_s3(r2, r1, r3) == Longitudinal::alpha_s(r1), tt::tolerance(tol) );
    BOOST_TEST( Longitudinal::alpha_s3(r3, r2, r1) == Longitudinal::alpha_s(r1), tt::tolerance(tol) );
}


BOOST_AUTO_TEST_CASE( test_x10_L )
{
    BOOST_TEST( Longitudinal::x10_value(x20def, x21def, phidef) == 0.836813, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_lo_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Longitudinal::qq_LO( x, 1,  &params) == 0.0427634, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_gammalm_L )
{
    BOOST_TEST( Longitudinal::Gamma_Lm(m, Qdef) == 0.254989, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_L_L )
{
    BOOST_TEST( Longitudinal::L(m, Qdef) == 1.32363, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_1dim_dw_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Longitudinal::qq_NLO_1_dim_dw( x, 1,  &params) == 0.0143608, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_1dim_wf_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Longitudinal::qq_NLO_1_dim_wf( x, 1,  &params) == -0.00002082, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_J1_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef, xidef};
    BOOST_TEST( Longitudinal::qq_NLO_J_1( x, 2,  &params) == 0.00425542, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_J2_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef, xidef, xdef};
    BOOST_TEST( Longitudinal::qq_NLO_J_2( x, 3,  &params) == 0.000338758, tt::tolerance(tol) );
}


BOOST_AUTO_TEST_CASE( test_int_K_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef, zdef};
    BOOST_TEST( Longitudinal::qq_NLO_K0( x, 2,  &params) == -0.018036, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_lambda_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Longitudinal::lambda_integrand( x, 1,  &params) == 0.0122184, tt::tolerance(tol) );
}


BOOST_AUTO_TEST_CASE( test_int_rel_200_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Longitudinal::qq_rel_200( x, 1,  &params) == 0.0164054, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_rel_002_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {rdef};
    BOOST_TEST( Longitudinal::qq_rel_002( x, 1,  &params) == -0.0463929, tt::tolerance(tol) );
}



BOOST_AUTO_TEST_CASE( test_int_BK_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {x20def, x21def, phidef, z2def};
    BOOST_TEST( Longitudinal::qqg_BK( x, 4,  &params) == 0.0754996, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_dim4_unsub_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {x20def, x21def, phidef, z2def};
    BOOST_TEST( Longitudinal::qqg_dim4_unsub( x, 4,  &params) == -0.308027, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_dim4_sub_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {x20def, x21def, phidef, z2def};
    BOOST_TEST( Longitudinal::qqg_dim4_sub( x, 4,  &params) == -0.383526, tt::tolerance(tol) );
}

BOOST_AUTO_TEST_CASE( test_int_dim6_L )
{
    struct Longitudinal::integ_params params = {0.0, m, Qdef, exp(-Ydef), Wdef};
    double x[] = {x20def, x21def, phidef, z2def, tdef, udef};
    BOOST_TEST( Longitudinal::qqg_dim6( x, 6,  &params) == -0.0235301, tt::tolerance(tol) );
}



// double qqg_rcBK(double x[], size_t dim, void *params);
// double qqg_KCBK(double x[], size_t dim, void *params);

// double delta_factor_qq(double z, double Delta, double x10);
// double delta_factor_qqg(double z2, double Delta, double x20, double x21, double ph);

