# -*- encoding: utf8 -*-

import textparser
import index
import collections

a = list(textparser.word_tokenize("pig's pig, hello 2 cruel's \"apples\" sisters' pig"))

# file_object = open('shakespeare-merchant.trec.1')
# try:
#     corpus = file_object.read().lower()
# finally:
#      file_object.close( )
#
# corpus_to_token = list(textparser.word_tokenize(corpus))

index = index.HashedIndex()

for term in a:
    index.add_term_occurrence(term[0].encode('utf-8'), 'doc1')
index.add_term_occurrence('pig'.encode('utf-8'), 'doc3')
index.add_term_occurrence('pig'.encode('utf-8'), 'doc5')

print index.inverted_index()
print collections.OrderedDict(sorted(index.inverted_index().items(), key=lambda t: t[0]))