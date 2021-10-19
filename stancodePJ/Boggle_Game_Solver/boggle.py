"""
File: boggle.py
Name:Cristine
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:When the game starts, user will enter a 4×4 square font platter.
	The program will start to connect the connected characters on the platter
	to find all the English characters in this 4 x 4 square font platter.
	"""
	start = time.time()
	####################
	d = read_dictionary()
	# Save the entered letters as a list.
	letter_list = []
	for i in range(4):
		print(i+1, end='')
		letter = input(' row of letters: ')
		letter = letter.split()
		for ch in letter:
			if len(ch) != 1:
				print('Illegal input')
				return
			else:
				letter_list.append(ch)
	# Convert the list to a dictionary and create XY coordinates.
	l_d = {}
	for i in range(len(letter_list)):
		x = i // 4
		y = i % 4
		l_d[x, y] = letter_list[i]
	search_word(l_d, d)
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def search_word(l_d, dictionary):
	"""
	Use the word of each coordinate as a prefix and concatenate the letters.
	:param l_d: (dict) The letter entered by the user, including its coordinates.
	:param dictionary: (list) dictionary
	"""
	# Count the number of words found.
	counter = [0]
	# Save the words found.
	word_list = []
	# Find the prefix
	for x in range(4):
		for y in range(4):
			ch = l_d[x, y]
			# Save the coordinates of each letter.
			coordinate_list = [(x, y)]
			# Concatenate the letters.
			connect_letter(l_d, dictionary, ch, coordinate_list, x, y, counter, word_list)
	print(f'There are {counter[0]} words in total')


def connect_letter(l_d, dictionary, ch, c_l, x, y, counter, word_list):
	"""
	Concatenate letters and find a word in the dictionary.
	The word length is 4 or more.
	:param l_d: (dict) The letter entered by the user, including its coordinates.
	:param dictionary: (list) dictionary
	:param ch: (str) letter
	:param c_l: (list) Coordinates of each letter
	:param x: (int) The x-coordinates of the last letter.
	:param y: (int) The y-coordinates of the last letter.
	:param counter: (list) Count the number of words found.
	:param word_list: (list) Save the words found.
	"""
	# base case
	if len(ch) >= 4:
		# Find words that are 4 or more in length.
		for i in range(-1, 2):
			for j in range(-1, 2):
				# choose
				if 0 <= x+i < 4 and 0 <= y+j < 4:
					# Avoid finding letters in repeated positions.
					if (x+i, y+j) not in c_l:
						# concatenate letter
						ch += l_d[x+i, y+j]
						# Is there a word beginning with ch in the dictionary.
						check = has_prefix(ch, dictionary)
						if check:
							new_x = x + i
							new_y = y + j
							c_l.append((new_x, new_y))
							# explore
							connect_letter(l_d, dictionary, ch, c_l, new_x, new_y, counter, word_list)
							# un_choose
							ch = ch[: len(ch) - 1]
							c_l = c_l[:len(ch)]
						else:
							ch = ch[: len(ch) - 1]
				if ch in dictionary:
					# Avoid finding the same word.
					if ch not in word_list:
						print(f'Found \"{ch}\"')
						counter[0] += 1
						word_list.append(ch)
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				# choose
				if 0 <= x+i < 4 and 0 <= y+j < 4:
					# Avoid finding letters in repeated positions.
					if (x+i, y+j) not in c_l:
						# concatenate letter
						ch += l_d[x+i, y+j]
						# Is there a word beginning with ch in the dictionary.
						check = has_prefix(ch, dictionary)
						if check:
							new_x = x+i
							new_y = y+j
							c_l.append((new_x, new_y))
							# explore
							connect_letter(l_d, dictionary, ch, c_l, new_x, new_y, counter, word_list)
							# un_choose
							ch = ch[: len(ch) - 1]
							c_l = c_l[:len(ch)]
						else:
							ch = ch[: len(ch)-1]


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	d = []
	with open(FILE) as f:
		for line in f:
			line = line.strip()
			d.append(line)
		return d


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) String.
	:param d:(list) dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for i in range(len(d)):
		a = d[i].startswith(sub_s)
		if a:
			return True
	return False


if __name__ == '__main__':
	main()
