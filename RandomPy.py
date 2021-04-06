import os
###################################
os.system('clear')
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])

def menu():
    print ("""
This is the liscencse so um yea dont steal""")

os.system('clear')
os.system('clear')
os.system('clear')
os.system('clear')


Logo = """\033[34m 
███████╗██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔══██╗
███████╗██████╔╝█████╗  ██║  ██║
╚════██║██╔═══╝ ██╔══╝  ██║  ██║
███████║██║     ███████╗██████╔╝
╚══════╝╚═╝     ╚══════╝╚═════╝ 
 """
def menu():
    print (Logo + """\033[1m
 This is deadass some random shit to help me with python
\033[34m
   {1}~~Faggot Option Select me!!
 """)
    choice = raw_input("StupidRandomShit~$ ")
    os.system('clear')
    if choice == "1":
       info()
    else:
       menu()

def info():
    print (Logo + "some easy testing hopefully works")
