# Read SVG into a list of path objects and list of dictionaries of attributes
from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc, svg2paths, wsvg
import re, csv, struct

paths, attributes = svg2paths('blueprint.svg')

d = attributes[1]['d']  # d-string from first path in SVG

# Now for some regular expressions magic
print('Start')
split_by_letters = re.findall('[A-Z|a-z][^A-Z|a-z]*', d)
waypoint = []
for x in split_by_letters:
    nums = x[1:].replace(',',' ').split()  # list of numbers after letter
    waypoint.append(nums)
print('Waypoints: ', waypoint)

with open('waypoint.csv', mode='w') as csv_file:
    fieldnames = ['x', 'y']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for k in range(len(waypoint)):
        writer.writerow({'x':waypoint[k][0],'y': waypoint[k][1]})
    
print("Done with writing")
# now let's read that file
print('Reading....')
with open('waypoint.csv', mode='r') as csv_file:
    line_count = 0
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['x'], row['y'])
        line_count += 1
    print('Processed lines:',line_count)      
print('Done')
