import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.data_eth_get_collections import DataEthGetCollections
from openapi_client.apis.paths.data_eth_get_tokens import DataEthGetTokens
from openapi_client.apis.paths.data_eth_get_collection_transactions import DataEthGetCollectionTransactions
from openapi_client.apis.paths.data_eth_get_token_transactions import DataEthGetTokenTransactions
from openapi_client.apis.paths.data_eth_get_marketplace_data import DataEthGetMarketplaceData
from openapi_client.apis.paths.data_eth_get_marketplace_trait_data import DataEthGetMarketplaceTraitData
from openapi_client.apis.paths.data_eth_get_wallet_nfts import DataEthGetWalletNFTs
from openapi_client.apis.paths.data_eth_get_wallet_transactions import DataEthGetWalletTransactions
from openapi_client.apis.paths.data_eth_get_historical_transactions import DataEthGetHistoricalTransactions
from openapi_client.apis.paths.data_eth_get_historical_events import DataEthGetHistoricalEvents
from openapi_client.apis.paths.data_eth_get_collection_owners import DataEthGetCollectionOwners
from openapi_client.apis.paths.data_eth_get_marketplace_floor_price import DataEthGetMarketplaceFloorPrice
from openapi_client.apis.paths.data_eth_get_ens_lookup import DataEthGetEnsLookup
from openapi_client.apis.paths.data_sol_get_collections import DataSolGetCollections
from openapi_client.apis.paths.data_sol_get_tokens import DataSolGetTokens
from openapi_client.apis.paths.data_sol_get_collection_transactions import DataSolGetCollectionTransactions
from openapi_client.apis.paths.data_sol_get_token_transactions import DataSolGetTokenTransactions
from openapi_client.apis.paths.data_sol_get_account_nfts import DataSolGetAccountNFTs
from openapi_client.apis.paths.data_sol_get_nft_account import DataSolGetNFTAccount
from openapi_client.apis.paths.data_sol_get_marketplace_data import DataSolGetMarketplaceData
from openapi_client.apis.paths.data_sol_get_marketplace_trait_data import DataSolGetMarketplaceTraitData
from openapi_client.apis.paths.data_sol_get_collection_traits import DataSolGetCollectionTraits
from openapi_client.apis.paths.data_sol_get_historical_transactions import DataSolGetHistoricalTransactions
from openapi_client.apis.paths.data_sol_get_marketplace_floor_price import DataSolGetMarketplaceFloorPrice
from openapi_client.apis.paths.data_pol_get_collections import DataPolGetCollections
from openapi_client.apis.paths.data_pol_get_collection_transactions import DataPolGetCollectionTransactions
from openapi_client.apis.paths.data_pol_get_token_transactions import DataPolGetTokenTransactions
from openapi_client.apis.paths.data_pol_get_tokens import DataPolGetTokens
from openapi_client.apis.paths.data_pol_get_collection_traits import DataPolGetCollectionTraits
from openapi_client.apis.paths.data_pol_get_wallet_nfts import DataPolGetWalletNFTs
from openapi_client.apis.paths.data_pol_get_collection_owners import DataPolGetCollectionOwners
from openapi_client.apis.paths.data_pol_get_marketplace_data import DataPolGetMarketplaceData
from openapi_client.apis.paths.data_pol_get_marketplace_floor_price import DataPolGetMarketplaceFloorPrice
from openapi_client.apis.paths.data_pol_get_wallet_transactions import DataPolGetWalletTransactions
from openapi_client.apis.paths.data_pol_get_historical_transactions import DataPolGetHistoricalTransactions
from openapi_client.apis.paths.data_skn_get_marketplace_floor_price import DataSknGetMarketplaceFloorPrice
from openapi_client.apis.paths.data_skn_get_marketplace_data import DataSknGetMarketplaceData
from openapi_client.apis.paths.analytics_eth_get_collection_summary import AnalyticsEthGetCollectionSummary
from openapi_client.apis.paths.analytics_eth_get_token_summary import AnalyticsEthGetTokenSummary
from openapi_client.apis.paths.analytics_eth_get_collection_price_diff import AnalyticsEthGetCollectionPriceDiff
from openapi_client.apis.paths.analytics_eth_get_wash_transactions import AnalyticsEthGetWashTransactions
from openapi_client.apis.paths.analytics_eth_get_wash_trade import AnalyticsEthGetWashTrade
from openapi_client.apis.paths.analytics_eth_get_rarity import AnalyticsEthGetRarity
from openapi_client.apis.paths.analytics_eth_get_collection_sales_ohlc import AnalyticsEthGetCollectionSalesOHLC
from openapi_client.apis.paths.analytics_eth_get_collection_floor_price_ohlc import AnalyticsEthGetCollectionFloorPriceOHLC
from openapi_client.apis.paths.analytics_eth_get_collection_listings_ohlc import AnalyticsEthGetCollectionListingsOHLC
from openapi_client.apis.paths.analytics_eth_get_leader_board import AnalyticsEthGetLeaderBoard
from openapi_client.apis.paths.analytics_sol_get_collection_summary import AnalyticsSolGetCollectionSummary
from openapi_client.apis.paths.analytics_sol_get_token_summary import AnalyticsSolGetTokenSummary
from openapi_client.apis.paths.analytics_sol_get_collection_price_diff import AnalyticsSolGetCollectionPriceDiff
from openapi_client.apis.paths.analytics_sol_get_wash_transactions import AnalyticsSolGetWashTransactions
from openapi_client.apis.paths.analytics_sol_get_wash_trade import AnalyticsSolGetWashTrade
from openapi_client.apis.paths.analytics_sol_get_rarity import AnalyticsSolGetRarity
from openapi_client.apis.paths.analytics_sol_get_collection_sales_ohlc import AnalyticsSolGetCollectionSalesOHLC
from openapi_client.apis.paths.analytics_pol_get_collection_summary import AnalyticsPolGetCollectionSummary
from openapi_client.apis.paths.analytics_pol_get_token_summary import AnalyticsPolGetTokenSummary
from openapi_client.apis.paths.analytics_pol_get_collection_price_diff import AnalyticsPolGetCollectionPriceDiff
from openapi_client.apis.paths.analytics_pol_get_wash_transactions import AnalyticsPolGetWashTransactions
from openapi_client.apis.paths.analytics_pol_get_wash_trade import AnalyticsPolGetWashTrade
from openapi_client.apis.paths.analytics_pol_get_rarity import AnalyticsPolGetRarity
from openapi_client.apis.paths.analytics_pol_get_collection_sales_ohlc import AnalyticsPolGetCollectionSalesOHLC
from openapi_client.apis.paths.analytics_pol_get_leader_board import AnalyticsPolGetLeaderBoard
from openapi_client.apis.paths.insights_eth_get_custom_collection_risk import InsightsEthGetCustomCollectionRisk
from openapi_client.apis.paths.insights_eth_get_custom_token_risk import InsightsEthGetCustomTokenRisk
from openapi_client.apis.paths.insights_eth_get_default_collection_risk import InsightsEthGetDefaultCollectionRisk
from openapi_client.apis.paths.insights_eth_get_default_token_risk import InsightsEthGetDefaultTokenRisk
from openapi_client.apis.paths.insights_eth_get_collection_forecasts import InsightsEthGetCollectionForecasts
from openapi_client.apis.paths.insights_eth_get_token_forecasts import InsightsEthGetTokenForecasts
from openapi_client.apis.paths.insights_eth_get_token_appraisal import InsightsEthGetTokenAppraisal
from openapi_client.apis.paths.insights_eth_get_wallet_labels import InsightsEthGetWalletLabels
from openapi_client.apis.paths.insights_sol_get_custom_collection_risk import InsightsSolGetCustomCollectionRisk
from openapi_client.apis.paths.insights_sol_get_custom_token_risk import InsightsSolGetCustomTokenRisk
from openapi_client.apis.paths.insights_sol_get_default_collection_risk import InsightsSolGetDefaultCollectionRisk
from openapi_client.apis.paths.insights_sol_get_default_token_risk import InsightsSolGetDefaultTokenRisk
from openapi_client.apis.paths.insights_sol_get_collection_forecasts import InsightsSolGetCollectionForecasts
from openapi_client.apis.paths.insights_sol_get_token_forecasts import InsightsSolGetTokenForecasts
from openapi_client.apis.paths.insights_sol_get_token_appraisal import InsightsSolGetTokenAppraisal
from openapi_client.apis.paths.insights_pol_get_custom_collection_risk import InsightsPolGetCustomCollectionRisk
from openapi_client.apis.paths.insights_pol_get_custom_token_risk import InsightsPolGetCustomTokenRisk
from openapi_client.apis.paths.insights_pol_get_default_collection_risk import InsightsPolGetDefaultCollectionRisk
from openapi_client.apis.paths.insights_pol_get_default_token_risk import InsightsPolGetDefaultTokenRisk
from openapi_client.apis.paths.insights_pol_get_collection_forecasts import InsightsPolGetCollectionForecasts
from openapi_client.apis.paths.insights_pol_get_token_forecasts import InsightsPolGetTokenForecasts
from openapi_client.apis.paths.insights_pol_get_token_appraisal import InsightsPolGetTokenAppraisal
from openapi_client.apis.paths.insights_pol_get_wallet_labels import InsightsPolGetWalletLabels

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DATA_ETH_GET_COLLECTIONS: DataEthGetCollections,
        PathValues.DATA_ETH_GET_TOKENS: DataEthGetTokens,
        PathValues.DATA_ETH_GET_COLLECTION_TRANSACTIONS: DataEthGetCollectionTransactions,
        PathValues.DATA_ETH_GET_TOKEN_TRANSACTIONS: DataEthGetTokenTransactions,
        PathValues.DATA_ETH_GET_MARKETPLACE_DATA: DataEthGetMarketplaceData,
        PathValues.DATA_ETH_GET_MARKETPLACE_TRAIT_DATA: DataEthGetMarketplaceTraitData,
        PathValues.DATA_ETH_GET_WALLET_NFTS: DataEthGetWalletNFTs,
        PathValues.DATA_ETH_GET_WALLET_TRANSACTIONS: DataEthGetWalletTransactions,
        PathValues.DATA_ETH_GET_HISTORICAL_TRANSACTIONS: DataEthGetHistoricalTransactions,
        PathValues.DATA_ETH_GET_HISTORICAL_EVENTS: DataEthGetHistoricalEvents,
        PathValues.DATA_ETH_GET_COLLECTION_OWNERS: DataEthGetCollectionOwners,
        PathValues.DATA_ETH_GET_MARKETPLACE_FLOOR_PRICE: DataEthGetMarketplaceFloorPrice,
        PathValues.DATA_ETH_GET_ENS_LOOKUP: DataEthGetEnsLookup,
        PathValues.DATA_SOL_GET_COLLECTIONS: DataSolGetCollections,
        PathValues.DATA_SOL_GET_TOKENS: DataSolGetTokens,
        PathValues.DATA_SOL_GET_COLLECTION_TRANSACTIONS: DataSolGetCollectionTransactions,
        PathValues.DATA_SOL_GET_TOKEN_TRANSACTIONS: DataSolGetTokenTransactions,
        PathValues.DATA_SOL_GET_ACCOUNT_NFTS: DataSolGetAccountNFTs,
        PathValues.DATA_SOL_GET_NFTACCOUNT: DataSolGetNFTAccount,
        PathValues.DATA_SOL_GET_MARKETPLACE_DATA: DataSolGetMarketplaceData,
        PathValues.DATA_SOL_GET_MARKETPLACE_TRAIT_DATA: DataSolGetMarketplaceTraitData,
        PathValues.DATA_SOL_GET_COLLECTION_TRAITS: DataSolGetCollectionTraits,
        PathValues.DATA_SOL_GET_HISTORICAL_TRANSACTIONS: DataSolGetHistoricalTransactions,
        PathValues.DATA_SOL_GET_MARKETPLACE_FLOOR_PRICE: DataSolGetMarketplaceFloorPrice,
        PathValues.DATA_POL_GET_COLLECTIONS: DataPolGetCollections,
        PathValues.DATA_POL_GET_COLLECTION_TRANSACTIONS: DataPolGetCollectionTransactions,
        PathValues.DATA_POL_GET_TOKEN_TRANSACTIONS: DataPolGetTokenTransactions,
        PathValues.DATA_POL_GET_TOKENS: DataPolGetTokens,
        PathValues.DATA_POL_GET_COLLECTION_TRAITS: DataPolGetCollectionTraits,
        PathValues.DATA_POL_GET_WALLET_NFTS: DataPolGetWalletNFTs,
        PathValues.DATA_POL_GET_COLLECTION_OWNERS: DataPolGetCollectionOwners,
        PathValues.DATA_POL_GET_MARKETPLACE_DATA: DataPolGetMarketplaceData,
        PathValues.DATA_POL_GET_MARKETPLACE_FLOOR_PRICE: DataPolGetMarketplaceFloorPrice,
        PathValues.DATA_POL_GET_WALLET_TRANSACTIONS: DataPolGetWalletTransactions,
        PathValues.DATA_POL_GET_HISTORICAL_TRANSACTIONS: DataPolGetHistoricalTransactions,
        PathValues.DATA_SKN_GET_MARKETPLACE_FLOOR_PRICE: DataSknGetMarketplaceFloorPrice,
        PathValues.DATA_SKN_GET_MARKETPLACE_DATA: DataSknGetMarketplaceData,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_SUMMARY: AnalyticsEthGetCollectionSummary,
        PathValues.ANALYTICS_ETH_GET_TOKEN_SUMMARY: AnalyticsEthGetTokenSummary,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_PRICE_DIFF: AnalyticsEthGetCollectionPriceDiff,
        PathValues.ANALYTICS_ETH_GET_WASH_TRANSACTIONS: AnalyticsEthGetWashTransactions,
        PathValues.ANALYTICS_ETH_GET_WASH_TRADE: AnalyticsEthGetWashTrade,
        PathValues.ANALYTICS_ETH_GET_RARITY: AnalyticsEthGetRarity,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_SALES_OHLC: AnalyticsEthGetCollectionSalesOHLC,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_FLOOR_PRICE_OHLC: AnalyticsEthGetCollectionFloorPriceOHLC,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_LISTINGS_OHLC: AnalyticsEthGetCollectionListingsOHLC,
        PathValues.ANALYTICS_ETH_GET_LEADER_BOARD: AnalyticsEthGetLeaderBoard,
        PathValues.ANALYTICS_SOL_GET_COLLECTION_SUMMARY: AnalyticsSolGetCollectionSummary,
        PathValues.ANALYTICS_SOL_GET_TOKEN_SUMMARY: AnalyticsSolGetTokenSummary,
        PathValues.ANALYTICS_SOL_GET_COLLECTION_PRICE_DIFF: AnalyticsSolGetCollectionPriceDiff,
        PathValues.ANALYTICS_SOL_GET_WASH_TRANSACTIONS: AnalyticsSolGetWashTransactions,
        PathValues.ANALYTICS_SOL_GET_WASH_TRADE: AnalyticsSolGetWashTrade,
        PathValues.ANALYTICS_SOL_GET_RARITY: AnalyticsSolGetRarity,
        PathValues.ANALYTICS_SOL_GET_COLLECTION_SALES_OHLC: AnalyticsSolGetCollectionSalesOHLC,
        PathValues.ANALYTICS_POL_GET_COLLECTION_SUMMARY: AnalyticsPolGetCollectionSummary,
        PathValues.ANALYTICS_POL_GET_TOKEN_SUMMARY: AnalyticsPolGetTokenSummary,
        PathValues.ANALYTICS_POL_GET_COLLECTION_PRICE_DIFF: AnalyticsPolGetCollectionPriceDiff,
        PathValues.ANALYTICS_POL_GET_WASH_TRANSACTIONS: AnalyticsPolGetWashTransactions,
        PathValues.ANALYTICS_POL_GET_WASH_TRADE: AnalyticsPolGetWashTrade,
        PathValues.ANALYTICS_POL_GET_RARITY: AnalyticsPolGetRarity,
        PathValues.ANALYTICS_POL_GET_COLLECTION_SALES_OHLC: AnalyticsPolGetCollectionSalesOHLC,
        PathValues.ANALYTICS_POL_GET_LEADER_BOARD: AnalyticsPolGetLeaderBoard,
        PathValues.INSIGHTS_ETH_GET_CUSTOM_COLLECTION_RISK: InsightsEthGetCustomCollectionRisk,
        PathValues.INSIGHTS_ETH_GET_CUSTOM_TOKEN_RISK: InsightsEthGetCustomTokenRisk,
        PathValues.INSIGHTS_ETH_GET_DEFAULT_COLLECTION_RISK: InsightsEthGetDefaultCollectionRisk,
        PathValues.INSIGHTS_ETH_GET_DEFAULT_TOKEN_RISK: InsightsEthGetDefaultTokenRisk,
        PathValues.INSIGHTS_ETH_GET_COLLECTION_FORECASTS: InsightsEthGetCollectionForecasts,
        PathValues.INSIGHTS_ETH_GET_TOKEN_FORECASTS: InsightsEthGetTokenForecasts,
        PathValues.INSIGHTS_ETH_GET_TOKEN_APPRAISAL: InsightsEthGetTokenAppraisal,
        PathValues.INSIGHTS_ETH_GET_WALLET_LABELS: InsightsEthGetWalletLabels,
        PathValues.INSIGHTS_SOL_GET_CUSTOM_COLLECTION_RISK: InsightsSolGetCustomCollectionRisk,
        PathValues.INSIGHTS_SOL_GET_CUSTOM_TOKEN_RISK: InsightsSolGetCustomTokenRisk,
        PathValues.INSIGHTS_SOL_GET_DEFAULT_COLLECTION_RISK: InsightsSolGetDefaultCollectionRisk,
        PathValues.INSIGHTS_SOL_GET_DEFAULT_TOKEN_RISK: InsightsSolGetDefaultTokenRisk,
        PathValues.INSIGHTS_SOL_GET_COLLECTION_FORECASTS: InsightsSolGetCollectionForecasts,
        PathValues.INSIGHTS_SOL_GET_TOKEN_FORECASTS: InsightsSolGetTokenForecasts,
        PathValues.INSIGHTS_SOL_GET_TOKEN_APPRAISAL: InsightsSolGetTokenAppraisal,
        PathValues.INSIGHTS_POL_GET_CUSTOM_COLLECTION_RISK: InsightsPolGetCustomCollectionRisk,
        PathValues.INSIGHTS_POL_GET_CUSTOM_TOKEN_RISK: InsightsPolGetCustomTokenRisk,
        PathValues.INSIGHTS_POL_GET_DEFAULT_COLLECTION_RISK: InsightsPolGetDefaultCollectionRisk,
        PathValues.INSIGHTS_POL_GET_DEFAULT_TOKEN_RISK: InsightsPolGetDefaultTokenRisk,
        PathValues.INSIGHTS_POL_GET_COLLECTION_FORECASTS: InsightsPolGetCollectionForecasts,
        PathValues.INSIGHTS_POL_GET_TOKEN_FORECASTS: InsightsPolGetTokenForecasts,
        PathValues.INSIGHTS_POL_GET_TOKEN_APPRAISAL: InsightsPolGetTokenAppraisal,
        PathValues.INSIGHTS_POL_GET_WALLET_LABELS: InsightsPolGetWalletLabels,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DATA_ETH_GET_COLLECTIONS: DataEthGetCollections,
        PathValues.DATA_ETH_GET_TOKENS: DataEthGetTokens,
        PathValues.DATA_ETH_GET_COLLECTION_TRANSACTIONS: DataEthGetCollectionTransactions,
        PathValues.DATA_ETH_GET_TOKEN_TRANSACTIONS: DataEthGetTokenTransactions,
        PathValues.DATA_ETH_GET_MARKETPLACE_DATA: DataEthGetMarketplaceData,
        PathValues.DATA_ETH_GET_MARKETPLACE_TRAIT_DATA: DataEthGetMarketplaceTraitData,
        PathValues.DATA_ETH_GET_WALLET_NFTS: DataEthGetWalletNFTs,
        PathValues.DATA_ETH_GET_WALLET_TRANSACTIONS: DataEthGetWalletTransactions,
        PathValues.DATA_ETH_GET_HISTORICAL_TRANSACTIONS: DataEthGetHistoricalTransactions,
        PathValues.DATA_ETH_GET_HISTORICAL_EVENTS: DataEthGetHistoricalEvents,
        PathValues.DATA_ETH_GET_COLLECTION_OWNERS: DataEthGetCollectionOwners,
        PathValues.DATA_ETH_GET_MARKETPLACE_FLOOR_PRICE: DataEthGetMarketplaceFloorPrice,
        PathValues.DATA_ETH_GET_ENS_LOOKUP: DataEthGetEnsLookup,
        PathValues.DATA_SOL_GET_COLLECTIONS: DataSolGetCollections,
        PathValues.DATA_SOL_GET_TOKENS: DataSolGetTokens,
        PathValues.DATA_SOL_GET_COLLECTION_TRANSACTIONS: DataSolGetCollectionTransactions,
        PathValues.DATA_SOL_GET_TOKEN_TRANSACTIONS: DataSolGetTokenTransactions,
        PathValues.DATA_SOL_GET_ACCOUNT_NFTS: DataSolGetAccountNFTs,
        PathValues.DATA_SOL_GET_NFTACCOUNT: DataSolGetNFTAccount,
        PathValues.DATA_SOL_GET_MARKETPLACE_DATA: DataSolGetMarketplaceData,
        PathValues.DATA_SOL_GET_MARKETPLACE_TRAIT_DATA: DataSolGetMarketplaceTraitData,
        PathValues.DATA_SOL_GET_COLLECTION_TRAITS: DataSolGetCollectionTraits,
        PathValues.DATA_SOL_GET_HISTORICAL_TRANSACTIONS: DataSolGetHistoricalTransactions,
        PathValues.DATA_SOL_GET_MARKETPLACE_FLOOR_PRICE: DataSolGetMarketplaceFloorPrice,
        PathValues.DATA_POL_GET_COLLECTIONS: DataPolGetCollections,
        PathValues.DATA_POL_GET_COLLECTION_TRANSACTIONS: DataPolGetCollectionTransactions,
        PathValues.DATA_POL_GET_TOKEN_TRANSACTIONS: DataPolGetTokenTransactions,
        PathValues.DATA_POL_GET_TOKENS: DataPolGetTokens,
        PathValues.DATA_POL_GET_COLLECTION_TRAITS: DataPolGetCollectionTraits,
        PathValues.DATA_POL_GET_WALLET_NFTS: DataPolGetWalletNFTs,
        PathValues.DATA_POL_GET_COLLECTION_OWNERS: DataPolGetCollectionOwners,
        PathValues.DATA_POL_GET_MARKETPLACE_DATA: DataPolGetMarketplaceData,
        PathValues.DATA_POL_GET_MARKETPLACE_FLOOR_PRICE: DataPolGetMarketplaceFloorPrice,
        PathValues.DATA_POL_GET_WALLET_TRANSACTIONS: DataPolGetWalletTransactions,
        PathValues.DATA_POL_GET_HISTORICAL_TRANSACTIONS: DataPolGetHistoricalTransactions,
        PathValues.DATA_SKN_GET_MARKETPLACE_FLOOR_PRICE: DataSknGetMarketplaceFloorPrice,
        PathValues.DATA_SKN_GET_MARKETPLACE_DATA: DataSknGetMarketplaceData,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_SUMMARY: AnalyticsEthGetCollectionSummary,
        PathValues.ANALYTICS_ETH_GET_TOKEN_SUMMARY: AnalyticsEthGetTokenSummary,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_PRICE_DIFF: AnalyticsEthGetCollectionPriceDiff,
        PathValues.ANALYTICS_ETH_GET_WASH_TRANSACTIONS: AnalyticsEthGetWashTransactions,
        PathValues.ANALYTICS_ETH_GET_WASH_TRADE: AnalyticsEthGetWashTrade,
        PathValues.ANALYTICS_ETH_GET_RARITY: AnalyticsEthGetRarity,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_SALES_OHLC: AnalyticsEthGetCollectionSalesOHLC,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_FLOOR_PRICE_OHLC: AnalyticsEthGetCollectionFloorPriceOHLC,
        PathValues.ANALYTICS_ETH_GET_COLLECTION_LISTINGS_OHLC: AnalyticsEthGetCollectionListingsOHLC,
        PathValues.ANALYTICS_ETH_GET_LEADER_BOARD: AnalyticsEthGetLeaderBoard,
        PathValues.ANALYTICS_SOL_GET_COLLECTION_SUMMARY: AnalyticsSolGetCollectionSummary,
        PathValues.ANALYTICS_SOL_GET_TOKEN_SUMMARY: AnalyticsSolGetTokenSummary,
        PathValues.ANALYTICS_SOL_GET_COLLECTION_PRICE_DIFF: AnalyticsSolGetCollectionPriceDiff,
        PathValues.ANALYTICS_SOL_GET_WASH_TRANSACTIONS: AnalyticsSolGetWashTransactions,
        PathValues.ANALYTICS_SOL_GET_WASH_TRADE: AnalyticsSolGetWashTrade,
        PathValues.ANALYTICS_SOL_GET_RARITY: AnalyticsSolGetRarity,
        PathValues.ANALYTICS_SOL_GET_COLLECTION_SALES_OHLC: AnalyticsSolGetCollectionSalesOHLC,
        PathValues.ANALYTICS_POL_GET_COLLECTION_SUMMARY: AnalyticsPolGetCollectionSummary,
        PathValues.ANALYTICS_POL_GET_TOKEN_SUMMARY: AnalyticsPolGetTokenSummary,
        PathValues.ANALYTICS_POL_GET_COLLECTION_PRICE_DIFF: AnalyticsPolGetCollectionPriceDiff,
        PathValues.ANALYTICS_POL_GET_WASH_TRANSACTIONS: AnalyticsPolGetWashTransactions,
        PathValues.ANALYTICS_POL_GET_WASH_TRADE: AnalyticsPolGetWashTrade,
        PathValues.ANALYTICS_POL_GET_RARITY: AnalyticsPolGetRarity,
        PathValues.ANALYTICS_POL_GET_COLLECTION_SALES_OHLC: AnalyticsPolGetCollectionSalesOHLC,
        PathValues.ANALYTICS_POL_GET_LEADER_BOARD: AnalyticsPolGetLeaderBoard,
        PathValues.INSIGHTS_ETH_GET_CUSTOM_COLLECTION_RISK: InsightsEthGetCustomCollectionRisk,
        PathValues.INSIGHTS_ETH_GET_CUSTOM_TOKEN_RISK: InsightsEthGetCustomTokenRisk,
        PathValues.INSIGHTS_ETH_GET_DEFAULT_COLLECTION_RISK: InsightsEthGetDefaultCollectionRisk,
        PathValues.INSIGHTS_ETH_GET_DEFAULT_TOKEN_RISK: InsightsEthGetDefaultTokenRisk,
        PathValues.INSIGHTS_ETH_GET_COLLECTION_FORECASTS: InsightsEthGetCollectionForecasts,
        PathValues.INSIGHTS_ETH_GET_TOKEN_FORECASTS: InsightsEthGetTokenForecasts,
        PathValues.INSIGHTS_ETH_GET_TOKEN_APPRAISAL: InsightsEthGetTokenAppraisal,
        PathValues.INSIGHTS_ETH_GET_WALLET_LABELS: InsightsEthGetWalletLabels,
        PathValues.INSIGHTS_SOL_GET_CUSTOM_COLLECTION_RISK: InsightsSolGetCustomCollectionRisk,
        PathValues.INSIGHTS_SOL_GET_CUSTOM_TOKEN_RISK: InsightsSolGetCustomTokenRisk,
        PathValues.INSIGHTS_SOL_GET_DEFAULT_COLLECTION_RISK: InsightsSolGetDefaultCollectionRisk,
        PathValues.INSIGHTS_SOL_GET_DEFAULT_TOKEN_RISK: InsightsSolGetDefaultTokenRisk,
        PathValues.INSIGHTS_SOL_GET_COLLECTION_FORECASTS: InsightsSolGetCollectionForecasts,
        PathValues.INSIGHTS_SOL_GET_TOKEN_FORECASTS: InsightsSolGetTokenForecasts,
        PathValues.INSIGHTS_SOL_GET_TOKEN_APPRAISAL: InsightsSolGetTokenAppraisal,
        PathValues.INSIGHTS_POL_GET_CUSTOM_COLLECTION_RISK: InsightsPolGetCustomCollectionRisk,
        PathValues.INSIGHTS_POL_GET_CUSTOM_TOKEN_RISK: InsightsPolGetCustomTokenRisk,
        PathValues.INSIGHTS_POL_GET_DEFAULT_COLLECTION_RISK: InsightsPolGetDefaultCollectionRisk,
        PathValues.INSIGHTS_POL_GET_DEFAULT_TOKEN_RISK: InsightsPolGetDefaultTokenRisk,
        PathValues.INSIGHTS_POL_GET_COLLECTION_FORECASTS: InsightsPolGetCollectionForecasts,
        PathValues.INSIGHTS_POL_GET_TOKEN_FORECASTS: InsightsPolGetTokenForecasts,
        PathValues.INSIGHTS_POL_GET_TOKEN_APPRAISAL: InsightsPolGetTokenAppraisal,
        PathValues.INSIGHTS_POL_GET_WALLET_LABELS: InsightsPolGetWalletLabels,
    }
)
