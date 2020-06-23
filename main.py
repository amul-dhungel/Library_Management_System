import readfile
import borrow
import returnbook
import updatefile


print("\t \t \t \t ///////////////////----------------\\\\\\\\\\\\\\\\\\")

a=readfile.readfile("stock.txt") # passes the text file into readfile module 
choice = 'y'
while choice == 'y':

    genius = True
    while genius== True:
        answer = input("Do you want to borrow or return the book?(B/R) : ")
        if answer=="B" or answer=="b":
            b=borrow.borrow(a) # passes the list into borrow moudle with the help of parameters
            l= updatefile.updatefile(b) #passes the updated list into updatefile moudle with the help of parameters
            genius =False
            
        elif answer=="R" or answer=="r":
            c=returnbook.returnbook(a) #passes the list into returnbook moudle with the help of parameters
            m = updatefile.updatefile(c) #passes the updated list into updatefile
            genius = False
            
        else:
            
            print("Enter a valid letter")

    new_reader= input("Do you want to continue(y/n)?")

    if new_reader == 'y':
        choice = 'y'
    else:
        choice = 'n'
    









    
