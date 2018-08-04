# Read SVG into a list of path objects and list of dictionaries of attributes
from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc, svg2paths, wsvg
import re, csv

paths, attributes = svg2paths('blueprint.svg')

d = attributes[1]['d']  # d-string from first path in SVG

# Now for some regular expressions magic
import re
split_by_letters = re.findall('[A-Z|a-z][^A-Z|a-z]*', d)
data = []
waypoint = []
for x in split_by_letters:
    nums = x[1:].replace(',',' ').split()  # list of numbers after letter
    for k in range(len(nums) // 2):
        data.append([x[0]] +  [nums[k]] + [nums[k+1]])
        if x[0] == 'M':
            print(x[0])
            print (nums[k],nums[k+1])
            waypoint.append('M')
            waypoint.append(nums[k])
            waypoint.append(nums[k+1])
            waypoint.append('L')
            print ('L')
        if x[0] == 'L':
            print (nums[k],nums[k+1])
            waypoint.append(nums[k])
            waypoint.append(nums[k+1])


file = open('waypoint.csv','w')   # write the waypoints to a file
file.write(str(waypoint))
file.close()
print("Done")
