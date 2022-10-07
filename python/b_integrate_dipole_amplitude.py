""" Does the impact parameter integration to the dipole amplitudes. """

import numpy as np
import os 

def read_file(file):
    """
    Read the dipoles from the files.
    """
    with open(file, "r") as f:
        lines = [line for line in f.readlines()]
        start_text = lines[0:13]
        dipole_amplitude_table = []
        r_min = float(lines[9][3:])
        r_factor = float(lines[10][3:])
        r_number = int(lines[11][3:])
        x0 = float(lines[12][3:])
        Y_0 = np.log(1/x0)
        Y_v = [ float(lines[13][3:])] # first Y value
        dipole_amplitude_v = []
        for l in lines[14:]:
            if l.startswith("###"):
                Y_v += [float(l[3:])]
                dipole_amplitude_table += [dipole_amplitude_v]
                dipole_amplitude_v = []
            else:
                dipole_amplitude_v += [  float(l) ]
        dipole_amplitude_table += [dipole_amplitude_v] # add also the last one

    results_dict = { 
                    "Y0": Y_0, 
                    "Y_vector": np.array(Y_v), 
                    "r_min": r_min,
                    "r_factor": r_factor,
                    "r_number": r_number,
                    "dipole_amplitude": np.array(dipole_amplitude_table)
                    }


    return results_dict

def b_integrate(dipole_amplitude_list, b_list):
    """
    Here dipole amplitude contains arrays of dipole amplitudes. Just sum these together. b_list has values in fm, we convert them to GeV^-1
    """

    b_step_size = 2

    # Trapezoid method
    dipole_amplitude_integrated = 1/2 * dipole_amplitude_list[0] * b_list[0] * 2*np.pi * b_step_size 
    for i in range((len(dipole_amplitude_list)))[1:-1]:
        dipole_amplitude_integrated += dipole_amplitude_list[i] * b_list[i] * 2*np.pi * b_step_size 
    
    dipole_amplitude_integrated += 1/2 *  dipole_amplitude_list[-1] * b_list[-1] * 2*np.pi * b_step_size 


    return dipole_amplitude_integrated


def write_b_integrated(file_name_start, file_name_end, file_name_output):
    dir_path_input = os.path.dirname(os.path.realpath(__file__)) + r'/../cpp/data/au_dipole_amplitudes/'
    dir_path_output = os.path.dirname(os.path.realpath(__file__)) + r'/../cpp/data/au_dipole_amplitudes_integrated/'

    b_values_string = ["0.000000", "2.000000","4.000000","6.000000","8.000000","10.000000","12.000000","14.000000","16.000000","18.000000", "20.000000", "22.000000", "24.000000", "26.000000", "28.000000", "30.000000"]
    b_values = [float(b) for b in b_values_string]

    dipole_amplitude_list = []
    r_min_list = []
    r_factor_list = []
    r_number_list = []
    Y0_list = []
    Yvector_list = []

    for i in range( len(b_values_string) ):
        file_name = dir_path_input + file_name_start + b_values_string[i] + file_name_end
        results = read_file(file_name)
        r_min_list += [results["r_min"]]
        r_factor_list += [results["r_factor"]]
        r_number_list += [results["r_number"]]
        Y0_list += [results["Y0"]]
        Yvector_list += [results["Y_vector"]]
        dipole_amplitude_list += [results["dipole_amplitude"]]


    dipole_amplitude_integrated = b_integrate( dipole_amplitude_list, b_values )

    file_o = dir_path_output + file_name_output

    with open(file_o, "w") as f:

        f.write( "###" + str(r_min_list[0]) + '\n')
        f.write( "###" + str(r_factor_list[0])  + '\n' )
        f.write( "###" + str(r_number_list[0])  + '\n' )
        f.write( "###" + str(Y0_list[0])  + '\n' )

        for Y_idx in range( len( Yvector_list[0] ) ):
            f.write( "###" + str( Yvector_list[0][Y_idx] )  + '\n' )
            for r_idx in range( r_number_list[0] ):
                f.write( str(  dipole_amplitude_integrated[ Y_idx, r_idx ])  + '\n' )



def main():

    file_name_start_1 = "dipole_kcbk_balsdrc_x0bk0.010000_qs0sqr0.090500_asC^20.845969_gamma1.210000_sigma044.561200_impactb"
    file_name_end_1 = "_A197.000000_ec1.000000_eta00.000000_maxy16.118096_euler1_step0.050000_rpoints100_rminmax0.000001--30.000000_intacc0.010000"
    file_output_1 = "dipole_kcbk_balsd_x0bk0.010000_lightq.dat"

    file_name_start_2 = "dipole_kcbk_pdrc_x0bk0.010000_qs0sqr0.083300_asC^23.493261_gamma0.980000_sigma050.021800_impactb"
    file_name_end_2 = "_A197.000000_ec1.000000_eta00.000000_maxy16.118096_euler1_step0.050000_rpoints100_rminmax0.000001--30.000000_intacc0.010000"
    file_output_2 = "dipole_kcbk_pd_x0bk0.010000_lightq.dat"

    file_name_start_3 = "dipole_resumbk_pdrc_x0bk1.000000_qs0sqr0.079400_asC^21477.595475_gamma1.920000_sigma0137.071800_impactb"
    file_name_end_3 = "_A197.000000_ec1.000000_eta00.000000_maxy20.723266_euler0_step0.400000_rpoints100_rminmax0.000001--30.000000_intacc0.010000"
    file_output_3 = "dipole_resumbk_pd_x0bk1.000000_lightq.dat"

    write_b_integrated( file_name_start_1, file_name_end_1, file_output_1 )
    write_b_integrated( file_name_start_2, file_name_end_2, file_output_2 )
    write_b_integrated( file_name_start_3, file_name_end_3, file_output_3 )



if( __name__ == "__main__" ):
    main()