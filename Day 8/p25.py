# Context Manager
# Context Manager like a Hotel room
# You check in (setup)
# You stay in the room (the code block)
# You check out (teardown) - Automatically Done 
# Thew room is cleaned and kept ready for the next guest 

# File Handling 
file = None 
try:
    file = open ('example.txt')
    content = file.read()
    print (content)

finally:
    if file :
        file.close()


# Multiple Context Managers 
with open('example.txt','r') as input_file, open('output.txt','w') as output_file:
    content = input_file
    output_file.write(content)