
# CompPyTools
Small Python scripts developed in the CompOmics group.

## MSF and MGF to MS2PIP SpecLib
Reads an MSF file (SQLite DB), combines it with the matched (multiple) MGF files and writes a spectral library as 1 MS2PIP PEPREC and MGF file. Filters by a given FDR threshold, using q-values calculated from decoy hits or 
from Percolator.

```
usage: MSF_to_MS2PIP_SpecLib.py [-h] [-s MSF_FOLDER] [-g MGF_FOLDER]
                                [-o OUTNAME] [-f FDR_CUTOFF] [-p]

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
```

## Download PRIDE Project
Download PRIDE project files for a given PRIDE identifier.

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
