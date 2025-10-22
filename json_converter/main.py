import json
import csv

with open('input.json','r') as file:
    data= json.load(file)

with open('output.csv','w', newline='') as output:
    filednames= set()
    for item in data:
        filednames.update(item.keys())
    
    writer= csv.DictWriter(output, fieldnames=sorted(filednames))
    writer.writeheader()
    writer.writerows(data)