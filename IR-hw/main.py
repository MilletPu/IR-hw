# -*- encoding: utf8 -*-

import textparser
import index
from bs4 import BeautifulSoup

file_object = open('shakespeare-merchant.trec.2')
corpus = file_object.read().lower()
file_object.close()

index = index.HashedIndex()
soup = BeautifulSoup(corpus, "html.parser")
all_docs = soup.findAll("doc")
for doc in all_docs:
    doc_content = doc.contents
    sp = BeautifulSoup(str(doc_content), "html.parser")
    all_doc_nos = sp.findAll("docno")

    doc_content_to_token = list(textparser.word_tokenize(str(doc_content)))

    for doc_no in all_doc_nos:
        doc_no_content = doc_no.contents[0]
        for term in doc_content_to_token:
            index.add_term_occurrence(term[0], doc_no_content)

print index.get_sorted_inverted_index()
print index.get_sorted_posting_list('title')
print index.get_corpus_statistics(corpus)
index.write_index_to_disk('data2.txt')