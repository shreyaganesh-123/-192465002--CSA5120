text=input("TEXT: ").upper(); K=[[3,3],[2,5]]
if len(text)%2: text+="X"
r=""
for i in range(0,len(text),2):
    a,b=ord(text[i])-65, ord(text[i+1])-65
    x=(a*K[0][0]+b*K[0][1])%26
    y=(a*K[1][0]+b*K[1][1])%26
    r+=chr(x+65)+chr(y+65)
print("Encrypted:", r)
