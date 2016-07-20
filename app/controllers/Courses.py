"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('Course')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        all_course = self.models['Course'].get_all_courses_m()

        # query = "SELECT * FROM courses"
        # all_courses = self.db.query_db(query)
        # print all_course
        return self.load_view('index.html', s_allcourse=all_course)

    def add(self):
        course_details = { 
        'title': request.form['f_course_name'],
        'desc': request.form['f_course_description']
        }
        self.models['Course'].add_one_course_m(course_details)
        return redirect('/')

    def remove(self, remove_id):
        removing_course = self.models['Course'].remove_m(remove_id)
        # print "REmoving Course is", removing_course
        return self.load_view('remove.html', s_removing_course=removing_course[0])
    
    def no(self):
        return redirect('/')

    def remove_one_id(self, remove_id):
        self.models['Course'].remove_one_course_m(remove_id)
        return redirect('/')

