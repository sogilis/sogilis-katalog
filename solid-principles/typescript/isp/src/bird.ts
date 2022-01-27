import Animal from './animal';

class Bird implements Animal {
  public bark(): void {}

  public run(): void {
    console.log('Bird is running');
  }

  public fly(): void {
    console.log('Bird is flying');
  }
}

export default Bird;
