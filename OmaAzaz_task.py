
class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = 'happy'
        elif hours < 7:
            self.mood = 'tired'
        else:
            self.mood = 'lazy'

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        self.money -= items * 10


class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self._fuelRate = min(max(fuelRate, 0), 100)
        self._velocity = min(max(velocity, 0), 200)

    @property
    def fuelRate(self):
        return self._fuelRate

    @fuelRate.setter
    def fuelRate(self, value):
        self._fuelRate = min(max(value, 0), 100)

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = min(max(value, 0), 200)

    def run(self, velocity, distance):
        self.velocity = velocity
        distance_possible = self.fuelRate
        if distance_possible >= distance:
            self.fuelRate -= distance
            self.stop(0)
        else:
            distance_traveled = self.fuelRate
            self.fuelRate = 0
            self.stop(distance - distance_traveled)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Stopped with {remaining_distance} km remaining.")
        else:
            print("Arrived at the destination.")


class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = 'happy'
        elif hours < 8:
            self.mood = 'lazy'
        else:
            self.mood = 'tired'

    def drive(self):
        self.car.run(60, self.distanceToWork)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    def send_mail(self, to, subject, body):
        print(f"Sending email to {to}\nSubject: {subject}\nBody: {body}")


class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)

    def fire(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.id != emp_id]

    def calculate_lateness(self, emp_id, expected_hour, actual_hour):
        emp = self.get_employee(emp_id)
        if not emp:
            print("Employee not found.")
            return

        lateness = actual_hour - expected_hour
        if lateness > 0:
            deduction = lateness * 10  
            self.deduct(emp_id, deduction)
            print(f"{emp.name} was {lateness} hour(s) late. Deducted {deduction}.")
        else:
            print(f"{emp.name} was on time or early.")

    def deduct(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary -= amount

    def reward(self, emp_id, amount):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += amount
