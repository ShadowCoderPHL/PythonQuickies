import re
import sys

with open('to-read/videos.txt') as f:
    lines = [line.rstrip() for line in f]
f.closed

try:
  get_title = sys.argv[1]
except:
  print("Error: Title requred as first argument")
  exit()

to_write = ''

for i in lines:
	if i == '' :
		to_write += '\n'
	elif re.match("(?:[01]\d|2[0123]):(?:[012345]\d):(?:[012345]\d)", i) :
		to_write += ''
	elif re.match("(\d+-\d+-\d+)", i) :
		to_write += i
	else:
		str = i.replace(" ", "_")
		to_write += get_title + '_' + str + '-'
		
print(to_write, end = '\n -------------------------------')	

#Append
fw = open("to-write/videos.txt", "a")
fw.write(to_write)
fw.close()