import Dog from '../src/dog';

describe('dog', () => {
  const dog: Dog = new Dog();
  let fakeConsoleLog: jest.SpyInstance;

  beforeEach(() => {
    fakeConsoleLog = jest.spyOn(console, 'log').mockImplementation();
  });

  afterAll(() => {
    fakeConsoleLog.mockRestore();
  });

  it('should run', () => {
    dog.run();

    expect(console.log).toBeCalledWith('Dog is running');
  });

  it('should bark', () => {
    dog.bark();

    expect(console.log).toBeCalledWith('Dog is barking');
  });
});
