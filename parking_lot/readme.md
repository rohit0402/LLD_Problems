# 🅿️ Parking Lot — Low-Level Design

A production-oriented Low-Level Design implementation of a Parking Lot system using Python, focusing on Object-Oriented Design, SOLID principles, Strategy Pattern, Factory Pattern, composition, inheritance, polymorphism, dependency injection, and clean modular architecture.

---

# 1. Problem

Design a Parking Lot system that can:

* Park vehicles
* Remove vehicles
* Generate parking tickets
* Assign appropriate parking spots
* Free parking spots when vehicles exit
* Calculate parking charges
* Display available parking spots

---

# 2. Clarifying Questions

Before designing the system, clarify the requirements with the interviewer.

Important questions:

* How many parking lots should the system support?
* Can a parking lot have multiple floors?
* What types of vehicles are supported?
* What types of parking spots are available?
* Can one spot hold multiple vehicles?
* When is the ticket generated?
* When is payment made?
* Are reservations supported?
* Is online booking required?
* Is concurrency required?
* Is an admin dashboard required?

---

# 3. Functional Requirements

The system should support:

* Park a vehicle
* Remove a vehicle
* Generate parking ticket
* Assign proper parking spot
* Free parking spot when vehicle exits
* Calculate parking charges
* Display available parking spots

---

# 4. Non-Functional Requirements

The design should be:

* Extensible — easy to add new vehicle types
* Maintainable
* Modular
* Low coupling
* High cohesion
* SOLID-compliant
* Easy to test

---

# 5. Assumptions

For this implementation:

* One parking lot
* Multiple floors
* One vehicle per parking spot
* Three vehicle types:

  * Bike
  * Car
  * Truck
* Three spot types:

  * Bike
  * Car
  * Truck
* Ticket generated at entry
* Payment at exit
* No reservations
* No online booking
* No concurrency
* No admin dashboard

---

# 6. Actors

### Driver

The driver interacts with the parking lot to:

* Enter the parking lot
* Park a vehicle
* Receive a ticket
* Exit the parking lot
* Pay the parking fee
* View available parking spots

---

# 7. Use Cases

## Entry

```text
Driver
   ↓
Enter Parking Lot
   ↓
Find/Get Parking Spot
   ↓
Generate Parking Ticket
   ↓
Park Vehicle
```

## Exit

```text
Driver
   ↓
Present Ticket
   ↓
Calculate Fee
   ↓
Pay
   ↓
Free Parking Spot
```

## Display Availability

```text
Driver
   ↓
View Available Parking Spots
```

---

# 8. Entities

## ParkingLot

Responsibilities:

* Manage floors
* Maintain overall parking status
* Park/unpark vehicles

Important data:

* Lot ID
* Floors
* Parked vehicles

---

## ParkingFloor

Responsibilities:

* Manage parking spots
* Search for available spots
* Track floor-level parking availability

Important data:

* Floor ID
* Parking spots

---

## ParkingSpot

Responsibilities:

* Maintain spot state
* Determine whether a spot is available
* Check vehicle/spot compatibility
* Park a vehicle
* Remove a vehicle

Important data:

* Spot ID
* Spot type
* Occupied/free state
* Current vehicle

---

## Vehicle

Common vehicle abstraction.

Vehicle types:

* Bike
* Car
* Truck

Vehicle follows inheritance because:

```text
Car IS-A Vehicle
Bike IS-A Vehicle
Truck IS-A Vehicle
```

All vehicles share common properties such as:

* License number
* Color
* Vehicle type

---

## Ticket

Represents a parking session.

Important data:

* Ticket ID
* Vehicle
* Parking spot
* Entry time
* Exit time

---

## Payment

Represents a payment record.

Important data:

* Payment ID
* Amount
* Payment method

  * Cash
  * Card
* Payment status
* Timestamp

---

## Driver

Represents the person using the parking lot.

Important data:

* Name
* License

---

# 9. Services

The system contains the following services.

### ParkingService

Coordinates the overall parking and exit workflow.

### FeeCalculator

Coordinates fee calculation using the selected fee strategy.

### PaymentService

Coordinates payment using the selected payment strategy.

---

# 10. Abstractions

The system uses the following abstractions:

* Vehicle Factory
* Fee Strategy
* Payment Strategy

---

# 11. Relationships

The main object relationships are:

