#!/usr/bin/env python

import unittest
import glob, os
import CoeffSchemaDefinitions
from lxml import etree as xmlParser
import lxml
import logging

class coeffFileTests(unittest.TestCase):

    def setUp(self):
        self.testDirectory = os.path.dirname(os.path.abspath(__file__))
        self.log = logging.getLogger("Coeff Test Logger")

    def tearDown(self):
        pass

    def testActuatorCoeffsValidSchema(self):
        schema_root = xmlParser.XML(CoeffSchemaDefinitions.std_coeff)
        schema = xmlParser.XMLSchema(schema_root)
        parser = xmlParser.XMLParser(schema = schema)
        coeffFileDirectory = self.testDirectory + '/../instance/coefficients/actuators'
        os.chdir(coeffFileDirectory)
        correctFiles = []
        incorrectFiles = []
        for coeffFile in glob.glob("*.xml"):
            try:
                root = xmlParser.parse(coeffFile, parser)
                correctFiles.append(coeffFile)
            except xmlParser.XMLSyntaxError:
                self.log.error(coeffFile + " has coeffs that are not in the schema")
                incorrectFiles.append(coeffFile)
        assert len(incorrectFiles) == 0


