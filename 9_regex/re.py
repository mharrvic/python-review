from re import compile

pattern = compile("search this inside of this text please!")
string = "search this inside of this text please!"

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(d.span())