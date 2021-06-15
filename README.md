# KBQA_Trial_One
==================================================================================================================================



==================================================================================================================================
Trial_one：On hiefer management

0, 
See KBQA_Trial_One_New file, others are out of date.
Some packages are used in python, may spend some time to download.

1, Used:
python, 
neo4j community

2, import data:
start neo4j community (cmd: neo4j console),
load csv files using neo4j language (see build_graph.txt)

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
Trial_two: A Knowledge Graph of cattle diseases, which is able to diagnose and recommend given symptoms

1, website resouces:

https://www.farmhealthonline.com/US/disease-management/cattle-diseases/

2, data schemas and question templates

![My_KG02](https://user-images.githubusercontent.com/77312114/122015338-988ba380-cdf2-11eb-9d3d-3e2b86f23398.jpg)


3, my procedures

manually create the csv files from the websites(the information from the website is not perfectly structured) --> load the file into neo4j with RDF format(see code in Trail_two_load_data.txt) --> use word stemming to process the question and match with the entities in the neo4j database

4, the data in neo4j 

![image](https://user-images.githubusercontent.com/77312114/122011997-49903f00-cdef-11eb-9e34-3aede95ec5e0.png)
![graph(2)](https://user-images.githubusercontent.com/77312114/122014688-fff52380-cdf1-11eb-92ed-eb96096881fa.png)


5, the question answering part

![image](https://user-images.githubusercontent.com/77312114/122015734-f0c2a580-cdf2-11eb-8d27-f5c7e77b3bc9.png)
![image](https://user-images.githubusercontent.com/77312114/122015821-0768fc80-cdf3-11eb-9fb4-77b4361a86bc.png)
![image](https://user-images.githubusercontent.com/77312114/122015872-151e8200-cdf3-11eb-8941-e18550af1b4e.png)


==================================================================================================================================

              
   
   
==================================================================================================================================
Planning for trial_three:

Trail two is based on question templates and manually created data. 

Next step: 

1, Using Transformer Models like T5 and BERT to antomate the Knowledge Graph Building and Question Answering procedures.

2, Looking for a more structured information or website to crawl
