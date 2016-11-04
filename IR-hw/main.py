# -*- encoding: utf8 -*-

import textparser
import index
from bs4 import BeautifulSoup


index = index.HashedIndex()

file_object = open('shakespeare-merchant.trec.1')
corpus = file_object.read().lower()
soup = BeautifulSoup(corpus, "html.parser")

all_docs = soup.findAll("doc")
for doc in all_docs:
    doc_content = str(doc)
    sp = BeautifulSoup(str(doc), "html.parser")
    all_doc_nos = sp.findAll("docno")
    doc_content_to_token = list(textparser.word_tokenize(doc_content))
    for doc_no in all_doc_nos:
        doc_no_content = doc_no.contents[0].encode('utf-8')
        for term in doc_content_to_token:
            index.add_term_occurrence(term[0].encode('utf-8'), doc_no_content)

print index.sorted_inverted_index()
print index.get_sorted_posting_list('saying')















