rooms = int(input("Enter the total number of rooms:"))
roomno = 1
for i in range(1,100):
 rollno= int(input("Enter your Roll.no:"))
 if(rollno<=rooms):
    print("Alloted room no:",roomno)
    roomno+=1
 else:
    print("Available rooms: 0")
    print("No rooms available")
 
