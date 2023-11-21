import yfinance as yf
from datetime import datetime, timedelta
from django.http import JsonResponse
import requests

def get_historic_data(request, symbol):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=500)

    df = yf.download(symbol, start=start_date, end=end_date)

    historic_data = []
    for index, row in df.iterrows():
        historic_data.append({
            'time': index.strftime('%Y-%m-%d'),
            'open': round(row['Open'], 2),
            'high': round(row['High'], 2),
            'low': round(row['Low'], 2),
            'close': round(row['Close'], 2),
        })

        print(historic_data)

    return JsonResponse(historic_data, safe=False)



def stockinfo(request,symbol):
   
    api_url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + symbol + '&apikey=TKIE85CZQ40XUZP0'


    try:
        response = requests.get(api_url)
        data = response.json()


        important_metrics = {
            'Symbol': data.get('Symbol', ''),
            'Company Name': data.get('Name', ''),
            'Market Cap': data.get('MarketCapitalization', ''),
            'PE Ratio': data.get('PERatio', ''),
            'Dividend Yield': data.get('DividendYield', ''),
        }
        print(important_metrics)

        return JsonResponse(important_metrics)
    except Exception as e:
        return JsonResponse({'error': str(e)})
