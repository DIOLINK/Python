class Clock:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self._hours

    @property
    def minutes(self):
        return self._minutes

    @property
    def seconds(self):
        return self._seconds

    @hours.setter
    def hours(self, hours):
        counter_hours = Counter(24, hours)
        self._hours = counter_hours.increment()

    @minutes.setter
    def minutes(self, minutes):
        counter_minutes = Counter(60, minutes)
        self._minutes = counter_minutes.increment()

    @seconds.setter
    def seconds(self, seconds):
        counter_seconds = Counter(60, seconds)
        self._seconds = counter_seconds.increment()

    def __str__(self):
        return f'{self.hours}:{self.minutes}:{self.seconds}'

    def __repr__(self):
        return f'{self._hours}:{self._minutes}:{self._seconds}'


class Counter:
    def __init__(self, max_value, start_value=0):
        self.max_value = max_value
        self.counter = start_value

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, counter):
        self._counter = counter

    @property
    def max_value(self):
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        self._max_value = max_value

    def increment(self):
        self._counter = (self._counter + 1) % self._max_value
        return self._counter

    def __repr__(self):
        return f'{self._counter }'


co = Counter(24)
co.increment()

clock = Clock(12, 25, 55)

print(clock)
