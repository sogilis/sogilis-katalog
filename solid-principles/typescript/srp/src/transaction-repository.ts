import Transaction from './transaction';

interface TransactionRepository {
  add(transaction: Transaction): void;
  all(): Transaction[];
}

export class FormatTransactions {
  private STATEMENT_HEADER: string = 'DATE | AMOUNT | BALANCE';

  private transactions;
  private lines = [this.STATEMENT_HEADER];

  constructor(transactions) {
    this.transactions = transactions;
  }
  
  public print() {
    let balance = 0;

    this.transactions
        .map(transaction => {
          balance += transaction.getAmount();
          return this.statementLine(transaction, balance);
        })
        .forEach(statement => this.addLine(statement));

    return this.lines;
  }

  private statementLine(transaction: Transaction, balance: number) {
    const formattedDate = this.formatDate(transaction.getDate());
    const formattedAmmount = this.formatNumber(transaction.getAmount());
    const formattedBalance = this.formatNumber(balance);

    return `${formattedDate} | ${formattedAmmount} | ${formattedBalance}`;
  }

  private addLine(line: string) {
    this.lines.push(line);
  }

  private formatDate(date: Date): string {
    return `${date.getDate()}/${date.getMonth() + 1}/${date.getFullYear()}`;
  }

  private formatNumber(amount: number): string {
    return amount.toFixed(2);
  }
}

export default TransactionRepository;
