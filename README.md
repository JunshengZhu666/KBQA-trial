# KBQA_Trial_One
==================================================================================================================================



==================================================================================================================================
Trial_one：On hiefer management

1, Used:
python, 
neo4j community

2, import data:
start neo4j community (cmd: neo4j console),
load csv files using neo4j language (see load_graph.txt)

3, run python:
python chatbot_graph.py

4, the code skeleton:


![image](https://user-images.githubusercontent.com/77312114/121019573-2273b500-c7d2-11eb-9fbd-9c50957b86ec.png)

5, how the data looks like in neo4j:

![image](https://user-images.githubusercontent.com/77312114/120652874-c13aa180-c4b2-11eb-8c18-5f5524a89d6c.png)

6, question answering:

![image](https://user-images.githubusercontent.com/77312114/119590979-5c26e200-be08-11eb-984f-7818448a09ce.png)
![image](https://user-images.githubusercontent.com/77312114/121019813-5b138e80-c7d2-11eb-9d2b-2201740a643a.png)



==================================================================================================================================

              
   
   
==================================================================================================================================
Trial_two: A Knowledge Graph of cattle diseases, which is able to diagnose and recommend given different symptoms 

1, website resouces:

https://www.farmhealthonline.com/US/disease-management/cattle-diseases/

2, data schemas and question templates

![My_KG02](https://user-images.githubusercontent.com/77312114/122015338-988ba380-cdf2-11eb-9d3d-3e2b86f23398.jpg)


3, my procedures

manually create the csv files from the websites(the information from the website is not perfectly structured) --> load the file into neo4j with RDF format(see code in load_data.txt) --> use word stemming to process the question and match with the entities in the neo4j database

4, the data in neo4j 

![image](https://user-images.githubusercontent.com/77312114/122011997-49903f00-cdef-11eb-9e34-3aede95ec5e0.png)
![graph(2)](https://user-images.githubusercontent.com/77312114/122014688-fff52380-cdf1-11eb-92ed-eb96096881fa.png)


5, the question answering part

![image](https://user-images.githubusercontent.com/77312114/122015734-f0c2a580-cdf2-11eb-8d27-f5c7e77b3bc9.png)
![image](https://user-images.githubusercontent.com/77312114/122015821-0768fc80-cdf3-11eb-9fb4-77b4361a86bc.png)
![image](https://user-images.githubusercontent.com/77312114/122015872-151e8200-cdf3-11eb-8941-e18550af1b4e.png)

6, the first three answers in comparsion with Google

6,1 ![image](https://user-images.githubusercontent.com/77312114/122173954-e36def80-ceb4-11eb-9a59-91ce0d89a2fb.png)
Not specific

6.2 ![image](https://user-images.githubusercontent.com/77312114/122174078-000a2780-ceb5-11eb-8e4b-b81c0eee8ad5.png)
Only give one reason while the reasons could be many others

6.3 ![image](https://user-images.githubusercontent.com/77312114/122174225-1fa15000-ceb5-11eb-8dda-34a12bc4de55.png)
Not answering the question in domian



==================================================================================================================================

              
   
   
==================================================================================================================================
Planning for trial_three:

Trail two is based on question templates and manually created data. 

Next step: 

Use NLP to automate the building process 

==================================================================================================================================
The benefits of NLP and KG in dairy industry: 

1, The untilization of textual data, like literatures, managament and medical records. 

2, The reusability of NLP models, which can update the knowledge by re-extracting the new text. 

3, The specialization of question answering in domain. 

==================================================================================================================================
# About the KBQA part 

1, Prepare:

    # Start neo4j database. 
    # Put into the two entity words list under the folder:
    #![image](https://user-images.githubusercontent.com/77312114/142640798-fbe6f71f-f930-4dfc-a187-ac9e93ea3e37.png)


2, Code skeleton:

![image](https://user-images.githubusercontent.com/77312114/121019573-2273b500-c7d2-11eb-9fbd-9c50957b86ec.png)

3, Question Template setting up:

3,1 answer_search.py:

    # 1 Change url, username and password to connect the neo4j database
    
    # 2 Set the final answer template for different question type:
    #  question_type == 'cause_diseases'
    #  '{0} might casue diseases：{1}', 'n.nname', 'm.dname'
    #![image](https://user-images.githubusercontent.com/77312114/142640139-b96c5fc8-761f-4e76-9ace-08ff69b8d67b.png)

    
3,2 chatbot_graph.py: 

    # 1 Can set the testing questions:
    #![image](https://user-images.githubusercontent.com/77312114/142640347-5fb0489f-1d42-4ab3-a26f-4be7d13a680b.png)
    
3,3 question_classifier.py:

    # 1 Load in the entity word lists
    #![image](https://user-images.githubusercontent.com/77312114/142641311-3c542fe2-d500-4840-883a-44793c187c17.png)
    # search and change all 'diseases' in script for your entity word list
    
    # 2 Set the question classification words 
    #![image](https://user-images.githubusercontent.com/77312114/142641975-47a00ce3-3cda-4f80-8337-0bcf240ca299.png)
    
    # 3 Set the question classification rules 
    #![image](https://user-images.githubusercontent.com/77312114/142642231-81612afa-8d0c-48c5-bd8b-2b09d231b733.png)

    # 4 Build word type dictionary (python dictionary)
    #![image](https://user-images.githubusercontent.com/77312114/142644574-f9c3109d-3020-4ecd-9ad1-56da4092f98a.png)
    
3,4 question_parser.py:
    
    # 1 Pass the retrived entities to according question template
    #![image](https://user-images.githubusercontent.com/77312114/142645569-561ad9ec-8b44-48c1-8cd4-485b790c5de7.png)

    # 2 Use different query language(Cypher) to query the neo4j database
    #![image](https://user-images.githubusercontent.com/77312114/142645858-69a399cb-fa5d-4d2d-8443-f47056061979.png)



