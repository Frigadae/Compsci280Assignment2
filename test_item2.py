'''
Created on 14/08/2019

@author: wany889
'''
import unittest
from datetime import date

from drones import Drone, DroneStore
from operators import Operator, OperatorStore, OperatorAction

class OperatorTest(unittest.TestCase):
    def test_validation(self):
        #arrange
        operator = Operator()
        opstore = OperatorStore()
        operator.first_name = "Jake"
        operator.date_of_birth = date(1998, 11, 23)
        operator.drone_license = 2
        operator.rescue_endorsement = True
        operator.operations = 5
        
        #act
        output = opstore.add(operator)

        #assert
        self.assertTrue(output.is_valid() == True, "Passes if no messages are logged")
    
    def test_first_name(self):
        #arrange
        operator = Operator()
        opstore = OperatorStore()
        operator.first_name
        operator.date_of_birth = date(1998, 11, 23)
        operator.drone_license = 2
        operator.rescue_endorsement = True
        operator.operations = 5
        
        #act
        output = opstore.add(operator)
            
        #assert
        self.assertTrue(output.is_valid() == False, "Passes if errors are found")
        self.assertTrue("First name is required" in output.messages, "Passes if first name error is logged")
        
    def test_birth_date(self):
        #arrange
        operator = Operator()
        opstore = OperatorStore()
        operator.first_name = "Jake"
        operator.date_of_birth
        operator.drone_license = 2
        operator.rescue_endorsement = True
        operator.operations = 5
        
        #act
        output = opstore.add(operator)
        
        #assert
        self.assertTrue(output.is_valid() == False, "Passes if errors are found")
        self.assertTrue("Date of birth is required" in output.messages, "Passes if DOB error is logged")
        
    def test_drone_license(self):
        #arrange
        operator = Operator()
        opstore = OperatorStore()
        operator.first_name = "Jake"
        operator.date_of_birth = date(1998, 11, 23)
        operator.drone_license
        operator.rescue_endorsement = True
        operator.operations = 5
        
        #act
        output = opstore.add(operator)

        #assert
        self.assertTrue(output.is_valid() == False, "Passes if errors are found")
        self.assertTrue("Drone license is required" in output.messages, "Passes if license error is logged")
           
    def test_under20(self):
        #arrange
        operator = Operator()
        opstore = OperatorStore()
        operator.first_name = "Jake"
        operator.date_of_birth = date(2005, 11, 23)
        operator.drone_license = 2
        operator.rescue_endorsement = True
        operator.operations = 5
        
        #act
        output = opstore.add(operator)

        #assert
        self.assertTrue(output.is_valid() == False, "Passes if errors are found")
        self.assertTrue("Operator should be at least twenty to hold a class 2 license" in output.messages, "Passes if op is found to be under 20")
    
    def test_rescue_endorsement(self):
        #arrange
        operator = Operator()
        opstore = OperatorStore()
        operator.first_name = "Jake"
        operator.date_of_birth = date(1998, 11, 23)
        operator.drone_license = 2
        operator.rescue_endorsement = True
        operator.operations = 3
        
        #act
        output = opstore.add(operator)
            
        #assert
        self.assertTrue(output.is_valid() == False, "Passes if errors are found")
        self.assertTrue("Operator needs to have done 5 or more rescue operations" in output.messages, "Passes if rescue ops is under 5")        
        
    def test_add_to_store(self):
        #arrange
        operator = Operator()
        opstore = OperatorStore()
        operator.first_name = "Charlie"
        operator.date_of_birth = date(1997, 11, 23)
        operator.drone_license = 2
        operator.rescue_endorsement = True
        operator.operations = 5
        
        #act
        output = opstore.add(operator)
        output.commit()
        stored_op = opstore.get(operator.id)
        
        #assert
        self.assertTrue(stored_op.id == operator.id, "Passes if operator is logged into the store list")

if __name__ == '__main__':
    unittest.main()
