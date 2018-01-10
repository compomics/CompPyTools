"""
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
"""

# --------------
# Import modules
# --------------
import os
import json
import requests
import argparse
import pandas as pd


def ArgParse():
    parser = argparse.ArgumentParser(description='Download files from PRIDE Archive for a given project.')
    parser.add_argument('projectID', action='store',
                        help='PRIDE identifier from project to download files from')
    parser.add_argument('-f', dest='filetypes', action='store', nargs='+',
                        help='filetypes to download (msf, raw, txt, zip...)')
    args = parser.parse_args()
    return(args)


def run():
    args = ArgParse()
    get_meta_url = "https://www.ebi.ac.uk:443/pride/ws/archive/project"
    get_files_url = "https://www.ebi.ac.uk:443/pride/ws/archive/file/list/project"

    # Make folder for project and download meta data
    print("Downloading meta data...")
    os.system("mkdir '{}'".format(args.projectID))
    url = "{}/{}".format(get_meta_url, args.projectID)
    response = json.loads(requests.get(url).content.decode('utf-8'))
    with open("{}/PRIDE_Meta_data.json".format(args.projectID), "w") as f:
        f.write(json.dumps(response))
    with open("{}/PRIDE_Meta_data.txt".format(args.projectID), "w") as f:
        f.write('{}\n'.format(response['accession']))
        f.write('{}\n'.format(response['publicationDate']))
        f.write('{}\n'.format(response['title']))
        try:
            f.write('{}\n'.format(response['references'][0]['desc']))
            for i, item in enumerate(response['references'][0]['ids']):
                f.write(item + '\n')
        except IndexError:
            pass

    # Get dataframe with file info through PRIDE Archive REST API
    url = "{}/{}".format(get_files_url, args.projectID)
    response = pd.DataFrame(json.loads(requests.get(url).content.decode('utf-8'))['list'])
    response['fileExtension'] = response['fileName'].str.split('.').apply(lambda x: x[-1])

    # Set extensions
    extensions = response['fileExtension'].unique()
    print("Found files with extensions: \t\t{}".format(extensions))
    if args.filetypes:
        extensions = args.filetypes
    print("Downloading files with extensions: \t{}".format(extensions))

    # Download files
    print("Downloading files...")
    for ext in extensions:
        os.system("mkdir '{}/{}'".format(args.projectID, ext))
        count = 0
        total = len(response[response['fileExtension'] == ext])
        for _, row in response[response['fileExtension'] == ext].iterrows():
            count += 1
            if count % 10 == 0 or count == 1:
                print("{} {}/{}".format(ext, count, total))
            os.system("wget -O '{}/{}/{}' '{}' -q --show-progress".format(args.projectID, ext, row['fileName'], row['downloadLink']))


if __name__ == '__main__':
    run()
