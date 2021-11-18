import unittest

from app.models import Comment,User
from app import db

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.user_shawn9717 = User(username = 'shawn9717',password = 'shawn', email = 'shawnnjoga@gmail.com')
        self.new_comment = Comment(comment='best',user = self.user_shawn9717 )

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()
    def test_check_instance_variables(self):

        self.assertEquals(self.new_comment.comment,'best')
        self.assertEquals(self.new_comment.user,self.user_shawn9717)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
