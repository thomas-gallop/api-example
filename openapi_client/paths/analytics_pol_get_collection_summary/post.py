# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from openapi_client import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401

from . import path

# body param


class SchemaForRequestBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        required = {
            "collection_address",
        }
        
        class properties:
            collection_address = schemas.StrSchema
            group_by = schemas.StrSchema
            start_date = schemas.StrSchema
            end_date = schemas.StrSchema
            
            
            class rept_curr(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "eth": "ETH",
                        "usd": "USD",
                        "matic": "MATIC",
                    }
                
                @schemas.classproperty
                def ETH(cls):
                    return cls("eth")
                
                @schemas.classproperty
                def USD(cls):
                    return cls("usd")
                
                @schemas.classproperty
                def MATIC(cls):
                    return cls("matic")
            exclude_wash = schemas.BoolSchema
            __annotations__ = {
                "collection_address": collection_address,
                "group_by": group_by,
                "start_date": start_date,
                "end_date": end_date,
                "rept_curr": rept_curr,
                "exclude_wash": exclude_wash,
            }
    
    collection_address: MetaOapg.properties.collection_address
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection_address"]) -> MetaOapg.properties.collection_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["group_by"]) -> MetaOapg.properties.group_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_date"]) -> MetaOapg.properties.end_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rept_curr"]) -> MetaOapg.properties.rept_curr: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclude_wash"]) -> MetaOapg.properties.exclude_wash: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["collection_address", "group_by", "start_date", "end_date", "rept_curr", "exclude_wash", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection_address"]) -> MetaOapg.properties.collection_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["group_by"]) -> typing.Union[MetaOapg.properties.group_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_date"]) -> typing.Union[MetaOapg.properties.end_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rept_curr"]) -> typing.Union[MetaOapg.properties.rept_curr, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclude_wash"]) -> typing.Union[MetaOapg.properties.exclude_wash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["collection_address", "group_by", "start_date", "end_date", "rept_curr", "exclude_wash", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        collection_address: typing.Union[MetaOapg.properties.collection_address, str, ],
        group_by: typing.Union[MetaOapg.properties.group_by, str, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, schemas.Unset] = schemas.unset,
        end_date: typing.Union[MetaOapg.properties.end_date, str, schemas.Unset] = schemas.unset,
        rept_curr: typing.Union[MetaOapg.properties.rept_curr, str, schemas.Unset] = schemas.unset,
        exclude_wash: typing.Union[MetaOapg.properties.exclude_wash, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaForRequestBodyApplicationJson':
        return super().__new__(
            cls,
            *_args,
            collection_address=collection_address,
            group_by=group_by,
            start_date=start_date,
            end_date=end_date,
            rept_curr=rept_curr,
            exclude_wash=exclude_wash,
            _configuration=_configuration,
            **kwargs,
        )


request_body_any_type = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'api_key',
]


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        schemas.Unset,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '403': _response_for_403,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _get_pol_collection_summary_oapg(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _get_pol_collection_summary_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def _get_pol_collection_summary_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _get_pol_collection_summary_oapg(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _get_pol_collection_summary_oapg(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Summary Statistics by Collection
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not schemas.unset:
            serialized_data = request_body_any_type.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=used_path,
            method='post'.upper(),
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class GetPolCollectionSummary(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def get_pol_collection_summary(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get_pol_collection_summary(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def get_pol_collection_summary(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get_pol_collection_summary(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get_pol_collection_summary(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_pol_collection_summary_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def post(
        self,
        content_type: typing_extensions.Literal["application/json"] = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...


    @typing.overload
    def post(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def post(
        self,
        content_type: str = ...,
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def post(
        self,
        content_type: str = 'application/json',
        body: typing.Union[SchemaForRequestBodyApplicationJson, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._get_pol_collection_summary_oapg(
            body=body,
            content_type=content_type,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


