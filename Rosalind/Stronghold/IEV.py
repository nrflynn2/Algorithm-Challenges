import sys

def expectation(data):
    expectation = 2*(int(data[0]) + int(data[1]) + int(data[2]) + (3/4)*int(data[3]) + (1/2)*int(data[4])) 
    return expectation

def main():
    with open(sys.argv[1]) as f:
        data = f.read()
    data = data.split()
    expected_value = expectation(data)
    print(expected_value)

main()
