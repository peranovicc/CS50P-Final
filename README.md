# Assignment generator and automatic grading system

#### Video Demo:  <URL HERE>

--------------------------------------------

### Description - Assignment  generator

- User input:
    - Assignment title
    - Assignment description
    - Test cases
        - Function or class + method name
        - Inputs and corresponding outputs
    - Hidden test cases that can be grouped (for easier grading) 

- Based on user input, program generates:
    - PDF with all assignment info
    - markdown file used in process (for potential manual adjusment)
    - Sample test file containing all test cases (both hidden and regular)

--------------------------------------------

### Description - Automatic grading system

- User input:
    - csv file with columns:
        - github username (ie `peranovicc`)
        - repository_name (ie `Quotes`)
        - path to file    (ie `src/service.js`)
    - `{path_to_test_file}` - path to test file used for grading

- Based on user input, program generates:
    - Grading report summary
    - Grading report for each student (in their folder)


 
