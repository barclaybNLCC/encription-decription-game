#que
que=[]
server = []
if not server:
    pass
else:que.append(server)

#send
def send(reciever, cipher):
  server.append(cipher)
  cipher = cipher.pop(0)
  reciever.append(server)
  server = server.pop(0)

#delete
def delete(reciever):
 print("If you would like to go to the home screen then type 0 and press enter")
 answer=input("Would you like to send a message?Y/N\n")
 if answer=="Y":
   reciever.pop(0)
 elif answer=="0":
   choice=='0'
 else:
    pass