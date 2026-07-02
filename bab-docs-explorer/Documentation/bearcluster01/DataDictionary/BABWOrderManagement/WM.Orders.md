# WM.Orders

**Database:** BABWOrderManagement  
**Server:** bearcluster01  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| OrderId | int | 4 | 0 | YES |  |  |
| TransactionID | int | 4 | 0 |  |  |  |
| OrderNum | varchar | 10 | 0 |  |  |  |
| EnterpriseSellingID | varchar | 20 | 1 |  |  |  |
| OrderDate | datetime | 8 | 0 |  |  |  |
| OrderStatus | varchar | 20 | 0 |  |  |  |
| OrderType | varchar | 3 | 1 |  |  |  |
| PickupStore | varchar | 4 | 1 |  |  |  |
| OrderAuthentication | varchar | 100 | 1 |  |  |  |
| SourceSite | varchar | 7 | 1 |  |  |  |
| BatchNo | int | 4 | 1 |  |  |  |
| SequenceNo | int | 4 | 1 |  |  |  |
| DatePrinted | datetime | 8 | 0 |  |  |  |
| HouseOrder | bit | 1 | 1 |  |  |  |
| HouseOrderReason | varchar | 20 | 1 |  |  |  |
| GiftSender | varchar | 30 | 1 |  |  |  |
| GiftMessage | varchar | 300 | 1 |  |  |  |
| SpecialInstructions | varchar | 4000 | 1 |  |  |  |
| ServiceRep | varchar | 5 | 1 |  |  |  |
| BillToFName | varchar | 20 | 1 |  |  |  |
| BillToLName | varchar | 50 | 1 |  |  |  |
| BillToAddress1 | varchar | 100 | 1 |  |  |  |
| BillToAddress2 | varchar | 100 | 1 |  |  |  |
| BillToCity | varchar | 50 | 1 |  |  |  |
| BillToState | varchar | 50 | 1 |  |  |  |
| BillToPostalCode | varchar | 20 | 0 |  |  |  |
| BillToCountry | varchar | 30 | 1 |  |  |  |
| BillToPhone | varchar | 20 | 0 |  |  |  |
| BillToEmail | varchar | 100 | 1 |  |  |  |
| ShipToFName | varchar | 20 | 1 |  |  |  |
| ShipToLName | varchar | 50 | 1 |  |  |  |
| ShipToAddress1 | varchar | 100 | 1 |  |  |  |
| ShipToAddress2 | varchar | 100 | 1 |  |  |  |
| ShipToCity | varchar | 50 | 1 |  |  |  |
| ShipToState | varchar | 50 | 1 |  |  |  |
| ShipToPostalCode | varchar | 20 | 0 |  |  |  |
| ShipToCountry | varchar | 30 | 1 |  |  |  |
| ShipToPhone | varchar | 20 | 0 |  |  |  |
| ShipToEmail | varchar | 100 | 1 |  |  |  |
| ShippingAmount | money | 8 | 1 |  |  |  |
| ShippingMethod | varchar | 20 | 1 |  |  |  |
| PickTicketFlag | bit | 1 | 1 |  |  |  |
| OrderNumber | varchar | 10 | 1 |  |  |  |
| ShipmentNumber | varchar | 10 | 1 |  |  |  |

## Referenced By Stored Procedures

