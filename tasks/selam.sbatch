#!/bin/bash
#SBATCH --job-name=selam_generator
#SBATCH --error=selam_errors.txt
#SBATCH --output=selam_results.txt
#SBATCH --time=00:10:00
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --deadline=00:10:00

module load libs/gsl/2.6
export PATH=$PATH:/home/avshmelev/SELAM-master/SELAM-master/src
cd ..
cd selam
srun ./data_generator.txt 0.01 10