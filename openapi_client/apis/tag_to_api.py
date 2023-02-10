import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.data_api import DataApi
from openapi_client.apis.tags.analytics_api import AnalyticsApi
from openapi_client.apis.tags.insights_api import InsightsApi
from openapi_client.apis.tags.ethereum_api import EthereumApi
from openapi_client.apis.tags.polygon_api import PolygonApi
from openapi_client.apis.tags.solana_api import SolanaApi
from openapi_client.apis.tags.starknet_api import StarknetApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DATA: DataApi,
        TagValues.ANALYTICS: AnalyticsApi,
        TagValues.INSIGHTS: InsightsApi,
        TagValues.ETHEREUM: EthereumApi,
        TagValues.POLYGON: PolygonApi,
        TagValues.SOLANA: SolanaApi,
        TagValues.STARKNET: StarknetApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DATA: DataApi,
        TagValues.ANALYTICS: AnalyticsApi,
        TagValues.INSIGHTS: InsightsApi,
        TagValues.ETHEREUM: EthereumApi,
        TagValues.POLYGON: PolygonApi,
        TagValues.SOLANA: SolanaApi,
        TagValues.STARKNET: StarknetApi,
    }
)
