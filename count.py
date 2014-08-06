#!/usr/bin/env python
# coding=utf-8
input = open('textfill.txt', 'r')
input_3000 = open('3000.txt', 'r')
input_3000meaning = open('3000meaning.txt', 'r')
output = open('count.txt', 'w')
raw_words = input.readlines()
word_3000 = input_3000.readlines()
word_3000meaning = input_3000meaning.readlines()
count_of_word = {}
dict_3000 = {}
for i in range(0,len(word_3000)):
	dict_3000[word_3000[i]] = word_3000meaning[i]

for word in raw_words:
	if count_of_word.has_key(word):
		count_of_word[word] = count_of_word[word] + 1
	else:
		count_of_word[word] = 1

word_set = list(set(raw_words))

result = []
for word in word_set:
	if dict_3000.has_key(word):
		result.append(str(count_of_word[word]) + '\t' + word + ':' + dict_3000[word]) #数字\t单词：释义
	else:
		result.append(str(count_of_word[word]) + '\t' + word)
result.sort(reverse=True)
output.writelines(result)
input.close()
input_3000.close()
input_3000meaning.close()
output.close()