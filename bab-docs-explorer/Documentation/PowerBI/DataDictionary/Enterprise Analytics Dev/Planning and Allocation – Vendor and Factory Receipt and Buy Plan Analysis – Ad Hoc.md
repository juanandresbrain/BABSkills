# Planning and Allocation – Vendor and Factory Receipt and Buy Plan Analysis – Ad Hoc

**Workspace:** Enterprise Analytics Dev  
**Report ID:** fd5140a1-3554-45f0-b461-ceea26375e5c  
**Dataset ID:** 05daff4b-5e80-4cd4-94ba-90a3110d5e14  
**Web URL:** https://app.powerbi.com/groups/109bd275-5f44-4366-b343-9b41b5cfb040/reports/fd5140a1-3554-45f0-b461-ceea26375e5c  
**Semantic Model:** [Merchandise Transactional Model](../../SemanticModels/Enterprise Analytics Dev/Merchandise Transactional Model.md)  

## Architecture Diagram

```mermaid
flowchart LR
    REPORT["Planning and Allocation – Vendor and Factory Receipt and Buy Plan Analysis – Ad Hoc"]
    VendorXFFactoryDepartmentView_FactoryLabel(["VendorXFFactoryDepartmentView.FactoryLabel"]) --> REPORT
    date_dim_actual_date(["date_dim.actual_date"]) --> REPORT
    VendorXFFactoryDepartmentView_DepartmentLabel(["VendorXFFactoryDepartmentView.DepartmentLabel"]) --> REPORT
    product_dim_le_chain(["product_dim_le.chain"]) --> REPORT
    VendorXFFactoryDepartmentView_Year(["VendorXFFactoryDepartmentView.Year"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Jan_(["Sum(VendorXFFactoryDepartmentView.Jan)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Feb_(["Sum(VendorXFFactoryDepartmentView.Feb)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Mar_(["Sum(VendorXFFactoryDepartmentView.Mar)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Apr_(["Sum(VendorXFFactoryDepartmentView.Apr)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_May_(["Sum(VendorXFFactoryDepartmentView.May)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Jun_(["Sum(VendorXFFactoryDepartmentView.Jun)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Jul_(["Sum(VendorXFFactoryDepartmentView.Jul)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Aug_(["Sum(VendorXFFactoryDepartmentView.Aug)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Sep_(["Sum(VendorXFFactoryDepartmentView.Sep)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Oct_(["Sum(VendorXFFactoryDepartmentView.Oct)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Nov_(["Sum(VendorXFFactoryDepartmentView.Nov)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Dec_(["Sum(VendorXFFactoryDepartmentView.Dec)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_QTR1_(["Sum(VendorXFFactoryDepartmentView.QTR1)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_QTR2_(["Sum(VendorXFFactoryDepartmentView.QTR2)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_QTR3_(["Sum(VendorXFFactoryDepartmentView.QTR3)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_QTR4_(["Sum(VendorXFFactoryDepartmentView.QTR4)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Total_Year_(["Sum(VendorXFFactoryDepartmentView.Total Year)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Total_Cost_(["Sum(VendorXFFactoryDepartmentView.Total Cost)"]) --> REPORT
    Sum_VendorXFFactoryDepartmentView_Total_Retail_(["Sum(VendorXFFactoryDepartmentView.Total Retail)"]) --> REPORT
    VendorXFFactoryDepartmentView_DepartmentName(["VendorXFFactoryDepartmentView.DepartmentName"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_QTR1_Dept_Total(["VendorXFFactoryDepartmentView.FD QTR1 Dept Total"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_QTR1___Units__Factory_Share_(["VendorXFFactoryDepartmentView.FD QTR1 % Units (Factory Share)"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_QTR2_Dept_Total(["VendorXFFactoryDepartmentView.FD QTR2 Dept Total"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_QTR2___Units__Factory_Share_(["VendorXFFactoryDepartmentView.FD QTR2 % Units (Factory Share)"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_QTR3_Dept_Total(["VendorXFFactoryDepartmentView.FD QTR3 Dept Total"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_QTR3___Units__Factory_Share_(["VendorXFFactoryDepartmentView.FD QTR3 % Units (Factory Share)"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_QTR4_Dept_Total(["VendorXFFactoryDepartmentView.FD QTR4 Dept Total"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_QTR4___Units__Factory_Share_(["VendorXFFactoryDepartmentView.FD QTR4 % Units (Factory Share)"]) --> REPORT
    select(["select"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_Total_Year_Dept_Total(["VendorXFFactoryDepartmentView.FD Total Year Dept Total"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_Total_Year___Units__Factory_Share_(["VendorXFFactoryDepartmentView.FD Total Year % Units (Factory Share)"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_Total_Cost_Dept_Total(["VendorXFFactoryDepartmentView.FD Total Cost Dept Total"]) --> REPORT
    VendorXFFactoryDepartmentView_FD_Total_Cost____Factory_Share_(["VendorXFFactoryDepartmentView.FD Total Cost % (Factory Share)"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Year1(["date_dim.actual_date.Variation.Date Hierarchy.Year1"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Quarter(["date_dim.actual_date.Variation.Date Hierarchy.Quarter"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Month(["date_dim.actual_date.Variation.Date Hierarchy.Month"]) --> REPORT
    date_dim_actual_date_Variation_Date_Hierarchy_Day(["date_dim.actual_date.Variation.Date Hierarchy.Day"]) --> REPORT
    product_dim_le_style_code(["product_dim_le.style_code"]) --> REPORT
    product_dim_le_primary_vendor_code(["product_dim_le.primary_vendor_code"]) --> REPORT
    d365LocationMapping_View_LocationCode(["d365LocationMapping_View.LocationCode"]) --> REPORT
    VendorXFDepartmentView_DepartmentLabel(["VendorXFDepartmentView.DepartmentLabel"]) --> REPORT
    Sum_VendorXFDepartmentView_Jan_(["Sum(VendorXFDepartmentView.Jan)"]) --> REPORT
    Sum_VendorXFDepartmentView_Feb_(["Sum(VendorXFDepartmentView.Feb)"]) --> REPORT
    Sum_VendorXFDepartmentView_Mar_(["Sum(VendorXFDepartmentView.Mar)"]) --> REPORT
    Sum_VendorXFDepartmentView_Apr_(["Sum(VendorXFDepartmentView.Apr)"]) --> REPORT
    Sum_VendorXFDepartmentView_May_(["Sum(VendorXFDepartmentView.May)"]) --> REPORT
    Sum_VendorXFDepartmentView_Jun_(["Sum(VendorXFDepartmentView.Jun)"]) --> REPORT
    Sum_VendorXFDepartmentView_Jul_(["Sum(VendorXFDepartmentView.Jul)"]) --> REPORT
    Sum_VendorXFDepartmentView_Aug_(["Sum(VendorXFDepartmentView.Aug)"]) --> REPORT
    Sum_VendorXFDepartmentView_Sep_(["Sum(VendorXFDepartmentView.Sep)"]) --> REPORT
    Sum_VendorXFDepartmentView_Oct_(["Sum(VendorXFDepartmentView.Oct)"]) --> REPORT
    Sum_VendorXFDepartmentView_Nov_(["Sum(VendorXFDepartmentView.Nov)"]) --> REPORT
    Sum_VendorXFDepartmentView_Dec_(["Sum(VendorXFDepartmentView.Dec)"]) --> REPORT
    Sum_VendorXFDepartmentView_QTR1_(["Sum(VendorXFDepartmentView.QTR1)"]) --> REPORT
    Sum_VendorXFDepartmentView_QTR2_(["Sum(VendorXFDepartmentView.QTR2)"]) --> REPORT
    Sum_VendorXFDepartmentView_QTR3_(["Sum(VendorXFDepartmentView.QTR3)"]) --> REPORT
    Sum_VendorXFDepartmentView_QTR4_(["Sum(VendorXFDepartmentView.QTR4)"]) --> REPORT
    Sum_VendorXFDepartmentView_Total_Year_(["Sum(VendorXFDepartmentView.Total Year)"]) --> REPORT
    Sum_VendorXFDepartmentView_Total_Cost_(["Sum(VendorXFDepartmentView.Total Cost)"]) --> REPORT
    Sum_VendorXFDepartmentView_Total_Retail_(["Sum(VendorXFDepartmentView.Total Retail)"]) --> REPORT
    VendorXFDepartmentView_Year(["VendorXFDepartmentView.Year"]) --> REPORT
    VendorXFDepartmentView_DepartmentName(["VendorXFDepartmentView.DepartmentName"]) --> REPORT
    VendorXFVendorDepartmentView_Year(["VendorXFVendorDepartmentView.Year"]) --> REPORT
    VendorXFVendorDepartmentView_VendorLabel(["VendorXFVendorDepartmentView.VendorLabel"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Jan_(["Sum(VendorXFVendorDepartmentView.Jan)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Feb_(["Sum(VendorXFVendorDepartmentView.Feb)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Mar_(["Sum(VendorXFVendorDepartmentView.Mar)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Apr_(["Sum(VendorXFVendorDepartmentView.Apr)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_May_(["Sum(VendorXFVendorDepartmentView.May)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Jun_(["Sum(VendorXFVendorDepartmentView.Jun)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Jul_(["Sum(VendorXFVendorDepartmentView.Jul)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Aug_(["Sum(VendorXFVendorDepartmentView.Aug)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Sep_(["Sum(VendorXFVendorDepartmentView.Sep)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Oct_(["Sum(VendorXFVendorDepartmentView.Oct)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Nov_(["Sum(VendorXFVendorDepartmentView.Nov)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Dec_(["Sum(VendorXFVendorDepartmentView.Dec)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_QTR1_(["Sum(VendorXFVendorDepartmentView.QTR1)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_QTR2_(["Sum(VendorXFVendorDepartmentView.QTR2)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_QTR3_(["Sum(VendorXFVendorDepartmentView.QTR3)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_QTR4_(["Sum(VendorXFVendorDepartmentView.QTR4)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Total_Year_(["Sum(VendorXFVendorDepartmentView.Total Year)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Total_Cost_(["Sum(VendorXFVendorDepartmentView.Total Cost)"]) --> REPORT
    Sum_VendorXFVendorDepartmentView_Total_Retail_(["Sum(VendorXFVendorDepartmentView.Total Retail)"]) --> REPORT
    VendorXFVendorDepartmentView_DepartmentName(["VendorXFVendorDepartmentView.DepartmentName"]) --> REPORT
    VendorXFVendorDepartmentView_DepartmentLabel(["VendorXFVendorDepartmentView.DepartmentLabel"]) --> REPORT
    VendorXFVendorDepartmentView_VD_QTR1_Vendor_Total(["VendorXFVendorDepartmentView.VD QTR1 Vendor Total"]) --> REPORT
    VendorXFVendorDepartmentView_VD_QTR1___Units__Dept_Share_of_Vendor_(["VendorXFVendorDepartmentView.VD QTR1 % Units (Dept Share of Vendor)"]) --> REPORT
    VendorXFVendorDepartmentView_VD_QTR2_Vendor_Total(["VendorXFVendorDepartmentView.VD QTR2 Vendor Total"]) --> REPORT
    VendorXFVendorDepartmentView_VD_QTR2___Units__Dept_Share_of_Vendor_(["VendorXFVendorDepartmentView.VD QTR2 % Units (Dept Share of Vendor)"]) --> REPORT
    VendorXFVendorDepartmentView_VD_QTR3_Vendor_Total(["VendorXFVendorDepartmentView.VD QTR3 Vendor Total"]) --> REPORT
    VendorXFVendorDepartmentView_VD_QTR3___Units__Dept_Share_of_Vendor_(["VendorXFVendorDepartmentView.VD QTR3 % Units (Dept Share of Vendor)"]) --> REPORT
    VendorXFVendorDepartmentView_VD_QTR4_Vendor_Total(["VendorXFVendorDepartmentView.VD QTR4 Vendor Total"]) --> REPORT
    VendorXFVendorDepartmentView_VD_QTR4___Units__Dept_Share_of_Vendor_(["VendorXFVendorDepartmentView.VD QTR4 % Units (Dept Share of Vendor)"]) --> REPORT
    VendorXFVendorDepartmentView_VD_Total_Year_Vendor_Total(["VendorXFVendorDepartmentView.VD Total Year Vendor Total"]) --> REPORT
    VendorXFVendorDepartmentView_VD_Total_Year___Units__Dept_Share_of_Vendor_(["VendorXFVendorDepartmentView.VD Total Year % Units (Dept Share of Vendor)"]) --> REPORT
    VendorXFVendorDepartmentView_VD_Total_Cost_Vendor_Total(["VendorXFVendorDepartmentView.VD Total Cost Vendor Total"]) --> REPORT
    VendorXFVendorDepartmentView_VD_Total_Cost____Dept_Share_of_Vendor_(["VendorXFVendorDepartmentView.VD Total Cost % (Dept Share of Vendor)"]) --> REPORT
    VendorXFVendorDepartmentView_VendorInvoiceGroup(["VendorXFVendorDepartmentView.VendorInvoiceGroup"]) --> REPORT
    VendorXFItemDetailView_DepartmentName(["VendorXFItemDetailView.DepartmentName"]) --> REPORT
    VendorXFItemDetailView_Factory(["VendorXFItemDetailView.Factory"]) --> REPORT
    VendorXFItemDetailView_Style(["VendorXFItemDetailView.Style"]) --> REPORT
    VendorXFItemDetailView_DepartmentNumber(["VendorXFItemDetailView.DepartmentNumber"]) --> REPORT
    VendorXFItemDetailView_Vendor(["VendorXFItemDetailView.Vendor"]) --> REPORT
    VendorXFItemDetailView_Description(["VendorXFItemDetailView.Description"]) --> REPORT
    VendorXFItemDetailView_VendorName(["VendorXFItemDetailView.VendorName"]) --> REPORT
    Sum_VendorXFItemDetailView_CurrentYearMinus3_(["Sum(VendorXFItemDetailView.CurrentYearMinus3)"]) --> REPORT
    Sum_VendorXFItemDetailView_CurrentYearMinus2_(["Sum(VendorXFItemDetailView.CurrentYearMinus2)"]) --> REPORT
    Sum_VendorXFItemDetailView_CurrentYearMinus1_(["Sum(VendorXFItemDetailView.CurrentYearMinus1)"]) --> REPORT
    Sum_VendorXFItemDetailView_CurrentYear_(["Sum(VendorXFItemDetailView.CurrentYear)"]) --> REPORT
    VendorXFDepartmentVendorView_VendorLabel(["VendorXFDepartmentVendorView.VendorLabel"]) --> REPORT
    VendorXFDepartmentVendorView_DepartmentLabel(["VendorXFDepartmentVendorView.DepartmentLabel"]) --> REPORT
    VendorXFDepartmentVendorView_Year(["VendorXFDepartmentVendorView.Year"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Jan_(["Sum(VendorXFDepartmentVendorView.Jan)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Feb_(["Sum(VendorXFDepartmentVendorView.Feb)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Mar_(["Sum(VendorXFDepartmentVendorView.Mar)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Apr_(["Sum(VendorXFDepartmentVendorView.Apr)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_May_(["Sum(VendorXFDepartmentVendorView.May)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Jun_(["Sum(VendorXFDepartmentVendorView.Jun)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Jul_(["Sum(VendorXFDepartmentVendorView.Jul)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Aug_(["Sum(VendorXFDepartmentVendorView.Aug)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Sep_(["Sum(VendorXFDepartmentVendorView.Sep)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Oct_(["Sum(VendorXFDepartmentVendorView.Oct)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Nov_(["Sum(VendorXFDepartmentVendorView.Nov)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Dec_(["Sum(VendorXFDepartmentVendorView.Dec)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_QTR1_(["Sum(VendorXFDepartmentVendorView.QTR1)"]) --> REPORT
    VendorXFDepartmentVendorView_DV_QTR1_Dept_Total(["VendorXFDepartmentVendorView.DV QTR1 Dept Total"]) --> REPORT
    VendorXFDepartmentVendorView_DV_QTR1___Units__Vendor_Share_(["VendorXFDepartmentVendorView.DV QTR1 % Units (Vendor Share)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_QTR2_(["Sum(VendorXFDepartmentVendorView.QTR2)"]) --> REPORT
    VendorXFDepartmentVendorView_DV_QTR2_Dept_Total(["VendorXFDepartmentVendorView.DV QTR2 Dept Total"]) --> REPORT
    VendorXFDepartmentVendorView_DV_QTR2___Units__Vendor_Share_(["VendorXFDepartmentVendorView.DV QTR2 % Units (Vendor Share)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_QTR3_(["Sum(VendorXFDepartmentVendorView.QTR3)"]) --> REPORT
    VendorXFDepartmentVendorView_DV_QTR3_Dept_Total(["VendorXFDepartmentVendorView.DV QTR3 Dept Total"]) --> REPORT
    VendorXFDepartmentVendorView_DV_QTR3___Units__Vendor_Share_(["VendorXFDepartmentVendorView.DV QTR3 % Units (Vendor Share)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_QTR4_(["Sum(VendorXFDepartmentVendorView.QTR4)"]) --> REPORT
    VendorXFDepartmentVendorView_DV_QTR4_Dept_Total(["VendorXFDepartmentVendorView.DV QTR4 Dept Total"]) --> REPORT
    VendorXFDepartmentVendorView_DV_QTR4___Units__Vendor_Share_(["VendorXFDepartmentVendorView.DV QTR4 % Units (Vendor Share)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Total_Year_(["Sum(VendorXFDepartmentVendorView.Total Year)"]) --> REPORT
    VendorXFDepartmentVendorView_DV_Total_Year_Dept_Total(["VendorXFDepartmentVendorView.DV Total Year Dept Total"]) --> REPORT
    VendorXFDepartmentVendorView_DV_Total_Year___Units__Vendor_Share_(["VendorXFDepartmentVendorView.DV Total Year % Units (Vendor Share)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Total_Cost_(["Sum(VendorXFDepartmentVendorView.Total Cost)"]) --> REPORT
    VendorXFDepartmentVendorView_DV_Total_Cost_Dept_Total(["VendorXFDepartmentVendorView.DV Total Cost Dept Total"]) --> REPORT
    VendorXFDepartmentVendorView_DV_Total_Cost____Vendor_Share_(["VendorXFDepartmentVendorView.DV Total Cost % (Vendor Share)"]) --> REPORT
    Sum_VendorXFDepartmentVendorView_Total_Retail_(["Sum(VendorXFDepartmentVendorView.Total Retail)"]) --> REPORT
    VendorXFDepartmentVendorView_VendorInvoiceGroup(["VendorXFDepartmentVendorView.VendorInvoiceGroup"]) --> REPORT
    VendorXFVendorFactoryView_VendorLabel(["VendorXFVendorFactoryView.VendorLabel"]) --> REPORT
    VendorXFVendorFactoryView_Year(["VendorXFVendorFactoryView.Year"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Jan_(["Sum(VendorXFVendorFactoryView.Jan)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Feb_(["Sum(VendorXFVendorFactoryView.Feb)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Mar_(["Sum(VendorXFVendorFactoryView.Mar)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Apr_(["Sum(VendorXFVendorFactoryView.Apr)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_May_(["Sum(VendorXFVendorFactoryView.May)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Jun_(["Sum(VendorXFVendorFactoryView.Jun)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Jul_(["Sum(VendorXFVendorFactoryView.Jul)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Aug_(["Sum(VendorXFVendorFactoryView.Aug)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Sep_(["Sum(VendorXFVendorFactoryView.Sep)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Oct_(["Sum(VendorXFVendorFactoryView.Oct)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Nov_(["Sum(VendorXFVendorFactoryView.Nov)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Dec_(["Sum(VendorXFVendorFactoryView.Dec)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_QTR1_(["Sum(VendorXFVendorFactoryView.QTR1)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_QTR2_(["Sum(VendorXFVendorFactoryView.QTR2)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_QTR3_(["Sum(VendorXFVendorFactoryView.QTR3)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_QTR4_(["Sum(VendorXFVendorFactoryView.QTR4)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Total_Year_(["Sum(VendorXFVendorFactoryView.Total Year)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Total_Cost_(["Sum(VendorXFVendorFactoryView.Total Cost)"]) --> REPORT
    Sum_VendorXFVendorFactoryView_Total_Retail_(["Sum(VendorXFVendorFactoryView.Total Retail)"]) --> REPORT
    VendorXFVendorFactoryView_FactoryLabel(["VendorXFVendorFactoryView.FactoryLabel"]) --> REPORT
    VendorXFVendorFactoryView_VF_QTR1_Factory_Total(["VendorXFVendorFactoryView.VF QTR1 Factory Total"]) --> REPORT
    VendorXFVendorFactoryView_VF_QTR1___Units__Factory_Share_(["VendorXFVendorFactoryView.VF QTR1 % Units (Factory Share)"]) --> REPORT
    VendorXFVendorFactoryView_VF_QTR2_Factory_Total(["VendorXFVendorFactoryView.VF QTR2 Factory Total"]) --> REPORT
    VendorXFVendorFactoryView_VF_QTR2___Units__Factory_Share_(["VendorXFVendorFactoryView.VF QTR2 % Units (Factory Share)"]) --> REPORT
    VendorXFVendorFactoryView_VF_QTR3_Factory_Total(["VendorXFVendorFactoryView.VF QTR3 Factory Total"]) --> REPORT
    VendorXFVendorFactoryView_VF_QTR3___Units__Factory_Share_(["VendorXFVendorFactoryView.VF QTR3 % Units (Factory Share)"]) --> REPORT
    VendorXFVendorFactoryView_VF_QTR4_Factory_Total(["VendorXFVendorFactoryView.VF QTR4 Factory Total"]) --> REPORT
    VendorXFVendorFactoryView_VF_QTR4___Units__Factory_Share_(["VendorXFVendorFactoryView.VF QTR4 % Units (Factory Share)"]) --> REPORT
    VendorXFVendorFactoryView_VF_Total_Year_Factory_Total(["VendorXFVendorFactoryView.VF Total Year Factory Total"]) --> REPORT
    VendorXFVendorFactoryView_VF_Total_Year___Units__Factory_Share_(["VendorXFVendorFactoryView.VF Total Year % Units (Factory Share)"]) --> REPORT
    VendorXFVendorFactoryView_VF_Total_Cost____Factory_Share_(["VendorXFVendorFactoryView.VF Total Cost % (Factory Share)"]) --> REPORT
    VendorXFVendorFactoryView_VF_Total_Cost__Vendor_Year_Total_(["VendorXFVendorFactoryView.VF Total Cost (Vendor-Year Total)"]) --> REPORT
    VendorXFVendorFactoryView_VendorInvoiceGroupLabel(["VendorXFVendorFactoryView.VendorInvoiceGroupLabel"]) --> REPORT
    product_dim_le_department_code(["product_dim_le.department_code"]) --> REPORT
    VendorXFDepartmentVendorView_DepartmentName(["VendorXFDepartmentVendorView.DepartmentName"]) --> REPORT
```

