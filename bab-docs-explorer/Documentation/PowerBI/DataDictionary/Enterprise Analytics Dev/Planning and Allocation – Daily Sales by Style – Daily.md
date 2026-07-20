# Planning and Allocation – Daily Sales by Style – Daily

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 1d254e84-27f0-4aa0-a4ea-e41e870f82d8  
**Dataset ID:** fba3b349-79e8-41c0-9703-c90e9ddeef23  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/1d254e84-27f0-4aa0-a4ea-e41e870f82d8  
**Semantic Model:** [Merchandise Aggregate Semantic Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Aggregate Semantic Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Planning and Allocation – Daily Sales by Style – Daily"]
    product_dim_le_department_code(["product_dim_le.department_code"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    PurchasingTransView_SubClass(["PurchasingTransView.SubClass"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    productattributesummaryview_LICNSR(["productattributesummaryview.LICNSR"]) --> REPORT
    product_dim_le_Department_Label(["product_dim_le.Department Label"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    WeeklySalesView_Net_Sales_Units(["WeeklySalesView.Net Sales Units"]) --> REPORT
    PurchasingTransView_Class(["PurchasingTransView.Class"]) --> REPORT
    product_dim_le_LegalEntity(["product_dim_le.LegalEntity"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    PurchasingTransView_Consumer_Group(["PurchasingTransView.Consumer Group"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| product_dim_le.department_code |
| product_dim_le.style_code |
| PurchasingTransView.SubClass |
| d365LocationMapping_View.inventlocationid |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| productattributesummaryview.LICNSR |
| product_dim_le.Department Label |
| product_dim_le.style_desc |
| WeeklySalesView.Net Sales Units |
| PurchasingTransView.Class |
| product_dim_le.LegalEntity |
| date_dim.fiscal_year |
| date_dim.actual_date |
| date_dim.fiscalQtr |
| date_dim.fiscalWk |
| date_dim.fiscalPer |
| PurchasingTransView.Consumer Group |

## Pages

| Page | Visuals |
|---|---|
| Daily Sales by Style | 25 |

## Visuals

### Daily Sales by Style

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | product_dim_le.department_code |
| 0b4140222c5f6ce0edbe | unknown |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | product_dim_le.style_code |
| 97f4659a5a12bc988c51 | image |  |
| f920f4a3989b72fd51af | textbox |  |
| 826e14c9840c3793285e | unknown |  |
| 7869095a179dc31dae86 | slicer | PurchasingTransView.SubClass |
| 72700f1eef3b47b6eaa3 | slicer | d365LocationMapping_View.inventlocationid |
| 6f0031da695b744bd74a | textbox |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 44b856414f1a82fa1972 | unknown |  |
| 3edf860c41bfa20e56ed | slicer | productattributesummaryview.LICNSR |
| f23d5b55029a0991e0da | tableEx | product_dim_le.Department Label, d365LocationMapping_View.inventlocationid, product_dim_le.department_code, product_dim_le.style_code, product_dim_le.style_desc, WeeklySalesView.Net Sales Units |
| ec739d70b14b7c06805a | actionButton |  |
| ebf4a2dc4872072b777f | unknown |  |
| e8e740717323d0200f7a | slicer | PurchasingTransView.Class |
| d986b5ee6dd8555a4031 | slicer | product_dim_le.LegalEntity |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalWk, date_dim.fiscalPer |
| c5bb2e2d468b021899e9 | slicer | PurchasingTransView.Consumer Group |
| 9ea736d49b75db93980e | textbox |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 2c050ec017a6225d6f41 | slicer | product_dim_le.style_code |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 0bcd43cda8b8c9272764 | textbox |  |
