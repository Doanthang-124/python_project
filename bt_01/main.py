
def test_report(list_tc, result):
    with open(list_tc, "r") as f_list_tc:
        list_tc = [line.strip() for line in f_list_tc]
    with open(result, "r") as f_result:
        result = [line.strip() for line in f_result]
    for i, tc in enumerate(list_tc):
        if('1' == result[i]):
            print("{t} pass".format(t=tc))
        elif ('2' == result[i]):
            print("{t} fail".format(t=tc))
        elif ('3' == result[i]):
            print("{t} not run".format(t=tc))
        else:
            print("{t} unknown".format(t=tc))

test_report('list_tc.txt','result.log')

""" f_list_tc = open('list_tc.txt', mode='r+')
f_result = open('result.log', mode='r')

list_tc = list(f_list_tc.readlines())
result = list(f_result.readlines())

def test_report():
    for i in range(len(list_tc)):
        if('1\n' == result[i]):
            print("Test case {t} pass".format(t=list_tc[i]))
        if('2\n' == result[i]):
            print("Test case {t} fail".format(t=list_tc[i]))
        if('3' == result[i]):
            print("Test case {t} not run".format(t=list_tc[i]))
test_report()
f_list_tc.close()
f_result.close() """