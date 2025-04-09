num=3
if num>0:
    print(num,"is posetive number")
num=-1
if num<0:
    print(num,"is a negetive number")

#profit loss
actual_cost=float(input("please actual product price"))
sale_amount=float(input("please the sales amount"))
if(sale_amount>actual_cost):
    amount=sale_amount-actual_cost
    print("total profit={0}".format(amount))
else:
    print("no profit")