<a name="__pageTop"></a>
# openapi_client.apis.tags.starknet_api.StarknetApi

All URIs are relative to *https://api.prod.gallop.run/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_skn_marketplace_data**](#get_skn_marketplace_data) | **post** /data/skn/getMarketplaceData | Gallop Marketplace Data
[**get_skn_marketplace_floor_price**](#get_skn_marketplace_floor_price) | **post** /data/skn/getMarketplaceFloorPrice | Marketplace Floor Price by Collection

# **get_skn_marketplace_data**
<a name="get_skn_marketplace_data"></a>
> get_skn_marketplace_data()

Gallop Marketplace Data

Lists marketplace data from contract address.

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import starknet_api
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
    api_instance = starknet_api.StarknetApi(api_client)

    # example passing only optional values
    body = dict(
        collection_address=[
            "0x04acd4b2a59eae7196f6a5c26ead8cb5f9d7ad3d911096418a23357bb2eac075"
        ],
    )
    try:
        # Gallop Marketplace Data
        api_response = api_instance.get_skn_marketplace_data(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling StarknetApi->get_skn_marketplace_data: %s\n" % e)
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
200 | [ApiResponseFor200](#get_skn_marketplace_data.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_skn_marketplace_data.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_skn_marketplace_data.ApiResponseFor403) | Unauthorized

#### get_skn_marketplace_data.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_skn_marketplace_data.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_skn_marketplace_data.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_skn_marketplace_floor_price**
<a name="get_skn_marketplace_floor_price"></a>
> get_skn_marketplace_floor_price()

Marketplace Floor Price by Collection

Returns current floor price for all collections by marketplace

### Example

* Api Key Authentication (api_key):
```python
import openapi_client
from openapi_client.apis.tags import starknet_api
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
    api_instance = starknet_api.StarknetApi(api_client)

    # example passing only optional values
    body = dict(
        page=1,
        page_size=100,
        collection_address=[
            "0x00002d0fe59a81c3c98fe65bbe62061e39e6effbd9ff9b4ca35ea3e9fdad7591"
        ],
    )
    try:
        # Marketplace Floor Price by Collection
        api_response = api_instance.get_skn_marketplace_floor_price(
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling StarknetApi->get_skn_marketplace_floor_price: %s\n" % e)
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
200 | [ApiResponseFor200](#get_skn_marketplace_floor_price.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_skn_marketplace_floor_price.ApiResponseFor400) | Bad request
403 | [ApiResponseFor403](#get_skn_marketplace_floor_price.ApiResponseFor403) | Unauthorized

#### get_skn_marketplace_floor_price.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### get_skn_marketplace_floor_price.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_skn_marketplace_floor_price.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[api_key](../../../README.md#api_key)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

