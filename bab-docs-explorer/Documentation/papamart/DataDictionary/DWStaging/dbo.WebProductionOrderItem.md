# dbo.WebProductionOrderItem

**Database:** DWStaging  
**Server:** papamart  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductionOrderItemId | bigint | 8 | 1 |  |  |  |
| ProductionOrderItemWebCartOrderItemId | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemParentOrderItemId | int | 4 | 1 |  |  |  |
| ProductionOrderItemParentWebCartOrderItemId | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderId | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemSku | nvarchar | 64 | 1 |  |  |  |
| ProductionOrderItemName | nvarchar | 160 | 1 |  |  |  |
| ProductionOrderItemQuantity | int | 4 | 1 |  |  |  |
| ProductionOrderItemUnitPrice | money | 8 | 1 |  |  |  |
| ProductionOrderItemExtendedPrice | money | 8 | 1 |  |  |  |
| ProductionOrderItemFriendEyeColor | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemFriendFurColor | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemFriendGender | nvarchar | 32 | 1 |  |  |  |
| ProductionOrderItemFriendHeight | nvarchar | 32 | 1 |  |  |  |
| ProductionOrderItemFriendWeight | nvarchar | 32 | 1 |  |  |  |
| ProductionOrderItemDepartment | nvarchar | 64 | 1 |  |  |  |
| ProductionOrderItemClass | nvarchar | 64 | 1 |  |  |  |
| ProductionOrderItemSubClass | nvarchar | 64 | 1 |  |  |  |
| ProductionOrderItemNameMeName | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemNameMeBirthday | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderItemNameMeIsGift | bit | 1 | 1 |  |  |  |
| ProductionOrderItemRecipientGender | nvarchar | 32 | 1 |  |  |  |
| ProductionOrderItemRecipientBirthday | datetime | 8 | 1 |  |  |  |
| ProductionOrderItemRecipientStateProvince | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemRecipientZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderItemRecipientCountry | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemSenderGender | nvarchar | 32 | 1 |  |  |  |
| ProductionOrderItemSenderBirthday | datetime | 8 | 1 |  |  |  |
| ProductionOrderItemSenderStateProvince | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemSenderZipPostalCode | nvarchar | 40 | 1 |  |  |  |
| ProductionOrderItemSenderCountry | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemBuildASoundId | int | 4 | 1 |  |  |  |
| ProductionOrderItemBuildASoundPathAndFilename | nvarchar | 1000 | 1 |  |  |  |
| ProductionOrderItemGiftCardNumber | nvarchar | 64 | 1 |  |  |  |
| ProductionOrderItemGiftDollarAmount | int | 4 | 1 |  |  |  |
| ProductionOrderItemShipUnstuffed | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsBackordered | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsBuildASound | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsPreBuilt | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsSound | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsAnimal | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsPhysicalGiftCard | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsVirtualGiftCard | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsAccessory | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsDoll | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsEmbroidery | bit | 1 | 1 |  |  |  |
| ProductionOrderItemCommodityCode | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemCountryOfManufacture | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemIsKit | bit | 1 | 1 |  |  |  |
| ProductionOrderItemTinyImage | nvarchar | 510 | 1 |  |  |  |
| ProductionOrderItemKitName | nvarchar | 100 | 1 |  |  |  |
| ProductionOrderItemWebCartKitSKU | nvarchar | 510 | 1 |  |  |  |
| ProductionOrderItemWebCartKitDisplayName | nvarchar | 510 | 1 |  |  |  |
| ProductionOrderItemIsCar | bit | 1 | 1 |  |  |  |
| ProductionOrderItemSenderEmailOptIn | bit | 1 | 1 |  |  |  |
| ProductionOrderItemSenderMailOptIn | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsBearBill | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsVirtualItem | bit | 1 | 1 |  |  |  |
| ProductionOrderItemClubBabwSerialNumber | nvarchar | 40 | 1 |  |  |  |
