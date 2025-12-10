# gedcom_to_csv.py
# Python 3.8+ required
# Install once: pip install gedcom-parser

from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser, FAMILY_MEMBERS_TYPE_ALL, FAMILY_MEMBERS_TYPE_PARENTS, FAMILY_MEMBERS_TYPE_CHILDREN
from gedcom import tags
import csv
from pathlib import Path

# ====================== CONFIGURATION ======================
GEDCOM_FILE = "HendricksonGEDCOM7.ged"   # ← Change this to your file
OUTPUT_CSV = "family_data.csv"                 # Output CSV file
# ===========================================================

def get_full_name(person):
    """Get full name as a single string"""
    first = person.get_name()[0] or ""
    last = person.get_name()[1] or ""
    return f"{first} {last}".strip()

def get_parents_names(parser, person):
    """Get parents' names as semicolon-separated string"""
    parents = parser.get_parents(person)
    if not parents:
        return ""
    names = [get_full_name(p) for p in parents]
    return "; ".join(names)

def get_spouses_names(parser, person):
    """Get spouses' names as semicolon-separated string"""
    # Get families where this person is a spouse
    families = parser.get_families(person, tags.GEDCOM_TAG_FAMILY_SPOUSE)
    if not families:
        return ""
    spouse_names = []
    for family in families:
        # Get parents from this family (should be the person and their spouse)
        parents = parser.get_family_members(family, FAMILY_MEMBERS_TYPE_PARENTS)
        for parent in parents:
            if parent != person:  # The other parent is the spouse
                spouse_names.append(get_full_name(parent))
                break
    return "; ".join(spouse_names)

def get_children_names(parser, person):
    """Get children's names as semicolon-separated string"""
    # Get families where this person is a spouse (parent)
    families = parser.get_families(person, tags.GEDCOM_TAG_FAMILY_SPOUSE)
    if not families:
        return ""
    children_names = []
    for family in families:
        # Get children from each family
        children = parser.get_family_members(family, FAMILY_MEMBERS_TYPE_CHILDREN)
        for child in children:
            children_names.append(get_full_name(child))
    return "; ".join(children_names)

def extract_person_data(parser, person):
    """Extract all relevant data from a person record"""
    birth = person.get_birth_data()
    death = person.get_death_data()
    
    return {
        'ID': person.get_pointer().replace('@', '') if person.get_pointer() else '',
        'First Name': person.get_name()[0] or '',
        'Last Name': person.get_name()[1] or '',
        'Full Name': get_full_name(person),
        'Gender': person.get_gender() or '',
        'Birth Date': birth[0] if birth and birth[0] else '',
        'Birth Place': birth[1] if birth and birth[1] else '',
        'Death Date': death[0] if death and death[0] else '',
        'Death Place': death[1] if death and death[1] else '',
        'Parents': get_parents_names(parser, person),
        'Spouses': get_spouses_names(parser, person),
        'Children': get_children_names(parser, person),
    }

def main():
    if not Path(GEDCOM_FILE).exists():
        print(f"Error: GEDCOM file not found: {GEDCOM_FILE}")
        print("   Put your exported .ged file in the same folder and rename it or edit the GEDCOM_FILE variable.")
        return
    
    print(f"Parsing GEDCOM file: {GEDCOM_FILE}")
    parser = Parser()
    parser.parse_file(GEDCOM_FILE, False)
    
    # Get all individuals from the GEDCOM file
    individuals = [element for element in parser.get_root_child_elements() 
                   if isinstance(element, IndividualElement)]
    
    print(f"Found {len(individuals)} individuals. Converting to CSV...")
    
    # Define CSV columns
    fieldnames = [
        'ID', 'First Name', 'Last Name', 'Full Name', 'Gender',
        'Birth Date', 'Birth Place', 'Death Date', 'Death Place',
        'Parents', 'Spouses', 'Children'
    ]
    
    # Write to CSV
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for i, person in enumerate(individuals, 1):
            data = extract_person_data(parser, person)
            writer.writerow(data)
            if i % 100 == 0:
                print(f"  Processed {i}/{len(individuals)} individuals...")
    
    print(f"\nDone! CSV file created:\n   {Path(OUTPUT_CSV).absolute()}")
    print(f"   Total records: {len(individuals)}")

if __name__ == "__main__":
    main()



