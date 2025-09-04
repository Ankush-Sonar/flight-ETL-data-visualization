from extract import Extract
from transform import Transform

if __name__ == "__main__":
    path = "data/Flight_data.csv"
    extractor = Extract()
    data= extractor.extract_info(path)
    
    transform= Transform()
    data = transform.transform_data(data)
    print(data.head())  # Display the first few rows of the extracted data
    # hello
    # hello
    # hello

    # hello
    # hello# hello
    # hello# hello
    # hello
    # hello
    # hello
    # hello
    # hello