import xml.etree.ElementTree as ET
tree = ET.parse("medical.xml")
root = tree.getroot()

issues = []
for issue in root.findall("Issue"):
    issues.append(issue.text)

issues.sort()

print("Medical Issues (Alphabetical Order):")
for issue in issues:
    print(issue)
