from Bio import ExPASy
from Bio import SwissProt
import sys

# Note: Syntax references functions but in actuality this will find GO 
# terms involved in biological processes

def find_function(prot):
    handle = ExPASy.get_sprot_raw(prot) # Can give several IDs separated by commas
    record = SwissProt.read(handle) # Use SwissProt.parse for multiple proteins  

    functions = []
    for ref in record.cross_references:
        if ref[0] == 'GO' and ref[2][0] == 'P':
            print(ref)
            functions.append(ref[2][2:])
    return functions

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
    data = data.strip('\n')
    go_functions = find_function(data)
    print('\n'.join(go_functions))

main()
