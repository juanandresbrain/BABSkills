# Planning and Allocation – 53 Week Inventory and Sales Ladder Analysis – Annual

**Workspace:** Enterprise Analytics Dev  
**Report ID:** 76f9b71c-f8b7-4817-b07e-228912d6dd24  
**Dataset ID:** fba3b349-79e8-41c0-9703-c90e9ddeef23  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/76f9b71c-f8b7-4817-b07e-228912d6dd24  
**Semantic Model:** [Merchandise Aggregate Semantic Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Aggregate Semantic Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Planning and Allocation – 53 Week Inventory and Sales Ladder Analysis – Annual"]
    productattributesummaryview_KEYSTY(["productattributesummaryview.KEYSTY"]) --> REPORT
    product_dim_le_department_code(["product_dim_le.department_code"]) --> REPORT
    productattributesummaryview_MSTAT(["productattributesummaryview.MSTAT"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year(["date_dim.actual_date.Variation.Date Hierarchy.Year"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    product_dim_le_Sub_Class_Label(["product_dim_le.Sub-Class Label"]) --> REPORT
    date_dim_fiscal_year(["date_dim.fiscal_year"]) --> REPORT
    date_dim_fiscalQtr(["date_dim.fiscalQtr"]) --> REPORT
    date_dim_fiscalPer(["date_dim.fiscalPer"]) --> REPORT
    date_dim_fiscalWk(["date_dim.fiscalWk"]) --> REPORT
    d365LocationMapping_View_inventlocationid(["d365LocationMapping_View.inventlocationid"]) --> REPORT
    product_dim_le_Class_Label(["product_dim_le.Class Label"]) --> REPORT
    product_dim_le_style_desc(["product_dim_le.style_desc"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_01_(["weeklyOnHandView.BOP ON Units:Total ( Week 01)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_02_(["weeklyOnHandView.BOP ON Units:Total ( Week 02)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_03_(["weeklyOnHandView.BOP ON Units:Total ( Week 03)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_04_(["weeklyOnHandView.BOP ON Units:Total ( Week 04)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_05_(["weeklyOnHandView.BOP ON Units:Total ( Week 05)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_06_(["weeklyOnHandView.BOP ON Units:Total ( Week 06)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_07_(["weeklyOnHandView.BOP ON Units:Total ( Week 07)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_08_(["weeklyOnHandView.BOP ON Units:Total ( Week 08)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_09_(["weeklyOnHandView.BOP ON Units:Total ( Week 09)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_10_(["weeklyOnHandView.BOP ON Units:Total ( Week 10)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_11_(["weeklyOnHandView.BOP ON Units:Total ( Week 11)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_12_(["weeklyOnHandView.BOP ON Units:Total ( Week 12)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_13_(["weeklyOnHandView.BOP ON Units:Total ( Week 13)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_14_(["weeklyOnHandView.BOP ON Units:Total ( Week 14)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_15_(["weeklyOnHandView.BOP ON Units:Total ( Week 15)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_16_(["weeklyOnHandView.BOP ON Units:Total ( Week 16)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_17_(["weeklyOnHandView.BOP ON Units:Total ( Week 17)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_18_(["weeklyOnHandView.BOP ON Units:Total ( Week 18)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_19_(["weeklyOnHandView.BOP ON Units:Total ( Week 19)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_20_(["weeklyOnHandView.BOP ON Units:Total ( Week 20)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_21_(["weeklyOnHandView.BOP ON Units:Total ( Week 21)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_22_(["weeklyOnHandView.BOP ON Units:Total ( Week 22)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_23_(["weeklyOnHandView.BOP ON Units:Total ( Week 23)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_24_(["weeklyOnHandView.BOP ON Units:Total ( Week 24)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_25_(["weeklyOnHandView.BOP ON Units:Total ( Week 25)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_26_(["weeklyOnHandView.BOP ON Units:Total ( Week 26)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_27_(["weeklyOnHandView.BOP ON Units:Total ( Week 27)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_28_(["weeklyOnHandView.BOP ON Units:Total ( Week 28)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_29_(["weeklyOnHandView.BOP ON Units:Total ( Week 29)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_30_(["weeklyOnHandView.BOP ON Units:Total ( Week 30)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_31_(["weeklyOnHandView.BOP ON Units:Total ( Week 31)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_32_(["weeklyOnHandView.BOP ON Units:Total ( Week 32)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_33_(["weeklyOnHandView.BOP ON Units:Total ( Week 33)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_34_(["weeklyOnHandView.BOP ON Units:Total ( Week 34)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_35_(["weeklyOnHandView.BOP ON Units:Total ( Week 35)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_36_(["weeklyOnHandView.BOP ON Units:Total ( Week 36)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_37_(["weeklyOnHandView.BOP ON Units:Total ( Week 37)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_38_(["weeklyOnHandView.BOP ON Units:Total ( Week 38)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_39_(["weeklyOnHandView.BOP ON Units:Total ( Week 39)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_40_(["weeklyOnHandView.BOP ON Units:Total ( Week 40)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_41_(["weeklyOnHandView.BOP ON Units:Total ( Week 41)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_42_(["weeklyOnHandView.BOP ON Units:Total ( Week 42)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_43_(["weeklyOnHandView.BOP ON Units:Total ( Week 43)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_44_(["weeklyOnHandView.BOP ON Units:Total ( Week 44)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_45_(["weeklyOnHandView.BOP ON Units:Total ( Week 45)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_46_(["weeklyOnHandView.BOP ON Units:Total ( Week 46)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_47_(["weeklyOnHandView.BOP ON Units:Total ( Week 47)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_48_(["weeklyOnHandView.BOP ON Units:Total ( Week 48)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_49_(["weeklyOnHandView.BOP ON Units:Total ( Week 49)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_50_(["weeklyOnHandView.BOP ON Units:Total ( Week 50)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_51_(["weeklyOnHandView.BOP ON Units:Total ( Week 51)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_52_(["weeklyOnHandView.BOP ON Units:Total ( Week 52)"]) --> REPORT
    weeklyOnHandView_BOP_ON_Units_Total___Week_53_(["weeklyOnHandView.BOP ON Units:Total ( Week 53)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__01_(["WeeklySalesView.Net Sales Units (01)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__02_(["WeeklySalesView.Net Sales Units (02)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__03_(["WeeklySalesView.Net Sales Units (03)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__04_(["WeeklySalesView.Net Sales Units (04)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__05_(["WeeklySalesView.Net Sales Units (05)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__06_(["WeeklySalesView.Net Sales Units (06)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__07_(["WeeklySalesView.Net Sales Units (07)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__08_(["WeeklySalesView.Net Sales Units (08)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__09_(["WeeklySalesView.Net Sales Units (09)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__10_(["WeeklySalesView.Net Sales Units (10)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__11_(["WeeklySalesView.Net Sales Units (11)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__12_(["WeeklySalesView.Net Sales Units (12)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__13_(["WeeklySalesView.Net Sales Units (13)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__14_(["WeeklySalesView.Net Sales Units (14)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__15_(["WeeklySalesView.Net Sales Units (15)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__16_(["WeeklySalesView.Net Sales Units (16)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__17_(["WeeklySalesView.Net Sales Units (17)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__18_(["WeeklySalesView.Net Sales Units (18)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__19_(["WeeklySalesView.Net Sales Units (19)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__20_(["WeeklySalesView.Net Sales Units (20)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__21_(["WeeklySalesView.Net Sales Units (21)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__22_(["WeeklySalesView.Net Sales Units (22)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__23_(["WeeklySalesView.Net Sales Units (23)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__24_(["WeeklySalesView.Net Sales Units (24)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__25_(["WeeklySalesView.Net Sales Units (25)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__26_(["WeeklySalesView.Net Sales Units (26)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__27_(["WeeklySalesView.Net Sales Units (27)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__28_(["WeeklySalesView.Net Sales Units (28)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__29_(["WeeklySalesView.Net Sales Units (29)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__30_(["WeeklySalesView.Net Sales Units (30)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__31_(["WeeklySalesView.Net Sales Units (31)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__32_(["WeeklySalesView.Net Sales Units (32)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__33_(["WeeklySalesView.Net Sales Units (33)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__34_(["WeeklySalesView.Net Sales Units (34)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__35_(["WeeklySalesView.Net Sales Units (35)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__36_(["WeeklySalesView.Net Sales Units (36)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__37_(["WeeklySalesView.Net Sales Units (37)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__38_(["WeeklySalesView.Net Sales Units (38)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__39_(["WeeklySalesView.Net Sales Units (39)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__40_(["WeeklySalesView.Net Sales Units (40)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__41_(["WeeklySalesView.Net Sales Units (41)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__42_(["WeeklySalesView.Net Sales Units (42)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__43_(["WeeklySalesView.Net Sales Units (43)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__44_(["WeeklySalesView.Net Sales Units (44)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__45_(["WeeklySalesView.Net Sales Units (45)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__46_(["WeeklySalesView.Net Sales Units (46)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__47_(["WeeklySalesView.Net Sales Units (47)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__48_(["WeeklySalesView.Net Sales Units (48)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__49_(["WeeklySalesView.Net Sales Units (49)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__50_(["WeeklySalesView.Net Sales Units (50)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__51_(["WeeklySalesView.Net Sales Units (51)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__52_(["WeeklySalesView.Net Sales Units (52)"]) --> REPORT
    WeeklySalesView_Net_Sales_Units__53_(["WeeklySalesView.Net Sales Units (53)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_01_(["WeeklySalesView.Received Units ( Week 01)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_02_(["WeeklySalesView.Received Units ( Week 02)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_03_(["WeeklySalesView.Received Units ( Week 03)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_04_(["WeeklySalesView.Received Units ( Week 04)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_05_(["WeeklySalesView.Received Units ( Week 05)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_06_(["WeeklySalesView.Received Units ( Week 06)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_07_(["WeeklySalesView.Received Units ( Week 07)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_08_(["WeeklySalesView.Received Units ( Week 08)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_09_(["WeeklySalesView.Received Units ( Week 09)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_10_(["WeeklySalesView.Received Units ( Week 10)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_11_(["WeeklySalesView.Received Units ( Week 11)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_12_(["WeeklySalesView.Received Units ( Week 12)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_13_(["WeeklySalesView.Received Units ( Week 13)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_14_(["WeeklySalesView.Received Units ( Week 14)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_15_(["WeeklySalesView.Received Units ( Week 15)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_16_(["WeeklySalesView.Received Units ( Week 16)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_17_(["WeeklySalesView.Received Units ( Week 17)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_18_(["WeeklySalesView.Received Units ( Week 18)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_19_(["WeeklySalesView.Received Units ( Week 19)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_20_(["WeeklySalesView.Received Units ( Week 20)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_21_(["WeeklySalesView.Received Units ( Week 21)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_22_(["WeeklySalesView.Received Units ( Week 22)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_23_(["WeeklySalesView.Received Units ( Week 23)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_24_(["WeeklySalesView.Received Units ( Week 24)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_25_(["WeeklySalesView.Received Units ( Week 25)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_26_(["WeeklySalesView.Received Units ( Week 26)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_27_(["WeeklySalesView.Received Units ( Week 27)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_28_(["WeeklySalesView.Received Units ( Week 28)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_29_(["WeeklySalesView.Received Units ( Week 29)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_30_(["WeeklySalesView.Received Units ( Week 30)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_31_(["WeeklySalesView.Received Units ( Week 31)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_32_(["WeeklySalesView.Received Units ( Week 32)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_33_(["WeeklySalesView.Received Units ( Week 33)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_34_(["WeeklySalesView.Received Units ( Week 34)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_35_(["WeeklySalesView.Received Units ( Week 35)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_36_(["WeeklySalesView.Received Units ( Week 36)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_37_(["WeeklySalesView.Received Units ( Week 37)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_38_(["WeeklySalesView.Received Units ( Week 38)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_39_(["WeeklySalesView.Received Units ( Week 39)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_40_(["WeeklySalesView.Received Units ( Week 40)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_41_(["WeeklySalesView.Received Units ( Week 41)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_42_(["WeeklySalesView.Received Units ( Week 42)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_43_(["WeeklySalesView.Received Units ( Week 43)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_44_(["WeeklySalesView.Received Units ( Week 44)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_45_(["WeeklySalesView.Received Units ( Week 45)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_46_(["WeeklySalesView.Received Units ( Week 46)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_47_(["WeeklySalesView.Received Units ( Week 47)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_48_(["WeeklySalesView.Received Units ( Week 48)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_49_(["WeeklySalesView.Received Units ( Week 49)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_50_(["WeeklySalesView.Received Units ( Week 50)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_51_(["WeeklySalesView.Received Units ( Week 51)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_52_(["WeeklySalesView.Received Units ( Week 52)"]) --> REPORT
    WeeklySalesView_Received_Units___Week_53_(["WeeklySalesView.Received Units ( Week 53)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_01_(["WeeklyOnOrderView.On Order Units ( Week 01)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_02_(["WeeklyOnOrderView.On Order Units ( Week 02)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_03_(["WeeklyOnOrderView.On Order Units ( Week 03)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_04_(["WeeklyOnOrderView.On Order Units ( Week 04)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_05_(["WeeklyOnOrderView.On Order Units ( Week 05)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_06_(["WeeklyOnOrderView.On Order Units ( Week 06)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_07_(["WeeklyOnOrderView.On Order Units ( Week 07)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_08_(["WeeklyOnOrderView.On Order Units ( Week 08)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_09_(["WeeklyOnOrderView.On Order Units ( Week 09)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_10_(["WeeklyOnOrderView.On Order Units ( Week 10)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_11_(["WeeklyOnOrderView.On Order Units ( Week 11)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_12_(["WeeklyOnOrderView.On Order Units ( Week 12)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_13_(["WeeklyOnOrderView.On Order Units ( Week 13)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_14_(["WeeklyOnOrderView.On Order Units ( Week 14)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_15_(["WeeklyOnOrderView.On Order Units ( Week 15)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_16_(["WeeklyOnOrderView.On Order Units ( Week 16)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_17_(["WeeklyOnOrderView.On Order Units ( Week 17)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_18_(["WeeklyOnOrderView.On Order Units ( Week 18)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_19_(["WeeklyOnOrderView.On Order Units ( Week 19)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_20_(["WeeklyOnOrderView.On Order Units ( Week 20)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_21_(["WeeklyOnOrderView.On Order Units ( Week 21)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_22_(["WeeklyOnOrderView.On Order Units ( Week 22)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_23_(["WeeklyOnOrderView.On Order Units ( Week 23)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_24_(["WeeklyOnOrderView.On Order Units ( Week 24)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_25_(["WeeklyOnOrderView.On Order Units ( Week 25)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_26_(["WeeklyOnOrderView.On Order Units ( Week 26)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_27_(["WeeklyOnOrderView.On Order Units ( Week 27)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_28_(["WeeklyOnOrderView.On Order Units ( Week 28)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_29_(["WeeklyOnOrderView.On Order Units ( Week 29)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_30_(["WeeklyOnOrderView.On Order Units ( Week 30)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_31_(["WeeklyOnOrderView.On Order Units ( Week 31)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_32_(["WeeklyOnOrderView.On Order Units ( Week 32)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_33_(["WeeklyOnOrderView.On Order Units ( Week 33)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_34_(["WeeklyOnOrderView.On Order Units ( Week 34)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_35_(["WeeklyOnOrderView.On Order Units ( Week 35)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_36_(["WeeklyOnOrderView.On Order Units ( Week 36)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_37_(["WeeklyOnOrderView.On Order Units ( Week 37)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_38_(["WeeklyOnOrderView.On Order Units ( Week 38)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_39_(["WeeklyOnOrderView.On Order Units ( Week 39)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_40_(["WeeklyOnOrderView.On Order Units ( Week 40)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_41_(["WeeklyOnOrderView.On Order Units ( Week 41)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_42_(["WeeklyOnOrderView.On Order Units ( Week 42)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_43_(["WeeklyOnOrderView.On Order Units ( Week 43)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_44_(["WeeklyOnOrderView.On Order Units ( Week 44)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_45_(["WeeklyOnOrderView.On Order Units ( Week 45)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_46_(["WeeklyOnOrderView.On Order Units ( Week 46)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_47_(["WeeklyOnOrderView.On Order Units ( Week 47)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_48_(["WeeklyOnOrderView.On Order Units ( Week 48)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_49_(["WeeklyOnOrderView.On Order Units ( Week 49)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_50_(["WeeklyOnOrderView.On Order Units ( Week 50)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_51_(["WeeklyOnOrderView.On Order Units ( Week 51)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_52_(["WeeklyOnOrderView.On Order Units ( Week 52)"]) --> REPORT
    WeeklyOnOrderView_On_Order_Units___Week_53_(["WeeklyOnOrderView.On Order Units ( Week 53)"]) --> REPORT
    product_dim_le_Department_Label(["product_dim_le.Department Label"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_1_(["weeklyOnHandView.BOP OH retail (month 1)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_2_(["weeklyOnHandView.BOP OH retail (month 2)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_3_(["weeklyOnHandView.BOP OH retail (month 3)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_4_(["weeklyOnHandView.BOP OH retail (month 4)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_5_(["weeklyOnHandView.BOP OH retail (month 5)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_6_(["weeklyOnHandView.BOP OH retail (month 6)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_7_(["weeklyOnHandView.BOP OH retail (month 7)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_8_(["weeklyOnHandView.BOP OH retail (month 8)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_9_(["weeklyOnHandView.BOP OH retail (month 9)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_10_(["weeklyOnHandView.BOP OH retail (month 10)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_11_(["weeklyOnHandView.BOP OH retail (month 11)"]) --> REPORT
    weeklyOnHandView_BOP_OH_retail__month_12_(["weeklyOnHandView.BOP OH retail (month 12)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_1_(["WeeklySalesView.Net receipts retail (month 1)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_2_(["WeeklySalesView.Net receipts retail (month 2)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_3_(["WeeklySalesView.Net receipts retail (month 3)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_4_(["WeeklySalesView.Net receipts retail (month 4)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_5_(["WeeklySalesView.Net receipts retail (month 5)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_6_(["WeeklySalesView.Net receipts retail (month 6)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_7_(["WeeklySalesView.Net receipts retail (month 7)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_8_(["WeeklySalesView.Net receipts retail (month 8)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_9_(["WeeklySalesView.Net receipts retail (month 9)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_10_(["WeeklySalesView.Net receipts retail (month 10)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_11_(["WeeklySalesView.Net receipts retail (month 11)"]) --> REPORT
    WeeklySalesView_Net_receipts_retail__month_12_(["WeeklySalesView.Net receipts retail (month 12)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_1_(["WeeklyOnOrderView.OO Retail (month 1)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_2_(["WeeklyOnOrderView.OO Retail (month 2)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_3_(["WeeklyOnOrderView.OO Retail (month 3)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_4_(["WeeklyOnOrderView.OO Retail (month 4)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_5_(["WeeklyOnOrderView.OO Retail (month 5)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_6_(["WeeklyOnOrderView.OO Retail (month 6)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_7_(["WeeklyOnOrderView.OO Retail (month 7)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_8_(["WeeklyOnOrderView.OO Retail (month 8)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_9_(["WeeklyOnOrderView.OO Retail (month 9)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_10_(["WeeklyOnOrderView.OO Retail (month 10)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_11_(["WeeklyOnOrderView.OO Retail (month 11)"]) --> REPORT
    WeeklyOnOrderView_OO_Retail__month_12_(["WeeklyOnOrderView.OO Retail (month 12)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_1_(["WeeklyOnOrderView.pass due on order (month 1)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_2_(["WeeklyOnOrderView.pass due on order (month 2)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_3_(["WeeklyOnOrderView.pass due on order (month 3)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_4_(["WeeklyOnOrderView.pass due on order (month 4)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_5_(["WeeklyOnOrderView.pass due on order (month 5)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_6_(["WeeklyOnOrderView.pass due on order (month 6)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_7_(["WeeklyOnOrderView.pass due on order (month 7)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_9_(["WeeklyOnOrderView.pass due on order (month 9)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_8_(["WeeklyOnOrderView.pass due on order (month 8)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_10_(["WeeklyOnOrderView.pass due on order (month 10)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_11_(["WeeklyOnOrderView.pass due on order (month 11)"]) --> REPORT
    WeeklyOnOrderView_pass_due_on_order__month_12_(["WeeklyOnOrderView.pass due on order (month 12)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_1_(["WeeklySalesView.Permanent markdowns (month 1)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_2_(["WeeklySalesView.Permanent markdowns (month 2)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_3_(["WeeklySalesView.Permanent markdowns (month 3)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_4_(["WeeklySalesView.Permanent markdowns (month 4)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_5_(["WeeklySalesView.Permanent markdowns (month 5)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_6_(["WeeklySalesView.Permanent markdowns (month 6)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_7_(["WeeklySalesView.Permanent markdowns (month 7)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_8_(["WeeklySalesView.Permanent markdowns (month 8)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_9_(["WeeklySalesView.Permanent markdowns (month 9)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_10_(["WeeklySalesView.Permanent markdowns (month 10)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_11_(["WeeklySalesView.Permanent markdowns (month 11)"]) --> REPORT
    WeeklySalesView_Permanent_markdowns__month_12_(["WeeklySalesView.Permanent markdowns (month 12)"]) --> REPORT
    WeeklySalesView_Promo__month_1_(["WeeklySalesView.Promo (month 1)"]) --> REPORT
    WeeklySalesView_Promo__month_2_(["WeeklySalesView.Promo (month 2)"]) --> REPORT
    WeeklySalesView_Promo__month_3_(["WeeklySalesView.Promo (month 3)"]) --> REPORT
    WeeklySalesView_Promo__month_4_(["WeeklySalesView.Promo (month 4)"]) --> REPORT
    WeeklySalesView_Promo__month_5_(["WeeklySalesView.Promo (month 5)"]) --> REPORT
    WeeklySalesView_Promo__month_6_(["WeeklySalesView.Promo (month 6)"]) --> REPORT
    WeeklySalesView_Promo__month_7_(["WeeklySalesView.Promo (month 7)"]) --> REPORT
    WeeklySalesView_Promo__month_8_(["WeeklySalesView.Promo (month 8)"]) --> REPORT
    WeeklySalesView_Promo__month_9_(["WeeklySalesView.Promo (month 9)"]) --> REPORT
    WeeklySalesView_Promo__month_10_(["WeeklySalesView.Promo (month 10)"]) --> REPORT
    WeeklySalesView_Promo__month_11_(["WeeklySalesView.Promo (month 11)"]) --> REPORT
    WeeklySalesView_Promo__month_12_(["WeeklySalesView.Promo (month 12)"]) --> REPORT
    WeeklySalesView_Shrink__month_1_(["WeeklySalesView.Shrink (month 1)"]) --> REPORT
    WeeklySalesView_Shrink__month_2_(["WeeklySalesView.Shrink (month 2)"]) --> REPORT
    WeeklySalesView_Shrink__month_3_(["WeeklySalesView.Shrink (month 3)"]) --> REPORT
    WeeklySalesView_Shrink__month_4_(["WeeklySalesView.Shrink (month 4)"]) --> REPORT
    WeeklySalesView_Shrink__month_5_(["WeeklySalesView.Shrink (month 5)"]) --> REPORT
    WeeklySalesView_Shrink__month_6_(["WeeklySalesView.Shrink (month 6)"]) --> REPORT
    WeeklySalesView_Shrink__month_7_(["WeeklySalesView.Shrink (month 7)"]) --> REPORT
    WeeklySalesView_Shrink__month_8_(["WeeklySalesView.Shrink (month 8)"]) --> REPORT
    WeeklySalesView_Shrink__month_9_(["WeeklySalesView.Shrink (month 9)"]) --> REPORT
    WeeklySalesView_Shrink__month_10_(["WeeklySalesView.Shrink (month 10)"]) --> REPORT
    WeeklySalesView_Shrink__month_11_(["WeeklySalesView.Shrink (month 11)"]) --> REPORT
    WeeklySalesView_Shrink__month_12_(["WeeklySalesView.Shrink (month 12)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_1_(["WeeklySalesView.Sales Retail (month 1)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_2_(["WeeklySalesView.Sales Retail (month 2)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_3_(["WeeklySalesView.Sales Retail (month 3)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_4_(["WeeklySalesView.Sales Retail (month 4)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_5_(["WeeklySalesView.Sales Retail (month 5)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_6_(["WeeklySalesView.Sales Retail (month 6)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_7_(["WeeklySalesView.Sales Retail (month 7)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_8_(["WeeklySalesView.Sales Retail (month 8)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_9_(["WeeklySalesView.Sales Retail (month 9)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_10_(["WeeklySalesView.Sales Retail (month 10)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_11_(["WeeklySalesView.Sales Retail (month 11)"]) --> REPORT
    WeeklySalesView_Sales_Retail__month_12_(["WeeklySalesView.Sales Retail (month 12)"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| productattributesummaryview.KEYSTY |
| product_dim_le.department_code |
| productattributesummaryview.MSTAT |
| product_dim_le.style_code |
| date_dim.actual_date.Variation.Date Hierarchy.Year |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| date_dim.actual_date |
| product_dim_le.Sub-Class Label |
| date_dim.fiscal_year |
| date_dim.fiscalQtr |
| date_dim.fiscalPer |
| date_dim.fiscalWk |
| d365LocationMapping_View.inventlocationid |
| product_dim_le.Class Label |
| product_dim_le.style_desc |
| weeklyOnHandView.BOP ON Units:Total ( Week 01) |
| weeklyOnHandView.BOP ON Units:Total ( Week 02) |
| weeklyOnHandView.BOP ON Units:Total ( Week 03) |
| weeklyOnHandView.BOP ON Units:Total ( Week 04) |
| weeklyOnHandView.BOP ON Units:Total ( Week 05) |
| weeklyOnHandView.BOP ON Units:Total ( Week 06) |
| weeklyOnHandView.BOP ON Units:Total ( Week 07) |
| weeklyOnHandView.BOP ON Units:Total ( Week 08) |
| weeklyOnHandView.BOP ON Units:Total ( Week 09) |
| weeklyOnHandView.BOP ON Units:Total ( Week 10) |
| weeklyOnHandView.BOP ON Units:Total ( Week 11) |
| weeklyOnHandView.BOP ON Units:Total ( Week 12) |
| weeklyOnHandView.BOP ON Units:Total ( Week 13) |
| weeklyOnHandView.BOP ON Units:Total ( Week 14) |
| weeklyOnHandView.BOP ON Units:Total ( Week 15) |
| weeklyOnHandView.BOP ON Units:Total ( Week 16) |
| weeklyOnHandView.BOP ON Units:Total ( Week 17) |
| weeklyOnHandView.BOP ON Units:Total ( Week 18) |
| weeklyOnHandView.BOP ON Units:Total ( Week 19) |
| weeklyOnHandView.BOP ON Units:Total ( Week 20) |
| weeklyOnHandView.BOP ON Units:Total ( Week 21) |
| weeklyOnHandView.BOP ON Units:Total ( Week 22) |
| weeklyOnHandView.BOP ON Units:Total ( Week 23) |
| weeklyOnHandView.BOP ON Units:Total ( Week 24) |
| weeklyOnHandView.BOP ON Units:Total ( Week 25) |
| weeklyOnHandView.BOP ON Units:Total ( Week 26) |
| weeklyOnHandView.BOP ON Units:Total ( Week 27) |
| weeklyOnHandView.BOP ON Units:Total ( Week 28) |
| weeklyOnHandView.BOP ON Units:Total ( Week 29) |
| weeklyOnHandView.BOP ON Units:Total ( Week 30) |
| weeklyOnHandView.BOP ON Units:Total ( Week 31) |
| weeklyOnHandView.BOP ON Units:Total ( Week 32) |
| weeklyOnHandView.BOP ON Units:Total ( Week 33) |
| weeklyOnHandView.BOP ON Units:Total ( Week 34) |
| weeklyOnHandView.BOP ON Units:Total ( Week 35) |
| weeklyOnHandView.BOP ON Units:Total ( Week 36) |
| weeklyOnHandView.BOP ON Units:Total ( Week 37) |
| weeklyOnHandView.BOP ON Units:Total ( Week 38) |
| weeklyOnHandView.BOP ON Units:Total ( Week 39) |
| weeklyOnHandView.BOP ON Units:Total ( Week 40) |
| weeklyOnHandView.BOP ON Units:Total ( Week 41) |
| weeklyOnHandView.BOP ON Units:Total ( Week 42) |
| weeklyOnHandView.BOP ON Units:Total ( Week 43) |
| weeklyOnHandView.BOP ON Units:Total ( Week 44) |
| weeklyOnHandView.BOP ON Units:Total ( Week 45) |
| weeklyOnHandView.BOP ON Units:Total ( Week 46) |
| weeklyOnHandView.BOP ON Units:Total ( Week 47) |
| weeklyOnHandView.BOP ON Units:Total ( Week 48) |
| weeklyOnHandView.BOP ON Units:Total ( Week 49) |
| weeklyOnHandView.BOP ON Units:Total ( Week 50) |
| weeklyOnHandView.BOP ON Units:Total ( Week 51) |
| weeklyOnHandView.BOP ON Units:Total ( Week 52) |
| weeklyOnHandView.BOP ON Units:Total ( Week 53) |
| WeeklySalesView.Net Sales Units (01) |
| WeeklySalesView.Net Sales Units (02) |
| WeeklySalesView.Net Sales Units (03) |
| WeeklySalesView.Net Sales Units (04) |
| WeeklySalesView.Net Sales Units (05) |
| WeeklySalesView.Net Sales Units (06) |
| WeeklySalesView.Net Sales Units (07) |
| WeeklySalesView.Net Sales Units (08) |
| WeeklySalesView.Net Sales Units (09) |
| WeeklySalesView.Net Sales Units (10) |
| WeeklySalesView.Net Sales Units (11) |
| WeeklySalesView.Net Sales Units (12) |
| WeeklySalesView.Net Sales Units (13) |
| WeeklySalesView.Net Sales Units (14) |
| WeeklySalesView.Net Sales Units (15) |
| WeeklySalesView.Net Sales Units (16) |
| WeeklySalesView.Net Sales Units (17) |
| WeeklySalesView.Net Sales Units (18) |
| WeeklySalesView.Net Sales Units (19) |
| WeeklySalesView.Net Sales Units (20) |
| WeeklySalesView.Net Sales Units (21) |
| WeeklySalesView.Net Sales Units (22) |
| WeeklySalesView.Net Sales Units (23) |
| WeeklySalesView.Net Sales Units (24) |
| WeeklySalesView.Net Sales Units (25) |
| WeeklySalesView.Net Sales Units (26) |
| WeeklySalesView.Net Sales Units (27) |
| WeeklySalesView.Net Sales Units (28) |
| WeeklySalesView.Net Sales Units (29) |
| WeeklySalesView.Net Sales Units (30) |
| WeeklySalesView.Net Sales Units (31) |
| WeeklySalesView.Net Sales Units (32) |
| WeeklySalesView.Net Sales Units (33) |
| WeeklySalesView.Net Sales Units (34) |
| WeeklySalesView.Net Sales Units (35) |
| WeeklySalesView.Net Sales Units (36) |
| WeeklySalesView.Net Sales Units (37) |
| WeeklySalesView.Net Sales Units (38) |
| WeeklySalesView.Net Sales Units (39) |
| WeeklySalesView.Net Sales Units (40) |
| WeeklySalesView.Net Sales Units (41) |
| WeeklySalesView.Net Sales Units (42) |
| WeeklySalesView.Net Sales Units (43) |
| WeeklySalesView.Net Sales Units (44) |
| WeeklySalesView.Net Sales Units (45) |
| WeeklySalesView.Net Sales Units (46) |
| WeeklySalesView.Net Sales Units (47) |
| WeeklySalesView.Net Sales Units (48) |
| WeeklySalesView.Net Sales Units (49) |
| WeeklySalesView.Net Sales Units (50) |
| WeeklySalesView.Net Sales Units (51) |
| WeeklySalesView.Net Sales Units (52) |
| WeeklySalesView.Net Sales Units (53) |
| WeeklySalesView.Received Units ( Week 01) |
| WeeklySalesView.Received Units ( Week 02) |
| WeeklySalesView.Received Units ( Week 03) |
| WeeklySalesView.Received Units ( Week 04) |
| WeeklySalesView.Received Units ( Week 05) |
| WeeklySalesView.Received Units ( Week 06) |
| WeeklySalesView.Received Units ( Week 07) |
| WeeklySalesView.Received Units ( Week 08) |
| WeeklySalesView.Received Units ( Week 09) |
| WeeklySalesView.Received Units ( Week 10) |
| WeeklySalesView.Received Units ( Week 11) |
| WeeklySalesView.Received Units ( Week 12) |
| WeeklySalesView.Received Units ( Week 13) |
| WeeklySalesView.Received Units ( Week 14) |
| WeeklySalesView.Received Units ( Week 15) |
| WeeklySalesView.Received Units ( Week 16) |
| WeeklySalesView.Received Units ( Week 17) |
| WeeklySalesView.Received Units ( Week 18) |
| WeeklySalesView.Received Units ( Week 19) |
| WeeklySalesView.Received Units ( Week 20) |
| WeeklySalesView.Received Units ( Week 21) |
| WeeklySalesView.Received Units ( Week 22) |
| WeeklySalesView.Received Units ( Week 23) |
| WeeklySalesView.Received Units ( Week 24) |
| WeeklySalesView.Received Units ( Week 25) |
| WeeklySalesView.Received Units ( Week 26) |
| WeeklySalesView.Received Units ( Week 27) |
| WeeklySalesView.Received Units ( Week 28) |
| WeeklySalesView.Received Units ( Week 29) |
| WeeklySalesView.Received Units ( Week 30) |
| WeeklySalesView.Received Units ( Week 31) |
| WeeklySalesView.Received Units ( Week 32) |
| WeeklySalesView.Received Units ( Week 33) |
| WeeklySalesView.Received Units ( Week 34) |
| WeeklySalesView.Received Units ( Week 35) |
| WeeklySalesView.Received Units ( Week 36) |
| WeeklySalesView.Received Units ( Week 37) |
| WeeklySalesView.Received Units ( Week 38) |
| WeeklySalesView.Received Units ( Week 39) |
| WeeklySalesView.Received Units ( Week 40) |
| WeeklySalesView.Received Units ( Week 41) |
| WeeklySalesView.Received Units ( Week 42) |
| WeeklySalesView.Received Units ( Week 43) |
| WeeklySalesView.Received Units ( Week 44) |
| WeeklySalesView.Received Units ( Week 45) |
| WeeklySalesView.Received Units ( Week 46) |
| WeeklySalesView.Received Units ( Week 47) |
| WeeklySalesView.Received Units ( Week 48) |
| WeeklySalesView.Received Units ( Week 49) |
| WeeklySalesView.Received Units ( Week 50) |
| WeeklySalesView.Received Units ( Week 51) |
| WeeklySalesView.Received Units ( Week 52) |
| WeeklySalesView.Received Units ( Week 53) |
| WeeklyOnOrderView.On Order Units ( Week 01) |
| WeeklyOnOrderView.On Order Units ( Week 02) |
| WeeklyOnOrderView.On Order Units ( Week 03) |
| WeeklyOnOrderView.On Order Units ( Week 04) |
| WeeklyOnOrderView.On Order Units ( Week 05) |
| WeeklyOnOrderView.On Order Units ( Week 06) |
| WeeklyOnOrderView.On Order Units ( Week 07) |
| WeeklyOnOrderView.On Order Units ( Week 08) |
| WeeklyOnOrderView.On Order Units ( Week 09) |
| WeeklyOnOrderView.On Order Units ( Week 10) |
| WeeklyOnOrderView.On Order Units ( Week 11) |
| WeeklyOnOrderView.On Order Units ( Week 12) |
| WeeklyOnOrderView.On Order Units ( Week 13) |
| WeeklyOnOrderView.On Order Units ( Week 14) |
| WeeklyOnOrderView.On Order Units ( Week 15) |
| WeeklyOnOrderView.On Order Units ( Week 16) |
| WeeklyOnOrderView.On Order Units ( Week 17) |
| WeeklyOnOrderView.On Order Units ( Week 18) |
| WeeklyOnOrderView.On Order Units ( Week 19) |
| WeeklyOnOrderView.On Order Units ( Week 20) |
| WeeklyOnOrderView.On Order Units ( Week 21) |
| WeeklyOnOrderView.On Order Units ( Week 22) |
| WeeklyOnOrderView.On Order Units ( Week 23) |
| WeeklyOnOrderView.On Order Units ( Week 24) |
| WeeklyOnOrderView.On Order Units ( Week 25) |
| WeeklyOnOrderView.On Order Units ( Week 26) |
| WeeklyOnOrderView.On Order Units ( Week 27) |
| WeeklyOnOrderView.On Order Units ( Week 28) |
| WeeklyOnOrderView.On Order Units ( Week 29) |
| WeeklyOnOrderView.On Order Units ( Week 30) |
| WeeklyOnOrderView.On Order Units ( Week 31) |
| WeeklyOnOrderView.On Order Units ( Week 32) |
| WeeklyOnOrderView.On Order Units ( Week 33) |
| WeeklyOnOrderView.On Order Units ( Week 34) |
| WeeklyOnOrderView.On Order Units ( Week 35) |
| WeeklyOnOrderView.On Order Units ( Week 36) |
| WeeklyOnOrderView.On Order Units ( Week 37) |
| WeeklyOnOrderView.On Order Units ( Week 38) |
| WeeklyOnOrderView.On Order Units ( Week 39) |
| WeeklyOnOrderView.On Order Units ( Week 40) |
| WeeklyOnOrderView.On Order Units ( Week 41) |
| WeeklyOnOrderView.On Order Units ( Week 42) |
| WeeklyOnOrderView.On Order Units ( Week 43) |
| WeeklyOnOrderView.On Order Units ( Week 44) |
| WeeklyOnOrderView.On Order Units ( Week 45) |
| WeeklyOnOrderView.On Order Units ( Week 46) |
| WeeklyOnOrderView.On Order Units ( Week 47) |
| WeeklyOnOrderView.On Order Units ( Week 48) |
| WeeklyOnOrderView.On Order Units ( Week 49) |
| WeeklyOnOrderView.On Order Units ( Week 50) |
| WeeklyOnOrderView.On Order Units ( Week 51) |
| WeeklyOnOrderView.On Order Units ( Week 52) |
| WeeklyOnOrderView.On Order Units ( Week 53) |
| product_dim_le.Department Label |
| weeklyOnHandView.BOP OH retail (month 1) |
| weeklyOnHandView.BOP OH retail (month 2) |
| weeklyOnHandView.BOP OH retail (month 3) |
| weeklyOnHandView.BOP OH retail (month 4) |
| weeklyOnHandView.BOP OH retail (month 5) |
| weeklyOnHandView.BOP OH retail (month 6) |
| weeklyOnHandView.BOP OH retail (month 7) |
| weeklyOnHandView.BOP OH retail (month 8) |
| weeklyOnHandView.BOP OH retail (month 9) |
| weeklyOnHandView.BOP OH retail (month 10) |
| weeklyOnHandView.BOP OH retail (month 11) |
| weeklyOnHandView.BOP OH retail (month 12) |
| WeeklySalesView.Net receipts retail (month 1) |
| WeeklySalesView.Net receipts retail (month 2) |
| WeeklySalesView.Net receipts retail (month 3) |
| WeeklySalesView.Net receipts retail (month 4) |
| WeeklySalesView.Net receipts retail (month 5) |
| WeeklySalesView.Net receipts retail (month 6) |
| WeeklySalesView.Net receipts retail (month 7) |
| WeeklySalesView.Net receipts retail (month 8) |
| WeeklySalesView.Net receipts retail (month 9) |
| WeeklySalesView.Net receipts retail (month 10) |
| WeeklySalesView.Net receipts retail (month 11) |
| WeeklySalesView.Net receipts retail (month 12) |
| WeeklyOnOrderView.OO Retail (month 1) |
| WeeklyOnOrderView.OO Retail (month 2) |
| WeeklyOnOrderView.OO Retail (month 3) |
| WeeklyOnOrderView.OO Retail (month 4) |
| WeeklyOnOrderView.OO Retail (month 5) |
| WeeklyOnOrderView.OO Retail (month 6) |
| WeeklyOnOrderView.OO Retail (month 7) |
| WeeklyOnOrderView.OO Retail (month 8) |
| WeeklyOnOrderView.OO Retail (month 9) |
| WeeklyOnOrderView.OO Retail (month 10) |
| WeeklyOnOrderView.OO Retail (month 11) |
| WeeklyOnOrderView.OO Retail (month 12) |
| WeeklyOnOrderView.pass due on order (month 1) |
| WeeklyOnOrderView.pass due on order (month 2) |
| WeeklyOnOrderView.pass due on order (month 3) |
| WeeklyOnOrderView.pass due on order (month 4) |
| WeeklyOnOrderView.pass due on order (month 5) |
| WeeklyOnOrderView.pass due on order (month 6) |
| WeeklyOnOrderView.pass due on order (month 7) |
| WeeklyOnOrderView.pass due on order (month 9) |
| WeeklyOnOrderView.pass due on order (month 8) |
| WeeklyOnOrderView.pass due on order (month 10) |
| WeeklyOnOrderView.pass due on order (month 11) |
| WeeklyOnOrderView.pass due on order (month 12) |
| WeeklySalesView.Permanent markdowns (month 1) |
| WeeklySalesView.Permanent markdowns (month 2) |
| WeeklySalesView.Permanent markdowns (month 3) |
| WeeklySalesView.Permanent markdowns (month 4) |
| WeeklySalesView.Permanent markdowns (month 5) |
| WeeklySalesView.Permanent markdowns (month 6) |
| WeeklySalesView.Permanent markdowns (month 7) |
| WeeklySalesView.Permanent markdowns (month 8) |
| WeeklySalesView.Permanent markdowns (month 9) |
| WeeklySalesView.Permanent markdowns (month 10) |
| WeeklySalesView.Permanent markdowns (month 11) |
| WeeklySalesView.Permanent markdowns (month 12) |
| WeeklySalesView.Promo (month 1) |
| WeeklySalesView.Promo (month 2) |
| WeeklySalesView.Promo (month 3) |
| WeeklySalesView.Promo (month 4) |
| WeeklySalesView.Promo (month 5) |
| WeeklySalesView.Promo (month 6) |
| WeeklySalesView.Promo (month 7) |
| WeeklySalesView.Promo (month 8) |
| WeeklySalesView.Promo (month 9) |
| WeeklySalesView.Promo (month 10) |
| WeeklySalesView.Promo (month 11) |
| WeeklySalesView.Promo (month 12) |
| WeeklySalesView.Shrink (month 1) |
| WeeklySalesView.Shrink (month 2) |
| WeeklySalesView.Shrink (month 3) |
| WeeklySalesView.Shrink (month 4) |
| WeeklySalesView.Shrink (month 5) |
| WeeklySalesView.Shrink (month 6) |
| WeeklySalesView.Shrink (month 7) |
| WeeklySalesView.Shrink (month 8) |
| WeeklySalesView.Shrink (month 9) |
| WeeklySalesView.Shrink (month 10) |
| WeeklySalesView.Shrink (month 11) |
| WeeklySalesView.Shrink (month 12) |
| WeeklySalesView.Sales Retail (month 1) |
| WeeklySalesView.Sales Retail (month 2) |
| WeeklySalesView.Sales Retail (month 3) |
| WeeklySalesView.Sales Retail (month 4) |
| WeeklySalesView.Sales Retail (month 5) |
| WeeklySalesView.Sales Retail (month 6) |
| WeeklySalesView.Sales Retail (month 7) |
| WeeklySalesView.Sales Retail (month 8) |
| WeeklySalesView.Sales Retail (month 9) |
| WeeklySalesView.Sales Retail (month 10) |
| WeeklySalesView.Sales Retail (month 11) |
| WeeklySalesView.Sales Retail (month 12) |

## Pages

| Page | Visuals |
|---|---|
| 53 Week Inventory and Sales Ladder Analysis | 25 |
| Ladder Data | 25 |

## Visuals

### 53 Week Inventory and Sales Ladder Analysis

| Visual | Type | Fields |
|---|---|---|
| 07e1e92fd438b7152740 | slicer | productattributesummaryview.KEYSTY |
| 0990f82a5dbf1a44dadb | slicer | product_dim_le.department_code |
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 0f34aad867ab56402702 | slicer | productattributesummaryview.MSTAT |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 2c050ec017a6225d6f41 | slicer | product_dim_le.style_code |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6f0031da695b744bd74a | textbox |  |
| 78a75b805ddddeda9cd7 | actionButton |  |
| 826e14c9840c3793285e | unknown |  |
| 97f4637b9433dd67029c | textFilter25A4896A83E0487089E2B90C9AE57C8A | product_dim_le.style_code |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| b139070dffc54f413671 | slicer | product_dim_le.Sub-Class Label |
| cc9c621b0f8156219228 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | textSlicer | d365LocationMapping_View.inventlocationid |
| e0290b3bdcd982dcae6f | tableEx | product_dim_le.department_code, product_dim_le.Class Label, productattributesummaryview.KEYSTY, productattributesummaryview.MSTAT, product_dim_le.style_code, product_dim_le.style_desc, weeklyOnHandView.BOP ON Units:Total ( Week 01), weeklyOnHandView.BOP ON Units:Total ( Week 02), weeklyOnHandView.BOP ON Units:Total ( Week 03), weeklyOnHandView.BOP ON Units:Total ( Week 04), weeklyOnHandView.BOP ON Units:Total ( Week 05), weeklyOnHandView.BOP ON Units:Total ( Week 06), weeklyOnHandView.BOP ON Units:Total ( Week 07), weeklyOnHandView.BOP ON Units:Total ( Week 08), weeklyOnHandView.BOP ON Units:Total ( Week 09), weeklyOnHandView.BOP ON Units:Total ( Week 10), weeklyOnHandView.BOP ON Units:Total ( Week 11), weeklyOnHandView.BOP ON Units:Total ( Week 12), weeklyOnHandView.BOP ON Units:Total ( Week 13), weeklyOnHandView.BOP ON Units:Total ( Week 14), weeklyOnHandView.BOP ON Units:Total ( Week 15), weeklyOnHandView.BOP ON Units:Total ( Week 16), weeklyOnHandView.BOP ON Units:Total ( Week 17), weeklyOnHandView.BOP ON Units:Total ( Week 18), weeklyOnHandView.BOP ON Units:Total ( Week 19), weeklyOnHandView.BOP ON Units:Total ( Week 20), weeklyOnHandView.BOP ON Units:Total ( Week 21), weeklyOnHandView.BOP ON Units:Total ( Week 22), weeklyOnHandView.BOP ON Units:Total ( Week 23), weeklyOnHandView.BOP ON Units:Total ( Week 24), weeklyOnHandView.BOP ON Units:Total ( Week 25), weeklyOnHandView.BOP ON Units:Total ( Week 26), weeklyOnHandView.BOP ON Units:Total ( Week 27), weeklyOnHandView.BOP ON Units:Total ( Week 28), weeklyOnHandView.BOP ON Units:Total ( Week 29), weeklyOnHandView.BOP ON Units:Total ( Week 30), weeklyOnHandView.BOP ON Units:Total ( Week 31), weeklyOnHandView.BOP ON Units:Total ( Week 32), weeklyOnHandView.BOP ON Units:Total ( Week 33), weeklyOnHandView.BOP ON Units:Total ( Week 34), weeklyOnHandView.BOP ON Units:Total ( Week 35), weeklyOnHandView.BOP ON Units:Total ( Week 36), weeklyOnHandView.BOP ON Units:Total ( Week 37), weeklyOnHandView.BOP ON Units:Total ( Week 38), weeklyOnHandView.BOP ON Units:Total ( Week 39), weeklyOnHandView.BOP ON Units:Total ( Week 40), weeklyOnHandView.BOP ON Units:Total ( Week 41), weeklyOnHandView.BOP ON Units:Total ( Week 42), weeklyOnHandView.BOP ON Units:Total ( Week 43), weeklyOnHandView.BOP ON Units:Total ( Week 44), weeklyOnHandView.BOP ON Units:Total ( Week 45), weeklyOnHandView.BOP ON Units:Total ( Week 46), weeklyOnHandView.BOP ON Units:Total ( Week 47), weeklyOnHandView.BOP ON Units:Total ( Week 48), weeklyOnHandView.BOP ON Units:Total ( Week 49), weeklyOnHandView.BOP ON Units:Total ( Week 50), weeklyOnHandView.BOP ON Units:Total ( Week 51), weeklyOnHandView.BOP ON Units:Total ( Week 52), weeklyOnHandView.BOP ON Units:Total ( Week 53), WeeklySalesView.Net Sales Units (01), WeeklySalesView.Net Sales Units (02), WeeklySalesView.Net Sales Units (03), WeeklySalesView.Net Sales Units (04), WeeklySalesView.Net Sales Units (05), WeeklySalesView.Net Sales Units (06), WeeklySalesView.Net Sales Units (07), WeeklySalesView.Net Sales Units (08), WeeklySalesView.Net Sales Units (09), WeeklySalesView.Net Sales Units (10), WeeklySalesView.Net Sales Units (11), WeeklySalesView.Net Sales Units (12), WeeklySalesView.Net Sales Units (13), WeeklySalesView.Net Sales Units (14), WeeklySalesView.Net Sales Units (15), WeeklySalesView.Net Sales Units (16), WeeklySalesView.Net Sales Units (17), WeeklySalesView.Net Sales Units (18), WeeklySalesView.Net Sales Units (19), WeeklySalesView.Net Sales Units (20), WeeklySalesView.Net Sales Units (21), WeeklySalesView.Net Sales Units (22), WeeklySalesView.Net Sales Units (23), WeeklySalesView.Net Sales Units (24), WeeklySalesView.Net Sales Units (25), WeeklySalesView.Net Sales Units (26), WeeklySalesView.Net Sales Units (27), WeeklySalesView.Net Sales Units (28), WeeklySalesView.Net Sales Units (29), WeeklySalesView.Net Sales Units (30), WeeklySalesView.Net Sales Units (31), WeeklySalesView.Net Sales Units (32), WeeklySalesView.Net Sales Units (33), WeeklySalesView.Net Sales Units (34), WeeklySalesView.Net Sales Units (35), WeeklySalesView.Net Sales Units (36), WeeklySalesView.Net Sales Units (37), WeeklySalesView.Net Sales Units (38), WeeklySalesView.Net Sales Units (39), WeeklySalesView.Net Sales Units (40), WeeklySalesView.Net Sales Units (41), WeeklySalesView.Net Sales Units (42), WeeklySalesView.Net Sales Units (43), WeeklySalesView.Net Sales Units (44), WeeklySalesView.Net Sales Units (45), WeeklySalesView.Net Sales Units (46), WeeklySalesView.Net Sales Units (47), WeeklySalesView.Net Sales Units (48), WeeklySalesView.Net Sales Units (49), WeeklySalesView.Net Sales Units (50), WeeklySalesView.Net Sales Units (51), WeeklySalesView.Net Sales Units (52), WeeklySalesView.Net Sales Units (53), WeeklySalesView.Received Units ( Week 01), WeeklySalesView.Received Units ( Week 02), WeeklySalesView.Received Units ( Week 03), WeeklySalesView.Received Units ( Week 04), WeeklySalesView.Received Units ( Week 05), WeeklySalesView.Received Units ( Week 06), WeeklySalesView.Received Units ( Week 07), WeeklySalesView.Received Units ( Week 08), WeeklySalesView.Received Units ( Week 09), WeeklySalesView.Received Units ( Week 10), WeeklySalesView.Received Units ( Week 11), WeeklySalesView.Received Units ( Week 12), WeeklySalesView.Received Units ( Week 13), WeeklySalesView.Received Units ( Week 14), WeeklySalesView.Received Units ( Week 15), WeeklySalesView.Received Units ( Week 16), WeeklySalesView.Received Units ( Week 17), WeeklySalesView.Received Units ( Week 18), WeeklySalesView.Received Units ( Week 19), WeeklySalesView.Received Units ( Week 20), WeeklySalesView.Received Units ( Week 21), WeeklySalesView.Received Units ( Week 22), WeeklySalesView.Received Units ( Week 23), WeeklySalesView.Received Units ( Week 24), WeeklySalesView.Received Units ( Week 25), WeeklySalesView.Received Units ( Week 26), WeeklySalesView.Received Units ( Week 27), WeeklySalesView.Received Units ( Week 28), WeeklySalesView.Received Units ( Week 29), WeeklySalesView.Received Units ( Week 30), WeeklySalesView.Received Units ( Week 31), WeeklySalesView.Received Units ( Week 32), WeeklySalesView.Received Units ( Week 33), WeeklySalesView.Received Units ( Week 34), WeeklySalesView.Received Units ( Week 35), WeeklySalesView.Received Units ( Week 36), WeeklySalesView.Received Units ( Week 37), WeeklySalesView.Received Units ( Week 38), WeeklySalesView.Received Units ( Week 39), WeeklySalesView.Received Units ( Week 40), WeeklySalesView.Received Units ( Week 41), WeeklySalesView.Received Units ( Week 42), WeeklySalesView.Received Units ( Week 43), WeeklySalesView.Received Units ( Week 44), WeeklySalesView.Received Units ( Week 45), WeeklySalesView.Received Units ( Week 46), WeeklySalesView.Received Units ( Week 47), WeeklySalesView.Received Units ( Week 48), WeeklySalesView.Received Units ( Week 49), WeeklySalesView.Received Units ( Week 50), WeeklySalesView.Received Units ( Week 51), WeeklySalesView.Received Units ( Week 52), WeeklySalesView.Received Units ( Week 53), WeeklyOnOrderView.On Order Units ( Week 01), WeeklyOnOrderView.On Order Units ( Week 02), WeeklyOnOrderView.On Order Units ( Week 03), WeeklyOnOrderView.On Order Units ( Week 04), WeeklyOnOrderView.On Order Units ( Week 05), WeeklyOnOrderView.On Order Units ( Week 06), WeeklyOnOrderView.On Order Units ( Week 07), WeeklyOnOrderView.On Order Units ( Week 08), WeeklyOnOrderView.On Order Units ( Week 09), WeeklyOnOrderView.On Order Units ( Week 10), WeeklyOnOrderView.On Order Units ( Week 11), WeeklyOnOrderView.On Order Units ( Week 12), WeeklyOnOrderView.On Order Units ( Week 13), WeeklyOnOrderView.On Order Units ( Week 14), WeeklyOnOrderView.On Order Units ( Week 15), WeeklyOnOrderView.On Order Units ( Week 16), WeeklyOnOrderView.On Order Units ( Week 17), WeeklyOnOrderView.On Order Units ( Week 18), WeeklyOnOrderView.On Order Units ( Week 19), WeeklyOnOrderView.On Order Units ( Week 20), WeeklyOnOrderView.On Order Units ( Week 21), WeeklyOnOrderView.On Order Units ( Week 22), WeeklyOnOrderView.On Order Units ( Week 23), WeeklyOnOrderView.On Order Units ( Week 24), WeeklyOnOrderView.On Order Units ( Week 25), WeeklyOnOrderView.On Order Units ( Week 26), WeeklyOnOrderView.On Order Units ( Week 27), WeeklyOnOrderView.On Order Units ( Week 28), WeeklyOnOrderView.On Order Units ( Week 29), WeeklyOnOrderView.On Order Units ( Week 30), WeeklyOnOrderView.On Order Units ( Week 31), WeeklyOnOrderView.On Order Units ( Week 32), WeeklyOnOrderView.On Order Units ( Week 33), WeeklyOnOrderView.On Order Units ( Week 34), WeeklyOnOrderView.On Order Units ( Week 35), WeeklyOnOrderView.On Order Units ( Week 36), WeeklyOnOrderView.On Order Units ( Week 37), WeeklyOnOrderView.On Order Units ( Week 38), WeeklyOnOrderView.On Order Units ( Week 39), WeeklyOnOrderView.On Order Units ( Week 40), WeeklyOnOrderView.On Order Units ( Week 41), WeeklyOnOrderView.On Order Units ( Week 42), WeeklyOnOrderView.On Order Units ( Week 43), WeeklyOnOrderView.On Order Units ( Week 44), WeeklyOnOrderView.On Order Units ( Week 45), WeeklyOnOrderView.On Order Units ( Week 46), WeeklyOnOrderView.On Order Units ( Week 47), WeeklyOnOrderView.On Order Units ( Week 48), WeeklyOnOrderView.On Order Units ( Week 49), WeeklyOnOrderView.On Order Units ( Week 50), WeeklyOnOrderView.On Order Units ( Week 51), WeeklyOnOrderView.On Order Units ( Week 52), WeeklyOnOrderView.On Order Units ( Week 53), product_dim_le.Department Label, product_dim_le.Sub-Class Label |
| e8e740717323d0200f7a | slicer | product_dim_le.Class Label |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f920f4a3989b72fd51af | textbox |  |

### Ladder Data

| Visual | Type | Fields |
|---|---|---|
| 0814a742009129e0860e | textbox |  |
| 0868b470c007d1469082 | slicer | product_dim_le.department_code |
| 0f22f160304d079d1a30 | textbox |  |
| 16055593ac4c47508b69 | actionButton |  |
| 1876af1ad5e47c092d02 | slicer | productattributesummaryview.MSTAT |
| 31ececa104045dc4d927 | slicer | product_dim_le.style_code |
| 3e82850a12d100810a22 | slicer | product_dim_le.Sub-Class Label |
| 40047d9aa6ae2431e600 | bookmarkNavigator |  |
| 43f85f578aaa0794bb0a | actionButton |  |
| 4c377caac0190d171596 | slicer | product_dim_le.Class Label |
| 51fd508fda79cb0ab800 | bookmarkNavigator |  |
| 59306f09a03a4273a611 | textSlicer | d365LocationMapping_View.inventlocationid |
| 5a9124f0aa04299154b0 | image |  |
| 5fcc9a6f078089cbad85 | slicer | date_dim.actual_date |
| 6d43d99c2d700babcd08 | unknown |  |
| 8154d7df8548a2ecc95c | unknown |  |
| 980d19e2815128e8e833 | textbox |  |
| 9ac0f9bc205c0c15d947 | unknown |  |
| 9b9c5e37a7e00079d0a8 | slicer | date_dim.fiscal_year, date_dim.actual_date, date_dim.fiscalQtr, date_dim.fiscalPer, date_dim.fiscalWk |
| b2ed7f074a08b5643e48 | unknown |  |
| c1f372913e41ba4cbc55 | textFilter25A4896A83E0487089E2B90C9AE57C8A | product_dim_le.style_code |
| c3c5c62fec27200a8c02 | slicer | productattributesummaryview.KEYSTY |
| c93155e4e9b202a0e049 | tableEx | product_dim_le.department_code, product_dim_le.Class Label, productattributesummaryview.KEYSTY, productattributesummaryview.MSTAT, product_dim_le.style_code, product_dim_le.style_desc, product_dim_le.Department Label, product_dim_le.Sub-Class Label, weeklyOnHandView.BOP OH retail (month 1), weeklyOnHandView.BOP OH retail (month 2), weeklyOnHandView.BOP OH retail (month 3), weeklyOnHandView.BOP OH retail (month 4), weeklyOnHandView.BOP OH retail (month 5), weeklyOnHandView.BOP OH retail (month 6), weeklyOnHandView.BOP OH retail (month 7), weeklyOnHandView.BOP OH retail (month 8), weeklyOnHandView.BOP OH retail (month 9), weeklyOnHandView.BOP OH retail (month 10), weeklyOnHandView.BOP OH retail (month 11), weeklyOnHandView.BOP OH retail (month 12), WeeklySalesView.Net receipts retail (month 1), WeeklySalesView.Net receipts retail (month 2), WeeklySalesView.Net receipts retail (month 3), WeeklySalesView.Net receipts retail (month 4), WeeklySalesView.Net receipts retail (month 5), WeeklySalesView.Net receipts retail (month 6), WeeklySalesView.Net receipts retail (month 7), WeeklySalesView.Net receipts retail (month 8), WeeklySalesView.Net receipts retail (month 9), WeeklySalesView.Net receipts retail (month 10), WeeklySalesView.Net receipts retail (month 11), WeeklySalesView.Net receipts retail (month 12), WeeklyOnOrderView.OO Retail (month 1), WeeklyOnOrderView.OO Retail (month 2), WeeklyOnOrderView.OO Retail (month 3), WeeklyOnOrderView.OO Retail (month 4), WeeklyOnOrderView.OO Retail (month 5), WeeklyOnOrderView.OO Retail (month 6), WeeklyOnOrderView.OO Retail (month 7), WeeklyOnOrderView.OO Retail (month 8), WeeklyOnOrderView.OO Retail (month 9), WeeklyOnOrderView.OO Retail (month 10), WeeklyOnOrderView.OO Retail (month 11), WeeklyOnOrderView.OO Retail (month 12), WeeklyOnOrderView.pass due on order (month 1), WeeklyOnOrderView.pass due on order (month 2), WeeklyOnOrderView.pass due on order (month 3), WeeklyOnOrderView.pass due on order (month 4), WeeklyOnOrderView.pass due on order (month 5), WeeklyOnOrderView.pass due on order (month 6), WeeklyOnOrderView.pass due on order (month 7), WeeklyOnOrderView.pass due on order (month 9), WeeklyOnOrderView.pass due on order (month 8), WeeklyOnOrderView.pass due on order (month 10), WeeklyOnOrderView.pass due on order (month 11), WeeklyOnOrderView.pass due on order (month 12), WeeklySalesView.Permanent markdowns (month 1), WeeklySalesView.Permanent markdowns (month 2), WeeklySalesView.Permanent markdowns (month 3), WeeklySalesView.Permanent markdowns (month 4), WeeklySalesView.Permanent markdowns (month 5), WeeklySalesView.Permanent markdowns (month 6), WeeklySalesView.Permanent markdowns (month 7), WeeklySalesView.Permanent markdowns (month 8), WeeklySalesView.Permanent markdowns (month 9), WeeklySalesView.Permanent markdowns (month 10), WeeklySalesView.Permanent markdowns (month 11), WeeklySalesView.Permanent markdowns (month 12), WeeklySalesView.Promo (month 1), WeeklySalesView.Promo (month 2), WeeklySalesView.Promo (month 3), WeeklySalesView.Promo (month 4), WeeklySalesView.Promo (month 5), WeeklySalesView.Promo (month 6), WeeklySalesView.Promo (month 7), WeeklySalesView.Promo (month 8), WeeklySalesView.Promo (month 9), WeeklySalesView.Promo (month 10), WeeklySalesView.Promo (month 11), WeeklySalesView.Promo (month 12), WeeklySalesView.Shrink (month 1), WeeklySalesView.Shrink (month 2), WeeklySalesView.Shrink (month 3), WeeklySalesView.Shrink (month 4), WeeklySalesView.Shrink (month 5), WeeklySalesView.Shrink (month 6), WeeklySalesView.Shrink (month 7), WeeklySalesView.Shrink (month 8), WeeklySalesView.Shrink (month 9), WeeklySalesView.Shrink (month 10), WeeklySalesView.Shrink (month 11), WeeklySalesView.Shrink (month 12), WeeklySalesView.Sales Retail (month 1), WeeklySalesView.Sales Retail (month 2), WeeklySalesView.Sales Retail (month 3), WeeklySalesView.Sales Retail (month 4), WeeklySalesView.Sales Retail (month 5), WeeklySalesView.Sales Retail (month 6), WeeklySalesView.Sales Retail (month 7), WeeklySalesView.Sales Retail (month 8), WeeklySalesView.Sales Retail (month 9), WeeklySalesView.Sales Retail (month 10), WeeklySalesView.Sales Retail (month 11), WeeklySalesView.Sales Retail (month 12) |
| d90d748f8a3312393027 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| f26d7286c3a9e9d050b8 | textbox |  |
