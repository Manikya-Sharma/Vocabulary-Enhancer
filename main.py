import tkinter as t
import tkinter.messagebox as msgbox


#TODO: 1. Add settings using listbox and manipulate game
#      2. Make the game
#      3. Restart and pause functionality

root = t.Tk()
root.geometry('1200x675')

def pause():
    pass#

def replay():
    pass#

def about():
    msgbox.showinfo("About Vocabulary Enhancer","It is a game to improve vocabulary \n\n(version-1)")

def play():
    newroot = t.Tk()
    newroot.geometry('500x100')
    t.Label(newroot,text = "PLEASE WAIT", font = 'comicsans 30 bold',bg = "#000000",fg = "#ffffff").pack(fill = 'both')
    import game_main
    newroot.destroy()

def settings():
    pass#

menubar = t.Menu(root)
filemenu = t.Menu(menubar,tearoff=0)
filemenu.add_command(label = "Pause",command = pause)
filemenu.add_command(label = "Replay",command = replay)
filemenu.add_separator()
filemenu.add_command(label = "Quit",command = root.destroy)
menubar.add_cascade(label = "Game", menu = filemenu)

filemenu2 = t.Menu(menubar, tearoff = 0)
filemenu2.add_command(label = "Settings", command = settings)
filemenu2.add_separator()
filemenu2.add_command(label = "About", command = about)
menubar.add_cascade(label = "Configure", menu = filemenu2)

root.config(menu = menubar)

frame1 = t.Frame(root, padx = 0, pady=0, bd = 0, relief=t.FLAT)
t.Label(frame1,text = "VOCABULARY ENHANCER",font = "times 45 bold", fg = "#1199ff",pady =50,bg = "#000000").pack(fill = "x")

frame2 = t.Frame(root,padx = 0, pady = 0,bd = 0,relief = t.FLAT)
t.Label(frame2,text = "Welcome!", font = "lucidaconsole 30",bg = "#000000",fg = "blue").pack(fill = 'x')

frame3 = t.Frame(root,padx = 0, pady = 15,bd = 0,relief = t.FLAT)


but1 = t.Button(frame3, text = "PLAY", font = "couriernew 40 bold", command = play,padx = 50,pady = 40, activebackground="green",activeforeground="white",bg = "gray")
but1.pack()

t.Label(frame3,text = "",pady = 10).pack()

but2 = t.Button(frame3, text = "SETTINGS", font = "couriernew 40 bold", command = settings,padx = 40,pady = 50, activebackground="green",activeforeground="white",bg = "gray")
but2.pack()


frame1.pack(fill = 'x')
frame2.pack(fill = 'x')
frame3.pack(fill = 'x')

t.mainloop()