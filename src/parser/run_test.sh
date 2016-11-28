#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -d.


python parseFilesLoadToDB.py -rp /mnt/lustre/lena/StereoGene/hea/hea_result_new/all_result_files -st /mnt/lustre/lena/StereoGene/hea/hea_result_new/statistics/statistics_tissue_Breast_Fibroblast_Primary_Cells -o homo_sapiens -v hg19 -chr /mnt/lustre/lena/StereoGene/All_tests/hea/human_chrom -cf /mnt/lustre/lena/StereoGene/hea/params/HEA_Breast_Fibroblast_Primary_Cells.cfg
python parseFilesLoadToDB.py -rp /mnt/lustre/lena/StereoGene/hea/hea_result_new/all_result_files -st /mnt/lustre/lena/StereoGene/hea/hea_result_new/statistics/statistics_feature_H3K4ac -o homo_sapiens -v hg19 -chr /mnt/lustre/lena/StereoGene/All_tests/hea/human_chrom -cf /mnt/lustre/lena/StereoGene/hea/params/HEA_H3K4ac.cfg
python parseFilesLoadToDB.py -rp /mnt/lustre/lena/StereoGene/hea/hea_result_new/all_result_files -st /mnt/lustre/lena/StereoGene/hea/hea_result_new/statistics/statistics_feature_H3K79me1 -o homo_sapiens -v hg19 -chr /mnt/lustre/lena/StereoGene/All_tests/hea/human_chrom -cf /mnt/lustre/lena/StereoGene/hea/params/HEA_H3K79me1.cfg
python parseFilesLoadToDB.py -rp /mnt/lustre/lena/StereoGene/hea/hea_result_new/all_result_files -st /mnt/lustre/lena/StereoGene/hea/hea_result_new/statistics/statistics_feature_H4K8ac -o homo_sapiens -v hg19 -chr /mnt/lustre/lena/StereoGene/All_tests/hea/human_chrom -cf /mnt/lustre/lena/StereoGene/hea/params/HEA_H4K8ac.cfg