```text
ParkingLot
   │
   └── HAS-A → ParkingFloor
                  │
                  └── HAS-A → ParkingSpot
                                 │
                                 └── HAS-A → Vehicle
```

Inheritance:

```text
             Vehicle
            /   |   \
           /    |    \
        Bike   Car   Truck
```

Fee strategy:

```text
          FeeStrategy
          /    |    \
         /     |     \
      Bike    Car    Truck
      Fee     Fee     Fee
```

Payment strategy:

```text
       PaymentStrategy
          /       \
         /         \
      Cash         Card
```

---

# 12. Design Patterns

## Factory Pattern

Factory is responsible for creating/selecting appropriate objects.

### VehicleFactory

```text
VehicleFactory
      │
      ├── BIKE  → Bike()
      ├── CAR   → Car()
      └── TRUCK → Truck()
```

### FeeStrategyFactory

```text
FeeStrategyFactory
      │
      ├── BIKE  → BikeFeeStrategy
      ├── CAR   → CarFeeStrategy
      └── TRUCK → TruckFeeStrategy
```

---

## Strategy Pattern

Strategy is used when behavior varies.

### Fee Strategy

```text
FeeStrategy
    ↑
    ├── BikeFeeStrategy
    ├── CarFeeStrategy
    └── TruckFeeStrategy
```

Each strategy implements:

```text
calculate_fee()
```

Instead of:

```python
if bike:
    ...
elif car:
    ...
elif truck:
    ...
```

we use polymorphism.

### Payment Strategy

```text
PaymentStrategy
    ↑
    ├── CashPaymentStrategy
    └── CardPaymentStrategy
```

Each strategy implements:

```text
pay()
```

---

# 13. Why Strategy?

Fee calculation changes depending on vehicle type.

For example:

```text
Bike  → ₹20/hour
Car   → ₹40/hour
Truck → ₹60/hour
```

Instead of putting all pricing logic into one large conditional block, each pricing rule is encapsulated inside its own strategy.

This makes the system easier to extend.

---

# 14. Why Factory + Strategy?

These patterns solve different problems.

### Strategy

Defines interchangeable behavior.

```text
"What algorithm/behavior should be used?"
```

### Factory

Creates/selects the appropriate object.

```text
"Which implementation should I create/use?"
```

For example:

```text
VehicleType.CAR
      ↓
FeeStrategyFactory
      ↓
CarFeeStrategy
      ↓
calculate_fee()
```

---

# 15. UML — Class Diagram

The main class relationships are:

```text
                         Vehicle
                        /   |   \
                       /    |    \
                    Bike   Car   Truck


ParkingLot
     │
     │ contains
     ▼
ParkingFloor
     │
     │ contains
     ▼
ParkingSpot
     │
     │ contains
     ▼
Vehicle


FeeStrategy
     ▲
     │
 ┌───┼──────────────┐
 │   │              │
Bike Car           Truck
Fee  Fee             Fee


PaymentStrategy
      ▲
      │
 ┌────┴─────┐
 │          │
Cash       Card
```

---

# 16. Runtime Architecture

The following shows how the main components interact during program execution.

```text
                         main.py
                            │
                ┌───────────┴───────────┐
                │                       │
          CREATE OBJECTS              PARK
                │                       │
                ▼                       ▼
          ParkingLot             ParkingService
                │                       │
                ▼                       ▼
          ParkingFloor         is_vehicle_parked()
                │                       │
                ▼                       ▼
          ParkingSpot               ParkingLot
                                        │
                                        ▼
                              find_available_spot()
                                        │
                                        ▼
                                      Floor
                                        │
                                        ▼
                                  Spot.can_park()
                                        │
                                        ▼
                                Spot.park_vehicle()
                                        │
                                        ▼
                                  Create Ticket
                                        │
                                        ▼
                                      EXIT
                                        │
                                        ▼
                                ParkingService
                                        │
                                        ▼
                              FeeStrategyFactory
                                        │
                         ┌──────────────┼──────────────┐
                         ▼              ▼              ▼
                       Bike            Car           Truck
                         │              │              │
                         └──────────────┼──────────────┘
                                        ▼
                                  FeeCalculator
                                        │
                                        ▼
                                  PaymentService
                                        │
                                        ▼
                              Card/Cash Strategy
                                        │
                                        ▼
                              Spot.remove_vehicle()
                                        │
                                        ▼
                            ParkingLot.remove_vehicle()
                                        │
                                        ▼
                                   Return Fee
```

---

