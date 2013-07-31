import os
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
		print "No this word."

if __name__ == "__main__":
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument('look_up_word',help='The word you want to look up')
	args = arg_parser.parse_args()
	getDefinitionFromWebster(args.look_up_word)

