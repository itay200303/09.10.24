
# a
text: str = "itay trauner hadera"
print('len:', len(text))

# b
print('upper:', text.upper())

# c
print('lower:', text.lower())

# d
print('start with itay?' , text.startswith('itay'))

# e
print('end with hadera?' , text.endswith('hadera'))

# f
print('split: ' , text.split())

# g
print('replace " " with *:',  text.replace(" " , '*'))
print('split : ' , text.split('*'))

# h
print('center: ',text.center(50, '='))

# i
print('[4] - [19] :',"itay trauner hadera"[4:19])

# j
print('[0] - [4] :',"itay trauner hadera"[0:4])

# k
print('zugi:', "itay trauner hadera"[::2])

# l
print('title: ', text.title())