# 17. Sequence Diagram

The parking sequence is:

```text
Driver        ParkingService      ParkingLot       Floor       Spot       Ticket
  |                 |                |               |           |           |
  | park(vehicle)   |                |               |           |           |
  |---------------->|                |               |           |           |
  |                 | findSpot()     |               |           |           |
  |                 |--------------->|               |           |           |
  |                 |                | findSpot()    |           |           |
  |                 |                |-------------->|           |           |
  |                 |                |               | find()    |           |
  |                 |                |               |---------->|           |
  |                 |                |               |           | available |
  |                 |                |               |<----------|           |
  |                 |<---------------|               |           |           |
  |                 | parkVehicle()   |               |           |           |
  |                 |------------------------------------------->|           |
  |                 | createTicket() |               |           |           |
  |                 |------------------------------------------------------>|
  |                 |<------------------------------------------------------|
  |<----------------| ticket         |               |           |           |
```

---

# 18. Folder Structure

```text
parking_lot/
│
├── main.py
│
├── entities/
│   ├── __init__.py
│   ├── vehicle.py
│   ├── parking_spot.py
│   ├── parking_floor.py
│   ├── parking_lot.py
│   ├── ticket.py
│   └── payment.py
│
├── enums/
│   ├── __init__.py
│   └── parking_enums.py
│
├── interfaces/
│   ├── __init__.py
│   ├── fee_strategy.py
│   └── payment_strategy.py
│
├── strategies/
│   ├── __init__.py
│   ├── fee_strategies.py
│   └── payment_strategies.py
│
├── factories/
│   ├── __init__.py
│   ├── vehicle_factory.py
│   └── fee_strategy_factory.py
│
└── services/
    ├── __init__.py
    ├── parking_service.py
    ├── fee_calculator.py
    └── payment_service.py
```

---

# 19. Runtime Flow

## Creating the Structure

```text
ParkingLot()
      ↓
ParkingFloor()
      ↓
ParkingSpot()
      ↓
floor.add_spot()
      ↓
lot.add_floor()
```

---

## Creating Vehicle

```text
VehicleFactory.create_vehicle()
      ↓
Car()
      ↓
Vehicle()
```

---

## Parking

```text
ParkingService.park_vehicle()
      ↓
ParkingLot.is_vehicle_parked()
      ↓
ParkingLot.find_available_spot()
      ↓
ParkingFloor.find_available_spot()
      ↓
ParkingSpot.can_park()
      ↓
ParkingSpot.is_available()
      ↓
ParkingSpot.park_vehicle()
      ↓
Ticket()
```

---

## Exit

```text
ParkingService.unpark_vehicle()
      ↓
FeeStrategyFactory.get_strategy()
      ↓
CarFeeStrategy.calculate_fee()
      ↓
FeeCalculator.calculate()
      ↓
PaymentService.process_payment()
      ↓
CardPaymentStrategy.pay()
      ↓
ParkingSpot.remove_vehicle()
      ↓
ParkingLot.remove_vehicle()
      ↓
return fee
```

---

# 20. Class Responsibilities

| Class                       | Main Responsibility                   |
| --------------------------- | ------------------------------------- |
| `Vehicle`                   | Common vehicle data                   |
| `Bike/Car/Truck`            | Specific vehicle type                 |
| `ParkingSpot`               | Occupancy + compatibility             |
| `ParkingFloor`              | Manage/search spots                   |
| `ParkingLot`                | Manage floors + parked vehicle lookup |
| `Ticket`                    | Parking session                       |
| `Payment`                   | Payment record                        |
| `VehicleFactory`            | Create vehicle                        |
| `FeeStrategy`               | Fee calculation contract              |
| `Bike/Car/TruckFeeStrategy` | Actual pricing                        |
| `FeeStrategyFactory`        | Select pricing strategy               |
| `FeeCalculator`             | Execute fee calculation               |
| `PaymentStrategy`           | Payment contract                      |
| `Cash/CardPaymentStrategy`  | Actual payment method                 |
| `PaymentService`            | Payment processing                    |
| `ParkingService`            | **Coordinates the overall workflow**  |

---

# 21. Complete Parking Flow

