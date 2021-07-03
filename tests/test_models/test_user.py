#!/usr/bin/python3

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test """

    def test_User(self):
        """test_user"""
        self.assertTrue(True)

    def test_email(self):
        """test email"""
        obj = User()
        obj.email = "holbie@holbertonschool.com"
        self.assertNotEqual(obj.email, "")

    def test_password(self):
        """test password"""
        obj = User()
        obj.password = "root"
        self.assertNotEqual(obj.password, "")

    def test_first_name(self):
        """test first name"""
        obj = User()
        obj.first_name = "Julien"
        self.assertNotEqual(obj.first_name, "")

    def test_last_name(self):
        """test last name"""
        obj = User()
        obj.last_name = "Barbier"
        self.assertNotEqual(obj.last_name, "")

if __name__ == "__main__":
    unittest.main()
