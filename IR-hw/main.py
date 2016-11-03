# -*- encoding: utf8 -*-

import textparser
import index

#a = list(textparser.word_tokenize("pig's pig, hello 2 cruel's \"apples\" sisters' pig"))

corpus = open('shakespeare-merchant.trec.1').read().lower()
b = list(textparser.word_tokenize(corpus))
index = index.HashedIndex()

for term in b:
    index.add_term_occurrence(term[0].encode('utf-8'), 'doc1')

print index.inverted_index()
