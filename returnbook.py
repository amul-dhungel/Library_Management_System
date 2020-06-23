def returnbook(p):
    import datetime
    
    book_id=[] # creates an empty list to store borrowed book id
    book_returned =[] # creates an empty list to store name of returned book and returner
    
    print("|Book   ID  |      Books                 |     Author         |  Quantity    |   Price    |")
    print("\n")
    for a,books in enumerate(p):
        if books[3]!=0:
            print("   ",a,"     ","|",books[0]," "*(25-len(books[0])),"|"," ",books[1]," "*(15-len(books[1])),"|",
                  "  ",books[2]," "*(8-len(str(books[2]))),"|","   ",
                  books[3]," "*(5-len(str((books[3])))),"|") #displaying the available products in tabular form
            book_id.append(a)
            print("\n")

    borrowed_namelist=[]                                                   
    nameStored_file = open("librarian.txt","r") # reades text file
    lines = nameStored_file.readlines() # reades data of text file line by line
    for stored_name in lines:
        borrowed_namelist.append(stored_name.replace("\n","").split(",")) # converts the data of text file into 2d list
    
    nameStored_file.close() #closes the opened text file
    
    
    
    firstName = input("Enter your first name : ").upper()
    secondName = input("Enter your second name : ").upper()
    fullName = firstName +" "+ secondName

    '''year = int(input("Enter a year"))
    month = int(input("Enter a month"))
    day = int(input("Enter a day"))'''

    #date = print(year,"-",month,"-",day)
    
    date_storedlist = [] 
    date_storedfile = open("Borrowedate.txt","r") #makes the textfile able to read
    lines = date_storedfile.readlines()
    for stored_date in lines:
        date_storedlist.append(stored_date.replace("\n","").split(",")) #adds the date in an empty list
    
    date_storedfile.close() # closes the opend file
    print(date_storedlist)

   
        
        
    
    
    
    for i in range(len(date_storedlist)):
        
        if fullName == date_storedlist[i][0]: #checks if the returner name matches to borrower name or not
            
            string_date = date_storedlist[i][1]
            format = "%Y-%m-%d" #making datetime object
            datetime_object = datetime.datetime.strptime(string_date,format)
            t = datetime.datetime.today()-datetime_object
            count=0
            choice= 'y'
            while choice == 'y':
                    
                success = True
                while success == True: 
                    try:
                        bookID =int( input("Enter a bookID that you want to return : ")) #ask the user to input the bookID
                        success = False
                        if bookID in book_returned:
                            print("You have already returned this book")
                            success = True

                                
                                    
                    except:
                        print("Book id must be a number")

                book_returned.append(bookID) #adds the returned book in an empty list

                count = count + 1

                if count== 2:
                        print("You have only borrowed 2 books from this libarary")
                        print(book_returned)
                        choice = 'n' 
                else:
                    choice = input("Do you want to return another book?(y/n)")


            print("*********************Receipt*********************")
            print()
            print()
            print()
            returnbill= open(fullName+".txt","w") #writes and saves data in a text file
            returnbill.write("*****************Receipt****************")
            returnbill.write("\n")
            returnbill.write("\n")
            #bill.write("Date: "+a+"/"+b+"/"+c+" Time: "+d+":"+e+":"+f)
            #print("Date: ",a,"/",b,"/",c," Time: ",d,":",e,":",f)
            print()
            print()
            returnbill.write("\n")
            returnbill.write("\n")
            returnbill.write("Returner name: "+fullName)#writing returner name on bill
            print("Returner name: ",fullName)#printing returner name
            print()
            returnbill.write("\n")
            returnbill.write("\n")
            print("Date : ",datetime.datetime.today())
            returnbill.write("Date : "+str(datetime.datetime.today()))#Writes date in a text file
            returnbill.write("\n")
            returnbill.write("\n")
            
            print()
            print()
            returnbill.write("Bookname               Author               price")
            returnbill.write("\n")
            print("Book name        Author        price")
            
            for i in book_returned:
                if t.days> 10: #checking for fine
                    total2=0
                    total2+=(t.days-10)*0.1
                    p[i][2]+=1
                    print(p[i][0],"               ",p[i][1],"               ",p[i][3])
                    returnbill.write(str(p[i][0])+"               "+str(p[i][1])+"               "+str(p[i][3])) # prints the bill in a tabular form
                    returnbill.write("\n")
                    print("The total fine is : ",total2)
                    returnbill.write("The total fine is : "+str(total2))
                else:
                    p[i][2]+=1
                    print(p[i][0],"               ",p[i][1],"               ",p[i][3])
                    returnbill.write(str(p[i][0])+"               "+str(p[i][1])+"               "+str(p[i][3])) # prints the bill in a tabular form
                    returnbill.write("\n")
            print()
            returnbill.write("\n")
            returnbill.write("\n")
            returnbill.write("Thanks for visiting")
            returnbill.close
            break;
            
    if fullName != date_storedlist[i][0]:
        print("Sorry you havent borrowed any book from this library")
            

    return p

        


            
    
