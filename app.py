import tkinter as tk
from tkinter import filedialog, Text
import os

root= tk.Tk()
apps=[]

if os.path.isfile("save.txt"):
    with open("save.txt", "r") as f:
            tempapps = f.read()
            tempapps= tempapps.split(",")
            print(tempapps)
            app=[x for x in tempapps if x.strip()]


def addApps():
    for widget in frame.winfo_children():
        widget.destroy()

    fileName= filedialog.askopenfile(initialdir="/", title="select file", filetypes=(("executables", "*.exe"), ("all file", "*.*")))
    
    apps.append(fileName.name)
    print(fileName.name)
    for app in apps:
        label= tk.Label(frame, text=app, bg="grey")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)

canvas= tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

frame= tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8,relx=0.1, rely=0.1)

openFile= tk.Button(root, text="open file", padx=10, pady=3, fg="white" ,bg="#263D42" , command=addApps)
openFile.pack()

runApps= tk.Button(root, text="Run App", padx=10, pady=3, fg="white" ,bg="#263D42", command=runApps)
runApps.pack()


for app in apps:
    label= tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open("save.txt", "w") as f:
    for app in apps:
        f.write(app + ',')