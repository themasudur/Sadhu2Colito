# README

**This project is a part of our Bangla Natural Language Processing Research work. We were planning to develop a system which can handle Bangla verbs in a sentence and can convert verbs written in sadhu form to cholito form of Bangla language.**

- [Paper link](#paper)
- [Abstract](#abstract)
- [Keywords](#keywords)
- [Introduction](#introduction)
- [Contribution](#contribution)
- [Algorithm 1](#algorithm-1)
- [Algorithm 2](#algorithm-2)
- [Cite this publication](#cite-this-publication)

## Paper
<a href="[about.html](https://ieeexplore.ieee.org/abstract/document/9038570" title="Paper">Read the paper here</a>



## Abstract
Bengali language follows Subject-Object-Verb (SOV) structure for constructing sentences where verb plays a crucial role. Machine translation for Bengali becomes easier if the verb is identified correctly in a semantically valid sentence. However, Bengali verbs are affected by various complex inflections while using in a sentence. Those inflections are determined according to tense (time of occurring event), person (nature of the subject), Sadhu and Cholito forms (historic evolution of writing styles of Bengali) of language. In this study, we propose an algorithm to identify different inflections of Bengali verbs to retrieve verb roots and present an approach to convert Sadhu to Cholito form of writing Bengali sentences. The methodology shows satisfying accuracy and fluency in the context of language evaluation.

## Keywords
Bengali language, Bengali verb, Verb root, Verbal inflection, Conversion of Sadhu to Cholito, Shadhu, Cholito.

## Introduction
Bengali language and literature have the most prominent and diverse tradition in the world, which is developed over the course of more than 1,300 years. The modern version of Bengali literary has been developed extensively during the 18th to 20th centuries. During this period, Bengali language exhibits a strong case of diglossia (also known as linguistic duality), a situation in which two forms of dialects are used in a single language. The two distinct varieties are named: 

- Sadhu Bhasha (সাধু; also spelt as Sadhu): A form of Bengali dialect for written purpose only.
- Cholito Bhasha (চলিত; also spelt as Chalita, Colito): An informal vernacular form of Bengali language.

The standard and formalized Sadhu bhasha came into usage in Medieval period of Bengali language in 16th century while the colloquial Cholito form came into vogue in the early of 19th century with a purpose of spoken dialect. The Cholito bhasha exhibits preponderance over Sadhu bhasha for both written and colloquial use by the influence of prominent writers— Pramatha Chaudhuri, Rabindranath Tagore etc. Although the Sadhu bhasha differs greatly from the Cholito style, an enormous number of literary works— proses, poetries, novels, have been written in Sadhu bhasha. Some pioneer writers of 19th century— Ishwar Chandra Vidyasagar, Bankim Chandra Chattopadhyay etc. wrote notable literature in Sadhu bhasha.

## Contribution
In this paper, we formulate an algorithm to find out the verb roots and verbal inflections hence to convert text of Sadhu form to Cholito language. To the best of our knowledge, it is the first time to deal with this kind of research work in Bangla language to convert from Sadhu to Cholito writing format, whereas finding verb root is accomplished by some researchers in different ways. This work has been investigated in phases: 
- Identify the verb root and verbal inflection
- Convert the Sadhu form of language to Cholito

## Algorithm 1
Algorithm 1: IndentifyVerbRoot(token) 
Input: Individual words of a sentence as token
Output: verb root, verbal inflection
Given: List: Kriyamul (Sadhu Bivokti, Cholito Bivokti)
Procedure:
1.	For i=1 to size(Kriyamul_list)
2.	If isSubString(Kriyamul_list[i], token) == TRUE
3.	temp_Bivokti = token — Kriyamul_list[i]
4.	If isBivokti(sadhuBivokti) == TRUE
5.	bivokti = temp_Bivokti
6.	End If
7.	kriyamul = Kriyamul_list[i]
8.	End If
9.	End For

## Algorithm 2
Algorithm 2: ConvertSadhu2Cholito(token) 
Input: Sentence with Sadhu inflection
Output: Sentence with Cholito inflection
Given: List: Kriyamul, (Sadhu Bivokti, Cholito Bivokti)
Procedure:
1.	For i=1 to size(Kriyamul_list)
2.	If isSubString(Kriyamul_list[i], token) == TRUE
3.	sadhuBivokti = token — Kriyamul_list[i]
4.	If isBivokti(sadhuBivokti) == TRUE
5.	Replace the Sadhu Bivokti with the corresponding Cholito Bivokti
6.	End If
7.	End If
8.	End For

## Cite this publication
```
Mohammad Masudur Rahman, Ashraful Islam, Md. Faisal Kabir, Mohammad Nurul Huda, "An Approach of Handling Verbal Inflections of Bengali Text: Conversion of Sadhu to Cholito Form of Language", 22nd International Conference of Computer and Information Technology (ICCIT), Dhaka, Bangladesh, 18-20 December, 2019.
```
