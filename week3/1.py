def rpn(data):
    lis = []
    operators = ['-', '+', '*', '/']
    
    for element in data.split(' '):
        if element in operators:
            n1 = lis.pop()
            n2 = lis.pop()
            if element=='-': result = n2 - n1
            if element=='+': result = n2 + n1
            if element=='*': result = n2 * n1
            if element=='/': result = n2 / n1
            lis.append(result)
        else:
            lis.append(float(element))
 
    return lis.pop()

if __name__ == '__main__':
 
    data = '2 5 3 * + 10 2 / -'
    print(rpn(data))
    
