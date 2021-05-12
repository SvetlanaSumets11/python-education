''' Tris module implements tasks from https://www.learnpython.org/'''
import re


def print_hallo_world():
    ''' Use the "print" function to print the line "Hello, World!".'''
    print("Hello, World!")


def variables_and_types():
    '''
    The target of this exercise is to create a string, an integer, and a floating point number.
    The string should be named mystring and should contain the word "hello".
    The floating point number should be named myfloat and should contain the number 10.0,
    and the integer should be named myint and should contain the number 20.
    '''
    # change this code
    mystring = "hello"
    myfloat = 10.0
    myint = 20

    # testing code
    if mystring == "hello":
        print("String: %s" % mystring)
    if isinstance(myfloat, float) and myfloat == 10.0:
        print("Float: %f" % myfloat)
    if isinstance(myint, int) and myint == 20:
        print("Integer: %d" % myint)


def lists():
    '''
    In this exercise, you will need to add numbers and strings to the correct lists
    using the "append" list method. You must add the numbers 1,2, and 3 to the "numbers"
    list, and the words 'hello' and 'world' to the strings variable. You will also have to
    fill in the variable second_name with the second name in the names list, using
    the brackets operator []. Note that the index is zero-based, so if you want to access
    the second item in the list, its index will be 1.
    '''
    numbers = []
    strings = []
    names = ["John", "Eric", "Jessica"]

    # write your code here
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)

    strings.append("hello")
    strings.append("world")

    second_name = names[1]

    # this code should write out the filled arrays and the second name in the names list (Eric).
    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)


def basic_operators():
    '''
    The target of this exercise is to create two lists called x_list and y_list,
    which contain 10 instances of the variables x and y, respectively.
    You are also required to create a list called big_list, which contains the variables x and y,
    10 times each, by concatenating the two lists you have created.
    '''
    my_x = object()
    my_y = object()

    # Change this code
    x_list = [my_x] * 10
    y_list = [my_y] * 10
    big_list = x_list + y_list

    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list))

    # testing code
    if x_list.count(my_x) == 10 and y_list.count(my_y) == 10:
        print("Almost there...")
    if big_list.count(my_x) == 10 and big_list.count(my_y) == 10:
        print("Great!")


def string_formatting():
    '''
    You will need to write a format string which prints out the data using
    the following syntax: Hello John Doe. Your current balance is $53.44.
    '''
    data = ("John", "Doe", 53.44)
    format_string = "Hello %s %s. Your current balance is $%s."
    print(format_string % data)


def basic_string_operations():
    '''
    Try to fix the code to print out the correct information by changing the string.
    '''
    my_s = "Strings are awesome!"
    # Length should be 20
    print("Length of s = %d" % len(my_s))

    # First occurrence of "a" should be at index 8
    print("The first occurrence of the letter a = %d" % my_s.index("a"))

    # Number of a's should be 2
    print("a occurs %d times" % my_s.count("a"))

    # Slicing the string into bits
    print("The first five characters are '%s'" % my_s[:5]) # Start to 5
    print("The next five characters are '%s'" % my_s[5:10]) # 5 to 10
    print("The thirteenth character is '%s'" % my_s[12]) # Just number 12
    print("The characters with odd index are '%s'" % my_s[1::2]) #(0-based indexing)
    print("The last five characters are '%s'" % my_s[-5:]) # 5th-from-last to end

    # Convert everything to uppercase
    print("String in uppercase: %s" % my_s.upper())

    # Convert everything to lowercase
    print("String in lowercase: %s" % my_s.lower())

    # Check how a string starts
    if my_s.startswith("Str"):
        print("String starts with 'Str'. Good!")

    # Check how a string ends
    if my_s.endswith("ome!"):
        print("String ends with 'ome!'. Good!")

    # Split the string into three separate strings,
    # each containing only a word
    print("Split the words of the string: %s" % my_s.split(" "))


def conditions():
    '''
    Change the variables in the first section, so that each if statement resolves as True.
    '''
    # change this code
    number = 16
    second_number = 0
    first_array = [1, 2, 3]
    second_array = [1, 2]

    if number > 15:
        print("1")

    if first_array:
        print("2")

    if len(second_array) == 2:
        print("3")

    if len(first_array) + len(second_array) == 5:
        print("4")

    if first_array and first_array[0] == 1:
        print("5")

    if not second_number:
        print("6")


def loops():
    '''
    Loop through and print out all even numbers from the numbers list in the same
    order they are received. Don't print any numbers that come after 237 in the sequence.
    '''
    numbers = [
        951, 402, 984, 651, 360,  69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615,  83,
        165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462,
         47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758,
        219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815,  67, 104,  58,
        512,  24, 892, 894, 767, 553,  81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451,
        688, 753, 854, 685,  93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527]

    # your code goes here
    for num in numbers:
        if num == 237:
            break
        if not num % 2:
            print(num)


def list_benefits():
    ''' This function return lists '''
    # Modify this function to return a list of strings as defined above
    my_list = ["More organized code", "More readable code", "Easier code reuse",
                "Allowing programmers to share and connect code together"]
    return my_list


def build_sentence(benefit):
    ''' This function return string '''
    # Modify this function to concatenate to each benefit - " is a benefit of functions!"
    return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions():
    '''
    In this exercise you'll use an existing function, and while adding your own to create
    a fully functional program. Add a function named list_benefits() that returns the following
    list of strings: "More organized code", "More readable code", "Easier code reuse", "Allowing
    programmers to share and connect code together" Add a function named build_sentence(info)
    which receives a single argument containing a string and returns a sentence starting
    with the given string and ending with the string " is a benefit of functions!"
    Run and see all the functions work together!
    '''
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


def dictionaries():
    '''
    Add "Jake" to the phonebook with the phone number 938273443, and remove Jill from the phonebook.
    '''
    phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
    }
    # your code goes here
    phonebook["Jake"] = 938273443
    del phonebook["Jill"]

    # testing code
    if "Jake" in phonebook:
        print("Jake is listed in the phonebook.")

    if "Jill" not in phonebook:
        print("Jill is not listed in the phonebook.")


def modules_and_packages():
    '''
    In this exercise, you will need to print an alphabetically sorted list of
    all functions in the re module, which contain the word find.
    '''
    # Your code goes here
    # print(sorted([i for i in dir(re) if 'find' in i]))
    find_members = []
    for i in dir(re):
        if "find" in i:
            find_members.append(i)

    print(sorted(find_members))


# print_hallo_world()
# variables_and_types()
# lists()
# basic_operators()
# string_formatting()
# basic_string_operations()
# conditions()
# loops()
# name_the_benefits_of_functions()
# dictionaries()
# modules_and_packages()
