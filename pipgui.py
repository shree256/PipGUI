import tkinter as tk
from GuiFunc import *
import os
import subprocess
from tkinter import filedialog


def main():
  root=tk.Tk()
  root.geometry("650x300")

  def upgrade_pip():
    os.chdir("/home/dragonfly/.virtualenvs/django_env/bin/")
    r=subprocess.run(['python -m pip install --upgrade pip'],shell=True,capture_output=True)
    if(r.stderr.decode()==""):
      for s in r.stdout.decode():
        outputText.insert(tk.END,s)
    else:
      for s in r.stderr.decode():
        outputText.insert(tk.END,s)
        
  menubar = tk.Menu(root)  
  menubar.add_command(label="upgrade",command=upgrade_pip)

  leftFrame=tk.Frame(root)
  leftFrame.pack(side=tk.LEFT,fill=tk.BOTH,expand=tk.TRUE)

  rightFrame=tk.Frame(root)
  rightFrame.pack(side=tk.RIGHT,fill=tk.BOTH,expand=tk.TRUE)
  
  ##############################################################RightFrame
  
  #install new packages
  inspackFrame=tk.Frame(rightFrame)
  inspackFrame.pack(side=tk.TOP,fill=tk.BOTH,expand=tk.TRUE,padx=2,pady=2)
  
  pknameLabel=tk.Label(inspackFrame,text="Package Name:")
  pknameLabel.pack(side=tk.LEFT)
  
  packname=tk.Entry(inspackFrame)
  packname.pack(side=tk.LEFT)

  #install from req.txt
  insreqFrame=tk.Frame(rightFrame)
  insreqFrame.pack(fill=tk.BOTH,expand=tk.TRUE,padx=2,pady=2)

  lb1=tk.Label(insreqFrame,text="-"*10+"OR"+"-"*10)
  lb1.pack(side=tk.TOP)

  def installPack():
    txt=packname.get()
    pip_install(txt,outputText)

  def btnSwitch():
    ptr=checkVal.get()
    if(ptr==1):
      fileLoc.configure(state=tk.NORMAL)
      packname.configure(state=tk.DISABLED)
    else:
      fileLoc.configure(state=tk.DISABLED)
      packname.configure(state=tk.NORMAL)
      
  checkVal=tk.IntVar()
  reqCheck = tk.Checkbutton(insreqFrame, text="requirements.txt:", variable=checkVal,command=btnSwitch)
  reqCheck.pack(side=tk.LEFT)

  def browseFiles():
    filename = tk.filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files","*.txt*"),("all files","*.*")))
    outputText.delete("1.0","end")
    outputText.insert(tk.END,filename)

  fileLoc=tk.Button(insreqFrame,text="Browse",command=browseFiles)
  fileLoc.configure(state=tk.DISABLED)
  fileLoc.pack(side=tk.LEFT)
  
  install=tk.Button(insreqFrame,text="Install",command=installPack)
  install.pack(side=tk.LEFT)

  #output window
  owFrame=tk.Frame(rightFrame)
  owFrame.pack(side=tk.BOTTOM,padx=2,pady=2)
  font=("Times New Roman", 10, "bold")
  outputText=tk.Text(owFrame,font=font)
  outputText.pack(side=tk.BOTTOM, fill = tk.BOTH)

  ###########################################################LeftFrame  
  #show installed packages
  shwFrame=tk.Frame(leftFrame)
  shwFrame.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=tk.TRUE,padx=2,pady=2)
  
  packlist = tk.Listbox(shwFrame)
  
  def refresh(): #refresh listbox items
    result=pip_list() #installed packages names
    index=0
    for s in result:
      packlist.insert(index,s.split(" "))
      index+=1

  refresh()
  
  packlist.pack(side=tk.TOP,fill=tk.BOTH,expand=tk.TRUE)


  def showDetails():
    txt=packlist.get(tk.ANCHOR)
    pip_show(txt,outputText)
    
  showDetails=tk.Button(shwFrame,text="Details",command=showDetails)
  showDetails.pack(side=tk.LEFT,fill=tk.BOTH,expand=tk.TRUE)

  def uninstallPack():
    txt=packlist.get(tk.ANCHOR)
    pip_uninstall(txt,outputText)
  
  uninstall=tk.Button(shwFrame,text="Uninstall",command=uninstallPack)
  uninstall.pack(side=tk.LEFT,fill=tk.BOTH,expand=tk.TRUE)

  #searchbox
  sbFrame=tk.Frame(leftFrame)
  sbFrame.pack(side=tk.TOP,padx=2,pady=2)

  refresh_photo=tk.PhotoImage(file=r"refresh.png")
  refresh_photo = refresh_photo.subsample(150)
  refbtn=tk.Button(sbFrame,text="R",image=refresh_photo,command=refresh)
  refbtn.pack(side=tk.LEFT)
  
  sbox=tk.Entry(sbFrame)
  sbox.pack(side=tk.LEFT)

  def search_pack():
    result=pip_list() #installed packages names
    txt=sbox.get()
    if txt in result:
      update_listbox(packlist,txt)

  search_photo=tk.PhotoImage(file=r"search.png")
  search_photo = search_photo.subsample(30)
  sbtn=tk.Button(sbFrame,text="S",image=search_photo,command=search_pack)
  sbtn.pack(side=tk.LEFT)

  photo = tk.PhotoImage(file = r"index.png")
  root.iconphoto(False, photo)

  root.title("PipGUI")
  root.config(menu=menubar)  
  root.resizable(width=False, height=False)
  root.mainloop()

if __name__ == "__main__":
  main()
