#!/bin/bash

CODE_FOLDER=build/bin                   # Where is the actual program?
INPUT_FOLDER=config_files               # Where are the config files located?
OUTPUT_FOLDER_L=output/longitudinal     # Where to output the longitudinal production files?
OUTPUT_FOLDER_T=output/transverse       # Where to output the transverse productin files?

calculate_amplitude () {
    CONF=$1                 # configuration file used (e.g. -conf-kcbk-hera-bal+sd-0.00.sh)
    FIXED_PARAMETER=$2      # Which is constant, W or Q^2? 'W' or 'Q2'
    FIXED_VALUE=$3          # Value of the fixed constant
    PARAMETER_MIN=$4        # Min value for the varied parameter
    PARAMETER_MAX=$5        # Min value for the varied parameter
    BOOL_L=$6               # Calculate longitudinal production? true or false
    BOOL_T=$7               # Calculate transverse produciton? true or false
    PARTICLE=${8:-"jpsi"}   # Which particle? Default: jpsi. Also works for "upsilon"
    ACCURACY_LEVEL=$9       # Level of accuracy for integration
    INFO_STRING=${10}          # Additional information, added to the names of the output files
    PARAMETERS=${11}           # Additional parameters in the call


    NTHREAD=8              # Number of threads used in the calculation
    
    evaluation_points $FIXED_PARAMETER $FIXED_VALUE $PARAMETER_MIN $PARAMETER_MAX
    source ${INPUT_FOLDER}/conf-${CONF}.sh
    masses $PARTICLE
    integration_points $ACCURACY_LEVEL

    if [ $BOOL_L = true ]
    then
        ${CODE_FOLDER}/NLO_amplitude $ACCURACY_STRING $CONF_STRING $POINTS_STRING $MASS_STRING $PARAMETERS -thread ${NTHREAD} -ofileL ${OUTPUT_FOLDER_L}/results-${CONF}-${PARTICLE}-L-${FIXED_PARAMETER}_${FIXED_VALUE}${INFO_STRING}.dat
    fi

    if [ $BOOL_T = true ]
    then
        ${CODE_FOLDER}/NLO_amplitude $ACCURACY_STRING $CONF_STRING $POINTS_STRING $MASS_STRING $PARAMETERS -thread ${NTHREAD} -ofileT ${OUTPUT_FOLDER_T}/results-${CONF}-${PARTICLE}-T-${FIXED_PARAMETER}_${FIXED_VALUE}${INFO_STRING}.dat
    fi

    echo ${CONF}, ${FIXED_PARAMETER}
    date +"%d-%m-%y %T"
}

repeat () {
	for (( i=0; i< $1; i++ )); do echo -n "$2"; done
}

