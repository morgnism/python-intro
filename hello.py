def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ").strip().title()
hello(name)
