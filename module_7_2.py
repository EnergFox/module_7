def custom_write(file_name: str, strings: list):
	strings_positions = {}
	line_number = 1
	file = open(file_name, 'w')
	for s in strings:
		fb = file.tell()
		file.write(f'{s}\n')
		strings_positions[(line_number, fb)] = s
		line_number += 1
	file.close()
	return strings_positions

info = [
	'Text for tell.',
	'Используйте кодировку utf-8.',
	'Because there are 2 languages!',
	'Спасибо!'
	]
result = custom_write('test.txt', info)
for elem in result.items():
	print(elem)