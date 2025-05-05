message=input('enter the message:')
word=message.split(" ")

em={":-)":"😊"}
output=('')

for words in word:

    output=output+ em.get(words,words)
print(output)
    