## Field Dependencies

| Referenced Field |
|---|
| VendorXFFactoryDepartmentView.FactoryLabel |
| date_dim.actual_date |
| VendorXFFactoryDepartmentView.DepartmentLabel |
| product_dim_le.chain |
| VendorXFFactoryDepartmentView.Year |
| Sum(VendorXFFactoryDepartmentView.Jan) |
| Sum(VendorXFFactoryDepartmentView.Feb) |
| Sum(VendorXFFactoryDepartmentView.Mar) |
| Sum(VendorXFFactoryDepartmentView.Apr) |
| Sum(VendorXFFactoryDepartmentView.May) |
| Sum(VendorXFFactoryDepartmentView.Jun) |
| Sum(VendorXFFactoryDepartmentView.Jul) |
| Sum(VendorXFFactoryDepartmentView.Aug) |
| Sum(VendorXFFactoryDepartmentView.Sep) |
| Sum(VendorXFFactoryDepartmentView.Oct) |
| Sum(VendorXFFactoryDepartmentView.Nov) |
| Sum(VendorXFFactoryDepartmentView.Dec) |
| Sum(VendorXFFactoryDepartmentView.QTR1) |
| Sum(VendorXFFactoryDepartmentView.QTR2) |
| Sum(VendorXFFactoryDepartmentView.QTR3) |
| Sum(VendorXFFactoryDepartmentView.QTR4) |
| Sum(VendorXFFactoryDepartmentView.Total Year) |
| Sum(VendorXFFactoryDepartmentView.Total Cost) |
| Sum(VendorXFFactoryDepartmentView.Total Retail) |
| VendorXFFactoryDepartmentView.DepartmentName |
| VendorXFFactoryDepartmentView.FD QTR1 Dept Total |
| VendorXFFactoryDepartmentView.FD QTR1 % Units (Factory Share) |
| VendorXFFactoryDepartmentView.FD QTR2 Dept Total |
| VendorXFFactoryDepartmentView.FD QTR2 % Units (Factory Share) |
| VendorXFFactoryDepartmentView.FD QTR3 Dept Total |
| VendorXFFactoryDepartmentView.FD QTR3 % Units (Factory Share) |
| VendorXFFactoryDepartmentView.FD QTR4 Dept Total |
| VendorXFFactoryDepartmentView.FD QTR4 % Units (Factory Share) |
| select |
| VendorXFFactoryDepartmentView.FD Total Year Dept Total |
| VendorXFFactoryDepartmentView.FD Total Year % Units (Factory Share) |
| VendorXFFactoryDepartmentView.FD Total Cost Dept Total |
| VendorXFFactoryDepartmentView.FD Total Cost % (Factory Share) |
| date_dim.actual_date.Variation.Date Hierarchy.Year1 |
| date_dim.actual_date.Variation.Date Hierarchy.Quarter |
| date_dim.actual_date.Variation.Date Hierarchy.Month |
| date_dim.actual_date.Variation.Date Hierarchy.Day |
| product_dim_le.style_code |
| product_dim_le.primary_vendor_code |
| d365LocationMapping_View.LocationCode |
| VendorXFDepartmentView.DepartmentLabel |
| Sum(VendorXFDepartmentView.Jan) |
| Sum(VendorXFDepartmentView.Feb) |
| Sum(VendorXFDepartmentView.Mar) |
| Sum(VendorXFDepartmentView.Apr) |
| Sum(VendorXFDepartmentView.May) |
| Sum(VendorXFDepartmentView.Jun) |
| Sum(VendorXFDepartmentView.Jul) |
| Sum(VendorXFDepartmentView.Aug) |
| Sum(VendorXFDepartmentView.Sep) |
| Sum(VendorXFDepartmentView.Oct) |
| Sum(VendorXFDepartmentView.Nov) |
| Sum(VendorXFDepartmentView.Dec) |
| Sum(VendorXFDepartmentView.QTR1) |
| Sum(VendorXFDepartmentView.QTR2) |
| Sum(VendorXFDepartmentView.QTR3) |
| Sum(VendorXFDepartmentView.QTR4) |
| Sum(VendorXFDepartmentView.Total Year) |
| Sum(VendorXFDepartmentView.Total Cost) |
| Sum(VendorXFDepartmentView.Total Retail) |
| VendorXFDepartmentView.Year |
| VendorXFDepartmentView.DepartmentName |
| VendorXFVendorDepartmentView.Year |
| VendorXFVendorDepartmentView.VendorLabel |
| Sum(VendorXFVendorDepartmentView.Jan) |
| Sum(VendorXFVendorDepartmentView.Feb) |
| Sum(VendorXFVendorDepartmentView.Mar) |
| Sum(VendorXFVendorDepartmentView.Apr) |
| Sum(VendorXFVendorDepartmentView.May) |
| Sum(VendorXFVendorDepartmentView.Jun) |
| Sum(VendorXFVendorDepartmentView.Jul) |
| Sum(VendorXFVendorDepartmentView.Aug) |
| Sum(VendorXFVendorDepartmentView.Sep) |
| Sum(VendorXFVendorDepartmentView.Oct) |
| Sum(VendorXFVendorDepartmentView.Nov) |
| Sum(VendorXFVendorDepartmentView.Dec) |
| Sum(VendorXFVendorDepartmentView.QTR1) |
| Sum(VendorXFVendorDepartmentView.QTR2) |
| Sum(VendorXFVendorDepartmentView.QTR3) |
| Sum(VendorXFVendorDepartmentView.QTR4) |
| Sum(VendorXFVendorDepartmentView.Total Year) |
| Sum(VendorXFVendorDepartmentView.Total Cost) |
| Sum(VendorXFVendorDepartmentView.Total Retail) |
| VendorXFVendorDepartmentView.DepartmentName |
| VendorXFVendorDepartmentView.DepartmentLabel |
| VendorXFVendorDepartmentView.VD QTR1 Vendor Total |
| VendorXFVendorDepartmentView.VD QTR1 % Units (Dept Share of Vendor) |
| VendorXFVendorDepartmentView.VD QTR2 Vendor Total |
| VendorXFVendorDepartmentView.VD QTR2 % Units (Dept Share of Vendor) |
| VendorXFVendorDepartmentView.VD QTR3 Vendor Total |
| VendorXFVendorDepartmentView.VD QTR3 % Units (Dept Share of Vendor) |
| VendorXFVendorDepartmentView.VD QTR4 Vendor Total |
| VendorXFVendorDepartmentView.VD QTR4 % Units (Dept Share of Vendor) |
| VendorXFVendorDepartmentView.VD Total Year Vendor Total |
| VendorXFVendorDepartmentView.VD Total Year % Units (Dept Share of Vendor) |
| VendorXFVendorDepartmentView.VD Total Cost Vendor Total |
| VendorXFVendorDepartmentView.VD Total Cost % (Dept Share of Vendor) |
| VendorXFVendorDepartmentView.VendorInvoiceGroup |
| VendorXFItemDetailView.DepartmentName |
| VendorXFItemDetailView.Factory |
| VendorXFItemDetailView.Style |
| VendorXFItemDetailView.DepartmentNumber |
| VendorXFItemDetailView.Vendor |
| VendorXFItemDetailView.Description |
| VendorXFItemDetailView.VendorName |
| Sum(VendorXFItemDetailView.CurrentYearMinus3) |
| Sum(VendorXFItemDetailView.CurrentYearMinus2) |
| Sum(VendorXFItemDetailView.CurrentYearMinus1) |
| Sum(VendorXFItemDetailView.CurrentYear) |
| VendorXFDepartmentVendorView.VendorLabel |
| VendorXFDepartmentVendorView.DepartmentLabel |
| VendorXFDepartmentVendorView.Year |
| Sum(VendorXFDepartmentVendorView.Jan) |
| Sum(VendorXFDepartmentVendorView.Feb) |
| Sum(VendorXFDepartmentVendorView.Mar) |
| Sum(VendorXFDepartmentVendorView.Apr) |
| Sum(VendorXFDepartmentVendorView.May) |
| Sum(VendorXFDepartmentVendorView.Jun) |
| Sum(VendorXFDepartmentVendorView.Jul) |
| Sum(VendorXFDepartmentVendorView.Aug) |
| Sum(VendorXFDepartmentVendorView.Sep) |
| Sum(VendorXFDepartmentVendorView.Oct) |
| Sum(VendorXFDepartmentVendorView.Nov) |
| Sum(VendorXFDepartmentVendorView.Dec) |
| Sum(VendorXFDepartmentVendorView.QTR1) |
| VendorXFDepartmentVendorView.DV QTR1 Dept Total |
| VendorXFDepartmentVendorView.DV QTR1 % Units (Vendor Share) |
| Sum(VendorXFDepartmentVendorView.QTR2) |
| VendorXFDepartmentVendorView.DV QTR2 Dept Total |
| VendorXFDepartmentVendorView.DV QTR2 % Units (Vendor Share) |
| Sum(VendorXFDepartmentVendorView.QTR3) |
| VendorXFDepartmentVendorView.DV QTR3 Dept Total |
| VendorXFDepartmentVendorView.DV QTR3 % Units (Vendor Share) |
| Sum(VendorXFDepartmentVendorView.QTR4) |
| VendorXFDepartmentVendorView.DV QTR4 Dept Total |
| VendorXFDepartmentVendorView.DV QTR4 % Units (Vendor Share) |
| Sum(VendorXFDepartmentVendorView.Total Year) |
| VendorXFDepartmentVendorView.DV Total Year Dept Total |
| VendorXFDepartmentVendorView.DV Total Year % Units (Vendor Share) |
| Sum(VendorXFDepartmentVendorView.Total Cost) |
| VendorXFDepartmentVendorView.DV Total Cost Dept Total |
| VendorXFDepartmentVendorView.DV Total Cost % (Vendor Share) |
| Sum(VendorXFDepartmentVendorView.Total Retail) |
| VendorXFDepartmentVendorView.VendorInvoiceGroup |
| VendorXFVendorFactoryView.VendorLabel |
| VendorXFVendorFactoryView.Year |
| Sum(VendorXFVendorFactoryView.Jan) |
| Sum(VendorXFVendorFactoryView.Feb) |
| Sum(VendorXFVendorFactoryView.Mar) |
| Sum(VendorXFVendorFactoryView.Apr) |
| Sum(VendorXFVendorFactoryView.May) |
| Sum(VendorXFVendorFactoryView.Jun) |
| Sum(VendorXFVendorFactoryView.Jul) |
| Sum(VendorXFVendorFactoryView.Aug) |
| Sum(VendorXFVendorFactoryView.Sep) |
| Sum(VendorXFVendorFactoryView.Oct) |
| Sum(VendorXFVendorFactoryView.Nov) |
| Sum(VendorXFVendorFactoryView.Dec) |
| Sum(VendorXFVendorFactoryView.QTR1) |
| Sum(VendorXFVendorFactoryView.QTR2) |
| Sum(VendorXFVendorFactoryView.QTR3) |
| Sum(VendorXFVendorFactoryView.QTR4) |
| Sum(VendorXFVendorFactoryView.Total Year) |
| Sum(VendorXFVendorFactoryView.Total Cost) |
| Sum(VendorXFVendorFactoryView.Total Retail) |
| VendorXFVendorFactoryView.FactoryLabel |
| VendorXFVendorFactoryView.VF QTR1 Factory Total |
| VendorXFVendorFactoryView.VF QTR1 % Units (Factory Share) |
| VendorXFVendorFactoryView.VF QTR2 Factory Total |
| VendorXFVendorFactoryView.VF QTR2 % Units (Factory Share) |
| VendorXFVendorFactoryView.VF QTR3 Factory Total |
| VendorXFVendorFactoryView.VF QTR3 % Units (Factory Share) |
| VendorXFVendorFactoryView.VF QTR4 Factory Total |
| VendorXFVendorFactoryView.VF QTR4 % Units (Factory Share) |
| VendorXFVendorFactoryView.VF Total Year Factory Total |
| VendorXFVendorFactoryView.VF Total Year % Units (Factory Share) |
| VendorXFVendorFactoryView.VF Total Cost % (Factory Share) |
| VendorXFVendorFactoryView.VF Total Cost (Vendor-Year Total) |
| VendorXFVendorFactoryView.VendorInvoiceGroupLabel |
| product_dim_le.department_code |
| VendorXFDepartmentVendorView.DepartmentName |

