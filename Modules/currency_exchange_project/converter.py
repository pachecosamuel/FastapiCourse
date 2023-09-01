import requests
from os import getenv
from fastapi import HTTPException

API_KEY = getenv('API_KEY')

def sync_version(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&/\
            from_currency={from_currency}&\
            to_currency={to_currency}&\
            apikey={API_KEY}'
            
    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    data = response.json(response)
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail="Currency change is not in response")
    
        
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    
    return price * exchange_rate
    