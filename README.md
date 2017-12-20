
# CompPyTools
Small Python scripts developed in the CompOmics group.

## Download PRIDE Project
Download PRIDE project files for a given PRIDE identifier. With the `-f` argument certain file types can be chosen for download.

*Download_PRIDE_Project.py*  
**Input:** PRIDE Archive identifier  
**Output:** Downloaded files, sorted in folders by file type  

```
usage: Download_PRIDE_Project.py [-h] [-f FILETYPES [FILETYPES ...]] projectID

Download files from PRIDE Archive for a given project.

positional arguments:
  projectID             PRIDE identifier from project to download files from

optional arguments:
  -h, --help            show this help message and exit
  -f FILETYPES [FILETYPES ...]
                        filetypes to download (msf, raw, txt, zip...)
```


## MSF and MGF to MS2PIP SpecLib
Reads an MSF file (SQLite DB), combines it with the matched (multiple) MGF files and writes a spectral library as 1 MS2PIP PEPREC and MGF file. Filters by a given FDR threshold, using q-values calculated from decoy hits or from Percolator.

*MSF_to_MS2PIP_SpecLib.py*  
**Input:** MSF and MGF files  
**Output:** Matched PEPREC and MGF file (MS2PIP spectral library)

```
usage: MSF_to_MS2PIP_SpecLib.py [-h] [-s MSF_FOLDER] [-g MGF_FOLDER]
                                [-o OUTNAME] [-f FDR_CUTOFF] [-p] [-c]

Convert Sequest MSF and MGF to MS2PIP spectral library.

optional arguments:
  -h, --help            show this help message and exit
  -s MSF_FOLDER, --msf MSF_FOLDER
                        Folder with Sequest MSF files (default: "msf")
  -g MGF_FOLDER, --mgf MGF_FOLDER
                        Folder with MGF spectrum files (default: "mgf")
  -o OUTNAME, --out OUTNAME
                        Name for output files (default: "SpecLib")
  -f FDR_CUTOFF, --fdr FDR_CUTOFF
                        FDR cut-off value to filter PSMs (default: 0.01)
  -p                    Use Percolator q-values instead of calculating them
                        from TDS (default: False)
  -c                    Combine multiple MSF files into one spectral library
                        (default: False)
```


## Split MS2PIP Spectral Library
Split MS2PIP spectral library (PEPREC and MGF file) into a train and test set.

*Split_MS2PIP_SpecLib.py*  
**Input:** PEPREC and MGF file  
**Output:** PEPREC and MGF files for both train and test data set.  

```
usage: Split_MS2PIP_SpecLib.py [-h] [-o OUT_FILENAME] [-f TEST_FRACTION]
                               peprec_file mgf_file

Split MS2PIP spectral library (PEPREC and MGF file) into a train and test set.

positional arguments:
  peprec_file       PEPREC file input
  mgf_file          MGF file input

optional arguments:
  -h, --help        show this help message and exit
  -o OUT_FILENAME   Name for output files (default: "SpecLib")
  -f TEST_FRACTION  Fraction of input to use for test data set (default: 0.1)
```
