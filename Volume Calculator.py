length , breadth , height , thing = input( 'Enter the length , breadth , height and object respectivly with a comma in between').split(',')
print('Here is the volume of your'+' '+thing.lower() )
print(int(length) * int(breadth) * int(height))