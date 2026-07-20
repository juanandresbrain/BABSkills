# Finance – Freight Factor – Ad Hoc

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 76c6571d-9cab-45d0-b7fe-926ea82e69db  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/76c6571d-9cab-45d0-b7fe-926ea82e69db  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Finance – Freight Factor – Ad Hoc"]
    product_dim_le_department_code(["product_dim_le.department_code"]) --> REPORT
    product_dim_le_LicensedCollection(["product_dim_le.LicensedCollection"]) --> REPORT
    PurchChargesView_itemid(["PurchChargesView.itemid"]) --> REPORT
    VendInvoiceView_ledgervoucher(["VendInvoiceView.ledgervoucher"]) --> REPORT
    product_dim_le_KeyStory(["product_dim_le.KeyStory"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    VendInvoiceView_markupcode(["VendInvoiceView.markupcode"]) --> REPORT
    product_dim_le_subclass_code(["product_dim_le.subclass_code"]) --> REPORT
    VendInvoiceView_purchid(["VendInvoiceView.purchid"]) --> REPORT
    PurchChargesView_received_date(["PurchChargesView.received_date"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    VendInvoiceView_dataareaid(["VendInvoiceView.dataareaid"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    VendInvoiceView_documentdate(["VendInvoiceView.documentdate"]) --> REPORT
    VendInvoiceView_itemid(["VendInvoiceView.itemid"]) --> REPORT
    Sum_VendInvoiceView_ChargeAmount_(["Sum(VendInvoiceView.ChargeAmount)"]) --> REPORT
    product_dim_le_MDSE_Supply(["product_dim_le.MDSE\Supply"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    product_dim_le_class_code(["product_dim_le.class_code"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| product_dim_le.department_code |
| product_dim_le.LicensedCollection |
| PurchChargesView.itemid |
| VendInvoiceView.ledgervoucher |
| product_dim_le.KeyStory |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| VendInvoiceView.markupcode |
| product_dim_le.subclass_code |
| VendInvoiceView.purchid |
| PurchChargesView.received_date |
| date_dim.fiscal_year |
| date_dim.actual_date |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| VendInvoiceView.dataareaid |
| d365LocationMapping_View.inventlocationid |
| VendInvoiceView.documentdate |
| VendInvoiceView.itemid |
| Sum(VendInvoiceView.ChargeAmount) |
| product_dim_le.MDSE\Supply |
| product_dim_le.style_desc |
| product_dim_le.class_code |

## Pages

| Page | Visuals |
|---|---|
| Freight Factor | 27 |

## Visuals

### Freight Factor

| Visual | Type | Fields |
|---|---|---|
| 0990f82a5dbf1a44dadb | slicer | product_dim_le.department_code |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 22da671c0667f2a982ae | slicer | product_dim_le.LicensedCollection |
| 2c050ec017a6225d6f41 | slicer | PurchChargesView.itemid |
| 2fe53e4e73dbaecc0854 | textFilter25A4896A83E0487089E2B90C9AE57C8A | VendInvoiceView.ledgervoucher |
| 3edf860c41bfa20e56ed | slicer | product_dim_le.KeyStory |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6041b2ff0982ad24d213 | slicer | VendInvoiceView.markupcode |
| 6f0031da695b744bd74a | textbox |  |
| 7869095a179dc31dae86 | slicer | product_dim_le.subclass_code |
| 826e14c9840c3793285e | unknown |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | VendInvoiceView.purchid |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | PurchChargesView.received_date |
| 9ea736d49b75db93980e | textbox |  |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | slicer | VendInvoiceView.dataareaid |
| e0290b3bdcd982dcae6f | tableEx | d365LocationMapping_View.inventlocationid, VendInvoiceView.purchid, VendInvoiceView.ledgervoucher, VendInvoiceView.documentdate, VendInvoiceView.itemid, Sum(VendInvoiceView.ChargeAmount), VendInvoiceView.markupcode, product_dim_le.MDSE\Supply, product_dim_le.style_desc |
| e8e740717323d0200f7a | slicer | product_dim_le.class_code |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f920f4a3989b72fd51af | textbox |  |
| fa57b4e085031445d628 | slicer | d365LocationMapping_View.inventlocationid |
