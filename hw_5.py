import os
import string

path1=os.getcwd()
#common.txt dosyasi "read" acilir ve kapanir
f=open(path1+"\\common.txt","r")
common_words_list=[]

for i in f.readlines():
    common_words_list.append(i.strip())

f.close()
#article.txt dosyasi "read" acilir ve kapanir
f=open(path1+"\\article.txt","r")
article_list=f.read().translate(str.maketrans('', '', string.punctuation)).split()
article_dict={}

for i in article_list:
    i=i.lower()
    if i not in article_dict:  
        article_dict[i]=1
    else:
        article_dict[i]+=1

f.close()
#output.txt dosyasi "write" acilir ve kapanir
f=open(path1+"\\output.txt","w")

for i in article_dict.copy().keys():

    if i in common_words_list:
        article_dict.pop(i)

    elif article_dict[i]>2:
        f.write(i+"\n")

f.close()


 