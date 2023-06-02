#Import Libs
from tkinter import *
import time
import os

#Create Window
main = Tk()
main.title("Roof Duck Folder (*rdf) Writer GUI")

#Commands
def application_exit():
    #Create dialogue
    conf = Tk()
    conf.title("RDF Writer Dialogue")
    #disable main window
    main.disabled = True

    #Commands
    def btn_ok():
        main.destroy()
        conf.destroy()
        quit()

    def btn_cancel():
        main.disabled = False
        conf.destroy()

    #Create UserForm Components
    lbl_info = Label(conf, text="Quit? Unsaved *rdf files will be deleted.")
    btn_ok = Button(conf, text="OK", command=btn_ok)
    btn_cancel = Button(conf, text="Cancel", command=btn_cancel)

    #Render UserForm Components
    lbl_info.grid(column=1, row=0)
    btn_ok.grid(column=0, row=1)
    btn_cancel.grid(column=2, row=1)

    

def rdf_create():
    #Retrieve paths as variables
    rdfpth = ebxrdf.get()
    pth0 = ebxpth0.get()
    pth1 = ebxpth1.get()
    pth2 = ebxpth2.get()
    pth3 = ebxpth3.get()
    pth4 = ebxpth4.get()

    #Create rdf file
    with open(rdfpth, 'a') as pth:
        pth.write("%s\n%s\n%s\n%s\n%s\nCreated by RDFWriter at %s"%(pth0, pth1, pth2, pth3, pth4, time.ctime()))

def rdf_delete():
    #Create Window
    delconf = Tk()
    delconf.title("RDF Writer Dialogue")
    main.disabled = True

    #Commands
    def btn_yes():
        pth = ebxrdf.get()
        if ".rdf" in pth:
            try:
                os.remove(pth)
            except FileNotFoundError:
                print("File Not Found")
        else:
            print("Must be *rdf file.")

        main.disabled = False
        delconf.destroy()

    def btn_no():
        main.disabled = False
        delconf.destroy()
        

    #Create UserForm Components
    lblinfo = Label(delconf, text="Delete specified *rdf file? This cannot be undone.")

    btnyes = Button(delconf, text="Yes", command=btn_yes)

    btnno = Button(delconf, text="No", command=btn_no)

    #Render UserForm Components
    lblinfo.grid(column=1, row=0)

    btnyes.grid(column=0, row=1)

    btnno.grid(column=2, row=1)
        
        

#Create UserForm Components
ebxrdf = Entry(main)
lblrdf = Label(main, text="Location and name of new *rdf file (include file extension):")

ebxpth0 = Entry(main)
lblpth0 = Label(main, text="Path 1:")

ebxpth1 = Entry(main)
lblpth1 = Label(main, text="Path 2 (optional):")

ebxpth2 = Entry(main)
lblpth2 = Label(main, text="Path 3 (optional):")

ebxpth3 = Entry(main)
lblpth3 = Label(main, text="Path 4 (optional):")

ebxpth4 = Entry(main)
lblpth4 = Label(main, text="Path 5 (optional):")

btncreate = Button(main, text="Create *rdf file", command=rdf_create)

btnexit = Button(main, text="Exit", command=application_exit)

btndeleterdf = Button(main, text="Delete specified *rdf file", command=rdf_delete)

#Render UserForm Components
ebxrdf.grid(column=0, row=1)
lblrdf.grid(column=0, row=0)

lblpth0.grid(column=0, row=2)
ebxpth0.grid(column=0, row=3)

lblpth1.grid(column=0, row=4)
ebxpth1.grid(column=0, row=5)

lblpth2.grid(column=0, row=6)
ebxpth2.grid(column=0, row=7)

lblpth3.grid(column=0, row=8)
ebxpth3.grid(column=0, row=9)

lblpth4.grid(column=0, row=10)
ebxpth4.grid(column=0, row=11)

btncreate.grid(column=1, row=11)

btnexit.grid(column=1, row=0)

btndeleterdf.grid(column=1, row=5)
