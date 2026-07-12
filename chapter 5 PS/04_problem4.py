s= set()
s.add(20)
s.add(20.0)
s.add('20') #length of s after these operations?

print(s)

print(len(s))  # 20==20.0 thats why len is 2 (both consider same value)
