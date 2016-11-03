# -*- encoding: utf8 -*-

import textparser
import index

a = list(textparser.word_tokenize("pig's pig, hello 2 cruel's \"apples\" sisters' pig"))
index = index.HashedIndex()

for term in a:
    index.add_term_occurrence(term[0].encode('utf-8'), 'doc1')
index.add_term_occurrence('pig', 'doc2')

index.add_term_occurrence('pig', 'doc3')

print 'index.items():'
print index.items(), '\n'

print 'index.to_dict():'
print index.to_dict(), '\n'

print 'index.inverted_index():'
print index.inverted_index(), '\n'

print index.get_posting_list('pig')
