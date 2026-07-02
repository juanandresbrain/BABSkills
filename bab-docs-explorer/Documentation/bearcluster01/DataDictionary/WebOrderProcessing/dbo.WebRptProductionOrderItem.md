# dbo.WebRptProductionOrderItem

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductionOrderItemId | bigint | 8 | 0 |  |  |  |
| ProductionOrderItemWebCartOrderItemId | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemParentWebCartOrderItemId | int | 4 | 1 |  |  |  |
| ProductionOrderId | int | 4 | 0 |  |  |  |
| ProductionOrderItemSku | nvarchar | 64 | 1 |  |  |  |
| StyleCode | varchar | 50 | 0 |  |  |  |
| ProductionOrderItemName | nvarchar | 160 | 1 |  |  |  |
| ProductionOrderItemWebCartKitDisplayName | nvarchar | 160 | 1 |  |  |  |
| ProductionOrderItemQuantity | int | 4 | 0 |  |  |  |
| ProductionOrderItemUnitPrice | money | 8 | 1 |  |  |  |
| ProductionOrderItemExtendedPrice | money | 8 | 1 |  |  |  |
| ProductionOrderItemFriendEyeColor | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemFriendFurColor | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemFriendHeight | numeric | 9 | 1 |  |  |  |
| ProductionOrderItemFriendWeight | numeric | 9 | 1 |  |  |  |
| ProductionOrderItemNameMeName | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemNameMeBirthday | datetime | 8 | 1 |  |  |  |
| ProductionOrderItemNameMeIsGift | int | 4 | 0 |  |  |  |
| ProductionOrderItemRecipientStateProvince | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemRecipientZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderItemRecipientCountry | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemSenderStateProvince | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemSenderZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderItemSenderCountry | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemBuildASoundId | varchar | 20 | 1 |  |  |  |
| ProductionOrderItemIsBuildASound | int | 4 | 0 |  |  |  |
| ProductionOrderItemIsKit | int | 4 | 0 |  |  |  |

