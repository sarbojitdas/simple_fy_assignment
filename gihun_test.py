def guihun(k):

#k=int(input(" enter the number of test cases"))
    for i in range(0,k):
    
    # creating an empty list
        lst = []

        # number of elements as input
        n = int(input("Enter number of elements : "))

        # iterating till the range
        for i in range(0, n):
            ele = int(input())

            lst.append(ele) # adding the element
            
        
        k = int(input(" enter the height of ali and gihun"))

        # count the number of person greater than ali and gihun 
        count = 0
        for i in lst :
            if i > k :
                count = count + 1

        # printing the intersection
        print ("The number persons to be shot : " + str(count))

num=int(input(" enter the number of test cases"))
guihun(num)