evaluation_points () {
    FIXED_PARAMETER=$1          # The parameter that is kept fixed. W or Q2.
    FIXED_VALUE=$2              # Value of the fixed parameter
    PARAMETER_MIN=$3            # Min value for the varied parameter
    PARAMETER_MAX=$4            # Min value for the varied parameter

    # if [ ${FIXED_PARAMETER} = "W" ]
    # then

    #     W_CONST=90                    # If W is constant, which value to use? [GeV]

    #     Q2_POINTS=20            # Number of points where to evaluate in Q^2

    #     # Q2_MIN=0.01             # Min value of evaluation for Q^2
    #     # Q2_MAX=100              # Max value of evaluation for Q^2

    #     Q2="0.01 0.016237767391887217 0.026366508987303583 0.04281332398719394 0.06951927961775606 0.1128837891684689 0.18329807108324356 0.2976351441631318 0.4832930238571752 0.7847599703514611 1.2742749857031335 2.06913808111479 3.359818286283781 5.455594781168521 8.858667904100823 14.384498882876631 23.357214690901216 37.9269019073225 61.584821106602604 100.0"
    #     W=`repeat $Q2_POINTS "$W_CONST "`

    # elif [ ${FIXED_PARAMETER} = "Q2" ]
    # then
    #     Q2_CONST=0.05                 # If Q^2 is constant, which value to use? [GeV^2]
    #     W_POINTS=20             # Number of points where to evaluate in W

    #     if [ ${PARTICLE} = "jpsi" ]
    #     then
    #         # W_MIN=20            # Min value of evaluation for W
    #         # W_MAX=3000          # Max value of evaluation for W
    #         W="20.0 26.035211769468635 33.89161259405391 44.11876555474919 57.432070211271686 74.76280551547248 97.32327370374618 126.6916020487495 164.922134437622 214.68913477781325 279.4738544272181 363.80804920211375 473.5909802207147 616.5020731078271 802.5381014839355 1044.712471260079 1359.9655213730532 1770.3495174061638 2304.571229582303 3000.0"
    #     elif [ ${PARTICLE} = "upsilon" ]
    #     then
    #         # W_MIN=50            # Min value of evaluation for W
    #         # W_MAX=5000          # Max value of evaluation for W
    #         W="50.0 63.71374928515669 81.18883695943609 103.45690405573949 131.8325449365179 167.9909143141891 214.06661993596967 272.77973905842595 347.5963980887803 442.9333952050412 564.4189458423444 719.2249441438315 916.4903554162178 1167.8607345450612 1488.175720815659 1896.3450953661247 2416.465119285876 3079.241055330132 3923.7998517573055 5000.0"
    #     else
    #         echo "Invalid particle: ${PARTICLE}"
    #         exit 1
    #     fi

    #     Q2=`repeat $W_POINTS "$Q2_CONST "`
    # else
    #     echo "Invalid parameter: ${FIXED_PARAMETER}"
    #     exit 1
    # fi

    # POINTS_STRING="-W $W -Q2 $Q2"


    if [ ${FIXED_PARAMETER} = "W" ]
    then


        N_POINTS=20            # Number of points where to evaluate in Q^2
        Q2_MIN=${PARAMETER_MIN}
        Q2_MAX=${PARAMETER_MAX}

        # N_POINTS=50            # Number of points where to evaluate in Q^2
        # Q2_MIN=1
        # Q2_MAX=10000

        W_MIN=${FIXED_VALUE}
        W_MAX=${FIXED_VALUE}

        # W_MIN=75              # If W is constant, which value to use? [GeV]
        # W_MAX=75              # If W is constant, which value to use? [GeV]
        # Q2_POINTS=50


    elif [ ${FIXED_PARAMETER} = "Q2" ]
    then
        N_POINTS=20             # Number of points where to evaluate in W

        # Q2_MIN=15.8
        # Q2_MAX=15.8
        Q2_MIN=${FIXED_VALUE}
        Q2_MAX=${FIXED_VALUE}

        W_MIN=${PARAMETER_MIN}            # Min value of evaluation for W
        W_MAX=${PARAMETER_MAX}          # Max value of evaluation for W
    else
        echo "Invalid parameter: ${FIXED_PARAMETER}"
        exit 1
    fi


    Q2=`python3 evaluation_points.py $Q2_MIN $Q2_MAX $N_POINTS`
    W=`python3 evaluation_points.py $W_MIN $W_MAX $N_POINTS`

    POINTS_STRING="-W $W -Q2 $Q2"

}

integration_points () {

    ACCURACY_LEVEL=$1       # Describes the level of accuracy, i.e. the amount of integration points used. 0,1,2,3 - higher valuer means more poitns (slower execution)

    if [ $ACCURACY_LEVEL = 0 ]
    then 
        DIM_LOW=10000
        DIM_4=10000
        DIM_6=10000
    elif [ $ACCURACY_LEVEL = 1 ]
    then 
        DIM_LOW=500000
        DIM_4=500000
        DIM_6=500000
    elif [ $ACCURACY_LEVEL = 2 ]
    then 
        DIM_LOW=500000
        DIM_4=5000000
        DIM_6=5000000
    elif [ $ACCURACY_LEVEL = 3 ]
    then 
        DIM_LOW=500000
        DIM_4=5000000
        DIM_6=20000000
    else
        echo "Invalid accuracy: ${ACCURACY_LEVEL}. Should be 0,1,2,3"
        exit 1
    fi

    ACCURACY_STRING="-int_points_dim_low $DIM_LOW -int_points_dim_4 $DIM_4 -int_points_dim_6 $DIM_6"

}


masses () {
    PARTICLE=$1                 # The particle we are interested in. jpsi or upsilon.

    if [ ${PARTICLE} = "jpsi" ]
    then
        M_V=3.0969
        M_Q=1.54845
    elif [ ${PARTICLE} = "upsilon" ]
    then
        M_V=9.46030
        M_Q=4.73015
    else
        echo "Invalid particle: ${PARTICLE}"
        exit 1
    fi

    MASS_STRING="-m_q $M_Q -M_V $M_V"
}


