#!/bin/sh

CODE_FOLDER=build/bin
INPUT_FOLDER=config_files
OUTPUT_FOLDER_L=output/longitudinal
OUTPUT_FOLDER_T=output/transverse

PARTICLE=jpsi
NTHREAD=20
Q2=0.05
W=90
# Wmin=50
# Wmax=5000
if [ ${PARTICLE} = jpsi ]
then
    Wmin=20
    Wmax=3000
elif [ ${PARTICLE} = upsilon ]
then
    Wmin=50
    Wmax=5000
else
    echo "Invalid particle ${PARTICLE}"
    exit 1
fi

Q2min=0.01
Q2max=100
Wpoints=20
Q2points=20

echo Folder for the config = $INPUT_FOLDER
echo Folder for the code = $CODE_FOLDER
echo Folder for the output, longitudinal = $OUTPUT_FOLDER_L
echo Folder for the output, transverse = $OUTPUT_FOLDER_T

date +"%d-%m-%y %T"

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61.txt -ofileL ${OUTPUT_FOLDER_L}/results-kcbk-hera-bal+sd-4.61-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-4.61-T-W_${W}.dat 
# echo KCBK 4.61, W ${W}

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-0.00.txt -ofileL ${OUTPUT_FOLDER_L}/results-kcbk-hera-bal+sd-0.00-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-0.00-T-W_${W}.dat 
# echo KCBK 0.00, W ${W}

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-4.61.txt -ofileL ${OUTPUT_FOLDER_L}/results-tbk-hera-bal+sd-4.61-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-tbk-hera-bal+sd-4.61-T-W_${W}.dat 
# echo TBK 4.61, W ${W}

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-0.00.txt -ofileL ${OUTPUT_FOLDER_L}/results-tbk-hera-bal+sd-0.00-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-tbk-hera-bal+sd-0.00-T-W_${W}.dat 
# echo TBK 0.00, W ${W}

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-4.61.txt -ofileL ${OUTPUT_FOLDER_L}/results-resumbk-hera-bal+sd-4.61-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-resumbk-hera-bal+sd-4.61-T-W_${W}.dat 
# echo ResumBK 4.61, W ${W}

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-0.00.txt -ofileL ${OUTPUT_FOLDER_L}/results-resumbk-hera-bal+sd-0.00-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-resumbk-hera-bal+sd-0.00-T-W_${W}.dat 
# echo ResumBK 0.00, W ${W}

# ${CODE_FOLDER}/NLO_amplitude -fast -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-4.61.txt -ofileL ${OUTPUT_FOLDER_L}/results-tbk-hera-bal+sd-4.61-L-W_${W}-fast.dat -ofileT ${OUTPUT_FOLDER_T}/results-tbk-hera-bal+sd-4.61-T-W_${W}-fast.dat 
# echo TBK 4.61, W ${W} -fast
# date +"%d-%m-%y %T"


# ${CODE_FOLDER}/NLO_amplitude -fast -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61.txt -ofileL ${OUTPUT_FOLDER_L}/results-kcbk-hera-bal+sd-4.61-L-fast.dat -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-4.61-T-fast.dat 
# echo KCBK 4.61 fast

# ${CODE_FOLDER}/NLO_amplitude -fast -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61.txt -ofileL ${OUTPUT_FOLDER_L}/results-kcbk-hera-bal+sd-4.61-L-fast.dat -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-4.61-T-fast.dat 
# echo KCBK 4.61 fast

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61-m1.4.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-hera-bal+sd-4.61_Q2_0.05-m_1.4.dat 
# echo KCBK 4.61 m1.4

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-0.00-m1.4.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-hera-bal+sd-0.00_Q2_0.05-m_1.4.dat 
# echo KCBK 0.00 m1.4

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-4.61-m1.4.txt -ofile ${OUTPUT_FOLDER}/results-tbk-hera-bal+sd-4.61_Q2_0.05-m_1.4.dat 
# echo TBK 4.61 m1.4

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-0.00-m1.4.txt -ofile ${OUTPUT_FOLDER}/results-tbk-hera-bal+sd-0.00_Q2_0.05-m_1.4.dat 
# echo TBK 0.00 m1.4

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-4.61-m1.4.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-4.61_Q2_0.05-m_1.4.dat 
# echo RESUMBK 4.61 m1.4

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-0.00-m1.4.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-0.00_Q2_0.05-m_1.4.dat 
# echo RESUMBK 0.00 m1.4

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -fast -ifile ${INPUT_FOLDER}/conf_LOBK_MVe-m1.4.txt -ofile ${OUTPUT_FOLDER}/results-LOBK-MVe_Q2_0.05-m_1.4.dat 
# echo MVe m 1.4


# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-lightq-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-lightq-bal+sd-0.00.dat 
# echo KCBK 0.00 lightq 


# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-lightq-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-lightq-bal+sd-4.61.dat 
# echo KCBK 4.61 lightq 



# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61.txt -ofileL ${OUTPUT_FOLDER_L}/results-kcbk-hera-bal+sd-4.61-L.dat -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-4.61-T.dat 
# echo KCBK 4.61

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-hera-bal+sd-0.00_Q2_0.05.dat 
# echo KCBK 0.00

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-tbk-hera-bal+sd-4.61_Q2_0.05.dat 
# echo TBK 4.61

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-tbk-hera-bal+sd-0.00_Q2_0.05.dat 
# echo TBK 0.00

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-4.61_Q2_0.05.dat 
# echo RESUMBK 4.61
# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-4.61_Q2_0.05-TEST.dat 
# echo RESUMBK 4.61 test

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-0.00_Q2_0.05.dat 
# echo RESUMBK 0.00

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-hera-bal+sd-4.61-Q.dat
# echo KCBK 4.61 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-hera-bal+sd-0.00-Q.dat
# echo KCBK 0.00 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-tbk-hera-bal+sd-4.61-Q.dat
# echo tBK 4.61 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-tbk-hera-bal+sd-0.00-Q.dat
# echo tBK 0.00 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-4.61-Q.dat
# echo resumBK 4.61 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-0.00-Q.dat
# echo resumBK 0.00 Q 




# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -thread ${NTHREAD} -fast -ifile ${INPUT_FOLDER}/conf-IP_SAT.txt -ofile ${OUTPUT_FOLDER}/results-IP_SAT.dat 
# echo IP SAT 

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -fast -ifile ${INPUT_FOLDER}/conf-IP_SAT_m1.4.txt -ofile ${OUTPUT_FOLDER}/results-IP_SAT_m1.4.dat 
# echo IP SAT m1.4 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -fast -ifile ${INPUT_FOLDER}/conf-IP_SAT_m1.4.txt -ofile ${OUTPUT_FOLDER}/results-IP_SAT_m1.4-Q.dat
# echo IPsat m1.4 Q

# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -fast -relxpom -ifile ${INPUT_FOLDER}/conf_LOBK_MVe.txt -ofileL ${OUTPUT_FOLDER_L}/results-LOBK-MVe_Q2_0.05.dat -ofileT ${OUTPUT_FOLDER_T}/results-LOBK-MVe_Q2_0.05.dat 
# echo MVe

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -fast -relxpom -ifile ${INPUT_FOLDER}/conf_LOBK_MVe.txt -ofileL ${OUTPUT_FOLDER_L}/results-LOBK-MVe-W_90.dat -ofileT ${OUTPUT_FOLDER_T}/results-LOBK-MVe-W_90.dat
# echo MVe Q


# ${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -fast -ifile ${INPUT_FOLDER}/conf_LOBK_MVgamma.txt -ofile ${OUTPUT_FOLDER}/results-LOBK-MVgamma.dat 
# echo MVgamma

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -fast -ifile ${INPUT_FOLDER}/conf_LOBK_MVgamma.txt -ofile ${OUTPUT_FOLDER}/results-LOBK-MVgamma-Q.dat
# echo MVgamma Q

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -fast -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/KCBK-4.61-Q-test1.dat
# echo KCBK test Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-hera-bal+sd-4.61-Q.dat
# echo KCBK 4.61 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-kcbk-hera-bal+sd-0.00-Q.dat
# echo KCBK 0.00 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-tbk-hera-bal+sd-4.61-Q.dat
# echo tBK 4.61 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-tbk-hera-bal+sd-0.00-Q.dat
# echo tBK 0.00 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-4.61-Q.dat
# echo resumBK 4.61 Q 

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-0.00.txt -ofile ${OUTPUT_FOLDER}/results-resumbk-hera-bal+sd-0.00-Q.dat
# echo resumBK 0.00 Q 




# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min 23.3572147 -Q2max ${Q2max} -Q2points 4 -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-A197-kcbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-A197-kcbk-hera-bal+sd-4.61-Q2-100.dat
# echo nucl A  197 Q100




# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-A197-kcbk-hera-bal+sd-4.61.txt -ofile ${OUTPUT_FOLDER}/results-A197-kcbk-hera-bal+sd-4.61-Q.dat
# echo nucl A  197 Q


# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-0.00-${PARTICLE}.txt -ofileL ${OUTPUT_FOLDER_L}/results-kcbk-hera-bal+sd-0.00-${PARTICLE}-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-0.00-${PARTICLE}-T-W_${W}.dat 
# echo KCBK 0.00, W ${W}
# date +"%d-%m-%y %T"

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61-${PARTICLE}.txt -ofileL ${OUTPUT_FOLDER_L}/results-kcbk-hera-bal+sd-4.61-${PARTICLE}-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-4.61-${PARTICLE}-T-W_${W}.dat 
# echo KCBK 4.61, W ${W}
# date +"%d-%m-%y %T"

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-0.00-${PARTICLE}.txt -ofileL ${OUTPUT_FOLDER_L}/results-resumbk-hera-bal+sd-0.00-${PARTICLE}-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-resumbk-hera-bal+sd-0.00-${PARTICLE}-T-W_${W}.dat 
# echo ResumBK 0.00, W ${W}
# date +"%d-%m-%y %T"

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-4.61-${PARTICLE}.txt -ofileL ${OUTPUT_FOLDER_L}/results-resumbk-hera-bal+sd-4.61-${PARTICLE}-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-resumbk-hera-bal+sd-4.61-${PARTICLE}-T-W_${W}.dat 
# echo ResumBK 4.61, W ${W}
# date +"%d-%m-%y %T"

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-0.00-${PARTICLE}.txt -ofileL ${OUTPUT_FOLDER_L}/results-tbk-hera-bal+sd-0.00-${PARTICLE}-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-tbk-hera-bal+sd-0.00-${PARTICLE}-T-W_${W}.dat 
# echo TBK 0.00, W ${W}
# date +"%d-%m-%y %T"

# ${CODE_FOLDER}/NLO_amplitude -W ${W} -Q2min ${Q2min} -Q2max ${Q2max} -Q2points ${Q2points} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-4.61-${PARTICLE}.txt -ofileL ${OUTPUT_FOLDER_L}/results-tbk-hera-bal+sd-4.61-${PARTICLE}-L-W_${W}.dat -ofileT ${OUTPUT_FOLDER_T}/results-tbk-hera-bal+sd-4.61-${PARTICLE}-T-W_${W}.dat 
# echo TBK 4.61, W ${W}
# date +"%d-%m-%y %T"



${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-0.00-${PARTICLE}.txt -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-0.00-${PARTICLE}-T-Q2_${Q2}.dat 
echo KCBK 0.00, Q2 ${Q2}
date +"%d-%m-%y %T"

${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-kcbk-hera-bal+sd-4.61-${PARTICLE}.txt -ofileT ${OUTPUT_FOLDER_T}/results-kcbk-hera-bal+sd-4.61-${PARTICLE}-T-Q2_${Q2}.dat 
echo KCBK 4.61, Q2 ${Q2}
date +"%d-%m-%y %T"

${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-0.00-${PARTICLE}.txt -ofileT ${OUTPUT_FOLDER_T}/results-resumbk-hera-bal+sd-0.00-${PARTICLE}-T-Q2_${Q2}.dat 
echo ResumBK 0.00, Q2 ${Q2}
date +"%d-%m-%y %T"

${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-resumbk-hera-bal+sd-4.61-${PARTICLE}.txt -ofileT ${OUTPUT_FOLDER_T}/results-resumbk-hera-bal+sd-4.61-${PARTICLE}-T-Q2_${Q2}.dat 
echo ResumBK 4.61, Q2 ${Q2}
date +"%d-%m-%y %T"

${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-0.00-${PARTICLE}.txt -ofileT ${OUTPUT_FOLDER_T}/results-tbk-hera-bal+sd-0.00-${PARTICLE}-T-Q2_${Q2}.dat 
echo TBK 0.00, Q2 ${Q2}
date +"%d-%m-%y %T"

${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf-tbk-hera-bal+sd-4.61-${PARTICLE}.txt -ofileT ${OUTPUT_FOLDER_T}/results-tbk-hera-bal+sd-4.61-${PARTICLE}-T-Q2_${Q2}.dat 
echo TBK 4.61, Q2 ${Q2}
date +"%d-%m-%y %T"

${CODE_FOLDER}/NLO_amplitude -Q2 ${Q2} -Wmin ${Wmin} -Wmax ${Wmax} -Wpoints ${Wpoints} -relxpom -fast -thread ${NTHREAD} -ifile ${INPUT_FOLDER}/conf_LOBK_MVe-${PARTICLE}.txt -ofileT ${OUTPUT_FOLDER_T}/results-LOBK-MVe-${PARTICLE}-T-Q2_${Q2}.dat 
echo MVe, Q2 ${Q2}
date +"%d-%m-%y %T"