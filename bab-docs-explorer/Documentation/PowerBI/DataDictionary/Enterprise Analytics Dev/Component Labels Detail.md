# Component Labels Detail

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 48052822-6679-408a-bb7e-0af45f87e375  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/48052822-6679-408a-bb7e-0af45f87e375  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Component Labels Detail"]
    ComponentSummaryView_SL_Component_Label(["ComponentSummaryView.SL_Component_Label"]) --> REPORT
    date_dim_FiscalYearPeriod(["date_dim.FiscalYearPeriod"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    product_dim_le_department(["product_dim_le.department"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    d365LocationMapping_View_legalentity(["d365LocationMapping_View.legalentity"]) --> REPORT
    Sum_ComponentSummaryView_SL_History_Value_(["Sum(ComponentSummaryView.SL_History_Value)"]) --> REPORT
    product_dim_le_MDSE_Supply(["product_dim_le.MDSE\Supply"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| ComponentSummaryView.SL_Component_Label |
| date_dim.FiscalYearPeriod |
| d365LocationMapping_View.inventlocationid |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| product_dim_le.department |
| date_dim.actual_date |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| d365LocationMapping_View.legalentity |
| Sum(ComponentSummaryView.SL_History_Value) |
| product_dim_le.MDSE\Supply |

## Pages

| Page | Visuals |
|---|---|
| DJR Component Split | 23 |

## Visuals

### DJR Component Split

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | ComponentSummaryView.SL_Component_Label |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 2c050ec017a6225d6f41 | slicer | date_dim.FiscalYearPeriod |
| 439290e644ba20e20e80 | slicer | d365LocationMapping_View.inventlocationid |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 5557a980b9a3ade3e7a9 | slicer | product_dim_le.department |
| 6f0031da695b744bd74a | textbox |  |
| 826e14c9840c3793285e | unknown |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | ComponentSummaryView.SL_Component_Label |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk, date_dim.actual_date |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | slicer | d365LocationMapping_View.legalentity |
| e0290b3bdcd982dcae6f | tableEx | product_dim_le.department, Sum(ComponentSummaryView.SL_History_Value), product_dim_le.MDSE\Supply, ComponentSummaryView.SL_Component_Label, date_dim.FiscalYearPeriod, d365LocationMapping_View.inventlocationid |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| ef07c99243bd2d36ca20 | slicer | product_dim_le.MDSE\Supply |
| f920f4a3989b72fd51af | textbox |  |
