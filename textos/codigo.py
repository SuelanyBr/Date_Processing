#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
#from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np


# Obtem o camilho do diretorio que possui o arquivo procurado
filepath = path.dirname(__file__)


# referencia conteudo dos arquivos
text1 = open(path.join(filepath, 'Temer.txt')).read()
text2 = open(path.join(filepath, 'Dilma.txt')).read()

myStopwords = ['a', 'e', 'o', 'as', 'os', 'da', 'de', 'do', 'das', 'dos', 'um', 'uma', 'ele', 'ela', 'desse', 'dessa',
	'na', 'no',	'esse', 'essa', 'mesmo', 'mesma', 'nesta', 'neste', 'essa', 'esse', 'disse', 'que', 'em', 'onde', 'aonde',
	'fez', 'por', 'mas', 'foi', 'nao', 'com', 'para', 'isso', 'me', 'qual', 'tambem', 'outras', 'sem', 'auto', 'isso',
	'isto', 'ira', 'se', 'logo', 'ja', 'tudo', 'todo', 'todos', 'muito', 'muita', 'pouco', 'mais', 'menos', 'quanto', 'ainda', 'antes' ]

print text1
print text2
