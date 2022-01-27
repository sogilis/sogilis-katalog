import Vehicle from './vehicle';

class PetrolCar extends Vehicle {
  private FUEL_TANK_FULL: number = 100;
  private fuelTankLevel: number = 0;

  public fillUpWithFuel(): void {
    this.fuelTankLevel = this.FUEL_TANK_FULL;
  }

  public chargeBattery(): void {
    throw new Error('A petrol car cannot be recharged');
  }

  public getFuelTankLevel(): number {
    return this.fuelTankLevel;
  }
}

export default PetrolCar;
