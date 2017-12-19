def run():
    import os
    import json
    import requests
    import argparse
    import pandas as pd

    parser = argparse.ArgumentParser(description='Download files from PRIDE Archive for a given project.')
    parser.add_argument('projectID', action='store',
                        help='PRIDE identifier from project to download files from')
    parser.add_argument('-f', dest='filetypes', action='store', nargs='+',
                        help='filetypes to download (msf, raw, txt, zip...)')
    args = parser.parse_args()

    get_meta_url = "https://www.ebi.ac.uk:443/pride/ws/archive/project"
    get_files_url = "https://www.ebi.ac.uk:443/pride/ws/archive/file/list/project"

    # Make folder for project and download meta data
    print("Downloading meta data...")
    os.system("mkdir '{}'".format(args.projectID))
    url = "{}/{}".format(get_meta_url, args.projectID)
    response = json.loads(requests.get(url).content.decode('utf-8'))
    with open("{}/PRIDE_Meta_data.json".format(args.projectID),"w") as f:
        f.write(json.dumps(response))
    with open("{}/PRIDE_Meta_data.txt".format(args.projectID),"w") as f:
        f.write(response['accession'] + '\n')
        f.write(response['publicationDate'] + '\n')
        f.write(response['title'] + '\n')
        f.write(response['references'][0]['desc'] + '\n')
        for i, item in enumerate(response['references'][0]['ids']):
            f.write(item + '\n')

    # Get dataframe with file info through PRIDE Archive REST API
    print("Getting list of files...")
    url = "{}/{}".format(get_files_url, args.projectID)
    response = pd.DataFrame(json.loads(requests.get(url).content.decode('utf-8'))['list'])
    response['fileExtension'] = response['fileName'].str.split('.').apply(lambda x: x[-1])
    
    # Set extensions
    extensions = response['fileExtension'].unique()
    print("Found files with extensions: {}".format(extensions))
    if args.filetypes:
        extensions = args.filetypes
    print("Downloading files with extensions: {}".format(extensions))

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