CityStopsList = ['Westmoreland Station', 'Hampton Station', 'Tyler/Verona Station']
IDTracker = [0]
class TrainSystem:
    uniqueID = IDTracker[-1]
    IDTracker.append(IDTracker[-1]+1)
    name = '' #Name of the train or line.
              #If line name then it would not work as the unique identifier in database
              #Name might also cause issues if there is nothing inplace to prevent duplicate entries
              #Consider using an auto incremental ID system with leading zeroes ie. 0001, 0206 5204, 9999
              #This system would limit the number of available ID systems, could cause issues on state, national or global scale
              #but should hold fine for local, city, and county scales. Removing formatting contrainsts would solve this, however train/line numbers would become less standardized

    routeLine = '' #Ordered list of bus stops representing the stops visited by the bus.
                   #Use modulus for loops where i is # iterations and n is total number of stops
                   #i%n = 0, 1, 2, ... n-1, 0, 1, 2 ...
                   #TODO: CURRENT IMPLAMETNED ROUTELINE IS PLACE HOLDER, MAKE EMPTY, OR CREATE LINE COLOR DICTIONARY

    maxSpeedMPH = 150 #If we display live locations speed of train would be used to calculate current position
                      #However this method requires calculating integrals to account for acceleration might be to complex for our current time scop

    onTime = True
    delayDictionary = {} #For the delay dictionary all stops that the train visits will be added as keys. The values represent the delay in minutes.
                         #Delays should propagate, if and earlier stop is delayed then so are later stops until the loop resets
                         #TODO: CREATE SYSTEM THAT ADDS EARLIER DELAYS TO LATER STOPS IE. IF STOP 3 IS DELAYED THEN STOPS 4 5 6 . . . N ARE ALSO DELAYED BY AN EQUAL AMOUNT OF TIME.

    for i in routeLine:
        delayDictionary[i] = 0

    def PrintSchedule(self): #TODO: DEVELOPE MORE INDEPTH
        print(self.routeLine)

    def PrintDelays(self): #TODO: COMPLETE FUNCTION TO PRINT DELAYS
        pass

    def UpdateDelays(self, delayList): #TODO: COMPLETE FUNCTION TO UPDATE DELAY DICTIONARY AND STATUS
        pass

    def UpdateRoute(self,newRoute): #TODO: COMPLETE FUNCTION TO UPDATE THE ROUTE THE TRAIN FOLLOWS
        pass

