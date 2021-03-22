def describe_city(city_name, country = 'south korea'):
    print(city_name.title() + " is in " + country.title())

describe_city('Seoul')
describe_city('Busan')
describe_city('Tokyo', 'Japan')