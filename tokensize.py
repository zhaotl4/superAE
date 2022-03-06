#encoding=utf-8
from __future__ import unicode_literals
import jieba

def tokensize_file(infile,outfile):
    total_write = []
    with open(infile,'r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            result = jieba.tokenize(line)
            ans_token = ''
            for tk in result:
                ans_token += tk[0]+' '
            total_write.append(ans_token)
    f.close()
    with open(outfile,'w',encoding='utf-8') as f:
        for sentence in total_write:
            f.write(sentence+'\n')
    f.close()
            
tokensize_file('valid.src','output.txt')