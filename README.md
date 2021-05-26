# KBQA_Trial_One
Knowledge Graph Question Answering Trial (heifer management)

=================================================================
Procedures:

1, packages:
python 
neo4j community

2, import data:
start neo4j community (cmd: neo4j console)
load csv files using neo4j language (cypher: do this in neo4j brower, I didn't save the code here)

3, run python:
python chatbot_graph.py

4, the code skeleton:
![Can2_KBQA](https://user-images.githubusercontent.com/77312114/119589555-9d69c280-be05-11eb-9922-067ccce5c747.jpg)

=================================================================
Demo:

1, how it looks like in neo4j:
![image](https://user-images.githubusercontent.com/77312114/119589797-27b22680-be06-11eb-9033-26f1c2603e6c.png)

2, question answering part:
![image](https://user-images.githubusercontent.com/77312114/119589846-3c8eba00-be06-11eb-9e6b-d2c5425a659d.png)
![image](https://user-images.githubusercontent.com/77312114/119589859-46182200-be06-11eb-87f4-17937c00acae.png)
![image](https://user-images.githubusercontent.com/77312114/119589875-4c0e0300-be06-11eb-8910-ed676df2fc18.png)

=================================================================
Problem:

1, this is too small and it can only answer a few questions

2, it has minimum ability to understand natural language questions(only named entity recognition is used)

3, next step: explore more precise and rich knowledge
              use NLP to better understand the questions
