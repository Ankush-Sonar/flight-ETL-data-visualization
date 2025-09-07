import pandas as pd

class Transform:
    def transform_data(self, data):
        return data

    def airline(self, data):
        airline = data[['airline', 'airline_id']].drop_duplicates().reset_index(drop=True)
        airline['airline_id'] = airline.index + 1
        return airline
    


        
    def airport(self, data):
        # Select needed columns
        airport = data[['source', 'destination', 'route']].copy()

        # Split route into list once and reuse
        split_route = airport['route'].str.split(',')

        airport['source_cd'] = split_route.str[0]
        airport['destination_cd'] = split_route.str[-1]

        # Reshape into long format in one step
        airport = pd.concat([
            airport[['source', 'source_cd']].rename(columns={'source': 'name', 'source_cd': 'code'}),
            airport[['destination', 'destination_cd']].rename(columns={'destination': 'name', 'destination_cd': 'code'})
        ], ignore_index=True)

        # Clean and finalize
        airport['name'] = airport['name'].str.strip()
        airport['code'] = airport['code'].str.strip()
        airport = airport.dropna(subset=['name', 'code']).drop_duplicates(subset=['name', 'code']).reset_index(drop=True)
        airport['country'] = 'India'
        airport['airport_id'] = range(1, len(airport) + 1)

        # Drop invalid "nan" string codes
        airport = airport[airport['code'] != 'nan']
        return airport
    
    def price_detail(self, data):
        price = data[['price']].drop_duplicates().reset_index(drop=True)
        price['currency'] = 'INR'
        price['price_id'] = price.index + 1 
        return price
    
    
    