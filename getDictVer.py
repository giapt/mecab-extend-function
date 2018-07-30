#coding:utf-8
import MeCab

tagger = MeCab.Tagger("-Ochasen")

def getDictVer(word):
	new_word = ''
	parse = tagger.parse(word)
	lines = parse.split('\n')

	for line in lines:
		if line =="EOS" or line =="":
			continue
		parts = line.split('	')
		new_word += parts[2]
		# print word
		# print new_word
		# print '========'
	new_word = new_word.replace('ます', '')
	return new_word