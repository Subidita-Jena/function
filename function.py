string = "mississippi"

count = {}
for x in string:
    if x in count.keys():
        count[x]+=1
    else:
        count[x] = 1

print(count)