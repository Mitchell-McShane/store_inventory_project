import unittest

from models.worker import *

class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.roy_trenneman = Worker('Roy Trenneman', 41, 1979)
        self.maurice_moss = Worker('Maurice Moss',47, 1973)
        self.jen_barber = Worker('Jen Barber', 43, 1977)
        
    # test for true/false works
    def test_can_test(self):
        self.assertEqual(True, True)

    # test for workers names
    def test_worker_has_name(self):
        self.assertEqual('Roy Trenneman', self.roy_trenneman.name)
        self.assertEqual('Maurice Moss', self.maurice_moss.name)
        self.assertEqual('Jen Barber', self.jen_barber.name)

    # test for workers age
    def test_worker_has_age(self):
        self.assertEqual(41, self.roy_trenneman.age)
        self.assertEqual(47, self.maurice_moss.age)
        self.assertEqual(43, self.jen_barber.age)

    # test for workers dob (Date of Birth)
    def test_worker_dob(self):
        self.assertEqual(1979, self.roy_trenneman.dob)
        self.assertEqual(1973, self.maurice_moss.dob)
        self.assertEqual(1977, self.jen_barber.dob)