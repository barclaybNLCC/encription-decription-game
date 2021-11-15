#this is ben's branch

ALPHABET = 'abcdefghijklmnopqrstuvwxyz.,?:1234567890' 
file=''
aliceTargetMailBox=''
bobTargetMailBox=''
chuckTargetMailBox=''
sheet=''
plaintext=''
#An actor in our scenario()
class Actor():
  plaintext=''
  def __init__(self, privateKey, publicKey):
    self.privateKey=privateKey
    self.publicKey=publicKey
    #messages are added to an actor's message box
    self.messageBox=[]
  
  #send a message to another actor
  #put/use encrypt in the send function
  def send(self, Actor):
    ciphertext = ''
    file.append(ciphertext)
    
    if Actor==Alice:
      aliceTargetMailBox.append(file)
    elif Actor==Bob:
      bobTargetMailBox.append(file)
    elif Actor==Chuck:
      chuckTargetMailBox.append(file)
    else:
      print("Something went wrong...try again later")
    #ben



             #!!!!!open dm's needs to be made as a new function!!!!!
    
  
 
  def get_plaintext():
    plaintext = input('Please type your message ')
    return plaintext.lower()  

  #encrypt the plaintext of the message, using a keyphrase
  def encrpyt(self, keyphrase):
    for position, character in enumerate(self.plaintext):
      if character not in ALPHABET:
        ciphertext = ''
        ciphertext += character
      else:
            encrypted = (ALPHABET.index(character) + enumerate(keyphrase))
            ciphertext += ALPHABET[encrypted]
    return ciphertext
    #ethan 


  
  #decrypt the ciphertext 
  def decrypt(message,keyphrase):
    ciphertext = ''
    for position, character in enumerate(plaintext):
      if character not in ALPHABET:
        ciphertext += character
      else:
            encrypted = (ALPHABET.index(character) + int(sheet[position])) % 40
            ciphertext += ALPHABET[encrypted]
    return ciphertext
    #elisha
 
 #A message that can be sent by Actors
class Message():
  def __init__(self):
    #the encrypted cleartext
    self.ciphertext
  
    #the unencrypted original message
    self.cleartext
  


Alice=Actor("","")
Bob=Actor("","")
Chuck=Actor("","")
