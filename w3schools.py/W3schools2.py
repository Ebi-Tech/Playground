a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
if "things" in txt:
    print("Yes, things is in txt")
    if "day" not in txt:
        print("No, 'day' not in txt")

b = "Hello, World!"
print(b[2:7])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.lower())

a = "Hello, World! "
print(a.replace(" ", ""))
print(a.replace("H", "J"))
