from sqlalchemy import types

class TableStructure:
    
    # def table_structure(self,data):
    #     data['route']= data['route'].astype(str)
    #     data['journey_id'] = data.index + 1
    #     data['arrival_time']= data['arrival_time'].str.split(' ').apply(lambda x: x[1] if len(x)>1 else x[0])
    #     data['departure'] = data['journey_date'].str.cat(data['dep_time'], sep=' ')
    #     data["departure"] = pd.to_datetime(data["departure"], format='%d-%m-%Y %H:%M')
    #     data['arrival_time'] = data['arrival_time'].str.strip()
    #     data['arrival_time'] = pd.to_datetime(data['arrival_time'], format='%H:%M').dt.time
    #     data['duration'] = pd.to_timedelta(data['duration'].str.replace('h', ' hours ').str.replace('m', ' minutes'))
    #     data['arrival'] = data['departure'] + data['duration']
    #     print(data['arrival_time'].dtypes)
    #     return data

    dtype_airport = {
    'airport_id': types.BIGINT(),
    'country': types.VARCHAR(20),
    'code': types.VARCHAR(20),
    'name': types.VARCHAR(20)
    }

    dtype_price = {
    'price_id': types.BIGINT(),
    'price': types.Float(20),
    'currency': types.VARCHAR(20)
    }
    
    dtype_airline = {
    'airline_id': types.BIGINT(),
    'name': types.VARCHAR(20)
    }

    dtype_route_dtls = {
    'route_dtls_id': types.BIGINT(),
    'airport_id': types.BIGINT(),
    'route': types.VARCHAR(10)
    }

    dtype_journey_dtls = {
    'journey_id': types.BIGINT(),
    'airline_id': types.BIGINT(),
    'source': types.VARCHAR(10),
    'source_id': types.BIGINT(),
    'destination': types.VARCHAR(20),
    'price_id': types.BIGINT(),
    'route_dtls_id': types.BIGINT(),
    'additional_info': types.VARCHAR(45),
    'departure': types.DATETIME(),
    'arrival': types.DATETIME(),
    }

