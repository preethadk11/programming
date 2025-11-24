words=["apple","banana","cherry","date"]
vowel=set(("aeiou"))
for x in words:
    if x[0] in vowel:
        print(x)
