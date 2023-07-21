a = int(input("Enter the number: "))
def print_num(n):
    if n==1:
        print(1)
        return 1
    else:
        print_num(n-1)
        print(n)
        return ""
l = print_num(a)


