user_password = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123" }
oddelovac = "-"*30

meno = input("username: ")
heslo = input("password: ")
print(oddelovac)

if heslo == user_password.get(meno):

  print(f"Welcome to the app {meno} ")
  print("We have 3 texts to be analyzed")

else:
  print("Wrong password")
  exit()

print(oddelovac)

try:
  c_textu = int(input("Enter a number between 1 and 3 to select the text you wish to analyze: "))-1

except ValueError:
  print("Unvalid Entry: ValueError")
  exit()
else:
  if c_textu > 2 or c_textu < 0 :
    print("Unvalid entry: Number out od range")
    exit()
  else:
    print(f"Let's have a look at the text n# {c_textu+1}")
print(oddelovac)

from texty import texts


my_text= (texts[c_textu]).split()
pocet_slov = len(my_text)
pocet_title = 0
pocet_upper = 0
pocet_lower = 0
pocet_numeric = 0
cisla = []
for i in my_text:
  if i.isupper():
    pocet_upper += 1
  elif i.islower():
    pocet_lower += 1
  elif i.istitle():
    pocet_title += 1
  elif i.isnumeric():
    pocet_numeric += 1
    cisla.append(int(i))

print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {pocet_title} titlecase words.")
print(f"There are {pocet_upper} uppercase words.")
print(f"There are {pocet_lower} lowercase words.")
print(f"There are {pocet_numeric} numeric strings.")
print(f"The sum of all the numbers is: {sum(cisla)} ")
print(oddelovac)


len_list= []
for j in my_text:
  len_list.append(len(j))

slovnik_cetnosti = {}
while len_list:
  cislo = len_list.pop(0)
  if cislo in slovnik_cetnosti:
    slovnik_cetnosti[cislo] += 1
  else:
    slovnik_cetnosti[cislo] = 1

print("LEN|     OCCURENCES       | NR.")
print(oddelovac)

for k in sorted(slovnik_cetnosti):
 print(f"{k:3}|    {slovnik_cetnosti.get(k)*'*':15}   |{slovnik_cetnosti.get(k):2}")



