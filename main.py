#An actor in our scenario()
#test
#test 
class Actor():
  def __init__(self, privateKey, publicKey):
    self.privateKey=privateKey
    self.publicKey=publicKey
    #messages are added to an actor's message box
    self.messageBox=[]
  
  #send a message to another actor
  #put/use encrypt in the send function
  def send(self, Actor):
    pass
    
  #encrypt the plaintext of the message, using a keyphrase
  def encrpyt(keyphrase):
    pass
  
  #decrypt the ciphertext 
  def decrypt(message,keyphrase):
     pass

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
