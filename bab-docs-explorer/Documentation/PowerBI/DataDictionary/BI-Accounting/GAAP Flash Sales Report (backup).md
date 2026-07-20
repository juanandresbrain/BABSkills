# GAAP Flash Sales Report (backup)

**Workspace:** BI-Accounting  
**Report ID:** 398c8d55-dab9-4425-ae83-8de5b8108709  
**Dataset ID:** 459ad959-d71a-481e-ae77-34987085c611  
**Web URL:** https://app.powerbi.com/groups/e996caff-15ec-41d5-ae2b-cc9137531fb6/reports/398c8d55-dab9-4425-ae83-8de5b8108709  
**Semantic Model:** [Sales Audit Data Model](../../SemanticModels/Enterprise Analytics Prod/Sales Audit Data Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["GAAP Flash Sales Report (backup)"]
    Sum_Retail_Transactions__JumpMind__Total_(["Sum(Retail Transactions (JumpMind).Total)"]) --> REPORT
    Retail_Transactions__JumpMind__ISO_Currency_Code(["Retail Transactions (JumpMind).ISO Currency Code"]) --> REPORT
    Business_Units__JumpMind__Location_Line(["Business Units (JumpMind).Location Line"]) --> REPORT
    Locations__Store_MDM__Country_name(["Locations (Store MDM).Country name"]) --> REPORT
    Transactions__JumpMind__Associate_Work_Group(["Transactions (JumpMind).Associate Work Group"]) --> REPORT
    Retail_Lines__JumpMind__Line_Item_Type(["Retail Lines (JumpMind).Line Item Type"]) --> REPORT
    Retail_Lines__JumpMind__Item_Type(["Retail Lines (JumpMind).Item Type"]) --> REPORT
    Products__PLM__Item_Line(["Products (PLM).Item Line"]) --> REPORT
    Products__PLM__Licensed_Collection(["Products (PLM).Licensed Collection"]) --> REPORT
    Products__PLM__Key_Story(["Products (PLM).Key Story"]) --> REPORT
    Products__PLM__Subclass(["Products (PLM).Subclass"]) --> REPORT
    Products__PLM__Class(["Products (PLM).Class"]) --> REPORT
    Products__PLM__Department(["Products (PLM).Department"]) --> REPORT
    Calendar_Calendar_Year__Header_(["Calendar.Calendar Year (Header)"]) --> REPORT
    Calendar_Calendar_Quarter__Header_(["Calendar.Calendar Quarter (Header)"]) --> REPORT
    Calendar_Calendar_Month__Header_(["Calendar.Calendar Month (Header)"]) --> REPORT
    Calendar_Calendar_Week__Header_(["Calendar.Calendar Week (Header)"]) --> REPORT
    Calendar_Fiscal_Year__Header_(["Calendar.Fiscal Year (Header)"]) --> REPORT
    Calendar_Fiscal_Quarter__Header_(["Calendar.Fiscal Quarter (Header)"]) --> REPORT
    Calendar_Fiscal_Month__Header_(["Calendar.Fiscal Month (Header)"]) --> REPORT
    Calendar_Fiscal_Week__Header_(["Calendar.Fiscal Week (Header)"]) --> REPORT
    Calendar_Actual_Date(["Calendar.Actual Date"]) --> REPORT
    Locations__Store_MDM__State_Province_name(["Locations (Store MDM).State/Province name"]) --> REPORT
    Locations__Store_MDM__City(["Locations (Store MDM).City"]) --> REPORT
    Locations__Store_MDM__Location_Line(["Locations (Store MDM).Location Line"]) --> REPORT
    Locations__Store_MDM__Country(["Locations (Store MDM).Country"]) --> REPORT
    Locations__Store_MDM__Active(["Locations (Store MDM).Active"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| Sum(Retail Transactions (JumpMind).Total) |
| Retail Transactions (JumpMind).ISO Currency Code |
| Business Units (JumpMind).Location Line |
| Locations (Store MDM).Country name |
| Transactions (JumpMind).Associate Work Group |
| Retail Lines (JumpMind).Line Item Type |
| Retail Lines (JumpMind).Item Type |
| Products (PLM).Item Line |
| Products (PLM).Licensed Collection |
| Products (PLM).Key Story |
| Products (PLM).Subclass |
| Products (PLM).Class |
| Products (PLM).Department |
| Calendar.Calendar Year (Header) |
| Calendar.Calendar Quarter (Header) |
| Calendar.Calendar Month (Header) |
| Calendar.Calendar Week (Header) |
| Calendar.Fiscal Year (Header) |
| Calendar.Fiscal Quarter (Header) |
| Calendar.Fiscal Month (Header) |
| Calendar.Fiscal Week (Header) |
| Calendar.Actual Date |
| Locations (Store MDM).State/Province name |
| Locations (Store MDM).City |
| Locations (Store MDM).Location Line |
| Locations (Store MDM).Country |
| Locations (Store MDM).Active |

## Pages

| Page | Visuals |
|---|---|
| SmartLook Report | 33 |

## Visuals

### SmartLook Report

| Visual | Type | Fields |
|---|---|---|
| 0b4140222c5f6ce0edbe | unknown |  |
| 120d7dafe353a868cec7 | pivotTable | Sum(Retail Transactions (JumpMind).Total), Retail Transactions (JumpMind).ISO Currency Code, Business Units (JumpMind).Location Line, Locations (Store MDM).Country name |
| 3907067465cb97118580 | textbox |  |
| 172c32e50b240ce9090b | slicer | Transactions (JumpMind).Associate Work Group |
| 9a867bcecd3d326e700a | slicer | Transactions (JumpMind).Associate Work Group |
| 1247fc727a61c0856ee0 | slicer | Transactions (JumpMind).Associate Work Group |
| df86f06e967c91d2414a | slicer | Transactions (JumpMind).Associate Work Group |
| 6638838506cceec393e7 | slicer | Transactions (JumpMind).Associate Work Group |
| d60b44ab0994153302b3 | unknown |  |
| 0990f82a5dbf1a44dadb | slicer | Retail Lines (JumpMind).Line Item Type |
| c5bb2e2d468b021899e9 | slicer | Retail Lines (JumpMind).Item Type |
| ebefc5b86b1ea14d3bca | slicer | Products (PLM).Item Line |
| 22da671c0667f2a982ae | slicer | Products (PLM).Licensed Collection |
| 3edf860c41bfa20e56ed | slicer | Products (PLM).Key Story |
| 7869095a179dc31dae86 | slicer | Products (PLM).Subclass, Products (PLM).Class |
| e8e740717323d0200f7a | slicer | Products (PLM).Department |
| 826e14c9840c3793285e | unknown |  |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| 4df0d921ab0b5d077f2c | slicer | Calendar.Calendar Year (Header), Calendar.Calendar Quarter (Header), Calendar.Calendar Month (Header), Calendar.Calendar Week (Header) |
| cc9c621b0f8156219228 | slicer | Calendar.Fiscal Year (Header), Calendar.Fiscal Quarter (Header), Calendar.Fiscal Month (Header), Calendar.Fiscal Week (Header), Calendar.Actual Date |
| 9a7956cae86f44783ec2 | slicer | Calendar.Actual Date |
| ebf4a2dc4872072b777f | unknown |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| b5ffd4d7c9991e903df4 | slicer | Locations (Store MDM).Country name, Locations (Store MDM).State/Province name, Locations (Store MDM).City |
| f492ce29c681642c039d | slicer | Locations (Store MDM).Location Line |
| 563e21e900833896b544 | slicer | Locations (Store MDM).Country |
| cd771722998da0d815e8 | slicer | Locations (Store MDM).Active |
| 44b856414f1a82fa1972 | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| 9ea736d49b75db93980e | textbox |  |
| 97f4659a5a12bc988c51 | image |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| f920f4a3989b72fd51af | textbox |  |
