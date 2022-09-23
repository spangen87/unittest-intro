import unittest
from students import Student


class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')
        # Körs innan hela testet

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')
        # Körs efter hela testet    

    
    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')
        # Körs före varje testenhet

    def tearDown(self):
        print('tearDown')    
        # Körs efter varje testenhet

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')


    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


    def test_email(self):
        print('test_email')
        self.assertEqual(student.email, 'john.doe@email.com')

if __name__ == '__main__':
    unittest.main()
