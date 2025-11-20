class Employee_Payroll:
    """
    Employee_Payroll handles payroll computations for each employee,
    including gross salary, provident fund (PF), and deductions.

    Attributes:
        name (str): Employee's name.
        base_salary (float): Base salary before any deductions.
        allowances (float): Total allowances added to base salary.
        deductions (float): Total deductions other than PF.
        pf_rate (float): Provident Fund percentage (default is 12% of base salary).
    """

    def __init__(self, name, base_salary, allowances=0.0, deductions=0.0, pf_rate=0.12):
        """
        Initializes the payroll record for an employee.

        Args:
            name (str): Name of the employee.
            base_salary (float): The basic salary amount.
            allowances (float): Additional allowances (default 0.0).
            deductions (float): Deductions besides PF (default 0.0).
            pf_rate (float): PF rate as a decimal (default 0.12, i.e., 12%).
        """
        self.name = name
        self.base_salary = base_salary
        self.allowances = allowances
        self.deductions = deductions
        self.pf_rate = pf_rate

    def compute_pf(self):
        """
        Compute the Provident Fund amount based on the base salary and PF rate.

        Returns:
            float: Computed PF amount.
        """
        pf_amount = self.base_salary * self.pf_rate
        # Provident fund is calculated only on base salary
        return pf_amount

    def compute_gross_salary(self):
        """
        Compute the gross salary before deductions.

        Returns:
            float: Gross salary.
        """
        gross_salary = self.base_salary + self.allowances
        return gross_salary

    def compute_total_deductions(self):
        """
        Compute total deductions including PF and any additional deductions.

        Returns:
            float: Total deductions.
        """
        total_ded = self.compute_pf() + self.deductions
        return total_ded

    def compute_net_salary(self):
        """
        Compute the net salary after all deductions.

        Returns:
            float: Net salary.
        """
        net_salary = self.compute_gross_salary() - self.compute_total_deductions()
        return net_salary

    def summary(self):
        """
        Generate a summary dict containing all payroll fields.

        Returns:
            dict: Payroll summary.
        """
        return {
            "name": self.name,
            "base_salary": self.base_salary,
            "allowances": self.allowances,
            "gross_salary": self.compute_gross_salary(),
            "pf": self.compute_pf(),
            "deductions": self.deductions,
            "total_deductions": self.compute_total_deductions(),
            "net_salary": self.compute_net_salary(),
        }

# ---------------- Test cases ----------------

def test_employee_payroll():
    print("=" * 60)
    print("EMPLOYEE PAYROLL TEST CASES")
    print("=" * 60)
    
    # Test 1: Basic salary with no allowances or extra deductions
    print("\nTest 1: Basic salary with no allowances or extra deductions")
    print("-" * 60)
    emp1 = Employee_Payroll("Alice", base_salary=50000)
    summary1 = emp1.summary()
    print(f"Employee: {summary1['name']}")
    print(f"Base Salary: {summary1['base_salary']}")
    print(f"Allowances: {summary1['allowances']}")
    print(f"Gross Salary: {summary1['gross_salary']}")
    print(f"PF (12%): {summary1['pf']:.2f}")
    print(f"Deductions: {summary1['deductions']}")
    print(f"Total Deductions: {summary1['total_deductions']:.2f}")
    print(f"Net Salary: {summary1['net_salary']:.2f}")
    assert round(emp1.compute_pf(), 2) == 6000.00  # 12% of 50000
    assert emp1.compute_gross_salary() == 50000
    assert emp1.compute_total_deductions() == 6000
    assert emp1.compute_net_salary() == 44000
    print("✓ Test 1 PASSED")

    # Test 2: With allowances and deductions
    print("\nTest 2: With allowances and deductions")
    print("-" * 60)
    emp2 = Employee_Payroll("Bob", base_salary=60000, allowances=10000, deductions=3000)
    summary2 = emp2.summary()
    print(f"Employee: {summary2['name']}")
    print(f"Base Salary: {summary2['base_salary']}")
    print(f"Allowances: {summary2['allowances']}")
    print(f"Gross Salary: {summary2['gross_salary']}")
    print(f"PF (12%): {summary2['pf']:.2f}")
    print(f"Deductions: {summary2['deductions']}")
    print(f"Total Deductions: {summary2['total_deductions']:.2f}")
    print(f"Net Salary: {summary2['net_salary']:.2f}")
    assert round(emp2.compute_pf(), 2) == 7200.00
    assert emp2.compute_gross_salary() == 70000
    assert emp2.compute_total_deductions() == 10200
    assert emp2.compute_net_salary() == 59800
    print("✓ Test 2 PASSED")

    # Test 3: With custom PF rate
    print("\nTest 3: With custom PF rate (10%)")
    print("-" * 60)
    emp3 = Employee_Payroll("Carol", base_salary=80000, pf_rate=0.10)
    summary3 = emp3.summary()
    print(f"Employee: {summary3['name']}")
    print(f"Base Salary: {summary3['base_salary']}")
    print(f"Allowances: {summary3['allowances']}")
    print(f"Gross Salary: {summary3['gross_salary']}")
    print(f"PF (10%): {summary3['pf']:.2f}")
    print(f"Deductions: {summary3['deductions']}")
    print(f"Total Deductions: {summary3['total_deductions']:.2f}")
    print(f"Net Salary: {summary3['net_salary']:.2f}")
    assert round(emp3.compute_pf(), 2) == 8000.00
    assert emp3.compute_gross_salary() == 80000
    assert emp3.compute_total_deductions() == 8000
    assert emp3.compute_net_salary() == 72000
    print("✓ Test 3 PASSED")

    # Test 4: Negative deductions should decrease total deductions
    print("\nTest 4: Negative deductions (decrease total deductions)")
    print("-" * 60)
    emp4 = Employee_Payroll("Dave", base_salary=50000, allowances=5000, deductions=-2000)
    summary4 = emp4.summary()
    print(f"Employee: {summary4['name']}")
    print(f"Base Salary: {summary4['base_salary']}")
    print(f"Allowances: {summary4['allowances']}")
    print(f"Gross Salary: {summary4['gross_salary']}")
    print(f"PF (12%): {summary4['pf']:.2f}")
    print(f"Deductions: {summary4['deductions']}")
    print(f"Total Deductions: {summary4['total_deductions']:.2f}")
    print(f"Net Salary: {summary4['net_salary']:.2f}")
    assert round(emp4.compute_pf(), 2) == 6000.00
    assert emp4.compute_gross_salary() == 55000
    assert emp4.compute_total_deductions() == 4000
    assert emp4.compute_net_salary() == 51000
    print("✓ Test 4 PASSED")

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED ✓")
    print("=" * 60)

if __name__ == '__main__':
    test_employee_payroll()
