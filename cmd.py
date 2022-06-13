class Terminal:

    def pwdfun(): #pwd function
        import os
        current_Dir=os.getcwd()
        print(current_Dir)

    def cdfun(path): # cd function
        import os
        last_path = os.getcwd()
        if os.path.exists(path):
            os.chdir(path)
            new_dir = os.getcwd()
            print("Current working directory: {0}".format(os.getcwd()))
        else:
            print("The path is invalid! ")

    def lsfun(path1): # ls function
        import os
        if os.path.exists(path1):
            ls = os.listdir(path1)
            print(ls)
        else:
            print("The path is invalid! ")

    def cpfun(path1,path2): # cp function
        import sys
        from shutil import copyfile
        from sys import exit
        source = path1
        target = path2
        # adding exception handling
        try:
            copyfile(source, target)
        except IOError as e:
            print("Unable to copy file. %s" % e)
            exit(1)
        except:
            print("Unexpected error:", sys.exc_info())
            exit(1)
        print("\nFile copy done!\n")
        while True:
            print("Do you like to print the file ? (y/n): ")
            check = input()
            if check == 'n':
                break
            elif check == 'y':
                file = open(target, "r")
                print("\nHere follows the file content:\n")
                print(file.read())
                file.close()
                print()
                break
            else:
                continue
    
    def mvfun(path1,path2): # mv function Move
        import os
        import shutil
        if os.path.exists(path1):
            shutil.move(path1,path2)
            print("The file is moved! ")
        else:
             print("The path is invalid! ")

    def rm1fun(path1): # remove 1 function to remove specific file (rm /home/myfile.txt)
        import os
        import shutil
        os.remove(path1)
        print("The file removed")

    def rm2fun(path2): # remove 2 function to remove directory (rm -r /home)
        import shutil
        shutil.rmtree(path2)
        print("directory removed")

    def rm3fun(path1,path2):   # remove 3 function to remove all files with the same typy in specific folder (rm /home *.txt to delete all txt files in folder home)
        from pathlib import Path 
        for f in Path(path1).glob(path2):
            try:
                f.unlink()
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))
        print("all",path2,"files removed in folder",path1)

    def mkdirfun(path1): # mkdir function
        import os
        try:
            mode = 0o777
            os.mkdir(path1, mode)
            print("folder created successfully! ") 
        except FileExistsError:
            print("folder already existes! ")

    def rmdirfun(path1): # rmdir function
        import os
        try:
            os.rmdir(path1)
            print("Directory has been removed successfully")
        except OSError as error:
            print(error)
            print("Directory can not be removed")
  
    def clearfun(): # clear function
        print('\n'*300)

    def datefun(): # data function
        import datetime
        now = datetime.datetime.now()
        print(now)


    def echofun(paragraph): # echo function
        chars = []
        str = ""
        commands = True
        while commands == True:
            chars.clear()
            command = paragraph
            chars[:0] = command
            if chars[0] == "e" and chars[1] == "c" and chars[2] == "h" and chars[3] == "o" and  chars[4] == " ":
                chars.remove("e")
                chars.remove("c")
                chars.remove("h")
                chars.remove("o")
                chars.remove(" ")
                str = "".join(chars)
                print(str)
                commands=False

    def cat1fun(path1): # cat 1 function
        file_Data = file_Data2 = ""
        lines = []
        with open(path1) as f:
            lines = f.readlines()
        for line in lines:
            print(f'{line}')

    def cat2fun(path1,path2): # cat 2 function
        file_Data = file_Data2 = ""
        with open(path1) as fp:
            file_Data = fp.readlines()
        with open(path2) as fp:
            file_Data2 = fp.readlines()
        file_Data += file_Data2
        for line in file_Data:
            print(f'{line}')

    def appendfun(path1): # append function >>
        string = input("enter your string  ")
        with open(path1, 'a') as f:
            print(string, file=f)
        print("\nappend done!\n")
        while True:
            print("Do you like to print the file ? (y/n): ")
            check = input()
            if check == 'n':
                break
            elif check == 'y':
                file = open(path1, "r")
                print("\nHere follows the file content:\n")
                print(file.read())
                file.close()
                print()
                break
            else:
                continue

    def replacefun(path1): # replace function >
        string = input("enter your string  ")
        with open(path1, 'w') as f:
            print(string , file=f)
        print("\nreplace done!\n")
        while True:
            print("Do you like to print the file ? (y/n): ")
            check = input()
            if check == 'n':
                break
            elif check == 'y':
                file = open(path1, "r")
                print("\nHere follows the file content:\n")
                print(file.read())
                file.close()
                print()
                break
            else:
                continue

    def morefun(path1):    # more function
        # Importing required modules
        import tkinter as tk
        import tkinter.scrolledtext as st
        # Creating tkinter window
        win = tk.Tk()
        win.title("ScrolledText Widget")
        # Title Label
        tk.Label(win, text = "ScrolledText Widget", font = ("Times New Roman", 15), background = 'green', foreground = "white").grid(column = 0,row = 0)
        # Creating scrolled text area
        # widget with Read only by
        # disabling the state
        text_area = st.ScrolledText(win,width = 30, height = 8, font = ("Times New Roman",15))
        text_area.grid(column = 0, pady = 10, padx = 10)
        # Inserting Text which is read only
        file = open(path1, "r")
        text_area.insert(tk.INSERT,file.read())
        # Making the text read only
        text_area.configure(state ='disabled')
        win.mainloop()

#commands call
check = True
while check :
    t1 = Terminal

    # take input
    paragraph = input('$')
    count = paragraph.count(' ')
    if count==0 :
        command = paragraph
    elif count==1 :
        command,path1 = paragraph.split(' ')
    elif count==2 :
        command,path1,path2 = paragraph.split(' ')
    elif count==3 :
        command,path1,path2,signal = paragraph.split(' ')

    #command pwd call
    if command == 'pwd':
        t1.pwdfun()  
        check = False

    #command cd call 
    elif command == 'cd':
        t1.cdfun(path1)
        check = False

    #command ls call
    elif command == 'ls':
        t1.lsfun(path1)
        check = False

    #command cp call
    elif command == 'cp':
        t1.cpfun(path1,path2)
        check = False

    #command mv call
    elif command == 'mv':
        t1.mvfun(path1,path2)
        check = False
    
    #command rm call
    elif command == 'rm' and count==1:
        t1.rm1fun(path1)
        check = False
    elif command == 'rm' and count==2:
        if path1=="-r":
            t1.rm2fun(path2)
            check = False
        else:
            t1.rm3fun(path1,path2)
            check = False

    #command mkdir call
    elif command == 'mkdir':
        t1.mkdirfun(path1)
        check = False  

    #command rmdir call  
    elif command == 'rmdir':
        t1.rmdirfun(path1)
        check = False

    #command clear call
    elif command == 'clear':
        t1.clearfun()
        check = False

    #command data call
    elif command == 'date':
        t1.datefun()
        check = False

    #command cat call
    elif command == 'cat' and count==1:
        t1.cat1fun(path1)
        check = False
    elif command == 'cat' and count==2:
        t1.cat2fun(path1,path2)
        check = False

    #command >> call    
    elif command == 'ls>>':
        t1.appendfun(path1)
        check = False  

    #command > call 
    elif command == 'ls>':
        t1.replacefun(path1)
        check = False

    #command echo call
    elif command == 'echo' and count==1:
        t1.echofun(paragraph)
        check = False  

    #command more call
    elif command == 'more':
        t1.morefun(path1)
        check = False  

    # user enter invalid input    
    else :
        print(" invald command name........try again ") 
        check = True 
    
        
        
    


    



    

