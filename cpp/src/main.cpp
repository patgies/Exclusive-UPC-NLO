
/**
 * 
 * 
 * Program for calculating exclusive vector meson production in DIS at NLO accuracy. 
 * Made by J. Penttala <jani.j.penttala@student.jyu.fi>, 2021-2022.
 * 
 * 
**/


#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <iomanip>
#include <gsl/gsl_errno.h>
#include "gitsha1.h"

#include <tools.hpp>

#include "b_integral.hpp"
#include "dipole_amplitudes.hpp"
#include "constants.hpp"
#include "evaluate_integral_L.cpp"
#include "evaluate_integral_T.cpp"
using namespace std;

int main(int argc, char* argv[])
{
    // Do not let code to crash if an error occurs.
    gsl_set_error_handler_off();
    
    
    string output_file_L;
    string output_file_T;
    double Delta = 0.0;
    double W_list[argc] ; 
    double Q2_list[argc];
    bool ofileL_bool = false;
    bool ofileT_bool = false;
    int n_thread = 1;
    string dipole_data_file;
    string b_folder;

    
    if (argc < 2) {
        cerr << "No arguments given. See --help for more details." << endl;
        exit(1);
    }

    if (string(argv[1])=="--help" || string(argv[1])=="-h")
    {
        cout << "Program for calculating exclusive vector meson production in DIS at NLO accuracy. Made by J. Penttala <jani.j.penttala@student.jyu.fi>, 2021.\n" << endl;
        cout << "Required parameters:" << endl;
        cout << "-ofileL:\tOutput file for longitudinal production amplitude" << endl;
        cout << "-ofileT:\tOutput file for transverse production amplitude" << endl;
        cout << "-Q2 and -W:\tValues of Q^2 and W for which we calculate the amplitude. Can be given as a list, separated by space." << endl;
        cout << "-M_V:\tMass of the vector meson" << endl;
        cout << "-m_q:\tMass of the heavy quark" << endl;
        cout << "-Y0_if:\tInitial value for the rapidity" << endl;
        cout << "-Q0:\tMass scale of the nucleon" << endl;
        cout << "-sigma_0_half_mb:\tCross section/2 for the quark dipole scattering in units of mb" << endl;
        cout << "\nOptional parameters:" << endl;
        cout << "-Delta:\tThe value of Delta = sqrt(-t). Default Delta=0. WARNING: At the moment Delta!=0 is not guaranteed to work!" << endl;
        cout << "-thread:\tAmount of CPU threads used for calculations. Default is "<< n_thread << endl;
        cout << "-xpom:\tCalculations are done at rapidity Y=ln(1/x_pom) instead of Y_dip. Meant for LO calculations."<<endl;
        cout << "-use_target_rapidity:\tUse target rapidity instead of projectile rapidity. For TBK dipole amplitude."<<endl;
        cout << "-m_N:\tMass of the nucleon (~1GeV, doesn't affect the results too much)" << endl;
        cout << "-alphas_const:\tUse constant alpha_s and set its value." << endl;
        cout << "-dipole_file:\tPath to the dipole file" << endl;
        cout << "-int_points_dim_low:\tNumber of integration points for the low-dimensional (<4) parts of the calculate" << endl;
        cout << "-int_points_dim_4:\tNumber of integration points for the 4-dimensional part of the calculate" << endl;
        cout << "-int_points_dim_6:\tNumber of integration points for the 6-dimensional part of the calculate" << endl;
        cout << "One can also set the integration limits if needed. However, this isn't necessary and default values may be used instead." << endl;
        cout << "If running alpha_s is used (as is by default), the following variables must be set:" << endl;
        cout << "-C^2:\tSet C^2" << endl;
        cout << "-lambda_QCD:\tSet lambda_QCD" << endl;
        cout << "-c_small:\tSet c (lower-case alphabet)" << endl;
        cout << "-mu_0:\tSet mu_0" << endl;
        cout << "-b_dependent:\tThe dipole amplitude has explicit b-dependence" << endl;
        cout << "Required parameters when b-dependent dipole amplitude is used(-b_dependent option is used):" << endl;
        cout << "-b_folder:\tFolder that contains unintegrated dipole amplitudes for different values of b" << endl;
        cout << "-A:\tAtomic mass number for the nucleus" << endl;
        cout << "-R_A_plus_fm:\tParameter for Wood-Saxon distribution (R_A ~ A^1/3*R_A_plus - A^(-1/3)*R_A_minus) in fm" << endl;
        cout << "-R_A_minus_fm:\tParameter for Wood-Saxon distribution (R_A ~ A^1/3*R_A_plus - A^(-1/3)*R_A_minus) in fm" << endl;
        cout << "-d_fm:\tParameter for Wood-Saxon distribution (thickness) in fm." << endl;
        return 0;
    }
    


    for (int i=1; i<argc; i++)
    {
        if (string(argv[i])=="-ofileL") {
            output_file_L = string(argv[i+1]);
            ofileL_bool = true;
        }
        else if (string(argv[i])=="-ofileT") {
            output_file_T = string(argv[i+1]);
            ofileT_bool = true;
        }
        else if (string(argv[i])=="-Delta")
            Delta = StrToReal(argv[i+1]);
        else if (string(argv[i])=="-W") {
            while( !(string(argv[i+1]).substr(0,1)=="-") )
            {
                double W = StrToReal(argv[i+1]);
                W_list[W_length] = W;
                i++; W_length++;
            }
        }
        else if (string(argv[i])=="-Q2") {
            while( !(string(argv[i+1]).substr(0,1)=="-") )
            {
                double Q2 = StrToReal(argv[i+1]);
                Q2_list[Q2_length] = Q2;
                i++; Q2_length++;
            }
        }
        else if (string(argv[i])=="-xpom") {
            x_pom_bool = true;
        }
        else if (string(argv[i])=="-thread") {
            n_thread = StrToInt(argv[i+1]);
        }
        else if(string(argv[i])== "-M_V") {
            Mv = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])== "-m_q") {
            m = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])== "-Y0_if") {
            Y0_if = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])== "-Q_0") {
            Q0 = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])== "-m_N") {
            m_N = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])== "-sigma_0_half_mb") {
            sigma0 = 2.56819*2.0*StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-C2") {
            C_big = sqrt(StrToReal(argv[i+1]));
        }
        else if(string(argv[i])=="-c_small") {
            c_small = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-lambda_QCD") {
            lambda_QCD = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-mu_0") {
            mu_0 = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-z2_max") {
            z2_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-x20_min") {
            x20_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-x20_max") {
            x20_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-x21_min") {
            x21_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-x21_max") {
            x21_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-ph_min") {
            ph_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-ph_max") {
            ph_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-x10_min") {
            x10_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-x10_max") {
            x10_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-z_K0_min") {
            z_K0_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-z_K0_max") {
            z_K0_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-xi_min") {
            xi_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-xi_max") {
            xi_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-x_J_min") {
            x_J_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-x_J_max") {
            x_J_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-t_min") {
            t_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-t_max") {
            t_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-u_min") {
            u_min = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-u_max") {
            u_max = StrToReal(argv[i+1]);
        }
        else if(string(argv[i])=="-int_points_dim_low") {
            calls_dim_low = StrToInt(argv[i+1]);
        }
        else if(string(argv[i])=="-int_points_dim_4") {
            calls_dim_4 = StrToInt(argv[i+1]);
        }
        else if(string(argv[i])=="-int_points_dim_6") {
            calls_dim_high = StrToInt(argv[i+1]);
        }
        else if(string(argv[i])=="-int_points_dim_5") {
            calls_dim_high = StrToInt(argv[i+1]);
        }
        else if(string(argv[i])=="-dipole_file") {
            dipole_data_file = argv[i+1];
        }
        else if(string(argv[i])=="-no_dipole_file") {
            dipole_file_bool = false;
        }
        else if(string(argv[i])=="-use_target_rapidity") {
            eta_bool = true;
        }
        else if(string(argv[i])=="-alphas_const") {
            alpha_s_const = StrToReal(argv[i+1]);
            alpha_s_run_bool = false;
        }
        else if(string(argv[i])== "-b_dependent") {
            b_dependence_bool = true;
        }
        else if(string(argv[i])== "-d_fm") {
            d_thickness = StrToReal(argv[i+1]) * fm_to_inv_gev;
        }
        else if(string(argv[i])=="-R_A_plus_fm") {
            R_A_plus = StrToReal(argv[i+1]) * fm_to_inv_gev;
        }
        else if(string(argv[i])=="-R_A_minus_fm") {
            R_A_minus = StrToReal(argv[i+1]) * fm_to_inv_gev;
        }
        else if(string(argv[i])=="-A") {
            A = StrToInt(argv[i+1]);
        }
        else if(string(argv[i])=="-b_folder") {
            b_folder = argv[i+1];
        }
        else if(string(argv[i])=="-alpha_s_scheme") {
            alpha_s_scheme = new string(argv[i+1]);
        }
        else if(string(argv[i])=="-dim6") {
            dim6_bool = true;
        }
        else if (string(argv[i]).substr(0,1)=="-")
        {
            cerr << "Unknown parameter " << argv[i] <<  ". See --help for more details." << endl;
            exit(1);
        }
        
    }



    //Check that the required variables are read
    if(m == 0.0) {
        cerr << "Set value: m_q" << endl;
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
    else if(Q2_length == 0) {
        cerr << "Set at least one value for Q^2" << endl;
        exit(1);
    }
    else if(W_length == 0) {
        cerr << "Set at least one value for W" << endl;
        exit(1);
    }
    else if(Q2_length != W_length) {
        cerr << "Error: Different amount of values for W and Q^2. W: " << W_length << " Q^2: " << Q2_length <<endl;
        exit(1);
    }
    
    if( alpha_s_run_bool) {
        if(C_big == 0.0) {
            cerr << "Set value: C^2" << endl;
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

    if( !alpha_s_scheme ) {
        cerr << "Set alpha_s_scheme: bal+sd or parent dipole" << endl;
        exit(1);
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


    if (!ofileL_bool && !ofileT_bool) {
        cerr << "No file for output! Need to give at least longitudinal or transverse file for output." << endl;
        exit(1);
    }
    
    // Calculate the production
    if(ofileL_bool) {

        cout << "Calculating longitudinal production..." << endl;

        ofstream ofile;
        ofile.open(output_file_L);
        ofile << "# Longitudinal exclusive vector meson production in DIS at NLO by J. Penttala <jani.j.penttala@student.jyu.fi>, 2021. These are the values for the production amplitude at t=0, up to a prefactor -e*ef*Q/(2*pi)*sqrt(Nc/2)*2*(wavefunction factor)." << endl;
        ofile << "# Git version " << g_GIT_SHA1 << " main build " << __DATE__  << " " << __TIME__ << endl;
        ofile << "# Command: ";
        for (int i=1; i<argc; i++)
            ofile << argv[i] << " ";
        ofile << endl;
        ofile.close();
        

        Longitudinal::write_amplitudes_thread(output_file_L, n_thread, W_list, Q2_list, Delta);

        cout << "Longitudinal done!" << endl;

    }    

    if(ofileT_bool) {

        cout << "Calculating transverse production..." << endl;

        ofstream ofile;
        ofile.open(output_file_T);
        ofile << "# Transverse exclusive vector meson production in DIS at NLO by J. Penttala <jani.j.penttala@student.jyu.fi>, 2021. These are the values for the production amplitude at t=0, up to a prefactor e*ef*m/(pi)*sqrt(Nc/2)*2*(wavefunction factor)." << endl;
        ofile << "# Git version " << g_GIT_SHA1 << " main build " << __DATE__  << " " << __TIME__ << endl;
        ofile << "# Command: ";
        for (int i=1; i<argc; i++)
            ofile << argv[i] << " ";
        ofile << endl;
        ofile.close();
        
        Transverse::write_amplitudes_thread(output_file_T, n_thread, W_list, Q2_list, Delta);

        cout << "Transverse done!" << endl;

    }    
    return 0;
}
