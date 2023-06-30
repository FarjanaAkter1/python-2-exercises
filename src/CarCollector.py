class CarCollector:

    car_list = [
        {"id": 1, "price": 10000},
        {"id": 2, "price": 20000},
        {"id": 3, "price": 30000},
    ]
    car_dict = {
        1: "Ford",
        2: "Mazda",
        3: "Chevy"
    }

    @staticmethod
    def get_data():
        return list(map(CarCollector._combine, CarCollector.car_list))
    
    @staticmethod
    def _combine(c):
      car_id =c ['id']

      car_make = CarCollector.car_dict[car_id] 

      car_price =c['price']

        # Todo...
      return { 'id': car_id ,'make': car_make,'price':car_price }
    
