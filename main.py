total_chores= 4
original_count= total_chores

print ("You have ",original_count,"chores to finish today!!\n")

completed_count = 0
chore_number = 1

while chore_number <= total_chores:
    if chore_number == 1 :
        next_chore= "Make your bed!!"

    elif chore_number == 2:
        next_chore="Feed the pet"

    elif chore_number == 3:
        next_chore="Take out the trash"

    else:
        next_chore= "Wash the dishes"   

    answer = input(f"Have you completed {next_chore} (yes/no):")     
        
    if answer=="yes":
        completed_count+=1
        chore_number+=1
        print ("Great Job! Chore completed.")

    else:
        print ("Okay, Finish it and check again!")

    print ("Chores remaining", total_chores-completed_count)
    print ()

    print ("==================================================")
    print ("          All chores complete!!")
    print ("Great work completeing yor entire checklist today!")
    print ("==================================================")