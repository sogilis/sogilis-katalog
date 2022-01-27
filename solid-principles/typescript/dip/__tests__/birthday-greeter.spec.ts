import MonthDay from '../src/month-day';
import EmployeeRepository from '../src/employee-repository';
import Clock from '../src/clock';
import BirthdayGreeter from '../src/birthday-greeter';
import Employee from '../src/employee';
import EmployeeBuilder from './employee-builder';

describe('birthday greeter', () => {
  const CURRENT_MONTH: number = 7;
  const CURRENT_DAY_OF_MONTH: number = 9;
  const TODAY: MonthDay = new MonthDay(CURRENT_MONTH, CURRENT_DAY_OF_MONTH);
  const employee: Employee = EmployeeBuilder.anEmployee().build();

  let employeeRepository: EmployeeRepository;
  let clock: Clock;
  let fakeConsoleLog: jest.SpyInstance;
  let birthdayGreeter: BirthdayGreeter;

  beforeEach(() => {
    employeeRepository = {
      findEmployeesBornOn: (monthDay: MonthDay): Employee[] => {
        const isToday =
          monthDay.getMonth() === CURRENT_MONTH &&
          monthDay.getDay() === CURRENT_DAY_OF_MONTH;
        return isToday ? [employee] : [];
      }
    };

    clock = { monthDay: (): MonthDay => TODAY };

    fakeConsoleLog = jest.spyOn(console, 'log').mockImplementation();

    birthdayGreeter = new BirthdayGreeter(employeeRepository, clock);
  });

  afterAll(() => {
    fakeConsoleLog.mockRestore();
  });

  it('should send greeting email to employee', () => {
    birthdayGreeter.sendGreetings();

    expect(console.log).toHaveBeenCalledWith(
      `To: ${employee.getEmail()}, Subject: Happy birthday!, Message: Happy birthday, dear ${employee.getFirstName()}!`
    );
  });
});
