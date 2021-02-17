#*******************************************#
#*********Author:Mahmoud Dardery************#
#*********codeBY:Mahmoud Dardery************#
#*********Date:17/2/2021********************#
#*************************************************************************#
#********'project':"make a bookmark for saving ur favourite websites."**s**#
#*************************************************************************#

# we make a list to save on it our loved websites :)
favwebs = []
# we make a variable to make a limit of our inputs websites in our list .
maxfavwebs = 5
# we will use a while loop to (ask user add website) and (add entered website to our list) .
a = 0
while a < maxfavwebs:
    x = input("enter ur fav web without http:\\:")
    favwebs.append(x.lower().strip())
    a += 1
    # we will print to user the empty places remained in our list . {in loop }
    print(f"web added , {maxfavwebs-a} positions free ")
print("you used all positions ")  # after loop ends we will print that
# congratulations u did it
# we will use sort function to make it more sortable
favwebs.sort()
# we will use a loop to print all websites in some beautiful shape
print("*"*40)
b = 0
while b < 5:
    print(favwebs[b])
    b += 1

print("*"*40)
# if u read it , Thanks to you :)
