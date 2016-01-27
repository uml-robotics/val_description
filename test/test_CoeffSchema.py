#!/usr/bin/env python

import unittest
import glob, os
import CoeffSchemaDefinitions
from lxml import etree as xmlParser

class coeffFileTests(unittest.TestCase):

    def setUp(self):
        self.testDirectory = os.path.dirname(os.path.abspath(__file__))

    def tearDown(self):
        pass

    def testCoeffValidSchema(self):
        schema_root = xmlParser.XML(CoeffSchemaDefinitions.std_coeff)
        schema = xmlParser.XMLSchema(schema_root)
        parser = xmlParser.XMLParser(schema = schema)
        coeffFileDirectory = self.testDirectory + '/../instance/coefficients/actuators'
        os.chdir(coeffFileDirectory)
        for coeffFile in glob.glob("*.xml"):
            root = xmlParser.parse(coeffFile, parser)



