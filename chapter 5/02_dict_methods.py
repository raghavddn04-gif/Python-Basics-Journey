marks = {
    "Harry": 100,
    "Shubham": 45,
    "Rohan": 23,
    0:"Harry"
}
print(marks.items())


marks = {
    "Harry": 100,
    "Shubham": 45,
    "Rohan": 23,
    0:"Harry"
}
print(marks.keys())


marks = {
    "Harry": 100,
    "Shubham": 45,
    "Rohan": 23,
    0:"Harry"
}
print(marks.values())



marks = {
    "Harry": 100,
    "Shubham": 45,
    "Rohan": 23,
    0:"Harry"
}
marks.update({"Harry":99, "Renuka":100})  #it change the original dict means it is mutable
print(marks)


marks = {
    "Harry": 100,
    "Shubham": 45,
    "Rohan": 23,
    0:"Harry"
}
#print(marks.get("shivika"))
print(marks.get("Harry"))




#what is the difference between
print(marks.get("Harry"))
print(marks["Harry"])
#now,if we change by
print(marks.get("Harry2")) #it will give none
print(marks["Harry2"])     #it will give error