echo Folder for the config = $INPUT_FOLDER
echo Folder for the code = $CODE_FOLDER
echo Folder for the output, longitudinal = $OUTPUT_FOLDER_L
echo Folder for the output, transverse = $OUTPUT_FOLDER_T

date +"%d-%m-%y %T"

# CONF FIXED_PARAM FIXED_VALUE PARAM_MIN PARAM_MAX CALC_LONG CALC_TRANS PARTICLE ACCURACY INFO ADDITIONAL_OPTIONS

# calculate_amplitude "LOBK-as-const" "Q2" 0.01 30 1000 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "LOBK-as-const" "Q2" 0.01 30 1000 false true "jpsi" 2 "_minus_cutoff_10-x20x21" "-minus_cutoff 10"

# calculate_amplitude "LOBK-as-const" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "LOBK-as-const" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_10-x20x21" "-minus_cutoff 10"


# calculate_amplitude "tbk-lightq-parent-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21-tbkscheme" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-parent-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_10-x20x21" "-minus_cutoff 10"

# calculate_amplitude "tbk-lightq-parent-0.00-proj-rapidity" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-parent-0.00-proj-rapidity" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_10-x20x21" "-minus_cutoff 10"


# calculate_amplitude "kcbk-lightq-parent-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "kcbk-lightq-parent-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "kcbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "kcbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"

# calculate_amplitude "resumbk-lightq-parent-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-parent-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"

# calculate_amplitude "tbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"

# calculate_amplitude "kcbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "kcbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "kcbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "kcbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"

# calculate_amplitude "resumbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"

# calculate_amplitude "tbk-lightq-parent-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-parent-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"

# calculate_amplitude "LOBK-as-const_invariant_mass_rapidity" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"
calculate_amplitude "LOBK-as-const_invariant_mass_rapidity" "Q2" 0.01 30 1000 false true "jpsi" 2 "_minus_cutoff_1-x20x21" "-minus_cutoff 1"



# calculate_amplitude "LOBK-as-const" "Q2" 0.01 100 3000 false true "jpsi" 2 "_high-W"

# calculate_amplitude "kcbk-lightq-parent-0.00" "W" 90 0.01 100 true true "jpsi" 2 "_high-W"
# calculate_amplitude "resumbk-lightq-parent-0.00" "W" 90 0.01 100 true true "jpsi" 2 "_high-W"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "W" 90 0.01 100 true true "jpsi" 2 "_high-W"

# calculate_amplitude "tbk-lightq-parent-0.00" "W" 90 0.01 100 false true "jpsi" 2
# calculate_amplitude "tbk-lightq-parent-0.00" "W" 90 0.01 100 false true "upsilon" 2
# calculate_amplitude "tbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_high-W"
# calculate_amplitude "tbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2 "_high-W"

# calculate_amplitude "A197-kcbk-lightq-parent-0.00" "W" 90 0.01 100 true true "jpsi" 2
# calculate_amplitude "A197-resumbk-lightq-parent-0.00" "W" 90 0.01 100 true true "jpsi" 2
# calculate_amplitude "A197-tbk-lightq-bal+sd-0.00" "W" 90 0.01 100 true true "jpsi" 2

# calculate_amplitude "A197-tbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "jpsi" 2
# calculate_amplitude "A197-kcbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 
# calculate_amplitude "A197-resumbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 
# calculate_amplitude "A197-tbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 


# calculate_amplitude "kcbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 
# calculate_amplitude "resumbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 
# calculate_amplitude "kcbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2
# calculate_amplitude "resumbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "upsilon" 2


# calculate_amplitude "kcbk-hera-parent-4.61" "Q2" 0.01 30 3000 false true "jpsi" 2 
# calculate_amplitude "kcbk-hera-parent-4.61" "W" 90 0.01 100 true true "jpsi" 2


# calculate_amplitude "kcbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_Y0-4.61" "-Y0_if 4.61"
# calculate_amplitude "resumbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_Y0-4.61" "-Y0_if 4.61"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_Y0-4.61" "-Y0_if 4.61"


