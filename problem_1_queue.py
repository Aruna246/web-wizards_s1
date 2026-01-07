queue = []
token_no = 1
max_size = 100
while True:
    choice = input("Enter your choice:")
    if choice == "1":
        if len(queue) < max_size:
            print("Token No:",token_no)
            queue.append(token_no)
            token_no += 1
        else:
            print("Queue is full. Please try later.")
    elif choice == "2":
        if queue:
            served_token = queue.pop(0)
            print("Served Token No:",served_token)
        else:
            print("No students waiting.")
    elif choice == "3":
        print("Students Waiting:",len(queue))
    else:
        print("Invalid choice.")
        
