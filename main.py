from extract import Extract
from transform import Transform
from load import Load

if __name__ == "__main__":
    path = "data/Flight_data.csv"
    extractor = Extract()
    data= extractor.extract_info(path)
    
    transform= Transform()
    data = transform.transform_data(data)
    flight, airline, airport, price, route_detail = data
    
    loader = Load()
    loader.load_data(flight, airline, airport, price, route_detail)

