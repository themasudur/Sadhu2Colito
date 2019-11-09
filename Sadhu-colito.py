# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:50:42 2019

@author: Masudur
"""
'''
kriya_mul_list = ['হ', 'ল', 'যা', 'খা', 'পা', 'দি', 'নি', 'শু', 'কর', 'লিখ', 'উঠ', 'শুন', 'চল', 'খুল', 'কিন', 'কাট', 'মার', 'ফাট', 'পার', 'পড়', 'দেখ', 'আঁক', 'বাঁধ', 'কাঁদ', 'ফির', 'খুল', 'উড়', 'খুঁজ', 'ডাক', 'শিখ', 'বস']
# kriya_purush = [নাম-সাধারণ, মধ্যম-সম্ভ্রান্ত, মধ্যম-সাধারণ, উত্তম] 
kriya_vibokti_sadhu = ['িতেছে', 'িতেছেন', 'িতেছ', 'িতেছি', 'ইতেছে', 'ইতেছেন', 'ইতেছ', 'ইতেছি', 'িয়াছে', 'িয়াছেন', 'িয়াছ', 'িয়াছি' , 'ইয়াছে', 'ইয়াছেন', 'ইয়াছ', 'ইয়াছি', 'িল', 'িলেন', 'িলে', 'িলাম', 'ইল', 'ইলেন', 'ইলে', 'ইলাম', 'িত', 'িতেন', 'িতে', 'িতাম', 'িতেছিল', 'িতেছিলেন', 'িতেছিলে', 'িতেছিলাম', 'ইতেছিল', 'ইতেছিলেন', 'ইতেছিলে', 'ইতেছিলাম', 'িয়াছিল', 'িয়াছিলেন', 'িয়াছিলে', 'িয়াছিলাম', 'িবে', 'িবেন', 'িবে', 'িব', 'ইবে', 'ইবেন', 'ইবে', 'ইব']
kriya_vibokti_colito = ['ছে', 'ছেন', 'ছ', 'ছি', 'চ্ছে', 'চ্ছেন', 'চ্ছ', 'চ্ছি', 'েছে', 'েছেন', 'েছ', 'েছি', 'চ্ছে', 'চ্ছেন', 'চ্ছ',' চ্ছি', 'ল', 'লেন', 'লে', 'লাম', 'ল', 'লেন', 'লে', 'লাম', 'ত', 'তেন', 'তে', 'তাম', 'ছিল', 'ছিলেন', 'ছিলে', 'ছিলাম', 'চ্ছিল', 'চ্ছিলেন', 'চ্ছিলে', 'চ্ছিলাম', 'েছিল', 'েছিলেন', 'েছিলে', 'েছিলাম', 'বে', 'বেন', 'বে', 'বো', 'বে', 'বেন', 'বে', 'বো']
# print("Size of sadhu Bibokti", len(kriya_vibokti_sadhu), "vs colito Bibokti", len(kriya_vibokti_colito))

'''
kriya_mul_list = []
fileName = 'F:\python_ml\sadhu-colito\kriya_mul_list.txt'
kriya_mul_list = [line.rstrip('\n') for line in open(fileName, encoding='utf-16')]
print(kriya_mul_list)

print("Total Kriya:", len(kriya_mul_list))

fileName = 'F:\python_ml\sadhu-colito\kriya_vibokti_list.txt'
kriya_vibokti_list = [line.rstrip('\n') for line in open(fileName, encoding='utf-16')]
print(kriya_vibokti_list)

kriya_vibokti_sadhu = [item.split('=')[0] for item in kriya_vibokti_list]
kriya_vibokti_colito = [item.split('=')[1] for item in kriya_vibokti_list]
    
print("Total Sadhu Bibokti:", len(kriya_vibokti_sadhu), "\nColito Bibokti:", len(kriya_vibokti_colito))

print(type(kriya_mul_list))

#fileName = 'F:\python_ml\shadhu-colito\robin1.txt'
fileName = 'F:\python_ml\sadhu-colito\corpus_.txt'
all_sentences = [line.rstrip('\n') for line in open(fileName, encoding='utf-16')]
all_sentences
print(len(all_sentences))

sadhu = all_sentences[0]

# List to String

type(all_sentences)
type(all_sentences[10])
sadhu = ''.join(all_sentences)
print("Sadhu Bakko: ", sadhu)
colito = sadhu
tokens = []
tokens = sadhu.split()
print("Tokens/Words: ", tokens)
temp_match=[]
temp_kriya_mul = []

# Remove comma, dari, proshonobodhok, quotation

for i in range(len(tokens)):
    tokens[i] = tokens[i].replace(',', '')
    tokens[i] = tokens[i].replace('।', '')
print("Tokens: ", tokens)

# Identify Kriyas
    
for i in range(len(tokens)):
    for j in range(len(kriya_mul_list)):
        if (tokens[i].find(kriya_mul_list[j])==0):
            temp_match.append(tokens[i])
            temp_kriya_mul.append(kriya_mul_list[j])
print("Kriya Found (All): ", temp_match, ">>", temp_kriya_mul)

# Identify Kriyas

match=[]
kriya_mul = []
kriya_vibokti = []
for i in range(len(temp_match)):
    temp_kriya_vibokti = temp_match[i].split(temp_kriya_mul[i],1)[1]
    # print(temp_match[i], ">>", temp_kriya_mul[i], ">>", temp_kriya_vibokti)
    if(temp_kriya_vibokti in kriya_vibokti_sadhu):
        kriya_vibokti.append(temp_kriya_vibokti)
        match.append(temp_match[i])
        kriya_mul.append(temp_kriya_mul[i])
print("Kriya Found (Actual): ", match, ">>", kriya_mul, ">>", kriya_vibokti)

for i in range(len(match)):
    index = kriya_vibokti_sadhu.index(kriya_vibokti[i])
    colito = colito.replace(match[i],kriya_mul[i]+kriya_vibokti_colito[index])

# Handling Exceptioanl Verb Roots

fileName = 'F:\python_ml\sadhu-colito\exceptional_cases.txt'
exceptional_cases = [line.rstrip('\n') for line in open(fileName, encoding='utf-16')]
print(exceptional_cases)

exceptional_cases_sadhu = [item.split('=')[0] for item in exceptional_cases]
exceptional_cases_colito = [item.split('=')[1] for item in exceptional_cases]

for i in range(len(tokens)):
    for j in range(len(exceptional_cases_sadhu)):
        if (tokens[i].find(exceptional_cases_sadhu[j])==0):
            colito = colito.replace(exceptional_cases_sadhu[j], exceptional_cases_colito[j])

print("Colito Bakko: ", colito)
# print("Sadhu Bakko: ", sadhu)
