# To Do list

tasks=[]

print("1.add task")
print("2.view task")
print("3.mark task completed")
print("4.update your task")
print("5.delete task")
print("6.exit")

while True:
    function=int(input("enter the required function you need to perform:"))

    if function==1:
        task_name=input("enter the task you want to add:")
        task_deadline=input("enter the deadline of the task:")
        task_info=input("enter the info you want to store in the task:")
    
        task_list={ "task name:": task_name,
                    "deadline:": task_deadline,
                    "info:":task_info,
                    "status:":"pending" }

        tasks.append(task_list)
        print("task has been added")

    elif function==2:
        if len(tasks)==0:
            print("no tasks left")

        else:
            for task_list in tasks:
                print("task name:",task_list["task name:"])
                print("deadline:",task_list["deadline:"])
                print("info:",task_list["info:"])
                print("status:",task_list["status:"])
                print()

    elif function==3:
        b=input("enter the task that has to be marked as completed:")
        found=False
            
        for task_list in tasks:
            if task_list["task name:"]==b:
                task_list["status:"]="completed"
                print("task status changed")
                found=True
                break

        if found==False:
            print("task not found")

    elif function==4:
        c=input("enter the task that has to be updated:")
        found=False
        
        for task_list in tasks:
            if task_list["task name:"]==c:
                updated_name=input("enter the updated name of the task:")
                updated_deadline=input("enter the updated deadline for the task:")
                updated_info=input("enter the updated info about the task:")
                updated_status=input("enter the updated status of the task:")
                task_list["task name:"]=updated_name
                task_list["deadline:"]=updated_deadline
                task_list["info:"]=updated_info
                task_list["status:"]=updated_status
                
                print("the task has been updated")
                found=True
                break
            
        if found==False:
            print("task is not available")

    elif function==5:
        delete_task=input("enter the name of the task that has to be deleted:")
        found=False

        for task_list in tasks:
            if task_list["task name:"]==delete_task:
                tasks.remove(task_list)
                print("task has been deleted successfully")
                found=True
                break
            
        if found==False:
            print("task is not available")

    elif function==6:
        print("thanks for using the to do list")
        break

    else:
        print("invalid operation")
            
            
            
        
                
                    
