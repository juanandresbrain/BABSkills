# Planning and Allocation – Wholesale Pricing and Cost Master Reference – Ad Hoc

**Workspace:** Enterprise Analytics Dev  
**Report ID:** e7a8e886-34c7-4d3e-8419-605bb66ad722  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/e7a8e886-34c7-4d3e-8419-605bb66ad722  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Planning and Allocation – Wholesale Pricing and Cost Master Reference – Ad Hoc"]
    product_dim_le_department_code(["product_dim_le.department_code"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    product_dim_le_jurisdiction_code(["product_dim_le.jurisdiction_code"]) --> REPORT
    Sum_product_dim_le_current_retail_(["Sum(product_dim_le.current_retail)"]) --> REPORT
    Sum_product_dim_le_Primary_Current_Cost_(["Sum(product_dim_le.Primary Current Cost)"]) --> REPORT
    product_dim_le_Department_Label(["product_dim_le.Department Label"]) --> REPORT
    product_dim_le_Class_Label(["product_dim_le.Class Label"]) --> REPORT
    product_dim_le_Sub_Class_Label(["product_dim_le.Sub-Class Label"]) --> REPORT
    product_dim_le_UPC(["product_dim_le.UPC"]) --> REPORT
    Sum_product_dim_le_babDistribMultiple_(["Sum(product_dim_le.babDistribMultiple)"]) --> REPORT
    product_dim_le_merch_status(["product_dim_le.merch_status"]) --> REPORT
    product_dim_le_KeyStory(["product_dim_le.KeyStory"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    productattributesummaryview_KEYSTY(["productattributesummaryview.KEYSTY"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| product_dim_le.department_code |
| product_dim_le.style_code |
| product_dim_le.style_desc |
| product_dim_le.jurisdiction_code |
| Sum(product_dim_le.current_retail) |
| Sum(product_dim_le.Primary Current Cost) |
| product_dim_le.Department Label |
| product_dim_le.Class Label |
| product_dim_le.Sub-Class Label |
| product_dim_le.UPC |
| Sum(product_dim_le.babDistribMultiple) |
| product_dim_le.merch_status |
| product_dim_le.KeyStory |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| productattributesummaryview.KEYSTY |
| date_dim.actual_date |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| d365LocationMapping_View.inventlocationid |

## Pages

| Page | Visuals |
|---|---|
| Wholesale Pricing and Cost Master Reference | 23 |

## Visuals

### Wholesale Pricing and Cost Master Reference

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | product_dim_le.department_code |
| 0b2093608127704ad689 | actionButton |  |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 2c050ec017a6225d6f41 | slicer | product_dim_le.style_code |
| 44b856414f1a82fa1972 | unknown |  |
| 45a73095a294cc7e5ad2 | tableEx | product_dim_le.style_code, product_dim_le.style_desc, product_dim_le.jurisdiction_code, Sum(product_dim_le.current_retail), Sum(product_dim_le.Primary Current Cost), product_dim_le.Department Label, product_dim_le.Class Label, product_dim_le.Sub-Class Label, product_dim_le.UPC, Sum(product_dim_le.babDistribMultiple), product_dim_le.merch_status, product_dim_le.KeyStory |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 7869095a179dc31dae86 | slicer | productattributesummaryview.KEYSTY |
| 826e14c9840c3793285e | unknown |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | product_dim_le.jurisdiction_code |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | textSlicer | d365LocationMapping_View.inventlocationid |
| e8e740717323d0200f7a | slicer | product_dim_le.jurisdiction_code |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f920f4a3989b72fd51af | textbox |  |
