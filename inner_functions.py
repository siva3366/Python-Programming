def parent_function():
    print("Printing from parent_function()")

    def first_child_function():
        print("Printing from first_child_function()")

    def second_child_function():
        print("Printing from second_child_function()")

    first_child_function()
    second_child_function()
    

parent_function()