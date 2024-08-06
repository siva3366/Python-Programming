def remove_duplicates(input_string):
    seen={}
    result=[]
    for char in input_string:
        if char not in seen:
            seen[char]=True
            result.append(char)

    return ''.join(result)

input_string="SivaReddy Siva"
output_string=remove_duplicates(input_string)
print(output_string)