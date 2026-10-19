#to day we wanna wirit todo list with python 
#we wanna practice csv file and pickel library and functions and loops togather and speak about them.

import pickle
my_work = []

work_file = open("csv" , "wb")
pickle.dump(my_work , work_file)
work_file.close()

while True :
    to_do = input("say your work : ")

    if to_do.lower() == "remove" or "finish" or "show":
        pass

    else :
        my_work.append(to_do)


    print(f"your todo list : {my_work}")
    if to_do.lower() == "finish":
        print (my_work)
        break

    if to_do.lower() == "remove":
        remove = input("say your work to remove it : ")
        if remove in my_work :
            my_work.remove(remove)
            print("file removed")
            print(f"your todo list : {my_work}")
            
        else :
            print("the work doesnt exisit !")


    if to_do.lower() == "show" :
        print(work_file)
    



