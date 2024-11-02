#This program is about 4 basic operation in python
#Initial List
my_list = [10,20,30,40,50]

#1.append()
my_list.append(60)
print("List after addition(append 60) :",my_list)

#2.extend()
my_list.extend([70,80])
print("List after addition(extend with ([70,80]) : ",my_list)

#3.Insert()
my_list.insert(2,25)
print("List after Insertion(insert 25 at index 2) : ",my_list)

#4.Slice()
sliced_list = my_list[1:4]
print("Sliced Portion (index 1 to 4) : ",sliced_list)