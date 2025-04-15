import json
userfile='myuser.txt'
user=[]

def read_user():

   with open (userfile,'r') as user_file:
      json.load(user_file)

def write_user():
   with open (userfile,'w') as user_file:
      data=json.dump(user,user_file, indent=4)
      print("current users",data)
      
def add_book(user_inp_name,user_mob_no,user_email_id):

 read_user()
 user_entry={
   'user_name':user_inp_name,  
   'mob_no':user_mob_no,
   'email_id':user_email_id
 }
    
 user.append(user_entry)
 print(user)
write_user()
  
 

 
def rem_user(user_inp_name,user_mob_no,user_email_id):
 read_user()
 for userinfo in user:
    print("rem user",userinfo)
    if (userinfo['user_name']==user_inp_name and
        userinfo['mob_no']==user_mob_no and 
        userinfo['email_id']==user_email_id):
        user.remove(userinfo)  
        print( "removed data")  
        break 
    else:
     print("no data found") 
 return user
write_user()
def search_user(user_inp_name,user_mob_no,user_email_id):
 read_user()    
 found = False
 for userinfo in user:
    print(userinfo)
    if (userinfo['user_name']==user_inp_name and
        userinfo['mob_no']==user_mob_no and 
        userinfo['email_id']==user_email_id):
        
         print("searched_data ",userinfo )
         found = True
         print("data found in user")
         break
    else:
          print("no data found")
 return user
write_user() 

def upd_user(user_inp_name,user_mob_no,user_email_id):  
    read_user()
    for userinfo in user:
      print(userinfo)
      if (userinfo['user_name']==user_inp_name and
        userinfo['mob_no']==user_mob_no and 
        userinfo['email_id']==user_email_id):
         print("Current user:", user)
         new_name = input("Enter new user name : ")
         new_mobileno= int(input("Enter new mobile no : "))
           
         new_emailid = input("Enter new email ID : ")
         
         if new_name:
            userinfo ['new_name'] = new_name
         if new_mobileno:
            userinfo ['new_mobileno'] =int(new_mobileno)
         if new_emailid:
            userinfo ['email_id'] = new_emailid

         print("user updated:", user)
         return user
    print("user not found.")
write_user()
  


while True:
 

 num=input("1.add user\n 2.remove user\n 3.search user\n 4.update user\n 5.exit\n")
 if num=='1':
    user_inp_name=input("enter a user name ")
    user_mob_no=int(input("enter a user mobile no "))
    user_email_id=input("enter a user email id ")
 
    add_book( user_inp_name,user_mob_no,user_email_id)
    print("cuurent users",user)
 elif num=='2':
    user_inp_name=input("enter a user name ")
    user_mob_no=int(input("enter a user mobile no "))
    user_email_id=input("enter a user email id ")
 
     
    rem_user(user_inp_name,user_mob_no,user_email_id)

    print("cuurent user",user)
 elif num=='3':
    user_inp_name=input("enter a user name ")
    user_mob_no=int(input("enter a user mobile no "))
    user_email_id=input("enter a user email id ")
    search_user(user_inp_name,user_mob_no,user_email_id)
    print("cuurent user",user)
 elif num=='4':
    user_inp_name=input("enter a user name ")
    user_mob_no=int(input("enter a user mobile no "))
    user_email_id=input("enter a user email id ")
 
      
 
    upd_user(user_inp_name,user_mob_no,user_email_id)
    print("cuurent user",user)
 elif num=='5':
   exit
 else:
   print("invalid")   
       
   

  




       
   


