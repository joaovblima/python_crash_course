def car_info(car_name, car_brand, **car_infos):
    
    car_infos['car_name'] = car_name
    car_infos['car_brand'] = car_brand
    return car_infos


my_car = car_info('gol', 'volksvagen', color='white', tow_package=True, hidraulic=True)
print(my_car)