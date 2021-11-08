#!/bin/sh

CODE_FOLDER=build/bin                   # Where is the actual program?
INPUT_FOLDER=config_files               # Where are the config files located?
OUTPUT_FOLDER_L=output/longitudinal     # Where to output the longitudinal production files?
OUTPUT_FOLDER_T=output/transverse       # Where to output the transverse productin files?

calculate_amplitude () {
    CONF=$1                 # configuration used (e.g. kcbk-hera-bal+sd-0.00)
    CONST_W_OR_Q2=$2        # Which is constant, W or Q^2? 'W' or 'Q2'
    BOOL_L=$3               # Calculate longitudinal production? true or false
    BOOL_T=$4               # Calculate transverse produciton? true or false
    PARTICLE=${5:-"jpsi"}   # Which particle? Default: jpsi. Also works for "upsilon"
    INFO_STRING=$6          # Additional information, added to the names of the output files
    PARAMETERS=$7           # Additional parameters in the call


    NTHREAD=20              # Number of threads used in the calculation
    Q2=0.05                 # If Q^2 is constant, which value to use? [GeV^2]
    W=90                    # If W is constant, which value to use? [GeV]

    W_POINTS=20             # Number of points where to evaluate in W
    Q2_POINTS=20            # Number of points where to evaluate in Q^2

    Q2_MIN=0.01             # Min value of evaluation for Q^2
    Q2_MAX=100              # Max value of evaluation for Q^2

    if [ ${PARTICLE} = "jpsi" ]
    then
        W_MIN=20            # Min value of evaluation for W
        W_MAX=3000          # Max value of evaluation for W
    elif [ ${PARTICLE} = "upsilon" ]
    then
        W_MIN=50            # Min value of evaluation for W
        W_MAX=5000          # Max value of evaluation for W
    else
        echo "Invalid particle: ${PARTICLE}"
        exit 1
    fi


    if [ $CONST_W_OR_Q2 = "W" ]
    then
        POINTS="-W ${W} -Q2min ${Q2_MIN} -Q2max ${Q2_MAX} -Q2points ${Q2_POINTS}"
        CONST_STRING="W_${W}"
    elif [ $CONST_W_OR_Q2 = "Q2" ]
    then
        POINTS="-Q2 ${Q2} -Wmin ${W_MIN} -Wmax ${W_MAX} -Wpoints ${W_POINTS}"
        CONST_STRING="Q2_${Q2}"
    else
        echo "Invalid choice (should be W or Q2): ${CONST_W_OR_Q2}"
        exit 1
    fi

    if [ $BOOL_L = true ]
    then
        ${CODE_FOLDER}/NLO_amplitude ${POINTS} ${PARAMETERS} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-${CONF}-${PARTICLE}.txt -ofileL ${OUTPUT_FOLDER_L}/results-${CONF}-${PARTICLE}-L-${CONST_STRING}${INFO_STRING}.dat
    fi

    if [ $BOOL_T = true ]
    then
        ${CODE_FOLDER}/NLO_amplitude ${POINTS} ${PARAMETERS} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-${CONF}-${PARTICLE}.txt -ofileT ${OUTPUT_FOLDER_T}/results-${CONF}-${PARTICLE}-T-${CONST_STRING}${INFO_STRING}.dat
    fi

    echo ${CONF}, ${CONST_W_OR_Q2}
    date +"%d-%m-%y %T"
}


echo Folder for the config = $INPUT_FOLDER
echo Folder for the code = $CODE_FOLDER
echo Folder for the output, longitudinal = $OUTPUT_FOLDER_L
echo Folder for the output, transverse = $OUTPUT_FOLDER_T

date +"%d-%m-%y %T"



calculate_amplitude "kcbk-hera-bal+sd-4.61" "Q2" true true "jpsi"
calculate_amplitude "kcbk-hera-bal+sd-0.00" "Q2" true true "jpsi"
calculate_amplitude "resumbk-hera-bal+sd-4.61" "Q2" true true "jpsi"
calculate_amplitude "resumbk-hera-bal+sd-0.00" "Q2" true true "jpsi"
calculate_amplitude "tbk-hera-bal+sd-4.61" "Q2" true true "jpsi"
calculate_amplitude "tbk-hera-bal+sd-0.00" "Q2" true true "jpsi"
calculate_amplitude "LOBK-MVe" "Q2" true true "jpsi" "" "-relxpom -fast"

calculate_amplitude "kcbk-hera-bal+sd-4.61" "W" true true "jpsi"
calculate_amplitude "kcbk-hera-bal+sd-0.00" "W" true true "jpsi"
calculate_amplitude "resumbk-hera-bal+sd-4.61" "W" true true "jpsi"
calculate_amplitude "resumbk-hera-bal+sd-0.00" "W" true true "jpsi"
calculate_amplitude "tbk-hera-bal+sd-4.61" "W" true true "jpsi"
calculate_amplitude "tbk-hera-bal+sd-0.00" "W" true true "jpsi"
calculate_amplitude "LOBK-MVe" "W" true true "jpsi" "" "-relxpom -fast"

calculate_amplitude "kcbk-hera-bal+sd-4.61" "Q2" false true "upsilon"
calculate_amplitude "kcbk-hera-bal+sd-0.00" "Q2" false true "upsilon"
calculate_amplitude "resumbk-hera-bal+sd-4.61" "Q2" false true "upsilon"
calculate_amplitude "resumbk-hera-bal+sd-0.00" "Q2" false true "upsilon"
calculate_amplitude "tbk-hera-bal+sd-4.61" "Q2" false true "upsilon"
calculate_amplitude "tbk-hera-bal+sd-0.00" "Q2" false true "upsilon"
calculate_amplitude "LOBK-MVe" "Q2" false true "upsilon" "" "-relxpom -fast"
