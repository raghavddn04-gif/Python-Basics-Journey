s1={1,45,6}
s2={1,55,45,32,56}

print(s1.union(s2))
print(s1.intersection(s2))


print({1,45}.issubset(s1))
print({1,32}.issubset(s2))
print({1,45,6}.issuperset(s1))