import os #operating system

products = []
if os.path.isfile('products.csv'): #檢查相對路徑是否有此檔案
	print('資料夾有此檔案，繼續執行步驟')

	#讀取檔案(運用split切割)
	with open('products.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #跳過商品與價格的資料不要寫入(跳過下一回，還在回圈內)
			name , price = line.strip().split(',') #用,作為分割，用strip去除\n換行
			products.append([name, price])#print(name[0],print[0])
	print(products)

else:
	print('資料夾中無此檔案，無法執行')


#讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':	
		break
	price = input('請輸入商品價格： ')
	p = [name , price] #建立小清單
	products.append(p)
print(products)

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#若使用utf-8仍出現亂碼，用excel開啟資料>取得外部資料>從檔案，就可以完成開啟中文字。	
with open('products.csv', 'w', encoding = 'utf-8') as f: #在python下with用法等同於有open與close功能
	f.write('商品,價格\n') #在csv格式之前加入名稱
	for p in products:
#寫入檔案
		f.write(p[0] + ',' + p[1] + '\n') #csv裡面都用,做為區隔
print('檔案已寫入完成')

