import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   try:
      num = 7
      assert 7*7 == 40
   except AssertionError:
      print("Hello world")

def testequality():
   assert 10 == 10