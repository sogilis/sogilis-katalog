import EmployeeRepository from './employee-repository';
import Clock from './clock';
import MonthDay from './month-day';
import Employee from './employee';
import Email from './email';
import EmailSender from './email-sender';

class BirthdayGreeter {
  private employeeRepository: EmployeeRepository;
  private clock: Clock;

  constructor(employeeRepository: EmployeeRepository, clock: Clock) {
    this.employeeRepository = employeeRepository;
    this.clock = clock;
  }

  public sendGreetings(): void {
    const today: MonthDay = this.clock.monthDay();
    this.employeeRepository
      .findEmployeesBornOn(today)
      .map(employee => this.emailFor(employee))
      .forEach(email => new EmailSender().send(email));
  }

  private emailFor(employee: Employee): Email {
    const message: string = `Happy birthday, dear ${employee.getFirstName()}!`;
    return new Email(employee.getEmail(), 'Happy birthday!', message);
  }
}

export default BirthdayGreeter;
