import matplotlib.pyplot as plt

aboveseventy = 0
abovesixty = 0
abovefourtyfive = 0
abovethirty = 0







# CLASS
class Student:
	def __init__(self, name, ids,days, percentage=0,mark=0):
		self.name = name
		self.ids = ids
		self.percentage = percentage
		self.mark = mark
		self.days = days




	 

Students = []
totals = 19








#input
Students.append(Student("Tajwar Hossain", "1310324", 9))
Students.append(Student("Abu Sayed", "1410194", 16))
Students.append(Student("Maruf Ahmed", "1512169", 13))
Students.append(Student("Jannatul Maowa", "1512331", 14))
Students.append(Student("Fatin Anjum", "1512448", 4))
Students.append(Student("Sharieaz Kavier", "1513192", 12))
Students.append(Student("Anikul Islam", "1520086", 18))
Students.append(Student("Sazid Khandaker", "1520347", 12))
Students.append(Student("Md Raihan", "1520527", 18))
Students.append(Student("Md. Wasy Anjum", "1520636", 18))
Students.append(Student("Shefaur Rahman", "1520661", 5))
Students.append(Student("Shanto Kumar", "1521289", 17))
Students.append(Student("Tanjila Rahman", "1521852", 15))
Students.append(Student("Bipasha Ahmed", "1521974", 17))
Students.append(Student("Md Rauful Islam", "1522041", 15))
Students.append(Student("Atique Hossain", "1530153", 12))
Students.append(Student("Fabliha Benzir", "1531424", 15))
Students.append(Student("Shah Ashisul Abed", "1610390", 18))
Students.append(Student("Sudipta Barman", "1611007", 16))
Students.append(Student("Md. Abdullah", "1611869", 14))
Students.append(Student("Dipta Kumar", "1612720", 17))
Students.append(Student("Prattoy Saha", "1620387", 20))
Students.append(Student("Alamin Islam", "1711244", 15))
Students.append(Student("Yearat Hossain", "1712275", 16))
Students.append(Student("Mashfiq Rizvee", "1811173", 20))



# CALCULATING PERCENTAGE AND ASSIGNING MARKS

def Calculatedays(days,total):
	a = days/totals
	a = a * 100
	if a>100: 
		return 100
	return a

for Student in Students:
	if (Calculatedays(Student.days, totals) >= 70):
		Student.mark = 5
		Student.percentage = round(Calculatedays(Student.days,totals))
		aboveseventy = aboveseventy + 1

	elif (Calculatedays(Student.days, totals) >= 60):
		Student.mark = 4
		Student.percentage = 60
		abovesixty = abovesixty + 1
		
	elif (Calculatedays(Student.days, totals) >= 45):
		Student.mark = 3
		Student.percentage = 45
		abovefourtyfive = abovefourtyfive + 1
		
	elif (Calculatedays(Student.days, totals) <= 30):
		Student.mark = 2
		Student.percentage = 30
		abovethirty = abovethirty + 1

print("Please enter the number of students: 30")
		
print("Calculated Attendance Percentage")

dash = '-' * 65
i = 0
serial = 1
print(dash)
print('{:<4s}{:<25s}{:>4s}{:>20s}{:>12s}'.format("No","Name","ID","Percentage","Marks"))
print(dash)

for Student in Students:
    name = Student.name
    ids = Student.ids
    per = str(Student.percentage) + "%"
    marks = str(Student.mark)
    num = str(serial)
    serial = serial+1
    print('{:<4s}{:<25s}{:>6s}{:^20s}{:>7s}'.format(num,name, ids, per, marks))



print('                                                                                                             ')
print('                                                                                                             ')
print('Attendance Percentage (Student Count):')
print('No.   Percentage   Count')
print('1.        70%       ' + str(aboveseventy))
print('2.        60%       ' + str(abovesixty))
print('3.        45%       ' + str(abovefourtyfive))
print('4.        30%       ' + str(abovethirty))



# PIE CHART PLOTTING
ranges = [aboveseventy, abovesixty, abovefourtyfive, abovethirty]


values = ["70%", "60%", "45%", "30%"]


plt.pie(ranges, labels=values, startangle=90, autopct='%.1f%%')


plt.title('Attendance Percentage (Student Count):')


plt.axis('equal')


plt.show()