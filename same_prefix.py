x = ['xxawsssdawqweqwe', 'xxdqweqwefeasssfqawd', 'qweqwexxdawfsssasa', 'xxdpawdqweqwesssawdna', 'xxqweqwedsssawda']
answer = []
longest = []
bla = []
a = 1
b = 0
for i in range(len(x)):
    if len(x[i]) > len(longest):
        longest = x[i]
while b <= len(longest):
    for i in range(b,len(longest)):
        bla = longest[b:i+1]
        for j in range(len(x)):
            if bla in x[j]:
                c = 1
            else:
                c = 0
                break
        if (c == 1) and (len(bla) > len(answer)):
            answer = bla
    b = b + 1
print(answer)





