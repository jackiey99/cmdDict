import os
import sys
import urllib2
import lxml.html as lh
from lxml.html.clean import clean_html
from lxml import etree
import argparse

def getDefinitionFromWebster(word):
	'''
	Look up the word in merriam-webster dictionary
	'''
	try:
		word_url = 'http://www.merriam-webster.com/dictionary/'+word
		source = lh.document_fromstring(urllib2.urlopen(word_url).read())
		word_list=source.find_class('scnt')
		for w in word_list:
			print w.text_content()
	#word is not actually an English word
	except urllib2.HTTPError:
		print "Sorry, what you are looking for is not found."

if __name__ == "__main__":
	#only one word
	if len(sys.argv)==2: 
		look_up_word = sys.argv[1]
	#phrase
	if len(sys.argv)>2:
		look_up_word = '%20'.join(sys.argv[1:]) #url encoding

	getDefinitionFromWebster(look_up_word)

