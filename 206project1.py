import os
import csv
import filecmp

## Referenced code from SI 106 textbook 'Programs, Information, and People' by Paul Resnick to complete this project

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.
#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	data_file = open(file, "r")
	new_file = csv.reader(data_file)
	final = []
	for row in new_file:
		d = {}
		d['First'] = row[0]
		d['Last'] = row[1]
		d['Email'] = row[2]
		d['Class'] = row[3]
		d['DOB'] = row[4]
		final.append(d)
	#print (final[1:])
	return final[1:]

		



#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	x = sorted(data, key = lambda x: x[col])
	return str(x[0]['First'])+ " " + str(x[0]['Last'])
	

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	#data = [{'first:keely, last: meyers, class: junior, dob: 5/18/97'}]
	dd = dict()
	for s in data:
		if s['Class'] == 'Freshman':
			if 'Freshman' not in dd:
				dd['Freshman'] = 1
			else:
				dd['Freshman'] += 1
		elif s['Class'] == 'Sophomore':
			if 'Sophomore' not in dd:
				dd['Sophomore'] = 1
			else:
				dd['Sophomore'] += 1
		elif s['Class'] == 'Junior':
			if 'Junior' not in dd:
				dd['Junior'] = 1
			else:
				dd['Junior'] += 1
		elif s['Class'] == 'Senior':
			if 'Senior' not in dd:
				dd['Senior'] = 1
			else: 
				dd['Senior'] += 1
	class_count = list(dd.items())
	new_class_count = sorted(class_count, key = lambda x: x[1], reverse = True)
	return new_class_count




# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	bday_dict = {}
	for names in a:
		n_bday = names['DOB'].strip()
		new_bday = n_bday[:-5]
		#print (new_bday)
		if new_bday[1] == '/':
			day = new_bday[2:]
		elif new_bday[2] == '/':
			day = new_bday[3:]
		bday_dict[names['First']] = day
	#print (bday_dict)
	day_counts = {}
	for birthday in bday_dict:
		if bday_dict[birthday] in day_counts:
			day_counts[bday_dict[birthday]] += 1
		else:
			day_counts[bday_dict[birthday]] = 1
	#print(day_counts)
	sorted_birthdays = sorted(day_counts.items(), key = lambda x: x[1], reverse = True)
	return int(sorted_birthdays[0][0])

# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	
	#Your code here:
	ages = []
	count = 0
	for item in a:
		year = item['DOB'][-4:]
		age = (2017 - int(year))
		ages.append(age)
		count += 1
	avg_age = round(sum(ages)/count)
	#print (avg_age)
	return avg_age

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	outfile = open(fileName, "w")
	x = sorted(a, key = lambda x: x[col])
	#print (x)
	#note: x is sorted correctly.
	for s in x:
		outfile.write("{},{},{}\n".format(s['First'], s['Last'], s['Email']))
	outfile.close()
	


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
	main()

