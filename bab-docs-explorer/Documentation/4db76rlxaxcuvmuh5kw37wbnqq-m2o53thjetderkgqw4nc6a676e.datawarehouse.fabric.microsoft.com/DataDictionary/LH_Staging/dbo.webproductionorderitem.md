# dbo.webproductionorderitem

**Database:** LH_Staging  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| ProductionOrderItemId | bigint | 8 | 1 |  |  |  |
| ProductionOrderItemWebCartOrderItemId | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemParentOrderItemId | int | 4 | 1 |  |  |  |
| ProductionOrderItemParentWebCartOrderItemId | varchar | 8000 | 1 |  |  |  |
| ProductionOrderId | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemSku | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemName | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemQuantity | int | 4 | 1 |  |  |  |
| ProductionOrderItemUnitPrice | decimal | 9 | 1 |  |  |  |
| ProductionOrderItemExtendedPrice | decimal | 9 | 1 |  |  |  |
| ProductionOrderItemFriendEyeColor | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemFriendFurColor | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemFriendGender | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemFriendHeight | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemFriendWeight | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemDepartment | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemClass | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemSubClass | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemNameMeName | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemNameMeBirthday | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemNameMeIsGift | bit | 1 | 1 |  |  |  |
| ProductionOrderItemRecipientGender | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemRecipientBirthday | datetime2 | 8 | 1 |  |  |  |
| ProductionOrderItemRecipientStateProvince | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemRecipientZipPostalCode | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemRecipientCountry | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemSenderGender | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemSenderBirthday | datetime2 | 8 | 1 |  |  |  |
| ProductionOrderItemSenderStateProvince | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemSenderZipPostalCode | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemSenderCountry | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemBuildASoundId | int | 4 | 1 |  |  |  |
| ProductionOrderItemBuildASoundPathAndFilename | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemGiftCardNumber | varchar | 8000 | 1 |  |  |  |
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
| ProductionOrderItemCommodityCode | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemCountryOfManufacture | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemIsKit | bit | 1 | 1 |  |  |  |
| ProductionOrderItemTinyImage | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemKitName | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemWebCartKitSKU | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemWebCartKitDisplayName | varchar | 8000 | 1 |  |  |  |
| ProductionOrderItemIsCar | bit | 1 | 1 |  |  |  |
| ProductionOrderItemSenderEmailOptIn | bit | 1 | 1 |  |  |  |
| ProductionOrderItemSenderMailOptIn | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsBearBill | bit | 1 | 1 |  |  |  |
| ProductionOrderItemIsVirtualItem | bit | 1 | 1 |  |  |  |
| ProductionOrderItemClubBabwSerialNumber | varchar | 8000 | 1 |  |  |  |
