'''
Tool for generating assignments and tests based on payload

{
  "title": "string",
  "description": "string",
  "tests":{
    "shown":[("input","output","group"),...],
    "hidden":[("input","output","group"),...],
    "function_name": "string"
  }
}
'''

def generate_assignment(json_payload):
    '''
    Create and return markdown based on json_payload

    Markdown is generated with a template

    Template must include:
    - {{TITLE}}
    - {{DESCRIPTION}}
    - {{FUNCTION_NAME}}
    - {{INPUT_OUTPUT_TABLE}}
        - |{INPUT}|{OUTPUT}| for each test 
    '''

    

def generate_tests(json_payload):
    '''
    Returns usable test file as a string

    Each test case is one assertion
    Assertions are grouped in separated test functions
    '''



def main():
    print('Assignment generator')

if __name__ == "__main__":
    main()
