# 1 IB THE BIG DUMP

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 42275d39-6eff-4a07-b28a-590cf6566b60  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/42275d39-6eff-4a07-b28a-590cf6566b60  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["1 IB THE BIG DUMP"]
    product_dim_le_color_code(["product_dim_le.color_code"]) --> REPORT
    product_dim_le_LicensedCollection(["product_dim_le.LicensedCollection"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    productattributesummaryview_KEYSTY(["productattributesummaryview.KEYSTY"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    InventJourTransView_Inventory_Document_Number(["InventJourTransView.Inventory Document Number"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    product_dim_le_color_desc(["product_dim_le.color_desc"]) --> REPORT
    InventJourTransView_Inventory_Trans_Type_Code(["InventJourTransView.Inventory Trans Type Code"]) --> REPORT
    InventJourTransView_Inventory_Trans_Date(["InventJourTransView.Inventory Trans Date"]) --> REPORT
    InventJourTransView_Inventory_Trans_Type_Desc(["InventJourTransView.Inventory Trans Type Desc"]) --> REPORT
    Sum_InventJourTransView_InventoryTrans_Units_(["Sum(InventJourTransView.InventoryTrans Units)"]) --> REPORT
    Sum_InventJourTransView_Inventory_Trans_Cost_(["Sum(InventJourTransView.Inventory Trans Cost)"]) --> REPORT
    Sum_InventJourTransView_Inventory_Trans_Retail_(["Sum(InventJourTransView.Inventory Trans Retail)"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| product_dim_le.color_code |
| product_dim_le.LicensedCollection |
| product_dim_le.style_code |
| d365LocationMapping_View.inventlocationid |
| productattributesummaryview.KEYSTY |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| InventJourTransView.Inventory Document Number |
| date_dim.actual_date |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| product_dim_le.style_desc |
| product_dim_le.color_desc |
| InventJourTransView.Inventory Trans Type Code |
| InventJourTransView.Inventory Trans Date |
| InventJourTransView.Inventory Trans Type Desc |
| Sum(InventJourTransView.InventoryTrans Units) |
| Sum(InventJourTransView.Inventory Trans Cost) |
| Sum(InventJourTransView.Inventory Trans Retail) |

## Pages

| Page | Visuals |
|---|---|
| 1 IB THE BIG DUMP | 24 |

## Visuals

### 1 IB THE BIG DUMP

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | product_dim_le.color_code |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 22da671c0667f2a982ae | slicer | product_dim_le.LicensedCollection |
| 2c050ec017a6225d6f41 | slicer | product_dim_le.style_code |
| 2fe53e4e73dbaecc0854 | textFilter25A4896A83E0487089E2B90C9AE57C8A | d365LocationMapping_View.inventlocationid |
| 3edf860c41bfa20e56ed | slicer | productattributesummaryview.KEYSTY |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 7869095a179dc31dae86 | slicer | InventJourTransView.Inventory Document Number |
| 826e14c9840c3793285e | unknown |  |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | slicer | d365LocationMapping_View.inventlocationid |
| e0290b3bdcd982dcae6f | tableEx | product_dim_le.style_code, product_dim_le.style_desc, product_dim_le.color_code, product_dim_le.color_desc, InventJourTransView.Inventory Trans Type Code, InventJourTransView.Inventory Document Number, InventJourTransView.Inventory Trans Date, InventJourTransView.Inventory Trans Type Desc, Sum(InventJourTransView.InventoryTrans Units), Sum(InventJourTransView.Inventory Trans Cost), Sum(InventJourTransView.Inventory Trans Retail), d365LocationMapping_View.inventlocationid |
| e8e740717323d0200f7a | slicer | InventJourTransView.Inventory Trans Type Code |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f920f4a3989b72fd51af | textbox |  |
