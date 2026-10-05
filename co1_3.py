s=input("enter a sentence:")
print(s)
wordslist=s.split()
print(wordslist)
uniquewords=set(wordslist)
for word in uniquewords:
    print(f"{word}occurs{wordslist.count(word)}times")
