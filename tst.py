def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

s = 'ab'
b = string2bits(s)
s2 = bits2string(b)


#print '\nList of Bits:'
#for x in b:
    #print x

#print b
g = ['01100010']
g += ['01100010']

print ''.join([chr(int(x, 2)) for x in g])