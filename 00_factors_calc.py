# functions go here

# puts series of symbols at start and end of text
def statement_generator(text, decoration):

    # make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# display instructions / information
def instructions():
   
    statement_generator("instructions / information", "=")
    print()
    print("please choose a data type (image/text/ integer)")
    print()
    print("this program assumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). for text, we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""





# check input is a number more than a given value
#  
def num_check (question):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than 1 and less than 200: "
        

        try:
            
            #ask user to enter a number
            response = int(input(question))
            
            # check number is more than zero
            if 0 < response < 201:
                return response
            
            #outputs error if input is invalid
            else:
                print(error)
                print() 

        except ValueError:
            print(error)

def get_factor():
     # list to hold factors
    factors = []

    # square root to factoe to find 'half way'
    limit = int(to_factor ** 0.5)

    # find factor pairs and add to list
    for item in range (1, limit + 1):

        # check factor is not 1 (unity)
        if to_factor == 1:
            break

        # check if number is a factor
        result = 
        factor_1 =

        # add factor to list if it is not already in there
        if result == 0:


        if factor_1 != item and result ==0:

        # sort list 
        factor.sort()      

        return factors  




# main routine

# heading
statement_generator("Factors Calculator", "-")\

# display instructions if user has not used the program before
first_time = input("press <enter> to see the instructions or any key to continue")

if first_time == "": 
    instructions()

# loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factorised
    var_to_factor = num_check("number?")

    if var_to_factor != 1:
        factor_list = get_factor(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! it only has ne factor. Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor) 

    # output factors and comment 

    # generate heading...
    if var_to_factor == 1:
        heading = "factor of {}".format(var_to_factor)

    # output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("press <enter> to continue or any key to quit")
    print()  

print()
print("thank you for using the factors calculator")
print()
