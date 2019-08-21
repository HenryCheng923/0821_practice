#記帳程式
products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':	
		break
	price = input('請輸入商品價格： ')
	p = [name , price] #建立小清單
	products.append(p)
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
	
with open('products.csv', 'w') as f: #在python下with用法等同於有open與close功能
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') #csv裡面都用,做為區隔
