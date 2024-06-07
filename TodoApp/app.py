def task():
  tasks = [] # empty list
  print("------welcome to the task management app")
  
  total_task=int(input("enter how many task you want to add ="))
  
  for i in range (1, total_task+1):
    task_name = input(f"enter task{i}=") # enter task 3
    tasks.append(task_name)
    
  print(f"today's task are\n{tasks}")
    
  while True:
      operation = int(input("enter 1=Add\n2-Update\n3-Delete\n4-view\n5-Exit/stop/"))
      if operation == 1:
        add=input("enter task you want to add = ")
        tasks.append(add)
        print(f"Task{add} has been successfully added...")
        
      elif operation == 2:
        updated_val=input("enter the task name you want to update = ")
        if updated_val in tasks:
          up = input("enter new task =")
          ind = tasks.index(updated_val)
          tasks[ind] = up
          print(f"Updated task {up}")
          
      elif operation == 3:
        del_val=input("ehich task do you want to delete=")
        if del_val in tasks:
          ind = tasks.index(del_val)
          del tasks[ind]
          print(f"task {del_val} has been deleted successfully...")
          
      elif operation==4:
        print(f"total task={tasks}")
        
      elif operation==5:
        print("closing the program:")
        break
      else :
        print("invalid choice")
          
          
          
task()