- [BABWOrderManagement: WM.RemoveOldTransactionData](../../StoredProcedures/BABWOrderManagement/WM.RemoveOldTransactionData.md)
- [BABWOrderManagement: WM.WareHouseQAapp_sp_GetOrder_V2](../../StoredProcedures/BABWOrderManagement/WM.WareHouseQAapp_sp_GetOrder_V2.md)
- [BABWOrderManagement: WM.WareHouseQAapp_sp_GetOrder_V3](../../StoredProcedures/BABWOrderManagement/WM.WareHouseQAapp_sp_GetOrder_V3.md)
- [WebOrderProcessing: ComHub.spGenerateCommHubCostcoConfirmations](../../StoredProcedures/WebOrderProcessing/ComHub.spGenerateCommHubCostcoConfirmations.md)
- [WebOrderProcessing: dbo.spBabDynamics0_BuildTargetTransactionsTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics0_BuildTargetTransactionsTable.md)
- [WebOrderProcessing: dbo.spBabDynamics5_BuildTenderStagingTable](../../StoredProcedures/WebOrderProcessing/dbo.spBabDynamics5_BuildTenderStagingTable.md)
- [WebOrderProcessing: dbo.spStoreforceBopis](../../StoredProcedures/WebOrderProcessing/dbo.spStoreforceBopis.md)
- [WebOrderProcessing: dbo.spUpdateOrderItemsRecordYourVoiceNumber](../../StoredProcedures/WebOrderProcessing/dbo.spUpdateOrderItemsRecordYourVoiceNumber.md)
- [WebOrderProcessing: WM.FlagCodosAndGiftBoxes](../../StoredProcedures/WebOrderProcessing/WM.FlagCodosAndGiftBoxes.md)
- [WebOrderProcessing: WM.spGetESUpdateOrderStatus](../../StoredProcedures/WebOrderProcessing/WM.spGetESUpdateOrderStatus.md)
- [WebOrderProcessing: WM.spGetPreviousWMOrderItemDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetPreviousWMOrderItemDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetReturnWMOrderPayments](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrderPayments.md)
- [WebOrderProcessing: WM.spGetReturnWMOrderPayments_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrderPayments_V2.md)
- [WebOrderProcessing: WM.spGetReturnWMOrderPayments_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrderPayments_V3.md)
- [WebOrderProcessing: WM.spGetReturnWMOrderPayments_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrderPayments_V3_1.md)
- [WebOrderProcessing: WM.spGetReturnWMOrderPayments_V3_1_BJB20210608](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrderPayments_V3_1_BJB20210608.md)
- [WebOrderProcessing: WM.spGetReturnWMOrderPayments_V3_2](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrderPayments_V3_2.md)
- [WebOrderProcessing: WM.spGetReturnWMOrdersTaxes_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetReturnWMOrdersTaxes_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderItems_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderItems_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments_V3_1](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments_V3_1.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments_V3_1_BJB2010608](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments_V3_1_BJB2010608.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments_V3_2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments_V3_2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderPayments_V3_2_BJB20250906](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderPayments_V3_2_BJB20250906.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrders_V2_BJB20200430](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrders_V2_BJB20200430.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderShippingDiscounts](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShippingDiscounts.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderShippingDiscounts_V2](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShippingDiscounts_V2.md)
- [WebOrderProcessing: WM.spGetShippedWMOrderShippingDiscounts_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrderShippingDiscounts_V3.md)
- [WebOrderProcessing: WM.spGetShippedWMOrdersTaxes_V3](../../StoredProcedures/WebOrderProcessing/WM.spGetShippedWMOrdersTaxes_V3.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup.md)
- [WebOrderProcessing: WM.spRptWebOrderLookup_ForStorForce](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookup_ForStorForce.md)
- [WebOrderProcessing: WM.spRptWebOrderLookupBACKUP20231012](../../StoredProcedures/WebOrderProcessing/WM.spRptWebOrderLookupBACKUP20231012.md)
- [WebOrderProcessing: WM.spUKUpdateOrdersToShipped](../../StoredProcedures/WebOrderProcessing/WM.spUKUpdateOrdersToShipped.md)
- [WebOrderProcessing: WM.spUpdateBrokenInStoreFulfillmentOrders](../../StoredProcedures/WebOrderProcessing/WM.spUpdateBrokenInStoreFulfillmentOrders.md)
- [WebOrderProcessing: WM.spUpdateChannelAdvisorSets](../../StoredProcedures/WebOrderProcessing/WM.spUpdateChannelAdvisorSets.md)
- [WebOrderProcessing: WM.spUpdateWMOrderStatus_to_SalesAuditComplete](../../StoredProcedures/WebOrderProcessing/WM.spUpdateWMOrderStatus_to_SalesAuditComplete.md)
- [WebOrderProcessing: WM.spWMPickticketXMLOnDemand](../../StoredProcedures/WebOrderProcessing/WM.spWMPickticketXMLOnDemand.md)
- [BABWPartyPlanner_Restore: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner_Restore: dbo.spLoadOrderIdForPartyESOrder](../../StoredProcedures/BABWPartyPlanner_Restore/dbo.spLoadOrderIdForPartyESOrder.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20190228](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20190228.md)
- [BABWPartyPlanner: dbo.sp_GetBookedPartiesByPartyID_BJB20240611](../../StoredProcedures/BABWPartyPlanner/dbo.sp_GetBookedPartiesByPartyID_BJB20240611.md)
- [BABWPartyPlanner: dbo.spLoadOrderIdForPartyESOrder](../../StoredProcedures/BABWPartyPlanner/dbo.spLoadOrderIdForPartyESOrder.md)

