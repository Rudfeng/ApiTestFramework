import lib.HTMLTestRunner_PY3
import unittest
from script.test_script import TestLogin
from script.test_reg_script import TestRegister


suite = unittest.TestSuite()
suite.addTests(unittest.makeSuite(TestLogin))
suite.addTests(unittest.makeSuite(TestRegister))
with open("../report/report.html", mode='wb') as f:
    runner = lib.HTMLTestRunner_PY3.HTMLTestRunner(f)
    result = runner.run(suite)
    runner.generateReport(suite, result)
