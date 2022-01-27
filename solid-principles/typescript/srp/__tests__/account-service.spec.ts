import Transaction from '../src/transaction';
import AccountService from '../src/account-service';
import Clock from '../src/clock';
import Console from '../src/console';
import TransactionRepository from '../src/transaction-repository';

describe('account service', () => {
  const POSITIVE_AMOUNT: number = 100;
  const NEGATIVE_AMOUNT: number = -POSITIVE_AMOUNT;
  const TODAY = new Date(2017, 10, 6);
  const TRANSACTIONS: Transaction[] = [
    new Transaction(new Date(2014, 5, 1), 1000),
    new Transaction(new Date(2014, 5, 2), -100),
    new Transaction(new Date(2014, 5, 10), 500)
  ];

  let clock: Clock;
  let transactionRepository: TransactionRepository;
  let console: Console;
  let accountService: AccountService;

  beforeEach(() => {
    clock = { today: (): Date => TODAY };

    transactionRepository = {
      add: jest.fn(),
      all: (): Transaction[] => TRANSACTIONS
    };

    console = { printLine: jest.fn() };

    accountService = new AccountService(transactionRepository, clock, console);
  });

  it('should deposit ammount into the account', () => {
    accountService.deposit(POSITIVE_AMOUNT);

    expect(transactionRepository.add).toHaveBeenCalledWith(
      new Transaction(TODAY, POSITIVE_AMOUNT)
    );
  });

  it('should withdraw amount from the account', () => {
    accountService.withdraw(POSITIVE_AMOUNT);

    expect(transactionRepository.add).toHaveBeenCalledWith(
      new Transaction(TODAY, NEGATIVE_AMOUNT)
    );
  });

  it('should print statement', () => {
    accountService.printStatement();

    expect(console.printLine).toHaveBeenCalledWith('DATE | AMOUNT | BALANCE');
    expect(console.printLine).toHaveBeenCalledWith(
      '1/6/2014 | 1000.00 | 1000.00'
    );
    expect(console.printLine).toHaveBeenCalledWith(
      '2/6/2014 | -100.00 | 900.00'
    );
    expect(console.printLine).toHaveBeenCalledWith(
      '10/6/2014 | 500.00 | 1400.00'
    );
  });
});
