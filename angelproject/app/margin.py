from . imports import *

class MarginCalculatorAPI(APIView):
    def get(self, request):
        # Fetch data from the URL
        url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Initialize an empty list to store matched data
            matched_data_list = []
            
            # Iterate over each item in the JSON data
            for item in data:
                # Check if the item's 'exch_seg' is 'NFO'
                if item.get('exch_seg') == 'NFO':
                    # Extract the required data
                    matched_data = {
                        'name': item.get('name'),
                        'symbol': item.get('symbol'),
                        'token': item.get('token'),
                        'expiry': item.get('expiry'),
                        'strike': item.get('strike'),
                        'lotsize': item.get('lotsize'),
                        'instrumenttype': item.get('instrumenttype')
                    }
                    matched_data_list.append(matched_data)
            
            # Check if any data was matched
            if matched_data_list:
                return Response(matched_data_list)
            else:
                return Response({"error": "No matching data found for exchange segment 'NFO'"}, status=404)
        else:
            # If there's an error fetching the data
            return Response({"error": "Failed to fetch data from the URL"}, status=response.status_code)



class Companyname_expiry(APIView):
    def get(self, request):
        # Fetch data from the URL
        url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Initialize a dictionary to store expiry dates grouped by company name
            expiry_dates_by_company = {}
            
            # Iterate through the data and group unique expiry dates by company name
            for item in data:
                if item.get('exch_seg') == 'NFO':
                    company_name = item.get('name')
                    expiry_date = item.get('expiry')
                    
                    # If company name already exists in the dictionary, append the expiry date if it's unique
                    if company_name in expiry_dates_by_company:
                        if expiry_date not in expiry_dates_by_company[company_name]:
                            expiry_dates_by_company[company_name].append(expiry_date)
                    # If company name doesn't exist, create a new entry with the expiry date
                    else:
                        expiry_dates_by_company[company_name] = [expiry_date]
            
            # Format the output as required
            formatted_output = [{"name": name, "expiry": expiry_dates_by_company[name]} for name in expiry_dates_by_company]
            
            return Response(formatted_output)
        else:
            # If there's an error fetching the data
            return Response({"error": "Failed to fetch data from the URL"}, status=response.status_code)



# class Option_Data_CEPE(APIView):
  
#     def get(self, request):
#         # Fetch data from the URL
#         url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
            
#             # Initialize a dictionary to store strike prices grouped by company name, expiry date, and option type
#             strike_prices_by_company_expiry = {}
            
#             # Iterate through the data and group strike prices by company name, expiry date, and option type
#             for item in data:
#                 if item.get('exch_seg') == 'NFO':
#                     company_name = item.get('name')
#                     expiry_date = item.get('expiry')
#                     symbol = item.get('symbol')
#                     strike_price = item.get('strike')
                    
#                     # Check if the symbol ends with "CE" or "PE"
#                     if symbol.endswith('CE'):
#                         option_type = 'CE'
#                     elif symbol.endswith('PE'):
#                         option_type = 'PE'
#                     else:
#                         continue  # Skip if symbol doesn't end with "CE" or "PE"
                    
#                     # Create a nested dictionary to store strike prices
#                     strike_prices = strike_prices_by_company_expiry.setdefault(company_name, {}).setdefault(expiry_date, {}).setdefault(option_type, [])
                    
#                     # Append the strike price to the list
#                     strike_prices.append(strike_price)
            
#             # Format the output as required
#             formatted_output = []
#             for name, expiry_data in strike_prices_by_company_expiry.items():
#                 expiry_list = [{"expiry": expiry, "strike": strike_prices} for expiry, strike_prices in expiry_data.items()]
#                 formatted_output.append({"name": name, "expiry": expiry_list})
            
#             return Response(formatted_output)
#         else:
#             # If there's an error fetching the data
#             return Response({"error": "Failed to fetch data from the URL"}, status=response.status_code)



from rest_framework.views import APIView
from rest_framework.response import Response
import requests

