class Car:
      def __init__(self, model, currentSpeed, maxSpeed, fuelLevel ):
            self.model = model
            self.currentSpeed = currentSpeed
            self.maxSpeed = maxSpeed
            self.fuelLevel = fuelLevel
      
      def accelerate(self, value):
            if self.fuelLevel > 0:
                  self.currentSpeed += value
                  self.fuelLevel -= value
                  if self.currentSpeed > self.maxSpeed:
                        self.currentSpeed = self.maxSpeed
            else:
                  print("No Fuel!")
      
      def brake(self, value):
            self.currentSpeed -= value
            if self.currentSpeed < 0:
                  self.currentSpeed = 0
      
      def refuel(self, value):
            self.fuelLevel += value
            if self.fuelLevel > 100:
                  self.fuelLevel = 100

      def race(self):
            self.accelerate(10)
            self.brake(20)
            self.refuel(100)

      def stringify(self):
            return str(self.model), str(self.currentSpeed) ,str(self.maxSpeed), str(self.fuelLevel)