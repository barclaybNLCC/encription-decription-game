
messages=[]

class Message:
  cipherText=""
  clearText=""

class Actor():
  name=""
  publicKey=""
  privateKey=""

  def generateKeys():
    pass 

  def createMessage():
    msg = Message()
    #do stuff!
    messages.append(msg)

    
running=True
while running:
  print("What would you like to do?")
  print("1. Create public and private keys")
  print("2. View messages")
  print("3. Send Messages")
  print("4. Quit the Program")

  _input = input("Enter the number of your selection\n")

  if _input == "1":
     
    player = Actor()
    player.name=input("Enter your name\n")
    print("Generating Keys...")
    player.generateKeys()
    print("Public Key: " + str(player.publicKey))
    print("Public Key: " + str(player.privateKey))

  elif _input =="2": #view messages
    for message in enumerate(messages):
      print(message.text)
  elif _input =="3":
    pass  #send msg
  elif _input =="4":
    exit()