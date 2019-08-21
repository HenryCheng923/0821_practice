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

#若使用utf-8仍出現亂碼，用excel開啟資料>取得外部資料>從檔案，就可以完成開啟中文字。	
with open('products.csv', 'w', encoding = 'utf-8') as f: #在python下with用法等同於有open與close功能

	f.write('商品,價格,測試\n') #在csv格式之前加入名稱
	for p in products:

		f.write(p[0] + ',' + p[1] + '\n') #csv裡面都用,做為區隔
print('檔案已寫入完成')