import random











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
    purple = '\033[35m'
messages=[]
actors = []

class Message:
  cipherText=""
  clearText=""

class Actor():

  def __init__(self, name,e,d,N):
    self.name=name
    self.generateKeys()
    self.publicKey=e
    self.privateKey=d
    self.N=N

  def encrypt(e, N, msg):
    cipher=""

    for c in msg:
      m=ord(c)
      cipher+=str(pow(m, e, N)) +" "
    return cipher

  def decrypt(d, N, cipher):
    msg=""

    parts = cipher.split()
    for part in parts:
      if part:
        c = int(part)
        msg+=chr(pow(c, d, N))

    return msg

  def rabinMiller(self, n,c):
    global d
    a=random.randint(2,(n-2)-2)
    x=pow(a,d,n)
    if x==1 or x==n-1:
      return True

    while d != n-1:
      x=pow(x,2,n)
      d*=2

      if x==1:
        return False
      elif x==n-1:
        return True

    return False

  def isPrime(n):
    if n<2:
      return False
    
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    
    if n in lowPrimes:
      return True

    for prime in lowPrimes:
      if n % prime == 0:
        return False

    c=n-1
    while c%2 ==0:
      c/=2

    for i in range(128):
      if not self.rabinMiller(n,c):
        return False

    return True
    
  def generateKeys(self,keysize) -> (str,str): #returns tuple of public and private 
      global d
      e=d=N=0

      #get prime numbers p & q
      p=generateLargePrime(keysize)
      q=generateLargePrime(keysize)

      N=p*q #RSA Modulous
      phiN=(p-1)*(q-1) #totient

      #choose e
      #e is coprime with phiN & 1<e<=phiN
      while True:
        e=random.randrange(2 ** (keysize-1), 2 ** keysize-1)
        if(isCoPrime(e,phiN)):
          break

      #choose d
      #d is mod inv of e with respect to phiN, e*d(mod phiN)=1
      d=modularInv(e, phiN)

      return e,d,N  

  def generateLargePrime(self, keysize):
    while True:
      num=random.randrange(2 ** (keysize-1), 2 ** keysize-1)
      if (self.isPrime(num)):
        return num 

  def isCoPrime(p,q):
    return gcd(p,q)==1

  def gcd(p,q):
    while q:
      p,q=q,p%q
    return p

  def egcd(a,b):
    s=0; old_s=1
    t=1; old_t=0
    r=b; old_r=a

    while r != 0:
      quotient=old_r//r
      old_r, r = r, old_r - quotient * r
      old_s, s = s, old_s - quotient * s
      old_t, t = t, old_t - quotient * t
    
    #return gcd, x, y
    return old_r, old_s, old_t

  #Calculate Modular Inverese
  def modularInv(a,b):
    gcd, x, y = egcd(a, b)

    if x<0:
      x+=b
    return x
  que=[]
  def queue():
   que.append(msg)
   msg.pop(0) 
    




player=""#global access for our player 
running=True
while running:

  print("What would you like to do?")
  print("1. Create public and private keys")
  print("2. View messages")
  print("3. Send Messages")
  print("4. Quit the Program\n")

  _input = input(bcolors.BOLD +"Enter the number of your selection"+bcolors.ENDC+"\n")

  if _input == "1":
    print(bcolors.purple + 'hello' + 'bold' + bcolors.BOLD)
    print(bcolors.BOLD + bcolors.purple +  + bcolors.ENDC)
    name=input(bcolors.BOLD + bcolors.purple + "Enter your name\n" + bcolors.ENDC)
    if name in [""," "]:
      print("Please enter a name\n")
    else:

      print(bcolors.OKGREEN+"Generating Keys..."+ bcolors.ENDC + "\n")
      e,d,N=player.generateKeys(10)
      player = Actor(name,e,d,N)
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

      msg=input("Enter your message:\n")



      cipher=encrypt(e, N, msg)

      keySelection = input("Enter your encryption key:\n")
      
      player.createMessage()

  elif _input =="4":
    exit()