## Pages

| Page | Visuals |
|---|---|
| Vendor and Factory Receipt and Buy Plan Analysis | 23 |
| Department | 19 |
| Department - FLAT | 19 |
| Vendor-Department | 20 |
| Item Detail | 22 |
| Department-Vendor - FLAT | 21 |
| Vendor-Factory | 23 |
| Vendor-Department - FLAT | 20 |
| Department-Vendor | 21 |
| Vendor-Factory - FLAT | 23 |
| Factory-Department - FLAT | 23 |

## Visuals

### Vendor and Factory Receipt and Buy Plan Analysis

| Visual | Type | Fields |
|---|---|---|
| 06f3e93279e4b4255de0 | actionButton |  |
| 0d5beb3fb664f684cfeb | slicer | VendorXFFactoryDepartmentView.FactoryLabel |
| 0e4b21cf2a88f6e73091 | bookmarkNavigator |  |
| 20fd66b1c7fb8b32654c | textbox |  |
| 27bf13bddc54b5352924 | slicer | date_dim.actual_date |
| 2bd9ae16b5d213d60c1f | slicer | VendorXFFactoryDepartmentView.DepartmentLabel |
| 31448b003bc3111fb5e1 | textbox |  |
| 37af2babf22b229a1a78 | slicer | product_dim_le.chain |
| 417d5e01a46d3c3371e3 | unknown |  |
| 4fce35f35330ae7865e6 | pivotTable | VendorXFFactoryDepartmentView.Year, VendorXFFactoryDepartmentView.FactoryLabel, Sum(VendorXFFactoryDepartmentView.Jan), Sum(VendorXFFactoryDepartmentView.Feb), Sum(VendorXFFactoryDepartmentView.Mar), Sum(VendorXFFactoryDepartmentView.Apr), Sum(VendorXFFactoryDepartmentView.May), Sum(VendorXFFactoryDepartmentView.Jun), Sum(VendorXFFactoryDepartmentView.Jul), Sum(VendorXFFactoryDepartmentView.Aug), Sum(VendorXFFactoryDepartmentView.Sep), Sum(VendorXFFactoryDepartmentView.Oct), Sum(VendorXFFactoryDepartmentView.Nov), Sum(VendorXFFactoryDepartmentView.Dec), Sum(VendorXFFactoryDepartmentView.QTR1), Sum(VendorXFFactoryDepartmentView.QTR2), Sum(VendorXFFactoryDepartmentView.QTR3), Sum(VendorXFFactoryDepartmentView.QTR4), Sum(VendorXFFactoryDepartmentView.Total Year), Sum(VendorXFFactoryDepartmentView.Total Cost), Sum(VendorXFFactoryDepartmentView.Total Retail), VendorXFFactoryDepartmentView.DepartmentName, VendorXFFactoryDepartmentView.DepartmentLabel, VendorXFFactoryDepartmentView.FD QTR1 Dept Total, VendorXFFactoryDepartmentView.FD QTR1 % Units (Factory Share), VendorXFFactoryDepartmentView.FD QTR2 Dept Total, VendorXFFactoryDepartmentView.FD QTR2 % Units (Factory Share), VendorXFFactoryDepartmentView.FD QTR3 Dept Total, VendorXFFactoryDepartmentView.FD QTR3 % Units (Factory Share), VendorXFFactoryDepartmentView.FD QTR4 Dept Total, VendorXFFactoryDepartmentView.FD QTR4 % Units (Factory Share), select, VendorXFFactoryDepartmentView.FD Total Year Dept Total, VendorXFFactoryDepartmentView.FD Total Year % Units (Factory Share), VendorXFFactoryDepartmentView.FD Total Cost Dept Total, VendorXFFactoryDepartmentView.FD Total Cost % (Factory Share) |
| 52c0a391c34f0e14f570 | textbox |  |
| 626a719e02702b41d9c8 | textbox |  |
| 6fb1d573665cf6903888 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 71608851bd447439f3f9 | image |  |
| 7342d03186ce1a40d6e6 | textSlicer | product_dim_le.style_code |
| 7d8895b786bc708fd9d9 | unknown |  |
| 8ba4f42f7ae569743720 | unknown |  |
| 9407934260b4d7994901 | slicer | VendorXFFactoryDepartmentView.Year |
| b8a7658aec4678183b97 | slicer | product_dim_le.primary_vendor_code |
| c20b701c653a171ecaca | unknown |  |
| d5b84ee329c0c2f0bdbd | textSlicer | d365LocationMapping_View.LocationCode |
| da7413889f5c1925e1ba | bookmarkNavigator |  |
| e97e92c5eeab602b5040 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1 |

