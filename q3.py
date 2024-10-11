from idlelib.replace import replace

# a
text1: str = "  fun-day  "
print("  fun-day  ", "strip:", text1.strip())

# b
text2 : str = "hello"
print('"hello", text2.isalpha() :',text2.isalpha())

# c
text3 : str = "777"
print('"777", text3.isdigit(): ', text3.isdigit())

# d
text4 : str = "  "
print('"  ", text4.isspace(): ', text4.isspace())

# e
text5 = (['N', 'I', 'N', 'J', 'A'])
print("join (['N', 'I', 'N', 'J', 'A']):", "".join(text5))

# f
text6 = ['N', 'I', 'N', 'J', 'A']
print("join (['N', 'I', 'N', 'J', 'A']):", "*".join(text6))

# g
text7 = "hELLo"
print('e' in text7.lower())

# h
word_input = input("Enter a word: ")
result = [char.upper() for char in word_input if char.isalpha()]
print(result)
