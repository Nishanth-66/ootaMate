def main():
    s2 = '''hello world
good morning
have a good day'''
    print(s2)

    s1 = "python"
    s2 = "python"
    print(s1, id(s1))
    print(s2, id(s2))
    print(s1 is s2)

    s1 = "python"
    s2 = "Python"
    print(s1, id(s1))
    print(s2, id(s2))
    print(s1 is s2)

    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print(a is b) #true
    print(a is c) #false
    print(a == c) #true

    s1 = "True" #string
    res = bool(s1) # t/f
    print(s1) # true
    print(type(res))

    s1 = "" #string
    res = bool(s1) # t/f
    print(s1) # true
    print(type(res))


if __name__ == '__main__':
    main()
