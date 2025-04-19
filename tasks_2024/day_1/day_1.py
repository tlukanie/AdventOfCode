# FIRST PART

# pseudo code
# put first column into array
	# sort
# put second column into array
	# sort
# iterate over each of them
# compare sorted in an increasing order values 
# increment distance

from re import T


first_column = []
second_column = []

with open("input.txt") as catalogue:
	for line in catalogue:
		column = line.split()
		fst = int(column[0])
		scnd = int(column[1])
		first_column.append(fst)
		second_column.append(scnd)

print(column)
first_column.sort()
second_column.sort()

distance = 0
d_help  = 0

for el, scnd_el in zip(first_column, second_column):
	#print(el, scnd_el)
	d_help = abs(el - scnd_el)
	#print(d_help)
	distance += d_help
	
	
#print(second_column)

print(distance)
#answer 1722302

# SECOND PART

# Test implementation
#iterate over first column (outter loop)
#iterate over second column (inner loop)
test_column_one = [3,4,2,1,3,3]
test_column_two = [4,3,5,3,9,3]

counter = 0
similarity_score = 0
total_similarity_score = 0


print(test_column_one)
for a in test_column_one:
	for b in test_column_two:
			#print(a, b)
			if a == b:
				counter += 1
				#print(counter)
	similarity_score = a * counter
	#print(f"Similarity score: {similarity_score}")
	counter = 0
	total_similarity_score += similarity_score
print(f"Total similarity score: {total_similarity_score}")



counter_pt = 0
sim_score_pt = 0
total_sim_score_pt = 0
# Implementation of the second Part
for x in first_column:
	for y in second_column:
		if x == y:
			counter_pt += 1
	sim_score_pt = x * counter_pt
	counter_pt = 0
	total_sim_score_pt += sim_score_pt
print(f"Total similarity score for the Second Part: {total_sim_score_pt}")
#answer 20373490

