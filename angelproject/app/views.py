
from .imports import *
from .models import *

from .serializers import *
api_key = '4dPdQcGs'
username = 'S2098754'
pwd = '2024'
smartApi = SmartConnect(api_key)

class get_details(APIView):
    def get(self,request):

        try:
            token = "AFH6577WNNSGC4TGXVLJWHVAQI"
            totp = pyotp.TOTP(token).now()
            print(totp)
        except Exception as e:
            logger.error("Invalid Token: The provided token is not valid.")
            raise e

        # correlation_id = "abcde"
        data = smartApi.generateSession(username, pwd, totp)
        jwt_token = data['data']['jwtToken']
        print(jwt_token)
        return Response(data)   


class get_trade_book(APIView):
    def get(self,request):
        try:
            token = "AFH6577WNNSGC4TGXVLJWHVAQI"
            totp = pyotp.TOTP(token).now()
            print(totp)
        except Exception as e:
            logger.error("Invalid Token: The provided token is not valid.")
            raise e

        # correlation_id = "abcde"
        data = smartApi.generateSession(username, pwd, totp)
        jwt_token = data['data']['jwtToken']

        conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
            
            
        payload = "{\n\"clientcode\":\"S2098754\",\n\"password\":\"2024\"\n,\n\"totp\":\"AFH6577WNNSGC4TGXVLJWHVAQI\"\n}"
        headers = {
        'Authorization': jwt_token,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-UserType': 'USER',
        'X-SourceID': 'WEB',
        'X-ClientLocalIP': ClientLocalIP,
        'X-ClientPublicIP': ClientPublicIP,
        'X-MACAddress': MACAddress,
        'X-PrivateKey': api_key
        }
        conn.request("GET","/rest/secure/angelbroking/order/v1/getTradeBook",payload,headers)
        

        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))

        return Response(data)
    
#  Program get trade book using smart api:
class get_order_book(APIView):
    def get(self,request):
        import http.client

        conn = http.client.HTTPSConnection(
            "apiconnect.angelbroking.com"
            )
        payload = '''{\n 
            \"exchange\": \"NSE\",
            \n    \"tradingsymbol\": \"INFY-EQ\",
            \n    \"quantity\": 5,
            \n    \"disclosedquantity\": 3,
            \n    \"transactiontype\": \"BUY\",
            \n    \"ordertype\": \"MARKET\",
            \n    \"variety\": \"STOPLOSS\",
            \n    \"producttype\": \"INTRADAY\"
            \n}'''
        headers = {
        'Authorization': 'Bearer AUTHORIZATION_TOKEN',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-UserType': 'USER',
        'X-SourceID': 'WEB',
        'X-ClientLocalIP': ClientLocalIP,
        'X-ClientPublicIP': ClientPublicIP,
        'X-MACAddress': 'MAC_ADDRESS',
        'X-PrivateKey': 'API_KEY'
        }
        conn.request("POST", "/rest/secure/angelbroking/order/v1/placeOrder", 
        payload, 
        headers)
        res = conn.getresponse()
        data = res.read()
        print(data.decode("utf-8"))


#  Get the real time data by using Smart Api code:
 
