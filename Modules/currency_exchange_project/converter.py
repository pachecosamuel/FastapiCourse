import aiohttp
import requests
from os import getenv
from fastapi import HTTPException

api_key = "FZXECI7425K14Z22"

async def async_version_exchange(from_currency: str, to_currency: str, price: float):
            
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(from_currency, to_currency, api_key)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url) as response:
                data = await response.json()
                
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail="Currency change is not in response")
    
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    
    return price * exchange_rate
    

def sync_version_exchange(from_currency: str, to_currency: str, price: float):
            
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey={}'.format(from_currency, to_currency, api_key)

    try:
        response = requests.get(url=url)
    except Exception as error:
        raise HTTPException(status_code=400, detail=error)
    
    data = response.json()
    
    if "Realtime Currency Exchange Rate" not in data:
        raise HTTPException(status_code=400, detail="Currency change is not in response")
    
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    
    return price * exchange_rate
    