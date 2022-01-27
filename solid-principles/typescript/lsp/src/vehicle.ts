abstract class Vehicle {
  private engineStarted: boolean = false;

  public startEngine(): void {
    this.engineStarted = true;
  }

  public engineIsStarted(): boolean {
    return this.engineStarted;
  }

  public stopEngine(): void {
    this.engineStarted = false;
  }

  abstract fillUpWithFuel(): void;

  abstract chargeBattery(): void;
}

export default Vehicle;
