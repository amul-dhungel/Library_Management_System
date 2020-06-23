def updatefile(savedata):

    books = [] # creates an empty list 
    for i in savedata:
        books.append(map(str,i)) #converting the values of list into strings
    file = open("stock.txt","w") #creates a test file which is able to write
    for j in books:
        file.write(",".join(j)) #joins the data of list with comma in text file 
        file.write("\n")
    file.close() # closes the file
        


  
    