# class Option_Data_CEPE(APIView):
#     def get(self, request):
#         # Fetch data from the URL
#         url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
#         response = requests.get(url)
        
#         if response.status_code == 200:
#             data = response.json()
            
#             # Filter data based on exch_seg: NFO
#             filtered_data = [item for item in data if item.get('exch_seg') == 'NFO']
            
#             # Initialize a dictionary to store strike prices grouped by company name, expiry date, and option type
#             strike_prices_by_company_expiry = {}
            
#             # Iterate through the filtered data and group strike prices by company name, expiry date, and option type
#             for item in filtered_data:
#                 company_name = item.get('name')
#                 expiry_date = item.get('expiry')
#                 symbol = item.get('symbol')
#                 token = item.get('token')
#                 strike_price = item.get('strike')
                
#                 # Check if the symbol ends with "CE" or "PE"
#                 if symbol.endswith('CE'):
#                     option_type = 'CE'
#                 elif symbol.endswith('PE'):
#                     option_type = 'PE'
#                 else:
#                     continue  # Skip if symbol doesn't end with "CE" or "PE"
                
#                 # Create a nested dictionary to store strike prices
#                 strike_prices = strike_prices_by_company_expiry.setdefault(company_name, {}).setdefault(expiry_date, {}).setdefault(option_type, [])
                
#                 # Append the strike price along with symbol and token to the list
#                 strike_prices.append({"symbol": symbol, "token": token, "strike": strike_price})
            
#             # Format the output as required
#             formatted_output = []
#             for name, expiry_data in strike_prices_by_company_expiry.items():
#                 expiry_list = [{"expiry": expiry, "strike": strike_prices} for expiry, strike_prices in expiry_data.items()]
#                 company_info = {"name": name, "expiry": expiry_list}
#                 formatted_output.append(company_info)
            
#             return Response(formatted_output)
#         else:
#             # If there's an error fetching the data
#             return Response({"error": "Failed to fetch data from the URL"}, status=response.status_code)

from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class Option_Data_CEPE(APIView):
    def get(self, request):
        # Fetch data from the URL
        url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            # Filter data based on exch_seg: NFO
            filtered_data = [item for item in data if item.get('exch_seg') == 'NFO']
            
            # Initialize a dictionary to store strike prices grouped by company name, expiry date, and option type
            strike_prices_by_company_expiry = {}
            
            # Iterate through the filtered data and group strike prices by company name, expiry date, and option type
            for item in filtered_data:
                company_name = item.get('name')
                expiry_date = item.get('expiry')
                symbol = item.get('symbol')
                token = item.get('token')
                strike_price = item.get('strike')
                lot_size = item.get('lotsize', '')  # Get lotsize if available, otherwise default to empty string
                instrument_type = item.get('instrumenttype', '')  # Get instrumenttype if available, otherwise default to empty string
                
                # Check if the symbol ends with "CE" or "PE"
                if symbol.endswith('CE'):
                    option_type = 'CE'
                elif symbol.endswith('PE'):
                    option_type = 'PE'
                else:
                    continue  # Skip if symbol doesn't end with "CE" or "PE"
                
                # Create a nested dictionary to store strike prices
                expiry_data = strike_prices_by_company_expiry.setdefault(company_name, {}).setdefault(expiry_date, {})
                expiry_data.setdefault(option_type, []).append({"symbol": symbol, "token": token, "strike": strike_price, "lotsize": lot_size, "instrumenttype": instrument_type})
            
            # Format the output as required
            formatted_output = []
            for name, expiry_data in strike_prices_by_company_expiry.items():
                company_info = {"name": name, "expiry": []}
                for expiry, strikes in expiry_data.items():
                    expiry_info = {"expiry": expiry, "strike": strikes}
                    company_info["expiry"].append(expiry_info)
                formatted_output.append(company_info)
            
            return Response(formatted_output)
        else:
            # If there's an error fetching the data
            return Response({"error": "Failed to fetch data from the URL"}, status=response.status_code)
