import MonthDay from './month-day';

class Clock {
  public monthDay(): MonthDay {
    const today = new Date();
    return new MonthDay(today.getMonth() + 1, today.getDate());
  }
}

export default Clock;
