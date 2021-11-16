print("line1")
#this is ben's branch

ALPHABET = 'abcdefghijklmnopqrstuvwxyz.,?:1234567890' 
class Actor():
  ciphertext = ''
  plaintext=''
  def __init__(self, privateKey, publicKey):
    self.privateKey=privateKey
    self.publicKey=publicKey
    #messages are added to an actor's message box
    self.messageBox=[]
  
  #send a message to another actor
  #put/use encrypt in the send function
 
  def send():
   #send a message to another actor
   #put/use encrypt in the send function
   def sendClearText(self, actor, message):
      actor.messageBox.append(message)

   def sendEncryptedText(self, actor, message, key):
     #ciphertext=encrypt(message,key)
     #actor.messageBox.append(ciphertext)
     pass

     
  def get_plaintext():
   plaintext = input('Please type your message ')
   return plaintext.lower()  

  #encrypt the plaintext of the message, using a keyphrase
  def encrpyt(self, keyphrase):
    for position, character in enumerate(self.plaintext):
      if character not in ALPHABET:
        self.ciphertext += character
      else:
            encrypted = (ALPHABET.index(character) + enumerate(keyphrase))
            self.ciphertext += ALPHABET[encrypted]
    return self.ciphertext
    #ethan 

  
  #decrypt the ciphertext 
  def decrypt(self, message,keyphrase):
    for position, character in enumerate(self.plaintext):
      if character not in ALPHABET:
        self.ciphertext += character
      else:
            encrypted = (ALPHABET.index(character) + int(self.sheet[position])) % 40
            self.ciphertext += ALPHABET[encrypted]
    return self.ciphertext
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
