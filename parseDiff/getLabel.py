import pandas as pd
import sys, io, getopt
import numpy as np
import gc
import re


FileDir = './parseDiff/inputDir/'


groupsInfo=pd.read_csv(FileDir+'read_groups.info', header = 0, sep = '\t', encoding = 'utf-8')
Fpkm=pd.read_csv(FileDir + 'genes.read_group_tracking', header = 0, sep = '\t', encoding = 'utf-8')


def cutstr(x):
    str=x
    patern1=re.compile('\/')
    patern2=re.compile('\.')
    cutstr=patern1.split(str)
    fileName=patern2.split(repr(cutstr[-1]))
    fileName=fileName[0]
    return fileName[1:]


groupsInfo['fileName']=groupsInfo['file'].map(lambda x:cutstr(x))
groupsInfo['replicate_num'] = groupsInfo['replicate_num'].map(lambda x: str(x))

groupsInfo['condition'] = groupsInfo['condition'].str.cat(groupsInfo['replicate_num'], sep = "_")

Fpkm['replicate'] = Fpkm['replicate'].map(lambda x: str(x))
Fpkm['condition'] = Fpkm['condition'].str.cat(Fpkm['replicate'], sep = "_")

groupsInfo.drop(['file','replicate_num','total_mass','norm_mass','internal_scale','external_scale'],axis=1,inplace=True)

info=pd.merge(left=Fpkm,right=groupsInfo,how='left',on='condition')
#print(Fpkm.head(5))
#print(groupsInfo)

print(info.head(5))