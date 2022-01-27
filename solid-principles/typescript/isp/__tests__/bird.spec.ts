import Bird from '../src/bird';

describe('bird', () => {
  const bird: Bird = new Bird();
  let fakeConsoleLog: jest.SpyInstance;

  beforeEach(() => {
    fakeConsoleLog = jest.spyOn(console, 'log').mockImplementation();
  });

  afterAll(() => {
    fakeConsoleLog.mockRestore();
  });

  it('should run', () => {
    bird.run();

    expect(console.log).toBeCalledWith('Bird is running');
  });

  it('should fly', () => {
    bird.fly();

    expect(console.log).toBeCalledWith('Bird is running');
  });
});
