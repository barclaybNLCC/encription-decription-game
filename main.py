#this is ben's branch
#test

#An actor in our scenario()
class Actor():
  def __init__(self, privateKey, publicKey):
    self.privateKey=privateKey
    self.publicKey=publicKey
    #messages are added to an actor's message box
    self.messageBox=[]
  
  #send a message to another actor
  #put/use encrypt in the send function
  def send(self, Actor):
    
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
    
def modularInv(a,b):
  gcd, x, y = egcd(a, b)

  if x<0:
    x+=m
  return x

def encrypt(PublicKey, RSAMod, msg):
  cipher=""

  for c in msg:
    m=ord(c)
    cipher+=str(pow(m, PublicKey, RSAMod)) +" "
  return cipher

def decrypt(PrivateKey, RSAMod, cipher):
  msg=""

  parts = cipher.split()
  for part in parts:
    if part:
      c = int(part)
      msg+=chr(pow(c, PrivateKey, RSAMod))

  return msg

def main():
  p=11
  q=13
  #RSA Modulous
  RSAMod=p*q
  phiN=(p-1)*(q-1)

  PublicKey=13
  PrivateKey=modularInv(PublicKey,phiN)

  msg="This is a secret message."

  encrypted=encrypt(PublicKey, RSAMod, msg)
  decrypted=decrypt(PrivateKey, RSAMod, encrypted)

  print(f"Message: {msg}")
  print(f"PublicKey: {PublicKey}")
  print(f"PrivateKey: {PrivateKey}")
  print(f"RSAMod: {RSAMod}")
  print(f"enc: {encrypted}")
  print(f"dec: {decrypted}")
main()

  def get_plaintext():
    plaintext = input('Please type your message ')
    return plaintext.lower()  

  
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
