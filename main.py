from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

print("test")

#An actor in our scenario
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

print("hello world")
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = private_key.public_key()

print(private_key)
print(public_key)
print(dir(public_key))
print("hello world")