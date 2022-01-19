
#include <iostream>
#include <vector>
#include <string>
#include <sstream> 
#include <iomanip>
#include <gsl/gsl_errno.h>
#include "gitsha1.h"

#include <tools.hpp>

#include "read_constants.cpp"
#include "evaluate_integral_L.cpp"
#include "evaluate_integral_T.cpp"
using namespace std;

int main(int argc, char* argv[])
{
    // Do not let code to crash if an error occurs, we should have error handling everywhere!
    gsl_set_error_handler_off();
    
    
    string output_file_L;
    string output_file_T;
    double Delta = 0.0;
    double W;
    double Q2;
    bool W_bool= false;
    bool Q_bool = false;
    bool ofileL_bool = false;
    bool ofileT_bool = false;
    bool ifile_bool = false;
    int n_thread = 1;
    
    if (argc < 2) {
        cerr << "No arguments given. See -help for more details." << endl;
        exit(1);
    }

    if (string(argv[1])=="-help" || string(argv[1])=="-h")
    {
        cout << "Program for calculating exclusive vector meson production in DIS at NLO accuracy. Made by J. Penttala <jani.j.penttala@student.jyu.fi>, 2021.\n" << endl;
        cout << "Required parameters:" << endl;
        cout << "-ifile:\tFile for reading the parameters" << endl;
        cout << "-ofileL:\tOutput file for longitudinal production amplitude" << endl;
        cout << "-ofileT:\tOutput file for transverse production amplitude" << endl;
        cout << "\nDifferent options:" << endl;
        cout << "Plot as a function of W or Q^2, keeping the other constant. One of the following (in each case) must be given as a parameter:" << endl;
        cout << "-Q2 or -W:\tSets the value of the parameter kept as constant" << endl;
        cout << "-Wmin or -Q2min:\tMinimum for the evaluation points" <<endl;
        cout << "-Wmax or -Q2max:\tMaximum for the evaluation points" <<endl;
        cout << "-Wpoints or -Q2points:\tNumber of evaluation points. The points are spread in evenly in the logarithmic scale." <<endl;
        cout << "As an example, the following options could be used:\t-W 100 -Q2min 1 -Q2max 30 -Q2points 100" <<endl;
        cout << "Both can also be used simultaneously, to evaluate as a function of W (with constant Q^2) and vice versa." << endl;
        cout << "\nOptional parameters:" << endl;
        cout << "-Delta:\tThe value of Delta = sqrt(-t). Default Delta=0" << endl;
        cout << "-W:\tThe value of W" << endl;
        cout << "-Q2:\tThe value of Q^2" << endl;
        cout << "-thread:\tAmount of CPU threads used for calculations. Default is "<< n_thread << endl;
        cout << "-fast:\tForces a small amount of MC integration points (1e4). Overrides the amount of points in the config file. This option is useful for quickly getting results that are roughly correct." << endl;
        cout << "-NLOxpom:\tUse x_pom at NLO instead of x'"<<endl;
        cout << "-relxpom:\tUse x_pom for relativistic corrections instead of x'. For LO calculations."<<endl;
        cout << "-rcBK:\tSubstitute rcBK to LO BK at NLO qqg expression."<<endl;

        cout << "\nConfig file help:" << endl;
        cout << "Start row with \'###\' to indicate the name of a variable. Then, put the value of the variable on the next row." << endl;
        cout << "See example files in the folder \'config_files\'." << endl;
        cout << "Possible variables:" << endl;
        cout << "M_V:\tMass of the vector meson" << endl;
        cout << "m:\tMass of the heavy quark" << endl;
        cout << "Y0_if:\tInitial value for the rapidity" << endl;
        cout << "Q0:\tMass scale of the nucleon" << endl;
        cout << "m_N:\tMass of the nucleon (~1GeV, doesn't affect the results too much)" << endl;
        cout << "sigma0/2(mb):\tCross section/2 for the quark dipole scattering in units of mb" << endl;
        cout << "sigma0:\tCross section for the quark dipole scattering in units of GeV^2" << endl;
        cout << "alpha_s const:\tUse constant alpha_s and set its value." << endl;
        cout << "dipole file:\tPath to the dipole file" << endl;
        cout << "integ calls low:\tNumber of integration points for the low-dimensional (<4) parts of the calculate" << endl;
        cout << "integ calls high:\tNumber of integration points for the 4-dimensional part of the calculate" << endl;
        cout << "integ calls dim 6:\tNumber of integration points for the 6-dimensional part of the calculate" << endl;
        cout << "One can also set the integration limits if needed. However, this isn't necessary and default values may be used instead." << endl;
        cout << "If running alpha_s is used (as is by default), the following variables must be set:" << endl;
        cout << "C^2 or C_big:\tSet C^2 or C" << endl;
        cout << "lambda_QCD:\tSet lambda_QCD" << endl;
        cout << "c_small:\tSet c (lower-case alphabet)" << endl;
        cout << "mu_0:\tSet mu_0" << endl;
        cout << "b-dependent:\tThe dipole amplitude has explicit b-dependence" << endl;
        cout << "b-folder:\tFolder that contains unintegrated dipole amplitudes for different values of b" << endl;
        cout << "A:\tAtomic mass number for the nucleus" << endl;
        cout << "R_A_plus:\tParameter for Wood-Saxon distribution (R_A ~ A^1/3*R_A_plus - A^(-1/3)*R_A_minus)" << endl;
        cout << "R_A_minus:\tParameter for Wood-Saxon distribution (R_A ~ A^1/3*R_A_plus - A^(-1/3)*R_A_minus)" << endl;
        cout << "d:\tParameter for Wood-Saxon distribution (thickness)" << endl;
        return 0;
    }
    

    for (int i=1; i<argc; i++)
    {
       
        if (string(argv[i])=="-ifile")
        {
            read_constants_from_file(string(argv[i+1]));
            // read_constants_default();
            ifile_bool = true;
        }
        else if (string(argv[i])=="-ofileL") {
            output_file_L = string(argv[i+1]);
            ofileL_bool = true;
        }
        else if (string(argv[i])=="-ofileT") {
            output_file_T = string(argv[i+1]);
            ofileT_bool = true;
        }
        else if (string(argv[i])=="-Delta")
            Delta = StrToReal(argv[i+1]);
        else if (string(argv[i])=="-thread")
            n_thread = StrToInt(argv[i+1]);
        else if (string(argv[i])=="-W") {
            W = StrToReal(argv[i+1]);
            W_bool = true;
        }
        else if (string(argv[i])=="-Q2") {
            Q2 = StrToReal(argv[i+1]);
            Q_bool = true;
        }
        else if (string(argv[i])=="-Wmin") {
            W_min = StrToReal(argv[i+1]);
        }
        else if (string(argv[i])=="-Wmax") {
            W_max = StrToReal(argv[i+1]);
        }
        else if (string(argv[i])=="-Q2min") {
            Q2_min = StrToReal(argv[i+1]);
        }
        else if (string(argv[i])=="-Q2max") {
            Q2_max = StrToReal(argv[i+1]);
        }
        else if (string(argv[i])=="-Wpoints") {
            W_points = StrToReal(argv[i+1]);
        }
        else if (string(argv[i])=="-Q2points") {
            Q_points = StrToReal(argv[i+1]);
        }
        else if (string(argv[i])=="-fast") {
            integ_points_small_bool = true;
        }
        else if (string(argv[i])=="-NLOxpom") {
            NLO_x_pom_bool = true;
        }
        else if (string(argv[i])=="-relxpom") {
            rel_x_pom_bool = true;
        }
        else if (string(argv[i])=="-rcBK") {
            rcBK_bool = true;
        }
        else if (string(argv[i]).substr(0,1)=="-")
        {
            cerr << "Unknown parameter " << argv[i] <<  ". See -help for more details." << endl;
            exit(1);
        }
        
    }

    if(integ_points_small_bool) set_integ_points_small();


    if (!ifile_bool) {
        cerr << "No file for input parameters!" << endl;
        exit(1);
    }
    if (!ofileL_bool && !ofileT_bool) {
        cerr << "No file for output! Need to give at least longitudinal or transverse file for output." << endl;
        exit(1);
    }
    if (Q_bool && W_bool) {
        cerr << "Give only W or Q! Otherwise the program will overwrite some results." << endl;
        exit(1);
    }
    

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
        

        if (Q_bool)
        {
            if(W_points == 0) {
                cerr<<"Error! No points to evaluate in W given" << endl;
                exit(1);
            }
            Longitudinal::write_amplitudes_W_thread(output_file_L, n_thread, Q2, Delta);
        }
        else if (W_bool)
        {
            if(Q_points == 0) {
                cerr<<"Error! No points to evaluate in Q^2 given" << endl;
                exit(1);
            }
            Longitudinal::write_amplitudes_Q_thread(output_file_L, n_thread, W, Delta);
        }
        else {
            cerr << "Set a value for either W or Q2." << endl;
            exit(1);
        }

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
        

        if (Q_bool)
        {
            if(W_points == 0) {
                cerr<<"Error! No points to evaluate in W given" << endl;
                exit(1);
            }
            Transverse::write_amplitudes_W_thread(output_file_T, n_thread, Q2, Delta);
        }
        else if (W_bool)
        {
            if(Q_points == 0) {
                cerr<<"Error! No points to evaluate in Q^2 given" << endl;
                exit(1);
            }
            Transverse::write_amplitudes_Q_thread(output_file_T, n_thread, W, Delta);
        }
        else {
            cerr << "Set a value for either W or Q2." << endl;
            exit(1);
        }

        cout << "Transverse done!" << endl;

    }    
    return 0;
}
