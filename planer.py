# -*- coding: utf-8 -*-
"""
o Add new tasks.
o View all tasks.
o Mark tasks as completed.
o Delete tasks
"""


main_user="";


while main_user != "quit":

        
    def planer():
        plans = []
        marks = []
        new_plans = " "

        while new_plans != "stop":
            new_plans = str(input("What are your plans for today? Type 'stop' to finish: "))
            if new_plans != "stop":  
                plans.append(new_plans)
                marks.append("Not done")

        print(plans)
        print(marks)

        return plans, marks

    ###################################################################
    #val1, val2 = planer()

    def check(d, v):  
        for i in d:  
            user = input(f"Have you done {i}? (yes/no) ")  
            if user.lower() == "yes":
                index = d.index(i)  
                v[index] = "Done!"  


    #check(val1, val2)

    def view(g, h):
        user=input("Would you like to view the plans for today?: ");
        if user =="yes":
            print(g)
            print(h)
        else:
            "nothing"
        return 
        
    #view(val1, val2)  

    def delete(plan, mark):
        user = input("Would you like to modify your list? (yes/no): ")
        if user.lower() == "yes":
            i = 0
            while i < len(plan):  
                print(f"Plan: {plan[i]}")
                user2 = input(f"Would you like to delete this plan: {plan[i]}? (yes/no): ")
                if user2.lower() == "yes":
                    del plan[i] 
                    del mark[i]  
                else:
                    i += 1  
        return plan, mark

    #delete(val1, val2)
    user_input=input("What would you like to do? Type the number throught 1-4 \n Add new task? \n View all task? \n Mark tasks as completed. \n Delete tasks? \n");
    if user_input == "1": 
        val1, val2 = planer()
    if user_input == "2": 
        view(val1, val2)
    if user_input == "3": 
        check(val1, val2)  
    if user_input == "4": 
        delete(val1, val2)
    
                          
    
    
    
    