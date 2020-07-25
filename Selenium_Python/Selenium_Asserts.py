#Demostrate the unittest framework
import unittest

def addition(x,y,z=0):
    #add the three parameters which are passed to the addition function
    return x+y+z


#This is where the test cases is implemented
class AddTest(unittest.TestCase):
    def setUp(self):

        pass

    def test_addition(self):
        self.assertEqual(addition(10,11,12),33)
        #x=11,y=12,z=44 if (x+y)=z, the test would raise an assert since
        #the test is for assertNotEqual operation
        self.assertNotEqual(addition(11,12,),44)

    def test_negative_value(self):
        self.assertNotEqual(addition(-9,25),16) #Changed Values#


    def tearDown(self):

        pass


if __name__=='__main__':
    unittest.main()