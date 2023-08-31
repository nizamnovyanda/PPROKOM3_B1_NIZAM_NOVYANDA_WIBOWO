txt='Hello world!'
z=txt.startswith('Hello')
print(z)
txt='Hello world!'
y=txt.endswith('world!')
print(y)
txt='abc123'
x=txt.startswith('abcdef') 
print(x)
txt='abc123'
w=txt.endswith('12')
print(w)
txt='Hello world!'
v=txt.startswith('Hello world!') 
print(v)
txt='Hello world!'
U=txt.endswith('Hello world!')
print(U)




a='Hello'
print(a.rjust(10)) 
b='Hello'
print(b.rjust(20)) 
c='Hello World'
print(c.rjust(20)) 
d='Hello'
print(d.ljust(10)) 
e='Hello'
print(e.rjust(20, '*')) 
f='Hello'
print(f.ljust(20, '-')) 
g='Hello'
print(g.center(20)) 
h='Hello'
print(h.center(20, '='))