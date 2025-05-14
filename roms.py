rom = {
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
while True :
    j = 0
    ans = 0
    list = []
    num = input("enter romans numerals : ")
    num = num.upper()
    for i in num:
        rnum = rom.get(i)
        list.append(rnum)
    for i in list:
        if j == i/10 or j == i/5 :
            ans += i-j-j
            j = i
        else :
            j = i
            ans += i
    print(ans)
