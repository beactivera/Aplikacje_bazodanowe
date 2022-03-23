text = "aplikacjebazodanowe"
result = {}
  
for char in text:
    result[char] = result.get(char, 0) + 1

print (f"Count of all characters in {text} is:\n {result}")