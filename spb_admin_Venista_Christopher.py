# ============== Selwyn Panel Beaters MAIN PROGRAM ==============
# Student Name: Nadar Venista Christopher
# Student ID : 1159129
# NOTE: Make sure your two files are in the same folder
# =================================================================================

import spb_data    # spb_data.py MUST be in the SAME FOLDER as this file!
                    # spb_data.py contains the data
import datetime     # We areusing date times for this assessment, and it is
                    # available in the column_output() fn, so do not delete this line

import re         #regex

# Data variables
#col variables contain the format of each data column and help display headings
#db variables contain the actual data
col_customers = spb_data.col_customers
db_customers = spb_data.db_customers
col_services = spb_data.col_services
db_services = spb_data.db_services
col_parts = spb_data.col_parts
db_parts = spb_data.db_parts
#col_bills is useful for displaying the headings when listing bills
col_bills = spb_data.col_bills


def next_id(db_data):
    #Pass in the dictionary that you want to return a new ID number for, this will return a new integer value
    # that is one higher than the current maximum in the list.
    return max(db_data.keys())+1

def column_output(db_data, cols, format_str):
    # db_data is a list of tuples.
    # cols is a dictionary with column name as the key and data type as the item.
    # format_str uses the following format, with one set of curly braces {} for each column:
    #   eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
    #   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    #   The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
    #       format_str = "{: <5}  {: ^10}  {: >15}"
    #   Make sure the column is wider than the heading text and the widest entry in that column,
    #       otherwise the columns won't align correctly.
    # You can also pad with something other than a space and put characters between the columns, 
    # eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
    #       format_str = "{:.<5} | {:.^10} | {:.>15}"
    print(format_str.format(*cols))
    for row in db_data:
        row_list = list(row)
        for index, item in enumerate(row_list):
            if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
                row_list[index] = ""       # Replaces them with an empty string
            elif isinstance(item, datetime.date):    # If item is a date, convert to a string to avoid formatting issues
                row_list[index] = str(item)
        print(format_str.format(*row_list))


def list_customers():
    # List the ID, name, telephone number, and email of all customers

    # Use col_Customers for display
   
    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    #Iterate over all the customers in the dictionary
    for customer in db_customers.keys():
        #append to the display list the ID, Name, Telephone and Email
        display_list.append((customer,
                             db_customers[customer]['details'][0],
                             db_customers[customer]['details'][1],
                             db_customers[customer]['details'][2]))
    format_columns = "{: >4} | {: <15} | {: <12} | {: ^12}"
    print("\nCustomer LIST\n")    # display a heading for the output
    column_output(display_list, col_customers, format_columns)   # An example of how to call column_output function

    input("\nPress Enter to continue.")     # Pauses the code to allow the user to see the output



def list_parts():
    # List the ID, name, cost of all parts
    # use col_parts for display

    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    for part_id, part_info in db_parts.items():
        display_list.append((part_id, part_info[0], part_info[1]))
        display_list = sorted(display_list, key=lambda x:x[1]) # Sort in alphabetical order
    format_columns = "{: >4} | {: <15} | {: ^5}"
    print("\nParts LIST\n") # display a heading for the output
    column_output(display_list, col_parts, format_columns) #calling column_output function
    input("\nPress Enter to continue.") # Pauses the code to allow the user to see the output

def list_services():
    # List the ID, name, cost of all services
    #use col_services for display

    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    for service_id, service_info in db_services.items():
        display_list.append((service_id, service_info[0], service_info[1]))
        display_list = sorted(display_list, key=lambda x:x[1]) #sort in alphabetical order
    format_columns = "{: >4} | {: <20} | {: ^5}"
    print("\nServices LIST\n") # display a heading for the output
    column_output(display_list, col_services, format_columns) # calling column_output functon
    input("\nPress Enter to continue.") #Pause the code to allow the user to see the output

