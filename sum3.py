from collections import Counter
text="hello world"
counter=Counter(text.replace(" ",""))
print(dict(counter))