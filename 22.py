from collections import Counter
numbers=[1,2,3,2,4,1,5]
counter=Counter(numbers)
common={x:c for x, c in counter.most_common() if c>1}
print(common)