import student_code_1
import student_code_2

tests = []
Pass = True

for i, test in enumerate(tests):
    i += 1
    current = function1(test) == function2(test)
    Pass |= current
    if current:
        print("Test " + str(i) + " Passed")

if Pass:
    print("All tests passed")