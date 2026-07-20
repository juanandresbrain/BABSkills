# CPT Raw Data (Saturday)

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 0ded7de0-851a-4388-98fc-2ad71b784ef5  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/0ded7de0-851a-4388-98fc-2ad71b784ef5  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["CPT Raw Data (Saturday)"]
    product_dim_le_department(["product_dim_le.department"]) --> REPORT
    productattributesummaryview_LICNSR(["productattributesummaryview.LICNSR"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    productattributesummaryview_KEYSTY(["productattributesummaryview.KEYSTY"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    product_dim_le_subclass(["product_dim_le.subclass"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    product_dim_le_InDate(["product_dim_le.InDate"]) --> REPORT
    productattributesummaryview_LICEN(["productattributesummaryview.LICEN"]) --> REPORT
    productattributesummaryview_MSTAT(["productattributesummaryview.MSTAT"]) --> REPORT
    productattributesummaryview_CCC(["productattributesummaryview.CCC"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    product_dim_le_class(["product_dim_le.class"]) --> REPORT
    product_dim_le_costprice(["product_dim_le.costprice"]) --> REPORT
    product_dim_le_primary_vendor_code(["product_dim_le.primary_vendor_code"]) --> REPORT
    productattributesummaryview_FACTRY(["productattributesummaryview.FACTRY"]) --> REPORT
    product_dim_le_OutDate(["product_dim_le.OutDate"]) --> REPORT
    Sum_product_dim_le_Style_Order_Multiple_(["Sum(product_dim_le.Style Order Multiple)"]) --> REPORT
    Sum_suntafretailreplenactivesettingsview_ordermultiple_(["Sum(suntafretailreplenactivesettingsview.ordermultiple)"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| product_dim_le.department |
| productattributesummaryview.LICNSR |
| product_dim_le.style_code |
| productattributesummaryview.KEYSTY |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| product_dim_le.subclass |
| date_dim.actual_date |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| d365LocationMapping_View.inventlocationid |
| product_dim_le.InDate |
| productattributesummaryview.LICEN |
| productattributesummaryview.MSTAT |
| productattributesummaryview.CCC |
| product_dim_le.style_desc |
| product_dim_le.class |
| product_dim_le.costprice |
| product_dim_le.primary_vendor_code |
| productattributesummaryview.FACTRY |
| product_dim_le.OutDate |
| Sum(product_dim_le.Style Order Multiple) |
| Sum(suntafretailreplenactivesettingsview.ordermultiple) |

## Pages

| Page | Visuals |
|---|---|
| CPT Raw Data (Saturday) | 24 |

## Visuals

### CPT Raw Data (Saturday)

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | product_dim_le.department |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 22da671c0667f2a982ae | slicer | productattributesummaryview.LICNSR |
| 2c050ec017a6225d6f41 | slicer | product_dim_le.style_code |
| 3edf860c41bfa20e56ed | slicer | productattributesummaryview.KEYSTY |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 7869095a179dc31dae86 | slicer | product_dim_le.subclass |
| 826e14c9840c3793285e | unknown |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | product_dim_le.style_code |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | textSlicer | d365LocationMapping_View.inventlocationid |
| e0290b3bdcd982dcae6f | tableEx | product_dim_le.subclass, product_dim_le.InDate, productattributesummaryview.LICEN, productattributesummaryview.LICNSR, productattributesummaryview.KEYSTY, productattributesummaryview.MSTAT, productattributesummaryview.CCC, product_dim_le.style_code, product_dim_le.style_desc, product_dim_le.department, product_dim_le.class, product_dim_le.costprice, product_dim_le.primary_vendor_code, productattributesummaryview.FACTRY, product_dim_le.OutDate, Sum(product_dim_le.Style Order Multiple), Sum(suntafretailreplenactivesettingsview.ordermultiple) |
| e8e740717323d0200f7a | slicer | product_dim_le.class |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f920f4a3989b72fd51af | textbox |  |
