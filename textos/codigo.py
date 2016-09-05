#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import matplotlib.pyplot as plt
import numpy as np
import nltk
from nltk.corpus import stopwords
from unicodedata import normalize
import string

def remover_acentuacao(txt, codif='utf-8'):
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')   

def exclui_stopwords_nltk(text):
	stopwords = nltk.corpus.stopwords.words('portuguese')
	content = [w for w in text if w.lower() not in stopwords]
	return content

def exclui_myStopwords(text):
	for i in myStopwords:
		while i in text:
			text.remove(i)

def exclui_stopwords(text):
	text = exclui_stopwords_nltk(text)
	text = exclui_myStopwords(text)
	return text

def exclui_pontuacoes(text):
	punctuation = list(string.punctuation)
	for palavra in text:
		for p in punctuation:
			while p in palavra:
				palavra.replace(p, "", 2)
	
# Obtem o camilho do diretorio que possui o arquivo procurado
filepath = path.dirname(__file__)


# referencia conteudo dos arquivos
text1 = open(path.join(filepath, 'Temer.txt')).read()
text2 = open(path.join(filepath, 'Dilma.txt')).read()

myStopwords = ['a', 'e', 'o', 'as', 'os', 'da', 'de', 'do', 'das', 'dos', 'um', 'uma', 'ele', 'ela', 'desse', 'dessa',
	'na', 'no',	'esse', 'essa', 'mesmo', 'mesma', 'nesta', 'neste', 'essa', 'esse', 'disse', 'que', 'em', 'onde', 'aonde',
	'fez', 'por', 'mas', 'foi', 'nao', 'com', 'para', 'isso', 'me', 'qual', 'tambem', 'outras', 'sem', 'auto', 'isso',
	'isto', 'ira', 'se', 'logo', 'ja', 'tudo', 'todo', 'todos', 'muito', 'muita', 'pouco', 'mais', 'menos', 'quanto', 'ainda', 'antes' ]

def modifica_texto(text):
	text = remove_acentuacao(text).split(' ')
	text = exclui_stopwords(text)
	return text

text1 = modifica_texto(text1)	
test2 = modifica_texto(text2)
