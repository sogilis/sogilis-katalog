class Email {
  private to: string;
  private subject: string;
  private message: string;

  constructor(to: string, subject: string, message: string) {
    this.to = to;
    this.subject = subject;
    this.message = message;
  }

  public getTo(): string {
    return this.to;
  }

  public getSubject(): string {
    return this.subject;
  }

  public getMessage(): string {
    return this.message;
  }
}

export default Email;
