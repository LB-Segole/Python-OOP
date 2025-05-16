class Employee:
    """
    Base class for all employees.
    """
    def __init__(self, employee_id, name, salary):
        """
        Constructor to initialize the employee object.

        Args:
            employee_id (int): The unique ID of the employee.
            name (str): The name of the employee.
            salary (float): The salary of the employee.
        """
        self.__employee_id = employee_id  # Private attribute
        self.name = name
        self.salary = salary

    def get_employee_id(self):
        """
        Public method to access the private employee_id.

        Returns:
            int: The employee's ID.
        """
        return self.__employee_id

    def display_details(self):
        """
        Method to display employee details.
        """
        print(f"ID: {self.__employee_id}, Name: {self.name}, Salary: ${self.salary:.2f}")

    def give_raise(self, amount):
        """
        Method to increase the employee's salary.

        Args:
            amount (float): The amount by which to increase the salary.
        """
        if amount > 0:
            self.salary += amount
            print(f"Raise of ${amount:.2f} given to {self.name}. New salary: ${self.salary:.2f}")
        else:
            print(f"Invalid raise amount for {self.name}.")



class Manager(Employee):
    """
    Class for managers, inheriting from Employee.
    """
    def __init__(self, employee_id, name, salary, department):
        """
        Constructor to initialize the manager object.

        Args:
            employee_id (int): The unique ID of the manager.
            name (str): The name of the manager.
            salary (float): The salary of the manager.
            department (str): The department the manager belongs to.
        """
        super().__init__(employee_id, name, salary)
        self.department = department
        self.employees = []  # List of direct reports

    def add_employee(self, employee):
        """
        Method to add an employee to the manager's list of direct reports.

        Args:
            employee (Employee): The employee object to add.
        """
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"{employee.name} added to {self.name}'s direct reports.")
        else:
            print(f"Invalid employee object. Cannot add to {self.name}'s reports.")

    def remove_employee(self, employee):
        """
        Method to remove an employee from the manager's list of direct reports.

        Args:
            employee (Employee): The employee object to remove.
        """
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee.name} removed from {self.name}'s direct reports.")
        else:
            print(f"{employee.name} is not a direct report of {self.name}.")

    def display_details(self):
        """
        Overrides the display_details method to also display the manager's
        department and direct reports.
        """
        super().display_details()
        print(f"Department: {self.department}")
        if self.employees:
            print("Direct Reports:")
            for employee in self.employees:
                print(f"- {employee.name}")
        else:
            print("No direct reports.")

    def give_raise(self, amount, include_reports=False):
        """
        Overrides the give_raise method to optionally give a raise to direct reports.

        Args:
            amount (float): The amount by which to increase the salary.
            include_reports (bool, optional): Whether to include direct reports in the raise.
                Defaults to False.
        """
        super().give_raise(amount)  # Give raise to the manager
        if include_reports:
            for employee in self.employees:
                employee.give_raise(amount)  # Give raise to direct reports


class SalesPerson(Employee):
    """
    Class for salespeople, inheriting from Employee
    """
    def __init__(self, employee_id, name, salary, commission_rate):
        """
        Constructor to initialize the salesperson object.

        Args:
            employee_id (int): The ID of the salesperson
            name (str): The name of the salesperson
            salary (float): the salary of the salesperson
            commission_rate (float): the commission rate of the salesperson
        """
        super().__init__(employee_id, name, salary)
        self.commission_rate = commission_rate
        self.sales_achieved = 0

    def calculate_commission(self):
        """
        Calculates the commission earned

        Returns:
           float: commission earned
        """
        return self.commission_rate * self.sales_achieved

    def display_details(self):
        """
        Overrides base class to display commission rate and sales achieved
        """
        super().display_details()
        print(f"Commission Rate: {self.commission_rate:.2f}, Sales Achieved: ${self.sales_achieved:.2f}")

    def give_raise(self, amount):
        """
        override the give_raise method to increase salary and commission rate
        """
        super().give_raise(amount)
        self.commission_rate += 0.01 # increase commission rate by 1%
        print(f"Commission rate increased to: {self.commission_rate:.2f}")

class Company:
    """
    Class to represent a company.
    """
    def __init__(self, name):
        """
        Constructor to initialize the company object.

        Args:
            name (str): The name of the company.
        """
        self.name = name
        self.employees = []  # List of all employees in the company

    def add_employee(self, employee):
        """
        Method to add an employee to the company's list.

        Args:
            employee (Employee): The employee object to add.
        """
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"{employee.name} added to {self.name}.")
        else:
            print(f"Invalid employee object. Cannot add to {self.name}'s employees.")

    def remove_employee(self, employee):
        """
        Method to remove an employee from the company's list.

        Args:
            employee (Employee): The employee object to remove.
        """
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee.name} removed from {self.name}.")
        else:
            print(f"{employee.name} is not an employee of {self.name}.")

    def display_all_employees(self):
        """
        Method to display the details of all employees in the company.
        """
        print(f"--- All Employees of {self.name} ---")
        for employee in self.employees:
            employee.display_details()
        print("------------------------")

    def get_employee_by_id(self, employee_id):
        """
        Method to retrieve an employee object by their ID.

        Args:
            employee_id (int): The ID of the employee to retrieve.

        Returns:
            Employee or None: The employee object if found, None otherwise.
        """
        for employee in self.employees:
            if employee.get_employee_id() == employee_id:
                return employee
        return None

    def calculate_total_salary(self):
        """
        Method to calculate the total salary of all employees in the company.

        Returns:
            float: The total salary.
        """
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary

# Example Usage
if __name__ == "__main__":
    # Create some employees
    employee1 = Employee(101, "Alice Smith", 50000)
    employee2 = Employee(102, "Bob Johnson", 60000)
    manager1 = Manager(201, "Charlie Brown", 80000, "Sales")
    salesperson1 = SalesPerson(301, "David Miller", 40000, 0.10)

    # Add employees to the company
    my_company = Company("Acme Corp")
    my_company.add_employee(employee1)
    my_company.add_employee(employee2)
    my_company.add_employee(manager1)
    my_company.add_employee(salesperson1)

    # Add employees to the manager's direct reports
    manager1.add_employee(employee1)
    manager1.add_employee(salesperson1)

    # Display all employees
    my_company.display_all_employees()

    # Get an employee by ID
    employee_bob = my_company.get_employee_by_id(102)
    if employee_bob:
        print("\nFound employee by ID:")
        employee_bob.display_details()

    # Calculate total salary
    total_salary = my_company.calculate_total_salary()
    print(f"\nTotal salary of all employees: ${total_salary:.2f}")

    # Give raises
    employee1.give_raise(5000)
    manager1.give_raise(10000, include_reports=True)
    salesperson1.give_raise(2000)

    # Display all employees after raises
    my_company.display_all_employees()
