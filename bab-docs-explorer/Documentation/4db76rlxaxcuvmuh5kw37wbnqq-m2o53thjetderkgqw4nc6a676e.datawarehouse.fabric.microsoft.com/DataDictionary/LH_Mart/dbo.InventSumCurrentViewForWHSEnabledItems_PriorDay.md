# dbo.InventSumCurrentViewForWHSEnabledItems_PriorDay

**Database:** LH_Mart  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Columns

| Column | Type | Max Length | Nullable | PK | FK | Description |
|---|---|---|---|---|---|---|
| LocationKey | varchar | 8000 | 1 |  |  |  |
| product_key | varchar | 8000 | 1 |  |  |  |
| dataareaid | varchar | 8000 | 1 |  |  |  |
| inventsiteid | varchar | 8000 | 1 |  |  |  |
| inventlocationid | varchar | 8000 | 1 |  |  |  |
| inventstatusid | varchar | 8000 | 1 |  |  |  |
| itemid | varchar | 8000 | 1 |  |  |  |
| AvailablePhysicalCalculated | decimal | 17 | 1 |  |  |  |
| Available to Distribute | decimal | 17 | 1 |  |  |  |
| AllocationUnit | decimal | 17 | 1 |  |  |  |
| onorder | decimal | 17 | 1 |  |  |  |
| lastupddateexpected | varchar | 8000 | 1 |  |  |  |
| AVAIL + INTRANS | decimal | 17 | 1 |  |  |  |
| CUR AVAI O/H | decimal | 17 | 1 |  |  |  |
| CUR AVAI O/H Sellable | decimal | 17 | 1 |  |  |  |
| CUR AVAI O/H Non-Sellable | decimal | 17 | 1 |  |  |  |
| InTr Qty | decimal | 17 | 1 |  |  |  |
| arrived | decimal | 17 | 1 |  |  |  |
| availordered | decimal | 17 | 1 |  |  |  |
| availphysical | decimal | 17 | 1 |  |  |  |
| deducted | decimal | 17 | 1 |  |  |  |
| ordered | decimal | 17 | 1 |  |  |  |
| physicalinvent | decimal | 17 | 1 |  |  |  |
| picked | decimal | 17 | 1 |  |  |  |
| postedqty | decimal | 17 | 1 |  |  |  |
| quotationissue | decimal | 17 | 1 |  |  |  |
| quotationreceipt | decimal | 17 | 1 |  |  |  |
| received | decimal | 17 | 1 |  |  |  |
| registered | decimal | 17 | 1 |  |  |  |
| reservordered | decimal | 17 | 1 |  |  |  |
| reservphysical | decimal | 17 | 1 |  |  |  |
| CreatedNotShippedQty | decimal | 17 | 1 |  |  |  |
| ShippedNotReceivedQty | decimal | 17 | 1 |  |  |  |
| SO On Order | decimal | 17 | 1 |  |  |  |
| PO Ordered | decimal | 17 | 1 |  |  |  |
| CurrentWeekSales | decimal | 17 | 1 |  |  |  |
| CUR AVAI O/H Prior Day | decimal | 17 | 1 |  |  |  |
| Next Ordered Quantity | decimal | 17 | 1 |  |  |  |
| Next Ordered Date | date | 3 | 1 |  |  |  |
| intransit_units | decimal | 17 | 1 |  |  |  |
| on_hand_unit_cost | decimal | 17 | 1 |  |  |  |
