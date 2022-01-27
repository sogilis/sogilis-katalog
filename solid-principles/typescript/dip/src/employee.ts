class Employee {
  private firstName: string;
  private lastName: string;
  private dateOfBirth: Date;
  private email: string;

  constructor(
    firstName: string,
    lastName: string,
    dateOfBirth: Date,
    email: string
  ) {
    this.firstName = firstName;
    this.lastName = lastName;
    this.dateOfBirth = dateOfBirth;
    this.email = email;
  }

  public getFirstName(): string {
    return this.firstName;
  }

  public getLastName(): string {
    return this.lastName;
  }

  public getDateOfBirth(): Date {
    return this.dateOfBirth;
  }

  public getEmail(): string {
    return this.email;
  }
}

export default Employee;
