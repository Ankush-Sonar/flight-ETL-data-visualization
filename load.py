from sqlalchemy import create_engine, types
from tablestructure import TableStructure

class Load:
    def load_data(self, flight, airline, airport, price, route_detail):
        engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/sys')
        self.save_to_db(flight, 'flight', engine)
        self.save_to_db(airline, 'airline', engine)
        self.save_to_db(airport, 'airport', engine) 
        self.save_to_db(price, 'price', engine)
        self.save_to_db(route_detail, 'route_detail', engine)

    def save_to_db(self, df, table_name, engine):
        tablestructure_obj = TableStructure()
        dtype_mapping = {
            'airport': tablestructure_obj.dtype_airport,
            'price': tablestructure_obj.dtype_price,
            'airline': tablestructure_obj.dtype_airline,
            'route_detail': tablestructure_obj.dtype_route_dtls,
            'flight': tablestructure_obj.dtype_journey_dtls
        }   
        if table_name in dtype_mapping:
            df.to_sql(name=table_name, con=engine, if_exists='append', index=False, dtype=dtype_mapping[table_name])
        else:
            raise ValueError(f"Unknown table name: {table_name}")