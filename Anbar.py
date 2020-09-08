#Mallarin sayini teyin edilmesi
choose_number_input=input("Please,Add the number:")
choose_number=int(choose_number_input)
#MElumatlari atacaqimiz data array kimi yaradilir
data=[]
#for ile onlari verilen say qeder cixardacayiq
for object in range(choose_number):
    name=input(str(object+1) +"-"+ "Entire name:")
    price=float(input("Entire price:"))
    amount=int(input("Entire number:" ))
    data.append([name,price,amount,price*amount])

print(data)
#En yuk olanini tapaq indi
max_price=data[0][1]
max_price_name=data[0][0]
for thing in data:
    if thing[1]>max_price:
            max_price=thing[1]
            max_price_name=thing[0]

print("Max is name:"+max_price_name+"-"+"Price:"+str(max_price))

sell_name=input("Sell name:")
demo_price=input("Sell amount:")
sell_price=int(demo_price)
tapdim=False
n=0
for thing in data:
    if(sell_name==data[n][0]):
        tapdim=True
        if(sell_price<data[0][3]):
            data[n][2]=data[n][2]-sell_price
            print("Right")
        else:
            print("Number is false")
n=n+1
if(tapdim==False):
    print("this thing is not")
print(data)




