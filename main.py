import tkinter as t
import tkinter.messagebox as msgbox

# TODO: Restart and pause functionality

root = t.Tk()
root.geometry('1200x675')
root.title("Vocabulary Enhancer - Main window")

icon = t.PhotoImage(file="Images/Icon.png")
root.iconphoto(False, icon)


def about():
    msgbox.showinfo("About Vocabulary Enhancer",
                    "It is a game to improve vocabulary \n\n(version-1)\n\n- Manikya Sharma\n      12-A\n   Jaspal Kaur Public School")


def play():
    import game_main


to_change = 'MAIN'


def settings():
    from tkinter import colorchooser
    import settings_change

    def show(event):
        global to_change
        cs = lb.curselection()
        for elem in cs:
            if elem == 0:
                to_change = "color"
            elif elem == 1:
                to_change = "difficulty"
            elif elem == 2:
                to_change = "default"
        if to_change == "color":
            bc1 = t.Button(f3, text="CHOOSE COLOR FOR BACKGROUND", command=change_color_b1, pady=20, font='calibri 20',
                           bg="black", fg="white", activebackground="green", activeforeground="white")
            bc1.pack()
            bc2 = t.Button(f3, text="CHOOSE COLOR FOR QUESTION", command=change_color_b2, pady=20, font='calibri 20',
                           bg="black", fg="white", activebackground="green", activeforeground="white")
            bc2.pack()
            bc3 = t.Button(f3, text="CHOOSE COLOR FOR OPTIONS", command=change_color_b3, pady=20, font='calibri 20',
                           bg="black", fg="white", activebackground="green", activeforeground="white")
            bc3.pack()
        if to_change == 'difficulty':
            t.Button(f3, text="EASY", command=change_diff_b1, pady=20, font='calibri 20', bg="black", fg="white",
                     activebackground="green", activeforeground="white").pack()
            t.Button(f3, text="MEDIUM", command=change_diff_b2, pady=20, font='calibri 20', bg="black", fg="white",
                     activebackground="green", activeforeground="white").pack()
            t.Button(f3, text="HARD", command=change_diff_b3, pady=20, font='calibri 20', bg="black", fg="white",
                     activebackground="green", activeforeground="white").pack()
        if to_change == "default":
            t.Button(f3, text="MAKE DEFAULTS", command=default, pady=20, font='calibri 20', bg="black", fg="white",
                     activebackground="green", activeforeground="white").pack()

    def change_color_b1():
        color_code = colorchooser.askcolor(title="Choose Color")
        hexa_code = color_code[0]
        if hexa_code == None:
            return
        settings_change.change_bg_color((hexa_code))

    def change_color_b2():
        color_code = colorchooser.askcolor(title="Choose Color")
        hexa_code = color_code[0]
        if hexa_code == None:
            return
        settings_change.change_q_color((hexa_code))

    def change_color_b3():
        color_code = colorchooser.askcolor(title="Choose Color")
        hexa_code = color_code[0]
        if hexa_code == None:
            return
        settings_change.change_options_color((hexa_code))

    def change_diff_b1():
        settings_change.change_difficulty("easy")
        set_root.destroy()

    def change_diff_b2():
        settings_change.change_difficulty("medium")
        set_root.destroy()

    def change_diff_b3():
        settings_change.change_difficulty("hard")
        set_root.destroy()

    def default():
        settings_change.defaults()
        set_root.destroy()

    import tkinter as t
    set_root = t.Tk()
    set_root.geometry('900x400')
    set_root.title("SETTINGS")
    f1 = t.Frame(set_root, padx=5, pady=5)
    t.Label(f1, text="SETTINGS", font='times 45 bold', fg='#1199ff', bg='black').pack(fill='x')
    t.Label(f1, text="Double Click to open side-bar", font="calibri 16 italic", fg="white", bg="black").pack(fill='x')
    f1.pack(side=t.TOP, fill='x')
    f2 = t.Frame(set_root, padx=5, pady=5)
    lb = t.Listbox(f2, height=20, bg='black', fg='white', selectbackground="#1199ff", relief=t.SUNKEN)
    lb.insert(1, "Colours")
    lb.insert(2, "Difficulty")
    lb.insert(3, "Default Settings")
    lb.bind('<Double-1>', show)
    lb.pack(fill='y')
    f2.pack(side=t.LEFT, fill='y')
    f3 = t.Frame(set_root, padx=5, pady=5)
    f3.pack()
    set_root.mainloop()


menubar = t.Menu(root)
filemenu = t.Menu(menubar, tearoff=0)
filemenu.add_command(label="Play Game", command=play)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.destroy)
menubar.add_cascade(label="Game", menu=filemenu)

filemenu2 = t.Menu(menubar, tearoff=0)
filemenu2.add_command(label="Settings", command=settings)
menubar.add_cascade(label="Configure", menu=filemenu2)

filemenu3 = t.Menu(menubar, tearoff=0)
filemenu3.add_command(label="About", command=about)
menubar.add_cascade(label="About", menu=filemenu3)

root.config(menu=menubar)

frame1 = t.Frame(root, padx=0, pady=0, bd=0, relief=t.FLAT)
t.Label(frame1, text="VOCABULARY ENHANCER", font="times 45 bold", fg="#1199ff", pady=50, bg="#000000").pack(fill="x")

frame2 = t.Frame(root, padx=0, pady=0, bd=0, relief=t.FLAT)
t.Label(frame2, text="Welcome!", font="lucidaconsole 30", bg="#000000", fg="blue").pack(fill='x')

frame3 = t.Frame(root, padx=0, pady=15, bd=0, relief=t.FLAT)

but1 = t.Button(frame3, text="PLAY", font="couriernew 40 bold", command=play, padx=50, pady=40,
                activebackground="green", activeforeground="white", bg="gray")
but1.pack()

t.Label(frame3, text="", pady=10).pack()

but2 = t.Button(frame3, text="SETTINGS", font="couriernew 40 bold", command=settings, padx=40, pady=50,
                activebackground="green", activeforeground="white", bg="gray")
but2.pack()

frame1.pack(fill='x')
frame2.pack(fill='x')
frame3.pack(fill='x')

t.mainloop()
