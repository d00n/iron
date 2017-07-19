import csv
import requests
 
with open('sample.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for line in reader:
        saveas = '-'.join([line[0], line[1].replace('/', '-'), line[2].replace('/', '-'), line[3]])
        # Reorganize to rename the output filename.
        url = 'https://www.sec.gov/Archives/' + line[4].strip()
        with open(saveas, 'wb') as f:
            f.write(requests.get('%s' % url).content)
            print(url, 'downloaded and wrote to text file')
