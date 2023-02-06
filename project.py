from assignment_generator.assignment_generator import generate_assignment

def main():
    test_data = '{\"title\":\"Title of an assignment\",\"description\":\"- This description\\n- Supports **markdown**\",\"tests\":{\"shown\":[{\"input\":[1,2,3,4,5],\"output\":\"1\",\"group\":\"group1\"},{\"input\":[1,2,3,4,5,232,-1,232,2],\"output\":\"-1\",\"group\":\"group1\"}],\"hidden\":[{\"input\":\"[]\",\"output\":\"None\",\"group\":\"hidden1\"},{\"input\":\"[1,1,1]\",\"output\":\"1\",\"group\":\"hidden2\"},{\"input\":\"[1]\",\"output\":\"1\",\"group\":\"hidden1\"},{\"input\":\"[0,-1,1]\",\"output\":\"-1\",\"group\":\"hidden2\"},{\"input\":\"[99,22,3,66]\",\"output\":\"3\",\"group\":\"hidden2\"}]},\"function_name\":\"get_minimum\"}'
    print(generate_assignment(test_data, './resources/assignment_template.md'))

if __name__ == "__main__":
    main()
