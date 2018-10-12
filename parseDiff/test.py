import os
import sys, io, getopt
import numpy as np
import pandas as pd
import gc
import re
inputDir='./parseDiff/inputDir/'

filelist=os.listdir(inputDir)

class parseDiff:
    

    def readFromTable(self,FileDir=r'./',reference='./parseDiff/hg19.txt'):
        groupsInfo=pd.read_csv(FileDir+'read_groups.info', header = 0, sep = '\t', encoding = 'utf-8')
        Fpkm = pd.read_csv(FileDir + 'genes.read_group_tracking', header = 0, sep = '\t', encoding = 'utf-8')
        Exp = pd.read_csv(FileDir + 'gene_exp.diff', header = 0, sep = '\t', encoding = 'utf-8')
        annotate = pd.read_csv(reference, header = None, sep = '\t', encoding = 'utf-8')

    def  writeToTable(self,output=r'./'):
        df_final.to_csv(output + 'Raw.' + sample1 + "-" + sample2 + "." + '.xls', header = True, index = False, sep = '\t', encoding = 'utf-8')
        DGE.to_csv(output + 'DEG.' + sample1 + "-" + sample2 + "." + '.xls', header = True, index = False, sep = '\t', encoding = 'utf-8')
        Up.to_csv(output + 'DEG.' + sample1 + "-" + sample2 + "." + sample2 + '-HighExp' + '.xls', header = True, index = False, sep = '\t', encoding = 'utf-8')
        Down.to_csv(output + 'DEG.' + sample1 + "-" + sample2 + "." + sample2 + '-LowExp' + '.xls', header = True, index = False, sep = '\t', encoding = 'utf-8')
        DGE_stat.to_csv(output + 'DEG.' + sample1 + "-" + sample2 + ".stat.xls", header = True, index = False, sep = '\t', encoding = 'utf-8')



for file in filelist:
        if os.path.isdir(inputDir+file):
            print(inputDir+file)


readFromTable(inputDir)
print(Fpkm)