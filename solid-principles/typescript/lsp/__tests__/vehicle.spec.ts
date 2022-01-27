import Vehicle from '../src/vehicle';

describe('vehicle', () => {
  it('should start engine', () => {
    const vehicle: Vehicle = new TestableVehicle();

    vehicle.startEngine();

    expect(vehicle.engineIsStarted()).toBe(true);
  });

  it('should stop engine', () => {
    const vehicle: Vehicle = new TestableVehicle();

    vehicle.startEngine();
    vehicle.stopEngine();

    expect(vehicle.engineIsStarted()).toBe(false);
  });
});

class TestableVehicle extends Vehicle {
  fillUpWithFuel(): void {}
  chargeBattery(): void {}
}
