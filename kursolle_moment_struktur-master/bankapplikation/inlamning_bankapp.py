import tkinter as tk

bal_global = str(0)

def balance():
    master = tk.Tk()

    tk.Label(master, text=bal_global).grid(row=2)

    master.mainloop()

def pw_check(name, pasword):
    global bal_global
    with open (str(name)+".txt", "r") as file:
        pword = file.readline()
        print(pword)
        if pword.strip() == pasword:
            bal_global = file_open_login(name)
            balance()
        else:
            exit()
        file.close()

def file_open_signup(name, pasword, balance):
    with open (str(name)+".txt", "w+") as file:
        file.write(str(pasword) + "\n" + str(balance))
        file.close()

def file_open_login(name):
    with open (str(name)+".txt", "r") as file:
        bal = file.readlines()[1:]
        return bal

def login():
    master = tk.Tk()
    tk.Label(master, text="Username: ").grid(row=0)
    tk.Label(master, text="Pasword: ").grid(row=1)
    
    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    
    def pw_check_local():
        name_1 = e1.get()
        pasword_2 = e2.get()
        pw_check(name_1, pasword_2)
    
    e3 = tk.Button(master, width="10", command= lambda: pw_check_local())
    
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)

    master.mainloop()

def signup():
    master = tk.Tk()
    tk.Label(master, text="Username").grid(row=0)
    tk.Label(master, text="Pasword").grid(row=1)
    tk.Label(master, text="bal: ").grid(row=2)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    
    def file_open_signup_local():
        name_1 = e1.get()
        pasword_2 = e2.get()
        balance_3 = e3.get()
        file_open_signup(name_1, pasword_2, balance_3)
        
        
    
    e4 = tk.Button(master, width="10", command= lambda: file_open_signup_local())

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)

    master.mainloop()

master = tk.Tk()
tk.Label(master, text="Log in").grid(row=0)
tk.Label(master, text="Sign up").grid(row=1)

e1 = tk.Button(master, width="10", command=login)
e2 = tk.Button(master, width="10", command=signup)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


master.mainloop()

