# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# EWaktola,9.7.2021,Modified code to complete assignment 8
# EWaktola,9.8.2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt' # The name of the data file
list_of_product_objects = []     # A list of product objects
strStatus = ''


class Product():
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        EWaktola,9.7.2021,Modified code to complete assignment 8
    """

    # -- Constructor --
    def __init__(self,  product_name='', product_price=''):
        # -- Attributes --
        self.product_name = product_name
        self.product_price = product_price

    def __str__(self):
        product_name = self.__product_name
        product_price = str(self.__product_price)
        product_data = product_name.strip() + ', ' + product_price.strip()
        return product_data  # a string with product name and price separated by a comma

    # -- Properites --
    # -- product_name
    @property
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter
    def product_name(self, value):
        value= value.strip()
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception('Product names cannot be numbers')
    # -- product_price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        try:
            self.__product_price = float(value)
        except:
            print('Product price must be a number')

class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        read_data_from_file(file_name): -> (a list of product objects)
        save_data_to_file(file_name, list_of_product_objects):
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        EWaktola,9.7.2021,Modified code to complete assignment 8
    """

    # Code to process data to a file

    @staticmethod
    def read_data_from_file(file_name):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: string with name of file:
        :return: list of product objects, status
        """
        list_of_product_objects = []  # local variable, list of products names & prices
        status = 'There is no data saved in the file.'
        try:
            file = open(file_name, "r")
            for line in file:
                product_name, product_price = [s.strip() for s in line.split(',')]
                product_object = Product(product_name, product_price)  # create a product object
                list_of_product_objects.append(product_object)
                status = 'Data read from file.'
            file.close()
        except:
            print(status)
        return list_of_product_objects

    @staticmethod
    def add_product_to_list(product, price, lstOfProductObjects):
        """ Adds user input data (product, price) as product object to a list
        :param product: (string) product
        :param price: (string) price of product
        :param lstOfProductObjects: (list) of product objects
        :return:(list) of product objects
        """
        product_1 = Product(product, price)
        lstOfProductObjects.append(product_1)
        status = 'Product name and price were added to list.'
        return lstOfProductObjects, status

    @staticmethod
    def write_data_to_file(file_name, lstOfProductObjects):
        """ Write data from a list of dictionary rows into a file
        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) of dictionary rows:
        :return: status
        """
        status = 'No data to save, Add a new product.'
        try:
            file = open(file_name, "w")
            if lstOfProductObjects != []:    # check that list is not empty
                for row in lstOfProductObjects:
                    row = row.__str__()      # gets the product info saved as a string
                    file.write(row + '\n')
                    status = 'Success, Your data has been saved'
            file.close()
        except:
            print(status)
        return status

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output products """

    @staticmethod
    def print_menu_products():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options:
        1) Add a new product name & price
        2) Show product name & price list
        3) Save Data to File   
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: choice
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Products_in_list(lstOfProductObjects):
        """ Shows the current products in list of product ojbects
        :param lstOfProductObjects: list of product names and prices
        :return: nothing
        """
        print("******* Current product names and prices are: *******")
        if lstOfProductObjects != []:  # check whether list is empty
            for row in lstOfProductObjects:
                row = row.__str__()  # gets the product info saved as a string
                print(row.strip())
        else:
            print(' ' * 8+'There are no entries in the list.')
        print('*' * 53)
        print()  # Add an extra line for looks
    @staticmethod
    def input_new_product():
        """ Asks user to input new product
        :return: (strings) product name
        """
        productName = input("Enter product name: ")
        productPrice = input("Enter product price: ")
        product_1 = Product(productName,productPrice)                   # instantiate an object from the class Product
        return product_1,product_1.product_name, product_1.product_price

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print('\n'+optional_message)
        print()
        input('Press the [Enter] key to continue.\n')

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, load data from file into a list of product objects when script starts
list_of_product_objects = FileProcessor.read_data_from_file(strFileName)

# Step 2 - Display a menu of choices to the user

while(True):
    IO.print_menu_products()
    strChoice = IO.input_menu_choice()

    # Step 3 - Process user's menu choice
    if strChoice == '1':  # Add a new product
        product_1, strProduct, floatPrice = IO.input_new_product()
        lstOfProductObjects, status = FileProcessor.add_product_to_list(strProduct, floatPrice,list_of_product_objects)
        IO.input_press_to_continue(strStatus)  # display status
        continue  # to show the menu
    elif strChoice == '2':  # Show current data in the list of product rows
        IO.print_current_Products_in_list(list_of_product_objects)  # Show current data in the list of objects
        IO.input_press_to_continue(strStatus)  # display status
        continue  # to show the menu

    elif strChoice == '3':
        status = FileProcessor.write_data_to_file(strFileName, list_of_product_objects)
        print(status)
        IO.input_press_to_continue(strStatus)  # display status
        continue  # to show the menu

    elif strChoice == '4':  #  Exit Program
        print("Goodbye!")
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #