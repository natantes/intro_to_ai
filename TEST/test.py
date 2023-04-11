from student_code_1 import gradient_search_1
from student_code_2 import gradient_search_2

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"
	BOLD = "\033[1m"
    
def init_board():
	return [[0 for x in range(0,10)] for x in range(0,10)]
	
	
def set_board(board, data):
	for y in range(0,10):
		for x in range(0,10):
			board[y][x]=int(data[y*10+x])

def check_result(map1, map2):
	result=True
	
	for y in range(0,10):
		v=""
		for x in range(0,10):
			if (map1[y][x]==map2[y][x]):
				v+=bcolors.GREEN+str(map1[y][x])+bcolors.NORMAL+' '
			else:
				result = False
				v+=bcolors.RED+str(map1[y][x])+bcolors.NORMAL+' '
		print(v)
	if (result):
		print("Test Result: " + bcolors.GREEN+"Passed"+bcolors.NORMAL)
	else:
		print("Test Result: " + bcolors.RED+"Failed"+bcolors.NORMAL)
	print()
	return result

tests = [("0110000000"
"0000000000"
"0000010000"
"0000000100"
"0000000001"
"0001000000"
"0000001000"
"0000100000"
"0000000010"
"1000000000"),
("1111111111"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"),
("1011111101"
"0000000010"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0100000000"
"0000000000"
"0000000000"),
]
Pass = True

for i, test in enumerate(tests):
    i += 1
    print(bcolors.NORMAL + bcolors.BOLD +"Testing Board " + str(i))
    board1 = init_board();
    solution1 = init_board();
    set_board(board1, test)

    agree = (gradient_search_1(board1) == gradient_search_2(board1))
    Pass |= agree
    if agree:
        print(bcolors.GREEN + "Test " + str(i) + " Passed")
    else:
        print(bcolors.RED + "Test " + str(i) + " Did Not Pass")
