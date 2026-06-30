a="hi hello ravi garu"
l=['a','e','i','o','u']
v=[i for i in a if i not in l and i!=' ']
c=[i for i in a if i in l]
print(v)
print(c)