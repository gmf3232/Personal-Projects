# George Fisk Project 1
# Section 003

class Random:
    def __init__(self, seed):
        self.seed = seed

    def nextOne(self, ranger):
        k = ((7**5)*self.seed)%((2**(31))-1) # Park-Miller Algorithm
        self.seed = k  # resets seed for new iteration
        result = k % ranger # to return a value within the desired range
        return result

    def choose(self, objects):
        index = self.nextOne(len(objects))   #random index
        return objects[index]       

class Nonce:
    def __init__(self, seed):
        self.first = []
        self.follow = {}
        self.random = Random(seed)

    def add(self, word):
        i = 0
        while i < len(word):
            if i == 0:      #then we have a letter that belongs in first
                self.first.append(word[i])   
                i += 1
            else:
                c = word[i-1]     # assign letter to be followed
                letter = word[i]
                if self.follow.has_key(c):   # if key is already in follow
                    self.follow[c].append(letter)
                else:                    # make a new key
                    self.follow[c] = [letter]
                i += 1

    def make(self, size):
        word = ""  
        first_letter = self.random.choose(self.first)  #choose random first letter
        word += first_letter
        i = 1
        while i < size:
            if self.follow.has_key(word[i-1]):   # if letter to be followed has a key in dictionary follow
                key = word[i-1]
                c = self.random.choose(self.follow[key])
                word += c
                i += 1
            else:
                c = self.random.choose(self.first)
                word += c
                i += 1

        return word


nw = Nonce(123)  
nw.add('ada')  
nw.add('algol')  
nw.add('bliss')  
nw.add('ceylon')  
nw.add('clojure')  
nw.add('curl')  
nw.add('dart')  
nw.add('eiffel')  
nw.add('elephant')  
nw.add('elisp')  
nw.add('falcon')  
nw.add('fortran')  
nw.add('go')  
nw.add('groovy')  
nw.add('haskell')  
nw.add('heron')  
nw.add('intercal')  
nw.add('java')  
nw.add('javascript')  
nw.add('latex')  
nw.add('lisp')  
nw.add('mathematica')  
nw.add('nice')  
nw.add('oak')  
nw.add('occam')  
nw.add('orson')  
nw.add('pascal')  
nw.add('postscript')  
nw.add('prolog')  
nw.add('python')  
nw.add('ruby')  
nw.add('scala')  
nw.add('scheme')  
nw.add('self')  
nw.add('snobol')  
nw.add('swift')  
nw.add('tex')  
nw.add('wolfram')   
            
i = 0
while i < 20: # prints 6 letter and 9 letter Nonce words with a given seed. Always gives same sequence of words for each seed, but gives new words for different seeds.
    print nw.make(6) # prints words 'osthak', 'jalada', 'hemada', 'caliso', etc.
    print nw.make(9) # prints 'javythali', 'exeladath', 'pasthante', etc.
    i += 1

nw = Nonce(2962)
nw.add('aaaaaaa')
i = 0
while i < 20:
    print nw.make(1) # prints 'a' for each iteration
    print nw.make(3) # prints 'aaa' for each iteration
    print nw.make(5) # prints 'aaaaa' for each iteration
    i += 1

nw = Nonce(20106)
nw.add('xyz')
nw.add('xyz')
i = 0
while i < 20:
    print nw.make(1) # always prints 'x'
    print nw.make(2) # always prints 'xy'
    print nw.make(3) # always prints 'xyz'
    print nw.make(4) # always prints 'xyzx'
    i += 1







            




        
        

                    
        
