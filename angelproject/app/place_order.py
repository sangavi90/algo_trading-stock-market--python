from .imports import *
# from django.conf import settings
# from angelproject.settings import api_key
from angelproject import settings




class PlaceOrderAPIView(APIView):
    def post(self, request):
        try:
            token = "AFH6577WNNSGC4TGXVLJWHVAQI"
            totp = pyotp.TOTP(token).now()
            # print(totp)
        except Exception as e:
            logger.error("Invalid Token: The provided token is not valid.")
            raise e

        # correlation_id = "abcde"
        data = smartApi.generateSession(username, pwd, totp)
        jwt_token = data['data']['jwtToken']
        # print(jwt_token)
        conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")

        #payload = "{\n \"exchange\": \"NSE\",\n    \"tradingsymbol\": \"INFY-EQ\",\n    \"quantity\": 5,\n    \"disclosedquantity\": 3,\n    \"transactiontype\": \"BUY\",\n    \"ordertype\": \"MARKET\", \n    \"variety\": \"STOPLOSS\",  \n    \"producttype\": \"INTRADAY\"  \n}"
        payload={
                    "variety":"AMO",
                    "tradingsymbol":"ADANIENT28MAR242350PE",
                    "symboltoken":"69954",
                    "transactiontype":"SELL",
                    "exchange":"NFO",
                    "ordertype":"LIMIT",
                    "producttype":"CARRYFORWARD",
                    "duration":"IOC",
                    "price":"2000.50",
                    "squareoff":"0",
                    "stoploss":"250",
                    "quantity":"600",


                    "triggerprice":"0",
                    "expirydate":"28MAR2024",
                    "strikeprice":"2350.000000"
                    }  
        

        headers = {
            'Authorization':jwt_token,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-UserType': 'USER',
            'X-SourceID': 'WEB',
            'X-ClientLocalIP':'192.168.0.101',
            'X-ClientPublicIP':'49.205.147.195',
            'X-MACAddress':'80-38-FB-B9-EE-20',
            'X-PrivateKey':'4dPdQcGs'
        }

        # Convert payload to JSON string
        payload_str = json.dumps(payload)

        conn.request("POST", "/rest/secure/angelbroking/order/v1/placeOrder", payload_str, headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        print(json.loads(data))

        return Response(json.loads(data))

#  /######## multiple leg order placede:
class multiple_legs(APIView):
    def post(self, request):
        try:
            token = "AFH6577WNNSGC4TGXVLJWHVAQI"
            totp = pyotp.TOTP(token).now()
        except Exception as e:
            logger.error("Invalid Token: The provided token is not valid.")
            raise e

        data = smartApi.generateSession(username, pwd, totp)
        jwt_token = data['data']['jwtToken']
        conn = http.client.HTTPSConnection("apiconnect.angelbroking.com")

        # Get orders from the request data
        orders = request.data.get("orders", [])

        response_data = []
        for order in orders:
            try:
                payload = {
                    "variety": order.get("variety"),
                    "tradingsymbol": order.get("tradingsymbol"),
                    "symboltoken": order.get("symboltoken"),
                    "transactiontype": order.get("transactiontype"),
                    "exchange": order.get("exchange"),
                    "ordertype": order.get("ordertype"),
                    "producttype": order.get("producttype"),
                    "duration": order.get("duration"),
                    "price": order.get("price"),
                    "squareoff": order.get("squareoff"),
                    "stoploss": order.get("stoploss"),
                    "quantity": order.get("quantity"),
                    "triggerprice": order.get("triggerprice"),
                    "expirydate": order.get("expirydate"),
                    "strikeprice": order.get("strikeprice")
                }

                payload_str = json.dumps(payload)
                headers = {
                    'Authorization': jwt_token,
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-UserType': 'USER',
                    'X-SourceID': 'WEB',
                    'X-ClientLocalIP': '192.168.0.101',
                    'X-ClientPublicIP': '49.205.147.195',
                    'X-MACAddress': '80-38-FB-B9-EE-20',
                    'X-PrivateKey': '4dPdQcGs'
                }

                conn.request("POST", "/rest/secure/angelbroking/order/v1/placeOrder", payload_str, headers)
                res = conn.getresponse()
                data = res.read().decode("utf-8")
                response_data.append(json.loads(data))
            except Exception as e:
                # Handle exceptions for individual orders if needed
                response_data.append({"error": str(e)})
        
        return Response(response_data)