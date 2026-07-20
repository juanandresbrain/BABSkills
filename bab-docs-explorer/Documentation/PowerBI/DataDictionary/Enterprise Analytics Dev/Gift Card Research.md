# Gift Card Research

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 22ada657-4425-4262-96d4-d4c6f2db71e7  
**Dataset ID:** 459ad959-d71a-481e-ae77-34987085c611  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/22ada657-4425-4262-96d4-d4c6f2db71e7  
**Semantic Model:** [Sales Audit Data Model](../../SemanticModels/Enterprise Analytics Prod/Sales Audit Data Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Gift Card Research"]
    Tender_Lines__JumpMind__Tender_Amount__Native_Currency_(["Tender Lines (JumpMind).Tender Amount (Native Currency)"]) --> REPORT
    Retail_Transactions__JumpMind__Loyalty_Card_Number(["Retail Transactions (JumpMind).Loyalty Card Number"]) --> REPORT
    Calendar_Actual_Date(["Calendar.Actual Date"]) --> REPORT
    Transactions__JumpMind__Business_Unit_Id(["Transactions (JumpMind).Business Unit Id"]) --> REPORT
    Transactions__JumpMind__Username_Id(["Transactions (JumpMind).Username Id"]) --> REPORT
    Retail_Lines__JumpMind__Item_Description(["Retail Lines (JumpMind).Item Description"]) --> REPORT
    Activated_Gift_Cards__JumpMind__Gift_Card_Action_Code(["Activated Gift Cards (JumpMind).Gift Card Action Code"]) --> REPORT
    Sum_Tender_Lines__JumpMind__Tender_Amount__Native_Currency__(["Sum(Tender Lines (JumpMind).Tender Amount (Native Currency))"]) --> REPORT
    Measure_Table_Activated_Gift_Cards_Gross_Amount_TE__Native_(["Measure Table.Activated Gift Cards Gross Amount TE (Native)"]) --> REPORT
    Retail_Transactions__JumpMind__Customer_Name(["Retail Transactions (JumpMind).Customer Name"]) --> REPORT
    Measure_Table_Activated_Gift_Cards_Net_Amount_TE__Native_(["Measure Table.Activated Gift Cards Net Amount TE (Native)"]) --> REPORT
    Transactions__JumpMind__Created_Datetime(["Transactions (JumpMind).Created Datetime"]) --> REPORT
    Transactions__JumpMind__retail_transaction_id(["Transactions (JumpMind).retail_transaction_id"]) --> REPORT
    Retail_Transactions__JumpMind__Device_Id(["Retail Transactions (JumpMind).Device Id"]) --> REPORT
    Locations__Store_MDM__Active(["Locations (Store MDM).Active"]) --> REPORT
    Locations__Store_MDM__Country(["Locations (Store MDM).Country"]) --> REPORT
    Locations__Store_MDM__Location_Line(["Locations (Store MDM).Location Line"]) --> REPORT
    Locations__Store_MDM__Country_name(["Locations (Store MDM).Country name"]) --> REPORT
    Locations__Store_MDM__State_Province_name(["Locations (Store MDM).State/Province name"]) --> REPORT
    Locations__Store_MDM__City(["Locations (Store MDM).City"]) --> REPORT
    Calendar_Fiscal_Year__Header_(["Calendar.Fiscal Year (Header)"]) --> REPORT
    Calendar_Fiscal_Quarter__Header_(["Calendar.Fiscal Quarter (Header)"]) --> REPORT
    Calendar_Fiscal_Month__Header_(["Calendar.Fiscal Month (Header)"]) --> REPORT
    Calendar_Fiscal_Week__Header_(["Calendar.Fiscal Week (Header)"]) --> REPORT
    Calendar_Calendar_Year__Header_(["Calendar.Calendar Year (Header)"]) --> REPORT
    Calendar_Calendar_Quarter__Header_(["Calendar.Calendar Quarter (Header)"]) --> REPORT
    Calendar_Calendar_Month__Header_(["Calendar.Calendar Month (Header)"]) --> REPORT
    Calendar_Calendar_Week__Header_(["Calendar.Calendar Week (Header)"]) --> REPORT
    Products__PLM__Department(["Products (PLM).Department"]) --> REPORT
    Products__PLM__Subclass(["Products (PLM).Subclass"]) --> REPORT
    Products__PLM__Class(["Products (PLM).Class"]) --> REPORT
    Products__PLM__Key_Story(["Products (PLM).Key Story"]) --> REPORT
    Products__PLM__Licensed_Collection(["Products (PLM).Licensed Collection"]) --> REPORT
    Activated_Gift_Cards__JumpMind__Card_Number(["Activated Gift Cards (JumpMind).Card Number"]) --> REPORT
    Retail_Lines__JumpMind__Line_Item_Type(["Retail Lines (JumpMind).Line Item Type"]) --> REPORT
    Retail_Lines__JumpMind__Item_Type(["Retail Lines (JumpMind).Item Type"]) --> REPORT
    Products__PLM__Item_Line(["Products (PLM).Item Line"]) --> REPORT
    Retail_Transactions__JumpMind__Date_Created(["Retail Transactions (JumpMind).Date Created"]) --> REPORT
    Tender_Lines__JumpMind__tender_auth_method_code(["Tender Lines (JumpMind).tender_auth_method_code"]) --> REPORT
    Tender_Card_Lines__JumpMind__Card_Number(["Tender Card Lines (JumpMind).Card Number"]) --> REPORT
    Transactions__JumpMind__Sequence_Number(["Transactions (JumpMind).Sequence Number"]) --> REPORT
    Tender_Card_Lines__JumpMind__Tender_Type_Code(["Tender Card Lines (JumpMind).Tender Type Code"]) --> REPORT
    Sum_Retail_Lines__JumpMind__Tax_Amount__Native_Currency__(["Sum(Retail Lines (JumpMind).Tax Amount (Native Currency))"]) --> REPORT
    Transactions__JumpMind__Transaction_Date(["Transactions (JumpMind).Transaction Date"]) --> REPORT
    Retail_Lines__JumpMind__Item_Line(["Retail Lines (JumpMind).Item Line"]) --> REPORT
    Sum_Retail_Lines__JumpMind__Actual_Unit_Price__Native_Currency__(["Sum(Retail Lines (JumpMind).Actual Unit Price (Native Currency))"]) --> REPORT
    Transactions__JumpMind__Associate_Work_Group(["Transactions (JumpMind).Associate Work Group"]) --> REPORT
    Business_Units__JumpMind__Business_Unit_Id(["Business Units (JumpMind).Business Unit Id"]) --> REPORT
    Sum_Retail_Lines__JumpMind__Regular_Unit_Price__Native_Currency__(["Sum(Retail Lines (JumpMind).Regular Unit Price (Native Currency))"]) --> REPORT
    Retail_Lines__JumpMind__Line_Sequence_Number(["Retail Lines (JumpMind).Line Sequence Number"]) --> REPORT
    Retail_Transactions__JumpMind__RegisterNo(["Retail Transactions (JumpMind).RegisterNo"]) --> REPORT
    Tender_Lines__JumpMind__Tender_Code(["Tender Lines (JumpMind).Tender Code"]) --> REPORT
    Sum_Retail_Lines__JumpMind__Actual_Sales_Amount_TE__Native_Currency__(["Sum(Retail Lines (JumpMind).Actual Sales Amount TE (Native Currency))"]) --> REPORT
    Sum_Retail_Lines__JumpMind__Regular_Sales_Amount_TE__Native_Currency__(["Sum(Retail Lines (JumpMind).Regular Sales Amount TE (Native Currency))"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| Tender Lines (JumpMind).Tender Amount (Native Currency) |
| Retail Transactions (JumpMind).Loyalty Card Number |
| Calendar.Actual Date |
| Transactions (JumpMind).Business Unit Id |
| Transactions (JumpMind).Username Id |
| Retail Lines (JumpMind).Item Description |
| Activated Gift Cards (JumpMind).Gift Card Action Code |
| Sum(Tender Lines (JumpMind).Tender Amount (Native Currency)) |
| Measure Table.Activated Gift Cards Gross Amount TE (Native) |
| Retail Transactions (JumpMind).Customer Name |
| Measure Table.Activated Gift Cards Net Amount TE (Native) |
| Transactions (JumpMind).Created Datetime |
| Transactions (JumpMind).retail_transaction_id |
| Retail Transactions (JumpMind).Device Id |
| Locations (Store MDM).Active |
| Locations (Store MDM).Country |
| Locations (Store MDM).Location Line |
| Locations (Store MDM).Country name |
| Locations (Store MDM).State/Province name |
| Locations (Store MDM).City |
| Calendar.Fiscal Year (Header) |
| Calendar.Fiscal Quarter (Header) |
| Calendar.Fiscal Month (Header) |
| Calendar.Fiscal Week (Header) |
| Calendar.Calendar Year (Header) |
| Calendar.Calendar Quarter (Header) |
| Calendar.Calendar Month (Header) |
| Calendar.Calendar Week (Header) |
| Products (PLM).Department |
| Products (PLM).Subclass |
| Products (PLM).Class |
| Products (PLM).Key Story |
| Products (PLM).Licensed Collection |
| Activated Gift Cards (JumpMind).Card Number |
| Retail Lines (JumpMind).Line Item Type |
| Retail Lines (JumpMind).Item Type |
| Products (PLM).Item Line |
| Retail Transactions (JumpMind).Date Created |
| Tender Lines (JumpMind).tender_auth_method_code |
| Tender Card Lines (JumpMind).Card Number |
| Transactions (JumpMind).Sequence Number |
| Tender Card Lines (JumpMind).Tender Type Code |
| Sum(Retail Lines (JumpMind).Tax Amount (Native Currency)) |
| Transactions (JumpMind).Transaction Date |
| Retail Lines (JumpMind).Item Line |
| Sum(Retail Lines (JumpMind).Actual Unit Price (Native Currency)) |
| Transactions (JumpMind).Associate Work Group |
| Business Units (JumpMind).Business Unit Id |
| Sum(Retail Lines (JumpMind).Regular Unit Price (Native Currency)) |
| Retail Lines (JumpMind).Line Sequence Number |
| Retail Transactions (JumpMind).RegisterNo |
| Tender Lines (JumpMind).Tender Code |
| Sum(Retail Lines (JumpMind).Actual Sales Amount TE (Native Currency)) |
| Sum(Retail Lines (JumpMind).Regular Sales Amount TE (Native Currency)) |

## Pages

| Page | Visuals |
|---|---|
| Duplicate of Gift Card Sold | 36 |
| Duplicate of Gift Card Sold | 36 |
| Duplicate of Gift Card Redeemed | 37 |
| Gift Card Redeemed | 37 |
| Gift Card Sold | 36 |

## Visuals

### Duplicate of Gift Card Sold

| Visual | Type | Fields |
|---|---|---|
| aa9fdc539404bd50cbff | slicer | Tender Lines (JumpMind).Tender Amount (Native Currency) |
| 23796b83540451b31303 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| b4f4cd9016ec093efa69 | textbox |  |
| 0d7acdb55f02f8ed9e54 | tableEx | Calendar.Actual Date, Transactions (JumpMind).Business Unit Id, Transactions (JumpMind).Username Id, Retail Lines (JumpMind).Item Description, Activated Gift Cards (JumpMind).Gift Card Action Code, Sum(Tender Lines (JumpMind).Tender Amount (Native Currency)), Measure Table.Activated Gift Cards Gross Amount TE (Native), Retail Transactions (JumpMind).Customer Name, Measure Table.Activated Gift Cards Net Amount TE (Native), Retail Transactions (JumpMind).Loyalty Card Number, Transactions (JumpMind).Created Datetime, Transactions (JumpMind).retail_transaction_id, Retail Transactions (JumpMind).Device Id |
| cefabb9bdb285698f0cf | unknown |  |
| 7ca5a226b2480d4a8775 | textbox |  |
| 181780942ac235b4ca5b | textbox |  |
| 2e545729060d79775590 | image |  |
| 39c2bc2949fe30544cf1 | textbox |  |
| 0e2a4a2405520554de60 | actionButton |  |
| 3d584b3d5c4355eab00d | unknown |  |
| fcf8c4f5a19f20af995a | slicer | Locations (Store MDM).Active |
| 43976c42098030855daf | slicer | Locations (Store MDM).Country |
| a3e89fec68b64421a1a2 | slicer | Locations (Store MDM).Location Line |
| fee01df979f28f6faf49 | slicer | Locations (Store MDM).Country name, Locations (Store MDM).State/Province name, Locations (Store MDM).City |
| 8820397c1925ee459887 | bookmarkNavigator |  |
| 970ecc8f1316f2f6b9ea | unknown |  |
| 9d6147e3aad7d1aad156 | slicer | Calendar.Actual Date |
| 4f1637281a1649764c4b | slicer | Calendar.Fiscal Year (Header), Calendar.Fiscal Quarter (Header), Calendar.Fiscal Month (Header), Calendar.Fiscal Week (Header), Calendar.Actual Date |
| fd11c03fc2225afbc140 | slicer | Calendar.Calendar Year (Header), Calendar.Calendar Quarter (Header), Calendar.Calendar Month (Header), Calendar.Calendar Week (Header) |
| c7eebb159625da16e364 | bookmarkNavigator |  |
| d2865d4a372ac3f27534 | unknown |  |
| fd5f0513ce8616643b04 | slicer | Products (PLM).Department |
| 6d27ed6712dcd3d84ce2 | slicer | Products (PLM).Subclass, Products (PLM).Class |
| 7b65efa41e744820400a | slicer | Products (PLM).Key Story |
| 9199c2068b9f944763a5 | slicer | Products (PLM).Licensed Collection |
| 84be627e01f759756eb1 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| a269946af031a7b242fc | slicer | Retail Transactions (JumpMind).Customer Name |
| ec2a748275b505a18a2b | slicer | Transactions (JumpMind).Username Id |
| 7c8f0297716d0285979f | slicer | Transactions (JumpMind).retail_transaction_id |
| eb197c5c6c85193711b0 | slicer | Activated Gift Cards (JumpMind).Card Number |
| 6f7d62efb0cbb3aba8fc | unknown |  |
| 80e47b2b1d4f999c2705 | slicer | Retail Lines (JumpMind).Line Item Type |
| 1a74a6a7290700333847 | slicer | Retail Lines (JumpMind).Item Type |
| 0d8a8321e883c51ba4c8 | slicer | Products (PLM).Item Line |
| a1940060244659591d65 | textbox |  |
| f6d3b5d802bc6d207870 | slicer | Tender Lines (JumpMind).Tender Amount (Native Currency) |
| e7e7aa83090d0010bee6 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| 248e3111ea8d0b25ea31 | textbox |  |
| 15a1cc2665c52898d652 | tableEx | Calendar.Actual Date, Transactions (JumpMind).Business Unit Id, Transactions (JumpMind).Username Id, Retail Lines (JumpMind).Item Description, Activated Gift Cards (JumpMind).Gift Card Action Code, Activated Gift Cards (JumpMind).Card Number, Sum(Tender Lines (JumpMind).Tender Amount (Native Currency)), Measure Table.Activated Gift Cards Gross Amount TE (Native), Retail Transactions (JumpMind).Customer Name, Measure Table.Activated Gift Cards Net Amount TE (Native), Retail Transactions (JumpMind).Loyalty Card Number, Transactions (JumpMind).Created Datetime, Transactions (JumpMind).retail_transaction_id, Retail Transactions (JumpMind).Device Id, Retail Transactions (JumpMind).Date Created |
| cdc7fcc0b234dbb0813b | unknown |  |
| 329834275abd35006e3b | textbox |  |
| 7931da01d370009ed588 | textbox |  |
| 5a680aa54e7a64ebad0b | image |  |
| 12c05b22278ad5b4d8a8 | textbox |  |
| 37ece0b0d72b1ca11e6a | actionButton |  |
| f376889d45087b05e739 | unknown |  |
| fe3341d3bba8c5644944 | slicer | Locations (Store MDM).Active |
| d26aa94589a0695a4846 | slicer | Locations (Store MDM).Country |
| 7f44281c58099bdb2a00 | slicer | Locations (Store MDM).Location Line |
| d6c2cfcb1ec81665ba07 | slicer | Locations (Store MDM).Country name, Locations (Store MDM).State/Province name, Locations (Store MDM).City |
| 743f8e1fee562021b091 | bookmarkNavigator |  |
| 0dcdbf2db000c9ca341d | unknown |  |
| 6110c4c867ca4b7271b1 | slicer | Calendar.Actual Date |
| 7bd1075d428b0e012b2a | slicer | Calendar.Fiscal Year (Header), Calendar.Fiscal Quarter (Header), Calendar.Fiscal Month (Header), Calendar.Fiscal Week (Header), Calendar.Actual Date |
| 3503e3600e9a9c5410be | slicer | Calendar.Calendar Year (Header), Calendar.Calendar Quarter (Header), Calendar.Calendar Month (Header), Calendar.Calendar Week (Header) |
| d966c3e7c060c7709148 | bookmarkNavigator |  |
| e3e2bf5f476be6bb48c3 | unknown |  |
| e059dd845c9030644560 | slicer | Products (PLM).Department |
| 05b4cda67c5b316b3150 | slicer | Products (PLM).Subclass, Products (PLM).Class |
| 573f37bd9d37e17b11ac | slicer | Products (PLM).Key Story |
| ed9273f0782a48140442 | slicer | Products (PLM).Licensed Collection |
| 12c2ecd4ed0740aea816 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| 2b7f82f35620da07045c | slicer | Retail Transactions (JumpMind).Customer Name |
| d4dbdabe4673974e8b90 | slicer | Transactions (JumpMind).Username Id |
| 2c8693eb3633a79cab99 | slicer | Transactions (JumpMind).retail_transaction_id |
| e610ea9196e0cd73b102 | slicer | Activated Gift Cards (JumpMind).Card Number |
| 0bebee8008b49e135cda | unknown |  |
| e86e83a1bd6a4c2a4069 | slicer | Retail Lines (JumpMind).Line Item Type |
| f71bd4bb45c88049e343 | slicer | Retail Lines (JumpMind).Item Type |
| cf6bdb26286341c07157 | slicer | Products (PLM).Item Line |
| 3aa582ec339b913db545 | textbox |  |

### Duplicate of Gift Card Sold

| Visual | Type | Fields |
|---|---|---|
| aa9fdc539404bd50cbff | slicer | Tender Lines (JumpMind).Tender Amount (Native Currency) |
| 23796b83540451b31303 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| b4f4cd9016ec093efa69 | textbox |  |
| 0d7acdb55f02f8ed9e54 | tableEx | Calendar.Actual Date, Transactions (JumpMind).Business Unit Id, Transactions (JumpMind).Username Id, Retail Lines (JumpMind).Item Description, Activated Gift Cards (JumpMind).Gift Card Action Code, Sum(Tender Lines (JumpMind).Tender Amount (Native Currency)), Measure Table.Activated Gift Cards Gross Amount TE (Native), Retail Transactions (JumpMind).Customer Name, Measure Table.Activated Gift Cards Net Amount TE (Native), Retail Transactions (JumpMind).Loyalty Card Number, Transactions (JumpMind).Created Datetime, Transactions (JumpMind).retail_transaction_id, Retail Transactions (JumpMind).Device Id |
| cefabb9bdb285698f0cf | unknown |  |
| 7ca5a226b2480d4a8775 | textbox |  |
| 181780942ac235b4ca5b | textbox |  |
| 2e545729060d79775590 | image |  |
| 39c2bc2949fe30544cf1 | textbox |  |
| 0e2a4a2405520554de60 | actionButton |  |
| 3d584b3d5c4355eab00d | unknown |  |
| fcf8c4f5a19f20af995a | slicer | Locations (Store MDM).Active |
| 43976c42098030855daf | slicer | Locations (Store MDM).Country |
| a3e89fec68b64421a1a2 | slicer | Locations (Store MDM).Location Line |
| fee01df979f28f6faf49 | slicer | Locations (Store MDM).Country name, Locations (Store MDM).State/Province name, Locations (Store MDM).City |
| 8820397c1925ee459887 | bookmarkNavigator |  |
| 970ecc8f1316f2f6b9ea | unknown |  |
| 9d6147e3aad7d1aad156 | slicer | Calendar.Actual Date |
| 4f1637281a1649764c4b | slicer | Calendar.Fiscal Year (Header), Calendar.Fiscal Quarter (Header), Calendar.Fiscal Month (Header), Calendar.Fiscal Week (Header), Calendar.Actual Date |
| fd11c03fc2225afbc140 | slicer | Calendar.Calendar Year (Header), Calendar.Calendar Quarter (Header), Calendar.Calendar Month (Header), Calendar.Calendar Week (Header) |
| c7eebb159625da16e364 | bookmarkNavigator |  |
| d2865d4a372ac3f27534 | unknown |  |
| fd5f0513ce8616643b04 | slicer | Products (PLM).Department |
| 6d27ed6712dcd3d84ce2 | slicer | Products (PLM).Subclass, Products (PLM).Class |
| 7b65efa41e744820400a | slicer | Products (PLM).Key Story |
| 9199c2068b9f944763a5 | slicer | Products (PLM).Licensed Collection |
| 84be627e01f759756eb1 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| a269946af031a7b242fc | slicer | Retail Transactions (JumpMind).Customer Name |
| ec2a748275b505a18a2b | slicer | Transactions (JumpMind).Username Id |
| 7c8f0297716d0285979f | slicer | Transactions (JumpMind).retail_transaction_id |
| eb197c5c6c85193711b0 | slicer | Activated Gift Cards (JumpMind).Card Number |
| 6f7d62efb0cbb3aba8fc | unknown |  |
| 80e47b2b1d4f999c2705 | slicer | Retail Lines (JumpMind).Line Item Type |
| 1a74a6a7290700333847 | slicer | Retail Lines (JumpMind).Item Type |
| 0d8a8321e883c51ba4c8 | slicer | Products (PLM).Item Line |
| a1940060244659591d65 | textbox |  |
| f6d3b5d802bc6d207870 | slicer | Tender Lines (JumpMind).Tender Amount (Native Currency) |
| e7e7aa83090d0010bee6 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| 248e3111ea8d0b25ea31 | textbox |  |
| 15a1cc2665c52898d652 | tableEx | Calendar.Actual Date, Transactions (JumpMind).Business Unit Id, Transactions (JumpMind).Username Id, Retail Lines (JumpMind).Item Description, Activated Gift Cards (JumpMind).Gift Card Action Code, Activated Gift Cards (JumpMind).Card Number, Sum(Tender Lines (JumpMind).Tender Amount (Native Currency)), Measure Table.Activated Gift Cards Gross Amount TE (Native), Retail Transactions (JumpMind).Customer Name, Measure Table.Activated Gift Cards Net Amount TE (Native), Retail Transactions (JumpMind).Loyalty Card Number, Transactions (JumpMind).Created Datetime, Transactions (JumpMind).retail_transaction_id, Retail Transactions (JumpMind).Device Id, Retail Transactions (JumpMind).Date Created |
| cdc7fcc0b234dbb0813b | unknown |  |
| 329834275abd35006e3b | textbox |  |
| 7931da01d370009ed588 | textbox |  |
| 5a680aa54e7a64ebad0b | image |  |
| 12c05b22278ad5b4d8a8 | textbox |  |
| 37ece0b0d72b1ca11e6a | actionButton |  |
| f376889d45087b05e739 | unknown |  |
| fe3341d3bba8c5644944 | slicer | Locations (Store MDM).Active |
| d26aa94589a0695a4846 | slicer | Locations (Store MDM).Country |
| 7f44281c58099bdb2a00 | slicer | Locations (Store MDM).Location Line |
| d6c2cfcb1ec81665ba07 | slicer | Locations (Store MDM).Country name, Locations (Store MDM).State/Province name, Locations (Store MDM).City |
| 743f8e1fee562021b091 | bookmarkNavigator |  |
| 0dcdbf2db000c9ca341d | unknown |  |
| 6110c4c867ca4b7271b1 | slicer | Calendar.Actual Date |
| 7bd1075d428b0e012b2a | slicer | Calendar.Fiscal Year (Header), Calendar.Fiscal Quarter (Header), Calendar.Fiscal Month (Header), Calendar.Fiscal Week (Header), Calendar.Actual Date |
| 3503e3600e9a9c5410be | slicer | Calendar.Calendar Year (Header), Calendar.Calendar Quarter (Header), Calendar.Calendar Month (Header), Calendar.Calendar Week (Header) |
| d966c3e7c060c7709148 | bookmarkNavigator |  |
| e3e2bf5f476be6bb48c3 | unknown |  |
| e059dd845c9030644560 | slicer | Products (PLM).Department |
| 05b4cda67c5b316b3150 | slicer | Products (PLM).Subclass, Products (PLM).Class |
| 573f37bd9d37e17b11ac | slicer | Products (PLM).Key Story |
| ed9273f0782a48140442 | slicer | Products (PLM).Licensed Collection |
| 12c2ecd4ed0740aea816 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| 2b7f82f35620da07045c | slicer | Retail Transactions (JumpMind).Customer Name |
| d4dbdabe4673974e8b90 | slicer | Transactions (JumpMind).Username Id |
| 2c8693eb3633a79cab99 | slicer | Transactions (JumpMind).retail_transaction_id |
| e610ea9196e0cd73b102 | slicer | Activated Gift Cards (JumpMind).Card Number |
| 0bebee8008b49e135cda | unknown |  |
| e86e83a1bd6a4c2a4069 | slicer | Retail Lines (JumpMind).Line Item Type |
| f71bd4bb45c88049e343 | slicer | Retail Lines (JumpMind).Item Type |
| cf6bdb26286341c07157 | slicer | Products (PLM).Item Line |
| 3aa582ec339b913db545 | textbox |  |

### Duplicate of Gift Card Redeemed

| Visual | Type | Fields |
|---|---|---|
| 8f6c1971a729c7e908b0 | textbox |  |
| af0ea37ac4020678a04b | tableEx | Calendar.Actual Date, Transactions (JumpMind).Business Unit Id, Transactions (JumpMind).Username Id, Sum(Tender Lines (JumpMind).Tender Amount (Native Currency)), Retail Transactions (JumpMind).Customer Name, Retail Transactions (JumpMind).Loyalty Card Number, Tender Lines (JumpMind).tender_auth_method_code, Transactions (JumpMind).retail_transaction_id, Tender Card Lines (JumpMind).Card Number, Transactions (JumpMind).Sequence Number, Tender Card Lines (JumpMind).Tender Type Code |
| 6dbc76f40102acbc53b9 | tableEx | Calendar.Actual Date, Sum(Retail Lines (JumpMind).Tax Amount (Native Currency)), Transactions (JumpMind).Sequence Number |
| ba7cfc74a22339a09277 | actionButton |  |
| 9f75eb2fe0eb0c08d642 | tableEx | Transactions (JumpMind).Sequence Number, Transactions (JumpMind).Transaction Date, Retail Lines (JumpMind).Item Line, Sum(Retail Lines (JumpMind).Actual Unit Price (Native Currency)) |
| 6d72abce930748aee949 | unknown |  |
| eb43ae980754b5097b5e | textbox |  |
| d25e77cd901eea50ce70 | textbox |  |
| 1e77a03f970e128444e6 | image |  |
| 882409990d0d9ab131c3 | textbox |  |
| e3b65390300a7e3a3cac | actionButton |  |
| d5499c3a681c2cad0bc0 | unknown |  |
| 48d20cb99a2408bc4cba | slicer | Locations (Store MDM).Active |
| 5e98a3a61b7346c266ee | slicer | Locations (Store MDM).Country |
| 7e1ae4322cda505d1002 | slicer | Locations (Store MDM).Location Line |
| ff463d5303ad1146ba02 | slicer | Locations (Store MDM).Country name, Locations (Store MDM).State/Province name, Locations (Store MDM).City |
| 8d9320df48da22aac60a | bookmarkNavigator |  |
| 11cac0425c165b310702 | unknown |  |
| 027d19d31ad06b905500 | slicer | Calendar.Actual Date |
| ac31e6155e226edca960 | slicer | Calendar.Fiscal Year (Header), Calendar.Fiscal Quarter (Header), Calendar.Fiscal Month (Header), Calendar.Fiscal Week (Header), Calendar.Actual Date |
| c428cb1ae3aeb6127a6b | slicer | Calendar.Calendar Year (Header), Calendar.Calendar Quarter (Header), Calendar.Calendar Month (Header), Calendar.Calendar Week (Header) |
| 6dd9b3e97b27244aeee1 | bookmarkNavigator |  |
| 779f8ec30a8dd94a1413 | unknown |  |
| ed855440c30271c18796 | slicer | Products (PLM).Department |
| 27be0a802be05d9dc5b4 | slicer | Products (PLM).Subclass, Products (PLM).Class |
| d0931280b386003064ac | slicer | Products (PLM).Key Story |
| 46f43164beae9811a216 | slicer | Transactions (JumpMind).Associate Work Group |
| 11d4e8f4a927a84d5172 | slicer | Transactions (JumpMind).Associate Work Group |
| 01d13ffd95ee35cc2d7b | slicer | Transactions (JumpMind).retail_transaction_id |
| f9d79a3f84d71d001ea5 | slicer | Business Units (JumpMind).Business Unit Id |
| 781969580da42392e04c | slicer | Tender Card Lines (JumpMind).Card Number |
| f3f569b4183d60954727 | unknown |  |
| 53ac9400893e49a7ebc9 | slicer | Retail Lines (JumpMind).Line Item Type |
| 48ca4a211d6780200c9b | slicer | Retail Lines (JumpMind).Item Type |
| e960a9a504cd08e59c38 | slicer | Products (PLM).Item Line |
| d9288ce952a634467e05 | slicer | Products (PLM).Licensed Collection |
| 2b2eed7908d987d57ac9 | textbox |  |

### Gift Card Redeemed

| Visual | Type | Fields |
|---|---|---|
| 07b328d18ecdab001d0b | textbox |  |
| 2523489aa1e51a167000 | tableEx | Calendar.Actual Date, Transactions (JumpMind).Business Unit Id, Transactions (JumpMind).Username Id, Sum(Tender Lines (JumpMind).Tender Amount (Native Currency)), Retail Transactions (JumpMind).Customer Name, Retail Transactions (JumpMind).Loyalty Card Number, Tender Lines (JumpMind).tender_auth_method_code, Transactions (JumpMind).retail_transaction_id, Tender Card Lines (JumpMind).Card Number, Transactions (JumpMind).Sequence Number, Tender Card Lines (JumpMind).Tender Type Code |
| 7b0b6a804c11e517c690 | tableEx | Calendar.Actual Date, Sum(Retail Lines (JumpMind).Tax Amount (Native Currency)), Transactions (JumpMind).Sequence Number |
| cb488a1ae20d730780d5 | actionButton |  |
| a45ecb5fa2818c60e4f9 | tableEx | Transactions (JumpMind).Sequence Number, Transactions (JumpMind).Transaction Date, Retail Lines (JumpMind).Item Line, Sum(Retail Lines (JumpMind).Regular Unit Price (Native Currency)), Retail Lines (JumpMind).Line Sequence Number |
| 63f25a605552c3c3dd01 | unknown |  |
| 827096d0de4e907a2a39 | textbox |  |
| 3b263da54c1003bac458 | textbox |  |
| 972fc6e0900405d5e680 | image |  |
| 76d96a4bd80ae2022e68 | textbox |  |
| f0d665728ee456823ee3 | actionButton |  |
| c3bd3a7544eb34e312c7 | unknown |  |
| 177c2967c18e64b0bcaa | slicer | Locations (Store MDM).Active |
| a4353178804a3355be38 | slicer | Locations (Store MDM).Country |
| 5b054426057901e2033d | slicer | Locations (Store MDM).Location Line |
| e415dbfb1961ac333304 | slicer | Locations (Store MDM).Country name, Locations (Store MDM).State/Province name, Locations (Store MDM).City |
| ea2dce6200b87415a64d | bookmarkNavigator |  |
| 671f725e8014939e7e62 | unknown |  |
| 05443540d6802a2034e0 | slicer | Calendar.Actual Date |
| c202f234c78e85c066b6 | slicer | Calendar.Fiscal Year (Header), Calendar.Fiscal Quarter (Header), Calendar.Fiscal Month (Header), Calendar.Fiscal Week (Header), Calendar.Actual Date |
| f4fda8b32817035b9dd0 | slicer | Calendar.Calendar Year (Header), Calendar.Calendar Quarter (Header), Calendar.Calendar Month (Header), Calendar.Calendar Week (Header) |
| f2bbc049d087db6004a6 | bookmarkNavigator |  |
| cef6c899a11086912015 | unknown |  |
| 1fe78fa50890abc900a1 | slicer | Products (PLM).Department |
| c091ec68aa5769854ea9 | slicer | Products (PLM).Subclass, Products (PLM).Class |
| 5795056e8830290b0bed | slicer | Products (PLM).Key Story |
| c14fbf6802411282c094 | slicer | Products (PLM).Licensed Collection |
| 2b6e100d0bab66674212 | slicer | Transactions (JumpMind).Associate Work Group |
| e8b911500a0e33c656d7 | slicer | Transactions (JumpMind).Associate Work Group |
| 606584f0ee084726d251 | slicer | Transactions (JumpMind).retail_transaction_id |
| daba0f43d0beb111b1c5 | slicer | Business Units (JumpMind).Business Unit Id |
| 2321641fe13407184cd6 | slicer | Tender Card Lines (JumpMind).Card Number |
| dc1c610f685bd06241d4 | unknown |  |
| 426d2cfe0a76b1520e90 | slicer | Retail Lines (JumpMind).Line Item Type |
| ddcb92d7b02896dca6c9 | slicer | Retail Lines (JumpMind).Item Type |
| 38ffd3e2883d6970dac5 | slicer | Products (PLM).Item Line |
| 35372cb27a7435c6b18e | textbox |  |

### Gift Card Sold

| Visual | Type | Fields |
|---|---|---|
| db2992d334940202bd54 | slicer | Tender Lines (JumpMind).Tender Amount (Native Currency) |
| fc4b38ec71ab641069c9 | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| 363d3089689cc31382ce | textbox |  |
| 720c9cdd1e389d91e560 | tableEx | Calendar.Actual Date, Transactions (JumpMind).Business Unit Id, Transactions (JumpMind).Username Id, Retail Lines (JumpMind).Item Description, Activated Gift Cards (JumpMind).Gift Card Action Code, Activated Gift Cards (JumpMind).Card Number, Sum(Tender Lines (JumpMind).Tender Amount (Native Currency)), Retail Transactions (JumpMind).Customer Name, Retail Transactions (JumpMind).Loyalty Card Number, Transactions (JumpMind).Created Datetime, Transactions (JumpMind).retail_transaction_id, Retail Transactions (JumpMind).RegisterNo, Tender Lines (JumpMind).Tender Code, Sum(Retail Lines (JumpMind).Actual Sales Amount TE (Native Currency)), Sum(Retail Lines (JumpMind).Regular Sales Amount TE (Native Currency)) |
| 0b4140222c5f6ce0edbe | unknown |  |
| f920f4a3989b72fd51af | textbox |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 97f4659a5a12bc988c51 | image |  |
| 9ea736d49b75db93980e | textbox |  |
| ec739d70b14b7c06805a | actionButton |  |
| 44b856414f1a82fa1972 | unknown |  |
| cd771722998da0d815e8 | slicer | Locations (Store MDM).Active |
| 563e21e900833896b544 | slicer | Locations (Store MDM).Country |
| f492ce29c681642c039d | slicer | Locations (Store MDM).Location Line |
| b5ffd4d7c9991e903df4 | slicer | Locations (Store MDM).Country name, Locations (Store MDM).State/Province name, Locations (Store MDM).City |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| ebf4a2dc4872072b777f | unknown |  |
| 9a7956cae86f44783ec2 | slicer | Calendar.Actual Date |
| cc9c621b0f8156219228 | slicer | Calendar.Fiscal Year (Header), Calendar.Fiscal Quarter (Header), Calendar.Fiscal Month (Header), Calendar.Fiscal Week (Header), Calendar.Actual Date |
| 4df0d921ab0b5d077f2c | slicer | Calendar.Calendar Year (Header), Calendar.Calendar Quarter (Header), Calendar.Calendar Month (Header), Calendar.Calendar Week (Header) |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| 826e14c9840c3793285e | unknown |  |
| e8e740717323d0200f7a | slicer | Products (PLM).Department |
| 7869095a179dc31dae86 | slicer | Products (PLM).Subclass, Products (PLM).Class |
| 3edf860c41bfa20e56ed | slicer | Products (PLM).Key Story |
| 22da671c0667f2a982ae | slicer | Products (PLM).Licensed Collection |
| 172c32e50b240ce9090b | slicer | Retail Transactions (JumpMind).Loyalty Card Number |
| 9a867bcecd3d326e700a | slicer | Retail Transactions (JumpMind).Customer Name |
| 1247fc727a61c0856ee0 | slicer | Transactions (JumpMind).Username Id |
| df86f06e967c91d2414a | slicer | Transactions (JumpMind).retail_transaction_id |
| 6638838506cceec393e7 | slicer | Activated Gift Cards (JumpMind).Card Number |
| d60b44ab0994153302b3 | unknown |  |
| 0990f82a5dbf1a44dadb | slicer | Retail Lines (JumpMind).Line Item Type |
| c5bb2e2d468b021899e9 | slicer | Retail Lines (JumpMind).Item Type |
| ebefc5b86b1ea14d3bca | slicer | Products (PLM).Item Line |
| 3907067465cb97118580 | textbox |  |
