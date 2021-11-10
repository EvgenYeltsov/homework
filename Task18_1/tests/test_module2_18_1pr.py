import unittest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from app.module2_18_1practice import Bike


class TestBikeAvgSpeed(unittest.TestCase):

    def setUp(self):
        self.bike = Bike()

    def test_distance(self):
        self.bike._avg_speed_ph = 30
        self.assertEqual(self.bike.cover_distance(60), f"I am a bike. It takes me about 2.0 hours")



