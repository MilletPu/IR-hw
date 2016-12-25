# -*- encoding: utf8 -*-

import textparser
import VB
import index
from bs4 import BeautifulSoup


# 读入莎士比亚语料库，构建索引。
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


# 主函数
if __name__ == '__main__':
    # 1，建立索引
    index, corpus = construct_inverted_index()

    # 2，打印建立好的所有倒排索引，并写入文件
    print index.get_sorted_inverted_index()
    index.write_index_to_disk('inverted_index_with_doc_id.txt')

    # 3，查询某个词项的倒排索引
    print index.get_sorted_posting_list('title')

    # 4，给出预料统计量
    print index.get_corpus_statistics(corpus)

    # 5，利用VB对倒排索引进行压缩，并写入文件
    print index.get_sorted_inverted_index_VB()
    index.write_index_to_disk_VB('inverted_index_with_doc_id_VB.txt')

    # 6，提取词典，并利用单一字符串压缩
    print index.get_longword()