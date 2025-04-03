"""dictionary={
    "cat":"a small pet animal",
    "table":("a piece of furniture","a list of fct and figure")
}
print(dictionary)
print(dictionary["cat"])
print(dictionary["table"])
#---------------------------------------------------------------------------------

classroom = {"python","java","c++","python","java","js","c++","js","python","c","c"}
print("required classroom is: ",(len(classroom)))

#----------------------------------------------------------------------------------"""

marks = {}

x=int(input("enter phy: "))
marks.update({"phy":x})
y=int(input("enter chem: "))
marks.update({"chem":y})
z=int(input("enter bio: "))
marks.update({"bio":z})

print (marks)