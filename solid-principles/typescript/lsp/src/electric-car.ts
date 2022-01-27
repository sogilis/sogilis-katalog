import Vehicle from './vehicle';

class ElectricCar extends Vehicle {
  private BATTERY_FULL: number = 100;
  private batteryLevel: number;

  public fillUpWithFuel(): void {
    throw new Error("It's an electric car");
  }

  public chargeBattery(): void {
    this.batteryLevel = this.BATTERY_FULL;
  }

  public getBatteryLevel(): number {
    return this.batteryLevel;
  }
}

export default ElectricCar;
