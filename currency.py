
# conver a number into rupees

def convert(input):
    

	# Find the length of the
	# input string
	Len = len(input)

	# Removing all the separators(, )
	# from the input string
	
	# Reverse the input string
	input=input[::-1]

	# Declaring the output string
	output = ""

	# Process the input string
	for i in range(Len):

		# Add a separator(, ) after the
		# third number
		if(i == 2 ):
			output += input[i]
			output += ","
		
		# Then add a separator(, ) after
		# every second number
		elif(i > 2 and i % 2 == 0 and
			i + 1 < Len):
			output += input[i]
			output += ","
        
		else:
			output += input[i]
	
	# Reverse the output string
	output=output[::-1]

	# Return the output string back
	# to the main function
	return output

# Driver code
#input1 = "504678"
input1=input(" enter the value")
print(convert(input1))


# This code is contributed by avanitrachhadiya2155
