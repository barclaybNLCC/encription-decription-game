#que
que=[]
def queue():
  que.append(msg)
  msg.pop(0)

#open message box
def openMessageBox():
  print(que)

#delete
def delete(reciever):
 print("If you would like to go to the home screen then type \"0\" and press enter")
 answer=input("Would you like to send a message?Y/N\n")
 if answer=="Y":
   reciever.pop(0)
 elif answer=="0":
   choice=='0'
 else:
    pass