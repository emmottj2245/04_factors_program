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