```text
                         PARKING

Driver
  │
  ▼
ParkingService.park_vehicle()
  │
  ▼
Check if vehicle already parked
  │
  ├── YES → Error
  │
  └── NO
       │
       ▼
ParkingLot.find_available_spot()
       │
       ▼
ParkingFloor.find_available_spot()
       │
       ▼
ParkingSpot.can_park()
       │
       ├── NO → Continue searching
       │
       └── YES
            │
            ▼
       ParkingSpot.park_vehicle()
            │
            ▼
       Add vehicle to parked set
            │
            ▼
       Create Ticket
```

---

# 22. Complete Exit Flow

```text
                         EXIT

Driver
  │
  ▼
ParkingService.unpark_vehicle()
  │
  ▼
Check ticket
  │
  ├── Already exited → Error
  │
  ▼
Get exit time
  │
  ▼
FeeStrategyFactory
  │
  ├── Bike → BikeFeeStrategy
  ├── Car → CarFeeStrategy
  └── Truck → TruckFeeStrategy
  │
  ▼
FeeCalculator
  │
  ▼
PaymentService
  │
  ├── CashPaymentStrategy
  └── CardPaymentStrategy
  │
  ▼
Payment successful?
  │
  ├── NO → Vehicle remains parked
  │
  └── YES
       │
       ▼
Set ticket exit time
       │
       ▼
ParkingSpot.remove_vehicle()
       │
       ▼
ParkingLot.remove_vehicle()
       │
       ▼
Return fee
```

---

# 23. Important Design Concepts Used

## 23.1 Encapsulation

We keep data and operations together.

Example:

```python
class ParkingSpot:

    def __init__(self, ...):
        self.vehicle = None

    def can_park(self, vehicle):
        ...

    def park_vehicle(self, vehicle):
        ...

    def remove_vehicle(self):
        ...
```

`ParkingSpot` owns:

* `vehicle`
* `spot_type`

and controls:

* `can_park()`
* `park_vehicle()`
* `remove_vehicle()`

### Interview Question

**Why not directly modify `spot.vehicle` from `ParkingService`?**

### Answer

Because `ParkingSpot` should control its own state. Encapsulating the state prevents invalid operations such as parking an incompatible vehicle or removing a vehicle from an empty spot.

---

# 24. Composition

Our objects are composed together:

```text
ParkingLot
   │
   └── ParkingFloor
          │
          └── ParkingSpot
                 │
                 └── Vehicle
```

This represents HAS-A relationships.

```python
class ParkingLot:
    self.floors

class ParkingFloor:
    self.spots

class ParkingSpot:
    self.vehicle
```

### Interview Question

**Why did you use composition instead of inheritance here?**

### Answer

Because a parking lot HAS floors, a floor HAS parking spots, and a parking spot HAS a vehicle. These are containment relationships, so composition is more appropriate than inheritance.

---

# 25. Inheritance

We use inheritance for vehicles:

```python
class Vehicle:
    ...

class Car(Vehicle):
    ...

class Bike(Vehicle):
    ...

class Truck(Vehicle):
    ...
```

Because:

```text
Car IS-A Vehicle
Bike IS-A Vehicle
Truck IS-A Vehicle
```

We also use inheritance for strategies:

```text
FeeStrategy
    ↑
    ├── BikeFeeStrategy
    ├── CarFeeStrategy
    └── TruckFeeStrategy
```

And:

```text
PaymentStrategy
    ↑
    ├── CashPaymentStrategy
    └── CardPaymentStrategy
```

---

# 26. Strategy Pattern

This is one of the most important patterns in our Parking Lot.

```python
class FeeStrategy(ABC):

    @abstractmethod
    def calculate_fee(...):
        ...
```

Then:

```text
FeeStrategy
    ↑
    ├── BikeFeeStrategy
    ├── CarFeeStrategy
    └── TruckFeeStrategy
```

Each strategy implements:

```text
calculate_fee()
```

### Why?

Because fee calculation changes depending on vehicle type.

Instead of:

```python
if bike:
    ...
elif car:
    ...
elif truck:
    ...
```

we use polymorphism.

---

# 27. Factory Pattern

We use:

```python
class FeeStrategyFactory:

    @staticmethod
    def get_strategy(vehicle_type):
        ...
```

This decides:

```text
CAR
 ↓
CarFeeStrategy

BIKE
 ↓
BikeFeeStrategy

TRUCK
 ↓
TruckFeeStrategy
```

We also have:

```text
VehicleFactory
```

which creates:

```text
CAR → Car()
BIKE → Bike()
TRUCK → Truck()
```

### Interview Question

**Why do you need Factory if you already have Strategy?**

### Answer

