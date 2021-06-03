from py2neo import Graph

class AnswerSearcher:
    def __init__(self):
        self.g = Graph("http://localhost:7474", user="neo4j", password="neo4jneo4j")
        self.num_limit = 20

    '''Cypher query'''
    def search_main(self, sqls):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
        return final_answers

    '''qustion_type，answer template'''
    def answer_prettify(self, question_type, answers):
        final_answer = []
        if not answers:
            return 'Sorry I cannot understand your question:<'
            
        elif question_type == 'heifer_question':
            l_ = []
            for i in answers:
                if i['m.htype'] not in l_:
                    l_.append(i['m.htype'])
                    final_answer = 'The advice for {0} : {1}'.format(i['m.htype'], i['m.hanswer'])
                    print(final_answer)

        

        return final_answer
       

if __name__ == '__main__':
    searcher = AnswerSearcher()