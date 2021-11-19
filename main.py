class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKRED = '\033[31m'
    Magenta = '\033[35'

messages=[]
actors = []

class Message:
  cipherText=""
  clearText=""

class Actor():

  def __init__(self, name):
    self.name=name
    self.generateKeys()
    self.publicKey="TODO implement public key gen"
    self.privateKey="TODO implemetn private key gen"

  def generateKeys(self) -> (str,str): #returns tuple of public and private keys
    pass 

  def createMessage(self):
    msg = Message()
    #do stuff!
    messages.append(msg)




player=""#global access for our player 
running=True
while running:

  print("What would you like to do?")
  print("1. Create public and private keys")
  print("2. View messages")
  print("3. Send Messages")
  print("4. Quit the Program\n")

  _input = input(bcolors.BOLD+"Enter the number of your selection"+bcolors.ENDC+"\n")

  if _input == "1":
     
    
    name=input(bcolors.BOLD.Magenta + "Enter your name\n" + bcolors.ENDC)
    if name in [""," "]:
      print("Please enter a name\n")
    else:
      player = Actor(name)
      print(bcolors.OKGREEN+"Generating Keys..."+ bcolors.ENDC + "\n")
      player.generateKeys()
      print("Public Key: " + str(player.publicKey))
      print("Public Key: " + str(player.privateKey))

  elif _input =="2": #view messages
    if type(player)!= type(Actor):
      print(bcolors.WARNING + "You must first create your public and private keys" + bcolors.ENDC + "\n")
    else:
      for message in enumerate(messages):
        print(message.text)

  elif _input =="3": #send msg
    if type(player)!= type(Actor):
      print(bcolors.OKRED+ "You must first create your public and private keys" + bcolors.ENDC + "\n")
    else:

      cleartext=input("Enter your message:\n")

      #for actor in enumerate(activeActor):
        
      keySelection = input("Enter your encryption key:\n")
      
      player.createMessage()

  elif _input =="4":
    exit()