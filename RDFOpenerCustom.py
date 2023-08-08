from tkinter import *
import subprocess
import clipboard

fopen = Tk()
fopen.title("Roof Duck Folder (*rdf) Opener")

def copy(text):
    clipboard.copy(text)

    

def exitapp():
    fopen.destroy()
    quit()

def rdfopen():
    path = rdfpathebx.get()
    with open(path) as index:
        targetpath = index.readlines()
        try:
            pth0 = targetpath[0]
            pthtrans = dict.fromkeys(map(ord, "\n"), None)
            pth0 = pth0.translate(pthtrans)
        except IndexError:
            print("No file (1)")
        

        try:
            pth1 = targetpath[1]
            pthtrans = dict.fromkeys(map(ord, "\n"), None)
            pth1 = pth1.translate(pthtrans)
        except IndexError:
            print("No file (2)")

        try:
            pth2 = targetpath[2]
            pthtrans = dict.fromkeys(map(ord, "\n"), None)
            pth2 = pth2.translate(pthtrans)
        except IndexError:
            print("No file (3)")

        try:    
            pth3 = targetpath[3]
            pthtrans = dict.fromkeys(map(ord, "\n"), None)
            pth3 = pth3.translate(pthtrans)
        except IndexError:
            print("No file (4)")

        try:
            pth4 = targetpath[4]
            pthtrans = dict.fromkeys(map(ord, "\n"), None)
            pth4 = pth4.translate(pthtrans)
        except IndexError:
            print("No file (5)")

        #print(pth0, "\n", pth1, "\n", pth2, "\n", pth3, "\n", pth4)
        print("Start View...")

        def viewindow(path):
            with open(path) as view:
                viewer = view.read()
                viewwnd = Tk()
                viewwnd.title("Open: %s" %(path))

                def viewindclose():
                    viewwnd.destroy()

                fnlbl = Label(viewwnd, text="Viewing File (%s)."%(path))
                fvlbl = Label(viewwnd, text=viewer)
                closebtn = Button(viewwnd, text="Close", command=viewindclose)

                fnlbl.grid(column=0, row=0)
                fvlbl.grid(column=0, row=1)
                closebtn.grid(column=1, row=0)


        
        try:
            with open(pth0) as view0:
                viewer0 = view0.read()
                print("File 1:\n", viewer0)
                viewindow(path=pth0)
                copy(text=pth0)
        except OSError as e1:
            print("File not present. Error %s" %(e1))
        except UnboundLocalError:
            pass
        except UnicodeDecodeError as ude1:
            print("Could not decode file. Code %s" %(ude1))

        try:
            with open(pth1) as view1:
                viewer1 = view1.read()
                print("File 2:\n", viewer1)
                viewindow(path=pth1)
                copy(text=pth1)
        except OSError as e2:
            print("File not present. Error %s" %(e2))
        except UnboundLocalError:
            pass

        try:
            with open(pth2) as view2:
                viewer2 = view2.read()
                print("File 3:\n", viewer2)
                viewindow(path=pth2)
                copy(text=pth2)
        except OSError as e3:
            print("File not present. Error %s"%(e3))
        except UnboundLocalError:
            pass

        try:
            with open(pth3) as view3:
                viewer3 = view3.read()
                print("File 4:\n", viewer3)
                viewindow(path=pth3)
                copy(text=pth3)
        except OSError as e4:
            print("File not present. Error %s"%(e4))
        except UnboundLocalError:
            pass

        try:
            with open(pth4) as view4:
                viewer4 = view4.read()
                print("File 5:\n", viewer4)
                viewindow(path=pth4)
                copy(text=pth4)
        except OSError as e5:
            print("File not present. Error %s"%(e5))
        except UnboundLocalError:
            pass

rdfpathebx = Entry(fopen)
btnsubmit = Button(fopen, text="Open RD Folder", command=rdfopen)
btnexit = Button(fopen, text="Exit", command=exitapp)

rdfpathebx.grid(column=0, row=0)
btnsubmit.grid(column=1, row=0)
btnexit.grid(column=0, row=1)