### Department

| Visual | Type | Fields |
|---|---|---|
| 0b4140222c5f6ce0edbe | unknown |  |
| 0bcd43cda8b8c9272764 | textbox |  |
| 122ea31d98d5e46b728a | bookmarkNavigator |  |
| 44b856414f1a82fa1972 | unknown |  |
| 4df0d921ab0b5d077f2c | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 6742439617599cab260c | slicer | VendorXFDepartmentView.DepartmentLabel |
| 6f0031da695b744bd74a | textbox |  |
| 826e14c9840c3793285e | unknown |  |
| 908fac9c59490a900d0a | pivotTable | Sum(VendorXFDepartmentView.Jan), Sum(VendorXFDepartmentView.Feb), Sum(VendorXFDepartmentView.Mar), Sum(VendorXFDepartmentView.Apr), Sum(VendorXFDepartmentView.May), Sum(VendorXFDepartmentView.Jun), Sum(VendorXFDepartmentView.Jul), Sum(VendorXFDepartmentView.Aug), Sum(VendorXFDepartmentView.Sep), Sum(VendorXFDepartmentView.Oct), Sum(VendorXFDepartmentView.Nov), Sum(VendorXFDepartmentView.Dec), Sum(VendorXFDepartmentView.QTR1), Sum(VendorXFDepartmentView.QTR2), Sum(VendorXFDepartmentView.QTR3), Sum(VendorXFDepartmentView.QTR4), Sum(VendorXFDepartmentView.Total Year), Sum(VendorXFDepartmentView.Total Cost), Sum(VendorXFDepartmentView.Total Retail), VendorXFDepartmentView.Year, VendorXFDepartmentView.DepartmentName, VendorXFDepartmentView.DepartmentLabel, select |
| 97f4659a5a12bc988c51 | image |  |
| 9a7956cae86f44783ec2 | slicer | date_dim.actual_date |
| 9ea736d49b75db93980e | textbox |  |
| cc9c621b0f8156219228 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| cca8d761cff72ee6b8d5 | bookmarkNavigator |  |
| d986b5ee6dd8555a4031 | textSlicer | d365LocationMapping_View.LocationCode |
| ebf4a2dc4872072b777f | unknown |  |
| ec739d70b14b7c06805a | actionButton |  |
| f565ef239c335c761d82 | slicer | VendorXFDepartmentView.Year |
| f920f4a3989b72fd51af | textbox |  |

