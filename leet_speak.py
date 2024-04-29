leet_speak = {"a": "@",
   "A": "4",
   "B": "8",
   "b": "8",
   "E": "3",
   "e": "3",
   "I": "!",
   "i": "!",
   "L": "1",
  "l": "1",
  "O": "0",
  "o": "0",
  "S": "5",
  "s": "5"
  }
 
def convert(text: str) -> str:
    new_word = ""
    for char in text:
        if char in leet_speak:
            new_word += leet_speak[char]
    return new_word
            
print(convert("ABbEeIiLlOoSs"))
    
