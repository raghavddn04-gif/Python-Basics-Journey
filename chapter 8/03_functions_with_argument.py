def goodday(name):            # argument name is added 
     print("Good day, "  + name)


goodday("Harry")  
goodday("Rohan") 




# add another argument 

def goodday(name,ending):           
     print("Good day, "  + name)
     print(ending)


goodday("Harry","thank you")  
goodday("Rohan", "thank you") 
goodday("Divya","Thanks")






# return concept


def goodday(name,ending):           
     print("Good day, "  + name)
     print(ending)
     return"ok"


a=goodday("Harry","thank you") 
print(a) 






