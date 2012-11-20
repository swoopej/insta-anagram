
DICT_FILE = '/usr/share/dict/words'


def is_word_anagram(user_word, check_word):
	'''checks if user_word can be made from chars in check_word'''
	for letter in check_word:
		index = user_word.find(letter)
		if index != -1:
			check_word = check_word.replace(letter, '', 1)
			user_word = user_word.replace(letter, '', 1)
		else:
			return None
	return True

#generator function that returns all the words in the dict_file that 
#can be created from the chars in user_word
def check_dictionary(user_word, file_stream):
	'''generator function that returns all the words in the dict_file that 
		can be created from the chars in user_word'''
	for line in file_stream:
		cur_word = line.strip()
		if len(cur_word) <= len(user_word):
			if is_word_anagram(user_word, cur_word):
				yield cur_word

def remove_spaces(sentence):
	'''returns a big giant string with no spaces'''
	word_list = sentence.split()
	big_word = ''.join(x for x in word_list)
	return big_word

def slice_input(sentence, file_stream):
	'''remove spaces from an input sentence, return result of check_dictionary'''
	big_word = remove_spaces(sentence)
	return check_dictionary(big_word, file_stream) #returns a generator

def remove_chars(word, sentence):
	'''function will remove all the characters in word from sentence
		and replace them with empty string '''
	for letter in word:
		sentence = sentence.replace(letter, '', 1)
	return sentence

def sentence_anagrammer(word_list, sentence, file_stream):
	'''not sure yet''' 
	for word in word_list:
		if word_list:
			sentence_anagrammer0(word, sentence, file_stream, [])

	#append word to some master
	#restart process with shortened sentence
	#rerun process for sub-list of words

def sentence_anagrammer0(word, sentence, file_stream, accumulator):
	shortened_sentence = remove_chars(word, sentence)
	if shortened_sentence:
		new_word_list = check_dictionary(shortened_sentence, file_stream)
		accumulator.append(word)
		for new_word in new_word_list:
			sentence_anagrammer0(new_word, shortened_sentence, file_stream, accumulator)

	print accumulator


if __name__ == '__main__':
	sentence = raw_input('Enter sentence to anagram-->  ')
	file_stream = open(DICT_FILE, 'r')
	word_list = slice_input(sentence, file_stream)
	sentence_anagrammer(word_list, sentence, file_stream)
	file_stream.close()

