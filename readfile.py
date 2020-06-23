def readfile(a): #defining a function to read a text file
    data =[] # creating an empty list
    
    stock = open(a,"r") #makes the file readable
    lines = stock.readlines() #changing the data of txt file into list
    for books in lines:
        data.append(books.replace("\n","").split(",")) # converts the given text into the 2d list form
   
    stock.close()
    for i in range(len(data)):
        for j in range(len(data[i])): 
           if j>1:
                data[i][j]=float(data[i][j]) # converts the string of text file into float
    return data
