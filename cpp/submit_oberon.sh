#!/bin/bash
#SBATCH --job-name=nlo_amplitudes
#SBATCH --output=slurm-%j.out
#SBATCH --error=slurm-%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20
#SBATCH --sockets-per-node=1
#SBATCH --time=24:00:00
#SBATCH --partition=normal


cd "$SLURM_SUBMIT_DIR"
time ./calculate_amplitudes.sh
