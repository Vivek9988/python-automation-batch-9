import xml.etree.ElementTree as ET

class ReadWrite():
    def read_car_data(self, filepath):
        cars = {}
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                key, value = line.split('=')
                car_id, attrib = key.split('.')
                if car_id not in cars:
                    cars[car_id] = {}
                cars[car_id][attrib] = value.strip()
        return cars

    def write_xml(self, cars, output_file):
        root = ET.Element('cars')
        for car_id, attrib in cars.items():
            car_elem = ET.SubElement(root, "car", id=car_id)
            for key, value in attrib.items():
                child = ET.SubElement(car_elem, key)
                child.text = value
        tree = ET.ElementTree(root)
        tree.write(output_file, encoding="utf-8")
        print("XML file written successfully")