# calculate_amplitude "kcbk-lightq-parent-0.00" "W" 90 0.01 100 true true "jpsi" 2 "_Y0-4.61" "-Y0_if 4.61"
# calculate_amplitude "resumbk-lightq-parent-0.00" "W" 90 0.01 100 true true "jpsi" 2 "_Y0-4.61" "-Y0_if 4.61"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "W" 90 0.01 100 true true "jpsi" 2 "_Y0-4.61" "-Y0_if 4.61"


# calculate_amplitude "A197-kcbk-lightq-parent-0.00" "Q2" 0.01 100 3000 false true "jpsi" 2 "_high-W"
# calculate_amplitude "A197-resumbk-lightq-parent-0.00" "Q2" 0.01 100 3000 false true "jpsi" 2 "_high-W"
# calculate_amplitude "A197-tbk-lightq-bal+sd-0.00" "Q2" 0.01 100 3000 false true "jpsi" 2 "_high-W"

# calculate_amplitude "kcbk-lightq-parent-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-parent-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "jpsi" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"

# calculate_amplitude "kcbk-lightq-parent-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-parent-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "W" 90 0.01 100 false true "upsilon" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"



# calculate_amplitude "kcbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"
# calculate_amplitude "resumbk-lightq-parent-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"
# calculate_amplitude "tbk-lightq-bal+sd-0.00" "Q2" 0.01 30 3000 false true "jpsi" 2 "_minus_cutoff-x20x21" "-minus_cutoff 1"



# calculate_amplitude "kcbk-lightq-parent-4.61" "Q2" true true "jpsi" 2
# calculate_amplitude "kcbk-lightq-parent-0.00" "Q2" true true "jpsi" 2
# calculate_amplitude "resumbk-lightq-parent-4.61" "Q2" true true "jpsi" 2
# calculate_amplitude "resumbk-lightq-parent-0.00" "Q2" true true "jpsi" 2
# calculate_amplitude "tbk-lightq-parent-4.61" "Q2" true true "jpsi" 2
# calculate_amplitude "tbk-lightq-parent-0.00" "Q2" true true "jpsi" 2


# calculate_amplitude "kcbk-hera-bal+sd-4.61" "Q2" true true "jpsi" 2
# calculate_amplitude "kcbk-hera-bal+sd-0.00" "Q2" true true "jpsi" 2
# calculate_amplitude "resumbk-hera-bal+sd-4.61" "Q2" true true "jpsi" 2
# calculate_amplitude "resumbk-hera-bal+sd-0.00" "Q2" true true "jpsi" 2
# calculate_amplitude "tbk-hera-bal+sd-4.61" "Q2" true true "jpsi" 2
# calculate_amplitude "tbk-hera-bal+sd-0.00" "Q2" true true "jpsi" 2
# calculate_amplitude "LOBK-MVe" "Q2" true true "jpsi" 0 "" "-xpom"

# calculate_amplitude "kcbk-hera-bal+sd-4.61" "W" true true "jpsi" 2
# calculate_amplitude "kcbk-hera-bal+sd-0.00" "W" true true "jpsi" 2
# calculate_amplitude "resumbk-hera-bal+sd-4.61" "W" true true "jpsi" 2
# calculate_amplitude "resumbk-hera-bal+sd-0.00" "W" true true "jpsi" 2
# calculate_amplitude "tbk-hera-bal+sd-4.61" "W" true true "jpsi" 2
# calculate_amplitude "tbk-hera-bal+sd-0.00" "W" true true "jpsi" 2
# calculate_amplitude "LOBK-MVe" "W" true true "jpsi" 0 "" "-relxpom -fast"

# calculate_amplitude "kcbk-hera-bal+sd-4.61" "Q2" false true "upsilon" 3
# calculate_amplitude "kcbk-hera-bal+sd-0.00" "Q2" false true "upsilon" 3
# calculate_amplitude "resumbk-hera-bal+sd-4.61" "Q2" false true "upsilon" 3
# calculate_amplitude "resumbk-hera-bal+sd-0.00" "Q2" false true "upsilon" 3
# calculate_amplitude "tbk-hera-bal+sd-4.61" "Q2" false true "upsilon" 3
# calculate_amplitude "tbk-hera-bal+sd-0.00" "Q2" false true "upsilon" 3
# calculate_amplitude "LOBK-MVe" "Q2" false true "upsilon" 0 "" "-relxpom -fast"
