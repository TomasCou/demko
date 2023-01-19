from tkinter import *
from tkinter import ttk

import sub1






root = Tk()
root.geometry('1280x920')
root.resizable(False, False)
root.title("GRCKA")






notebook = ttk.Notebook(root)

hraci =         Frame(notebook)
skupiny =       Frame(notebook)
pavouk =        Frame(notebook)
hraciStats =    Frame(notebook)

notebook.add(hraci, text="  Hráči  ")
notebook.add(skupiny, text="  Skupiny  ")
notebook.add(pavouk, text="  Playoff  ")
notebook.add(hraciStats, text="  Statistika Hráčů  ")
notebook.pack(expand=True, fill="both", pady=5, padx=10)







scrolableFramesVar = [] # all scrolable frames stored here








def _on_mouse_wheel(event):
    for i in range(len(scrolableFramesVar)):
        scrolableFramesVar[i].my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


def addbtns ():

    scrolableFramesVar.insert(0,sub1.createScrolableFrame(hraci, 'frameScrolableHraci'))
    for i in range(200):
        for x in range(3):
            bt = Button(scrolableFramesVar[0].scrolableFrame, text=f"Btn number {(i + 1) * (x + 1)}", padx=2, pady=2)
            bt.grid(column=x, row=i, pady=10, padx=10)

    for i in range(len(scrolableFramesVar)):
        scrolableFramesVar[i].my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)







hraciMenuMainFrame = LabelFrame(hraci, pady=10, padx=10 ,width=1800)
hraciMenuMainFrame.pack(pady=10, padx=10, anchor=CENTER)

add = Button(hraciMenuMainFrame, text= "asd", comman= addbtns , width=20)
add.grid(column=0, row=0,padx= 10)




def addbtns2 ():

    scrolableFramesVar.insert(0,sub1.createScrolableFrame(skupiny, 'frameScrolableHraci'))
    for i in range(200):
        for x in range(3):
            bt = Button(scrolableFramesVar[0].scrolableFrame, text=f"Btn number {(i + 1) * (x + 1)}", padx=2, pady=2)
            bt.grid(column=x, row=i, pady=10, padx=10)

    for i in range(len(scrolableFramesVar)):
        scrolableFramesVar[i].my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)


hraciMenuMainFrame = LabelFrame(skupiny, pady=10, padx=10 ,width=1800)
hraciMenuMainFrame.pack(pady=10, padx=10, anchor=CENTER)

add = Button(hraciMenuMainFrame, text= "asd", comman= addbtns2 , width=20)
add.grid(column=0, row=0,padx= 10)






root.mainloop()


