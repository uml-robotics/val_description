schema_header = '''
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
'''

actuator_coeffs_definition = \
'''
<xs:simpleType name="ValidCoeffs">
    <xs:restriction base="xs:string">
        <xs:enumeration value="AltVel_MountingGain"/>
        <xs:enumeration value="EncMountingDir"/>
        <xs:enumeration value="EncoderIndexOffset"/>
        <xs:enumeration value="JointKinematicDir"/>
        <xs:enumeration value="JointOutputAPS_MountingGain"/>
        <xs:enumeration value="JointSafety_LimitZone_Rad"/>
        <xs:enumeration value="JointSafety_LimitZone_m"/>
        <xs:enumeration value="JointSensors_MotorPosition"/>
        <xs:enumeration value="JointSensors_OutputForce"/>
        <xs:enumeration value="JointSensors_OutputPosition"/>
        <xs:enumeration value="JointSensors_OutputVelocity"/>
        <xs:enumeration value="JointSensors_LinearPosition"/>
        <xs:enumeration value="JointSensors_LinearVelocity"/>
        <xs:enumeration value="PositionOffset_Rad"/>
        <xs:enumeration value="SpringAPS_BitOffset"/>
        <xs:enumeration value="SpringAPS_MountingGain"/>
        <xs:enumeration value="LoadCell_MountingGain"/>
        <xs:enumeration value="LoadCell_OffsetBits"/>
        <xs:enumeration value="LoadCell_NmPerCount"/>
        <xs:enumeration value="TemperatureSensor_SensorLoc1"/>
        <xs:enumeration value="TorqueOffset_Nm"/>
        <xs:enumeration value="ForceOffset_N"/>
    </xs:restriction>
</xs:simpleType>
'''

class_coeffs_definition = \
'''
<xs:simpleType name="ValidCoeffs">
    <xs:restriction base="xs:string">
        <xs:enumeration value="CurrentSafeLimit"/>
        <xs:enumeration value="EncoderCPR"/>
        <xs:enumeration value="FluxLinkage"/>
        <xs:enumeration value="Inductance_DAxis"/>
        <xs:enumeration value="Inductance_QAxis"/>
        <xs:enumeration value="JointGearRatio"/>
        <xs:enumeration value="JointMaxValue"/>
        <xs:enumeration value="JointMinValue"/>
        <xs:enumeration value="JointOutputAPS_CountsToRad"/>
        <xs:enumeration value="MotorWindingType"/>
        <xs:enumeration value="NumberOfPoles"/>
        <xs:enumeration value="Renishaw_CountsToRad"/>
        <xs:enumeration value="SpringStiffness"/>
        <xs:enumeration value="WindingResistance"/>
    </xs:restriction>
</xs:simpleType>
'''

actuator_coeff_files_definition = \
'''
<xs:element name="ClassFile">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="ControllerFile">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="LocationFile">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="SensorsFile">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="SafetyFile">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
<xs:element name="ModeFile">
      <xs:complexType>
            <xs:attribute name="id" type="xs:string"></xs:attribute>
      </xs:complexType>
</xs:element>
'''

header_coeff_definition = \
'''
    <xs:element name="CoeffData">
        <xs:complexType>
        <xs:sequence>
            <xs:element name="Properties">
                <xs:complexType>
                <xs:sequence>
                    <xs:element name="CalibrationDate"></xs:element>
                    <xs:element name="FileGenDate">
                        <xs:complexType>
                            <xs:attribute name="date" type="xs:date"></xs:attribute>
                            <xs:attribute name="time" type="xs:string"></xs:attribute>
                        </xs:complexType>
                    </xs:element>
                </xs:sequence>
                </xs:complexType>
            </xs:element>
'''

footer_coeff_definition = \
'''
             </xs:element>
        </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
'''

coeff_definition = \
'''
                  <xs:element name="Coeffs">
                  <xs:complexType>
                  <xs:sequence>
                      <xs:element name="Coeff" maxOccurs="unbounded">
                            <xs:complexType>
                                  <xs:attribute name="id" type="ValidCoeffs"/>
                                  <xs:attribute name="description" type="xs:string"/>
                                  <xs:attribute name="value" type="xs:float"/>
                            </xs:complexType>
                      </xs:element>
                  </xs:sequence>
                  </xs:complexType>
'''