### Department - FLAT

| Visual | Type | Fields |
|---|---|---|
| 041fbe9fe878be0160ba | unknown |  |
| 1cd707827a2938460da7 | slicer | VendorXFDepartmentView.DepartmentLabel |
| 2a6f8f24e1a2ce47ab9c | slicer | VendorXFDepartmentView.Year |
| 3574d26b01465b6a5d58 | bookmarkNavigator |  |
| 57ec5bfedd916d01e18b | textbox |  |
| 77bb13441db703a5d3c4 | textSlicer | d365LocationMapping_View.LocationCode |
| 80a52967b94259a73725 | bookmarkNavigator |  |
| 8519a7bb507bad58b007 | tableEx | VendorXFDepartmentView.DepartmentLabel, VendorXFDepartmentView.Year, Sum(VendorXFDepartmentView.Jan), Sum(VendorXFDepartmentView.Feb), Sum(VendorXFDepartmentView.Mar), Sum(VendorXFDepartmentView.Apr), Sum(VendorXFDepartmentView.May), Sum(VendorXFDepartmentView.Jun), Sum(VendorXFDepartmentView.Jul), Sum(VendorXFDepartmentView.Aug), Sum(VendorXFDepartmentView.Sep), Sum(VendorXFDepartmentView.Oct), Sum(VendorXFDepartmentView.Nov), Sum(VendorXFDepartmentView.Dec), Sum(VendorXFDepartmentView.QTR1), Sum(VendorXFDepartmentView.QTR2), Sum(VendorXFDepartmentView.QTR3), Sum(VendorXFDepartmentView.QTR4), Sum(VendorXFDepartmentView.Total Year), Sum(VendorXFDepartmentView.Total Cost), Sum(VendorXFDepartmentView.Total Retail), select |
| 8deacda0a573005e567d | textbox |  |
| 909406f8e5dc01b95801 | unknown |  |
| 91a8bb1203a55dc08e49 | image |  |
| 9e6d7bfd1dc00cdd70c9 | unknown |  |
| a2116e2eae04ad04987a | actionButton |  |
| c8d94cfa9eac160308b9 | textbox |  |
| cfab0b2d174721659438 | unknown |  |
| e48d1f5f63cc192635a1 | slicer | date_dim.actual_date |
| e98a0416193b3293b504 | textbox |  |
| ea863b0915d4a00349e0 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| fdf5342f797b140e5683 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |

### Vendor-Department

