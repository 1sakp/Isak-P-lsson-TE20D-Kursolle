import tkinter as tk

def pw_check(name, pasword):
    global check
    name_l = name
    with open (str(name_l)+".txt", "r") as file:
        pword = file.readline()
        if pword == pasword:
            check = True
        else:
            check = False
        file.close()

def file_open_signup(name, pasword, balance):
    name_l = name
    with open (str(name_l)+".txt", "w+") as file:
        file.write(str(pasword) + "\n" + str(balance))
        file.close()

def login():
    master = tk.Tk()
    tk.Label(master, text="Username").grid(row=0)
    tk.Label(master, text="Pasword").grid(row=1)
    tk.Label(master, text="bal: ").grid(row=2)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    master.mainloop()

def signup():
    
    master = tk.Tk()
    tk.Label(master, text="Username").grid(row=0)
    tk.Label(master, text="Pasword").grid(row=1)
    tk.Label(master, text="bal: ").grid(row=2)

    e1 = tk.Entry(master)
    e2 = tk.Entry(master)
    e3 = tk.Entry(master)
    e4 = tk.Button(master, width="10", command= lambda: file_open_signup(e1, e2, e3))

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

