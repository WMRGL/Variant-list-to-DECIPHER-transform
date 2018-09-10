# Variant-list-to-DECIPHER-transform
Creating an Excel spreadsheet that conforms to the DECIPHER bulk variant upload format

## Overview
This script is to be used as detailed in SOP BI 01.01.16.


## Usage

## Expected Output
Output will be in the form of an Excel spread sheet with the followong columns (in order and with examples):

1.	**Internal reference number or ID** (Lab ID)
2.	**HGVS code** (NM_001159673.1:c.1224_1225insC)
3.	**Genome assembly** (GRCh37/hg19)
4.	Transcript (NM_001159673.1)
5.	Gene name (SYNCRIP)
6.	**Intergenic** (No)
7.	**Chromosomal sex** (46XX)
8.	Other rearrangements/aneuploidy
9.	Open-access consent
10.	Age at last clinical assessment
11.	Prenatal age in weeks
12.	Note
13.	Inheritance
14.	Pathogenicity
15.	Phenotypes
16.	**Genotype** (Heterozygous)
17.	Responsible contact (email address of responsible individual)

**All columns in bold are mandatory**. Other fields are non-mandatory and do not need to be in the file; if not deemed necessary for submission, they should be left blank. All fields will be validated after upload and before submission to DECIPHER.

