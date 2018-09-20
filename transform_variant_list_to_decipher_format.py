import pandas as pd
import glob
import os
import openpyxl
import re
import numpy as np


# Change the location of the variant list and chromosome sex list as required
var_list = '/media/sf_G_DRIVE/DNA/NON CANCER SECTION/Rare diseases Variant lists/Rare Diseases Variant List.xlsx'
chr_sex = '/media/sf_Shared/TSO_DECIPHER_Variants/TSO-sex.xls'
output_file = '/media/sf_Shared/TSO_DECIPHER_Variants/reformatted_variants.xlsx'

# Open the variants spreadsheet
var_file = pd.ExcelFile(var_list)
var_data = pd.read_excel(var_file, sheet_name='Rare diseases TSO variant list').reset_index(drop=True)

# remove class 1s
var_data = var_data[var_data['CLASSIFICATION'] != 'Class 1'].reset_index(drop=True)

#remove variants that have been previosly uploaded to DECIPHER
var_data = var_data[var_data['Uploaded'] != 'Uploaded'].reset_index(drop=True)

# Open the sex spreadsheet
chr_sex_file = pd.ExcelFile(chr_sex)
chr_sex_data = pd.read_excel(chr_sex_file).reset_index(drop=True)

# replace dot in lab numbers with dashes and determine the chromosomal sex
for i in range(len(chr_sex_data)):
    chr_sex_data.loc[i,'Internal Reference'] = re.sub('\.','-',chr_sex_data['LABNO'][i])
    if chr_sex_data['SEX'][i] == 'F':
        chr_sex_data.loc[i,'Chromosomal sex'] = '46XX'
    elif chr_sex_data['SEX'][i] == 'M':
        chr_sex_data.loc[i,'Chromosomal sex'] = '46XY'
    elif chr_sex_data['SEX'][i] == 'U':
        chr_sex_data.loc[i,'Chromosomal sex'] = 'Undetermined'
    else:
        chr_sex_data.loc[i,'Chromosomal sex'] = np.nan

# drop irrelevant columns, this list may vary depending on the boxes ticked in MS Access while downloading the sex data     
chr_sex_data = chr_sex_data.drop(['LABNO','SEX','SIGN_BY_DATE'], axis=1).drop_duplicates().reset_index(drop=True)


# Create DECIPHER format columns using information from the variants list
for i in range(len(var_data)):    
    if len(str(var_data['HGVS-refGene'][i]).split(',')[0].split(':')) < 5:
        if var_data['HGVS-refGene'][i] == 'UNKNOWN':
            if len(str(var_data['HGVS-UCSC'][i]).split(',')[0].split(':')) < 4:
                if 'uc' in str(var_data['HGVS-UCSC'][i]).split(',')[1]:
                    var_data.loc[i,'HGVS code'] = ":".join([str(var_data['HGVS-UCSC'][i]).split(',')[0].strip(':'),str(var_data['HGVS-UCSC'][i]).split(',')[1]])
                    var_data.loc[i,'Transcript'] = str(var_data['HGVS code'][i]).split(':')[1]
                else:
                    var_data.loc[i,'HGVS code'] = np.nan
                    var_data.loc[i,'Transcript'] = np.nan
            else:
                var_data.loc[i,'HGVS code'] = str(var_data['HGVS-UCSC'][i]).split(',')[0]   
                var_data.loc[i,'Transcript'] = str(var_data['HGVS code'][i]).split(':')[1]

        else:
            if 'NM_' in str(var_data['HGVS-refGene'][i]):
                var_data.loc[i,'HGVS code'] = ":".join([str(var_data['HGVS-refGene'][i]).split(',')[0].strip(':'),str(var_data['HGVS-refGene'][i]).split(',')[1]])
                var_data.loc[i,'Transcript'] = str(var_data['HGVS code'][i]).split(':')[1]
            else:
                if len(str(var_data['HGVS-UCSC'][i]).split(',')[0].split(':')) < 4:
                    if 'uc' in str(var_data['HGVS-UCSC'][i]):
                        var_data.loc[i,'HGVS code'] = ":".join([str(var_data['HGVS-UCSC'][i]).split(',')[0].strip(':'),str(var_data['HGVS-UCSC'][i]).split(',')[1]])
                        var_data.loc[i,'Transcript'] = str(var_data['HGVS code'][i]).split(':')[1]
                    else:
                        var_data.loc[i,'HGVS code'] = np.nan
                        var_data.loc[i,'Transcript'] = np.nan
                else:
                    var_data.loc[i,'HGVS code'] = str(var_data['HGVS-UCSC'][i]).split(',')[0]
                    var_data.loc[i,'Transcript'] = str(var_data['HGVS code'][i]).split(':')[1]
    else:
        var_data.loc[i,'HGVS code'] = str(var_data['HGVS-refGene'][i]).split(',')[0]
        var_data.loc[i,'Transcript'] = str(var_data['HGVS code'][i]).split(':')[1]
        
        
for i in range(len(var_data)):        
    var_data.loc[i,'Gene name'] = var_data['GENE'][i]
    var_data.loc[i,'Internal Reference'] = "-".join(re.sub("(-[A-Z][A-Z])","",var_data.SAMPLE[i]).split('_')[0].split('-')[1:])  
    var_data.loc[i,'Internal Reference'] = "-".join(re.sub("(-[A-Z][A-Z])","",var_data.SAMPLE[i]).split('_')[0].split('-')[1:])
    var_data.loc[i,'Genome assembly'] = 'GRCh37/hg19'
    var_data.loc[i,'Intergenic'] = 'No'
    var_data.loc[i, 'Open-access consent'] = 'No'
    var_data.loc[i, 'Responsible contact'] = 'Thalia.Antoniadi@bwnft.nhs.uk'
        
# add other columns
var_data = pd.concat([var_data,pd.DataFrame(columns=['Other rearrangements/aneuploidy', 'Age at last clinical assessment', 'Prenatal age in weeks', 'Note', 'Inheritance', 'Pathogenicity', 'Phenotypes'])])

# merge the chromosomal sex df with the var_data df
merged_df = var_data.merge(chr_sex_data, how='left',on='Internal Reference')

#create genotype column
for i in range(len(merged_df)):
    if pd.isnull(merged_df.GT[i]):
        pass
    else:
        if merged_df.GT[i].split('/')[0] == merged_df.GT[i].split('/')[1]:
            if merged_df['Chromosomal sex'][i] == "46XY" and merged_df.CHROM[i] == 'chrX':
                merged_df.loc[i,'Genotype'] = 'Hemizygous'
            else:
                merged_df.loc[i,'Genotype'] = 'Homozygous'
        else:
            merged_df.loc[i,'Genotype'] = 'Heterozygous'  

final = merged_df[['Internal Reference','HGVS code','Genome assembly','Transcript','Gene name','Intergenic','Chromosomal sex','Other rearrangements/aneuploidy','Open-access consent','Age at last clinical assessment','Prenatal age in weeks','Note','Inheritance','Pathogenicity','Phenotypes','Genotype','Responsible contact']]


# write to excel
writer = pd.ExcelWriter(output_file, engine = 'xlsxwriter')
final.to_excel(writer,sheet_name='DECIPHER_formatted',index=False)
writer.save()
