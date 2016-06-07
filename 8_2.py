'''
Created on 6 Jun 2016

@author: Luo Long Zhao Mars
'''
#account management
def toregister():
    prompt = 'Please register bt entering your account name here '
    while True:
        name = input(prompt)
        if name in database:
            prompt = 'The name has been taken, please try another '
            continue
        else:
            pwd = input("Please input your password here")
            db[name] = pwd
            break

def returnuser():
    name = input("account: ")
    password_check = input("password: ")
    password = db.get(name)
    if password == password_check:
        print ('login successfully')
    else:
        print ('invalid password, please try again')

def showmenu():   #Prerequisite to the processing of the code blocks upmentioned.
    prompt = """
    (N)ew User login
    (R)eturn User login
    (Q)uit

    You are:"""
    
    finished = False
    while not finished:   #To ensure user made a choice between N,E and Q, otherwise quit
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print ('\nYou selected [%s] as your choice' % choice)
            if choice not in 'nrq':   #'neq'as a string in which could be chopped and compared on each character
                print ('invalid choice, please try again')
            else:
                chosen = True
                finished = True
    if choice == 'n':
        newuser()
    elif choice == 'r':
        returnuser()
    elif choice == 'q':
        exit()
    showmenu()

showmenu()  #the first code block to be executed.