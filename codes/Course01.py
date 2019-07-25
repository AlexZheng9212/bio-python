if __name__ == "__main__":

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