class real_time_data(APIView):
    def get(self,request):

        # conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
        # payload = {
        #     "mode": "FULL",
        #     "exchangeTokens": {
        #         "NSE": ["3045"]
        #     }

            
        # }

        
        # payload_json = json.dumps(payload)
        # headers = {
        # 'X-PrivateKey': api_key,
        # 'Accept': 'application/json',
        # 'X-SourceID': 'WEB',
        # 'X-ClientLocalIP': ClientLocalIP,
        # 'X-ClientPublicIP': ClientPublicIP,
        # 'X-MACAddress': MACAddress,
        # 'X-UserType': 'USER',
        # 'Authorization': jwt_token,
        # 'Accept': 'application/json',
        # 'X-SourceID': 'WEB',
        # 'Content-Type': 'application/json'
        # }
        # conn.request("POST", "rest/secure/angelbroking/market/v1/quote/", payload_json, headers)
        # res = conn.getresponse()
        # data = res.read()
        # print(data.decode("utf-8"))
        # conn.close()



        api_url = 'https://apiconnect.angelbroking.com/rest/secure/angelbroking/market/v1/quote/'

        # Define your API key and other necessary headers
        headers = {
            'X-PrivateKey': api_key,
            'Authorization': jwt_token,
            'Content-Type': 'application/json'
        }

        # Define the payload (optional)
        payload = {
            "mode": "FULL",
            "exchangeTokens": {
                 "NSE": ["3045"]
        }

        
        }

        # Make a POST request to the API endpoint
        response = requests.post(api_url, json=payload, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract and process the real-time market data from the response
            market_data = response.json()
            print(market_data)
        else:
            # Print an error message if the request failed
            print("Failed to retrieve real-time market data. Status code:", response.status_code)

        return Response(market_data)



#  Based on NIFTY and Expiry-date it shows all the details of CE and PE: 

class NSE_real_time_data(APIView):
    def get(self,request):
        url='https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        response=requests.get(url,headers=headers)
        print(response)


        response_text=response.text
        print(response_text)
        json_object=json.loads(response_text)
        # print(type(json_object))
        
        return Response(json_object)
        
#  it display only Strike_price of CE,PE:
    
class NSE_option_chain_data_check(APIView):
    def get(self,request,symbol):
        url='https://www.nseindia.com/api/option-chain-equities?symbol={}'.format(symbol)
        print(url)
        print("jhvjgfjgjg=",symbol)
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
        response=requests.get(url,headers=headers)
        


        response_text=response.text
        # print(response_text)
        json_object=json.loads(response_text)
        # print(json_object)
        ce_strike_prices = []
        pe_strike_prices = []
        
        for data in json_object['records']['data']:
            if 'CE' in data:
                ce_strike_prices.append(data['CE']['strikePrice'])
            if 'PE' in data:
                pe_strike_prices.append(data['PE']['strikePrice'])
        
        data= {
            'CE': ce_strike_prices,
            'PE': pe_strike_prices
        }
    
        return Response(data)
 
# it display all the company name only ,which are all take it from OI_Spruts:

class NSE_company_name(APIView):
     def get(self,request):
         companies = company_name.objects.all()
         
        
        #  serializer = CompanyNameSerializer(com_name, many=True)
         data=[i.company_name for i in companies]
        
         return Response(data)
     

# It stores all the company name into database:

class NSE_option_chain_data(APIView):
    def get(self, request):
        companies = company_name.objects.all()
        i = 0
        for company in companies:
            symbol = company.company_name
            url = 'https://www.nseindia.com/api/option-chain-equities?symbol={}'.format(symbol)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                json_object = response.json()

                ce_strike_prices = []
                pe_strike_prices = []

                for data in json_object['records']['data']:
                    if 'CE' in data:
                        ce_strike_prices.append(data['CE']['strikePrice'])
                    if 'PE' in data:
                        pe_strike_prices.append(data['PE']['strikePrice'])

                # Check if options entry already exists for the company
                existing_options = options.objects.filter(company_name=company)
                if existing_options.exists():
                    print(company.company_name, "already exists")
                    continue

                # Create or update options instance
                options.objects.create(
                    company_name=company,
                    ce=ce_strike_prices,
                    pe=pe_strike_prices
                )
                i += 1
                print(company.company_name, " ", i)
            else:
                print(company.company_name, " not appended ")
        c = options.objects.all().count()
        print("total companies = ", c)
        return JsonResponse({'message': 'Data saved successfully'})
    

#  Based on company name it display Strike_price of CE and PE:

import ast
class OptionsData(APIView):
    def get(self, request, symbol):
        try:
            # Retrieve options data for the provided company name
            company = company_name.objects.get(company_name=symbol)
            options_data = options.objects.get(company_name=company)

            # Serialize the CE and PE values
            serializer = OptionsSerializer(options_data)
            ce_list = ast.literal_eval(serializer.data['ce'])
            pe_list = ast.literal_eval(serializer.data['pe'])
            data={
                'company_name':symbol,
                'ce':ce_list,
                'pe':pe_list
            }
            return Response(data)
        except company_name.DoesNotExist:
            return Response({'error': 'Company not found'}, status=404)
        except options.DoesNotExist:
            return Response({'error': 'Options data not found for the company'}, status=404)    
        
class Order_placing(APIView):
    def get(self, request):
        try:
            # Generate TOTP
            token = "AFH6577WNNSGC4TGXVLJWHVAQI"
            totp = pyotp.TOTP(token).now()

            # Generate session
            data = smartApi.generateSession(username, pwd, totp)
            jwt_token = data['data']['jwtToken']

            # Prepare payload for placing order
            payload = {
                "exchange": "NSE",
                "tradingsymbol": "INFY-EQ",
                "quantity": 5,
                "disclosedquantity": 3,
                "transactiontype": "BUY",
                "ordertype": "MARKET",
                "variety": "STOPLOSS",
                "producttype": "INTRADAY"
            }

            # Make request to place order
            headers = {
                'Authorization': jwt_token,
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-UserType': 'USER',
                'X-SourceID': 'WEB',
                'X-ClientLocalIP': ClientLocalIP,
                'X-ClientPublicIP': ClientPublicIP,
                'X-MACAddress': MACAddress,
                'X-PrivateKey': api_key
            }
            conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")
            conn.request("POST", "/rest/secure/angelbroking/order/v1/placeOrder", json.dumps(payload), headers)
            res = conn.getresponse()
            data = res.read().decode("utf-8")

            # Close connection
            conn.close()

            return Response(data)
        except Exception as e:
            logger.error("Error placing order: {}".format(str(e)))
            return Response("Error placing order: {}".format(str(e)), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# class ExpiryStrikePrice (APIView):
#     def get(self,request,symbol):
#         companies = company_name.objects.all()
#         for company in companies:
#             symbol = company.company_name
#             url='https://www.nseindia.com/api/option-chain-equities?symbol={}'.format(symbol)
#             print(url)
#             print("jhvjgfjgjg=",symbol)
#             headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
#             # print("the headers is ",headers)
#             response=requests.get(url,headers=headers)
#             print("the response is ",response)
#             response_text=response.text
#             # print(response_text)
#             json_object=json.loads(response_text)
#             # print(json)      
#             ce_options = []
#             pe_options = []
            
#             for data in json_object['records']['data']:
#                 if 'CE' in data:
#                     ce_option = {
#                         'expiry_date': data['expiryDate'],
#                         'strike_price': data['CE']['strikePrice']
#                     }
#                     ce_options.append(ce_option)
#                 if 'PE' in data:
#                     pe_option = {
#                         'expiry_date': data['expiryDate'],
#                         'strike_price': data['PE']['strikePrice']
#                     }
#                     pe_options.append(pe_option)
            
#             data= {
#                 'CE': ce_options,
#                 'PE': pe_options
#             }
#             existing_options = expirystrikeprice.objects.filter(company_name=company)
#             if existing_options.exists():
#                     print(company.company_name, "already exists")
#                     continue

#             expirystrikeprice.objects.create(
#                     company_name=company,
#                     ce= ce_options,
#                     pe=pe_options)
            
        
#             # print(data)
#             print(len(data))
#             return Response(data)
        


# Based on CE and PE it display all the collection of Expiry_date,Strike_Price:

class ExpiryStrikePrice(APIView):
    def get(self, request, symbol):
        companies = company_name.objects.all()
        error_companies = []

        for company in companies:
            symbol = company.company_name
            url = 'https://www.nseindia.com/api/option-chain-equities?symbol={}'.format(symbol)
            print(url)
            print("Company:", symbol)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
            
            try:
                response = requests.get(url, headers=headers)
                response.raise_for_status()  # Raise an exception for bad responses (e.g., 404, 500)
                json_object = response.json()

                ce_options = []
                pe_options = []

                for data in json_object['records']['data']:
                    if 'CE' in data:
                        ce_option = {
                            'expiry_date': data['expiryDate'],
                            'strike_price': data['CE']['strikePrice']
                        }
                        ce_options.append(ce_option)
                    if 'PE' in data:
                        pe_option = {
                            'expiry_date': data['expiryDate'],
                            'strike_price': data['PE']['strikePrice']
                        }
                        pe_options.append(pe_option)

                data = {
                    'CE': ce_options,
                    'PE': pe_options
                }

                existing_options = expirystrikeprice.objects.filter(company_name=company)
                if existing_options.exists():
                    print(company.company_name, "already exists")
                    continue

                expirystrikeprice.objects.create(
                    company_name=company,
                    ce=ce_options,
                    pe=pe_options)

                print(len(data))
                return Response(data)

            except (requests.RequestException, json.JSONDecodeError) as e:
                print(f"Error processing {symbol}: {e}")
                error_companies.append(symbol)
                print(error_companies) 
                print(len(error_companies))
                continue
        
        return Response({"error_companies": error_companies})



 # Based on company name it shows collection of Expiry-date and Strike price of CE and PE: 
    
import ast
class ExpiryStrikeData(APIView):      # this API for display expiry date , strike_price with their  company_name.
    def get(self, request, symbol):
        try:
            # Retrieve options data for the provided company name
            company = company_name.objects.get(company_name=symbol)
            options_data =expirystrikeprice.objects.get(company_name=company)

            # Serialize the CE and PE values
            serializer =ExpiryPriceSerializer(options_data)
            ce_list = ast.literal_eval(serializer.data['ce'])
            pe_list = ast.literal_eval(serializer.data['pe'])
            data={
                'company_name':symbol,
                'ce':ce_list,
                'pe':pe_list
            }
            return Response(data)
        except company_name.DoesNotExist:
            return Response({'error': 'Company not found'}, status=404)
        except expirystrikeprice.DoesNotExist:
            return Response({'error': 'Options data not found for the company'}, status=404)   


#  based on Expiry-date it shows collecction of Stike_price of CE and PE:

class based_on_expiry_date(APIView): 
    def get(self, request, symbol):
        try:
            url = f'https://www.nseindia.com/api/option-chain-equities?symbol={symbol}'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
            }

            response = requests.get(url, headers=headers)
            response_json = response.json()

            ce_options = {}
            pe_options = {}

            for data in response_json['records']['data']:
                expiry_date = data['expiryDate']

                # CE (Call Option) strike price
                if 'CE' in data:
                    ce_strike_price = data['CE']['strikePrice']
                    if expiry_date not in ce_options:
                        ce_options[expiry_date] = []
                    ce_options[expiry_date].append(ce_strike_price)

                # PE (Put Option) strike price
                if 'PE' in data:
                    pe_strike_price = data['PE']['strikePrice']
                    if expiry_date not in pe_options:
                        pe_options[expiry_date] = []
                    pe_options[expiry_date].append(pe_strike_price)

            result = {
                'CE': ce_options,
                'PE': pe_options
            }

            return Response(result)
        
        except Exception as e:
            return Response({'error': str(e)})


import requests
from rest_framework.response import Response
from rest_framework.views import APIView

class Tradingsymbol_token(APIView):
    def get(self, request):
        # Fetch data from the URL
        url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Filter data for symbols ending with "-EQ", exch_seg="NSE", and specific names
            filtered_data = [item for item in data if item.get('exch_seg', '') == "NSE"  if item.get('symbol', '').endswith("-EQ") 
                             or item.get('name', '') in ["NIFTY", "FINNIFTY", "BANKNIFTY", "MIDCPNIFTY"]]
            
            if filtered_data:
                # Extract name, trading_symbol, and token for filtered data
                extracted_data = [{'name': item['name'], 'trading_symbol': item['symbol'], 'token': item['token']} for item in filtered_data]
                print("djfbhdfdkfdfd=",len(extracted_data))
                j=0
                for i in extracted_data:
                    j+=1
                    if i['name']=="NIFTY"or i['name']=="FINNIFTY" or i['name']=="BANKNIFTY" or i['name']=="MIDCPNIFTY" :
                        print("yes",i['name'],"   ",i['trading_symbol'],"   ",i['token'])
                        
                        
                print("count of al companies are =",j)
                return Response(extracted_data)
                
            else:
                return Response({"error": "No symbols found ending with '-EQ' for exch_seg='NSE' and specified names"}, status=404)
        else:
            # If there's an error fetching the data
            return Response({"error": "Failed to fetch data from the URL"}, status=response.status_code)
    


        


import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import company_name# Import your CompanyName model

class NSE_Tradingsymbol_token(APIView):
    def get(self, request):
        # Fetch data from the URL
        url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        response = requests.get(url)
        
        if response.status_code == 200:
            # Get company names from the model
            company_names = company_name.objects.values_list('company_name', flat=True)
            
            data = response.json()
            
            # Initialize an empty list to store matched data
            matched_data_list = []
            
            # Iterate over each item in the JSON data
            for item in data:
                # Check if the company name from the model matches the 'name' attribute in the JSON data
                if item.get('name', '') in company_names and item.get('symbol', '').endswith("-EQ"):
                    # If there's a match, extract the required data
                    matched_data = {
                        'name': item['name'],
                        'symbol': item['symbol'],
                        'token': item['token']
                    }
                    matched_data_list.append(matched_data)
            
            # Check if any data was matched
            if matched_data_list:
                return Response(matched_data_list)
            else:
                return Response({"error": "No matching data found"}, status=404)
        else:
            # If there's an error fetching the data
            return Response({"error": "Failed to fetch data from the URL"}, status=response.status_code)
        


        

# class ExpiryStrikePrice (APIView):
#     def get(self,request,symbol):
#         try:

#             url='https://www.nseindia.com/api/option-chain-equities?symbol={}'.format(symbol)
#             # url='https://www.nseindia.com/api/option-chain-equities?symbol=BEL'
#             print(url)
#             print("jhvjgfjgjg=",symbol)
#             headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
#             print("the headers is ",headers)
#             try:

#                 response=requests.get(url,headers=headers)
#             except Exception as e:
#                 print(e)

#             print("the response is ",response)
#             response_text=response.text
#             print(response_text)
#             json_object=json.loads(response_text)
#             print(json_object)      
#             ce_options = []
#             pe_options = []
            
#             for data in json_object['records']['data']:
#                 if 'CE' in data:
#                     ce_option = {
#                         'expiry_date': data['expiryDate'],
#                         'strike_price': data['CE']['strikePrice']
#                     }
#                     ce_options.append(ce_option)
#                 if 'PE' in data:
#                     pe_option = {
#                         'expiry_date': data['expiryDate'],
#                         'strike_price': data['PE']['strikePrice']
#                     }
#                     pe_options.append(pe_option)
            
#             data= {
#                 'CE': ce_options,
#                 'PE': pe_options
#             }
            
        
#             print(data)
#             print(type(data))
#             return Response(data)
        
#         except Exception as e:
#             print(e)
#             return Response(e)

# class NSE_company_name(APIView):
#     def get(self,request):
#         url='https://www.nseindia.com/api/live-analysis-oi-spurts-underlyings'
#         headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
#         response=requests.get(url,headers=headers)
        


        

#         print("Response status code:", response.status_code)

#         # Check the response content
#         print("Response content:", response.text)

#         try:
#             response_text=response.text
#             json_object=json.loads(response_text)
#         except json.decoder.JSONDecodeError as e:
#             print("Error decoding JSON:", e)
#             return Response({"error": "Error decoding JSON"}, status=500)
        
#         symbols = [entry['symbol'] for entry in json_object['data']]

#         for symbol in symbols:
#             company = company_name.objects.create(company_name=symbol)
#             company.save()

#         print(len(symbols))
#         print("Symbols extracted from the API:", symbols)
#         return Response(symbols)
    


                