#!/usr/bin/python3.5
# coding=utf-8
import sys, io, getopt
import numpy as np
import pandas as pd
import gc
import re

from functools import reduce
from argparse import ArgumentParser

FileDir = './parseDiff/inputDir/'
output_file='./parseDiff/outputDir/'
reference='./parseDiff/hg19.txt'

# setting
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('max_colwidth', 300)

# input
groupsInfo=pd.read_csv(FileDir+'read_groups.info', header = 0, sep = '\t', encoding = 'utf-8')
Fpkm = pd.read_csv(FileDir + 'genes.read_group_tracking', header = 0, sep = '\t', encoding = 'utf-8')
Exp = pd.read_csv(FileDir + 'gene_exp.diff', header = 0, sep = '\t', encoding = 'utf-8')
annotate = pd.read_csv(reference, header = None, sep = '\t', encoding = 'utf-8')
output = output_file
# Fpkm = pd.read_table('/Users/panxu/Downloads/SMART-Seq_statistics/Chen.SZ_AM20180608-02/Ctrl_SPION10/genes.read_group_tracking.txt', header = 0, sep = '\t', encoding = 'utf-8')# Exp = pd.read_table('/Users/panxu/Downloads/SMART-Seq_statistics/Chen.SZ_AM20180608-02/Ctrl_SPION10/gene_exp.diff', header = 0, sep = '\t', encoding = 'utf-8')# annotate = pd.read_table('/Users/panxu/Downloads/SMART-Seq_statistics/Chen.SZ_AM20180608-02/Ctrl_SPION10/GeneType.mm10.txt', header = None, sep = '\t', encoding = 'utf-8')# output = '/Users/panxu/Downloads/SMART-Seq_statistics/Chen.SZ_AM20180608-02/Ctrl_SPION10/'

def getFileName(x):
    str=x
    patern1=re.compile('\/')
    patern2=re.compile('\.')
    cutstr=patern1.split(str)
    fileName=patern2.split(repr(cutstr[-1]))
    fileName=fileName[0]
    return fileName[1:]

#get grooup file

groupsInfo['fileName']=groupsInfo['file'].map(lambda x:getFileName(x))
groupsInfo['replicate_num'] = groupsInfo['replicate_num'].map(lambda x: str(x))
groupsInfo['condition'] = groupsInfo['condition'].str.cat(groupsInfo['replicate_num'], sep = "_")
groupsInfo.drop(['file','replicate_num','total_mass','norm_mass','internal_scale','external_scale'],axis=1,inplace=True)

# Fpkm reshap
Fpkm['replicate'] = Fpkm['replicate'].map(lambda x: str(x))
Fpkm['condition'] = Fpkm['condition'].str.cat(Fpkm['replicate'], sep = "_")

Fpkm=pd.merge(left=Fpkm,right=groupsInfo,how='right',on='condition')

print(Fpkm.head(5))

Fpkm_pivot = Fpkm.pivot_table(index = ["tracking_id"], columns = ["fileName"], values = ["FPKM"])
Fpkm_pivot = Fpkm_pivot['FPKM'].reset_index(drop = False)
Fpkm_pivot.rename(columns = {
    'tracking_id': 'gene'
}, inplace = True)


annotate.columns = ['gene', 'type']
Exp.drop(['test_id', 'gene_id', 'test_stat'], axis = 1, inplace = True)


dfs = [annotate, Exp, Fpkm_pivot]

df_final = reduce(lambda left, right: pd.merge(left, right, on = 'gene'), dfs)


print("=============Merge2================")
#print(df_final.head(5));
print("\n")

# filter merge# DGE = raw_df[(raw_df["value_1"] > 0.5) & (raw_df["value_2"] > 0.5) & ((raw_df["log2(fold_change)"] > 0.5849) | (raw_df["log2(fold_change)"] < (-0.5849)))]
DGE = df_final[ ((df_final["log2(fold_change)"] > 0.5849) | (df_final["log2(fold_change)"] < (-0.5849)))]
Up = DGE[DGE["log2(fold_change)"] > 0.5849]
Down = DGE[DGE["log2(fold_change)"] < (-0.5849)]

DGE_stat = pd.DataFrame([
    ['All', len(df_final)],
    ['DGE', len(DGE)],
    ['DGE_Up', len(Up)],
    ['DGE_down', len(Down)]
], columns = [u'Type', u'Counts'])
print("Differential Expression Gene Matrix:")
#print(DGE.head(5));
print("\n")
print("Differential Expression Gene Statistics:")
print(DGE_stat)


# output
sample1 = df_final['sample_1'].ix[1]
sample2 = df_final['sample_2'].ix[1]

df_final.to_csv(output + 'Raw.' + sample1 + "-" + sample2 + "." + '.xls', header = True, index = False, sep = '\t', encoding = 'utf-8')
DGE.to_csv(output + 'DEG.' + sample1 + "-" + sample2 + "." + '.xls', header = True, index = False, sep = '\t', encoding = 'utf-8')
Up.to_csv(output + 'DEG.' + sample1 + "-" + sample2 + "." + sample2 + '-HighExp' + '.xls', header = True, index = False, sep = '\t', encoding = 'utf-8')
Down.to_csv(output + 'DEG.' + sample1 + "-" + sample2 + "." + sample2 + '-LowExp' + '.xls', header = True, index = False, sep = '\t', encoding = 'utf-8')
DGE_stat.to_csv(output + 'DEG.' + sample1 + "-" + sample2 + ".stat.xls", header = True, index = False, sep = '\t', encoding = 'utf-8')



del Fpkm
del Exp
del annotate
gc.collect()
