# f=open("sample.txt","w") 
# f.write("Hi everyone! \n")
# print(f)
# f=open("sample.txt","a")
# f.write("I am learning file I/O in python") 
# print(f)
#---------------------------------------------------------

# with open("practice.txt","w")as f: 
#     f.write("Hi everyone!\nI am learning file I/O using python\n")
#     f.write("I like programing in python")
#----------------------------------------------------------------------

with open("practice.txt","r")as f:
    data=f.read()
new_data = data.replace("python","java")
print(new_data)
with open("practice.txt","w")as f:
    f.write(new_data)