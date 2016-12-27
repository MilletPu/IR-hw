# -*- encoding: utf8 -*-

import textparser
import index
from bs4 import BeautifulSoup


# 读入莎士比亚语料库，构建索引。
def construct_inverted_index():
    invertedIndex = index.HashedIndex()
    global corpus
    doc_id = 1
    for i in range(1, 3):
        url = 'shakespeare-merchant.trec.' + str(i)
        file_object = open(url)
        corpus = file_object.read().lower()
        file_object.close()

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
                    invertedIndex.add_term_occurrence(term[0], doc_id)
            doc_id += 1
    return invertedIndex, corpus


# 主函数
if __name__ == '__main__':
    con = 'yes'
    while con == 'yes':
        global index, corpus
        print '''
            ---------------------Menu Bar---------------------
            1: Build the inverted index of Shakespear-Merchant\n
            2: Check the inverted index of Shakespear-Merchant\n
            3: Check the posting list of a certain word\n
            4: Check the statistics of the corpus\n
            5: Check the inverted index compressed by VB\n
            6: Check the dictionary compressed by a long word\n
            0: Quit
            --------------------------------------------------'''

        print "Input a corresponding number: "
        choice = input()

        if choice == 0:
            print "Quit main.py successfully! Thank you very much. "
            break

        if choice == 1:
            # 1，建立索引
            print '-------1. Build the inverted index of Shakespear-Merchant:--------'
            index, corpus = construct_inverted_index()
            print 'Successfully build the index! Input number 2 to see the index!'
            print '------------------------------------------------------------------'
            print 'Input \"yes\" to continue.'
            con = raw_input()

        if choice == 2:
            # 2，打印建立好的所有倒排索引，并写入文件
            print '------------2. The inverted index of Shakespear-Merchant:---------'
            # print index.get_sorted_inverted_index()
            index.write_index_to_disk('inverted_index_with_doc_id.txt')
            print '------------------------------------------------------------------'
            print 'Input \"yes\" to continue.'
            con = raw_input()

        if choice == 3:
            print "Please input a word existing in the corpus, like \"a\", \"almost\", \"title\" and so on."
            word = raw_input()
            # 3，查询某个词项的倒排索引
            print '-----------------3. Search a word\'s posting list:----------------'
            print index.get_sorted_posting_list(word)
            print '------------------------------------------------------------------'
            print 'Input \"yes\" to continue.'
            con = raw_input()

        if choice == 4:
            # 4，给出预料统计量
            print '--------------4. Statistics of the inverted index:----------------'
            print index.get_corpus_statistics(corpus)
            print '------------------------------------------------------------------'
            print 'Input \"yes\" to continue.'
            con = raw_input()

        if choice == 5:
            # 5，利用VB对倒排索引进行压缩，并写入文件
            print '--------------5. The inverted index by VB compressed:-------------'
            # print index.get_sorted_inverted_index_VB()
            index.write_index_to_disk_VB('inverted_index_with_doc_id_VB.txt')
            print '------------------------------------------------------------------'
            print 'Input \"yes\" to continue.'
            con = raw_input()

        if choice == 6:
            # 6，提取词典，并利用单一字符串压缩
            print '-----------6. The dictionary by a long word compressed:-----------'
            print index.get_longword()
            print '------------------------------------------------------------------'
            print 'Input \"yes\" to continue.'
            con = raw_input()
