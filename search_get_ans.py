#!/usr/bin/python3

from googlesearch import search
import re
from stackapi import StackAPI

query=input('enter you want to search')
data=search(query+' stackoverflow',num=10,tld="com",stop=10)
questions=[]
for url in data:
	if re.search('stackoverflow.com',url)!=None:
		questions.append(url)
questions_ids=[]
for url in questions:
	q_id=url.split('/')[4]
	questions_ids.append(q_id)
	
site = StackAPI('stackoverflow')
ans_list=[]
length=len(questions_ids)
all_answers=site.fetch('questions/{ids}/answers',filter='!9Z(-wzftf',ids=questions_ids)
items=all_answers['items']
for answer in items:
	if answer['is_accepted']==True:
		ans_list.append(answer['body_markdown'])
for i in ans_list:
	print(i)
	print('\n\n')


