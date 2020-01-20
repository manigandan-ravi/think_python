class Time():

    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def time_to_int(self):
        minutes = self.hours*60 + self.minutes
        seconds = minutes*60 + self.seconds
        #print(minutes, seconds)
        return seconds

    def int_to_time(seconds):
        time = Time()
        minutes, time.seconds = divmod(seconds,60)
        time.hours,time.minutes = divmod(minutes,60)
        return time

    def add_time(self,other):
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)

    def __add__(self, other):
        # seconds = self.time_to_int() + other.time_to_int()
        # return Time.int_to_time(seconds)
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return  self.__add__(other)

    def increment(self,seconds):
        seconds += self.time_to_int()
        #print(seconds)
        return Time.int_to_time(seconds)

    # def print_time(self):
    #     #print(self.hours, ":", self.minutes, ":", self.seconds)
    #     print(('%.2d:%.2d:%.2d')%(self.hours,self.minutes,self.seconds))

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hours, self.minutes, self.seconds)


start = Time(9,45,0)
duration = Time(1,35,0)
#duration = duration.increment(100)
duration += 100
# total = Time().add_time(start,duration)
total = start+duration
# start.print_time()
# duration.print_time()
#total.print_time()
print(start)
print(duration)
print(total)
#print(100+total)