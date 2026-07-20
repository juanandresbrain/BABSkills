# Planning and Allocation – Sounds Royalty Report – Ad Hoc

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 545f88ee-abd8-4696-aa89-32406522c5cb  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/545f88ee-abd8-4696-aa89-32406522c5cb  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Planning and Allocation – Sounds Royalty Report – Ad Hoc"]
    productattributesummaryview_LICEN(["productattributesummaryview.LICEN"]) --> REPORT
    RetailSalesTransactionLicensedView_jurisdiction_code(["RetailSalesTransactionLicensedView.jurisdiction_code"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    RetailSalesTransactionView_jurisdiction_code(["RetailSalesTransactionView.jurisdiction_code"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    productattributesummaryview_LICNSR(["productattributesummaryview.LICNSR"]) --> REPORT
    product_dim_le_subclass_code(["product_dim_le.subclass_code"]) --> REPORT
    product_dim_le_jurisdiction_code(["product_dim_le.jurisdiction_code"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    Sum_RetailSalesTransactionLicensedView_Gross_Sales_(["Sum(RetailSalesTransactionLicensedView.Gross Sales)"]) --> REPORT
    Sum_RetailSalesTransactionLicensedView_qty_(["Sum(RetailSalesTransactionLicensedView.qty)"]) --> REPORT
    Sum_RetailSalesTransactionLicensedView_Net_Sales_(["Sum(RetailSalesTransactionLicensedView.Net Sales)"]) --> REPORT
    Sum_RetailSalesTransactionLicensedView_discamount_(["Sum(RetailSalesTransactionLicensedView.discamount)"]) --> REPORT
    RetailSalesTransactionLicensedView_transdate(["RetailSalesTransactionLicensedView.transdate"]) --> REPORT
    RetailSalesTransactionLicensedView_subclass_code(["RetailSalesTransactionLicensedView.subclass_code"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| productattributesummaryview.LICEN |
| RetailSalesTransactionLicensedView.jurisdiction_code |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| RetailSalesTransactionView.jurisdiction_code |
| date_dim.actual_date |
| product_dim_le.style_code |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| d365LocationMapping_View.inventlocationid |
| productattributesummaryview.LICNSR |
| product_dim_le.subclass_code |
| product_dim_le.jurisdiction_code |
| product_dim_le.style_desc |
| Sum(RetailSalesTransactionLicensedView.Gross Sales) |
| Sum(RetailSalesTransactionLicensedView.qty) |
| Sum(RetailSalesTransactionLicensedView.Net Sales) |
| Sum(RetailSalesTransactionLicensedView.discamount) |
| RetailSalesTransactionLicensedView.transdate |
| RetailSalesTransactionLicensedView.subclass_code |

## Pages

| Page | Visuals |
|---|---|
| Sounds Royalty Report | 24 |

## Visuals

### Sounds Royalty Report

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | productattributesummaryview.LICEN |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 2c050ec017a6225d6f41 | slicer | RetailSalesTransactionLicensedView.jurisdiction_code |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 826e14c9840c3793285e | unknown |  |
| 8521e1935e2ddb44a772 | actionButton |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | RetailSalesTransactionView.jurisdiction_code |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| c5bb2e2d468b021899e9 | slicer | product_dim_le.style_code |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | slicer | d365LocationMapping_View.inventlocationid |
| e8e740717323d0200f7a | slicer | productattributesummaryview.LICNSR |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f079f02957fcbae49430 | slicer | product_dim_le.subclass_code |
| f23d5b55029a0991e0da | tableEx | d365LocationMapping_View.inventlocationid, product_dim_le.style_code, productattributesummaryview.LICEN, productattributesummaryview.LICNSR, product_dim_le.jurisdiction_code, product_dim_le.style_desc, Sum(RetailSalesTransactionLicensedView.Gross Sales), Sum(RetailSalesTransactionLicensedView.qty), Sum(RetailSalesTransactionLicensedView.Net Sales), Sum(RetailSalesTransactionLicensedView.discamount), RetailSalesTransactionLicensedView.transdate, RetailSalesTransactionLicensedView.subclass_code |
| f920f4a3989b72fd51af | textbox |  |
