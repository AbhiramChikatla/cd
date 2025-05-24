import xml.etree.ElementTree as ET

def parser(xml_string):
    """Parses an XML string and prints it in a tree-like structure."""
    try:
        root = ET.fromstring(xml_string)  # Parse XML
        print_tree(root)  # Print tree structure
    except ET.ParseError as e:
        print("XML Parsing Error:", e)

def print_tree(element, indent=0):
    """Recursively prints XML elements as a tree structure."""
    print("  " * indent + f"└── <{element.tag}>")

    for child in element:
        print_tree(child, indent + 1)  # Recursively print children
    
    if element.text and element.text.strip():
        print("  " * (indent + 1) + f"└── {element.text.strip()}")  # Print text content

# Example XML input
xml_input = """<root>
    <name>John</name>
    <age>25</age>
    <address>
        <city>New York</city>
        <zip>10001</zip>
    </address>
</root>"""

# Run the parser
print(xml_input)
print("-------")
parser(xml_input)