def add_customer():
    # Add a customer to the db_customers database, use the next_id to get an id for the customer.
    # Remember to add all required dictionaries.
    new_customer_id = next_id(db_customers)
    # Get input for name, validate, and repeat until valid
    while True:
        name = input("Enter customer name: ") #Enter name field
        if validate_name(name):
            break

    # Get input for telephone, validate, and repeat until valid
    while True:
        telephone = input("Enter customer telephone: ") #Enter telephone number field
        if validate_telephone(telephone):
            break

    # Get input for email, validate, and repeat until valid
    while True:
        email = input("Enter customer email: ") #Enter email field
        if validate_email(email):
            break
    db_customers[new_customer_id] = {'details': [name, telephone, email], 'jobs': {}}
    print(f"\nCustomer {new_customer_id} added successfully.")
    input("\nPress Enter to continue.")

def add_job():
    # Add a Job to a customer
    # Remember to validate part and service ids
    customer_id = input("Enter customer ID: ")  #check whether customer ID is valid or not
    if not validate_number_input(customer_id, "customer ID"):
        print("Invalid customer ID. Please try again.")
        return
    customer_id = int(customer_id)
    if customer_id not in db_customers:
        print("Invalid customer ID. Please try again.")
        return

    job_date = input("Enter job date (YYYY-MM-DD): ")
    try:
        job_date = datetime.datetime.strptime(job_date, "%Y-%m-%d").date() #strptime returns string representation of date and time
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return
            
    service_id = input("Enter service ID: ") # check whether service ID is valid or not
    if not validate_number_input(service_id, "service ID"):
        print("Invalid service ID. Please try again.")
        return
    service_id = int(service_id)
    if service_id not in db_services:
        print("Invalid service ID. Please try again.")
        return

    part_id = input("Enter part ID (or press Enter to skip): ") # check whether part id is valid or not
    if not validate_partid_number_input(part_id, "part ID"):
        print("Invalid part ID. Please try again.")
        return
    part_id = int(part_id) if part_id else None  # Convert to int only if not empty
    if part_id and part_id not in db_parts:
        print("Invalid part ID. Please try again.")
        return

    amount = db_services[service_id][1] #Calculate amount of part and services using ID numbers 
    if part_id:
        amount += db_parts[part_id][1]

    db_customers[customer_id]['jobs'][job_date] = [(service_id, part_id), (), amount,False]
    print("\nJob added successfully.")
    input("\nPress Enter to continue.")

def bills_to_pay():
    # List the ID, name, cost of all services
    #use col_bills for display

    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    for customer_id, customer_info in db_customers.items():
        for job_date, job_info in customer_info['jobs'].items():
            if not job_info[3]:  # Check if the bill is unpaid
                display_list.append((db_customers[customer_id]['details'][0],
                                     db_customers[customer_id]['details'][1],
                                     job_date,
                                     job_info[2]))

    format_columns = "{: <15} | {: <12} | {: ^19} | {: >10}"
    print("\nUnpaid Bills\n") # Display heading for the table
    column_output(display_list, col_bills, format_columns) # calling column_output functon
    input("\nPress Enter to continue.") #Pause the code to allow the user to see the output

