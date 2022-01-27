import Animal from './animal';

class Dog implements Animal {
  public fly(): void {}

  public run(): void {
    console.log('Dog is running');
  }

  public bark(): void {
    console.log('Dog is barking');
  }
}

export default Dog;
