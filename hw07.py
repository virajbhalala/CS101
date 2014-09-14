
#6.20
def revese(dict):
    for k, v in dict.items():
        dict[v] = k
    return dict



#6.27
def index(file, wordList):
    infile=open(file)
    s=infile.read()
    wordDict= {}
    
    for word in wordList:
        cnt=s.count(word)
        for i in range(cnt):
            wordDict[word].append(s.index(word))
            s=s.remove(word)
    return wordDict
    
