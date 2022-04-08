word = input("Enter a word: ")
let = input("Enter a letter: ")
count = 0
def count(word, let):
  count = 0
  for char in word:
    if let == char:
      count = count + 1
  print(count)
count(word, let)


prefixes = "JKLMNOPQ"
suffix = "ack"
for letter in prefixes:
  if letter == "O" or letter == "Q":
    letter += "u"
  print(letter + suffix)


string = input("Enter a name or pronoun: ")
print(string.lower())
print(len(string))