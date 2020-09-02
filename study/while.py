name = ''
while not name.strip():
     name = input('Please enter your name:')
print('Hello, {}!'.format(name))


while True:
     word = input('Please enter a word: ')
     if not word: break
     # 使用这个单词做些事情
     print('The word was ', word)
