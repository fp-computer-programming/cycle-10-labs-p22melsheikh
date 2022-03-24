# MEE 03/23/22

def num(lst):
    ans = []
    for x in lst:
        if(x > 500):
            break
        elif x % 5 == 0 and x <= 150:
            ans.append(x)
    return ans


print(num([20, 40, 150, 60, 75, 160, 25, 602, 251]))