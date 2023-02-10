<a name="__pageTop"></a>
# openapi_client.apis.tags.polygon_api.PolygonApi

All URIs are relative to *https://api.prod.gallop.run/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pol_collection_forecasts**](#get_pol_collection_forecasts) | **post** /insights/pol/getCollectionForecasts | Price Forecast by Collection
[**get_pol_collection_owners**](#get_pol_collection_owners) | **post** /data/pol/getCollectionOwners | Wallet Owners by Collection
[**get_pol_collection_price_diff**](#get_pol_collection_price_diff) | **post** /analytics/pol/getCollectionPriceDiff | Price Differentiation by Trait
[**get_pol_collection_sales_ohlc**](#get_pol_collection_sales_ohlc) | **post** /analytics/pol/getCollectionSalesOHLC | Collection Sales Price Candlesticks
[**get_pol_collection_summary**](#get_pol_collection_summary) | **post** /analytics/pol/getCollectionSummary | Summary Statistics by Collection
[**get_pol_collection_traits**](#get_pol_collection_traits) | **post** /data/pol/getCollectionTraits | Traits by Collection
[**get_pol_collection_transactions**](#get_pol_collection_transactions) | **post** /data/pol/getCollectionTransactions | Transactions by Collection
[**get_pol_collections**](#get_pol_collections) | **post** /data/pol/getCollections | Aggregated Collections Supported by Gallop
[**get_pol_custom_collection_risk**](#get_pol_custom_collection_risk) | **post** /insights/pol/getCustomCollectionRisk | Custom Volatility &amp; Risk Metrics by Collection
[**get_pol_custom_token_risk**](#get_pol_custom_token_risk) | **post** /insights/pol/getCustomTokenRisk | Custom Volatility &amp; Risk Metrics by Token
[**get_pol_default_collection_risk**](#get_pol_default_collection_risk) | **post** /insights/pol/getDefaultCollectionRisk | Default Volatility &amp; Risk Metrics by Collection
[**get_pol_default_token_risk**](#get_pol_default_token_risk) | **post** /insights/pol/getDefaultTokenRisk | Default Volatility &amp; Risk Metrics by Token
[**get_pol_historical_transactions**](#get_pol_historical_transactions) | **post** /data/pol/getHistoricalTransactions | Historical Transactions by Collection
[**get_pol_leader_board**](#get_pol_leader_board) | **post** /analytics/pol/getLeaderBoard | Polygon Leaderboard by Collection
[**get_pol_marketplace_data**](#get_pol_marketplace_data) | **post** /data/pol/getMarketplaceData | Collection Summary by Marketplace
[**get_pol_marketplace_floor_price**](#get_pol_marketplace_floor_price) | **post** /data/pol/getMarketplaceFloorPrice | Marketplace Floor Price by Collection
[**get_pol_rarity**](#get_pol_rarity) | **post** /analytics/pol/getRarity | Token Rarity by Collection
[**get_pol_token_appraisal**](#get_pol_token_appraisal) | **post** /insights/pol/getTokenAppraisal | Liquidation &amp; Appraisal Estimate by Token
[**get_pol_token_forecasts**](#get_pol_token_forecasts) | **post** /insights/pol/getTokenForecasts | Price Forecast by Token
[**get_pol_token_summary**](#get_pol_token_summary) | **post** /analytics/pol/getTokenSummary | Summary Statistics by Token
[**get_pol_token_transactions**](#get_pol_token_transactions) | **post** /data/pol/getTokenTransactions | Transactions by Token
[**get_pol_tokens**](#get_pol_tokens) | **post** /data/pol/getTokens | Tokens by Collection
[**get_pol_wallet_labels**](#get_pol_wallet_labels) | **post** /insights/pol/getWalletLabels | Wallet Activity Labels
[**get_pol_wallet_nfts**](#get_pol_wallet_nfts) | **post** /data/pol/getWalletNFTs | Tokens Owned by Wallet
[**get_pol_wallet_transactions**](#get_pol_wallet_transactions) | **post** /data/pol/getWalletTransactions | Historical Token Transactions by Wallet
[**get_pol_wash_trade**](#get_pol_wash_trade) | **post** /analytics/pol/getWashTrade | Wash Trades by Transaction
[**get_pol_wash_transactions**](#get_pol_wash_transactions) | **post** /analytics/pol/getWashTransactions | Wash Trades by Collection

# **get_pol_collection_forecasts**
<a name="get_pol_collection_forecasts"></a>
> get_pol_collection_forecasts()

Price Forecast by Collection

Returns price, return, and volatility forecast for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        percentiles=[
            33
        ],
        voltype="har",
        horizon=5,
        frequency="1D",
        dist="norm",
        start_date="2021-01-01",
        end_date="2022-02-25",
        return_price_forecasts=True,
        alpha=0.05,
        rept_curr="eth",
        exclude_wash=True,
        arch_params=dict(
            mean="mean_example",
            lags=1,
            vol="vol_example",
            p=1,
            dist="norm",
        ),
    )
    try:
        # Price Forecast by Collection
        api_response = api_instance.get_pol_collection_forecasts(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_collection_forecasts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**[percentiles](#percentiles)** | list, tuple,  | tuple,  | The collection percentile(s) | [optional] 
**voltype** | str,  | str,  | Type of statistical forecasting model to be calculated as a 3-char string, e.g. &#x60;arc&#x60; for ARCH | [optional] must be one of ["arc", "gar", "har", ] 
**horizon** | decimal.Decimal, int,  | decimal.Decimal,  | The forecast horizon (i.e. the number of periods to forecast out) | [optional] 
**frequency** | str,  | str,  | The interval at which to calculate returns to base the forecasts upon, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**dist** | str,  | str,  | The distribution assumed to calculate parametric risk for. | [optional] must be one of ["norm", "t", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**return_price_forecasts** | bool,  | BoolClass,  | Set to true, returns confidencve intervals at alpha significance for price on top of forecasts for returns and volatilities | [optional] 
**alpha** | decimal.Decimal, int, float,  | decimal.Decimal,  | The significance level, e.g. 0.05 for 95% confidence | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**[arch_params](#arch_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH family model. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# percentiles

The collection percentile(s)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The collection percentile(s) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# arch_params

JSON containing options for the ARCH family model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH family model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... .  | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**p** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the symmetric innovation(s). | [optional] 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_collection_forecasts.ApiResponseFor200) | An object containing a set of forecasts for a (set of) collection percentile(s).
400 | [ApiResponseFor400](#get_pol_collection_forecasts.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_collection_forecasts.ApiResponseFor403) | Unauthorized

#### get_pol_collection_forecasts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_collection_forecasts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_collection_forecasts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_collection_owners**
<a name="get_pol_collection_owners"></a>
> get_pol_collection_owners()

Wallet Owners by Collection

Returns all wallet owners for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0x78306a498516d75a76beeacea04fe772d20fe41b",
        page=1,
        page_size=100,
    )
    try:
        # Wallet Owners by Collection
        api_response = api_instance.get_pol_collection_owners(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_collection_owners: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the collection. | 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_collection_owners.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_collection_owners.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_collection_owners.ApiResponseFor403) | Unauthorized

#### get_pol_collection_owners.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_collection_owners.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_collection_owners.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_collection_price_diff**
<a name="get_pol_collection_price_diff"></a>
> get_pol_collection_price_diff()

Price Differentiation by Trait

Returns how trait differentiates price for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xad59ecb77033391e847cc96829b08beb83151088",
        start_date="2021-08-01",
        end_date="2022-03-04",
        exclude_wash=True,
    )
    try:
        # Price Differentiation by Trait
        api_response = api_instance.get_pol_collection_price_diff(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_collection_price_diff: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The Polygon contract address to identify the collection. | 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_collection_price_diff.ApiResponseFor200) | An object containing the collection&#x27;s price differentiation
400 | [ApiResponseFor400](#get_pol_collection_price_diff.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_collection_price_diff.ApiResponseFor403) | Unauthorized

#### get_pol_collection_price_diff.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_collection_price_diff.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_collection_price_diff.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_collection_sales_ohlc**
<a name="get_pol_collection_sales_ohlc"></a>
> get_pol_collection_sales_ohlc()

Collection Sales Price Candlesticks

Returns collection sales price open, high, low, close and volume at a selected time interval

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        frequency="1D",
        group_by="Hat",
        volume=False,
        n_trades=False,
        rept_curr="eth",
        start_date="2021-08-01",
        end_date="2022-03-04",
        exclude_wash=True,
    )
    try:
        # Collection Sales Price Candlesticks
        api_response = api_instance.get_pol_collection_sales_ohlc(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_collection_sales_ohlc: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The Polygon contract address to identify the collection. | 
**frequency** | str,  | str,  | The interval at which to return OHLC, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**group_by** | str,  | str,  | An attribute of the NFT to group results by. | [optional] 
**volume** | bool,  | BoolClass,  | If &#x27;true&#x27;, response dicts contain OHLCV | [optional] 
**n_trades** | bool,  | BoolClass,  | If &#x27;true&#x27;, append number of trades to OHLC(V) | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_collection_sales_ohlc.ApiResponseFor200) | An object containing the collection sales OHLC prices
400 | [ApiResponseFor400](#get_pol_collection_sales_ohlc.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_collection_sales_ohlc.ApiResponseFor403) | Unauthorized

#### get_pol_collection_sales_ohlc.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_collection_sales_ohlc.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_collection_sales_ohlc.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_collection_summary**
<a name="get_pol_collection_summary"></a>
> get_pol_collection_summary()

Summary Statistics by Collection

Returns summary analytics for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        group_by="Fur",
        start_date="2021-01-01",
        end_date="2022-02-25",
        rept_curr="eth",
        exclude_wash=True,
    )
    try:
        # Summary Statistics by Collection
        api_response = api_instance.get_pol_collection_summary(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_collection_summary: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the collection. | 
**group_by** | str,  | str,  | An attribute of the NFT. | [optional] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_collection_summary.ApiResponseFor200) | An object containing the collection&#x27;s analytical summary.
400 | [ApiResponseFor400](#get_pol_collection_summary.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_collection_summary.ApiResponseFor403) | Unauthorized

#### get_pol_collection_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_collection_summary.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_collection_summary.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_collection_traits**
<a name="get_pol_collection_traits"></a>
> get_pol_collection_traits()

Traits by Collection

Returns a list of traits for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0x67f4732266c7300cca593c814d46bee72e40659f",
    )
    try:
        # Traits by Collection
        api_response = api_instance.get_pol_collection_traits(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_collection_traits: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the collection. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_collection_traits.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_collection_traits.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_collection_traits.ApiResponseFor403) | Unauthorized

#### get_pol_collection_traits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_collection_traits.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_collection_traits.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_collection_transactions**
<a name="get_pol_collection_transactions"></a>
> get_pol_collection_transactions()

Transactions by Collection

Returns all transactions for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0x0833566d5c6926ba123f6587fb16ff4aa8d7680b",
        page=1,
        page_size=100,
        start_block_number=100,
        start_date="2021-01-01",
        end_date="2022-02-25",
    )
    try:
        # Transactions by Collection
        api_response = api_instance.get_pol_collection_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_collection_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the collection. | 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**start_block_number** | decimal.Decimal, int,  | decimal.Decimal,  | The oldest block number to return. | [optional] 
**start_date** | str,  | str,  | The earliest block timestamp. | [optional] 
**end_date** | str,  | str,  | The latest block timestamp. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_collection_transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_collection_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_collection_transactions.ApiResponseFor403) | Unauthorized

#### get_pol_collection_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_collection_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_collection_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_collections**
<a name="get_pol_collections"></a>
> get_pol_collections()

Aggregated Collections Supported by Gallop

Returns all Gallop aggregated collections

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        page=1,
        page_size=100,
        collection_name="punks",
        traded=True,
        created_after="2023-01-15",
        sort_by="created_at",
    )
    try:
        # Aggregated Collections Supported by Gallop
        api_response = api_instance.get_pol_collections(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_collections: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**collection_name** | str,  | str,  | The name of the collection searched. | [optional] 
**traded** | bool,  | BoolClass,  | Only return collections that have traded. | [optional] 
**created_after** | str,  | str,  | Only return collections recorded after this day [YYYY-MM-DD] | [optional] 
**sort_by** | str,  | str,  | The value to sort by. Defaults to created_at | [optional] must be one of ["created_at", "collection_name", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_collections.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_collections.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_collections.ApiResponseFor403) | Unauthorized

#### get_pol_collections.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_collections.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_collections.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_custom_collection_risk**
<a name="get_pol_custom_collection_risk"></a>
> get_pol_custom_collection_risk()

Custom Volatility & Risk Metrics by Collection

Returns summary of customizable volatility and risk metrics for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        holding_period="6M",
        percentiles=[
            33
        ],
        amount=1,
        dist="norm",
        start_date="2021-01-01",
        end_date="2022-02-25",
        risk_free_rate=0.001,
        wins_outliers=True,
        frequency="1D",
        rept_curr="eth",
        exclude_wash=True,
        drawdown=False,
        arc_params=dict(
            mean="mean_example",
            lags=1,
            vol="vol_example",
            p=1,
            dist="norm",
        ),
        gar_params=dict(
            mean="mean_example",
            lags=1,
            vol="vol_example",
            p=1,
            dist="norm",
        ),
        har_params=dict(
            mean="mean_example",
            lags=1,
            vol="vol_example",
            p=[
                1
            ],
            q=1,
            dist="norm",
        ),
    )
    try:
        # Custom Volatility & Risk Metrics by Collection
        api_response = api_instance.get_pol_custom_collection_risk(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_custom_collection_risk: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**holding_period** | str,  | str,  | The holding period to evaluate risk for, e.g. &#x60;12M&#x60; | 
**[percentiles](#percentiles)** | list, tuple,  | tuple,  | The collection percentile(s) | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of tokens in your portfolio | [optional] 
**dist** | str,  | str,  | The distribution assumed to calculate parametric risk for | [optional] must be one of ["norm", "t", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**risk_free_rate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The rate of return for an asset deemed risk free in the contemplated holding period | [optional] 
**wins_outliers** | bool,  | BoolClass,  | Whether to winsorize time series outliers prior to calculating risk | [optional] 
**frequency** | str,  | str,  | The interval at which to calculate returns to base the forecasts upon, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**drawdown** | bool,  | BoolClass,  | If true, report drawdown volatility (based on negative returns only). | [optional] 
**[arc_params](#arc_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH model. | [optional] 
**[gar_params](#gar_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the GARCH model. | [optional] 
**[har_params](#har_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the HARCH model. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# percentiles

The collection percentile(s)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The collection percentile(s) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# arc_params

JSON containing options for the ARCH model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... . | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**p** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the symmetric innovation(s). | [optional] 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# gar_params

JSON containing options for the GARCH model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the GARCH model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... . | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**p** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the symmetric innovation(s). | [optional] 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# har_params

JSON containing options for the HARCH model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the HARCH model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... . | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**[p](#p)** | list, tuple,  | tuple,  | Order of the symmetric innovation(s). | [optional] 
**q** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the lagged (transformed) conditional variance. | [optional] 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# p

Order of the symmetric innovation(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Order of the symmetric innovation(s). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_custom_collection_risk.ApiResponseFor200) | An object containing a summary of volatility and risk metrics for a (set of) collection percentile(s).
400 | [ApiResponseFor400](#get_pol_custom_collection_risk.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_custom_collection_risk.ApiResponseFor403) | Unauthorized

#### get_pol_custom_collection_risk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_custom_collection_risk.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_custom_collection_risk.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_custom_token_risk**
<a name="get_pol_custom_token_risk"></a>
> get_pol_custom_token_risk()

Custom Volatility & Risk Metrics by Token

Returns summary of customizable volatility and risk metrics for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        token_id=[
            "303"
        ],
        holding_period="6M",
        dist="norm",
        start_date="2021-08-01",
        end_date="2022-02-04",
        risk_free_rate=0.001,
        wins_outliers=True,
        frequency="1D",
        rept_curr="sol",
        exclude_wash=True,
        drawdown=False,
        arc_params=dict(
            mean="mean_example",
            lags=1,
            vol="vol_example",
            p=1,
            dist="norm",
        ),
        gar_params=dict(
            mean="mean_example",
            lags=1,
            vol="vol_example",
            p=1,
            dist="norm",
        ),
        har_params=dict(
            mean="mean_example",
            lags=1,
            vol="vol_example",
            p=[
                1
            ],
            q=1,
            dist="norm",
        ),
    )
    try:
        # Custom Volatility & Risk Metrics by Token
        api_response = api_instance.get_pol_custom_token_risk(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_custom_token_risk: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[token_id](#token_id)** | list, tuple,  | tuple,  | The id(s) for the token(s). | 
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**holding_period** | str,  | str,  | The holding period to evaluate risk for, e.g. &#x60;12M&#x60; | 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**risk_free_rate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The rate of return for an asset deemed risk free in the contemplated holding period | [optional] 
**wins_outliers** | bool,  | BoolClass,  | Whether to winsorize time series outliers prior to calculating risk | [optional] 
**frequency** | str,  | str,  | The interval at which to calculate returns to base the forecasts upon, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**drawdown** | bool,  | BoolClass,  | If true, report drawdown volatility (based on negative returns only). | [optional] 
**[arc_params](#arc_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH model. | [optional] 
**[gar_params](#gar_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the GARCH model. | [optional] 
**[har_params](#har_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the HARCH model. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# token_id

The id(s) for the token(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The id(s) for the token(s). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# arc_params

JSON containing options for the ARCH model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... . | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**p** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the symmetric innovation(s). | [optional] 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# gar_params

JSON containing options for the GARCH model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the GARCH model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... . | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**p** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the symmetric innovation(s). | [optional] 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# har_params

JSON containing options for the HARCH model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the HARCH model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... . | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**[p](#p)** | list, tuple,  | tuple,  | Order of the symmetric innovation(s). | [optional] 
**q** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the lagged (transformed) conditional variance. | [optional] 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# p

Order of the symmetric innovation(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Order of the symmetric innovation(s). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_custom_token_risk.ApiResponseFor200) | An object containing a summary of volatility and risk metrics for a (set of) given token id(s).
400 | [ApiResponseFor400](#get_pol_custom_token_risk.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_custom_token_risk.ApiResponseFor403) | Unauthorized

#### get_pol_custom_token_risk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_custom_token_risk.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_custom_token_risk.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_default_collection_risk**
<a name="get_pol_default_collection_risk"></a>
> get_pol_default_collection_risk()

Default Volatility & Risk Metrics by Collection

Returns summary of default volatility and risk metrics for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        holding_period="6M",
        rept_curr="eth",
        amount=1,
        drawdown=False,
    )
    try:
        # Default Volatility & Risk Metrics by Collection
        api_response = api_instance.get_pol_default_collection_risk(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_default_collection_risk: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**holding_period** | str,  | str,  | The holding period to evaluate risk for, e.g. &#x27;12M&#x27; | 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of tokens in your portfolio | [optional] 
**drawdown** | bool,  | BoolClass,  | If true, report drawdown volatility (based on negative returns only). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_default_collection_risk.ApiResponseFor200) | An object containing a summary of volatility and risk metrics for a (set of) collection percentile(s).
400 | [ApiResponseFor400](#get_pol_default_collection_risk.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_default_collection_risk.ApiResponseFor403) | Unauthorized

#### get_pol_default_collection_risk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_default_collection_risk.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_default_collection_risk.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_default_token_risk**
<a name="get_pol_default_token_risk"></a>
> get_pol_default_token_risk()

Default Volatility & Risk Metrics by Token

Returns summary of default volatility and risk metrics for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        token_id=[
            "6000"
        ],
        holding_period="6M",
        rept_curr="eth",
        drawdown=False,
    )
    try:
        # Default Volatility & Risk Metrics by Token
        api_response = api_instance.get_pol_default_token_risk(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_default_token_risk: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[token_id](#token_id)** | list, tuple,  | tuple,  | The id(s) for the token(s). | 
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**holding_period** | str,  | str,  | The holding period to evaluate risk for, e.g. &#x27;12M&#x27; | 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**drawdown** | bool,  | BoolClass,  | If true, report drawdown volatility (based on negative returns only). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# token_id

The id(s) for the token(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The id(s) for the token(s). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_default_token_risk.ApiResponseFor200) | An object containing a summary of volatility and risk metrics for a (set of) given token id(s).
400 | [ApiResponseFor400](#get_pol_default_token_risk.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_default_token_risk.ApiResponseFor403) | Unauthorized

#### get_pol_default_token_risk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_default_token_risk.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_default_token_risk.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_historical_transactions**
<a name="get_pol_historical_transactions"></a>
> get_pol_historical_transactions()

Historical Transactions by Collection

Returns all transactions for a given collection in bulk

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0x78306a498516d75a76beeacea04fe772d20fe41b",
        token_id="token_id_example",
        page=1,
    )
    try:
        # Historical Transactions by Collection
        api_response = api_instance.get_pol_historical_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_historical_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the collection. | 
**token_id** | str,  | str,  | The id for the token. | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_historical_transactions.ApiResponseFor200) | An object of property arrays.
400 | [ApiResponseFor400](#get_pol_historical_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_historical_transactions.ApiResponseFor403) | Unauthorized

#### get_pol_historical_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_historical_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_historical_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_leader_board**
<a name="get_pol_leader_board"></a>
> get_pol_leader_board()

Polygon Leaderboard by Collection

Returns top collections by volume transaction volume or sales count

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        page=1,
        page_size=100,
        interval="one_day",
        ranking_metric="eth_volume",
    )
    try:
        # Polygon Leaderboard by Collection
        api_response = api_instance.get_pol_leader_board(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_leader_board: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ranking_metric** | str,  | str,  | The requested calculation metric | must be one of ["eth_volume", "sales_count", ] 
**interval** | str,  | str,  | The requested time interval | must be one of ["one_day", "seven_days", "thirty_days", "ninety_days", "all_time", ] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_leader_board.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_leader_board.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_leader_board.ApiResponseFor403) | Unauthorized

#### get_pol_leader_board.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_leader_board.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_leader_board.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_marketplace_data**
<a name="get_pol_marketplace_data"></a>
> get_pol_marketplace_data()

Collection Summary by Marketplace

Returns summary statistics for collections by marketplace

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address=[
            "0x5cc5b05a8a13e3fbdb0bb9fccd98d38e50f90c38"
        ],
    )
    try:
        # Collection Summary by Marketplace
        api_response = api_instance.get_pol_marketplace_data(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_marketplace_data: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[collection_address](#collection_address)** | list, tuple,  | tuple,  | Array of collection addresses | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# collection_address

Array of collection addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of collection addresses | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_marketplace_data.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_marketplace_data.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_marketplace_data.ApiResponseFor403) | Unauthorized

#### get_pol_marketplace_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_marketplace_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_marketplace_data.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_marketplace_floor_price**
<a name="get_pol_marketplace_floor_price"></a>
> get_pol_marketplace_floor_price()

Marketplace Floor Price by Collection

Returns current floor price for all collections by marketplace

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        page=1,
        page_size=100,
        collection_address=[
            "0x049f8204bde39355b7892bac2a028a9d2f693792"
        ],
    )
    try:
        # Marketplace Floor Price by Collection
        api_response = api_instance.get_pol_marketplace_floor_price(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_marketplace_floor_price: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**[collection_address](#collection_address)** | list, tuple,  | tuple,  | Array of collection addresses | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# collection_address

Array of collection addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of collection addresses | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_marketplace_floor_price.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_marketplace_floor_price.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_marketplace_floor_price.ApiResponseFor403) | Unauthorized

#### get_pol_marketplace_floor_price.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_marketplace_floor_price.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_marketplace_floor_price.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_rarity**
<a name="get_pol_rarity"></a>
> get_pol_rarity()

Token Rarity by Collection

Returns rarity by token for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        weights=dict(),
        token_id=[
            "1327"
        ],
    )
    try:
        # Token Rarity by Collection
        api_response = api_instance.get_pol_rarity(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_rarity: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The Polygon contract address to identify the collection. | 
**[weights](#weights)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Dict containing trait keys and weight values. | [optional] 
**[token_id](#token_id)** | list, tuple,  | tuple,  | An array of token ids. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# weights

Dict containing trait keys and weight values.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Dict containing trait keys and weight values. | 

# token_id

An array of token ids.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of token ids. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_rarity.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_rarity.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_rarity.ApiResponseFor403) | Unauthorized

#### get_pol_rarity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_rarity.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_rarity.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_token_appraisal**
<a name="get_pol_token_appraisal"></a>
> get_pol_token_appraisal()

Liquidation & Appraisal Estimate by Token

Get estimates of appraisal and liquidation values for a set of tokens. The app returns nowcasts by default, but if provided a `horizon` and `frequency`, it will return forcasts for `horizon` periods out at interval `frequency`. The app is does not deliver individualized financial advice, but merely provides analytical estimates of token appraisal and liquidation values

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xad59ecb77033391e847cc96829b08beb83151088",
        token_id=[
            "5715"
        ],
        rept_curr="eth",
        frequency="1W",
        horizon=5,
        alpha=0.1,
        exclude_wash=True,
    )
    try:
        # Liquidation & Appraisal Estimate by Token
        api_response = api_instance.get_pol_token_appraisal(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_token_appraisal: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[token_id](#token_id)** | list, tuple,  | tuple,  | The id(s) for the token(s). | 
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**frequency** | str,  | str,  | The interval at which to calculate intermediate results and forecasts. | [optional] 
**horizon** | decimal.Decimal, int,  | decimal.Decimal,  | The forecast horizon (i.e. the number of periods to forecast out). Defaults to zero which only returns nowcasts. | [optional] 
**alpha** | decimal.Decimal, int, float,  | decimal.Decimal,  | The significance level for the liquidation estimate, e.g. 0.05 for 95% confidence | [optional] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# token_id

The id(s) for the token(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The id(s) for the token(s). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_token_appraisal.ApiResponseFor200) | An object containing appraisal and liquidation value estimates for a (set of) given token id(s).
400 | [ApiResponseFor400](#get_pol_token_appraisal.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_token_appraisal.ApiResponseFor403) | Unauthorized

#### get_pol_token_appraisal.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_token_appraisal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_token_appraisal.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_token_forecasts**
<a name="get_pol_token_forecasts"></a>
> get_pol_token_forecasts()

Price Forecast by Token

Returns price, return, and volatility forecast for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        token_id=["1722","2233"],
        voltype="har",
        horizon=5,
        frequency="1W",
        dist="norm",
        start_date="2021-01-01",
        end_date="2022-02-25",
        return_price_forecasts=True,
        alpha=0.05,
        rept_curr="eth",
        exclude_wash=True,
        arch_params=dict(
            mean="mean_example",
            lags=1,
            vol="vol_example",
            p=1,
            dist="norm",
        ),
    )
    try:
        # Price Forecast by Token
        api_response = api_instance.get_pol_token_forecasts(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_token_forecasts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[token_id](#token_id)** | list, tuple,  | tuple,  | The id(s) for the token(s). | 
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**voltype** | str,  | str,  | Type of statistical forecasting model to be calculated as a 3-char string, e.g. &#x60;arc&#x60; for ARCH | [optional] must be one of ["arc", "gar", "har", ] 
**horizon** | decimal.Decimal, int,  | decimal.Decimal,  | The forecast horizon (i.e. the number of periods to forecast out) | [optional] 
**frequency** | str,  | str,  | The interval at which to calculate returns to base the forecasts upon, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**dist** | str,  | str,  | The distribution assumed to calculate parametric risk for. | [optional] must be one of ["norm", "t", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**return_price_forecasts** | bool,  | BoolClass,  | Set to True, returns confidencve intervals at alpha significance for price on top of forecasts for returns and volatilities | [optional] 
**alpha** | decimal.Decimal, int, float,  | decimal.Decimal,  | The significance level, e.g. 0.05 for 95% confidence | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**[arch_params](#arch_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH family model. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# token_id

The id(s) for the token(s).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The id(s) for the token(s). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# arch_params

JSON containing options for the ARCH family model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH family model. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... .  | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**p** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the symmetric innovation(s). | [optional] 
**dist** | str,  | str,  | Return distribution assumed. | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_token_forecasts.ApiResponseFor200) | An object containing a set of forecasts for a (set of) collection percentile(s).
400 | [ApiResponseFor400](#get_pol_token_forecasts.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_token_forecasts.ApiResponseFor403) | Unauthorized

#### get_pol_token_forecasts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_token_forecasts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_token_forecasts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_token_summary**
<a name="get_pol_token_summary"></a>
> get_pol_token_summary()

Summary Statistics by Token

Returns summary analytics for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        token_id=[
            "1608"
        ],
        start_date="2021-01-01",
        end_date="2022-02-25",
        rept_curr="eth",
        exclude_wash=True,
    )
    try:
        # Summary Statistics by Token
        api_response = api_instance.get_pol_token_summary(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_token_summary: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[token_id](#token_id)** | list, tuple,  | tuple,  | The id for the token. | 
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["eth", "usd", "matic", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# token_id

The id for the token.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The id for the token. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_token_summary.ApiResponseFor200) | An object containing the token&#x27;s analytical summary.
400 | [ApiResponseFor400](#get_pol_token_summary.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_token_summary.ApiResponseFor403) | Unauthorized

#### get_pol_token_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_token_summary.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_token_summary.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_token_transactions**
<a name="get_pol_token_transactions"></a>
> get_pol_token_transactions()

Transactions by Token

Returns all transactions for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0x9d305a42A3975Ee4c1C57555BeD5919889DCE63F",
        token_id="993",
        page=1,
        page_size=100,
        start_date="2021-01-01",
        start_block_number=100,
        end_date="2022-02-25",
    )
    try:
        # Transactions by Token
        api_response = api_instance.get_pol_token_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_token_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**token_id** | str,  | str,  | The token id. | 
**collection_address** | str,  | str,  | The contract address the token belongs to. | 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**start_date** | str,  | str,  | The earliest block timestamp. | [optional] 
**start_block_number** | decimal.Decimal, int,  | decimal.Decimal,  | The oldest block number to return. | [optional] 
**end_date** | str,  | str,  | The latest block timestamp. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_token_transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_token_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_token_transactions.ApiResponseFor403) | Unauthorized

#### get_pol_token_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_token_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_token_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_tokens**
<a name="get_pol_tokens"></a>
> get_pol_tokens()

Tokens by Collection

Returns all tokens for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0x0004be0357533839ef78038b991fa24ace95544b",
        token_id=[
            "192"
        ],
        page=1,
        page_size=100,
    )
    try:
        # Tokens by Collection
        api_response = api_instance.get_pol_tokens(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_tokens: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The contract address of the token collection. | 
**[token_id](#token_id)** | list, tuple,  | tuple,  | A list of token ids. | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# token_id

A list of token ids.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of token ids. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_tokens.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_tokens.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_tokens.ApiResponseFor403) | Unauthorized

#### get_pol_tokens.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_tokens.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_tokens.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_wallet_labels**
<a name="get_pol_wallet_labels"></a>
> get_pol_wallet_labels()

Wallet Activity Labels

Classifies a wallet's behaviour according to its on-chain activity

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        wallet_address="0xcf561ea02950b819b0999ab3c3b43243d53e9b51",
    )
    try:
        # Wallet Activity Labels
        api_response = api_instance.get_pol_wallet_labels(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_wallet_labels: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wallet_address** | str,  | str,  | The EVM compatible wallet address | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_wallet_labels.ApiResponseFor200) | An object containing the wallet labels
400 | [ApiResponseFor400](#get_pol_wallet_labels.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_wallet_labels.ApiResponseFor403) | Unauthorized

#### get_pol_wallet_labels.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_wallet_labels.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_wallet_labels.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_wallet_nfts**
<a name="get_pol_wallet_nfts"></a>
> get_pol_wallet_nfts()

Tokens Owned by Wallet

Returns all tokens owned for a given wallet

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        wallet_address="0xab0cda4cc21207fd9433356afe9428b6fac8a8a5",
    )
    try:
        # Tokens Owned by Wallet
        api_response = api_instance.get_pol_wallet_nfts(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_wallet_nfts: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wallet_address** | str,  | str,  | The wallet address to search. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_wallet_nfts.ApiResponseFor200) | An object containing the tokens owned by this wallet
400 | [ApiResponseFor400](#get_pol_wallet_nfts.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_wallet_nfts.ApiResponseFor403) | Unauthorized

#### get_pol_wallet_nfts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_wallet_nfts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_wallet_nfts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_wallet_transactions**
<a name="get_pol_wallet_transactions"></a>
> get_pol_wallet_transactions()

Historical Token Transactions by Wallet

Returns all historical token transactions for a given wallet

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        wallet_address="0x88cf00c11883db002382e67527f1b8b1b5e6adad",
        page=1,
        page_size=100,
    )
    try:
        # Historical Token Transactions by Wallet
        api_response = api_instance.get_pol_wallet_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_wallet_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**wallet_address** | str,  | str,  | The wallet address to search. | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_wallet_transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_wallet_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_wallet_transactions.ApiResponseFor403) | Unauthorized

#### get_pol_wallet_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_wallet_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_wallet_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_wash_trade**
<a name="get_pol_wash_trade"></a>
> get_pol_wash_trade()

Wash Trades by Transaction

Returns suspected wash trades for a given transaction hash

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        transaction_hash="0x40692e18987ef5237cb0f9f0eaf8898e044a140b94d1cfc2a66dc9eb39033c1a",
    )
    try:
        # Wash Trades by Transaction
        api_response = api_instance.get_pol_wash_trade(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_wash_trade: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**transaction_hash** | str,  | str,  | The transaction hash to valildate. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_wash_trade.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_wash_trade.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_wash_trade.ApiResponseFor403) | Unauthorized

#### get_pol_wash_trade.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_wash_trade.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_wash_trade.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pol_wash_transactions**
<a name="get_pol_wash_transactions"></a>
> get_pol_wash_transactions()

Wash Trades by Collection

Returns suspected wash trades by token for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import polygon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.prod.gallop.run/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.prod.gallop.run/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = polygon_api.PolygonApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address="0xfbe3ab0cbfbd17d06bdd73aa3f55aaf038720f59",
        token_id=[
            "2334"
        ],
        page=1,
        page_size=100,
    )
    try:
        # Wash Trades by Collection
        api_response = api_instance.get_pol_wash_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling PolygonApi->get_pol_wash_transactions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection_address** | str,  | str,  | The collection address to search. | 
**[token_id](#token_id)** | list, tuple,  | tuple,  | An optional list of token ids. | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# token_id

An optional list of token ids.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of token ids. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pol_wash_transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_pol_wash_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_pol_wash_transactions.ApiResponseFor403) | Unauthorized

#### get_pol_wash_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_pol_wash_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_pol_wash_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

