# Finance – Receipt Cost Analysis – Ad Hoc

**Workspace:** Enterprise Analytics Dev  
**Report ID:** fe362010-8691-4c91-af13-9d6dec49c2b2  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/fe362010-8691-4c91-af13-9d6dec49c2b2  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Finance – Receipt Cost Analysis – Ad Hoc"]
    PurchasingTransView_Department(["PurchasingTransView.Department"]) --> REPORT
    product_dim_le_LicensedCollection(["product_dim_le.LicensedCollection"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    PurchasingTransView_Vendor_Purch_Name(["PurchasingTransView.Vendor Purch Name"]) --> REPORT
    PurchasingTransView_PO_number(["PurchasingTransView.PO number"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    PurchasingTransView_Short_Desciption(["PurchasingTransView.Short Desciption"]) --> REPORT
    Sum_PurchasingTransView_on_order_units_(["Sum(PurchasingTransView.on order units)"]) --> REPORT
    Sum_PurchasingTransView_units_received_(["Sum(PurchasingTransView.units received)"]) --> REPORT
    PurchasingTransView_Receipt_number(["PurchasingTransView.Receipt number"]) --> REPORT
    PurchasingTransView_Receipt_Date(["PurchasingTransView.Receipt Date"]) --> REPORT
    Sum_PurchasingTransView_Cost_(["Sum(PurchasingTransView.Cost)"]) --> REPORT
    Sum_PurchasingTransView_X_Cost_(["Sum(PurchasingTransView.X-Cost)"]) --> REPORT
    product_dim_le_MDSE_Supply(["product_dim_le.MDSE\Supply"]) --> REPORT
    Sum_PurchasingTransView_first_cost_(["Sum(PurchasingTransView.first cost)"]) --> REPORT
    PurchasingTransView_Received_Cost_W_o_Charge_by_Receipt_Date(["PurchasingTransView.Received Cost W/o Charge by Receipt Date"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| PurchasingTransView.Department |
| product_dim_le.LicensedCollection |
| product_dim_le.style_code |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| PurchasingTransView.Vendor Purch Name |
| PurchasingTransView.PO number |
| date_dim.actual_date |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| d365LocationMapping_View.inventlocationid |
| PurchasingTransView.Short Desciption |
| Sum(PurchasingTransView.on order units) |
| Sum(PurchasingTransView.units received) |
| PurchasingTransView.Receipt number |
| PurchasingTransView.Receipt Date |
| Sum(PurchasingTransView.Cost) |
| Sum(PurchasingTransView.X-Cost) |
| product_dim_le.MDSE\Supply |
| Sum(PurchasingTransView.first cost) |
| PurchasingTransView.Received Cost W/o Charge by Receipt Date |

## Pages

| Page | Visuals |
|---|---|
| Receipt Cost Analysis | 23 |

## Visuals

### Receipt Cost Analysis

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | PurchasingTransView.Department |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 22da671c0667f2a982ae | slicer | product_dim_le.LicensedCollection |
| 2c050ec017a6225d6f41 | slicer | product_dim_le.style_code |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 7869095a179dc31dae86 | slicer | PurchasingTransView.Vendor Purch Name |
| 826e14c9840c3793285e | unknown |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | PurchasingTransView.PO number |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | slicer | d365LocationMapping_View.inventlocationid |
| e0290b3bdcd982dcae6f | tableEx | PurchasingTransView.PO number, PurchasingTransView.Department, PurchasingTransView.Short Desciption, Sum(PurchasingTransView.on order units), Sum(PurchasingTransView.units received), PurchasingTransView.Vendor Purch Name, PurchasingTransView.Receipt number, PurchasingTransView.Receipt Date, Sum(PurchasingTransView.Cost), Sum(PurchasingTransView.X-Cost), product_dim_le.style_code, d365LocationMapping_View.inventlocationid, product_dim_le.MDSE\Supply, Sum(PurchasingTransView.first cost), PurchasingTransView.Received Cost W/o Charge by Receipt Date |
| e8e740717323d0200f7a | slicer | PurchasingTransView.Receipt number |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f920f4a3989b72fd51af | textbox |  |
