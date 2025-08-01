class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parkSpace = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parkSpace[carType - 1] > 0:
            self.parkSpace[carType - 1] -= 1
            return True
        return False
        
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)