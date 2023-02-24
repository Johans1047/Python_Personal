"""
--- 
Data Format Problem
A company has a system that obtains all the information from its customers, it has a method to collect the data obtaining this format:
"Abel Murgas 25" Name last name Age, and the company want to change the format supported by the Database.
...
Important things:
1. Some customers have a middle name and maternal last name: "Abel Jazir Murgas Tapia 25"
2. Some customers write their first or last name in lower case: "abel jazir Murgas tapia 25"
3. Some clients do not put their age: "Abel Jazir Murgas Tapia"
The expected result:
The method must be able to change this format:
"
abel murgas tapia 25
Carmen Ortega 30
july ruiz
roberto lopez
Marta Campos" (str)
to:
[
    [1,Abel,Murgas,Tapia,25],
    [2, Carmen, Ortega, 30],
    [3, Julio, Ruiz, None],
    [4, Roberto, Lopez, None],
    [5,Marta, Campos, None]
] (list)
Validation:
1- Names and lastname must begin with a capital letter
2- If the client has no age, you must put None in the last position of the list
3- Each client must have a unique code
4- The client renders a vector inside the main list
¡Good luck!
Data example (use to test):
"""
clients_example = """Abel Murgas Tapia 25
Raul ortega martinez 10
paul Walker
martin Ruiz 100
carlos juan martinez castillo"""

result_expected = [
    ["Abel","Murgas","Tapia",25],
    ["Raul","Ortega","Martinez",10],
    ["Paul","Walker",None],
    ["Martin","Ruiz",100],
    ["Carlos","Juan","Martinez","Castillo", None]
]

def divide_sentences(clients:str) -> list:
    """
    This method is to split each line of the string into a list

    Args:
        clients (str): string variable

    Returns:
        list: phrases
    """
    phrases = clients.splitlines()
        
    return phrases

def number_of_lines(clients:str) -> int:
    """This method is to count the number of lines in the initial string

    Args:
        clients (str): string variable

    Returns:
        int: lines_number
    """
    
    lines = clients.split("\n")
    lines_number = len(lines)
    
    return lines_number
    
def divide_words(name:str) -> list:
    """This method is for converting each string into a list and adding the word 'None' if there is no age.

    Args:
        name (str): string variable

    Returns:
        list: words
    """ 
    words = name.split()
    
    if name[-1].isdigit() == False:
    
        words.append("None")
    
    return words
    
def capital_letter(word:list) -> list:
    """This method is for transforming lowercase names into uppercase. 
    The first for loop checks if the first letter of each word is lowercase, if it is, 
    it takes the first letter and converts it to uppercase in a new variable. Then, another 
    variable uses the replace() function to remove the first letter, and in a final variable, 
    the variable with the uppercase letter is concatenated with the variable containing the 
    rest of the word. Once this is done, the corrected word is inserted into the last position
    of the list using the insert() function.
    
    We create a list and in a for loop we check if the first letter of a word is lowercase. 
    If it is, we save its position and store it in the list.
    
    Finally, we create a new for loop that iterates over the entire length of the previously 
    created list. Then we use the 'del list_name[index]' function to remove the lowercase words 
    from the first detected position to the last detected position (hence the size of the list).

    Args:
        word (list): list variable

    Returns:
        list: word
    """
    
    for wrd in word:#poner la mayuscula
        
        if wrd[0].islower() == True:
        
            Upper_wrd = wrd[0].upper()
            
            wrd1 = wrd.replace(wrd[0],"")
            concatenate = Upper_wrd + wrd1
            
            word.insert(-1, concatenate)

    numbers = []
    
    for wrd in word:#tomar posicion
                
        if wrd[0].islower() == True:
            index_position = word.index(wrd)
            numbers.append(index_position)
            
    for number in range(len(numbers)):# eliminar sobrantes
        
        del word[numbers[0]]

    return word

def unique_code(words:list, number:int) -> list:
    """This method is to add the password on each list at the first position.

    Args:
        words (list): first variable, contains the list with the names ang age
        number (int): second variable, contains the number of the line, the password.

    Returns:
        list: words
    """
    
    words.insert(0, number)
    
    return words

def str_to_int(words:list) -> list:
    """This method is for converting the age from string to integer. If the last element 
    of the list is a number or digit [using isdigit()], it is extracted into a variable 
    using the pop() function. Then, the previous variable is converted to an integer using 
    the int() function in a new variable, and the age is added back to the list using the 
    append() function.

    Args:
        words (list): list variable

    Returns:
        list: words
    """
    
    if words[-1].isdigit() == True:
        num = words.pop()
        convert = int(num)
        words.append(convert)
        
    return words
    
def str_to_none(words:list) -> list:
    """This method is for converting the none from string to the actual value 'None'. If the 
    last element of the list is a string [using isinstance()], it is extracted into a variable 
    using the 'del list_name[index]' function. Then, the previous variable is converted to 'None'
    or empty assigning that value to a new variable, and the value is added back to the list 
    using the append() function.

    Args:
        words (list): list variable

    Returns:
        list: words
    """
    
    if isinstance(words[-1], str) == True:
    
        del words[-1]
        convert = None
        words.append(convert)
   
    return words

clients = """
abel murgas tapia 25
Carmen Ortega 30
july ruiz
roberrto lopez
Marta Campos"""

sentences = divide_sentences(clients)
lines = number_of_lines(clients)

for i in range(1,lines):
    
    sentence = sentences[i]

results_expected = []

for i in range(1,len(sentences)):
    
    function1 = divide_words(sentences[i])
    function2 = capital_letter(function1)
    function3 = unique_code(function2, i)
    function4 = str_to_int(function3)
    function5 = str_to_none(function4)
    results_expected.append(function5)
    
print(results_expected)  
    