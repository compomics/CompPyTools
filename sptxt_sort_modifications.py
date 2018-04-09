"""
## Sort modifications in .sptxt spectral library
Sort modifications properly in a SpectraST .sptxt spectral library file.

After parsing an MSP spectral library file through SpectraST to convert it to
an .sptxt file, other software tools (Deliberator) threw an error: `molecule
{15.99}({57.02}` not found. The modifications were not sorted by location in
the sequence...

This script parses the .sptxt file and writes a new file with the modifications
sorted properly. For instance, `Mods=2/12,M,Oxidation/5,C,Carbamidomethyl`
becomes `Mods=2/5,C,Carbamidomethyl/12,M,Oxidation`.

The `tqdm` libarary is used to display progress.

*sptxt_sort_modifications.py*
**Input:** .sptxt spectral library
**Output:** .sptxt spectral library with modifications sorted properly

```
usage: sptxt_sort_modifications.py [-h] input_file

Sort modifications properly in a SpectraST .sptxt spectral library file.

positional arguments:
  input_file  Input .sptxt file

optional arguments:
  -h, --help  show this help message and exit
```
"""


# Native libraries
import re
import argparse

# Third party libraries
from tqdm import tqdm


def ArgParse():
    parser = argparse.ArgumentParser(description='Sort modifications properly in a SpectraST .sptxt spectral library file.')
    parser.add_argument('input_file', action='store',
                        help='Input .sptxt file')
    args = parser.parse_args()
    return(args)


def main():
    args = ArgParse()
    output_file = '{}_SortedMods.sptxt'.format(args.input_file.split('.')[0])
    print("Writing spectral library with sorted modifications to {}".format(output_file))
    with open(output_file, mode='xt') as speclib_out:
        with open(args.input_file, mode='rt') as speclib_in:
            for line in tqdm(speclib_in):
                if line[0] == 'C':
                    if line[0:9] == 'Comment: ':
                        mods_original = re.search('Mods=.*? ', line).group(0)
                        mods = mods_original.strip()[5:].split('/')
                        if mods[0] != '0':
                            mods_n = '/'.join(sorted(mods[1:], key=lambda x: int(x.split(',')[0])))
                            line = line.replace(mods_original, "Mods={}/{} ".format(mods[0], mods_n))
                speclib_out.write(line)
    print("Ready!")


if __name__ == '__main__':
    main()
