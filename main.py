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
print("If you would like to go to the home screen then type 0 and press enter")
  answer=input("Would you like to send a message?")