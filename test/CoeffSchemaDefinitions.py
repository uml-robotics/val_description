std_coeff = \
'''
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified" attributeFormDefault="unqualified">
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
                  <xs:element name="Coeffs">
                  <xs:complexType>
                  <xs:sequence>
                      <xs:element name="Coeff" maxOccurs="unbounded">
                            <xs:complexType>
                                  <xs:attribute name="id" type="xs:string"/>
                                  <xs:attribute name="description" type="xs:string"/>
                                  <xs:attribute name="value" type="xs:float"/>
                            </xs:complexType>
                      </xs:element>
                  </xs:sequence>
                  </xs:complexType>
             </xs:element>
        </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
'''
