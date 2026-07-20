# (SW) 2020RPT WHLSL OH

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 6ff55aef-0e2f-45e1-b717-8c3c42aa7100  
**Dataset ID:** fba3b349-79e8-41c0-9703-c90e9ddeef23  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/6ff55aef-0e2f-45e1-b717-8c3c42aa7100  
**Semantic Model:** [Merchandise Aggregate Semantic Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Aggregate Semantic Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["(SW) 2020RPT WHLSL OH"]
    product_dim_le_department(["product_dim_le.department"]) --> REPORT
    weeklyOnHandView_style_code(["weeklyOnHandView.style_code"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    productattributesummaryview_MSTAT(["productattributesummaryview.MSTAT"]) --> REPORT
    productattributesummaryview_KEYSTY(["productattributesummaryview.KEYSTY"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    product_dim_le_chain(["product_dim_le.chain"]) --> REPORT
    product_dim_le_class(["product_dim_le.class"]) --> REPORT
    Sum_weeklyOnHandView_on_hand_units_(["Sum(weeklyOnHandView.on_hand_units)"]) --> REPORT
    Sum_weeklyOnHandView_allocation_units_(["Sum(weeklyOnHandView.allocation_units)"]) --> REPORT
    d365LocationMapping_View_name(["d365LocationMapping_View.name"]) --> REPORT
    Sum_weeklyOnHandView_BOP_OH_Units_Inv_Status_Available___This_Period___(["Sum(weeklyOnHandView.BOP OH Units:Inv Status Available ( This Period ))"]) --> REPORT
    Sum_weeklyOnHandView_BOP_OH_Units_Inv_Status_Unavail_pending_shrink___This_Period___(["Sum(weeklyOnHandView.BOP OH Units:Inv Status Unavail:pending shrink ( This Period ))"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    weeklyOnHandView_actual_date(["weeklyOnHandView.actual_date"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| product_dim_le.department |
| weeklyOnHandView.style_code |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| productattributesummaryview.MSTAT |
| productattributesummaryview.KEYSTY |
| product_dim_le.style_desc |
| product_dim_le.chain |
| product_dim_le.class |
| Sum(weeklyOnHandView.on_hand_units) |
| Sum(weeklyOnHandView.allocation_units) |
| d365LocationMapping_View.name |
| Sum(weeklyOnHandView.BOP OH Units:Inv Status Available ( This Period )) |
| Sum(weeklyOnHandView.BOP OH Units:Inv Status Unavail:pending shrink ( This Period )) |
| d365LocationMapping_View.inventlocationid |
| date_dim.fiscal_year |
| date_dim.actual_date |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| weeklyOnHandView.actual_date |

## Pages

| Page | Visuals |
|---|---|
| (SW) 2020RPT WHLSL OH | 24 |

## Visuals

### (SW) 2020RPT WHLSL OH

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | product_dim_le.department |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 2c050ec017a6225d6f41 | slicer | weeklyOnHandView.style_code |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 826e14c9840c3793285e | unknown |  |
| 8d580b230200a1dd08d5 | slicer | productattributesummaryview.MSTAT |
| 91ab9d0a2ae72b60dce4 | slicer | productattributesummaryview.KEYSTY |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f23d5b55029a0991e0da | tableEx | weeklyOnHandView.style_code, product_dim_le.style_desc, product_dim_le.chain, product_dim_le.department, product_dim_le.class, Sum(weeklyOnHandView.on_hand_units), Sum(weeklyOnHandView.allocation_units), d365LocationMapping_View.name, productattributesummaryview.KEYSTY, productattributesummaryview.MSTAT, Sum(weeklyOnHandView.BOP OH Units:Inv Status Available ( This Period )), Sum(weeklyOnHandView.BOP OH Units:Inv Status Unavail:pending shrink ( This Period )), d365LocationMapping_View.inventlocationid |
| f920f4a3989b72fd51af | textbox |  |
| e8e740717323d0200f7a | slicer | product_dim_le.class |
| d986b5ee6dd8555a4031 | slicer | d365LocationMapping_View.inventlocationid |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| c5bb2e2d468b021899e9 | slicer | product_dim_le.chain |
| 9ea736d49b75db93980e | textbox |  |
| 9a7956cae86f44783ec2 | slicer | weeklyOnHandView.actual_date |
| 97f4659a5a12bc988c51 | image |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | d365LocationMapping_View.inventlocationid |
