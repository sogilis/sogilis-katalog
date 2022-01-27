import FillingStation from '../src/filling-station';
import PetrolCar from '../src/petrol-car';
import ElectricCar from '../src/electric-car';

describe('filling station', () => {
  const FULL: number = 100;
  const fillingStation: FillingStation = new FillingStation();

  it('should refuel a petrol car', () => {
    const car: PetrolCar = new PetrolCar();

    fillingStation.refuel(car);

    expect(car.getFuelTankLevel()).toEqual(FULL);
  });

  it('should not fail refueling an electric car', () => {
    const car: ElectricCar = new ElectricCar();

    expect(() => fillingStation.refuel(car)).not.toThrow();
  });

  it('should recharge an electric car', () => {
    const car: ElectricCar = new ElectricCar();

    fillingStation.charge(car);

    expect(car.getBatteryLevel()).toEqual(FULL);
  });

  it('should not fail recharging a petrol car', () => {
    const car: PetrolCar = new PetrolCar();
    expect(() => fillingStation.charge(car)).not.toThrow();
  });
});
