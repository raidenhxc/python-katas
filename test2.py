def valid_parentheses(string):
    counter = 0
    for character in string:
        if character == "(":
            counter += 1
        elif character == ")":
            counter -=1
            
        if counter<0:
            break;
        
    if counter == 0:
        return True
    else:
        return False


print (valid_parentheses("hola()) (qué tal)"))