Strategy defines interchangeable behavior, while Factory is responsible for selecting or creating the appropriate strategy.

In our case, the Factory selects the fee strategy based on the vehicle type.

This distinction is very important.

---

# 28. Dependency Injection

Our:

```text
ParkingService
```

doesn't create everything internally.

We give it:

```text
ParkingLot
FeeCalculator
PaymentService
```

Example:

```python
parking_service = ParkingService(
    parking_lot,
    fee_calculator,
    payment_service
)
```

This is dependency injection.

### Why?

Because now `ParkingService` isn't tightly coupled to concrete implementations.

For example:

```text
ParkingService
      │
      ├── PaymentService(Card)
      │
      OR
      │
      └── PaymentService(Cash)
```

We can change dependencies without modifying `ParkingService`.

### Interview Question

**Why didn't you create `PaymentService()` inside `ParkingService`?**

### Answer

To reduce coupling and make the service easier to test and extend. Dependencies are supplied from outside.

---

# 29. Polymorphism

We use polymorphism heavily.

For example:

```python
strategy.calculate_fee(...)
```

We don't care whether:

```text
BikeFeeStrategy
CarFeeStrategy
TruckFeeStrategy
```

is being used.

They all satisfy:

```text
FeeStrategy.calculate_fee()
```

Similarly:

```python
payment_strategy.pay(amount)
```

works for:

```text
Cash
Card
```

This is one of the strongest reasons Strategy works well here.

---

# 30. Single Responsibility Principle

We separated responsibilities.

```text
Vehicle
 → vehicle information

ParkingSpot
 → spot occupancy

ParkingFloor
 → manage spots

ParkingLot
 → manage floors/vehicles

Ticket
 → parking session

FeeStrategy
 → fee calculation

PaymentStrategy
 → payment method

ParkingService
 → coordinate workflow
```

Instead of making one giant:

```text
ParkingLotManager
```

with 1000 lines.

---

# 31. Open/Closed Principle

Suppose tomorrow:

```text
SUV
```

needs a different fee.

We can add:

```python
class SUVFeeStrategy(FeeStrategy):
    ...
```

and update the Factory.

Existing strategies don't need modification.

Similarly:

```text
UPIPaymentStrategy
```

can be added without modifying:

```text
CashPaymentStrategy
CardPaymentStrategy
```

---

# 32. Patterns We Did NOT Use

Our Parking Lot does not meaningfully use:

* Singleton
* Builder
* Observer
* Adapter
* Decorator
* Command
* State

Don't force patterns into a design.

### Interview Question

**What design patterns did you use?**

### Answer

> I primarily used Strategy and Factory. Strategy handles varying fee and payment behavior, while Factory selects the appropriate vehicle or fee strategy. I also used composition, inheritance, polymorphism, dependency injection, and encapsulation. I intentionally avoided unnecessary patterns.

This answer is better than saying:

> I used eight design patterns.

---

# 33. Why Didn't You Use Singleton for ParkingLot?

### Interview Question

**Why didn't you use Singleton for `ParkingLot`?**

### Answer

> Singleton would unnecessarily restrict the design to one parking lot instance. Although the current requirement models one parking lot, the domain could naturally support multiple parking lots in the future. I prefer normal object ownership unless the requirement explicitly guarantees a single instance.

---

# 34. Where Everything Is in the Project

```text
entities/
│
├── vehicle.py
│      └── Inheritance
│
├── parking_spot.py
│      └── Encapsulation
│
├── parking_floor.py
│      └── Composition
│
├── parking_lot.py
│      └── Composition + collection management
│
└── ticket.py
       └── Domain entity


interfaces/
│
├── fee_strategy.py
│      └── Strategy interface
│
└── payment_strategy.py
       └── Strategy interface


strategies/
│
├── fee_strategies.py
│      └── Strategy implementations
│
└── payment_strategies.py
       └── Strategy implementations


factories/
│
├── vehicle_factory.py
│      └── Factory Pattern
│
└── fee_strategy_factory.py
       └── Factory Pattern


services/
│
├── parking_service.py
│      └── Workflow orchestration
│
├── fee_calculator.py
│      └── Fee calculation coordination
│
└── payment_service.py
       └── Payment coordination
```

---

# 35. Reusable LLD Structure

We'll see variations of this structure again and again in upcoming LLD problems:

