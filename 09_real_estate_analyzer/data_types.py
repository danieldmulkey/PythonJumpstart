class Purchase:
    def __init__(self, street, city, zipcode, state, beds, baths, sq_ft, home_type,
                 sale_date, price, latitude, longitude):
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.state = state
        self.beds = beds
        self.baths = baths
        self.sq_ft = sq_ft
        self.home_type = home_type
        self.sale_date = sale_date
        self.price = price
        self.latitude = latitude
        self.longitude = longitude

    @staticmethod  # deals with class/type, not instance of class/the object --> staticmethod --> no self
    def create_from_dict(lookup):
        return Purchase(
            lookup['street'],
            lookup['city'],
            lookup['zip'],
            lookup['state'],
            int(lookup['beds']),
            int(lookup['baths']),
            int(lookup['sq_ft']),
            lookup['type'],
            lookup['sale_date'],
            float(lookup['price']),
            float(lookup['latitude']),
            float(lookup['longitude']))
