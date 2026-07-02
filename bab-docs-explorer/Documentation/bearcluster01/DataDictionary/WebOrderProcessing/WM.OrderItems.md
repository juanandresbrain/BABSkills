# WM.OrderItems

**Database:** WebOrderProcessing  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderItemID | int | 4 | 0 | YES |  |  |
| OrderId | int | 4 | 0 | YES | YES |  |
| OrderId | int | 4 | 0 | YES | YES |  |
| sku | varchar | 50 | 0 |  |  |  |
| qty | int | 4 | 0 |  |  |  |
| ItemDescription | varchar | 100 | 1 |  |  |  |
| Price | money | 8 | 1 |  |  |  |
| DiscountedPrice | money | 8 | 1 |  |  |  |
| PreviousQTY | int | 4 | 1 |  |  |  |
| PreviousOriginalPrice | money | 8 | 1 |  |  |  |
| PreviousDiscountedPrice | money | 8 | 1 |  |  |  |
| GuestSatisfactionRefund | money | 8 | 1 |  |  |  |
| GiftCardNumber | varchar | 20 | 1 |  |  |  |
| Note | varchar | 50 | 1 |  |  |  |
| RecordYourVoiceOrder | varchar | 20 | 1 |  |  |  |
| EmbroideryCode | varchar | 32 | 1 |  |  |  |
| DateofBirth | datetime | 8 | 1 |  |  |  |
| FullName | nvarchar | 100 | 1 |  |  |  |
| Height | numeric | 9 | 1 |  |  |  |
| Weight | numeric | 9 | 1 |  |  |  |
| FurColor | varchar | 20 | 1 |  |  |  |
| EyeColor | varchar | 10 | 1 |  |  |  |
| BelongsTo | nvarchar | 100 | 1 |  |  |  |
| StuffedBy | nvarchar | 100 | 1 |  |  |  |
| idNum | varchar | 20 | 1 |  |  |  |
| tmpItemID | int | 4 | 1 |  |  |  |
| ParentItem | int | 4 | 1 |  | YES |  |
| ItemId | varchar | 20 | 1 |  |  |  |
| TrackingNumber | varchar | 30 | 1 |  |  |  |
| TransactionID | int | 4 | 1 |  | YES |  |

## Referenced By Stored Procedures

- [BABWOrderManagement: WM.RemoveOldTransactionData](../../StoredProcedures/BABWOrderManagement/WM.RemoveOldTransactionData.md)
- [WebOrderProcessing: dbo.spStoreforceBopis](../../StoredProcedures/WebOrderProcessing/dbo.spStoreforceBopis.md)
- [WebOrderProcessing: dbo.spUpdateOrderItemsRecordYourVoiceNumber](../../StoredProcedures/WebOrderProcessing/dbo.spUpdateOrderItemsRecordYourVoiceNumber.md)
- [WebOrderProcessing: WM.FlagCodosAndGiftBoxes](../../StoredProcedures/WebOrderProcessing/WM.FlagCodosAndGiftBoxes.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItemDiscounts_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItemDiscounts_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V3_1.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup_ForStorForce](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup_ForStorForce.md)
- [WebOrderProcessing: WM.spRptWebOrderLookupBACKUP20231012](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookupBACKUP20231012.md)
- [WebOrderProcessing: WM.spUpdateChannelAdvisorSets](../../StoredProcedures/WebOrderProcessing/WM.spUpdateChannelAdvisorSets.md)
- [WebOrderProcessing: WM.spWMPickticketXMLOnDemand](../../StoredProcedures/WebOrderProcessing/WM.spWMPickticketXMLOnDemand.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)

