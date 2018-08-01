import re
import csv

data = '<path id="58" d="M 457984.36 7575754.89 L 468060.3 7580832.86 L 520309.28 7583741.78 L 553166.03 7596446.73 L 555605.05 7594867.37 L 561992.47 7597226.43 z" />'
all_coords = re.findall('id="([0-9]{1,4})" d="((?:[ML] [0-9]{6,8}\.[0-9]{1,2} [0-9]{6,8}\.[0-9]{1,2}).+?)\s."', data)
#file = open('blueprint.svg','r')
#data = file.read()
print ("Data = ", data)
# all_coords = re.findall('([0-9]{1,8}\.[1-9]{1,2})',data)
print ("Raw = ", all_coords)
coordDict = dict(all_coords)
print("Dict = ", coordDict)

#with open('test.csv', 'wb') as f:
#    csv.writer(f).writerows((k, v) for k, v in coordDict.items())

with open('test.csv','w') as data:
    data.write(str(coordDict))

print("Done")
