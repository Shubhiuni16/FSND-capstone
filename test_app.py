
import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from settings import DB_NAME, DB_USER, DB_PASSWORD

from app import create_app
from models import setup_db, Movies, Actors
from settings import DATABASE_PATH
class CapstoneTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = DATABASE_PATH
        # self.unauthorized_jwt = os.environ['INVALID_TOKEN']
        self.assistant_jwt = os.environ['CASTING_ASSISTANT_JWT']
        # self.producer_jwt = os.environ['PRODUCER_TOKEN']
        setup_db(self.app, self.database_path)

    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def testGetMovies(self):
        authHeader = {'Authorization': f'Bearer {self.assistant_jwt}'}
        res=self.client().get('/movies', headers=authHeader)
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data!=None)

    def testGetMovies_error(self):
        res = self.client().get('/movies')  #without authToken
        data=json.loads(res.data)
        self.assertEqual(res.status_code,401)

    def testGetActors(self):
        authHeader = {'Authorization': f'Bearer {self.assistant_jwt}'}
        res = self.client().get('/actors',headers=authHeader)
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertTrue(data!=None)

    def testGetActors_error(self):
        res = self.client().get('/actors')
        data=json.loads(res.data)
        self.assertEqual(res.status_code,401)

    # def test_delete_question(self):
    #     new_question=Question(
    #         question="What is your name",
    #         answer="Shubhi",
    #         difficulty=1,
    #         category=2
    #     )
    #     self.db.session.add(new_question)
    #     self.db.session.commit()
    #     id=new_question.id
    #     res = self.client().delete('/questions/'+str(id))
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code,200)
    #     self.assertEqual(data['id'],id)

    # def test_delete_question_error(self):
    #     res = self.client().delete('/questions/1000')
    #     data=json.loads(res.data)
    #     self.assertEqual(res.status_code,422)
    #     self.assertEqual(data['success'],False)

    # def test_add_question(self):
    #     new_question={
    #         "question":"What is your name",
    #         "answer":"Shubhi",
    #         "difficulty":1,
    #         "category":2
    #     }
    #     res = self.client().post('/questions',json=new_question)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data['success'],True)

    # def test_add_question_error(self):
    #     new_question={
    #         "question":"What is your name",
    #         "difficulty":1,
    #         "category":2
    #     }
    #     res = self.client().post('/questions',json=new_question)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'],False)
    #     self.assertEqual(data["message"],"Bad Request")

    # def test_search_questions(self):
    #     res = self.client().post('/questions/search',json={"searchTeerm":"What"})
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['questions'])
    #     self.assertTrue(data["totalQuestions"])

    # def test_search_questions_error(self):
    #     res = self.client().post('/questions/search',json=None)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'],False)
    #     self.assertEqual(data["message"],"Bad Request")

    # def test_questions_by_category(self):
    #     res = self.client().get('/categories/1/questions')
    #     data = json.loads(res.data)
    #     category = Category.query.get(1).type
    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["currentCategory"],category)

    # def test_questions_by_category_error(self):
    #     res = self.client().get('/categories/100/questions')
    #     data = json.loads(res.data)
    #     category = Category.query.get(1).type
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data["success"],False)

    # def test_quiz(self):
    #     request={
    #         "previous_questions":[1,2,3],
    #         "quiz_category":{
    #             "id":0,
    #             "type":"click"
    #         }
    #     }
    #     res = self.client().post('/quizzes',json=request)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 200)
    #     self.assertTrue(data['question'])

    # def test_quiz_error(self):
    #     request={
    #         "previous_questions":[1,2,3]
    #     }
    #     res = self.client().post('/quizzes',json=request)
    #     data = json.loads(res.data)
    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'],False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()