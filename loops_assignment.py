# i = 1
# while i<=100 :
#     print(i)
#     i+=1

#---------------------------------------------------------

# num = int(input("enter a number: "))
# i = 1
# while i<=10 :
#     print(num*i)
#     i+=1
#--------------------------------------------------------------

# list = [1,4,6,8,9,15,14,23,26,30,80,95,100]
# i=0
# while i<=len(list)-1:
#     print(list[i])
#     i+=1
#-----------------------------------------------------

# tup = (1,4,6,8,9,15,14,23,26,30,80,95,100)
# x=15
# i=0
# while i<len(tup):
#     if(tup[i]==x):
#         print("found at index: ",i)
#     i+=1
#------------------------------------------------------------------

# numlist = [1,4,5,15,20,31,45,65,84,92,20,100]
# x = 20
# idx = 0
# for num in numlist:
#     if(num == x):
#         print("number found at index: ",idx)
#     idx += 1
    
#----------------------------------------------------------------------
n=int(input("enter a number:"))
for i in range(1,11,1):
    i=n*i
    print(i)
