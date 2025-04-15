import json
filename='mybook.txt'
books=[]


def read_book():
   with open (filename,'r') as book_file:
      json.load(book_file)
    
      
def write_book():
   with open (filename,'w') as book_file:
      data=json.dump(books,book_file, indent=4)
      print("current books",data)
      
def add_book(user_book_name, user_aut_name, user_book_id):

 read_book()
 books_entry={
   'book_name':user_book_name,  
   'aut_name':user_aut_name,
   'book_id':user_book_id
 }
    
 books.append(books_entry)
 print(books)

write_book()
  
 

 
def rem_book(user_book_name, user_aut_name, user_book_id):
 read_book() 
 for book in books:
   print(book)
   if (book['book_name']==user_book_name and
        book['aut_name']==user_aut_name and 
        book['book_id']==user_book_id):
     removeed_data=books.remove(book)  
     print( removeed_data)  
     break 
   else:
     print("no data found") 
 return books
write_book()
def search_book(user_book_name, user_aut_name, user_book_id):
 read_book()    
 found = False
 for book in books:
    print(book)
    if (book['book_name']==user_book_name and
        book['aut_name']==user_aut_name and 
        book['book_id']==user_book_id):
        
         print("searched_data",book)
         found = True
         break
    else:
          print("no data found")
 return books
write_book()  
def upd_book(user_book_name, user_aut_name, user_book_id):  
    read_book() 
    for book in books:
      print(book)
      if (book['book_name']==user_book_name and
        book['aut_name']==user_aut_name and 
        book['book_id']==user_book_id):
         print("Current book:", book)
         new_name = input("Enter new book name : ")
         new_aut = input("Enter new author name: ")
           
         new_id = input("Enter new book ID : ")
         
         if new_name:
                book['book_name'] = new_name
         if new_aut:
                book['aut_name'] = new_aut
         if new_id:
                book['book_id'] = int(new_id)

         print("Book updated:", book)
         return
    print("Book not found.")
write_book()
  


while True:
 

 num=input("1.add book 2.remove book 3.search book 4.update book 5.exit\n")
 if num=='1':
    user_book_name=input("enter a book name ")
    user_aut_name=input("enter a author name ")
    user_book_id=int(input("enter a book id "))    
 
    add_book( user_book_name, user_aut_name, user_book_id)
    print("cuurent book",books)
 elif num=='2':
    user_book_name=input("enter a book name ")
    user_aut_name=input("enter a author name ")
    user_book_id=int(input("enter a book id "))    
 
   # book_id=int(input("enter a book id "))    
    rem_book(user_book_name, user_aut_name, user_book_id)

    print("new books")
    print("cuurent book",books)
 elif num=='3':
    user_book_name=input("enter a book name ")
    user_aut_name=input("enter a author name ")
    user_book_id=int(input("enter a book id "))
   
 
    search_book(user_book_name, user_aut_name, user_book_id)
    print("cuurent book",books)
 elif num=='4':
    user_book_name=input("enter a book name ")
    user_aut_name=input("enter a author name ")
    user_book_id=int(input("enter a book id "))
      
 
    upd_book(user_book_name, user_aut_name, user_book_id)
    print("cuurent book",books)
 elif num=='5':
   exit
 else:
   print("invalid")   
       
   

  




       
   


