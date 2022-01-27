import EmployeeType from './employee-type';

class Employee {
  private salary: number;
  private bonus: number;
  private type: EmployeeType;

  constructor(salary: number, bonus: number, type: EmployeeType) {
    this.salary = salary;
    this.bonus = bonus;
    this.type = type;
  }

  public payAmount(): number {
    switch (this.type) {
      case EmployeeType.ENGINEER:
        return this.salary;
      case EmployeeType.MANAGER:
        return this.salary + this.bonus;
      default:
        return 0;
    }
  }
}

export default Employee;
