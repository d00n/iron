import csv
import requests
import os.path
 
with open('comps.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    i = 0
    for line in reader:
        i += 1
        print ('i: ', i)
        saveas = '-'.join([line[0], line[1].replace('/', '-'), line[2].replace('/', '-'), line[3]]) + '.txt'
        # Reorganize to rename the output filename.
        url = 'https://www.sec.gov/Archives/' + line[4].strip()
        if not os.path.isfile(saveas):
            with open(saveas, 'wb') as f:
                f.write(requests.get('%s' % url).content)
                print(url, 'downloaded and wrote to text file')
        else:
            print('skipping: ',  saveas)