| Visual | Type | Fields |
|---|---|---|
| 0b322811c1cff775d4ad | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 0c41812b7fafe18cb358 | textbox |  |
| 11a78fd2fae11ab9dd4f | textbox |  |
| 181d712ee51b40baafff | slicer | VendorXFVendorDepartmentView.Year |
| 1a30bd1d18cadc04e0ec | unknown |  |
| 531bb268efe15b7b1ff8 | textbox |  |
| 71fbe9e0837e1342192a | unknown |  |
| 8bc442b5385ea93a764b | slicer | date_dim.actual_date |
| 8da59bce6db47b43925d | slicer | VendorXFVendorDepartmentView.VendorLabel |
| 94a972885912635c1d36 | unknown |  |
| a0006b207ecc64872494 | textbox |  |
| bb6be7895f2ff7e0c0c3 | pivotTable | VendorXFVendorDepartmentView.VendorLabel, VendorXFVendorDepartmentView.Year, Sum(VendorXFVendorDepartmentView.Jan), Sum(VendorXFVendorDepartmentView.Feb), Sum(VendorXFVendorDepartmentView.Mar), Sum(VendorXFVendorDepartmentView.Apr), Sum(VendorXFVendorDepartmentView.May), Sum(VendorXFVendorDepartmentView.Jun), Sum(VendorXFVendorDepartmentView.Jul), Sum(VendorXFVendorDepartmentView.Aug), Sum(VendorXFVendorDepartmentView.Sep), Sum(VendorXFVendorDepartmentView.Oct), Sum(VendorXFVendorDepartmentView.Nov), Sum(VendorXFVendorDepartmentView.Dec), Sum(VendorXFVendorDepartmentView.QTR1), Sum(VendorXFVendorDepartmentView.QTR2), Sum(VendorXFVendorDepartmentView.QTR3), Sum(VendorXFVendorDepartmentView.QTR4), Sum(VendorXFVendorDepartmentView.Total Year), Sum(VendorXFVendorDepartmentView.Total Cost), Sum(VendorXFVendorDepartmentView.Total Retail), VendorXFVendorDepartmentView.DepartmentName, VendorXFVendorDepartmentView.DepartmentLabel, select, VendorXFVendorDepartmentView.VD QTR1 Vendor Total, VendorXFVendorDepartmentView.VD QTR1 % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD QTR2 Vendor Total, VendorXFVendorDepartmentView.VD QTR2 % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD QTR3 Vendor Total, VendorXFVendorDepartmentView.VD QTR3 % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD QTR4 Vendor Total, VendorXFVendorDepartmentView.VD QTR4 % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD Total Year Vendor Total, VendorXFVendorDepartmentView.VD Total Year % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD Total Cost Vendor Total, VendorXFVendorDepartmentView.VD Total Cost % (Dept Share of Vendor) |
| bf52c0b4ecb0d7a046ad | slicer | VendorXFVendorDepartmentView.VendorInvoiceGroup |
| cd7445e139dadba4ccc2 | bookmarkNavigator |  |
| d037ca21ef35cc4fc9e3 | bookmarkNavigator |  |
| dfdfff4b26d68c63ad73 | image |  |
| e0764f97364b1b1ad632 | textSlicer | d365LocationMapping_View.LocationCode |
| ed5e7678652ddf97f3e0 | slicer | VendorXFVendorDepartmentView.DepartmentLabel |
| f2885216e30865c8e745 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| fc49bdebcfa889a3e64b | actionButton |  |

### Item Detail

| Visual | Type | Fields |
|---|---|---|
| 2193e2edc827f31719be | textbox |  |
| 21b7447b387262d5374b | slicer | VendorXFItemDetailView.DepartmentName |
| 2ea2459e3929de419a83 | textFilter25A4896A83E0487089E2B90C9AE57C8A | product_dim_le.style_code |
| 304ec1bf661c8deae9bd | textbox |  |
| 3d8601a79b6794f6b4a5 | bookmarkNavigator |  |
| 4bb72fc04f5cc1ae96ee | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 60d659d82e41d4e25116 | textbox |  |
| 6565d867f7f438c4cc0a | image |  |
| 66ff435ed7ff273b5f8a | textbox |  |
| 6a616d95f61ea000f212 | unknown |  |
| 6db65c752deadfbcb294 | unknown |  |
| 7a993867479e4c75ec62 | slicer | date_dim.actual_date |
| 7c26d62a962337ccd320 | actionButton |  |
| 87a70addfe1711297f73 | slicer | VendorXFItemDetailView.Factory |
| a0684b424688eb691986 | textSlicer | VendorXFItemDetailView.Style |
| adad71e1e37baf39186c | bookmarkNavigator |  |
| d3e95565674c1086f680 | slicer | VendorXFItemDetailView.DepartmentNumber |
| d7467565f318ab599dfd | slicer | VendorXFItemDetailView.Vendor |
| eabb47256ede0be48f91 | tableEx | VendorXFItemDetailView.Vendor, VendorXFItemDetailView.Factory, VendorXFItemDetailView.DepartmentNumber, VendorXFItemDetailView.DepartmentName, VendorXFItemDetailView.Style, VendorXFItemDetailView.Description, VendorXFItemDetailView.VendorName, Sum(VendorXFItemDetailView.CurrentYearMinus3), Sum(VendorXFItemDetailView.CurrentYearMinus2), Sum(VendorXFItemDetailView.CurrentYearMinus1), Sum(VendorXFItemDetailView.CurrentYear) |
| f0f6569ed00b9f8784d8 | unknown |  |
| f6d1d55c0f658018953c | textSlicer | d365LocationMapping_View.LocationCode |
| fe33fa0f0a76db549409 | unknown |  |

### Department-Vendor - FLAT

| Visual | Type | Fields |
|---|---|---|
| 05e8f27fb3ac11c9e7e0 | textbox |  |
| 05f5724304055db23c45 | unknown |  |
| 46d8f1ce3a42c8a44e18 | textSlicer | d365LocationMapping_View.LocationCode |
| 507973f47c30754ec0b9 | textbox |  |
| 53d1011070336579d2db | image |  |
| 543061560a27e01e2e50 | slicer | VendorXFDepartmentVendorView.VendorLabel |
| 599769b005266c630846 | bookmarkNavigator |  |
| 59b71d16460710e49719 | slicer | date_dim.actual_date |
| 5c673774a1690dc5ba07 | textbox |  |
| 7218a4b893605c53c7a1 | textbox |  |
| 83161a6dc3c42a710b47 | tableEx | VendorXFDepartmentVendorView.DepartmentLabel, VendorXFDepartmentVendorView.VendorLabel, VendorXFDepartmentVendorView.Year, Sum(VendorXFDepartmentVendorView.Jan), Sum(VendorXFDepartmentVendorView.Feb), Sum(VendorXFDepartmentVendorView.Mar), Sum(VendorXFDepartmentVendorView.Apr), Sum(VendorXFDepartmentVendorView.May), Sum(VendorXFDepartmentVendorView.Jun), Sum(VendorXFDepartmentVendorView.Jul), Sum(VendorXFDepartmentVendorView.Aug), Sum(VendorXFDepartmentVendorView.Sep), Sum(VendorXFDepartmentVendorView.Oct), Sum(VendorXFDepartmentVendorView.Nov), Sum(VendorXFDepartmentVendorView.Dec), Sum(VendorXFDepartmentVendorView.QTR1), VendorXFDepartmentVendorView.DV QTR1 Dept Total, VendorXFDepartmentVendorView.DV QTR1 % Units (Vendor Share), Sum(VendorXFDepartmentVendorView.QTR2), VendorXFDepartmentVendorView.DV QTR2 Dept Total, VendorXFDepartmentVendorView.DV QTR2 % Units (Vendor Share), Sum(VendorXFDepartmentVendorView.QTR3), VendorXFDepartmentVendorView.DV QTR3 Dept Total, VendorXFDepartmentVendorView.DV QTR3 % Units (Vendor Share), Sum(VendorXFDepartmentVendorView.QTR4), VendorXFDepartmentVendorView.DV QTR4 Dept Total, VendorXFDepartmentVendorView.DV QTR4 % Units (Vendor Share), Sum(VendorXFDepartmentVendorView.Total Year), VendorXFDepartmentVendorView.DV Total Year Dept Total, VendorXFDepartmentVendorView.DV Total Year % Units (Vendor Share), Sum(VendorXFDepartmentVendorView.Total Cost), VendorXFDepartmentVendorView.DV Total Cost Dept Total, VendorXFDepartmentVendorView.DV Total Cost % (Vendor Share), Sum(VendorXFDepartmentVendorView.Total Retail), select |
| 8a8f7a21d6389bb5da60 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 978aa1adce1b65c39d20 | actionButton |  |
| 9a842b31dc584ca179ed | slicer | VendorXFDepartmentVendorView.Year |
| 9af59bcd7d07e38a4067 | slicer | VendorXFDepartmentVendorView.DepartmentLabel |
| aa8ecd5f0779b4330c5a | unknown |  |
| aab5a725e77e5aec0901 | unknown |  |
| b25ada696a154e4d3a2b | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| d395a5cd6700060a01d0 | unknown |  |
| f120acde66466090be43 | bookmarkNavigator |  |
| f629a529b588301c1e05 | slicer | VendorXFDepartmentVendorView.VendorInvoiceGroup |

### Vendor-Factory