def pay_bill():
    # Mark a bill as paid
    # list all customers
    list_customers()
    display_list = []

    customer_id = input("Enter customer ID: ") # Enter customer name and validate
    if not validate_number_input(customer_id, "customer ID"):
        print("Invalid customer ID. Please try again.")
        return

    customer_id = int(customer_id)
    if customer_id not in db_customers:
        print("Invalid customer ID. Please try again.")
        return

    customer_info = db_customers[customer_id]

    for job_date, job_info in customer_info['jobs'].items():
            if not job_info[3]:  # Check if the bill is unpaid
                display_list.append((db_customers[customer_id]['details'][0],
                                     db_customers[customer_id]['details'][1],
                                     job_date,
                                     job_info[2]))

    if not display_list:
        print(f"No unpaid bills for Customer {customer_id}.")
        input("\nPress Enter to continue.") #Pause the code to allow the user to see the output
        return

    format_columns = "{: <15} | {: <12} | {: ^12} | {: >10}"
    print("\nUnpaid Bills\n") #display the heading of the table
    column_output(display_list, col_bills, format_columns) #calling col_bills function

    confirm = input(f"\nAre you sure you want to mark the bill for customer {customer_id} as paid? (Y/N): ").lower() #comment to mark the customer has paid the bill or not
    if confirm != 'y':
        print("Bill payment canceled.")
        input("\nPress Enter to continue.")
        return

    for job_date, job_info in customer_info['jobs'].items():
        if not job_info[3]:  
            db_customers[customer_id]['jobs'][job_date][3] = 'true'

    # print(db_customers[customer_id]['jobs'].items())
    # display_list = []
    # all_jobs = db_customers[customer_id]['jobs'].items()
    # for cust_info, job_info  in db_customers[customer_id].items():
    #     print(cust_info)
    #     print(job_info)
        # for job_date, job_info in job_info.items():
        #      print(job_info)


        # for job_date, job_info in job_info['jobs'].items():
        #     print(job_date)
        #     print(job_info)

        # if not job_info[1][3]:
        #     print(job_info[1][3])
        #     display_list.append((db_customers[customer_id]['details'][0],
        #                              db_customers[customer_id]['details'][1],
        #                              job_date,
        #                              job_info[2]))



    # db_customers[customer_id]['jobs'][job_date][3] = True

    print("\nBill marked as paid.") # display the message if the bill is marked Y
    input("\nPress Enter to continue.") #Pause the code to allow the user to see the output


#util functions
def validate_name(name):
    # Validate that the name contains only letters and may include a period (.)
    if len(name) < 3 or not re.match("^[a-zA-Z. ]+$", name) or '..' in name:
        print("Invalid name. Please enter a valid name (at least 3 characters), "
              "containing only letters and optional period, and no two consecutive dots. ")
        return False
    return True

def validate_email(email):
    # Validate email using a simple pattern
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email. Please enter a valid email address or press 'Ctrl + X' to exit.")
        return False
    return True

def validate_telephone(telephone):
    # Validate telephone number using a simple pattern
    if not re.match("^[0-9]+$", telephone):
        print("Invalid telephone number")
        return False
    return True

def validate_number_input(input_value, input_name):
    # Validate that the input is a valid number
    if not re.match("^[0-9]+$", input_value):
        print(f"Invalid {input_name}. Please enter a valid number.")
        return False
    return True

def validate_partid_number_input(input_value, input_name):
    # Validate that the input is a valid number or an empty string (skipping)
    if input_value and not re.match("^[0-9]+$", input_value):
        print(f"Invalid {input_name}. Please enter a valid number or press Enter to skip.")
        return False
    return True

# function to display the menu
def disp_menu():
    print("==== WELCOME TO SELWYN PANEL BEATERS ===")
    print(" 1 - List Customers")
    print(" 2 - List Services")
    print(" 3 - List Parts")
    print(" 4 - Add Customer")
    print(" 5 - Add Job")
    print(" 6 - Display Unpaid Bills")
    print(" 7 - Pay Bill")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ")

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X" and "x"
while response.upper() != "X":
    if response == "1":
        list_customers()
    elif response == "2":
        list_services()
    elif response == "3":
        list_parts()
    elif response == "4":
        add_customer()
    elif response == "5":
        add_job()
    elif response == "6":
        bills_to_pay()
    elif response == "7":
        pay_bill()
    else:
        print("\n***Invalid response, please try again (enter 1-6 or X)")

    print("")
    disp_menu()
    response = input("Please select menu choice: ")

print("\n=== Thank you for using Selywn Panel Beaters! ===\n")

