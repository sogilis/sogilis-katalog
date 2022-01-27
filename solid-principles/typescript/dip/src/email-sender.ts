import Email from './email';

class EmailSender {
  public send(email: Email) {
    console.log(
      `To: ${email.getTo()}, Subject: ${email.getSubject()}, Message: ${email.getMessage()}`
    );
  }
}

export default EmailSender;
