

def read_input(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as r: #加上sig就可以去除怪符號了
		for line in r:
			lines.append(line.strip())
	return lines	

def write_output(filename, news):
	with open(filename, 'w', encoding = 'utf-8') as w:
		for new in news:
			w.write(new + '\n' )

def convert(lines):
	new = []
	person = None  #python特有，預設為沒有值
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue

		if person:		#如果Person沒有值執行下列行數
			new.append(person + ': ' + line)
	return new

def main():
	lines = read_input('input.txt')
	new = convert(lines)
	write_output('output.txt',new)
	print("寫入完成")

main()