class MonthDay {
  private month: number;
  private day: number;

  constructor(month: number, day: number) {
    this.month = month;
    this.day = day;
  }

  getMonth(): number {
    return this.month;
  }

  getDay(): number {
    return this.day;
  }
}

export default MonthDay;
