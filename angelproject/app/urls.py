from django.contrib import admin
from django.urls import path
from.import views,place_order,get_trade,history,margin
from .place_order import *
from . get_trade import *
from .margin import *

urlpatterns = [
    path('viewdetails/',views.get_details.as_view(),name="viewdeatils"),
    path('gettradebook/',views.get_trade_book.as_view(),name='gettradebook'),
    path('get_real_time_data/',views.real_time_data.as_view(),name='real_time_data'),
    path('NSE_real_time_data/',views.NSE_real_time_data.as_view(),name='NSE_real_time_data'),
    path('NSE_option_chain_data_check/<str:symbol>/',views.NSE_option_chain_data_check.as_view(),name='NSE_option_chain_data_check'),
    path('NSE_option_chain_data/',views.NSE_option_chain_data.as_view(),name='NSE_option_chain_data'),
    path('NSE_company_name/',views.NSE_company_name.as_view(),name='NSE_company_name'),
    path('OptionsData/<str:symbol>/',views.OptionsData.as_view(),name='OptionsData'),
    path('Order_placing/',views.Order_placing.as_view(),name='Order_placing'),
    path('ExpiryStrikePrice/<str:symbol>/',views.ExpiryStrikePrice.as_view(),name="ExpiryStrikePrice"),
    path('ExpiryStrikeData/<str:symbol>/',views.ExpiryStrikeData.as_view(),name='ExpiryStrikeData'),
    path('OrderPlacementAPIView/',place_order.PlaceOrderAPIView.as_view(),name='OrderPlacementAPIView'),
    path('based_on_expiry_date/<str:symbol>/',views. based_on_expiry_date.as_view(),name=' based_on_expiry_date'),
    path('GetTradeBookAPIView/',get_trade.GetTradeBookAPIView.as_view(),name='GetTradeBookAPIView'),
    path('Tradingsymbol_token/',views.Tradingsymbol_token.as_view(),name=" Tradingsymbol_token"),
    path('NSE_Tradingsymbol_token/',views.NSE_Tradingsymbol_token.as_view(),name='NSE_Tradingsymbol_token'),
    path('Historical_data/',history.Historical_data.as_view(),name="Historical_data"),
    path('MarginCalculatorAPI/',margin.MarginCalculatorAPI.as_view(),name="MarginCalculatorAPI"),
    path('Companyname_expiry/',margin.Companyname_expiry.as_view(),name="Companyname_expiry"),
    path("Option_Data_CEPE/",margin.Option_Data_CEPE.as_view(),name="Option_Data_CEPE"),
    path("multiple_legs/",place_order.multiple_legs.as_view(),name="multiple_legs"),
]
