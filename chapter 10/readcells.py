#example 10.5
sheet1 = wb['PriceList']
pricelist=[]
for row in range(1,7):
        prod=[]
        for col in range(1,4):
                val=sheet1.cell(column=col, row=2+row).value
                prod.append(val)
        pricelist.append(tuple(prod))
print (pricelist)
