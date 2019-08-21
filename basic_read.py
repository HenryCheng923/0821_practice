data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有', len(data),'筆資料')

sum_len = 0 
for d in data:
	sum_len += len(d)
print('留言平均長度', sum_len/len(data))

new = []
for d in data:
	if len(d)<100:
		new.append(d)
print('一共有 ', len(new), '筆留言長度小於100')

find_good = []
for d in data :
	if 'good' in d:
		find_good.append(d)
print('一共有', len(find_good), '筆留言提到good') 


#list 清單快寫法
find_good = [d for d in data if 'good'in d]
#第一個d的意思是"find_good.append(d)的意思，
#for d in data ，將data資料放到d裡面，
#if 'good' in d  ，如果d裡面有good的，
#放入第一個d裡面