# coding: utf-8
import MeCab
import jaconv
import re
import string
m = MeCab.Tagger ("-Ochasen")
new_sentence = ''
print ("明日はナムさんと学校で本を読みます")
sentence = "明日はナムさんと学校で本を読みます"
parse = m.parse(sentence)
info_of_words = parse.split('\n')

for word in info_of_words:
	if word =="EOS" or word =="":
		continue
		pass
	
	parse = m.parse(word)
	parts = parse.split('	')
	if len(parts)>2:
		word_parts = string.split(word, '	')
		u = unicode(parts[1], "utf-8")
		hira = jaconv.kata2hira(u)
		if word_parts[0] == parts[1]:
			new_sentence += unicode(word_parts[0], "utf-8")
			continue
			pass
		if hira != unicode(word_parts[0], "utf-8"):
			# new_sentence += unicode(word_parts[0], "utf-8")
			# new_sentence += '(' + hira + ')'
			new_sentence += getText(unicode(word_parts[0], "utf-8"), hira)
		else:
			new_sentence += unicode(word_parts[0], "utf-8")

print new_sentence