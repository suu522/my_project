#最大正向匹配分词MMF

def readDict(fn):#读取词典内容，返回集合和最长词长
    words, max_len = set(), 0  # 用一个集合来存储词汇，用整数记录最长词长度
    with open(fn, encoding='utf-8') as fr:  # 使用 utf-8 编码打开文件
        for line in fr:  # 遍历文件的每一行
            line = line.strip()  # 去除行首尾的空格和换行符
            words.add(line)  # 将词汇添加到集合中
            if max_len < len(line):  # 更新最长词长度
                max_len = len(line)
    return words, max_len  # 返回词汇集合和最长词长度

def segment(inp,words,max_len):  #将输入的字符串进行中文分词操作，输入，词典和最大词长
    segged,rest='',inp  #初始化已分词字符串segged，未分词字符串rest
    while rest:  #只要还有为分词的字符串，就持续循环，直到全分完
        for i in range(max_len,0,-1):  #从最大长度开始切，倒序切
            candi=rest[:i]  #按照切词策略，切下长度i的部分为候选词（candidate）
            if candi in words:
                segged+=candi+' '  #candi确认是词，已分词字符串增长
                rest=rest[i:]  #更新未分词字符串，缩短
                break  #终止循环
            elif i==1:  #循环到i=1的单音节词的情况下，无论如何都切分
                segged+=candi+' '
                rest=rest[i:]
            #print(i,segged,rest)  #观察每次循环
    return segged
    
def main(fn):# 总控执行分词
    words, max_len = readDict(r"C:\Users\67327\Desktop\python\dict.txt")
    output_file = r"C:\Users\67327\Desktop\seg.txt"
    with open(output_file, 'w', encoding='utf-8') as fo:
        with open(fn, encoding='utf-8') as fr:
            for line in fr:
                line = segment(line.strip(), words, max_len)
                fo.write(line + '\n')
    print("分词完成。分词结果保存在:", output_file)

input_file = r"C:\Users\67327\Desktop\python\news (1).txt" # 输入文件路径
main(input_file)
