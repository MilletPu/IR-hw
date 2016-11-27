
from bs4 import BeautifulSoup
import textparser


file_object = open('shakespeare-merchant.trec.1')
corpus = file_object.read().lower()

soup = BeautifulSoup(corpus, "html.parser")
trs = soup.findAll("doc")

for i in range(len(trs)):
    print trs[i].contents

# index = index.HashedIndex()
# a = list(textparser.word_tokenize("pig's pig, hello 2 cruel's \"apples\" sisters' pig"))
# file_object = open('shakespeare-merchant.trec.1')
#
# try:
#     corpus = file_object.read().lower()
# finally:
#      file_object.close( )
#
# corpus_to_token =list(textparser.word_tokenize(corpus))
# for term in corpus_to_token:
#     index.add_term_occurrence(term[0].encode('utf-8'), 'doc1')
# index.add_term_occurrence('a'.encode('utf-8'), 'doc3')
# index.add_term_occurrence('a'.encode('utf-8'), 'doc5')
#
#
# print index.sorted_inverted_index()
# print index.get_sorted_posting_list('a')