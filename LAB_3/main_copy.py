import time
start_time = time.time()

import student_code
import copy

grade=0

puzzle=[5,2,7,0,1,4,6,8,3]
depth=23
steps=678
path=[1,1,0,3,3,2,1,2,3,0,1,1,2,3,0,3,2,1,0,0,1,2,2]

print("\n\rrunning test 1")
depth_r,steps_r,path_r=student_code.astar(puzzle)


if steps_r==steps:
	grade=grade+1
	print("number of nodes expanded passed")
else:
	print("error in number of nodes expanded expected ",steps, " but got ",steps_r)


if depth_r==depth:
	grade=grade+1
	print("depth passed")
else:
	print("error in depth")

correct=1
if len(path)==len(path_r):
	for i in range(len(path)):
		if path[i]!=path_r[i]:
			correct=0
	if correct==1:
		grade=grade+1
		print("path is correct")
	else:
		print("error in path, expected ",path)
		print("got ",path_r)
else:
	print("error in path size",len(path),len(path_r))
	print("error in path, expected ",path)
	print("got                     ",path_r)
	
	
	

print("\n\n\n\n----------------------------")
print("your program has passed ",grade," out of 21 tests")

print("--- %s seconds ---" % (time.time() - start_time))

