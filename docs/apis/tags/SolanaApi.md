<a name="__pageTop"></a>
# openapi_client.apis.tags.solana_api.SolanaApi

All URIs are relative to *https://api.prod.gallop.run/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sol_account_nfts**](#get_sol_account_nfts) | **post** /data/sol/getAccountNFTs | Tokens Owned by Wallet
[**get_sol_collection_forecasts**](#get_sol_collection_forecasts) | **post** /insights/sol/getCollectionForecasts | Price Forecast by Collection
[**get_sol_collection_price_diff**](#get_sol_collection_price_diff) | **post** /analytics/sol/getCollectionPriceDiff | Price Differentiation by Trait
[**get_sol_collection_sales_ohlc**](#get_sol_collection_sales_ohlc) | **post** /analytics/sol/getCollectionSalesOHLC | Collection Sales Price Candlesticks
[**get_sol_collection_summary**](#get_sol_collection_summary) | **post** /analytics/sol/getCollectionSummary | Summary Statistics by Collection
[**get_sol_collection_traits**](#get_sol_collection_traits) | **post** /data/sol/getCollectionTraits | Traits by Collection
[**get_sol_collection_transactions**](#get_sol_collection_transactions) | **post** /data/sol/getCollectionTransactions | Transactions by Collections
[**get_sol_collections**](#get_sol_collections) | **post** /data/sol/getCollections | Aggregated Collections Supported by Gallop
[**get_sol_custom_collection_risk**](#get_sol_custom_collection_risk) | **post** /insights/sol/getCustomCollectionRisk | Custom Volatility &amp; Risk Metrics by Collection
[**get_sol_custom_token_risk**](#get_sol_custom_token_risk) | **post** /insights/sol/getCustomTokenRisk | Custom Volatility &amp; Risk Metrics by Token
[**get_sol_default_collection_risk**](#get_sol_default_collection_risk) | **post** /insights/sol/getDefaultCollectionRisk | Default Volatility &amp; Risk Metrics by Collection
[**get_sol_default_token_risk**](#get_sol_default_token_risk) | **post** /insights/sol/getDefaultTokenRisk | Default Volatility &amp; Risk Metrics by Token
[**get_sol_historical_transactions**](#get_sol_historical_transactions) | **post** /data/sol/getHistoricalTransactions | Historical Transactions by Collection
[**get_sol_marketplace_data**](#get_sol_marketplace_data) | **post** /data/sol/getMarketplaceData | Collection Summary by Marketplace
[**get_sol_marketplace_floor_price**](#get_sol_marketplace_floor_price) | **post** /data/sol/getMarketplaceFloorPrice | Marketplace Floor Price by Collection
[**get_sol_marketplace_trait_data**](#get_sol_marketplace_trait_data) | **post** /data/sol/getMarketplaceTraitData | Collection Listings by Trait &amp; Marketplace
[**get_sol_nft_account**](#get_sol_nft_account) | **post** /data/sol/getNFTAccount | Wallet Owners by Token
[**get_sol_rarity**](#get_sol_rarity) | **post** /analytics/sol/getRarity | Token Rarity by Collection
[**get_sol_token_appraisal**](#get_sol_token_appraisal) | **post** /insights/sol/getTokenAppraisal | Liquidation &amp; Appraisal Estimate by Token
[**get_sol_token_forecasts**](#get_sol_token_forecasts) | **post** /insights/sol/getTokenForecasts | Price Forecast by Token
[**get_sol_token_summary**](#get_sol_token_summary) | **post** /analytics/sol/getTokenSummary | Summary Statistics by Token
[**get_sol_token_transactions**](#get_sol_token_transactions) | **post** /data/sol/getTokenTransactions | Transactions by Token
[**get_sol_tokens**](#get_sol_tokens) | **post** /data/sol/getTokens | Tokens by Collection
[**get_sol_wash_trade**](#get_sol_wash_trade) | **post** /analytics/sol/getWashTrade | Wash Trades by Transaction
[**get_sol_wash_transactions**](#get_sol_wash_transactions) | **post** /analytics/sol/getWashTransactions | Wash Trades by Collection

# **get_sol_account_nfts**
<a name="get_sol_account_nfts"></a>
> get_sol_account_nfts()

Tokens Owned by Wallet

Returns all tokens owned for a given wallet

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        account_address="6CDuoSsn4ZRVvcBMdh9NEKkJebF3AFMdYTnPV4YrfEy6",
    )
    try:
        # Tokens Owned by Wallet
        api_response = api_instance.get_sol_account_nfts(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_account_nfts: %s\n" % e)
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
**account_address** | str,  | str,  | The account address to query. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_account_nfts.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_account_nfts.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_account_nfts.ApiResponseFor403) | Unauthorized

#### get_sol_account_nfts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_account_nfts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_account_nfts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_collection_forecasts**
<a name="get_sol_collection_forecasts"></a>
> get_sol_collection_forecasts()

Price Forecast by Collection

Returns price, return, and volatility forecast for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="shadowysupercoder",
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
        rept_curr="sol",
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
        api_response = api_instance.get_sol_collection_forecasts(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_collection_forecasts: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop tag to identify the collection. | 
**[percentiles](#percentiles)** | list, tuple,  | tuple,  | The collection percentile(s) | [optional] 
**voltype** | str,  | str,  | Type of statistical forecasting model to be calculated as a 3-char string, e.g. &#x27;arc&#x27; for ARCH | [optional] must be one of ["arc", "gar", "har", ] 
**horizon** | decimal.Decimal, int,  | decimal.Decimal,  | The forecast horizon (i.e. the number of periods to forecast out) | [optional] 
**frequency** | str,  | str,  | The interval at which to calculate returns to base the forecasts upon, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**dist** | str,  | str,  | The distribution assumed to calculate parametric risk for | [optional] must be one of ["norm", "t", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**return_price_forecasts** | bool,  | BoolClass,  | Set to True, returns confidencve intervals at alpha significance for price on top of forecasts for returns and volatilities | [optional] 
**alpha** | decimal.Decimal, int, float,  | decimal.Decimal,  | The significance level, e.g. 0.05 for 95% confidence | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**[arch_params](#arch_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH family model | [optional] 
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

JSON containing options for the ARCH family model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH family model | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean** | str,  | str,  | Estimator for the location model of the time series, e.g: &#x60;Zero&#x60;, &#x60;Constant&#x60;, &#x60;ARX&#x60;, ... .  | [optional] 
**lags** | decimal.Decimal, int,  | decimal.Decimal,  | Number of time time period lags considered. Note that the time period is set by the &#x60;frequency&#x60; parameter, so a value of 2 will assume 2-day lags if &#x60;frequency&#x3D;&#x3D;&#x27;1D&#x27;&#x60;. | [optional] 
**vol** | str,  | str,  | Estimator used for the volatility process of the time series, e.g: &#x60;Constant&#x60;, &#x60;ARCH&#x60;, &#x60;GARCH&#x60;, ...  | [optional] 
**p** | decimal.Decimal, int,  | decimal.Decimal,  | Order of the symmetric innovation(s). | [optional] 
**dist** | str,  | str,  | Return distribution assumed | [optional] must be one of ["norm", "t", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_collection_forecasts.ApiResponseFor200) | An object containing a set of forecasts for a (set of) collection percentile(s).
400 | [ApiResponseFor400](#get_sol_collection_forecasts.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_collection_forecasts.ApiResponseFor403) | Unauthorized

#### get_sol_collection_forecasts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_collection_forecasts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_collection_forecasts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_collection_price_diff**
<a name="get_sol_collection_price_diff"></a>
> get_sol_collection_price_diff()

Price Differentiation by Trait

Returns how trait differentiates price for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="shadowysupercoder",
        start_date="2021-08-01",
        end_date="2022-03-04",
        exclude_wash=True,
    )
    try:
        # Price Differentiation by Trait
        api_response = api_instance.get_sol_collection_price_diff(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_collection_price_diff: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop tag to identify the collection. | 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_collection_price_diff.ApiResponseFor200) | An object containing the collection&#x27;s price differentiation
400 | [ApiResponseFor400](#get_sol_collection_price_diff.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_collection_price_diff.ApiResponseFor403) | Unauthorized

#### get_sol_collection_price_diff.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_collection_price_diff.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_collection_price_diff.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_collection_sales_ohlc**
<a name="get_sol_collection_sales_ohlc"></a>
> get_sol_collection_sales_ohlc()

Collection Sales Price Candlesticks

Returns collection sales price open, high, low, close and volume at a selected time interval

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="shadowysupercoder",
        frequency="1D",
        group_by="Favorite Programming Language",
        volume=False,
        rept_curr="sol",
        start_date="2021-08-01",
        end_date="2022-03-04",
        exclude_wash=True,
    )
    try:
        # Collection Sales Price Candlesticks
        api_response = api_instance.get_sol_collection_sales_ohlc(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_collection_sales_ohlc: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop tag to identify the collection. | 
**frequency** | str,  | str,  | The interval at which to return OHLC, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**group_by** | str,  | str,  | An attribute of the NFT to group results by. | [optional] 
**volume** | bool,  | BoolClass,  | If &#x27;true&#x27;, response dicts contain OHLCV | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_collection_sales_ohlc.ApiResponseFor200) | An object containing the collection sales OHLC prices
400 | [ApiResponseFor400](#get_sol_collection_sales_ohlc.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_collection_sales_ohlc.ApiResponseFor403) | Unauthorized

#### get_sol_collection_sales_ohlc.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_collection_sales_ohlc.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_collection_sales_ohlc.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_collection_summary**
<a name="get_sol_collection_summary"></a>
> get_sol_collection_summary()

Summary Statistics by Collection

Returns summary analytics for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="shadowysupercoder",
        group_by="Favorite Programming Language",
        start_date="2021-08-01",
        end_date="2022-03-04",
        rept_curr="sol",
        exclude_wash=True,
    )
    try:
        # Summary Statistics by Collection
        api_response = api_instance.get_sol_collection_summary(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_collection_summary: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop tag to identify the collection. | 
**group_by** | str,  | str,  | An attribute of the NFT. | [optional] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_collection_summary.ApiResponseFor200) | An object containing the collection&#x27;s analytical summary.
400 | [ApiResponseFor400](#get_sol_collection_summary.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_collection_summary.ApiResponseFor403) | Unauthorized

#### get_sol_collection_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_collection_summary.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_collection_summary.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_collection_traits**
<a name="get_sol_collection_traits"></a>
> get_sol_collection_traits()

Traits by Collection

Returns a list of traits for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="solanamonkerejectsget",
    )
    try:
        # Traits by Collection
        api_response = api_instance.get_sol_collection_traits(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_collection_traits: %s\n" % e)
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
**collection_tag** | str,  | str,  | The tag of the collection. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_collection_traits.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_collection_traits.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_collection_traits.ApiResponseFor403) | Unauthorized

#### get_sol_collection_traits.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_collection_traits.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_collection_traits.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_collection_transactions**
<a name="get_sol_collection_transactions"></a>
> get_sol_collection_transactions()

Transactions by Collections

Returns all transactions for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="degenape",
        page=1,
        page_size=100,
        start_date="2021-01-01",
        end_date="2022-02-25",
    )
    try:
        # Transactions by Collections
        api_response = api_instance.get_sol_collection_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_collection_transactions: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop slug for the collection. Please see sol/getCollections endpoint. | 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**start_date** | str,  | str,  | The earliest block timestamp. | [optional] 
**end_date** | str,  | str,  | The latest block timestamp. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_collection_transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_collection_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_collection_transactions.ApiResponseFor403) | Unauthorized

#### get_sol_collection_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_collection_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_collection_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_collections**
<a name="get_sol_collections"></a>
> get_sol_collections()

Aggregated Collections Supported by Gallop

Returns all Gallop aggregated collections

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        page=1,
        page_size=100,
        collection_name="degen",
    )
    try:
        # Aggregated Collections Supported by Gallop
        api_response = api_instance.get_sol_collections(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_collections: %s\n" % e)
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
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_collections.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_collections.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_collections.ApiResponseFor403) | Unauthorized

#### get_sol_collections.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_collections.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_collections.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_custom_collection_risk**
<a name="get_sol_custom_collection_risk"></a>
> get_sol_custom_collection_risk()

Custom Volatility & Risk Metrics by Collection

Returns summary of customizable volatility and risk metrics for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="shadowysupercoder",
        holding_period="4M",
        percentiles=[
            73
        ],
        amount=1,
        dist="norm",
        start_date="2021-08-01",
        end_date="2022-02-04",
        wins_outliers=True,
        risk_free_rate=0.001,
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
        # Custom Volatility & Risk Metrics by Collection
        api_response = api_instance.get_sol_custom_collection_risk(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_custom_collection_risk: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop tag to identify the collection. | 
**holding_period** | str,  | str,  | The holding period to evaluate risk for, e.g. &#x60;12M&#x60; | 
**[percentiles](#percentiles)** | list, tuple,  | tuple,  | The collection percentile(s) | [optional] 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of tokens in your portfolio | [optional] 
**dist** | str,  | str,  | The distribution assumed to calculate parametric risk for | [optional] must be one of ["norm", "t", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**wins_outliers** | bool,  | BoolClass,  | Whether to winsorize time series outliers prior to calculating risk | [optional] 
**risk_free_rate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The rate of return for an asset deemed risk free in the contemplated holding period | [optional] 
**frequency** | str,  | str,  | The interval at which to calculate returns to base the forecasts upon, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
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
200 | [ApiResponseFor200](#get_sol_custom_collection_risk.ApiResponseFor200) | An object containing a summary of volatility and risk metrics for a (set of) collection percentile(s).
400 | [ApiResponseFor400](#get_sol_custom_collection_risk.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_custom_collection_risk.ApiResponseFor403) | Unauthorized

#### get_sol_custom_collection_risk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_custom_collection_risk.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_custom_collection_risk.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_custom_token_risk**
<a name="get_sol_custom_token_risk"></a>
> get_sol_custom_token_risk()

Custom Volatility & Risk Metrics by Token

Returns summary of customizable volatility and risk metrics for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        mint_address=[
            "DcFTUfcU4WRr4ybkgqpy26Y4g5g4YaCz42dryV6AiHp8"
        ],
        holding_period="4M",
        token_id="123",
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
        api_response = api_instance.get_sol_custom_token_risk(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_custom_token_risk: %s\n" % e)
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
**holding_period** | str,  | str,  | The holding period to evaluate risk for, e.g. &#x60;12M&#x60; | 
**[mint_address](#mint_address)** | list, tuple,  | tuple,  | A token mint address or list of mint addresses. | 
**token_id** | str,  | str,  | The numerical id for the token. Provide either id or mint address. | [optional] 
**dist** | str,  | str,  | The distribution assumed to calculate parametric risk for | [optional] must be one of ["norm", "t", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**risk_free_rate** | decimal.Decimal, int, float,  | decimal.Decimal,  | The rate of return for an asset deemed risk free in the contemplated holding period | [optional] 
**wins_outliers** | bool,  | BoolClass,  | Whether to winsorize time series outliers prior to calculating risk | [optional] 
**frequency** | str,  | str,  | The interval at which to calculate returns to base the forecasts upon, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**drawdown** | bool,  | BoolClass,  | If true, report drawdown volatility (based on negative returns only). | [optional] 
**[arc_params](#arc_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH model. | [optional] 
**[gar_params](#gar_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the GARCH model. | [optional] 
**[har_params](#har_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the HARCH model. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mint_address

A token mint address or list of mint addresses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A token mint address or list of mint addresses. | 

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
200 | [ApiResponseFor200](#get_sol_custom_token_risk.ApiResponseFor200) | An object containing a summary of volatility and risk metrics for a (set of) given token id(s).
400 | [ApiResponseFor400](#get_sol_custom_token_risk.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_custom_token_risk.ApiResponseFor403) | Unauthorized

#### get_sol_custom_token_risk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_custom_token_risk.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_custom_token_risk.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_default_collection_risk**
<a name="get_sol_default_collection_risk"></a>
> get_sol_default_collection_risk()

Default Volatility & Risk Metrics by Collection

Returns summary of default volatility and risk metrics for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="shadowysupercoder",
        holding_period="4M",
        amount=1,
        rept_curr="sol",
        drawdown=False,
    )
    try:
        # Default Volatility & Risk Metrics by Collection
        api_response = api_instance.get_sol_default_collection_risk(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_default_collection_risk: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop tag to identify the collection. | 
**holding_period** | str,  | str,  | The holding period to evaluate risk for, e.g. &#x27;12M&#x27; | 
**amount** | decimal.Decimal, int,  | decimal.Decimal,  | The amount of tokens in your portfolio | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**drawdown** | bool,  | BoolClass,  | If true, report drawdown volatility (based on negative returns only). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_default_collection_risk.ApiResponseFor200) | An object containing a summary of volatility and risk metrics for a (set of) collection percentile(s).
400 | [ApiResponseFor400](#get_sol_default_collection_risk.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_default_collection_risk.ApiResponseFor403) | Unauthorized

#### get_sol_default_collection_risk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_default_collection_risk.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_default_collection_risk.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_default_token_risk**
<a name="get_sol_default_token_risk"></a>
> get_sol_default_token_risk()

Default Volatility & Risk Metrics by Token

Returns summary of default volatility and risk metrics for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        mint_address=[
            "DcFTUfcU4WRr4ybkgqpy26Y4g5g4YaCz42dryV6AiHp8"
        ],
        holding_period="4M",
        rept_curr="sol",
        drawdown=False,
    )
    try:
        # Default Volatility & Risk Metrics by Token
        api_response = api_instance.get_sol_default_token_risk(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_default_token_risk: %s\n" % e)
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
**holding_period** | str,  | str,  | The holding period to evaluate risk for, e.g. &#x27;12M&#x27; | 
**[mint_address](#mint_address)** | list, tuple,  | tuple,  | A token mint address or list of mint addresses. | 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**drawdown** | bool,  | BoolClass,  | If true, report drawdown volatility (based on negative returns only). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mint_address

A token mint address or list of mint addresses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A token mint address or list of mint addresses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_default_token_risk.ApiResponseFor200) | An object containing a summary of volatility and risk metrics for a (set of) given token id(s).
400 | [ApiResponseFor400](#get_sol_default_token_risk.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_default_token_risk.ApiResponseFor403) | Unauthorized

#### get_sol_default_token_risk.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_default_token_risk.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_default_token_risk.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_historical_transactions**
<a name="get_sol_historical_transactions"></a>
> get_sol_historical_transactions()

Historical Transactions by Collection

Returns all transactions for a given collection in bulk

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="degenape",
        page=1,
    )
    try:
        # Historical Transactions by Collection
        api_response = api_instance.get_sol_historical_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_historical_transactions: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop slug for the collection. Please see sol/getCollections endpoint. | 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_historical_transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_historical_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_historical_transactions.ApiResponseFor403) | Unauthorized

#### get_sol_historical_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_historical_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_historical_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_marketplace_data**
<a name="get_sol_marketplace_data"></a>
> get_sol_marketplace_data()

Collection Summary by Marketplace

Returns summary statistics for collections by marketplace

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag=[
            "downtowngirlz"
        ],
    )
    try:
        # Collection Summary by Marketplace
        api_response = api_instance.get_sol_marketplace_data(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_marketplace_data: %s\n" % e)
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
**[collection_tag](#collection_tag)** | list, tuple,  | tuple,  | Array of Gallop collection tags | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# collection_tag

Array of Gallop collection tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of Gallop collection tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_marketplace_data.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_marketplace_data.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_marketplace_data.ApiResponseFor403) | Unauthorized

#### get_sol_marketplace_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_marketplace_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_marketplace_data.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_marketplace_floor_price**
<a name="get_sol_marketplace_floor_price"></a>
> get_sol_marketplace_floor_price()

Marketplace Floor Price by Collection

Returns current floor price for all collections by marketplace

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        page=1,
        page_size=100,
        collection_tag=[
            "downtowngirlz"
        ],
    )
    try:
        # Marketplace Floor Price by Collection
        api_response = api_instance.get_sol_marketplace_floor_price(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_marketplace_floor_price: %s\n" % e)
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
**[collection_tag](#collection_tag)** | list, tuple,  | tuple,  | Array of Gallop collection tags | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# collection_tag

Array of Gallop collection tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of Gallop collection tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_marketplace_floor_price.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_marketplace_floor_price.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_marketplace_floor_price.ApiResponseFor403) | Unauthorized

#### get_sol_marketplace_floor_price.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_marketplace_floor_price.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_marketplace_floor_price.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_marketplace_trait_data**
<a name="get_sol_marketplace_trait_data"></a>
> get_sol_marketplace_trait_data()

Collection Listings by Trait & Marketplace

Returns listing statistics for a collection by trait and marketplace

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="downtowngirlz",
    )
    try:
        # Collection Listings by Trait & Marketplace
        api_response = api_instance.get_sol_marketplace_trait_data(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_marketplace_trait_data: %s\n" % e)
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
**collection_tag** | str,  | str,  | Collection_tag | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_marketplace_trait_data.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_marketplace_trait_data.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_marketplace_trait_data.ApiResponseFor403) | Unauthorized

#### get_sol_marketplace_trait_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_marketplace_trait_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_marketplace_trait_data.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_nft_account**
<a name="get_sol_nft_account"></a>
> get_sol_nft_account()

Wallet Owners by Token

Returns all wallet owners for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        mint_address="G6oNTZRyrU2tN1YnWREmFaLwEcMA7QDoCscxon4Xrkbp",
    )
    try:
        # Wallet Owners by Token
        api_response = api_instance.get_sol_nft_account(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_nft_account: %s\n" % e)
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
**mint_address** | str,  | str,  | The Solana token mint address. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_nft_account.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_nft_account.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_nft_account.ApiResponseFor403) | Unauthorized

#### get_sol_nft_account.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_nft_account.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_nft_account.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_rarity**
<a name="get_sol_rarity"></a>
> get_sol_rarity()

Token Rarity by Collection

Returns rarity by token for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="portals",
        mint_address=[
            "9quKRGQ73y25CfVCeZ5u9VpaXZ27JzYQM374QDzGAXK2"
        ],
        weights=dict(),
    )
    try:
        # Token Rarity by Collection
        api_response = api_instance.get_sol_rarity(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_rarity: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop tag for the Solana collection. Please see sol/getCollections endpoint. | 
**[mint_address](#mint_address)** | list, tuple,  | tuple,  | A list of token addresses. | [optional] 
**[weights](#weights)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Dict containing trait keys and weight values. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mint_address

A list of token addresses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of token addresses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# weights

Dict containing trait keys and weight values.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Dict containing trait keys and weight values. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_rarity.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_rarity.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_rarity.ApiResponseFor403) | Unauthorized

#### get_sol_rarity.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_rarity.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_rarity.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_token_appraisal**
<a name="get_sol_token_appraisal"></a>
> get_sol_token_appraisal()

Liquidation & Appraisal Estimate by Token

Get estimates of appraisal and liquidation values for a set of tokens. The app returns nowcasts by default, but if provided a `horizon` and `frequency`, it will return forcasts for `horizon` periods out at interval `frequency`. The app is does not deliver individualized financial advice, but merely provides analytical estimates of token appraisal and liquidation values

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        mint_address=[
            "8hBJ4TfzgozfNxqaWLT9hwgMzrbWRKCoeJysjPQnNea5"
        ],
        rept_curr="sol",
        frequency="1W",
        horizon=5,
        alpha=0.1,
        exclude_wash=True,
    )
    try:
        # Liquidation & Appraisal Estimate by Token
        api_response = api_instance.get_sol_token_appraisal(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_token_appraisal: %s\n" % e)
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
**[mint_address](#mint_address)** | list, tuple,  | tuple,  | List of mint addresses of tokens to appraise | 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**frequency** | str,  | str,  | The interval at which to calculate intermediate results and forecasts. | [optional] 
**horizon** | decimal.Decimal, int,  | decimal.Decimal,  | The forecast horizon (i.e. the number of periods to forecast out). Defaults to zero which only returns nowcasts. | [optional] 
**alpha** | decimal.Decimal, int, float,  | decimal.Decimal,  | The significance level for the liquidation estimate, e.g. 0.05 for 95% confidence | [optional] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mint_address

List of mint addresses of tokens to appraise

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of mint addresses of tokens to appraise | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_token_appraisal.ApiResponseFor200) | An object containing appraisal and liquidation value estimates for a (set of) given mint address(es).
400 | [ApiResponseFor400](#get_sol_token_appraisal.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_token_appraisal.ApiResponseFor403) | Unauthorized

#### get_sol_token_appraisal.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_token_appraisal.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_token_appraisal.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_token_forecasts**
<a name="get_sol_token_forecasts"></a>
> get_sol_token_forecasts()

Price Forecast by Token

Returns price, return, and volatility forecast for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        mint_address=[
            "DcFTUfcU4WRr4ybkgqpy26Y4g5g4YaCz42dryV6AiHp8"
        ],
        token_id="token_id_example",
        voltype="har",
        horizon=5,
        frequency="1D",
        dist="norm",
        start_date="2021-01-01",
        end_date="2022-02-25",
        return_price_forecasts=True,
        alpha=0.05,
        rept_curr="sol",
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
        api_response = api_instance.get_sol_token_forecasts(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_token_forecasts: %s\n" % e)
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
**[mint_address](#mint_address)** | list, tuple,  | tuple,  | A token mint address or list of token addresses. | 
**token_id** | str,  | str,  | The numerical id for the token. Provide either id or mint address. | [optional] 
**voltype** | str,  | str,  | Type of statistical forecasting model to be calculated as a 3-char string, e.g. &#x27;arc&#x27; for ARCH | [optional] must be one of ["arc", "gar", "har", ] 
**horizon** | decimal.Decimal, int,  | decimal.Decimal,  | The forecast horizon (i.e. the number of periods to forecast out) | [optional] 
**frequency** | str,  | str,  | The interval at which to calculate returns to base the forecasts upon, e.g. &#x60;1D&#x60; for daily, &#x60;1M&#x60; for monthly etc. | [optional] 
**dist** | str,  | str,  | The distribution assumed to calculate parametric risk for | [optional] must be one of ["norm", "t", ] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**return_price_forecasts** | bool,  | BoolClass,  | Set to True, returns confidencve intervals at alpha significance for price on top of forecasts for returns and volatilities | [optional] 
**alpha** | decimal.Decimal, int, float,  | decimal.Decimal,  | The significance level, e.g. 0.05 for 95% confidence | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**[arch_params](#arch_params)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH family model | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mint_address

A token mint address or list of token addresses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A token mint address or list of token addresses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# arch_params

JSON containing options for the ARCH family model

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | JSON containing options for the ARCH family model | 

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
200 | [ApiResponseFor200](#get_sol_token_forecasts.ApiResponseFor200) | An object containing a set of forecasts for a (set of) collection percentile(s).
400 | [ApiResponseFor400](#get_sol_token_forecasts.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_token_forecasts.ApiResponseFor403) | Unauthorized

#### get_sol_token_forecasts.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_token_forecasts.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_token_forecasts.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_token_summary**
<a name="get_sol_token_summary"></a>
> get_sol_token_summary()

Summary Statistics by Token

Returns summary analytics for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        mint_address=[
            "DcFTUfcU4WRr4ybkgqpy26Y4g5g4YaCz42dryV6AiHp8"
        ],
        token_id="token_id_example",
        start_date="2021-01-01",
        end_date="2022-02-25",
        rept_curr="sol",
        exclude_wash=True,
    )
    try:
        # Summary Statistics by Token
        api_response = api_instance.get_sol_token_summary(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_token_summary: %s\n" % e)
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
**[mint_address](#mint_address)** | list, tuple,  | tuple,  | A token mint address or list of token addresses. | 
**token_id** | str,  | str,  | The numerical id for the token. Provide either id or mint address. | [optional] 
**start_date** | str,  | str,  | The start date to pull data for calculations | [optional] 
**end_date** | str,  | str,  | The end date to pull data for calculations | [optional] 
**rept_curr** | str,  | str,  | The currency to report results in | [optional] must be one of ["sol", "usd", ] 
**exclude_wash** | bool,  | BoolClass,  | Exclude suspected wash transactions? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mint_address

A token mint address or list of token addresses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A token mint address or list of token addresses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_token_summary.ApiResponseFor200) | An object containing the token&#x27;s analytical summary.
400 | [ApiResponseFor400](#get_sol_token_summary.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_token_summary.ApiResponseFor403) | Unauthorized

#### get_sol_token_summary.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_token_summary.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_token_summary.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_token_transactions**
<a name="get_sol_token_transactions"></a>
> get_sol_token_transactions()

Transactions by Token

Returns all transactions for a given token

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        mint_address="5uarH96GLf4APmipQRrsD3SsW4K77zRPtWGwETcyz5GE",
        page=1,
        page_size=100,
        start_date="2021-01-01",
        end_date="2022-02-25",
    )
    try:
        # Transactions by Token
        api_response = api_instance.get_sol_token_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_token_transactions: %s\n" % e)
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
**mint_address** | str,  | str,  | The mint address of the token. | 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**start_date** | str,  | str,  | The earliest block timestamp. | [optional] 
**end_date** | str,  | str,  | The latest block timestamp. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_token_transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_token_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_token_transactions.ApiResponseFor403) | Unauthorized

#### get_sol_token_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_token_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_token_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_tokens**
<a name="get_sol_tokens"></a>
> get_sol_tokens()

Tokens by Collection

Returns all tokens for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="degenape",
        mint_address=[
            "G4Tbp5zWZRt1thiuv7ywkotcXZvf24DrUEMoM2j6Vj63"
        ],
        page=1,
        page_size=100,
    )
    try:
        # Tokens by Collection
        api_response = api_instance.get_sol_tokens(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_tokens: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop tag for the Solana collection. Please see sol/getCollections endpoint. | 
**[mint_address](#mint_address)** | list, tuple,  | tuple,  | A list of token addresses. | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mint_address

A list of token addresses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of token addresses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_tokens.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_tokens.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_tokens.ApiResponseFor403) | Unauthorized

#### get_sol_tokens.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_tokens.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_tokens.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_wash_trade**
<a name="get_sol_wash_trade"></a>
> get_sol_wash_trade()

Wash Trades by Transaction

Returns suspected wash trades for a given transaction hash

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        first_signature="jAV6y8eKCACX9bwNaiVgh6mqoxiCHrovWSYVXWmZfj5EhHDmXHeu23DwgnvnPQHjudKj9DK5ed73zq2yAkaJtqg",
    )
    try:
        # Wash Trades by Transaction
        api_response = api_instance.get_sol_wash_trade(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_wash_trade: %s\n" % e)
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
**first_signature** | str,  | str,  | The first signature to valildate. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_wash_trade.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_wash_trade.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_wash_trade.ApiResponseFor403) | Unauthorized

#### get_sol_wash_trade.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_wash_trade.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_wash_trade.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_sol_wash_transactions**
<a name="get_sol_wash_transactions"></a>
> get_sol_wash_transactions()

Wash Trades by Collection

Returns suspected wash trades by token for a given collection

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import solana_api
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
    api_instance = solana_api.SolanaApi(api_client)

    # example passing only optional values
    body = dict(
        collection_tag="degods",
        mint_address=[
            "G4Tbp5zWZRt1thiuv7ywkotcXZvf24DrUEMoM2j6Vj63"
        ],
        page=1,
        page_size=100,
    )
    try:
        # Wash Trades by Collection
        api_response = api_instance.get_sol_wash_transactions(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling SolanaApi->get_sol_wash_transactions: %s\n" % e)
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
**collection_tag** | str,  | str,  | The Gallop slug for the collection. Please see sol/getCollections endpoint. | 
**[mint_address](#mint_address)** | list, tuple,  | tuple,  | An optional list of token addresses. | [optional] 
**page** | decimal.Decimal, int,  | decimal.Decimal,  | The pagination cursor. | [optional] 
**page_size** | decimal.Decimal, int,  | decimal.Decimal,  | The number of records returned per page. | [optional] must be one of [50, 100, 500, 1000, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mint_address

An optional list of token addresses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An optional list of token addresses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sol_wash_transactions.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_sol_wash_transactions.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_sol_wash_transactions.ApiResponseFor403) | Unauthorized

#### get_sol_wash_transactions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_sol_wash_transactions.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_sol_wash_transactions.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

