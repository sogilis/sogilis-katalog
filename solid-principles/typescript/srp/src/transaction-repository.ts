import Transaction from './transaction';

interface TransactionRepository {
  add(transaction: Transaction): void;
  all(): Transaction[];
}

export default TransactionRepository;
