# E-Commerce - Daily Inventory - Daily

**Workspace:** Enterprise Analytics Prod  
**Report ID:** 290f024b-33e2-4769-9508-eefd33a2f702  
**Dataset ID:** 45a1a956-440b-4517-9958-da0b9e2f26a6  
**Web URL:** https://app.powerbi.com/groups/ccdd9d66-24e9-48c6-a8d0-b71a2f03dff1/reports/290f024b-33e2-4769-9508-eefd33a2f702  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["E-Commerce - Daily Inventory - Daily"]
    Products_JurisdictionCode(["Products.JurisdictionCode"]) --> REPORT
    Products_Style(["Products.Style"]) --> REPORT
    Products_StyleDescription(["Products.StyleDescription"]) --> REPORT
    Products_Class(["Products.Class"]) --> REPORT
    Products_ClassCode(["Products.ClassCode"]) --> REPORT
    Products_KeyStory(["Products.KeyStory"]) --> REPORT
    Products_MSTAT(["Products.MSTAT"]) --> REPORT
    Products_WebActiveDate(["Products.WebActiveDate"]) --> REPORT
    Sum_DailyInventory_OrderMultiple_(["Sum(DailyInventory.OrderMultiple)"]) --> REPORT
    Sum_DailyInventory_EffectiveInv_(["Sum(DailyInventory.EffectiveInv)"]) --> REPORT
    DailyInventory_DaysSupply(["DailyInventory.DaysSupply"]) --> REPORT
    Sum_DailyInventory_AvailToDist_(["Sum(DailyInventory.AvailToDist)"]) --> REPORT
    DailyInventory_MTDSales(["DailyInventory.MTDSales"]) --> REPORT
    DailyInventory_MTDEnterpriseSales(["DailyInventory.MTDEnterpriseSales"]) --> REPORT
    DailyInventory_PWSales(["DailyInventory.PWSales"]) --> REPORT
    DailyInventory_PWEnterpriseSales(["DailyInventory.PWEnterpriseSales"]) --> REPORT
    DailyInventory_WTDSales(["DailyInventory.WTDSales"]) --> REPORT
    DailyInventory_WTDEnterpriseSales(["DailyInventory.WTDEnterpriseSales"]) --> REPORT
    DailyInventory_yesterdaysSales(["DailyInventory.yesterdaysSales"]) --> REPORT
    DailyInventory_YesterdayEnterpriseSales(["DailyInventory.YesterdayEnterpriseSales"]) --> REPORT
    Sum_DailyInventory_OnHand_(["Sum(DailyInventory.OnHand)"]) --> REPORT
    Sum_DailyInventory_Purchased_(["Sum(DailyInventory.Purchased)"]) --> REPORT
    Sum_DailyInventory_Allocated_(["Sum(DailyInventory.Allocated)"]) --> REPORT
    Sum_DailyInventory_InventoryBuffer_(["Sum(DailyInventory.InventoryBuffer)"]) --> REPORT
    NewDateDim_DescDate(["NewDateDim.DescDate"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| Products.JurisdictionCode |
| Products.Style |
| Products.StyleDescription |
| Products.Class |
| Products.ClassCode |
| Products.KeyStory |
| Products.MSTAT |
| Products.WebActiveDate |
| Sum(DailyInventory.OrderMultiple) |
| Sum(DailyInventory.EffectiveInv) |
| DailyInventory.DaysSupply |
| Sum(DailyInventory.AvailToDist) |
| DailyInventory.MTDSales |
| DailyInventory.MTDEnterpriseSales |
| DailyInventory.PWSales |
| DailyInventory.PWEnterpriseSales |
| DailyInventory.WTDSales |
| DailyInventory.WTDEnterpriseSales |
| DailyInventory.yesterdaysSales |
| DailyInventory.YesterdayEnterpriseSales |
| Sum(DailyInventory.OnHand) |
| Sum(DailyInventory.Purchased) |
| Sum(DailyInventory.Allocated) |
| Sum(DailyInventory.InventoryBuffer) |
| NewDateDim.DescDate |

## Pages

| Page | Visuals |
|---|---|
| Page 1 | 4 |

## Visuals

### Page 1

| Visual | Type | Fields |
|---|---|---|
| 6bc62b3124ea3cd4b9da | textbox |  |
| cffc7216258c282c7cbc | basicShape |  |
| 976997f5b1dcca9c8b1b | tableEx | Products.JurisdictionCode, Products.Style, Products.StyleDescription, Products.Class, Products.ClassCode, Products.KeyStory, Products.MSTAT, Products.WebActiveDate, Sum(DailyInventory.OrderMultiple), Sum(DailyInventory.EffectiveInv), DailyInventory.DaysSupply, Sum(DailyInventory.AvailToDist), DailyInventory.MTDSales, DailyInventory.MTDEnterpriseSales, DailyInventory.PWSales, DailyInventory.PWEnterpriseSales, DailyInventory.WTDSales, DailyInventory.WTDEnterpriseSales, DailyInventory.yesterdaysSales, DailyInventory.YesterdayEnterpriseSales, Sum(DailyInventory.OnHand), Sum(DailyInventory.Purchased), Sum(DailyInventory.Allocated), Sum(DailyInventory.InventoryBuffer) |
| 1f4faf530da3f7e76d5a | slicer | NewDateDim.DescDate |
