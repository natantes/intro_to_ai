import student_code
import statistics
import random
import time
import math

n = 0

# get the start time
st = time.time()


start_array = [1, 3, 2, 8, 9, 11, 100, 4]
final_array = [1, 2, 3, 4, 8, 9, 11, 100]
start_stats = [0, 0, 0]
final_stats = [17, 4, 1]

print("\n\rrunning test 1")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

tests_passed=0
if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
n += 3


start_array = [1, 3, 2, 8, 9, 11, 100, 4, -10]
final_array = [-10, 1, 2, 3, 4, 8, 9, 11, 100]
start_stats = [0, 0, 0]
final_stats = [14, 4, -10]

print("\n\rrunning test 2")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
n += 3


start_array = [1]
final_array = [1]
start_stats = [0, 0, 0]
final_stats = [1, 1, 1]

print("\n\rrunning test 3")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
n += 3



start_array = [1000, 0, -1000, -1000]
final_array = [-1000, -1000, 0, 1000]
start_stats = [0, 0, 0]
final_stats = [-250, -1000, -1000]

print("\n\rrunning test 4")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
n += 3




start_array = [1, 17, -3, -105, 0, 0, 586, 103, 18, 22, 198, -999, 901]
final_array = [-999, -105, -3, 0, 0, 1, 17, 18, 22, 103, 198, 586, 901]
start_stats = [0, 0, 0]
final_stats = [56, 17, 0]

print("\n\rrunning test 5")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
n += 3



start_array = [0,0,0,1,1,1]
final_array = [0,0,0,1,1,1]
start_stats = [0, 0, 0]
final_stats = [0, 0, 0]

print("\n\rrunning test 6")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
n += 3






start_array = [2,1,0,1,0]
final_array = [0, 0, 1, 1, 2]
start_stats = [0, 0, 0]
final_stats = [0, 1, 0]

print("\n\rrunning test 7")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
n += 3



start_array = [2,1,0,1,0]
final_array = [0, 0, 1, 1, 2]
start_stats = [0, 0, 0]
final_stats = [0, 1, 0]

print("\n\rrunning test 7")
print("input data",start_array)
student_code.order(start_array,start_stats)
print("student sorted data",start_array)
print("expected data", final_array)
print("student stats",start_stats)
print("expected stats", final_stats)
grade=2

if len(start_array)==len(final_array):
	tests_passed=tests_passed+1
	print("size test passed")
	grade=1
	for x in range(len(start_array)):
		if start_array[x]!=final_array[x]:
			grade=0
	if grade==1:
		print("sorted array passed")
		tests_passed=tests_passed+1
	else:
		print("sorted array failed")
	grade=1
	for x in range(len(start_stats)):
		if start_stats[x]!=final_stats[x]:
			grade=0
	if grade==1:
		print("stats passed")
		tests_passed=tests_passed+1
	else:
		print("stats failed")
else:
	print("size test failed")
n += 3



for i in range(50):
	start_array = [random.randrange(0, 1000) - 1000 for i in range(1000)]
	final_array = sorted(start_array)
	start_stats = [0, 0, 0]
	final_stats = [math.floor(statistics.mean(start_array)), 0 , statistics.multimode(final_array)[0]]
	final_stats[1] = final_array[len(final_array) // 2 - 1] if len(final_array) % 2 == 0 else final_array[len(final_array) // 2]

	print("\n\rrunning test 7 LOOK: " + str(statistics.mean(start_array)) + " " + str(math.floor(statistics.mean(start_array))))
	print("input data",start_array)
	student_code.order(start_array,start_stats)
	print("student sorted data",start_array)
	print("expected data", final_array)
	print("student stats",start_stats)
	print("expected stats", final_stats)
	grade=2

	if len(start_array)==len(final_array):
		tests_passed=tests_passed+1
		print("size test passed")
		grade=1
		for x in range(len(start_array)):
			if start_array[x]!=final_array[x]:
				grade=0
		if grade==1:
			print("sorted array passed")
			tests_passed=tests_passed+1
		else:
			print("sorted array failed")
		grade=1
		for x in range(len(start_stats)):
			if start_stats[x]!=final_stats[x]:
				grade=0
		if grade==1:
			print("stats passed")
			tests_passed=tests_passed+1
		else:
			print("stats failed")
	else:
		print("size test failed")
	
	n += 3

for i in range(50):
	start_array = [random.randrange(0, 2000) - 1000 for i in range(1000)]
	final_array = sorted(start_array)
	start_stats = [0, 0, 0]
	final_stats = [math.floor(statistics.mean(start_array)), 0 , statistics.multimode(final_array)[0]]
	final_stats[1] = final_array[len(final_array) // 2 - 1] if len(final_array) % 2 == 0 else final_array[len(final_array) // 2]

	print("\n\rrunning test")
	print("input data",start_array)
	student_code.order(start_array,start_stats)
	print("student sorted data",start_array)
	print("expected data", final_array)
	print("student stats",start_stats)
	print("expected stats", final_stats)
	grade=2

	if len(start_array)==len(final_array):
		tests_passed=tests_passed+1
		print("size test passed")
		grade=1
		for x in range(len(start_array)):
			if start_array[x]!=final_array[x]:
				grade=0
		if grade==1:
			print("sorted array passed")
			tests_passed=tests_passed+1
		else:
			print("sorted array failed")
		grade=1
		for x in range(len(start_stats)):
			if start_stats[x]!=final_stats[x]:
				grade=0
		if grade==1:
			print("stats passed")
			tests_passed=tests_passed+1
		else:
			print("stats failed")
	else:
		print("size test failed")
	
	print(statistics.multimode(final_array))
	n += 3

### blah blah 

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st

print("\n\n\n\n----------------------------")
print('Execution time:', elapsed_time, 'seconds')
print("your program has passed ",tests_passed," out of " + str(n) + " tests")