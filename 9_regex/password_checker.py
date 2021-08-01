from re import compile

pattern = compile("search this inside of this text please!")
string = "search this inside of this text please!"

pattern2 = compile(r"[A-Za-z-0-9$%#@]{8,}\d")
password = "hdkasdfsdfd3432s$%$@3"

a = pattern.search(string)
check = pattern2.fullmatch(password)

print(check)