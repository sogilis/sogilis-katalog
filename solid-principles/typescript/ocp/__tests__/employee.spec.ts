import Employee from '../src/employee';
import EmployeeType from '../src/employee-type';

describe('employee', () => {
  const BONUS: number = 100;
  const SALARY: number = 1000;

  it('should not add bonus to the engineer pay amount', () => {
    const employee = new Employee(SALARY, BONUS, EmployeeType.ENGINEER);
    expect(employee.payAmount()).toEqual(SALARY);
  });

  it('should add bonus to the manager pay amount', () => {
    const employee = new Employee(SALARY, BONUS, EmployeeType.MANAGER);
    expect(employee.payAmount()).toEqual(SALARY + BONUS);
  });
});
