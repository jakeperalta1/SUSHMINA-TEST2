print("WELCOME TO THE GRANN'S PHONE DIRECTORY") 
#creating empty list
phoneDirectory={}

while True:
    
    print("Menu")
    print("1. Add a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Quit")

    x=int(input("Enter your choice: "))
    if x==1:
       
        while True:    
            p=input("Enter name: ")
            #allowing only letters and space as input
            if all(p.isalpha() or p.isspace() for p in p):
                break
            else:
                print("Error")
        
        
        
        q=input("Enter your 10-digit phone: ")
        
        #allowing 10 digits only
        if len(str(q))==10 or q.isdigit() :
            
                phoneDirectory.update({p:q})
        else:
                print("Invalid digit of number. ")
        
                continue
	        
        print("Record added")
    
    elif x==2:
        f= input("Enter name to search:")
        if f in phoneDirectory:
                print({f:phoneDirectory(p)})
        else:
                 print("Record doesnot exist.")
    
    elif x==3:
        p=input("Enter name: ")
        q=input("Enter your 10-digit phone: ")
        phoneDirectory.update({p:q})
        print(phoneDirectory)
        print("Record added")
        
    elif x==4:
        g= input("Enter name:")
        if phoneDirectory == {}:
            print("Record is empty.")
        else:
            del phoneDirectory[g]
            print("Record deleted")
        #if phoneDirectory == {}:
           # print("Record is empty.")
    
    elif x==5:
        break
    
    else:
        print("Invalid option.")
        
            
        