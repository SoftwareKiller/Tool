#coding=utf-8
# 检索网页后用于单词频率计数的Python3程序
from lib2to3.pygram import Symbols
import requests
from bs4 import BeautifulSoup
import datetime
from collections import Counter
'''定义网络爬虫/核心蜘蛛的函数，它将从给定的网站获取信息，并将内容推送到第二个函数clean_wordlist()'''
def start(urlList):
    print("爬虫开始, list长度为: %d" % len(urlList))
    wordlist = []
    word_count = {}
    # 空列表，用于存储从我们的网络爬虫获取的网站内容
    for url in urlList:
        source_code = requests.get(url).text
         # BeautifulSoup对象，它将对请求的URL进行ping操作
        soup = BeautifulSoup(source_code, 'html.parser')
        # 给定网页中的文本存储在<div>标记下的类为<entry-content>
        for each_text in soup.findAll('div'):
            content = each_text.text
            # 使用split()将句子分解为单词并将其转换为小写
            words = content.lower().split()
            for each_word in words:
                wordlist.append(each_word)
        clean_list = clean_wordlist(wordlist)
        wordlist = []
        create_dictionary(clean_list, word_count)
    print("爬虫结束, list长度为: %d" % len(word_count))
    c = Counter(word_count)
    print(len(word_count))
    # 返回出现次数最多的元素
    top = c.most_common(10)
    for word, count in top:
        print(word, count)
    top = c.most_common(2000)
    print("dir长度为: %d" % len(top))
    save_to_file(top)
# 该功能删除所有不需要的符号
def clean_wordlist(wordlist):
    clean_list =[]
    symbols = {}
    symbols['!'] = 1
    symbols['@'] = 1
    symbols['#'] = 1
    symbols['$'] = 1
    symbols['%'] = 1
    symbols['^'] = 1
    symbols['&'] = 1
    symbols['*'] = 1
    symbols['('] = 1
    symbols[')'] = 1
    symbols['-'] = 1
    symbols['_'] = 1
    symbols['+'] = 1
    symbols['='] = 1
    symbols['{'] = 1
    symbols['}'] = 1
    symbols['['] = 1
    symbols[']'] = 1
    symbols['|'] = 1
    symbols[';'] = 1
    symbols[':'] = 1
    symbols['<'] = 1
    symbols['>'] = 1
    symbols['.'] = 1
    symbols[','] = 1
    symbols['?'] = 1
    symbols['/'] = 1
    symbols['”'] = 1
    symbols['“'] = 1
    symbols['—'] = 1
    symbols['©'] = 1
    symbols['0'] = 1
    symbols['1'] = 1
    symbols['2'] = 1
    symbols['3'] = 1
    symbols['4'] = 1
    symbols['5'] = 1
    symbols['6'] = 1
    symbols['7'] = 1
    symbols['8'] = 1
    symbols['9'] = 1
    character = {}
    character['a'] = 1
    character['an'] = 1
    character['and'] = 1
    character['at'] = 1
    character['as'] = 1
    character['are'] = 1
    character['be'] = 1
    character['by'] = 1
    character['for'] = 1
    character['from'] = 1
    character['has'] = 1
    character['he'] = 1
    character['in'] = 1
    character['is'] = 1
    character['it'] = 1
    character['its'] = 1
    character['of'] = 1
    character['on'] = 1
    character['or'] = 1
    character['that'] = 1
    character['the'] = 1
    character['to'] = 1
    character['was'] = 1
    character['were'] = 1
    character['will'] = 1
    character['with'] = 1
    character['you'] = 1
    character['your'] = 1
    character['this'] = 1
    character['these'] = 1
    character['those'] = 1
    character['there'] = 1
    character['then'] = 1
    character['than'] = 1
    character['new'] = 1
    for word in wordlist:
        if word in character:
            continue
        flag = False
        for char in word:
            if char in symbols:
                flag = True
                break
        if flag == True:
            continue
        if len(word) > 0:
            clean_list.append(word)
    return clean_list
# 创建一个字典，其中包含每个单词的计数和top_20个出现的单词
def create_dictionary(clean_list, word_count):
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    ''' 获取已爬网页面中每个单词的计数 -->
    # operator.itemgetter()接受一个参数1(表示键)或0(表示对应值)
    for key, value in sorted(word_count.items(),
                    key = operator.itemgetter(1)):
        print ("% s : % s " % (key, value))
    <-- '''

def save_to_file(wordlist):
    f = open("wordlist.txt", "a")
    for word in wordlist:
        if word[1] > 1:
            f.write(word[0] + "\n")
    f.close()
# 测试代码
if __name__ == '__main__':
    urlList = ["https://docs.redis.com/latest/rs/", "https://nginx.org/en/docs/http/ngx_http_core_module.html","https://nginx.org/en/docs/control.html",
    "https://nginx.org/en/docs/configure.html","https://docs.oracle.com/en-us/iaas/Content/StorageGateway/Reference/storagegatewayfeatures.htm",
    "https://docs.oracle.com/en-us/iaas/Content/StorageGateway/Concepts/storagegatewayoverview.htm", "https://docs.oracle.com/en/cloud/paas/data-safe/udscs/security-assessment-overview.html"]
    print(datetime.datetime.now())
    start(urlList)
    print(datetime.datetime.now())
