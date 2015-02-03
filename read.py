message_parts = '01101000 01100001 01101000 01100001 01101000 01100001'.split(' ')

for part in message_parts:
	print(chr(int(part, 2)), end='')

print('\n')
