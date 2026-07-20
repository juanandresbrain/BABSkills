# Finance – Freight On Board (FOB) Royalty Report – On Demand

**Workspace:** Enterprise Analytics Dev  
**Report ID:** d45a930c-85f9-4985-8d02-1927a64a2391  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/d45a930c-85f9-4985-8d02-1927a64a2391  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Finance – Freight On Board (FOB) Royalty Report – On Demand"]
    d365LocationMapping_View_legalentity(["d365LocationMapping_View.legalentity"]) --> REPORT
    VendInvoiceView_documentid(["VendInvoiceView.documentid"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    product_dim_le_Licensor(["product_dim_le.Licensor"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    VendInvoiceView_ledgervoucher(["VendInvoiceView.ledgervoucher"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    VendInvoiceView_Licensor(["VendInvoiceView.Licensor"]) --> REPORT
    Sum_VendInvoiceView_lineamount_(["Sum(VendInvoiceView.lineamount)"]) --> REPORT
    VendInvoiceView_inventlocationid(["VendInvoiceView.inventlocationid"]) --> REPORT
    Sum_VendInvoiceView_qty_(["Sum(VendInvoiceView.qty)"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    Sum_product_dim_le_RoyaltyPercent_(["Sum(product_dim_le.RoyaltyPercent)"]) --> REPORT
    VendInvoiceView_documentdate(["VendInvoiceView.documentdate"]) --> REPORT
    Sum_VendInvoiceView_ChargeAmount_(["Sum(VendInvoiceView.ChargeAmount)"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| d365LocationMapping_View.legalentity |
| VendInvoiceView.documentid |
| product_dim_le.style_code |
| product_dim_le.Licensor |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| VendInvoiceView.ledgervoucher |
| date_dim.actual_date |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| d365LocationMapping_View.inventlocationid |
| VendInvoiceView.Licensor |
| Sum(VendInvoiceView.lineamount) |
| VendInvoiceView.inventlocationid |
| Sum(VendInvoiceView.qty) |
| product_dim_le.style_desc |
| Sum(product_dim_le.RoyaltyPercent) |
| VendInvoiceView.documentdate |
| Sum(VendInvoiceView.ChargeAmount) |

## Pages

| Page | Visuals |
|---|---|
| Freight On Board (FOB) Royalty Report | 23 |

## Visuals

### Freight On Board (FOB) Royalty Report

| Visual | Type | Fields |
|---|---|---|
| 020026ca22a2f6936d26 | slicer | d365LocationMapping_View.legalentity |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 23cf248ccf0d178dc319 | textFilter25A4896A83E0487089E2B90C9AE57C8A | VendInvoiceView.documentid |
| 2c050ec017a6225d6f41 | slicer | product_dim_le.style_code |
| 3edf860c41bfa20e56ed | slicer | product_dim_le.Licensor |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 7eabc2d4a0a4fa7b4278 | textFilter25A4896A83E0487089E2B90C9AE57C8A | VendInvoiceView.ledgervoucher |
| 826e14c9840c3793285e | unknown |  |
| 8521e1935e2ddb44a772 | actionButton |  |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | slicer | d365LocationMapping_View.inventlocationid |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f23d5b55029a0991e0da | tableEx | VendInvoiceView.Licensor, Sum(VendInvoiceView.lineamount), VendInvoiceView.inventlocationid, Sum(VendInvoiceView.qty), VendInvoiceView.ledgervoucher, product_dim_le.style_code, product_dim_le.style_desc, Sum(product_dim_le.RoyaltyPercent), VendInvoiceView.documentid, VendInvoiceView.documentdate, Sum(VendInvoiceView.ChargeAmount) |
| f920f4a3989b72fd51af | textbox |  |
