from re import T

# PSEUDO CODE
# count elements in line
# iterate over each element and compare that they are increasing/decreasing
# iterate over each element and compare adjusent difference (max 3, min 1)
# update safe counter on each step
# increment safe_reports number if counter meats the requirements if safety_counter == 3
# reset safety_counter

rows = []
line_length = 0
safety_counter = 0
red_flag = False
abs_dif = 0
safe_report = 0

#split into functions

#def safety_counter(line_length, rows, red_flag):
	


with open("input.txt") as f:
	for line in f:
		rows = line.split()
		#print(rows)
		line_length = len(rows)
		#print(line_length)
		red_flag = False
		for i in range(line_length - 1):
			abs_dif = abs(int(rows[i]) - int(rows[i + 1]))
			if (int(rows[i]) < int(rows[i + 1]) and (abs_dif <= 3) and (abs_dif > 0)):
				print("ok")
			else:
				red_flag = True
				break
		if (red_flag == False):
			safety_counter = 1
			safe_report += 1
		else:
			safety_counter = 0
		print(safety_counter)


with open("input.txt") as f:
	for line in f:
		rows = line.split()
		print(rows)
		line_length = len(rows)
		print(line_length)
		red_flag = False
		for i in range(line_length - 1):
			abs_dif = abs(int(rows[i]) - int(rows[i + 1]))
			if (int(rows[i]) > int(rows[i + 1]) and (abs_dif <= 3) and (abs_dif > 0)):
				print("ok")
			else:
				red_flag = True
				break
		if (red_flag == False):
			safety_counter = 1
			safe_report += 1
		else:
			safety_counter = 0
		print(safety_counter)


print(f"Safe report: {safe_report}")
# answer: 502








# safety_counter = 0
# safety_counter_2 = 0
# safety_helper = 0
# safety_helper_2 = 0
# safety_helper_dcrs = 0
# safety_helper_dcrs_2 = 0
# safe_reports = 0
# analyze_levels = []
# i = 0
# red_flag = False
# red_flag_2 = False

# with open("input_test.txt") as catalogue:
# 	for line in catalogue:
# 		analyze_levels = line.split()
# 		print(analyze_levels)
# 		for i in range(len(analyze_levels) - 1):
# 			if (int(analyze_levels[i]) < int(analyze_levels[i + 1])):
# 				if safety_helper_dcrs > 0:
# 					safety_helper_dcrs = 0
# 				safety_helper += 1
# 				if (safety_helper == len(analyze_levels) - 1):
# 					safety_counter += 1
# 					safety_helper = 0
# 					for i in range(len(analyze_levels) - 1):
# 						#print(abs(int(analyze_levels[i]) - int(analyze_levels[i + 1])))
# 						if (abs(int(analyze_levels[i]) - int(analyze_levels[i + 1])) > 3
# 		  					or (abs(int(analyze_levels[i]) - int(analyze_levels[i + 1])) == 0)):
# 							print("OH NOOO")
# 							red_flag = True
# 							break
# 						else:
# 							safety_helper_2 += 1
# 							#print(f"Safety helper 2: {safety_helper_2}")
# 					if (safety_helper_2 == len(analyze_levels) - 1 and (red_flag == False)):
# 						safety_counter += 1
# 					safety_helper_2 = 0
# 				#print(f"Safety counter: {safety_counter}")
# 				if (safety_counter == 2 and red_flag == False):
# 					safe_reports += 1
# 				safety_counter = 0
# 			elif (int(analyze_levels[i]) > int(analyze_levels[i + 1])):
# 				if safety_helper > 0:
# 					safety_helper = 0
# 				safety_helper_dcrs += 1
# 				if (safety_helper_dcrs == len(analyze_levels) - 1):
# 					safety_counter_2 += 1
# 					safety_helper_dcrs = 0
# 					for i in range(len(analyze_levels) - 1):
# 						#print(abs(int(analyze_levels[i]) - int(analyze_levels[i + 1])))
# 						if (abs(int(analyze_levels[i]) - int(analyze_levels[i + 1])) > 3
# 		  					or (abs(int(analyze_levels[i]) - int(analyze_levels[i + 1])) == 0)):
# 							print("OH NOOO")
# 							red_flag_2 = True
# 							break
# 						else:
# 							safety_helper_dcrs += 1
# 							#print(f"Safety helper 2: {safety_helper_dcrs}")
# 					if ((safety_helper_dcrs == len(analyze_levels) - 1) and (red_flag == False)):
# 						safety_counter_2 += 1
# 					safety_helper_dcrs = 0
# 				#print(f"Safety counter: {safety_counter_2}")
# 				if (safety_counter_2 == 2 and red_flag_2 == False):
# 					safe_reports += 1
# 				safety_counter_2 = 0
# 		#print(f"SAFE REPORTS: {safe_reports}")
# 		print(f"SAFE REPORTS: {safe_reports}")

# print(f"SAFE REPORTS: {safe_reports}")


	

