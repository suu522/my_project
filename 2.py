#分析语料库
'''
3分析语料库
3.1字频表->频次、频率、累积
3.2词频表->同、词长分布
3.3词性分布->实词比例、动词比例等
3.4句子形态->单句、复句、疑问句、感叹句、句长分布等
'''
import re
import pandas as pd

def char_proc(fn):  #用于处理文本文件，生成字符频率表
    chars,count,af={},0,0  #af是累计频次
    with open('path/to/your/file.txt', encoding='utf-8') as fr:
        for line in fr:
            for c in line:
                count+=1
                if c not in chars:
                    chars[c]=1
                else:
                    chars[c]+=1
        
        charList=sorted(chars.items(),key=lambda d:d[1],reverse=True)
        output_file = 'path/to/your/output/file.txt'  # 实际的输出文件路径和文件名
        with open(output_file, 'w', encoding='utf-8') as fo:
            for c, f in charList:
                af += f
                fo.write(c + '\t' + str(f) + '\t' + str(f / count) + '\t' + str(af / count) + '\n')        

def word_proc(fn):#处理文件并生成词频表和词长分析报告
    words, count, af, wl = {}, 0, 0, []
    with open(fn, encoding='utf-8') as fr:
        for line in fr:
            for c in line.split(' '):
                count += 1
                w = c.split('/')[0]
                wl.append(len(w))
                if w not in words:
                    words[w] = 1
                else:
                    words[w] += 1
        
        wordList = sorted(words.items(), key=lambda d: d[1], reverse=True)
        fo = open('wordList.txt', 'w', encoding='utf-8')
        
        pwl = pd.Series(wl)
        fo.write(str(pwl.describe()) + '\n')
        
        for c, f in wordList:
            af += f
            fo.write(c + '\t' + str(f) + '\t' + str(f / count) + '\t' + str(af / count) + '\n')
        
        fo.close()

def pos_proc(fn):  #输入是路径，输出是词性分布表
    pos,count,af={},0,0  #af是累计频次
    with open(fn,encoding='utf-8') as fr:
        for line in fr:
            for c in line.split(' '):
                count+=1
                tmp=c.split('/')
                if len(tmp)>1:
                    p=tmp[1]
                    if p not in pos:
                        pos[p]=1
                    else:
                        pos[p]+=1
        
        posList=sorted(pos.items(),key=lambda d:d[1],reverse=True)
        fo=open('posList.txt','w',encoding='utf-8')
        for c,f in posList:
            af+=f
            fo.write(c+'\t'+str(f)+'\t'+str(f/count)+'\t'+str(af/count)+'\n')
        fo.close()
# 调用pos_proc函数处理文件
file_path = 'path/to/your/file.txt'  # 实际的文件路径和文件名
pos_proc(file_path) #调用单个 
        
def sent_proc(fn):  #输入为文件路径，输出是句型分布和句长分析报告
    sents_total,dec,que,exc,count,af,sl=[],0,0,0,0,0,[]  #af是累计频次，sl是句长序列列表
    with open(fn,encoding='utf-8') as fr:
        for line in fr:
            dec+=line.count('。')
            que+=line.count('？')
            exc+=line.count('！')
            sents=re.split(r'[。！？]',line)
            sents_total+=sents
            count+=len(sents)
            for sent in sents:#统计每个句子长度
                sl.append(len(sent))
    
    fo=open('sentList.txt','w',encoding='utf-8')
    #用pandas分析句长分布
    psl=pd.Series(sl)
    fo.write(str(psl.describe()))
    #输出具体句长列表
    for c,f in {'dec':dec,'que':que,'exc':exc}.items():
        af+=f
        fo.write(c+'\t'+str(f)+'\t'+str(f/count)+'\t'+str(af/count)+'\n')
    fo.close()
                    
def main(fn): #总控
    char_proc(fn+r'.raw.txt')#计算字频表
    word_proc(fn+r'.seg_pos.txt')#计算词频表
    pos_proc(fn+r'.seg_pos.txt')#计算词性分布
    sent_proc(fn+r'.raw.txt')#计算三种句子占比
    
fn = r'path/to/your/file'  # 实际的文件路径和文件名（不包含文件扩展名）
main(fn) #调用所有