
def get_min(a,b):

    if a>b :
        return b
    else :
        return a

def get_gcd(a, b):

    min_value = get_min(a,b)
    for i in range(min_value , 0 ,-1):
        if a % i == 0 and b % i == 0:
            return i
        

# 直接このファイルを実行したときだけ動くブロック
#if __name__ == "__main__":
#    a = int(input("a: "))
#    b = int(input("b: "))
#    gcd = get_gcd(a, b)
#    print(gcd)
