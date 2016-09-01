#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from wordcloud import WordCloud

# Obtem o camilho do diretorio que possui o arquivo procurado
filepath = path.dirname(__file__)

# referencia conteudo dos arquivos
text1 = open(path.join(filepath, 'Temer.txt')).read()
text2 = open(path.join(filepath, 'Dilma.txt')).read()


print text1
print text2
