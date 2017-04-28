'''
Created on Nov 26, 2015

@author: Muresan
'''
import unittest
from Repository.ClientsRepository import *
from Domain.Clients import *


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repo= ClientsRepository()
        cl1=Clients(5,"Nico",1700925060074)
        cl2=Clients(6,"Nico",1700925060085)
        self.repo.add(cl1)
        self.repo.add(cl2)
        
    def testFind(self):
        c = self.repo.findById(5)
        self.assertTrue(c.getID()==5)
        c = self.repo.findById(6)
        
    def testRemove(self):
        self.repo.remove(5)
        self.assertEqual(len(self.repo),1,"Test failed")
        self.assertRaises(MovieException, self.repo.remove, 5) # No Error because it raises MovieException, 5 was already been removed 
        self.assertRaises(MovieException, self.repo.remove, 6) # AssertionError because the client 6 exist in the repo and can be removed
        
        