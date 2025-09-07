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
    
    
    def route_detail(self,data):
        route_detail = (
        data['route']
        .str.strip()
        .str.split(',')
        .explode()
        .reset_index()
        .rename(columns={'index': 'route_dtls_id', 'route': 'route'})
        )
        route_detail["route"] = route_detail["route"].str.strip()

        route_detail['route_dtls_id'] += 1
        route_detail = route_detail.merge(airport, left_on='route', right_on='code', how='left')
        route_detail = route_detail[['route_dtls_id', 'airport_id', 'route','code']]
        route_detail['airport_id'] = route_detail['airport_id'].fillna(-1)
        route_detail['airport_id'] = route_detail['airport_id'].astype(int)

    def flight(self, data, airline, airport, price, route_detail):
        # Merge with airline, keep only relevant columns
        journey_table = journey_table.merge(
            airline[['airline', 'airline_id']], on='airline', how='left'
        )

        # Merge to get source airport info, rename duplicated airport_id as source_id
        journey_table = journey_table.merge(
            airport, left_on='source', right_on='name', how='left',
            suffixes=('', '_source')
        ).rename(columns={'airport_id': 'source_id'})