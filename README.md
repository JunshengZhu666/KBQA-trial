# KBQA_Trial_One
Knowledge Graph Question Answering Trial (heifer management)

==================================================================================================================================
Procedures:

1, packages:
python, 
neo4j community

2, import data:
start neo4j community (cmd: neo4j console),
load csv files using neo4j language (cypher: do this in neo4j brower, I didn't save the code here)

3, run python:
python chatbot_graph.py

4, the code skeleton:


![Can2_KBQA](https://user-images.githubusercontent.com/77312114/119589555-9d69c280-be05-11eb-9922-067ccce5c747.jpg)


==================================================================================================================================
Demo:

1, how the data looks like in neo4j:

![image](https://user-images.githubusercontent.com/77312114/120652874-c13aa180-c4b2-11eb-8c18-5f5524a89d6c.png)

2, question answering:


![image](https://user-images.githubusercontent.com/77312114/119590979-5c26e200-be08-11eb-984f-7818448a09ce.png)
![image](https://user-images.githubusercontent.com/77312114/119590992-62b55980-be08-11eb-95f1-93c9e85c0bd0.png)
![image](https://user-images.githubusercontent.com/77312114/119591005-68ab3a80-be08-11eb-821a-42ecdd69813e.png)
![image](https://user-images.githubusercontent.com/77312114/120653021-e4655100-c4b2-11eb-98d9-f7a4927136ab.png)



==================================================================================================================================
Problem:

1, this is too small and it can only answer a few questions

2, it has minimum ability to understand natural language questions

3, next step: explore more precise and rich knowledge,
              use NLP to better understand the questions
              
              
   
   
==================================================================================================================================
Planning for trial_two:

1, websites:

https://www.farmhealthonline.com/US/disease-management/cattle-diseases/

2, data schemas and question templates

![image](https://user-images.githubusercontent.com/77312114/120652632-86d10480-c4b2-11eb-850e-128513194d9b.png)

