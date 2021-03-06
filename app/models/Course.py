""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """


    def get_all_courses_m(self):
        return self.db.query_db("SELECT * FROM courses ORDER BY created_at DESC")

    def add_one_course_m(self, new_course_details):
        query = "INSERT INTO courses (course_name, description, created_at, updated_at) \
        VALUES (:spec_course_name, :spec_description, NOW(), NOW())"
        data = { 
        'spec_course_name': new_course_details['title'],
        'spec_description': new_course_details['desc']
        }
        return self.db.query_db(query, data)

    def remove_m(self,remove_id):
        query = "SELECT * from courses WHERE id= :spec_id"
        data = { 'spec_id': remove_id }
        return self.db.query_db(query, data)

    def remove_one_course_m(self, new_remove_id):
        query = "DELETE FROM courses where id = :spec_id"
        data = {'spec_id': new_remove_id}
        return self.db.query_db(query, data)


