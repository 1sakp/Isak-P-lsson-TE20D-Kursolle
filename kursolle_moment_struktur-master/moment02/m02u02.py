a=9
b=2
f=4.0
namn="Isak"
c=a*b
print(c, type(c))
c=a*f
print(c, type(c))
c=a/b
print(c, type(c)) #eftersom det inte blir ett heltal utan får en decimal så blir den en float

print(namn, type(namn))
c=a//b
print(c, type(c)) #eftersom det blir ett heltal så blir det en int och eftersom ingen av dem var floats innan
c=a%b
print(c, type(c)) #eftersom det blir ett heltal så blir det en int och eftersom ingen av dem var floats innan
c=a**0.5
print(c, type(c)) #eftersom det inte blir ett heltal utan får en decimal så blir den en float
c=b**2
print(c, type(c)) #eftersom det blir ett heltal så blir det en int och eftersom ingen av dem var floats innan
c=f**2
print(c, type(c)) #eftersom det inte blir ett heltal utan får en decimal så blir den en float
b+=a
print(b)