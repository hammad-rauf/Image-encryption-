import prime
import calPublicKey
import calPrivateKey

#def power(x, y, p) :
#    res = 1     # Initialize result

#    # Update x if it is more
#    # than or equal to p
#    x = x % p 
 
#    while (y > 0) :
         
#        # If y is odd, multiply
#        # x with result
#        if ((y & 1) == 1) :
#            res = (res * x) % p
 
#        # y must be even now
#        y = y >> 1      # y = y/2
#        x = (x * x) % p
         
#    return res
#def power(x, y, z):
#    "Calculate (x ** y) % z efficiently."
#    number = 1
#    while y:
#        if y & 1:
#            number = number * x % z
#        y >>= 1
#        x = x * x % z
#    return number

#def power(x,y,p):

#    res = 1
 
#    x = x % p 

 
#    while (y > 0):

#        if (y & 1):
#            res = (res*x) % p

#        y = y >>1;
#        x = (x*x) % p

#    return res

def power(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y
class rsa:
    def __init__(self):
        self.p,self.q=prime.gen_prime() #step 1 get prime numbers
        #step 2 cal n
        self.n=self.p*self.q
        #step 3 cal totient of n
        self.phi=(self.p-1)*(self.q-1)
        #step 4 cal public key e
        self.e=calPublicKey.cal(self.phi,self.n)
        #step 5 cal private key d
        self.d=calPrivateKey.cal(self.e,self.phi)

    def Cipher(self,x):
         return (power(x,self.e,self.n))
    def deCipher(self,x):
        return (power(x,self.d,self.n))