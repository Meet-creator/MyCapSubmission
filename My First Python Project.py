import csv 

def write_into_csv(info_list):
	with open("Student_list.csv", "a", newline="") as csvfile:
		writer = csv.writer(csvfile)

		if csvfile.tell() == 0:
			writer.writerow(["Name", "Age", "Contact Number", "E-Mail ID"])

		writer.writerow(info_list)
def deleting_last_line():
	f = open('Student_list.csv', "r+")
	lines = f.readlines()
	lines.pop()
	f = open('Student_list.csv', "w+")
	f.writelines(lines)

condition = True
num_students = int(input("Please write the number of students data you want to enter: "))
num_input = 1
student_info = input("Please write the data on student 1 (Format -- Name Age Contact_number E-Mail)(Keywords -- 'stop' => stop taking input; 'del' => del the previous entered information): ")
while condition:
	if student_info == "stop":
		break
	student_info_list = student_info.split(" ")
	if student_info == "del":
		deleting_last_line()
		print("Last Input will be deleted")
		num_input -= 1
	if student_info != "del":
		num_input += 1
		print("The registered list will be:" + student_info)
		write_into_csv(student_info_list)
	student_info = input(f"Please write the data on student {num_input}:")
	if num_input == (num_students + 2):
		break