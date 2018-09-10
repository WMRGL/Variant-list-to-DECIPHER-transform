# Variant-list-to-DECIPHER-transform
Creating an Excel spreadsheet that conforms to the DECIPHER bulk variant upload format

## Overview
This script is to be used as detailed in SOP BI 01.01.16.


## Usage

## Expected Output
Output will be in the form of an Excel spread sheet with the followong columns (in order and with examples):

a.	*Internal reference number or ID* (Lab ID)
b.	*HGVS code* (NM_001159673.1:c.1224_1225insC)
c.	*Genome assembly* (GRCh37/hg19)
d.	Transcript (NM_001159673.1)
e.	Gene name (SYNCRIP)
f.	*Intergenic* (No)
g.	*Chromosomal sex* (46XX)
h.	Other rearrangements/aneuploidy
i.	Open-access consent
j.	Age at last clinical assessment
k.	Prenatal age in weeks
l.	Note
m.	Inheritance
n.	Pathogenicity
o.	Phenotypes
p.	*Genotype* (Heterozygous)
q.	Responsible contact (email address of responsible individual)

*All columns in bold are mandatory*. Other fields are non-mandatory and do not need to be in the file; if not deemed necessary for submission, they should be left blank. All fields will be validated after upload and before submission to DECIPHER.

