# DynamicsGiftCardLineDiscountsMissing

**Workspace:** BI-Accounting  
**Report ID:** b11220c9-2d7a-46e7-ac49-e0792d9cbcf6  
**Dataset ID:** acf7ca8d-8471-4806-84ee-be32bc475d26  
**Web URL:** https://app.powerbi.com/groups/e996caff-15ec-41d5-ae2b-cc9137531fb6/reports/b11220c9-2d7a-46e7-ac49-e0792d9cbcf6  
**Semantic Model:** [DynamicsGiftCardLineDiscountsMissing](../../SemanticModels/BI-Accounting/DynamicsGiftCardLineDiscountsMissing.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["DynamicsGiftCardLineDiscountsMissing"]
    Azure_vwDynamicsGiftCardLineDiscountsMissing_Entity(["Azure vwDynamicsGiftCardLineDiscountsMissing.Entity"]) --> REPORT
    Azure_vwDynamicsGiftCardLineDiscountsMissing_TransDate(["Azure vwDynamicsGiftCardLineDiscountsMissing.TransDate"]) --> REPORT
    Azure_vwDynamicsGiftCardLineDiscountsMissing_InventLocationId(["Azure vwDynamicsGiftCardLineDiscountsMissing.InventLocationId"]) --> REPORT
    Sum_Azure_vwDynamicsGiftCardLineDiscountsMissing_GiftCardLineDiscMissingAmt_(["Sum(Azure vwDynamicsGiftCardLineDiscountsMissing.GiftCardLineDiscMissingAmt)"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| Azure vwDynamicsGiftCardLineDiscountsMissing.Entity |
| Azure vwDynamicsGiftCardLineDiscountsMissing.TransDate |
| Azure vwDynamicsGiftCardLineDiscountsMissing.InventLocationId |
| Sum(Azure vwDynamicsGiftCardLineDiscountsMissing.GiftCardLineDiscMissingAmt) |

## Pages

| Page | Visuals |
|---|---|
| Page 1 | 4 |

## Visuals

### Page 1

| Visual | Type | Fields |
|---|---|---|
| 216890114a02bc36b754 | tableEx | Azure vwDynamicsGiftCardLineDiscountsMissing.Entity, Azure vwDynamicsGiftCardLineDiscountsMissing.TransDate, Azure vwDynamicsGiftCardLineDiscountsMissing.InventLocationId, Sum(Azure vwDynamicsGiftCardLineDiscountsMissing.GiftCardLineDiscMissingAmt) |
| 3a5d9809841c20875442 | slicer | Azure vwDynamicsGiftCardLineDiscountsMissing.Entity |
| d69279411b7adecde99e | slicer | Azure vwDynamicsGiftCardLineDiscountsMissing.InventLocationId |
| 4c587833086e9bc550c4 | slicer | Azure vwDynamicsGiftCardLineDiscountsMissing.TransDate |
