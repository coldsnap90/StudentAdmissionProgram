import unittest
import studentadmissionsprogram
from studentadmissionsprogram import domesticStudent as domStu

class testStudentAdmissionsProgram(unittest.TestCase):
    domesticStudent = domStu.domesticStudent()
    
    def test(self):
        self.domStu.set_first_name('john')
        print(self.domStu.get_first_name())

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
