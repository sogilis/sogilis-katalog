import Employee from './employee';
import MonthDay from './month-day';

interface EmployeeRepository {
  findEmployeesBornOn(monthDay: MonthDay): Employee[];
}

export default EmployeeRepository;
