#記帳程式
products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':	
		break
	price = input('請輸入商品價格： ')
	p = [name , price] #建立小清單
	products.append(p)

print(products[0][0],products[0][1])