class Band:
    def __init__(self, name, hometown):
        assert len(name) > 0
        assert len(hometown) > 0
        self._name = name
        self._hometown = hometown
        self.concert_list = []
        self.venue_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if not 0 <  len(value):
            raise ValueError("Must be greater than zero")
        self._name = value


    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):

        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if not 0 <  len(value):
            raise ValueError("Must be greater than zero")
        if hasattr(self, "_hometown"):
            raise AttributeError("Cannot be changed")
        self._hometown = value

    def add_concert(self, concert):
        self.concert_list.append(concert)

    def concerts(self):
        return self.concert_list

    def add_venue(self, venue):
        self.venue_list.append(venue)

    def venues(self):
        venue = [concert.venue for concert in self.concert_list]

        return list(set(venue))

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        return concert

    def all_introductions(self):
        
        return f"Hello NYC !!!!! We are {self.name} and we are from {self.hometown}"



class Concert:
    all = []
    def __init__(self, date, band, venue):
        
        self._date = date
        self._band = band
        self._venue = venue 
        band.add_concert(self)
        venue.add_concert(self)
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if not 0 <  len(value):
            raise ValueError("Must be greater than zero")
        self._date = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if not isinstance(value, Venue):
            raise TypeError("Venue must be an instance of Venue")
        self._venue = value

        


    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if not isinstance(value, Band):
            raise TypeError("Venue must be an instance of Venue")
    
        self._band = value

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    all = []

    def __init__(self, name, city):
        self._name = name
        self._city = city
        self.concert_list = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if not 0 <  len(value):
            raise ValueError("Must be greater than zero")
        self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")
        if not 0 <  len(value):
            raise ValueError("Must be greater than zero")
        self._city = value

    def add_concert(self, concert):
        self.concert_list.append(concert)

    def concerts(self):
        return self.concert_list

    # def concert_on(self, date):
    #     count = Counter([concert.date for concert in self.concert_list])
    #     first_concert = [concert for concert, count in count.items if count[0]]
    #     return first_concert if first_concert else None

    def bands(self):
        band = [concert.band for concert in self.concert_list]
        return list(set(band))


# muso1 = Band("Muso", "AHS")
# # # muso1.hometown = "Lenana"
# venue1 = Venue("Kisumu", "Kisumu")

# concert = Concert(11, muso1, venue1)

# print(muso1.concerts())

# print(muso1.add_concert())

# print(muso1.venues)
