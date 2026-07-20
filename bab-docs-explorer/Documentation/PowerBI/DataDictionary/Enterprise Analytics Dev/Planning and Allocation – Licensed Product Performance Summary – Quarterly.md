# Planning and Allocation – Licensed Product Performance Summary – Quarterly

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 753cc4b6-02a7-463a-b116-6eaaae15e190  
**Dataset ID:** fba3b349-79e8-41c0-9703-c90e9ddeef23  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/753cc4b6-02a7-463a-b116-6eaaae15e190  
**Semantic Model:** [Merchandise Aggregate Semantic Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Aggregate Semantic Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Planning and Allocation – Licensed Product Performance Summary – Quarterly"]
    product_dim_le_department_code(["product_dim_le.department_code"]) --> REPORT
    product_dim_le_LicensedCollection(["product_dim_le.LicensedCollection"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    productattributesummaryview_KEYSTY(["productattributesummaryview.KEYSTY"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    product_dim_le_Sub_Class_Label(["product_dim_le.Sub-Class Label"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    product_dim_le_concept_code(["product_dim_le.concept_code"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    d365LocationMapping_View_LocationCode(["d365LocationMapping_View.LocationCode"]) --> REPORT
    product_dim_le_Department_Label(["product_dim_le.Department Label"]) --> REPORT
    product_dim_le_Class_Label(["product_dim_le.Class Label"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    Sum_product_dim_le_costprice_(["Sum(product_dim_le.costprice)"]) --> REPORT
    PurchasingTransView_Style_Last_PO_Cost(["PurchasingTransView.Style Last PO Cost"]) --> REPORT
    product_dim_le_Style_Attribute_Set_Label_O_ROYALTY_STYLES(["product_dim_le.Style Attribute Set Label O ROYALTY STYLES"]) --> REPORT
    weeklyOnHandView_BOP_OH_Cost_Total___Quarter_01__(["weeklyOnHandView.BOP OH Cost:Total ( Quarter 01 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Cost_Total___Quarter_02__(["weeklyOnHandView.BOP OH Cost:Total ( Quarter 02 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Cost_Total___Quarter_03__(["weeklyOnHandView.BOP OH Cost:Total ( Quarter 03 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Cost_Total___Quarter_04__(["weeklyOnHandView.BOP OH Cost:Total ( Quarter 04 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Retail_Total___Quarter_01__(["weeklyOnHandView.BOP OH Retail:Total ( Quarter 01 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Retail_Total___Quarter_02__(["weeklyOnHandView.BOP OH Retail:Total ( Quarter 02 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Retail_Total___Quarter_03__(["weeklyOnHandView.BOP OH Retail:Total ( Quarter 03 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Retail_Total___Quarter_04__(["weeklyOnHandView.BOP OH Retail:Total ( Quarter 04 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Units_Total___Quarter_01__(["weeklyOnHandView.BOP OH Units:Total ( Quarter 01 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Units_Total___Quarter_02__(["weeklyOnHandView.BOP OH Units:Total ( Quarter 02 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Units_Total___Quarter_03__(["weeklyOnHandView.BOP OH Units:Total ( Quarter 03 )"]) --> REPORT
    weeklyOnHandView_BOP_OH_Units_Total___Quarter_04__(["weeklyOnHandView.BOP OH Units:Total ( Quarter 04 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Cost___Quarter_01__(["WeeklySalesView.Net Sales Cost ( Quarter 01 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Cost___Quarter_02__(["WeeklySalesView.Net Sales Cost ( Quarter 02 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Cost___Quarter_03__(["WeeklySalesView.Net Sales Cost ( Quarter 03 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Cost___Quarter_04__(["WeeklySalesView.Net Sales Cost ( Quarter 04 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Retail___Quarter_01__(["WeeklySalesView.Net Sales Retail ( Quarter 01 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Retail___Quarter_02__(["WeeklySalesView.Net Sales Retail ( Quarter 02 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Retail___Quarter_03__(["WeeklySalesView.Net Sales Retail ( Quarter 03 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Retail___Quarter_04__(["WeeklySalesView.Net Sales Retail ( Quarter 04 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Units___Quarter_01__(["WeeklySalesView.Net Sales Units ( Quarter 01 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Units___Quarter_02__(["WeeklySalesView.Net Sales Units ( Quarter 02 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Units___Quarter_03__(["WeeklySalesView.Net Sales Units ( Quarter 03 )"]) --> REPORT
    WeeklySalesView_Net_Sales_Units___Quarter_04__(["WeeklySalesView.Net Sales Units ( Quarter 04 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Cost___Quarter_01__(["WeeklySalesView.Net Receipts Cost ( Quarter 01 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Cost___Quarter_02__(["WeeklySalesView.Net Receipts Cost ( Quarter 02 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Cost___Quarter_03__(["WeeklySalesView.Net Receipts Cost ( Quarter 03 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Cost___Quarter_04__(["WeeklySalesView.Net Receipts Cost ( Quarter 04 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Retatil___Quarter_01__(["WeeklySalesView.Net Receipts Retatil ( Quarter 01 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Retatil___Quarter_02__(["WeeklySalesView.Net Receipts Retatil ( Quarter 02 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Retatil___Quarter_03__(["WeeklySalesView.Net Receipts Retatil ( Quarter 03 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Retatil___Quarter_04__(["WeeklySalesView.Net Receipts Retatil ( Quarter 04 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Units___Quarter_01__(["WeeklySalesView.Net Receipts Units ( Quarter 01 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Units___Quarter_02__(["WeeklySalesView.Net Receipts Units ( Quarter 02 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Units___Quarter_03__(["WeeklySalesView.Net Receipts Units ( Quarter 03 )"]) --> REPORT
    WeeklySalesView_Net_Receipts_Units___Quarter_04__(["WeeklySalesView.Net Receipts Units ( Quarter 04 )"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| product_dim_le.department_code |
| product_dim_le.LicensedCollection |
| product_dim_le.style_code |
| productattributesummaryview.KEYSTY |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| product_dim_le.Sub-Class Label |
| date_dim.actual_date |
| product_dim_le.concept_code |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| d365LocationMapping_View.LocationCode |
| product_dim_le.Department Label |
| product_dim_le.Class Label |
| product_dim_le.style_desc |
| Sum(product_dim_le.costprice) |
| PurchasingTransView.Style Last PO Cost |
| product_dim_le.Style Attribute Set Label O ROYALTY STYLES |
| weeklyOnHandView.BOP OH Cost:Total ( Quarter 01 ) |
| weeklyOnHandView.BOP OH Cost:Total ( Quarter 02 ) |
| weeklyOnHandView.BOP OH Cost:Total ( Quarter 03 ) |
| weeklyOnHandView.BOP OH Cost:Total ( Quarter 04 ) |
| weeklyOnHandView.BOP OH Retail:Total ( Quarter 01 ) |
| weeklyOnHandView.BOP OH Retail:Total ( Quarter 02 ) |
| weeklyOnHandView.BOP OH Retail:Total ( Quarter 03 ) |
| weeklyOnHandView.BOP OH Retail:Total ( Quarter 04 ) |
| weeklyOnHandView.BOP OH Units:Total ( Quarter 01 ) |
| weeklyOnHandView.BOP OH Units:Total ( Quarter 02 ) |
| weeklyOnHandView.BOP OH Units:Total ( Quarter 03 ) |
| weeklyOnHandView.BOP OH Units:Total ( Quarter 04 ) |
| WeeklySalesView.Net Sales Cost ( Quarter 01 ) |
| WeeklySalesView.Net Sales Cost ( Quarter 02 ) |
| WeeklySalesView.Net Sales Cost ( Quarter 03 ) |
| WeeklySalesView.Net Sales Cost ( Quarter 04 ) |
| WeeklySalesView.Net Sales Retail ( Quarter 01 ) |
| WeeklySalesView.Net Sales Retail ( Quarter 02 ) |
| WeeklySalesView.Net Sales Retail ( Quarter 03 ) |
| WeeklySalesView.Net Sales Retail ( Quarter 04 ) |
| WeeklySalesView.Net Sales Units ( Quarter 01 ) |
| WeeklySalesView.Net Sales Units ( Quarter 02 ) |
| WeeklySalesView.Net Sales Units ( Quarter 03 ) |
| WeeklySalesView.Net Sales Units ( Quarter 04 ) |
| WeeklySalesView.Net Receipts Cost ( Quarter 01 ) |
| WeeklySalesView.Net Receipts Cost ( Quarter 02 ) |
| WeeklySalesView.Net Receipts Cost ( Quarter 03 ) |
| WeeklySalesView.Net Receipts Cost ( Quarter 04 ) |
| WeeklySalesView.Net Receipts Retatil ( Quarter 01 ) |
| WeeklySalesView.Net Receipts Retatil ( Quarter 02 ) |
| WeeklySalesView.Net Receipts Retatil ( Quarter 03 ) |
| WeeklySalesView.Net Receipts Retatil ( Quarter 04 ) |
| WeeklySalesView.Net Receipts Units ( Quarter 01 ) |
| WeeklySalesView.Net Receipts Units ( Quarter 02 ) |
| WeeklySalesView.Net Receipts Units ( Quarter 03 ) |
| WeeklySalesView.Net Receipts Units ( Quarter 04 ) |

## Pages

| Page | Visuals |
|---|---|
| Licensed Product Performance Summary | 25 |

## Visuals

### Licensed Product Performance Summary

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | product_dim_le.department_code |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 22da671c0667f2a982ae | slicer | product_dim_le.LicensedCollection |
| 2c050ec017a6225d6f41 | slicer | product_dim_le.style_code |
| 2fe53e4e73dbaecc0854 | textFilter25A4896A83E0487089E2B90C9AE57C8A | product_dim_le.style_code |
| 3edf860c41bfa20e56ed | slicer | productattributesummaryview.KEYSTY |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 7869095a179dc31dae86 | slicer | product_dim_le.Sub-Class Label |
| 826e14c9840c3793285e | unknown |  |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| a99d9d223ab659bfe4dd | slicer | product_dim_le.concept_code |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | textSlicer | d365LocationMapping_View.LocationCode |
| e0290b3bdcd982dcae6f | tableEx | product_dim_le.department_code, product_dim_le.Department Label, product_dim_le.Class Label, product_dim_le.Sub-Class Label, product_dim_le.style_code, product_dim_le.style_desc, productattributesummaryview.KEYSTY, Sum(product_dim_le.costprice), PurchasingTransView.Style Last PO Cost, product_dim_le.Style Attribute Set Label O ROYALTY STYLES, weeklyOnHandView.BOP OH Cost:Total ( Quarter 01 ), weeklyOnHandView.BOP OH Cost:Total ( Quarter 02 ), weeklyOnHandView.BOP OH Cost:Total ( Quarter 03 ), weeklyOnHandView.BOP OH Cost:Total ( Quarter 04 ), weeklyOnHandView.BOP OH Retail:Total ( Quarter 01 ), weeklyOnHandView.BOP OH Retail:Total ( Quarter 02 ), weeklyOnHandView.BOP OH Retail:Total ( Quarter 03 ), weeklyOnHandView.BOP OH Retail:Total ( Quarter 04 ), weeklyOnHandView.BOP OH Units:Total ( Quarter 01 ), weeklyOnHandView.BOP OH Units:Total ( Quarter 02 ), weeklyOnHandView.BOP OH Units:Total ( Quarter 03 ), weeklyOnHandView.BOP OH Units:Total ( Quarter 04 ), WeeklySalesView.Net Sales Cost ( Quarter 01 ), WeeklySalesView.Net Sales Cost ( Quarter 02 ), WeeklySalesView.Net Sales Cost ( Quarter 03 ), WeeklySalesView.Net Sales Cost ( Quarter 04 ), WeeklySalesView.Net Sales Retail ( Quarter 01 ), WeeklySalesView.Net Sales Retail ( Quarter 02 ), WeeklySalesView.Net Sales Retail ( Quarter 03 ), WeeklySalesView.Net Sales Retail ( Quarter 04 ), WeeklySalesView.Net Sales Units ( Quarter 01 ), WeeklySalesView.Net Sales Units ( Quarter 02 ), WeeklySalesView.Net Sales Units ( Quarter 03 ), WeeklySalesView.Net Sales Units ( Quarter 04 ), WeeklySalesView.Net Receipts Cost ( Quarter 01 ), WeeklySalesView.Net Receipts Cost ( Quarter 02 ), WeeklySalesView.Net Receipts Cost ( Quarter 03 ), WeeklySalesView.Net Receipts Cost ( Quarter 04 ), WeeklySalesView.Net Receipts Retatil ( Quarter 01 ), WeeklySalesView.Net Receipts Retatil ( Quarter 02 ), WeeklySalesView.Net Receipts Retatil ( Quarter 03 ), WeeklySalesView.Net Receipts Retatil ( Quarter 04 ), WeeklySalesView.Net Receipts Units ( Quarter 01 ), WeeklySalesView.Net Receipts Units ( Quarter 02 ), WeeklySalesView.Net Receipts Units ( Quarter 03 ), WeeklySalesView.Net Receipts Units ( Quarter 04 ) |
| e8e740717323d0200f7a | slicer | product_dim_le.Class Label |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f920f4a3989b72fd51af | textbox |  |
