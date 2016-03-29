#!/usr/bin/env python

import unittest
import glob, os
import CoeffSchemaDefinitions as csd
import CoeffCollectionDefinitions as ccd
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

    def checkForDuplicates(self, directory):
        # Assemble the schema
        os.chdir(directory)
        for coeffFile in glob.glob("*.xml"):
            try:
                xmlCoeffObject = xmlParser.parse(coeffFile)
                coeffNames = []
                for coeff in xmlCoeffObject.iter('Coeff'):
                    coeffNames.append(coeff.get('id'))
                if len(coeffNames) != len(set(coeffNames)):
                    raise Exception
            except Exception:
                self.log.error(coeffFile + " has duplicate coeffs")
                self.incorrectFiles.append(coeffFile)
        assert len(self.incorrectFiles) == 0

    def checkForNeeded(self, directory, neededCoeffs):
        # Assemble the schema
        os.chdir(directory)
        for coeffFile in glob.glob("*.xml"):
            try:
                xmlCoeffObject = xmlParser.parse(coeffFile)
                coeffNames = []
                for coeff in xmlCoeffObject.iter('Coeff'):
                    coeffNames.append(coeff.get('id'))
                for coeff in neededCoeffs:
                    if coeff not in coeffNames:
                        raise Exception
            except Exception:
                self.log.error(coeffFile + " is missing a needed coeff " + coeff)
                self.incorrectFiles.append(coeffFile)
        assert len(self.incorrectFiles) == 0

    def checkValidSchema(self, schema, directory):
        parser = self.getSchemaParser(schema)
        os.chdir(directory)
        for coeffFile in glob.glob("*.xml"):
            try:
                root = xmlParser.parse(coeffFile, parser)
                self.correctFiles.append(coeffFile)
            except xmlParser.XMLSyntaxError:
                self.log.error(coeffFile + " has coeffs that are not in the schema")
                self.incorrectFiles.append(coeffFile)
        assert len(self.incorrectFiles) == 0

    ####################################################################################
    #    Check that actuator coeff files only have coeffs that should be in them.      #
    ####################################################################################
    def testActuatorCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.actuator_coeffs_definition + csd.header_coeff_definition + csd.properties_coeff_definition + csd.actuator_coeff_files_definition + csd.coeff_definition + csd.footer_coeff_definition
        self.checkValidSchema(schema, self.actuatorCoeffDirectory)

    ####################################################################################
    #    Check that actuator coeff files have no duplicate coeffs.                     #
    ####################################################################################
    def testActuatorNoDuplicateCoeffs(self):
        self.checkForDuplicates(self.actuatorCoeffDirectory)

    ####################################################################################
    #    Check that actuator coeff files have coeffs that need to be in them.          #
    ####################################################################################
    def testActuatorEssentialCoeffs(self):
        self.checkForNeeded(self.actuatorCoeffDirectory, ccd.ActuatorNeededCoeffs)

    ####################################################################################
    #    Check that class coeff files only have coeffs that should be in them.         #
    ####################################################################################
    def testClassCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.class_coeffs_definition + csd.header_coeff_definition + csd.actuator_class_info_definition + csd.coeff_definition + csd.footer_coeff_definition
        self.checkValidSchema(schema, self.classCoeffDirectory)

    ####################################################################################
    #    Check that class coeff files have no duplicate coeffs.                        #
    ####################################################################################
    def testClassNoDuplicateCoeffs(self):
        self.checkForDuplicates(self.classCoeffDirectory)

    ####################################################################################
    #    Check that class coeff files have coeffs that need to be in them.             #
    ####################################################################################
    def testClassEssentialCoeffs(self):
        self.checkForNeeded(self.classCoeffDirectory, ccd.ClassNeededCoeffs)

    ####################################################################################
    #    Check that controller coeff files only have coeffs that should be in them.    #
    ####################################################################################
    def testControllerCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.controller_coeffs_definition + csd.header_coeff_definition + csd.coeff_definition + csd.footer_coeff_definition
        self.checkValidSchema(schema, self.controllerCoeffDirectory)

    ####################################################################################
    #    Check that controller coeff files have no duplicate coeffs.                   #
    ####################################################################################
    def testControllerNoDuplicateCoeffs(self):
        self.checkForDuplicates(self.controllerCoeffDirectory)

    ####################################################################################
    #    Check that controller coeff files have coeffs that need to be in them.        #
    ####################################################################################
    def testControllerEssentialCoeffs(self):
        self.checkForNeeded(self.controllerCoeffDirectory, ccd.ControllerNeededCoeffs)

    ####################################################################################
    #    Check that location coeff files only have coeffs that should be in them.      #
    ####################################################################################
    def testLocationCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.location_coeffs_definition + csd.header_coeff_definition + csd.coeff_definition + csd.footer_coeff_definition
        self.checkValidSchema(schema, self.controllerCoeffDirectory)

    ####################################################################################
    #    Check that location coeff files have no duplicate coeffs.                     #
    ####################################################################################
    def testLocationNoDuplicateCoeffs(self):
        self.checkForDuplicates(self.locationCoeffDirectory)

    ####################################################################################
    #    Check that location coeff files have coeffs that need to be in them.          #
    ####################################################################################
    def testLocationEssentialCoeffs(self):
        self.checkForNeeded(self.locationCoeffDirectory, ccd.LocationNeededCoeffs)

    ####################################################################################
    #    Check that mode coeff files only have coeffs that should be in them.          #
    ####################################################################################
    def testModesCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.modes_coeffs_definition + csd.header_coeff_definition + csd.coeff_definition + csd.footer_coeff_definition
        self.checkValidSchema(schema, self.controllerCoeffDirectory)

    ####################################################################################
    #    Check that mode coeff files have no duplicate coeffs.                         #
    ####################################################################################
    def testModeNoDuplicateCoeffs(self):
        self.checkForDuplicates(self.modesCoeffDirectory)

    ####################################################################################
    #    Check that mode coeff files have coeffs that need to be in them.              #
    ####################################################################################
    def testModeEssentialCoeffs(self):
        self.checkForNeeded(self.modesCoeffDirectory, ccd.ModesNeededCoeffs)

    ####################################################################################
    #    Check that safety coeff files only have coeffs that should be in them.        #
    ####################################################################################
    def testSafetyCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.safety_coeffs_definition + csd.header_coeff_definition + csd.coeff_definition + csd.footer_coeff_definition
        self.checkValidSchema(schema, self.controllerCoeffDirectory)

    ####################################################################################
    #    Check that safety coeff files have no duplicate coeffs.                       #
    ####################################################################################
    def testSafetyNoDuplicateCoeffs(self):
        self.checkForDuplicates(self.safetyCoeffDirectory)

    ####################################################################################
    #    Check that safety coeff files have coeffs that need to be in them.            #
    ####################################################################################
    def testSafetyEssentialCoeffs(self):
        self.checkForNeeded(self.safetyCoeffDirectory, ccd.SafetyNeededCoeffs)

    ####################################################################################
    #    Check that sensor coeff files only have coeffs that should be in them.        #
    ####################################################################################
    def testSensorCoeffsValidSchema(self):
        # Assemble the schema
        schema = csd.schema_header + csd.sensor_coeffs_definition + csd.header_coeff_definition + csd.coeff_definition + csd.footer_coeff_definition
        self.checkValidSchema(schema, self.controllerCoeffDirectory)

    ####################################################################################
    #    Check that sensor coeff files have no duplicate coeffs.                       #
    ####################################################################################
    def testSensorNoDuplicateCoeffs(self):
        self.checkForDuplicates(self.sensorCoeffDirectory)

    ####################################################################################
    #    Check that sensor coeff files have coeffs that need to be in them.            #
    ####################################################################################
    def testSensorEssentialCoeffs(self):
        self.checkForNeeded(self.sensorCoeffDirectory, ccd.SensorNeededCoeffs)
