print("****************")
print("New test score\n")
print("9 test scores\n")
print (25 * "=")
print(25 * "=")
#
test_1 = int(input("enter test score\t\t\t"))
test_2 = int(input("enter test score\t\t\t"))
test_3 = int(input("enter test score\t\t\t"))
test_4 = int(input("enter test score\t\t\t"))
test_5 = int(input("enter test score\t\t\t"))
test_6 = int(input("enter test score\t\t\t"))
test_7 = int(input("enter test score\t\t\t"))
test_8 = int(input("enter test score\t\t\t"))
test_9 = int(input("enter test score\t\t\t"))
total_score=(test_1 + test_2 + test_3 + test_4 + test_5 + test_6 + test_7 + test_8 + test_9)
average_score = total_score / 9
print(25 * "=")

letter_grade="\n"
if average_score >=90:
   letter_grade  = "A\n"
elif average_score >=80:
   letter_grade ="B\n"
elif average_score >=60:
   letter_grade ="C\n"
elif average_score >=40:
   letter_grade ="D\n"
elif average_score  < 40:
   letter_grade = "F\n"

print(25*"=")
#
print("totalscore\t\t\t{}".format(total_score))
print("\naverage test score\t\t\t\n{}".format(average_score))
print(25 * "=")
print("\n" +letter_grade)
