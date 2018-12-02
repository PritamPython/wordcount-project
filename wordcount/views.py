from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
	return render(request,"home.html")

def about(request):
	return render(request,"about.html")

def count(request):
	full_text = request.GET['fulltext']
	print(full_text)
	word_list = full_text.split()
	word_dictionary={}

	for word in word_list:
		if(word in word_dictionary):
			word_dictionary[word] = word_dictionary[word]+1
		else:
			word_dictionary[word] = 1
	sortedwords = sorted(word_dictionary.items(), key=operator.itemgetter(1) , reverse=True)
	return render(request,"count.html",{'fulltext':full_text,'count':len(word_list),'worddictionary':sortedwords})
