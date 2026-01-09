from read_write import ReadWrite
FILE_PATH = r'code-python\day_20\notd\xml_read_write\data.txt'
OUTPUT_XML = r'code-python\day_20\notd\xml_read_write\car_data.xml'
car_read = ReadWrite()
car_data = car_read.read_car_data(FILE_PATH)
car_read.write_xml(car_data, OUTPUT_XML)