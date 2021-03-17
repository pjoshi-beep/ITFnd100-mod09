# ---------------------------------------------------------#
# Title: Assignment 09
# Description: working with modules in python
# Change log (who, when, what)
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# PJoshi, 3.16.21, modified code to complete assignment 9
# ---------------------------------------------------------#

# import modules
import DataClasses
import ProcessingClasses
import IOClasses

if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# main body of script
lstEmployeeTable = [] # A list/table of Employee objects
lstFileData = []

lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    lstEmployeeTable.append(Emp(row[0], row[1], row[2].strip()))

while True:
    Eio.print_menu_items()   #shows menu of options

    strOption = Eio.input_menu_options()
    if strOption == "1":
        Eio.print_current_list_items(lstEmployeeTable)
        continue

    elif strOption == "2":
        lstEmployeeTable.append(Eio.input_employee_data())
        continue

    elif strOption == "3":
        Fp.save_data_to_file("EmployeeData.txt", lstEmployeeTable)
        continue

    elif strOption == "4":
        break








