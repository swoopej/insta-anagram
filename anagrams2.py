
DICT_FILE = '/usr/share/dict/words'

def is_word_anagram(user_word, check_word):
	for letter in check_word:
		if letter in user_word:
			check_word = check_word.replace(letter, '', 1)
		else:
			return None
	return True

def check_dictionary(user_word, filename):
	file_stream = open(filename, 'r')
	for line in file_stream:
		cur_word = line.strip()
		if len(cur_word) <= len(user_word):
			if is_word_anagram(user_word, cur_word):
				print cur_word
	file_stream.close()

def sentence_slicer(sentence):
	word_list = sentence.split()
	big_word = ''.join(x for x in word_list)
	check_dictionary(big_word, DICT_FILE)

if __name__ == '__main__':
	sentence = raw_input('Enter sentence to anagram-->  ')
	word_list = sentence_slicer(sentence)
