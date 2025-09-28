
import csv
def test_report(list_tc, result):
    with open(list_tc, "r") as f_list_tc:
        list_tc = [line.strip() for line in f_list_tc]
    with open(result, "r") as f_result:
        result = [line.strip() for line in f_result]
    test_result = []
    tc_result = []
    for i, tc in enumerate(list_tc):
        if('1' == result[i]):
            tc_result = [tc, 'Pass']
        elif ('2' == result[i]):
            tc_result = [tc, 'Failed']
        elif ('3' == result[i]):
            tc_result = [tc, 'Not Run']
        else:
            tc_result = [tc, 'UnKnown']
        test_result.append(tc_result)
    with open("test_summary_report.csv", 'w', newline="") as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(["Test Case", "Result"])
        writer.writerows(test_result)
        #print(f"Report saved to {report_file}")

test_report('list_tc.txt','result.log')