import re

file  = open("output.txt", "r")
file1 = open("final.txt","w")

regex = "([a-zA-Z]+) ([0-9]+)"
regex2 = "\[[a-zA-Z]+\]([a-zA-Z0-9-]+)\s- ([a-zA-Z]+\s)- ([a-zA-Z0-9]+)\s- (.*)"

while True:
	line = file.readline()
	if not line:
		break
	match = re.match(regex, line)
	count = int(match.group(2))
	annot = match.group(1)
	dict = {}
	for i in range(count):
		line = file.readline()
		if not line:
			break
		match1 = re.match(regex2, line)
		code = match1.group(1)
		operation = match1.group(2)
		project = match1.group(3)
		description = match1.group(4)
		if project in dict:
			dict2 = dict[project]
			if code in dict2:
				value = dict2[code]
				value.append(description)
				dict2[code] = value
			else:
				dict2[code] = [description]
		else:
			dict2 = {}
			dict2[code] = [description]
			dict[project] = dict2
	file1.write(annot + ":\n")
	for i in dict.keys():
		file1.write("\tProject: "+ i + ":\n")
		for j in dict[i].keys():
			file1.write("\t\tCode: " + j + "\n")
			lst = dict[i][j]
			count = 1
			for value in lst:
				if value.find(' - ') != -1 :
					lst = value.split(' - ')
					for l in lst:
						file1.write("\t\t\t" + str(count) +  ". " + l + ".\n")
						count = count + 1
				else:
					file1.write("\t\t\t" + str(count) +  ". " + value + ".\n")
					count = count + 1	
file.close()
file1.close()
				
