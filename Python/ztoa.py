import string
import os
import time

a = 'hello world'

b = ['-' if i!=' ' else ' ' for i in a]

reversed_alphabet = string.ascii_lowercase[::-1]
reversed_alphabet_display = list(string.ascii_lowercase[::-1])

print(reversed_alphabet)
print(''.join(b))

print_list_a = []
print_list = []

counter = 0
for letter in reversed_alphabet:
	for index in range(len(a)):
		if a[index] == letter:
			b[index] = letter

	reversed_alphabet_display[counter] = '-'
	counter += 1
	print_list_a.append(''.join(reversed_alphabet_display))
	print_list.append(''.join(b))
	# os.system('cls')

	# print(''.join(reversed_alphabet_display))
	# print(''.join(b))
	# time.sleep(0.3)

for i in range(len(print_list_a)):
	os.system('cls')
	print(print_list_a[i])
	print(print_list[i])
	time.sleep(0.3)
