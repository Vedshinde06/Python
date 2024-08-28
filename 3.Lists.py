#1.Let us say your expense for every month are listed below,
#January - 2200
#February - 2350
#March - 2600
#April - 2130
#May - 2190
#Create a list to store these monthly expenses and using that find out,
'''1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''


list = [2200, 2350, 2600, 2130, 2190 ]

print("Extra money spent in feb compared to jan", list[1] - list[0] )

print("Total expanse first qurter : ", list[0]+list[1]+list[2])

print("Did I spend exact 2000 in any month?", 2000 in list)

list.append(1980)
print(list)

list[3] = list[3] - 200

print(list)

print(dir(list))