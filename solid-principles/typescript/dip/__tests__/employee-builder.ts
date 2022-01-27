import Employee from '../src/employee';

class EmployeeBuilder {
  private firstName: string = 'John';
  private lastName: string = 'Doe';
  private dateOfBirth: Date = new Date(1980, 8, 10);
  private email: string = 'john.doe@foobar.com';

  public static anEmployee(): EmployeeBuilder {
    return new EmployeeBuilder();
  }

  public withEmail(email: string): EmployeeBuilder {
    this.email = email;
    return this;
  }

  public withFirstName(firstName: string): EmployeeBuilder {
    this.firstName = firstName;
    return this;
  }

  public withLastName(lastName: string): EmployeeBuilder {
    this.lastName = lastName;
    return this;
  }

  public withDateOfBirth(dateOfBirth: Date): EmployeeBuilder {
    this.dateOfBirth = dateOfBirth;
    return this;
  }

  public build(): Employee {
    return new Employee(
      this.firstName,
      this.lastName,
      this.dateOfBirth,
      this.email
    );
  }
}

export default EmployeeBuilder;
