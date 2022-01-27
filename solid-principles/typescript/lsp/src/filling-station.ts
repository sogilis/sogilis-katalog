import Vehicle from './vehicle';
import PetrolCar from './petrol-car';
import ElectricCar from './electric-car';

class FillingStation {
  public refuel(vehicle: Vehicle): void {
    if (vehicle instanceof PetrolCar) {
      vehicle.fillUpWithFuel();
    }
  }

  public charge(vehicle: Vehicle): void {
    if (vehicle instanceof ElectricCar) {
      vehicle.chargeBattery();
    }
  }
}

export default FillingStation;
