def StringCode():

    stringA = 'Abcde'
    stringB = "School"
    print('The type of stringA is %s' % type(stringA))
    print('The type of stringB is %s' % type(stringB))

    for alpha in stringA:
        print(alpha)
    
    for idx in range(len(stringA)):
        print('No.%s alpha is %s' % (idx, stringA[idx]))

    stringA.replace(stringA[0],'xyc')
    print(stringA)

    stringA = stringA.replace(stringA[0],'xyc')
    print(stringA)

    stringD = stringA + 'xyz'
    print(stringD)

    print(stringA[1:5])
    print(stringA[1:-1])
    print(stringA[1:])

def ListCode():
    import numpy as np
    list_a = [1,2,3,4,5]
    list_b = [1,'23','xixi',2,45]
    print(list_a)
    print(list_b)

    for item in list_b:
        print(item)
    list_c = list([1,2,3])
    array_b = np.array(list_b, ndmin=2)
    print(array_b)
    print(list_c)

    print(type(list_b))
    print(type(array_b))
    
    list_d = [[1,2,3],[4,5,6],[7,8,9]]
    print(list_d)
    print(list_d)
    
    array_d = np.array(list_d,ndmin=2)
    print(array_d)
    print(array_d.shape)

    matrix_d = np.matrix(list_d)
    print(matrix_d)
    print(matrix_d.shape)
    
    array_d.shape = (1,9)
    print('array_d shape 1,9')
    print(array_d)

    matrix_d.shape = (1,9)
    print('matrix_d shape 1,9')
    print(matrix_d)

    array_d.reshape(3,3)
    print(array_d)

    matrix_d.reshape(3,3)
    print(matrix_d)

    array_d = array_d.reshape(3,3)
    print(array_d)

    matrix_d = matrix_d.reshape(3,3)
    print(matrix_d)

    list_e = [1,2,3]
    list_e.append(56)
    print(list_e)
    list_e.append([90,1901])
    print(list_e)

    list_f = [1,2,3]
    list_f.extend([90,1101])
    print(list_f)









ListCode()