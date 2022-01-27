class Transaction {
  private date: Date;
  private amount: number;

  constructor(date: Date, amount: number) {
    this.date = date;
    this.amount = amount;
  }

  public getDate(): Date {
    return this.date;
  }

  public getAmount(): number {
    return this.amount;
  }
}

export default Transaction;
