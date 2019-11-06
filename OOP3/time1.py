class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

    def print_time(self):
       print(f"{self.hour:02d}:{self.minute:02d}
       :{self.second:02d}")

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    

start = Time()
start.hour = 3
start.minute = 11
start.second = 30

start.print_time()
print(start.time_to_int())

end = start.increment(100)
end.print_time()
print(end.is_after(start))

