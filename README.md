# Variant-list-to-DECIPHER-transform
Creating an Excel spreadsheet that conforms to the DECIPHER bulk variant upload format

## Overview
### Requirements

1. **The Rare Diseases Variants list**, a live list which gets amended regularly. The columns in this list that are used to populate the DECIPHER-formatted list are as follows:

  *	**HGVS-refGene** or **HGVS-UCSC**  for information that populates the Transcript and HGVS code columns
  *	**GENE** for information that populates the Gene name column
  *	**SAMPLE** for information that populates the Internal Reference column
  
2. **Lab Numbers and Sex List(s)** obtained from Shire following the steps detailed in SOP BI 01.01.16. The main columns that are required are as follows:

  * **LABNO** for patient lab numbers
  * **SEX** for information indicating the sex of the patient

3. A \*nix operating system. This script was written and tested on a CentOS 7 operating system
4. Python2.7
  
### Usage
1. Download the GitHub repository:
```bash
git clone https://github.com/WMRGL/Variant-list-to-DECIPHER-transform.git
```
2. Create a virtual environment:
```bash
virtualenv -p python2.7 <venv_name>
```
3. Activate the virtual environment:
```bash
source <venv_name>/bin/activate
```
4. Update pip and install requirements:
```bash
pip install -U pip
pip install -r requirements.txt
```
5. Download sex data from Shire for all TSO patients as instructed in SOP BI 01.01.16.
6. Open the *transform_variant_list_to_decipher_format.py* file and change the paths to the variant list (var_list), patient sex data (chr_sex), and the file to which you would like to write the output (output_file). These are in lines 10-12 of the file. 
7. Run the script as follows:
```bash
python2.7 transform_variant_list_to_decipher_format.py
```
8. Deactivate the virtual environment when the script is don processing the data:
```bash
deactivate
```

### Expected Output
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

