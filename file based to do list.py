# to do list based on functions

print("1.add task")
print("2.view task")
print("3.mark task completed")
print("4.update your task")
print("5.delete task")
print("6.exit")

while True:
    choice=int(input("enter the function that you need to perform:"))

    if choice==1:
        task_name=input("enter the task you want to add:")
        task_deadline=input("enter the deadline of the task:")
        task_info=input("enter the info you want to store in the task:")
        task_status="pending"
        file=open("task.txt","a")
               
        file.write(task_name+"\n")
        file.write(task_deadline+"\n")
        file.write(task_info+"\n")
        file.write(task_status+"\n")
        file.close()

        print("task added successfully")

    elif choice==2:
        file=open("task.txt","r")
        content=file.read()
        print(content)

        file.close()

    elif choice==3:
        task_completed=input("enter the task that has been completed:")

        file=open("task.txt","r")
        lines=file.readlines()
        file.close()

        found=False

        for i in range(0, len(lines), 4):
            if lines[i].strip() == task_completed:
                lines[i + 3] = "completed\n"
                found = True
                break

        file=open("task.txt","w")
        file.writelines(lines)
        file.close()

        if found:
            print("task marked as completed")
        else:
            print("task not found")


    elif choice==4:
        task_update=input("enter the task to be updated:")

        file=open("task.txt","r")
        lines=file.readlines()
        file.close()

        found=False

        for i in range(0,len(lines),4):
            if lines[i].strip()==task_update:
                update_name=input("enter the new name:")
                update_deadline=input("enter the new deadline:")
                update_info=input("enter the new info:")
                update_status=input("completed/pending :")
                lines[i]=update_name + "\n"
                lines[i+1]=update_deadline + "\n"
                lines[i+2]=update_info + "\n"
                lines[i+3]=update_status + "\n"
                found=True
                break

        file=open("task.txt","w")
        file.writelines(lines)
        file.close()

        if found:
            print("task updated")
        else:
            print("task not found")


    elif choice==5:
        task_delete=input("enter the task to be deleted:")

        file=open("task.txt","r")
        lines=file.readlines()
        file.close()

        found=False

        for i in range(0,len(lines),4):
            if lines[i].strip()==task_delete:
                del lines[i:i+4]
                found=True
                break

        if found:
            print("task deleted")
        else:
            print("task not found")

        file=open("task.txt","w")
        file.writelines(lines)
        file.close() 

    elif choice==6:
        print("thank you for using the to do list")
        break   
    
    else:
        print("invalid choice")

        
            
