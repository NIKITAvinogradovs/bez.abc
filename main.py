text = input("Ievadi tekstu: ")#ievadam tekstu
def deleteCombo(text): #daram funkciju ar tekstu
  if text.count("abc")>0:#skatamies vai ir abc kombinacija
   text = text.replace("abc","") #mainam abc uz neko
   print(text) #rakstam teksty bez abc
  else:# ja teksta nav abc
    text = "nav vajadzigas kombinacijas" #mainam tekstu uz šo
    print(text)#rakstam tekstu kurš bija 7 rinda
  return text #atgriežam vērtibu teksts
deleteCombo(text)#arguments = teksts

