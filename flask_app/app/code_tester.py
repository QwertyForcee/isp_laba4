import unittest
import os
import uuid
import re

class Tester:
    author_src = None
    tests = None
    user_src = None
    def __init__(self,author_src,user_src,user_name,tests):
        self.unique_filename = str(uuid.uuid4())+'.txt'
        self.author_src = author_src
        exec(user_src)
        self.user_src = eval(user_name)

        self.tests = eval(tests)
        self.testcase = self.create_testcase()

    async def run_tests(self):
        if self.isvalid():
            with open(self.unique_filename,'w') as f:
                suite = unittest.defaultTestLoader.loadTestsFromTestCase(self.testcase)
                #suite.addTest(self.testcase())
                unittest.TextTestRunner(f).run(suite)
            with open(self.unique_filename,'r') as f:
                res = f.read()
            os.remove(self.unique_filename)
            lines = res.split('\n')
            status = 'OK' in lines[len(lines)-2]
            return (status,res)
                #unittest.main(testRunner=runner)
        else:
            return (False,'Source code is not valid.')
            

    def create_testcase(self):
        class TestsContainer(unittest.TestCase):
            longMessage = True

        def make_test_function(description, a, b):
            def test(self):
                self.assertEqual(a, b, description)
            return test

        for name,params in self.tests.items():
            if isinstance(params[1],(list,tuple)):
                test_func = make_test_function(name,params[0],self.user_src(*params[1]))
            else:
                test_func = make_test_function(name,params[0],self.user_src(params[1]))

            setattr(TestsContainer,f"test_{name}",test_func)
        
        return TestsContainer
    def isvalid(self):
        #todO:
        #src code validation
        return True
