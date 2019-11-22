d = {'A':1,'B':2,'C':3} #DUMMY INNITIALIZATION
key = input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:",d[key])
else:
      print("Key isn't present!")