""" A practice problem for object-oriented programming """

class Date(object):
    """ Represents a particular day on the calendar """
    def __init__(self, month, day, year):
        """ Initializes a Date object

            month: the month (represented as an integer in [1,12])
            day: the day of the month (represented as an integer)
            year: the year (represented as an integer)
            This method will not validate whether a given date is invalid
            (e.g. April 31, 2000) """
        self.month = month
        self.day = day
        self.year = year 


    def is_before(self,other_date):
        """ Returns true if and only if self occurs before other_date

            >>> d1 = Date(4,20,1981)
            >>> d2 = Date(5,31,1995)
            >>> d1.is_before(d2)
            True
        """
        d1 = self
        d2 = other_date
        if d1.year > d2.year:
            return False
        elif d1.year == d2.year:
            if d1.month > d2.month:
                return False
            elif d1.month == d2.month:
                if d1.day > d2.day:
                    return False
        else:
            return True


    def __str__(self):
        """ Converts the date to a string in the following format:
            Month, Day Year (where Month is the name of the month, e.g. January)

        >>> print Date(3,26,2015)
        March, 26th 2015
        """
        pass

    def increment_year(self):
        """ Modifies the Date object self so that it represents a date of the
            same month and day but for the following year. 
        >>> d1 = Date(4,20,2003)
        >>> d1.increment_year()
        >>> d1.is_leap_year()
        True
        """
        self.date += 1

    def is_leap_year(self):
        """ Returns true if the year that this date falls in is a leap year
            see: http://en.wikipedia.org/wiki/Leap_year

            Note: please add appropriate doctests BEFORE you start coding 

        >>> d1 = Date(4,20,2004)
        >>> d1.is_leap_year()
        True
        >>> d2 = Date(4,20,2014)
        >>> d2.is_leap_year()
        False
        """
        if self.year % 4 == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()