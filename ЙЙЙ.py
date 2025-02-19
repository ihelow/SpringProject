
main_user="";


while main_user != "quit":
    full_list = ["algebra", "geometry", "linear algebra", "calc 1"]

    def register():
        plans = []
        
        print("You are allowed to register for up to 3 classes.")
        
        while len(plans) < 3:  
            new_plans = input("What class do you want to register for? \
                              Type 'stop' to finish: ").strip()
            
            if new_plans.lower() == "stop":
                break  
            
            if new_plans not in full_list:
                print("Sorry, that class is not available. Choose from:", 
                      full_list)
                continue  
            
            if new_plans in plans:
                print("Sorry! You have already registered for this course. \
                      Try a different one.")
                continue  
            
            plans.append(new_plans) 
            print("You have successfully registered for:", plans)

        print("Final registered courses:", plans)
        return plans



    #=======================================================================================  
      
    def view_full(): 
        print(full_list) 
        return 





    #=======================================================================================

    def view_plan(regist): 
        print(regist) 

        return
     
   # view_full()
   # regist = register()   
   # view_plan(regist)
    
    user_input=input("What would you like to do? Type the number throught 1-4 \n \
                     View the full list of available courses? \
                         \n Register for courses? \
                             \n View registered courses? \
                                 \n Quit the program \n");
    if user_input == "1": 
        view_full()
    if user_input == "2": 
        regist = register() 
    if user_input == "3": 
        view_plan(regist)  
    if user_input == "4":
        main_user="quit"


