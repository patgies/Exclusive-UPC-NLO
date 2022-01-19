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

repeat () {
	for (( i=0; i<= $1; i++ )); do echo -n "$2"; done
}

evaluation_points () {
    FIXED_PARAMETER=$1          # The parameter that is kept fixed. W or Q2.
    PARTICLE=$2                 # The particle we are interested in. jpsi or upsilon.

    if [ ${FIXED_PARAMETER} = "W" ]
    then

        W_CONST=90                    # If W is constant, which value to use? [GeV]

        Q2_POINTS=20            # Number of points where to evaluate in Q^2

        # Q2_MIN=0.01             # Min value of evaluation for Q^2
        # Q2_MAX=100              # Max value of evaluation for Q^2

        Q2="0.01 0.016237767391887217 0.026366508987303583 0.04281332398719394 0.06951927961775606 0.1128837891684689 0.18329807108324356 0.2976351441631318 0.4832930238571752 0.7847599703514611 1.2742749857031335 2.06913808111479 3.359818286283781 5.455594781168521 8.858667904100823 14.384498882876631 23.357214690901216 37.9269019073225 61.584821106602604 100.0"
        W=`repeat $Q2_POINTS "$W_CONST "`

    elif [ ${FIXED_PARAMETER} = "Q2" ]
    then
        Q2=0.05                 # If Q^2 is constant, which value to use? [GeV^2]
        W_POINTS=20             # Number of points where to evaluate in W

        if [ ${PARTICLE} = "jpsi" ]
        then
            # W_MIN=20            # Min value of evaluation for W
            # W_MAX=3000          # Max value of evaluation for W
            W="20.0 26.035211769468635 33.89161259405391 44.11876555474919 57.432070211271686 74.76280551547248 97.32327370374618 126.6916020487495 164.922134437622 214.68913477781325 279.4738544272181 363.80804920211375 473.5909802207147 616.5020731078271 802.5381014839355 1044.712471260079 1359.9655213730532 1770.3495174061638 2304.571229582303 3000.0"
        elif [ ${PARTICLE} = "upsilon" ]
        then
            # W_MIN=50            # Min value of evaluation for W
            # W_MAX=5000          # Max value of evaluation for W
            W="50.0 63.71374928515669 81.18883695943609 103.45690405573949 131.8325449365179 167.9909143141891 214.06661993596967 272.77973905842595 347.5963980887803 442.9333952050412 564.4189458423444 719.2249441438315 916.4903554162178 1167.8607345450612 1488.175720815659 1896.3450953661247 2416.465119285876 3079.241055330132 3923.7998517573055 5000.0"
        else
            echo "Invalid particle: ${PARTICLE}"
            exit 1
        fi

        Q2=`repeat $W_POINTS "$Q2_CONST "`

    else
        echo "Invalid parameter: ${PARTICLE}"
        exit 1
    fi

    return -W $W -Q2 $Q2

}


echo Folder for the config = $INPUT_FOLDER
echo Folder for the code = $CODE_FOLDER
echo Folder for the output, longitudinal = $OUTPUT_FOLDER_L
echo Folder for the output, transverse = $OUTPUT_FOLDER_T

date +"%d-%m-%y %T"

calculate_amplitude conf points files(L or T)

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