| Visual | Type | Fields |
|---|---|---|
| 089374fe3a0f8b0ff8b6 | unknown |  |
| 0ad3549cc07a583496f8 | bookmarkNavigator |  |
| 137693158523e12b14c6 | slicer | date_dim.actual_date |
| 2b9baeb3f4cd320fac9a | slicer | VendorXFVendorFactoryView.VendorLabel |
| 2e5cc1ac76d5e3edf86d | pivotTable | VendorXFVendorFactoryView.Year, Sum(VendorXFVendorFactoryView.Jan), Sum(VendorXFVendorFactoryView.Feb), Sum(VendorXFVendorFactoryView.Mar), Sum(VendorXFVendorFactoryView.Apr), Sum(VendorXFVendorFactoryView.May), Sum(VendorXFVendorFactoryView.Jun), Sum(VendorXFVendorFactoryView.Jul), Sum(VendorXFVendorFactoryView.Aug), Sum(VendorXFVendorFactoryView.Sep), Sum(VendorXFVendorFactoryView.Oct), Sum(VendorXFVendorFactoryView.Nov), Sum(VendorXFVendorFactoryView.Dec), Sum(VendorXFVendorFactoryView.QTR1), Sum(VendorXFVendorFactoryView.QTR2), Sum(VendorXFVendorFactoryView.QTR3), Sum(VendorXFVendorFactoryView.QTR4), Sum(VendorXFVendorFactoryView.Total Year), Sum(VendorXFVendorFactoryView.Total Cost), Sum(VendorXFVendorFactoryView.Total Retail), VendorXFVendorFactoryView.FactoryLabel, VendorXFVendorFactoryView.VendorLabel, VendorXFVendorFactoryView.VF QTR1 Factory Total, VendorXFVendorFactoryView.VF QTR1 % Units (Factory Share), VendorXFVendorFactoryView.VF QTR2 Factory Total, VendorXFVendorFactoryView.VF QTR2 % Units (Factory Share), VendorXFVendorFactoryView.VF QTR3 Factory Total, VendorXFVendorFactoryView.VF QTR3 % Units (Factory Share), VendorXFVendorFactoryView.VF QTR4 Factory Total, VendorXFVendorFactoryView.VF QTR4 % Units (Factory Share), select, VendorXFVendorFactoryView.VF Total Year Factory Total, VendorXFVendorFactoryView.VF Total Year % Units (Factory Share), VendorXFVendorFactoryView.VF Total Cost % (Factory Share), VendorXFVendorFactoryView.VF Total Cost (Vendor-Year Total) |
| 38440bb4442de6a654a2 | unknown |  |
| 3fddad135c2e91346ec5 | textSlicer | product_dim_le.style_code |
| 46d82a8e1f5753e4614d | actionButton |  |
| 4b9ebb6ddf0d627b0c5f | slicer | VendorXFVendorFactoryView.FactoryLabel |
| 52c532cb359abd9006cd | textbox |  |
| 5bceafb6d74e9c42c0e4 | textbox |  |
| 751024a6a6888f8b9c4c | textSlicer | d365LocationMapping_View.LocationCode |
| 84c20b5d638c697e2577 | image |  |
| 860adf5867ebfd0e4507 | bookmarkNavigator |  |
| 8808160efc1cfa8a58e6 | textbox |  |
| 932f906216af6b7c9667 | unknown |  |
| a39fe4396ca695260321 | slicer | VendorXFVendorFactoryView.Year |
| bc51bc622c1d0876d073 | slicer | VendorXFVendorFactoryView.VendorInvoiceGroupLabel |
| c469e7c85e8f2437c89b | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| d9cc54b479b36b7915ce | unknown |  |
| eb3a52317e53118563d9 | slicer | product_dim_le.department_code |
| f43d0113da14de310382 | textbox |  |
| f68603ba5aabb5bc2630 | slicer | product_dim_le.chain |

### Vendor-Department - FLAT

| Visual | Type | Fields |
|---|---|---|
| 2a3d85d1b07e0da05169 | tableEx | VendorXFVendorDepartmentView.VendorLabel, VendorXFVendorDepartmentView.DepartmentLabel, VendorXFVendorDepartmentView.Year, Sum(VendorXFVendorDepartmentView.Jan), Sum(VendorXFVendorDepartmentView.Feb), Sum(VendorXFVendorDepartmentView.Mar), Sum(VendorXFVendorDepartmentView.Apr), Sum(VendorXFVendorDepartmentView.May), Sum(VendorXFVendorDepartmentView.Jun), Sum(VendorXFVendorDepartmentView.Jul), Sum(VendorXFVendorDepartmentView.Aug), Sum(VendorXFVendorDepartmentView.Sep), Sum(VendorXFVendorDepartmentView.Oct), Sum(VendorXFVendorDepartmentView.Nov), Sum(VendorXFVendorDepartmentView.Dec), Sum(VendorXFVendorDepartmentView.QTR1), Sum(VendorXFVendorDepartmentView.QTR2), Sum(VendorXFVendorDepartmentView.QTR3), Sum(VendorXFVendorDepartmentView.QTR4), Sum(VendorXFVendorDepartmentView.Total Year), Sum(VendorXFVendorDepartmentView.Total Cost), Sum(VendorXFVendorDepartmentView.Total Retail), select, VendorXFVendorDepartmentView.VD QTR1 Vendor Total, VendorXFVendorDepartmentView.VD QTR1 % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD QTR2 Vendor Total, VendorXFVendorDepartmentView.VD QTR2 % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD QTR3 Vendor Total, VendorXFVendorDepartmentView.VD QTR3 % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD QTR4 Vendor Total, VendorXFVendorDepartmentView.VD QTR4 % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD Total Year Vendor Total, VendorXFVendorDepartmentView.VD Total Year % Units (Dept Share of Vendor), VendorXFVendorDepartmentView.VD Total Cost Vendor Total, VendorXFVendorDepartmentView.VD Total Cost % (Dept Share of Vendor) |
| 5f40308b30d21b733813 | textbox |  |
| 6f5f0cfd4ad0d6954d3b | slicer | date_dim.actual_date |
| 718723aa2e06195511be | textbox |  |
| 8e21220993540569c0a0 | unknown |  |
| 994a1230d8e4b7e124c4 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 9ffbc3000740dc282398 | image |  |
| a13232a00aea0bd055b8 | unknown |  |
| b698f4335509c7e5b634 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| c25f4e74ebca15c54a50 | slicer | VendorXFVendorDepartmentView.DepartmentLabel |
| c4f958d7d08bd1604d03 | slicer | VendorXFVendorDepartmentView.Year |
| cbbd3d33004200980b07 | slicer | VendorXFVendorDepartmentView.VendorLabel |
| cea83ad88ee0ec9742ce | slicer | VendorXFVendorDepartmentView.VendorInvoiceGroup |
| d0d55edde63081d60345 | textbox |  |
| de79eae0bc209ece2579 | bookmarkNavigator |  |
| e2d3d24999c0156d5e06 | unknown |  |
| e61662570d5dcb6b8ed9 | bookmarkNavigator |  |
| eb7811b5c2dd56417140 | actionButton |  |
| f3434dfebe088ab8052a | textSlicer | d365LocationMapping_View.LocationCode |
| fcd3154f4568b1710240 | textbox |  |

### Department-Vendor

| Visual | Type | Fields |
|---|---|---|
| 0837d7750907138961b9 | textbox |  |
| 1bc4324f8e2f97534b59 | slicer | VendorXFDepartmentVendorView.DepartmentLabel |
| 351eddd042ef94f10d90 | bookmarkNavigator |  |
| 4bad39d77cc3157adf06 | unknown |  |
| 59db8713a2f0be54afd1 | unknown |  |
| 6b0a5a272f7965e4b789 | textbox |  |
| 6d8823639a35c6368a72 | actionButton |  |
| 7de5a79fd55b173207e3 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 7df03db69b05ced4ccb0 | slicer | VendorXFDepartmentVendorView.Year |
| 906e3874d36c393315d7 | bookmarkNavigator |  |
| 94fcfc838934f9830be0 | textbox |  |
| 9f78352ad208a299998d | slicer | VendorXFDepartmentVendorView.VendorLabel |
| b4405b7bd2af574553fd | unknown |  |
| b5a857360b202ab7ddff | slicer | date_dim.actual_date |
| c11bd192f6ca3f2778b0 | image |  |
| cb5bc382a68c8c5cbc39 | textSlicer | d365LocationMapping_View.LocationCode |
| dfca3db9abfdb48f606a | pivotTable | Sum(VendorXFDepartmentVendorView.Jan), Sum(VendorXFDepartmentVendorView.Feb), Sum(VendorXFDepartmentVendorView.Mar), Sum(VendorXFDepartmentVendorView.Apr), Sum(VendorXFDepartmentVendorView.May), Sum(VendorXFDepartmentVendorView.Jun), Sum(VendorXFDepartmentVendorView.Jul), Sum(VendorXFDepartmentVendorView.Aug), Sum(VendorXFDepartmentVendorView.Sep), Sum(VendorXFDepartmentVendorView.Oct), Sum(VendorXFDepartmentVendorView.Nov), Sum(VendorXFDepartmentVendorView.Dec), Sum(VendorXFDepartmentVendorView.QTR1), Sum(VendorXFDepartmentVendorView.QTR2), Sum(VendorXFDepartmentVendorView.QTR3), Sum(VendorXFDepartmentVendorView.QTR4), Sum(VendorXFDepartmentVendorView.Total Year), Sum(VendorXFDepartmentVendorView.Total Cost), Sum(VendorXFDepartmentVendorView.Total Retail), VendorXFDepartmentVendorView.DepartmentLabel, VendorXFDepartmentVendorView.VendorLabel, VendorXFDepartmentVendorView.Year, VendorXFDepartmentVendorView.DepartmentName, VendorXFDepartmentVendorView.DV QTR1 Dept Total, VendorXFDepartmentVendorView.DV QTR1 % Units (Vendor Share), VendorXFDepartmentVendorView.DV QTR2 Dept Total, VendorXFDepartmentVendorView.DV QTR2 % Units (Vendor Share), VendorXFDepartmentVendorView.DV QTR3 Dept Total, VendorXFDepartmentVendorView.DV QTR3 % Units (Vendor Share), VendorXFDepartmentVendorView.DV QTR4 Dept Total, VendorXFDepartmentVendorView.DV QTR4 % Units (Vendor Share), select, VendorXFDepartmentVendorView.DV Total Year Dept Total, VendorXFDepartmentVendorView.DV Total Year % Units (Vendor Share), VendorXFDepartmentVendorView.DV Total Cost Dept Total, VendorXFDepartmentVendorView.DV Total Cost % (Vendor Share) |
| e69c5a720338fd6b116e | unknown |  |
| ed7d26a59b150da1519a | slicer | VendorXFDepartmentVendorView.VendorInvoiceGroup |
| f0250e7e74c7df91c577 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| fbd73e301d7355069ffd | textbox |  |

