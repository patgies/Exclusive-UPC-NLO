#include "constants.hpp"
#include "dipole_amplitudes.hpp"
#include "b_integral.hpp"
#include "tools.hpp"
#include <fstream>
#include <iostream>
using namespace std;

void read_constants_from_file(string path) {
    ifstream file(path);
    if (!file.is_open())
    {
        cerr <<  "ERROR! Coudn't read the configuration file " << path << endl ;
        exit(1);
    }
    string dipole_data_file;
    string b_folder;
    while(!file.eof())
    {
        string line;
        string variable_value;
        getline(file, line);
        string variable_name;
        if(line.length() >= 3 ) {
            variable_name = line.substr(3,line.length()-3);
        }
        else {
            cerr << "Unknown line: " << line << endl;
            exit(1);
        }

        if (line.substr(0, 3)=="###")
        {                 
            if(variable_name == "M_V") {
                getline(file,variable_value);
                Mv = StrToReal(variable_value);
            }
            else if(variable_name == "m") {
                getline(file,variable_value);
                m = StrToReal(variable_value);
            }
            else if(variable_name == "Y0_if") {
                getline(file,variable_value);
                Y0_if = StrToReal(variable_value);
            }
            else if(variable_name == "Q_0") {
                getline(file,variable_value);
                Q0 = StrToReal(variable_value);
            }
            else if(variable_name == "m_N") {
                getline(file,variable_value);
                m_N = StrToReal(variable_value);
            }
            else if(variable_name == "sigma_0/2(mb)") {
                getline(file,variable_value);
                sigma0 = 2.56819*2.0*StrToReal(variable_value);
            }
            else if(variable_name == "sigma_0") {
                getline(file,variable_value);
                sigma0 = StrToReal(variable_value);
            }
            else if(variable_name == "C^2") {
                getline(file,variable_value);
                C_big = sqrt(StrToReal(variable_value));
            }
            else if(variable_name == "C_big") {
                getline(file,variable_value);
                C_big = StrToReal(variable_value);
            }
            else if(variable_name == "c_small") {
                getline(file,variable_value);
                c_small = StrToReal(variable_value);
            }
            else if(variable_name == "lambda_QCD") {
                getline(file,variable_value);
                lambda_QCD = StrToReal(variable_value);
            }
            else if(variable_name == "mu_0") {
                getline(file,variable_value);
                mu_0 = StrToReal(variable_value);
            }
            else if(variable_name == "z2_max") {
                getline(file,variable_value);
                z2_max = StrToReal(variable_value);
            }
            else if(variable_name == "x20_min") {
                getline(file,variable_value);
                x20_min = StrToReal(variable_value);
            }
            else if(variable_name == "x20_max") {
                getline(file,variable_value);
                x20_max = StrToReal(variable_value);
            }
            else if(variable_name == "x21_min") {
                getline(file,variable_value);
                x21_min = StrToReal(variable_value);
            }
            else if(variable_name == "x21_max") {
                getline(file,variable_value);
                x21_max = StrToReal(variable_value);
            }
            else if(variable_name == "ph_min") {
                getline(file,variable_value);
                ph_min = StrToReal(variable_value);
            }
            else if(variable_name == "ph_max") {
                getline(file,variable_value);
                ph_max = StrToReal(variable_value);
            }
            else if(variable_name == "x10_min") {
                getline(file,variable_value);
                x10_min = StrToReal(variable_value);
            }
            else if(variable_name == "x10_max") {
                getline(file,variable_value);
                x10_max = StrToReal(variable_value);
            }
            else if(variable_name == "z_K0_min") {
                getline(file,variable_value);
                z_K0_min = StrToReal(variable_value);
            }
            else if(variable_name == "z_K0_max") {
                getline(file,variable_value);
                z_K0_max = StrToReal(variable_value);
            }
            else if(variable_name == "xi_min") {
                getline(file,variable_value);
                xi_min = StrToReal(variable_value);
            }
            else if(variable_name == "xi_max") {
                getline(file,variable_value);
                xi_max = StrToReal(variable_value);
            }
            else if(variable_name == "x_J_min") {
                getline(file,variable_value);
                x_J_min = StrToReal(variable_value);
            }
            else if(variable_name == "x_J_max") {
                getline(file,variable_value);
                x_J_max = StrToReal(variable_value);
            }
            else if(variable_name == "t_min") {
                getline(file,variable_value);
                t_min = StrToReal(variable_value);
            }
            else if(variable_name == "t_max") {
                getline(file,variable_value);
                t_max = StrToReal(variable_value);
            }
            else if(variable_name == "u_min") {
                getline(file,variable_value);
                u_min = StrToReal(variable_value);
            }
            else if(variable_name == "u_max") {
                getline(file,variable_value);
                u_max = StrToReal(variable_value);
            }
            else if(variable_name == "W_points") {
                getline(file,variable_value);
                // W_points = StrToReal(variable_value);
                cout << "Deprecated: W_points in config file. Using the ones given in the command line argument." << endl;
            }
            else if(variable_name == "Q_points") {
                getline(file,variable_value);
                // Q_points = StrToReal(variable_value);
                cout << "Deprecated: Q_points in config file. Using the ones given in the command line argument." << endl;
            }
            else if(variable_name == "Q^2_min") {
                getline(file,variable_value);
                // Q2_min = StrToReal(variable_value);
                cout << "Deprecated: Q2_min in config file. Using the ones given in the command line argument." << endl;
            }
            else if(variable_name == "Q^2_max") {
                getline(file,variable_value);
                // Q2_max = StrToReal(variable_value);
                cout << "Deprecated: Q2_max in config file. Using the ones given in the command line argument." << endl;
            }
            else if(variable_name == "W_min") {
                getline(file,variable_value);
                // W_min = StrToReal(variable_value);
                cout << "Deprecated: W_min in config file. Using the ones given in the command line argument." << endl;
            }
            else if(variable_name == "W_max") {
                getline(file,variable_value);
                // W_max = StrToReal(variable_value);
                cout << "Deprecated: W_max in config file. Using the ones given in the command line argument." << endl;
            }
            else if(variable_name == "integ calls low") {
                getline(file,variable_value);
                calls_low = StrToInt(variable_value);
            }
            else if(variable_name == "integ calls high") {
                getline(file,variable_value);
                calls_high = StrToInt(variable_value);
            }
            else if(variable_name == "integ calls dim 6") {
                getline(file,variable_value);
                calls_dim6 = StrToInt(variable_value);
            }
            else if(variable_name == "dipole file") {
                getline(file,variable_value);
                dipole_data_file = variable_value;
            }
            else if(variable_name == "no dipole") {
                dipole_file_bool = false;
            }
            else if(variable_name == "target rapidity") {
                eta_bool = true;
            }
            else if(variable_name == "alpha_s const") {
                getline(file,variable_value);
                alpha_s_const = StrToReal(variable_value);
                alpha_s_run_bool = false;
            }
            else if(variable_name == "IP SAT") {
                IPsat_bool = true;
            }
            else if(variable_name == "b-dependent") {
                b_dependence_bool = true;
            }
            else if(variable_name == "d(fm)") {
                getline(file,variable_value);
                d_thickness = StrToReal(variable_value) * fm_to_inv_gev;
            }
            else if(variable_name == "R_A_plus(fm)") {
                getline(file,variable_value);
                R_A_plus = StrToReal(variable_value) * fm_to_inv_gev;
            }
            else if(variable_name == "R_A_minus(fm)") {
                getline(file,variable_value);
                R_A_minus = StrToReal(variable_value) * fm_to_inv_gev;
            }
            else if(variable_name == "A") {
                getline(file,variable_value);
                A = StrToInt(variable_value);
            }
            else if(variable_name == "b-folder") {
                getline(file,variable_value);
                b_folder = variable_value;
            }
            else {
                cerr << "Unknown variable name: " << variable_name << endl;
                exit(1);
            }
        }
    }

    //Check that the required variables are read
    if(m == 0.0) {
        cerr << "Set value: m" << endl;
        exit(1);
    }
    else if(Mv == 0.0) {
        cerr << "Set value: M_V" << endl;
        exit(1);
    }
    else if(Q0 == 0.0) {
        cerr << "Set value: Q_0" << endl;
        exit(1);
    }
    else if(sigma0 == 0.0) {
        cerr << "Set value: sigma_0" << endl;
        exit(1);
    }
    
    if( alpha_s_run_bool) {
        if(C_big == 0.0) {
            cerr << "Set value: C_big" << endl;
            exit(1);
        }
        else if(c_small == 0.0) {
            cerr << "Set value: c_small" << endl;
            exit(1);
        }
        else if(lambda_QCD == 0.0) {
            cerr << "Set value: lambda_QCD" << endl;
            exit(1);
        }
        else if(mu_0 == 0.0) {
            cerr << "Set value: mu_0" << endl;
            exit(1);
        }
    }
    else {
        if( alpha_s_const == 0.0 ) {
            cerr << "Set value: alpha_s_const" << endl;
            exit(1);
        }

    }

    if(dipole_file_bool && dipole_data_file == "") {
        cerr << "Set value: dipole_data_file" << endl;
        exit(1);
    }

    x_max = exp(-Y0_if);
    if( b_dependence_bool ) {
        initialize_amplitudes(b_folder, dipole_data_file);
        initialize_rho0();
        initialize_T_A();
        initialize_T_A_squared();
    }
    else initialize_amplitude(dipole_data_file);
    file.close();

}

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

    W_points = 12;
    Q_points = 24;
    Q2_min = 0.01;
    Q2_max = 100.0;
    W_min = 50.0;
    W_max = 1000.0;

    // calls_low = 1e5;
    // calls_high = 1e6;
    // calls_dim6 = 1e7;

    calls_low = 1e5;
    calls_high = 1e5;
    calls_dim6 = 1e5;


    // dipole_data_file="data/fixed_as_mv_qs0_0.1114_gamma_1.94";
    // string dipole_data_file="data/dipole-kcbk-hera-bal+sd-0.00.dip";
    // initialize_amplitude(dipole_data_file);
    dipole_file_bool = false;
    eta_bool = false;

    return 0;
}

void set_integ_points_small() {
    calls_low = 1e4;
    calls_high = 1e4;
    calls_dim6 = 1e4;
}