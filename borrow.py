
def borrow(z):
    book_id=[] # stores the unique book id of each book
    book_borrowed =[] # stores the 
    borrower_name = []
    users_date = []
    
    print("|Book   ID  |      Books                 |     Author         |  Quantity    |   Price    |")
    print("\n")
    for a,books in enumerate(z):
        if books[3]!=0:
            print("   ",a,"     ","|",books[0]," "*(25-len(books[0])),"|"," ",books[1]," "*(15-len(books[1])),"|",
                  "  ",books[2]," "*(8-len(str(books[2]))),"|","   ",
                  books[3]," "*(5-len(str((books[3])))),"|") #displaying the available products
            book_id.append(a)
            print("\n")
    
    firstName = input("Enter your first name : ").upper()
    secondName = input("Enter your second name : ").upper()
    fullName = firstName +" "+ secondName
    borrower_name.append(fullName)

    count=0
    choice= 'y'
    while choice == 'y':
        questions = True
        while questions == True:
            success = True
            while success == True: 
                try:
                    bookID =int( input("Enter a bookID : ")) 
                    success = False
                    if bookID in book_borrowed:
                        print("You haven't returned the previous book")
                        success = True

                    
                        
                except:
                    print("Book id must be a number")
               
            if bookID in book_id:
                    book_borrowed.append(bookID) #adds the book borrowed in an empty list
                    
                    questions = False
            else:
                print("You entered invalid book id")
                
            
        count=count+1
        
        if count== 2:
            print("You reached your limitation")
            print(book_borrowed)
            choice = 'n' 
        else:
            hallucination = True
            while hallucination == True:
                
                dillema = input("Do you want to borrow another book?(y/n)")
                
                
                if dillema == 'y':
                    choice ='y'
                    break;
                elif dillema == 'n':
                    choice ='n'
                    break;
                else:
                    print("only 'y' or 'n' are allowed as yes or no")
                    hallucination = True
                        

# billing starts from here

    total=0
    j=0
    import datetime
    a=str(datetime.datetime.now().year) 
    b=str(datetime.datetime.now().month) 
    c=str(datetime.datetime.now().day)
    date_combination = a+"-"+b+"-"+c
    d=str(datetime.datetime.now().hour) 
    e=str(datetime.datetime.now().minute) 
    f=str(datetime.datetime.now().second)
    print()
    users_name = open("Librarian.txt","a") #makes the txt file readable
    for items in borrower_name:
        users_name.write(str(items)+",") #wrties the name of borrower in text file
        for numbers in book_borrowed:
            
            users_name.write(str(numbers)+",") #writes the name of borrowed books
            
        users_name.write("\n")

    users_name.close()

    users_date = open("Borrowedate.txt","a") #makes the txt file write and append
    for items in borrower_name:
        users_date.write(str(items)+",") #writes the name of borrower in txt file
        for items in borrower_name:
        
            users_date.write(date_combination) #writes the date of borrowed books
        users_date.write("\n")
    
    users_date.close()
    
    print("*********************Receipt*********************")
    print()
    print()
    print()
    bill= open(a+b+c+d+e+f+fullName+".txt","w") #writes and saves data in a text file
    bill.write("*****************Receipt****************")
    bill.write("\n")
    bill.write("\n")
    bill.write("Date: "+a+"/"+b+"/"+c+" Time: "+d+":"+e+":"+f)
    print("Date: ",a,"/",b,"/",c," Time: ",d,":",e,":",f)
    print()
    print()
    bill.write("\n")
    bill.write("\n")
    bill.write("Borrower name: "+fullName)#writing Borrrower name on bill
    print("Borrower name: ",fullName)#printing borrower name
    print()
    bill.write("\n")
    bill.write("\n")
    bill.write("Bookname               Author               price")
    bill.write("\n")
    print("Book name                    Author                      price")
    for i in book_borrowed:
        total+= z[i][3] #calculates the price
        z[i][2]-=1 #update the list
        print(z[i][0],"               ",z[i][1],"               ",z[i][3])
        bill.write(str(z[i][0])+"               "+str(z[i][1])+"               "+str(z[i][3])) #prints bill in tabular format
        bill.write("\n")
    print()
    bill.write("\n")
    bill.write("\n")
    print("Total Amount: "+str(total))
    bill.write("Total Amount: "+str(total  ))
    bill.write("\n")
    bill.write("\n")
    bill.write("Thanks for visiting")
    bill.close()
    

    return z # returns the update list
    
 
        
    
    
  
   
     
   
