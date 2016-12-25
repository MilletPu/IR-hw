# -*- encoding: utf8 -*-

import textparser
import VB
import index
from bs4 import BeautifulSoup


def construct_inverted_index():
    invertedIndex = index.HashedIndex()
    global corpus
    for i in range(1, 3):
        url = 'shakespeare-merchant.trec.' + str(i)
        file_object = open(url)
        corpus = file_object.read().lower()
        file_object.close()

        soup = BeautifulSoup(corpus, "html.parser")
        all_docs = soup.findAll("doc")
        doc_id = 1
        for doc in all_docs:
            doc_content = doc.contents
            sp = BeautifulSoup(str(doc_content), "html.parser")
            all_doc_nos = sp.findAll("docno")

            doc_content_to_token = list(textparser.word_tokenize(str(doc_content)))

            for doc_no in all_doc_nos:
                doc_no_content = doc_no.contents[0]
                for term in doc_content_to_token:
                    invertedIndex.add_term_occurrence(term[0], doc_id)
            doc_id += 1
    return invertedIndex, corpus

def VBcompressed(inverted_index):
    VBcompressed_index = inverted_index
    for i in range(0,len(inverted_index)):
        print VB.VB(inverted_index.values()[i].values()[0])
        VBcompressed_index.values()[i].values()[0] = VB.VB(inverted_index.values()[i].values()[0])
    return VBcompressed_index

if __name__ == '__main__':
    index, corpus = construct_inverted_index()
    # print index.get_sorted_inverted_index()  # 打印所有倒排索引
    # print index.get_sorted_posting_list('title')  # 打印某个词项的倒排索引
    # print index.get_corpus_statistics(corpus)  # 打印统计数据
    # index.write_index_to_disk('inverted_index_with_doc_id.txt')  #写入磁盘
    #
    # print index.get_sorted_inverted_index().values()[0].values()[0]
    # print VB.VB(index.get_sorted_inverted_index().values()[0].values()[0])
    print VBcompressed(index.get_sorted_inverted_index())