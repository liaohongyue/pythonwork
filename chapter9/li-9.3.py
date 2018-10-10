from urllib import request
import re

pmid='18235848'
url='https://www.ncbi.nlm.nih.gov/pubmed?term=%s' % pmid
handler=request.urlopen(url)
html=handler.read()
html=html.decode('utf-8')

title_reg=re.compile(r'<h1>.{3,400}</h1>')
title_txt=title_reg.search(html).group()
abstract_reg=re.compile(r'<h3>Abstract</h3><div class=""><p>.{20,30000}</p></div>')
abstract_text=abstract_reg.search(html).group()
print("title:\n",title_txt)
print("abatract\n",abstract_text)