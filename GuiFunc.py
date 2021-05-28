import os
import sys
import subprocess
import tkinter as tk

def update_listbox(lbox,searchtxt):
  lbox.delete(0,tk.END)
  lbox.insert(0,searchtxt)
  

def pip_list():
  result=subprocess.run("pip list",shell=True,capture_output=True)
  packages=[]
  for s in result.stdout.decode().split("\n")[2:-1]:
    packages.append(s.split(" ")[0])
  return packages

def pip_install(packname,outputText):
  outputText.delete("1.0","end")
  pn=['echo y | pip3 install '+packname]
  result=subprocess.run(pn,shell=True,capture_output=True)
  if(result.stderr.decode()==""):
    for s in result.stdout.decode():
      outputText.insert(tk.END,s)
  else:
    for s in result.stderr.decode():
      outputText.insert(tk.END,s)
def pip_install_req():
  pn=['echo y | pip3 install '+packname]
  result=subprocess.run(pn,shell=True,capture_output=True)
  if(result.stderr.decode()==""):
    for s in result.stdout.decode():
      outputText.insert(tk.END,s)
  else:
    for s in result.stderr.decode():
      outputText.insert(tk.END,s)
      
def pip_uninstall(packname,outputText):
  outputText.delete("1.0","end")
  if(len(packname[0])>2):
    pn=['echo y | pip3 uninstall '+packname[0]]
  else:
    pn=['echo y | pip3 uninstall '+packname]
  pn=['echo y | pip3 uninstall '+packname]
  result=subprocess.run(pn,shell=True,capture_output=True)
  #result=subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall',pn])
  
  if(result.stderr.decode()==""):
    for s in result.stdout.decode():
      outputText.insert(tk.END,s)
  else:
    for s in result.stderr.decode():
      outputText.insert(tk.END,s)
      
def pip_show(packname,outputText):
  outputText.delete("1.0","end")
  if(len(packname[0])>2):
    pn="pip3 show "+packname[0]
  else:
    pn="pip3 show "+packname
  result=subprocess.run(pn,shell=True,capture_output=True)
  print(result.stderr.decode())
  if(result.stderr.decode()==""):
    for s in result.stdout.decode():
      outputText.insert(tk.END,s)
  else:
    for s in result.stderr.decode():
      outputText.insert(tk.END,s)

def pip_freeze():
  pass