```text
                 DOMAIN ENTITIES
                       │
                       ▼
                 SERVICE LAYER
                       │
              ┌────────┴────────┐
              ▼                 ▼
          STRATEGY           FACTORY
              │                 │
              ▼                 ▼
        Different          Select/Create
        behaviors             object
```

For Parking:

```text
Vehicle / Spot / Ticket
          │
          ▼
    ParkingService
       │       │
       ▼       ▼
 FeeStrategy  PaymentStrategy
       ▲
       │
FeeStrategyFactory
```

We'll recognize variations of this structure in:

* ATM
* Restaurant
* Movie Booking
* Inventory
* Elevator
* Splitwise

But not every problem will use the same patterns.

---

# 36. Important Interview Questions

## Design

### Q: Why is ParkingService needed?

**Answer:**

It coordinates the parking and exit workflows while keeping individual entities focused on their own responsibilities.

---

### Q: Why is ParkingSpot responsible for `park_vehicle()`?

**Answer:**

Because it owns the occupancy state and should enforce its own invariants.

---

### Q: Why is Vehicle an abstraction?

**Answer:**

Car, Bike and Truck share common vehicle properties and form an IS-A relationship.

---

### Q: Why separate VehicleType and SpotType?

**Answer:**

They represent different domain concepts. A vehicle has a type, while a spot defines compatibility/capacity. Keeping them separate allows independent evolution.

---

# 37. Pattern Interview Questions

### Q: Why Strategy?

**Answer:**

Because fee and payment behavior can vary independently and may grow over time.

---

### Q: Why Factory?

**Answer:**

To centralize object/strategy creation and avoid spreading conditional construction logic throughout the application.

---

### Q: Strategy vs Factory?

**Answer:**

> Strategy chooses behavior; Factory creates/selects the appropriate object.

---

# 38. SOLID Interview Questions

### Q: Which SOLID principles did you apply?

Mention:

* SRP
* OCP
* DIP / Dependency Injection

Don't claim every SOLID principle unless you can explain it.

---

# 39. Edge Cases

An interviewer may ask:

* What if the parking lot is full?
* What if a vehicle is already parked?
* What if the wrong vehicle enters a spot?
* What if the ticket is invalid?
* What if the ticket is used twice?
* What if payment fails?
* What if payment succeeds but spot release fails?
* What if two cars try to take the same spot simultaneously?

The last question introduces **concurrency**, which becomes more important when discussing real backend/system design.

---

# 40. Key Design Recognition Rules

Don't memorize:

> Parking Lot uses Factory + Strategy.

Instead learn to recognize **why**.

```text
If behavior varies
        ↓
Think Strategy
```

```text
If object selection/creation varies
        ↓
Think Factory
```

```text
If objects contain other objects
        ↓
Think Composition
```

```text
If objects share an IS-A relationship
        ↓
Think Inheritance
```

```text
If one class has too many responsibilities
        ↓
Think SRP / decomposition
```

```text
If a class directly creates all its dependencies
        ↓
Think Dependency Injection
```

This recognition skill will let us solve:

* Tic Tac Toe
* ATM
* Elevator
* Splitwise
* Movie Booking
* Restaurant Management
* Inventory Management

without memorizing complete designs.

---

# 41. Interview Explanation — 60 Second Version

If the interviewer asks:

> **"Explain your Parking Lot design."**

Don't start explaining every class randomly.

Say:

> The `ParkingService` acts as the main orchestrator. During parking, it first checks whether the vehicle is already parked, asks `ParkingLot` to find a compatible spot, and delegates the actual parking operation to `ParkingSpot`. It then creates a `Ticket`.
>
> During exit, it gets the vehicle type from the ticket, uses `FeeStrategyFactory` to select the appropriate pricing strategy, calculates the fee, processes payment through `PaymentService`, and only after successful payment releases the spot and removes the vehicle from the active parking set.

---

# 42. Core Takeaway

The most important lesson from this Parking Lot problem is not:

```text
"Parking Lot = Factory + Strategy"
```

The important lesson is recognizing the underlying design principles:

```text
Behavior varies
      ↓
Strategy

Object creation/selection varies
      ↓
Factory

HAS-A relationship
      ↓
Composition

IS-A relationship
      ↓
Inheritance

Separate responsibilities
      ↓
SRP

Depend on abstractions / inject dependencies
      ↓
Dependency Injection

Common interface + different implementations
      ↓
Polymorphism
```

This is the foundation we will reuse when solving the remaining LLD problems.
