Total_classes= int(input("Enter the Total Classes:"))
Attended_classes= int(input("Enter the Attended Classes:"))
percentage = (Attended_classes/Total_classes)*100
require= (0.75*Total_classes)-Attended_classes
print("Attendance percentage=",percentage)
if(percentage>=75):
 print("Eligible to attend the exam")
else:
 print("Not Eligible to attend the exam")
 print("Required to attend the class:",require)
