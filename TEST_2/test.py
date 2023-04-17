import common
from student_code_1 import df_search_1
from student_code_2 import df_search_2
from student_code_1 import bf_search_1
from student_code_2 import bf_search_2

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"
	BOLD = "\033[1m"

tests = [("2000000000"
"0101111111"
"0100000000"
"0101111111"
"0101000001"
"0101010110"
"0101010000"
"0100011110"
"0011111110"
"1011111110"
"1011111111"
"1000000003"),
("2000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000003"),
("2000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0030000000"
"0000000000"),
("2000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"1111111110"
"0000000000"
"0000000000"
"0000000000"
"0030000000"
"0000000000"),
("2000000000"
"0000000000"
"0000000000"
"0111111111"
"0010000000"
"0000001000"
"1111111110"
"0000000000"
"0000000000"
"0000000000"
"0030000000"
"0000000000"),
("2000000000"
"1111111110"
"0000000000"
"0111111111"
"0010000000"
"0000001000"
"0111111111"
"0011111111"
"0000000001"
"1111111101"
"0031111100"
"0000000000"),
("2100000000"
"1100000000"
"0000000000"
"0000000000"
"0000000000"
"0000000000"
"1111111110"
"0000000000"
"0000000000"
"0000000000"
"0030000000"
"0000000000"),
			  ]
Pass = True

for i, test in enumerate(tests):
    agree = True
    i += 1
    print(bcolors.NORMAL + bcolors.BOLD +"Testing Board " + str(i))

    dfmap1 = common.init_map()
    common.set_map(dfmap1, test)
    dfmap2 = common.init_map()
    common.set_map(dfmap2, test)
    bfmap1 = common.init_map()
    common.set_map(bfmap1, test)
    bfmap2 = common.init_map()
    common.set_map(bfmap2, test)

    df1 = df_search_1(dfmap1)
    df2 = df_search_2(dfmap2)
    bf1 = bf_search_1(bfmap1)
    bf2 = bf_search_2(bfmap2)

    agree |= (dfmap1 == dfmap2)
    agree |= (bfmap1 == bfmap2)
    Pass |= agree
    if agree:
        print(bcolors.GREEN + "Test " + str(i) + " Passed")
    else:
        print(bcolors.RED + "Test " + str(i) + " Did Not Pass")
