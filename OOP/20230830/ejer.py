class Clock:
  def __init__(self, hours,minutes,seconds):
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
    counter_hours = Counter(24)
    self._hours = counter_hours.increment(hours)

  @minutes.setter
  def minutes(self, minutes):
    counter_minutes = Counter(60)
    self._minutes = counter_minutes.increment(minutes)
  
  @seconds.setter
  def seconds(self, seconds):
    counter_seconds = Counter(60)
    self._seconds = counter_seconds.increment(seconds)
  
  def __str__(self):
    return f'{self.hours}:{self.minutes}:{self.seconds}'
  def __repr__(self):
    return f'{self.hours}:{self.minutes}:{self.seconds}'

  

class Counter:
  def __init__(self, max_value):
    self.max_value = max_value
    self.counter = 0

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
    self._max_value = (self._max_value + 1) % self._max_value

  def __repr__(self):
    return f'{self._counter}'