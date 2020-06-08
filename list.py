# list is a collection of heterogeneous data items
# list is a mutable i.e changble
# example of a list :-
list = ["siva",22,5.11,"india"]
print(list)
# access the list using index numbers
print(list[1]) # 22
print(list[0:len(list)+1]) # ["siva",22,5.11,"india"]
print(list[::-1]) # it prints reverse of a list
# loop through list
for i in list:
  print(i)
  
# add elements
# append,extend,insert
list = [1,2,3,4,5]
list.append(5)
print(list)
list.extend((6,7,8,9,10))
print(list)
list.insert(0,1)
print(list)

# del,remove,pop
# above methods are used to delete

li = ["hai","hello","ok","hmm"]
del li[2]
print(li)
li.remove("hmm")
print(li)
li.pop(0)
print(li)
li.clear()
print(li)

# sorted order i.e asec,desc
lis = [36,67,87,98,43,88,23,19,34,76]
lis.sort(reverse = True)
print(lis)
lis.sort(reverse = False)
print(lis)
print(sorted(lis))

# particular
l = ["hyd","bangalore","chennai","mumbai","ongole"]
a = l.index("ongole")
print(a)
#count
b = l.count("hyd")
print(b)
for i in l:
    print(i)
print(l[::-1])

# how to check if list is empty or not
list = []
if not list:
  print("empty")
else:
  print("not empty")
# remove duplicates from list
list = [1,1,2,2,2,3,4,2,5,5,6,4]
res = []
for i in list:
  if i not in res:
      res.append(i)
print(res)
########### or ##########
print(set(list))
######## or ########
from collections import Counter
res = []
A = Counter(list)
for i,j in A.items():
  res.append(i)
print(res)
  