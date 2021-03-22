def create_car(manufacturer, model, **car_info):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car


car = create_car('subaru','outback', color='blue', tow_package=True)
print(car)