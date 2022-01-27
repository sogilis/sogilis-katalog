import TransactionRepository, {FormatTransactions} from './transaction-repository';
import Clock from './clock';
import Console from './console';
import Transaction from './transaction';

class AccountService {

  private transactionRepository: TransactionRepository;
  private clock: Clock;
  private console: Console;

  constructor(
    transactionRepository: TransactionRepository,
    clock: Clock,
    console: Console
  ) {
    this.transactionRepository = transactionRepository;
    this.clock = clock;
    this.console = console;
  }

  public deposit(amount: number): void {
    this.transactionRepository.add(this.transactionWith(amount));
  }

  public withdraw(amount: number): void {
    this.transactionRepository.add(this.transactionWith(-amount));
  }

  public printStatement(): void {
    const formatTransaction = new FormatTransactions(this.transactionRepository.all());
    const lines = formatTransaction.print();
    lines.forEach(line => this.console.printLine(line));
  }

  // ===== Private =====
  private transactionWith(amount: number): Transaction {
    return new Transaction(this.clock.today(), amount);
  }
}

export default AccountService;
