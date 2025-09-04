from extract import Extract
from transform import Transform

if __name__ == "__main__":
    path = "data/Flight_data.csv"
    extractor = Extract()
    data= extractor.extract_info(path)
    
    transform= Transform()
    data = transform.transform_data(data)
    print(data.head())  # Display the first few rows of the extracted data
    data.to_csv("data/transformed_flight_data.csv", index=False)
    print("Transformed data saved to 'data/transformed_flight_data.csv'")
    print(data.dtypes)
    print(data.columns)
    # You can add more processing or saving logic here as needed
    # additional_info,arrival_time,dep_time,duration,flight,journey_date,price,route