### Vendor-Factory - FLAT

| Visual | Type | Fields |
|---|---|---|
| 021d27f21e2342007d13 | textbox |  |
| 099b98eed13d70a18752 | slicer | VendorXFVendorFactoryView.FactoryLabel |
| 43a1d6feb64b106e231d | slicer | VendorXFVendorFactoryView.Year |
| 507f64866ed561894e0c | tableEx | VendorXFVendorFactoryView.VendorLabel, VendorXFVendorFactoryView.FactoryLabel, VendorXFVendorFactoryView.Year, Sum(VendorXFVendorFactoryView.Jan), Sum(VendorXFVendorFactoryView.Feb), Sum(VendorXFVendorFactoryView.Mar), Sum(VendorXFVendorFactoryView.Apr), Sum(VendorXFVendorFactoryView.May), Sum(VendorXFVendorFactoryView.Jun), Sum(VendorXFVendorFactoryView.Jul), Sum(VendorXFVendorFactoryView.Aug), Sum(VendorXFVendorFactoryView.Sep), Sum(VendorXFVendorFactoryView.Oct), Sum(VendorXFVendorFactoryView.Nov), Sum(VendorXFVendorFactoryView.Dec), Sum(VendorXFVendorFactoryView.QTR1), VendorXFVendorFactoryView.VF QTR1 Factory Total, VendorXFVendorFactoryView.VF QTR1 % Units (Factory Share), Sum(VendorXFVendorFactoryView.QTR2), VendorXFVendorFactoryView.VF QTR2 Factory Total, VendorXFVendorFactoryView.VF QTR2 % Units (Factory Share), Sum(VendorXFVendorFactoryView.QTR3), VendorXFVendorFactoryView.VF QTR3 Factory Total, VendorXFVendorFactoryView.VF QTR3 % Units (Factory Share), Sum(VendorXFVendorFactoryView.QTR4), VendorXFVendorFactoryView.VF QTR4 Factory Total, VendorXFVendorFactoryView.VF QTR4 % Units (Factory Share), Sum(VendorXFVendorFactoryView.Total Year), VendorXFVendorFactoryView.VF Total Year Factory Total, VendorXFVendorFactoryView.VF Total Year % Units (Factory Share), Sum(VendorXFVendorFactoryView.Total Cost), VendorXFVendorFactoryView.VF Total Cost (Vendor-Year Total), VendorXFVendorFactoryView.VF Total Cost % (Factory Share), Sum(VendorXFVendorFactoryView.Total Retail), select |
| 530a7468500ebbe0ac21 | unknown |  |
| 64973bb7e833556802eb | textbox |  |
| 69c0934307c37c07e62e | textbox |  |
| 72f948258ded6e7254bc | bookmarkNavigator |  |
| 7916cf407c1c0ca13598 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 813ae7b88d47ee0c35e6 | slicer | product_dim_le.chain |
| a067cce7e468b4d0ee3c | slicer | VendorXFVendorFactoryView.VendorLabel |
| a7b5405891a618ce710d | textSlicer | product_dim_le.style_code |
| b0a2f8d639361914dd81 | image |  |
| b154d0bd6861d4d530e6 | actionButton |  |
| b410985d52a390c4cc84 | unknown |  |
| c2da2249a1086879a02b | textbox |  |
| c96e35ce94a901d0e7e6 | textSlicer | d365LocationMapping_View.LocationCode |
| d8310c70d6d37586bda0 | bookmarkNavigator |  |
| db0632275dab1017b3e0 | slicer | date_dim.actual_date |
| e19090b33a4540500016 | slicer | product_dim_le.department_code |
| e2badf2323dd34308500 | slicer | VendorXFVendorFactoryView.VendorInvoiceGroupLabel |
| ea62ab48b19ec09a7082 | unknown |  |
| fcf8a6b64c1049bc0435 | unknown |  |

### Factory-Department - FLAT

| Visual | Type | Fields |
|---|---|---|
| 08552e1fdea8dc0d3e34 | actionButton |  |
| 0c5ef2726918205eba81 | unknown |  |
| 2465f6d17ecabeeeb0a0 | slicer | VendorXFFactoryDepartmentView.DepartmentLabel |
| 275121dde0ce680018d5 | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1 |
| 37993d48ec110b18cdb4 | textSlicer | d365LocationMapping_View.LocationCode |
| 5560ea2a0c6ea298d0aa | bookmarkNavigator |  |
| 59bb6ebb0c2a2601515a | tableEx | VendorXFFactoryDepartmentView.FactoryLabel, VendorXFFactoryDepartmentView.DepartmentLabel, VendorXFFactoryDepartmentView.Year, Sum(VendorXFFactoryDepartmentView.Jan), Sum(VendorXFFactoryDepartmentView.Feb), Sum(VendorXFFactoryDepartmentView.Mar), Sum(VendorXFFactoryDepartmentView.Apr), Sum(VendorXFFactoryDepartmentView.May), Sum(VendorXFFactoryDepartmentView.Jun), Sum(VendorXFFactoryDepartmentView.Jul), Sum(VendorXFFactoryDepartmentView.Aug), Sum(VendorXFFactoryDepartmentView.Sep), Sum(VendorXFFactoryDepartmentView.Oct), Sum(VendorXFFactoryDepartmentView.Nov), Sum(VendorXFFactoryDepartmentView.Dec), Sum(VendorXFFactoryDepartmentView.QTR1), VendorXFFactoryDepartmentView.FD QTR1 Dept Total, VendorXFFactoryDepartmentView.FD QTR1 % Units (Factory Share), Sum(VendorXFFactoryDepartmentView.QTR2), VendorXFFactoryDepartmentView.FD QTR2 Dept Total, VendorXFFactoryDepartmentView.FD QTR2 % Units (Factory Share), Sum(VendorXFFactoryDepartmentView.QTR3), VendorXFFactoryDepartmentView.FD QTR3 Dept Total, VendorXFFactoryDepartmentView.FD QTR3 % Units (Factory Share), Sum(VendorXFFactoryDepartmentView.QTR4), VendorXFFactoryDepartmentView.FD QTR4 Dept Total, VendorXFFactoryDepartmentView.FD QTR4 % Units (Factory Share), Sum(VendorXFFactoryDepartmentView.Total Year), VendorXFFactoryDepartmentView.FD Total Year Dept Total, VendorXFFactoryDepartmentView.FD Total Year % Units (Factory Share), Sum(VendorXFFactoryDepartmentView.Total Cost), VendorXFFactoryDepartmentView.FD Total Cost Dept Total, VendorXFFactoryDepartmentView.FD Total Cost % (Factory Share), Sum(VendorXFFactoryDepartmentView.Total Retail), select |
| 5aadeb0308a1abde6eb0 | unknown |  |
| 603388fa9b4eea660e09 | slicer | product_dim_le.primary_vendor_code |
| 6dfa753fcbc1730dd510 | textbox |  |
| 805f6cb97186c9812115 | textbox |  |
| 85d17ee2873393600716 | unknown |  |
| 870a05d8da10e1182920 | textbox |  |
| 8b121fd3cc22013ad6a6 | bookmarkNavigator |  |
| 8ba5dd18e5c2895dc67a | slicer | date_dim.actual_date.Variation.Date Hierarchy.Year1, date_dim.actual_date.Variation.Date Hierarchy.Quarter, date_dim.actual_date.Variation.Date Hierarchy.Month, date_dim.actual_date.Variation.Date Hierarchy.Day |
| 8d7c3510a70593d91746 | textbox |  |
| 9cd6e26061028193ba18 | slicer | date_dim.actual_date |
| a22667b25084ae7dc813 | image |  |
| a71ec1477a8ae5e08c4a | textSlicer | product_dim_le.style_code |
| b386f06b061c2ea901d0 | unknown |  |
| c7d2113b90e49c68075c | slicer | product_dim_le.chain |
| f80da8802564abcaabca | slicer | VendorXFFactoryDepartmentView.Year |
| e0f3626b70531b0188a0 | slicer | VendorXFFactoryDepartmentView.FactoryLabel |
