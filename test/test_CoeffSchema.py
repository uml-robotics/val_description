#!/usr/bin/env python

import unittest
import glob, os
import CoeffSchemaDefinitions as csd
from lxml import etree as xmlParser
import lxml
import logging

class coeffFileTests(unittest.TestCase):

    def setUp(self):
        self.testDirectory = os.path.dirname(os.path.abspath(__file__))

        # Define the directories that coeffs live in
        self.actuatorCoeffDirectory = self.testDirectory + '/../instance/coefficients/actuators'
        self.classCoeffDirectory = self.testDirectory + '/../instance/coefficients/class'
        self.controllerCoeffDirectory = self.testDirectory + '/../instance/coefficients/controllers'
        self.locationCoeffDirectory = self.testDirectory + '/../instance/coefficients/location'
        self.modesCoeffDirectory = self.testDirectory + '/../instance/coefficients/modes'
        self.safetyCoeffDirectory = self.testDirectory + '/../instance/coefficients/safety'
        self.sensorCoeffDirectory = self.testDirectory + '/../instance/coefficients/sensors'

        self.log = logging.getLogger("Coeff Test Logger")
        self.correctFiles = []
        self.incorrectFiles = []

    def tearDown(self):
        pass

    def getSchemaParser(self, schema_definition):
        schema_root = xmlParser.XML(schema_definition)
        schema = xmlParser.XMLSchema(schema_root)
        return xmlParser.XMLParser(schema = schema)

    def testActuatorCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.actuator_coeffs_definition + csd.header_coeff_definition + csd.properties_coeff_definition + csd.actuator_coeff_files_definition + csd.coeff_definition + csd.footer_coeff_definition
        parser = self.getSchemaParser(schema)
        os.chdir(self.actuatorCoeffDirectory)
        for coeffFile in glob.glob("*.xml"):
            try:
                root = xmlParser.parse(coeffFile, parser)
                self.correctFiles.append(coeffFile)
            except xmlParser.XMLSyntaxError:
                self.log.error(coeffFile + " has coeffs that are not in the schema")
                self.incorrectFiles.append(coeffFile)
        assert len(self.incorrectFiles) == 0


    def testClassCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.class_coeffs_definition + csd.header_coeff_definition + csd.actuator_class_info_definition + csd.coeff_definition + csd.footer_coeff_definition
        print schema
        parser = self.getSchemaParser(schema)
        os.chdir(self.classCoeffDirectory)
        for coeffFile in glob.glob("*.xml"):
            try:
                root = xmlParser.parse(coeffFile, parser)
                self.correctFiles.append(coeffFile)
            except xmlParser.XMLSyntaxError as e:
                self.log.error(coeffFile + " has coeffs that are not in the schema" + e.msg)
                self.incorrectFiles.append(coeffFile)
        assert len(self.incorrectFiles) == 0

    def testControllerCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.controller_coeffs_definition + csd.header_coeff_definition + csd.coeff_definition + csd.footer_coeff_definition
        print schema
        parser = self.getSchemaParser(schema)
        os.chdir(self.controllerCoeffDirectory)
        for coeffFile in glob.glob("*.xml"):
            try:
                root = xmlParser.parse(coeffFile, parser)
                self.correctFiles.append(coeffFile)
            except xmlParser.XMLSyntaxError as e:
                self.log.error(coeffFile + " has coeffs that are not in the schema" + e.msg)
                self.incorrectFiles.append(coeffFile)
        assert len(self.incorrectFiles) == 0

    def testLocationCoeffsValidSchema(self):
        pass

    def testModesCoeffsValidSchema(self):
        pass

    def testSafetyCoeffsValidSchema(self):
        pass

    def testSensorCoeffsValidSchema(self):
        pass
