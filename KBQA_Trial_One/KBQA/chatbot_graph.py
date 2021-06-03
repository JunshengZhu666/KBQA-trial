from question_classifier import *
from question_parser import *
from answer_search import *

'''Query and Answer'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = 'Good Question!!! Ask for advisors for more help ~ '
        res_classify = self.classifier.classify(sent)
        if not res_classify=='':
            print(answer)
        #print('class：',res_classify)
        res_sql = self.parser.parser_main(res_classify)
        #print('sql query',res_sql)

        final_answers = self.searcher.search_main(res_sql)
        if final_answers=='':
            print(answer)

            #return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    #Test-start
    problems=["When should I breed my heifers?", "How should I feed my heifer?", "How to keep my heifer healthy?", "How should I set the brans for my heifers?","Why my heifers conception rate is low?","How to feed colostrum for my calves?","Why my heifers always get diarrhea?", "Group1 bran setting for my heifer?"]
    for id,problem in enumerate(problems):
        print("========== The {0} question is:  {1}： ==========".format(id,problem))
        handler.chat_main(problem)
        print("\n")
    print("End of the test","\n")
    #Test-end
    while 1:
        question = input('Any other questions?:')
        handler.chat_main(question)
        print("\n")


