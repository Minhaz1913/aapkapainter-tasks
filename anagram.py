str1 = input("Enter the First String  = ").lower()
str2 = input("Enter the Second String = ").lower()
if(sorted(str1) == sorted(str2)):
    print("Yes")
else:
    print("No")