from itertools import groupby

def main():
    
    # List of string 
    list1 = ['Hi' ,  'hello', 'at', 'this', 'there', 'from']
    
    # List of string
    list2 = ['there' , 'hello', 'Hi']
    
    '''    
        check if list1 contains all elements in list2
    '''
    result =  all(elem in list1  for elem in list2)
    
    if result:
        print("Yes, list1 contains all elements in list2")    
    else :
        print("No, list1 does not contains all elements in list2")    
        
    
    '''    
        check if list1 contains any elements of list2
    '''
    result =  any(elem in list1  for elem in list2)
    
    if result:
        print("Yes, list1 contains any elements of list2")    
    else :
        print("No, list1 contains any elements of list2")        

def demo1():
    
    list1 = ['x' , 'AND', 'y']
    list2 = ['x']
    list3 = ['x', 'y']
    
    print(all(elem in list1  for elem in list2))
    look_vals = [list1[0],list1[2]]
    print(all(elem in list2  for elem in look_vals))
    print(all(elem in list3  for elem in look_vals))


def demo2():
    c = "6#666#665533999"
    c_out = ["".join(g) for k, g in groupby(c) if k != '#']
    print(c_out)
    #['6', '666', '66', '55', '33', '999']

    c = "111221"
    c_out = ["".join(g) for k, g in groupby(c)]
    print(c_out)
        



if __name__ == '__main__':
    main()
    demo1()
    demo2()