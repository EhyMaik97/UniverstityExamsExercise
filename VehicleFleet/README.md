***VEHICLE FLEET***


Simulate a paid fleet of cars and motorcycles. To do this, implement the following
classes, documenting them appropriately and possibly reusing the classes of the standard packages, with constructors
necessary, __str__() and (at least) the indicated methods:


**Vehicle**: identified by a license plate (string) with subtypes:
+ **Cars** with parking cost 0:10$/unit
+ **Motorbikes** with parking cost 0:25$/unit


**Seat**: with a status (FREE, OCCUPIED),
and data on any vehicle occupant and methods:
+ constructor for FREE Seat;
+ occupies the place, with the necessary parameters;
+ free the place, with the necessary parameters;


**Park**: with two collections of places, distinguished by type of vehicle,
its own clock that ticks the units of time and, moreover:
+ the constructor initializes a parking with maximum capacity maxAuto and maxMoto;
+ entry: manages an entry vehicle printing information on the occupied seat;
+ exit: manages an exiting vehicle, with printing of a receipt with 
vehicle data, the indication of the time of entry and exit, the calculated parking cost;
+ tic to scan the units of time, passing to the next;
+ promo: offers a discount of one for free certain percentage of the
total cost of parking at all vehicles in the parking lot whose license
plate ends with code, two-digit numeric string;
+ status returns the two lists of vehicle seats, one per type, sorted by duration.


**Test**: simulation of the passing of 99 units of time with output also
on file of text
1. in each unit of time:
   + an arrival or departure occurs (if permissible) 
   of a vehicle with 50% probability (otherwise nothing to do):
   it will have to be a car in about 60% of cases;
   + parking status printout;
2. handle two promotion cases at random times, while also randomly 
generating the code lucky and a percentage discount (max 20%)
