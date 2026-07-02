# SSIS Package: SalesAuditToDynamicsStaging

**Project:** SalesAuditToDynamicsStaging  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        auditworks_conn(["auditworks [OLEDB]"])
        BronzeDataLake_conn(["BronzeDataLake [OLEDB]"])
        dw_conn(["dw [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        Dynamics_conn(["Dynamics [DynamicsAX]"])
        EJ_conn(["EJ [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        me_01_conn(["me_01 [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        SalesAuditToDynamicsStaging_task["SalesAuditToDynamicsStaging"]
        Master_Container_task["Master Container"]
        SalesAuditToDynamicsStaging_task --> Master_Container_task
        Merge_and_Update_Sales_Data_task["Merge and Update Sales Data"]
        Master_Container_task --> Merge_and_Update_Sales_Data_task
        SeqCont____Dynamics_Import_Validations___Daily_task["SeqCont -  Dynamics Import Validations - Daily"]
        Merge_and_Update_Sales_Data_task --> SeqCont____Dynamics_Import_Validations___Daily_task
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake_task["Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake"]
        SeqCont____Dynamics_Import_Validations___Daily_task --> Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake_task
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old_task["Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old"]
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake_task --> Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old_task
        Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task["Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag"]
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old_task --> Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task
        Execute_SQL_Task___Truncate_Staging_task["Execute SQL Task - Truncate Staging"]
        Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task --> Execute_SQL_Task___Truncate_Staging_task
        SeqCont___Execute_Initial_Transaction_Insert_Merges_task["SeqCont - Execute Initial Transaction Insert Merges"]
        Execute_SQL_Task___Truncate_Staging_task --> SeqCont___Execute_Initial_Transaction_Insert_Merges_task
        Execute_SQL_Task___spMergeDynamicsDiscountFacts_task["Execute SQL Task - spMergeDynamicsDiscountFacts"]
        SeqCont___Execute_Initial_Transaction_Insert_Merges_task --> Execute_SQL_Task___spMergeDynamicsDiscountFacts_task
        Execute_SQL_Task___spMergeDynamicsPaymentFacts_task["Execute SQL Task - spMergeDynamicsPaymentFacts"]
        Execute_SQL_Task___spMergeDynamicsDiscountFacts_task --> Execute_SQL_Task___spMergeDynamicsPaymentFacts_task
        Execute_SQL_Task___spMergeDynamicsSalesDetailFacts_task["Execute SQL Task - spMergeDynamicsSalesDetailFacts"]
        Execute_SQL_Task___spMergeDynamicsPaymentFacts_task --> Execute_SQL_Task___spMergeDynamicsSalesDetailFacts_task
        Execute_SQL_Task___spMergeDynamicsTaxFacts_task["Execute SQL Task - spMergeDynamicsTaxFacts"]
        Execute_SQL_Task___spMergeDynamicsSalesDetailFacts_task --> Execute_SQL_Task___spMergeDynamicsTaxFacts_task
        Execute_SQL_Task___spMergeDynamicsTransactionHeaderFacts_task["Execute SQL Task - spMergeDynamicsTransactionHeaderFacts"]
        Execute_SQL_Task___spMergeDynamicsTaxFacts_task --> Execute_SQL_Task___spMergeDynamicsTransactionHeaderFacts_task
        SeqCont___Execute_Transaction_Updates_Merge_task["SeqCont - Execute Transaction Updates Merge"]
        Execute_SQL_Task___spMergeDynamicsTransactionHeaderFacts_task --> SeqCont___Execute_Transaction_Updates_Merge_task
        SeqCont____Dynamics_Import_Validations___Weekly_task["SeqCont -  Dynamics Import Validations - Weekly"]
        SeqCont___Execute_Transaction_Updates_Merge_task --> SeqCont____Dynamics_Import_Validations___Weekly_task
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables_task["Data Flow Task - Load tmpDynamics ODATA Validation Tables"]
        SeqCont____Dynamics_Import_Validations___Weekly_task --> Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables_task
        Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task["Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag"]
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables_task --> Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task
        Execute_SQL_Task___Truncate_Staging_task["Execute SQL Task - Truncate Staging"]
        Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task --> Execute_SQL_Task___Truncate_Staging_task
        SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_task["SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables"]
        Execute_SQL_Task___Truncate_Staging_task --> SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_task
        Execute_SQL_Task___Delete_Transactions_From_Fact_Tables_task["Execute SQL Task - Delete Transactions From Fact Tables"]
        SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_task --> Execute_SQL_Task___Delete_Transactions_From_Fact_Tables_task
        SeqCont___Execute_Insert_Merges_task["SeqCont - Execute Insert Merges"]
        Execute_SQL_Task___Delete_Transactions_From_Fact_Tables_task --> SeqCont___Execute_Insert_Merges_task
        Execute_SQL_Task___spMergeDynamicsDiscountFacts_task["Execute SQL Task - spMergeDynamicsDiscountFacts"]
        SeqCont___Execute_Insert_Merges_task --> Execute_SQL_Task___spMergeDynamicsDiscountFacts_task
        Execute_SQL_Task___spMergeDynamicsPaymentFacts_task["Execute SQL Task - spMergeDynamicsPaymentFacts"]
        Execute_SQL_Task___spMergeDynamicsDiscountFacts_task --> Execute_SQL_Task___spMergeDynamicsPaymentFacts_task
        Execute_SQL_Task___spMergeDynamicsSalesDetailFacts_task["Execute SQL Task - spMergeDynamicsSalesDetailFacts"]
        Execute_SQL_Task___spMergeDynamicsPaymentFacts_task --> Execute_SQL_Task___spMergeDynamicsSalesDetailFacts_task
        Execute_SQL_Task___spMergeDynamicsTaxFacts_task["Execute SQL Task - spMergeDynamicsTaxFacts"]
        Execute_SQL_Task___spMergeDynamicsSalesDetailFacts_task --> Execute_SQL_Task___spMergeDynamicsTaxFacts_task
        Execute_SQL_Task___spMergeDynamicsTransactionHeaderFacts_task["Execute SQL Task - spMergeDynamicsTransactionHeaderFacts"]
        Execute_SQL_Task___spMergeDynamicsTaxFacts_task --> Execute_SQL_Task___spMergeDynamicsTransactionHeaderFacts_task
        SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_task["SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn"]
        Execute_SQL_Task___spMergeDynamicsTransactionHeaderFacts_task --> SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_task
        Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___New_task["Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - New"]
        SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_task --> Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___New_task
        Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___Old_task["Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - Old"]
        Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___New_task --> Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___Old_task
        Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_for_Negate_Only_Trans_task["Execute SQL Task - Update Step 2 - Set IsCurrent to Null for Negate Only Trans"]
        Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___Old_task --> Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_for_Negate_Only_Trans_task
        Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions___Negate_Only_task["Execute SQL Task - Update Step 3 - Insert Negating Transactions - Negate Only"]
        Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_for_Negate_Only_Trans_task --> Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions___Negate_Only_task
        SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_task["SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base"]
        Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions___Negate_Only_task --> SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_task
        Execute_SQL_Task____Update_Step_4___Insert_Updated_Transaction_Data_task["Execute SQL Task -  Update Step 4 - Insert Updated Transaction Data"]
        SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_task --> Execute_SQL_Task____Update_Step_4___Insert_Updated_Transaction_Data_task
        Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Updated_task["Execute SQL Task - Update Step 1 - Identify Records to Be Updated"]
        Execute_SQL_Task____Update_Step_4___Insert_Updated_Transaction_Data_task --> Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Updated_task
        Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_task["Execute SQL Task - Update Step 2 - Set IsCurrent to Null"]
        Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Updated_task --> Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_task
        Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions_task["Execute SQL Task - Update Step 3 - Insert Negating Transactions"]
        Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_task --> Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions_task
        SeqCont___Stage_Sales_Data_task["SeqCont - Stage Sales Data"]
        Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions_task --> SeqCont___Stage_Sales_Data_task
        SeqCont___Load_Staging_Tables_task["SeqCont - Load Staging Tables"]
        SeqCont___Stage_Sales_Data_task --> SeqCont___Load_Staging_Tables_task
        Execute_SQL_Task___Exclude_Trans_Before_Cutover_Start_Date_task["Execute SQL Task - Exclude Trans Before Cutover Start Date"]
        SeqCont___Load_Staging_Tables_task --> Execute_SQL_Task___Exclude_Trans_Before_Cutover_Start_Date_task
        Execute_SQL_Task___Truncate_Stage_task["Execute SQL Task - Truncate Stage"]
        Execute_SQL_Task___Exclude_Trans_Before_Cutover_Start_Date_task --> Execute_SQL_Task___Truncate_Stage_task
        SeqCont___Clean_Up_Payment_Table_task["SeqCont - Clean Up Payment Table"]
        Execute_SQL_Task___Truncate_Stage_task --> SeqCont___Clean_Up_Payment_Table_task
        Execute_SQL_Task___Clean_up__0_Payment_Lines_task["Execute SQL Task - Clean up $0 Payment Lines"]
        SeqCont___Clean_Up_Payment_Table_task --> Execute_SQL_Task___Clean_up__0_Payment_Lines_task
        Execute_SQL_Task___Clean_up_1_Cent_Variances_task["Execute SQL Task - Clean up 1 Cent Variances"]
        Execute_SQL_Task___Clean_up__0_Payment_Lines_task --> Execute_SQL_Task___Clean_up_1_Cent_Variances_task
        SeqCont___Load_Discounts_and_Tax_Stage_task["SeqCont - Load Discounts and Tax Stage"]
        Execute_SQL_Task___Clean_up_1_Cent_Variances_task --> SeqCont___Load_Discounts_and_Tax_Stage_task
        Data_Flow_Task___Load_Discounts___New_task["Data Flow Task - Load Discounts - New"]
        SeqCont___Load_Discounts_and_Tax_Stage_task --> Data_Flow_Task___Load_Discounts___New_task
        Data_Flow_Task___UK_and_IE_TAx_task["Data Flow Task - UK and IE TAx"]
        Data_Flow_Task___Load_Discounts___New_task --> Data_Flow_Task___UK_and_IE_TAx_task
        Data_Flow_Task___US_and_CA_Tax_task["Data Flow Task - US and CA Tax"]
        Data_Flow_Task___UK_and_IE_TAx_task --> Data_Flow_Task___US_and_CA_Tax_task
        SeqCont___Load_Header_and_Detail_Stage_task["SeqCont - Load Header and Detail Stage"]
        Data_Flow_Task___US_and_CA_Tax_task --> SeqCont___Load_Header_and_Detail_Stage_task
        Data_Flow_Task___Load_Header_task["Data Flow Task - Load Header"]
        SeqCont___Load_Header_and_Detail_Stage_task --> Data_Flow_Task___Load_Header_task
        Data_Flow_Task___Load_Sales_Detail___Sound_Chip_task["Data Flow Task - Load Sales Detail - Sound Chip"]
        Data_Flow_Task___Load_Header_task --> Data_Flow_Task___Load_Sales_Detail___Sound_Chip_task
        Data_Flow_Task___Load_Sales_Detail_Discounts_task["Data Flow Task - Load Sales Detail Discounts"]
        Data_Flow_Task___Load_Sales_Detail___Sound_Chip_task --> Data_Flow_Task___Load_Sales_Detail_Discounts_task
        DF___Header__1_store__task["DF - Header (1 store)"]
        Data_Flow_Task___Load_Sales_Detail_Discounts_task --> DF___Header__1_store__task
        DF___Load_Sales_Detail___Sound_Chip__1_store__task["DF - Load Sales Detail - Sound Chip (1 store)"]
        DF___Header__1_store__task --> DF___Load_Sales_Detail___Sound_Chip__1_store__task
        Execute_SQL_Task___Append_Blank_Sound_Chip___New_task["Execute SQL Task - Append Blank Sound Chip - New"]
        DF___Load_Sales_Detail___Sound_Chip__1_store__task --> Execute_SQL_Task___Append_Blank_Sound_Chip___New_task
        SeqCont___Load_Payment_Table_task["SeqCont - Load Payment Table"]
        Execute_SQL_Task___Append_Blank_Sound_Chip___New_task --> SeqCont___Load_Payment_Table_task
        Data_Flow_Task___Load_Payments_task["Data Flow Task - Load Payments"]
        SeqCont___Load_Payment_Table_task --> Data_Flow_Task___Load_Payments_task
        SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_task["SeqCont - Load Tax  Discount and Tender Reference Data"]
        Data_Flow_Task___Load_Payments_task --> SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_task
        SeqCont___Load_Discount_Ref_Table_task["SeqCont - Load Discount Ref Table"]
        SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_task --> SeqCont___Load_Discount_Ref_Table_task
        Data_Flow_Task_task["Data Flow Task"]
        SeqCont___Load_Discount_Ref_Table_task --> Data_Flow_Task_task
        Execute_SQL_Task_task["Execute SQL Task"]
        Data_Flow_Task_task --> Execute_SQL_Task_task
        SeqCont___Load_Tax_Data_from_AW___Replaced_by_Dans_ETL_task["SeqCont - Load Tax Data from AW - Replaced by Dans ETL"]
        Execute_SQL_Task_task --> SeqCont___Load_Tax_Data_from_AW___Replaced_by_Dans_ETL_task
        Data_Flow_Task_task["Data Flow Task"]
        SeqCont___Load_Tax_Data_from_AW___Replaced_by_Dans_ETL_task --> Data_Flow_Task_task
        Execute_SQL_Task_task["Execute SQL Task"]
        Data_Flow_Task_task --> Execute_SQL_Task_task
        SeqCont___Load_Tender_Exchange_Ref_Table_task["SeqCont - Load Tender Exchange Ref Table"]
        Execute_SQL_Task_task --> SeqCont___Load_Tender_Exchange_Ref_Table_task
        Data_Flow_Task_task["Data Flow Task"]
        SeqCont___Load_Tender_Exchange_Ref_Table_task --> Data_Flow_Task_task
        Execute_SQL_Task_task["Execute SQL Task"]
        Data_Flow_Task_task --> Execute_SQL_Task_task
        spMergeDynamicsTenderExchangeFacts_task["spMergeDynamicsTenderExchangeFacts"]
        Execute_SQL_Task_task --> spMergeDynamicsTenderExchangeFacts_task
        SeqCont___Load_Tender_Facts__Reference_Table_task["SeqCont - Load Tender Facts  Reference Table"]
        spMergeDynamicsTenderExchangeFacts_task --> SeqCont___Load_Tender_Facts__Reference_Table_task
        Data_Flow_Task_task["Data Flow Task"]
        SeqCont___Load_Tender_Facts__Reference_Table_task --> Data_Flow_Task_task
        Execute_SQL_Task_task["Execute SQL Task"]
        Data_Flow_Task_task --> Execute_SQL_Task_task
        SeqCont___Validations_and__Exception_Routing_task["SeqCont - Validations and  Exception Routing"]
        Execute_SQL_Task_task --> SeqCont___Validations_and__Exception_Routing_task
        Data_Flow_Task___Route_Exceptions_to_Review_Table___With_Item_in_Dynamics_Check_task["Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check"]
        SeqCont___Validations_and__Exception_Routing_task --> Data_Flow_Task___Route_Exceptions_to_Review_Table___With_Item_in_Dynamics_Check_task
        Execute_SQL_Task___Delete_Exception_Records_From_Staging_Tables_task["Execute SQL Task - Delete Exception Records From Staging Tables"]
        Data_Flow_Task___Route_Exceptions_to_Review_Table___With_Item_in_Dynamics_Check_task --> Execute_SQL_Task___Delete_Exception_Records_From_Staging_Tables_task
        Execute_SQL_Task___Update_IsCurrent_on_Exception_Table_and_Delete_Old_Records_task["Execute SQL Task - Update IsCurrent on Exception Table and Delete Old Records"]
        Execute_SQL_Task___Delete_Exception_Records_From_Staging_Tables_task --> Execute_SQL_Task___Update_IsCurrent_on_Exception_Table_and_Delete_Old_Records_task
        Sequence_Container_task["Sequence Container"]
        Execute_SQL_Task___Update_IsCurrent_on_Exception_Table_and_Delete_Old_Records_task --> Sequence_Container_task
        SeqCont____Dynamics_Import_Validations___Daily_task["SeqCont -  Dynamics Import Validations - Daily"]
        Sequence_Container_task --> SeqCont____Dynamics_Import_Validations___Daily_task
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake_task["Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake"]
        SeqCont____Dynamics_Import_Validations___Daily_task --> Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake_task
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old_task["Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old"]
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake_task --> Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old_task
        Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task["Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag"]
        Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old_task --> Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task
        Execute_SQL_Task___Truncate_Staging_task["Execute SQL Task - Truncate Staging"]
        Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag_task --> Execute_SQL_Task___Truncate_Staging_task
        Send_Mail_Task_task["Send Mail Task"]
        Execute_SQL_Task___Truncate_Staging_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| auditworks | OLEDB |
| BronzeDataLake | OLEDB |
| dw | OLEDB |
| DWStaging | OLEDB |
| Dynamics | DynamicsAX |
| EJ | OLEDB |
| IntegrationStaging | OLEDB |
| me_01 | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| SalesAuditToDynamicsStaging | Microsoft.Package |
| Master Container | STOCK:SEQUENCE |
| Merge and Update Sales Data | STOCK:SEQUENCE |
| SeqCont -  Dynamics Import Validations - Daily | STOCK:SEQUENCE |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | Microsoft.Pipeline |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old | Microsoft.Pipeline |
| Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Truncate Staging | Microsoft.ExecuteSQLTask |
| SeqCont - Execute Initial Transaction Insert Merges | STOCK:SEQUENCE |
| Execute SQL Task - spMergeDynamicsDiscountFacts | Microsoft.ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsPaymentFacts | Microsoft.ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsSalesDetailFacts | Microsoft.ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsTaxFacts | Microsoft.ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsTransactionHeaderFacts | Microsoft.ExecuteSQLTask |
| SeqCont - Execute Transaction Updates Merge | STOCK:SEQUENCE |
| SeqCont -  Dynamics Import Validations - Weekly | STOCK:SEQUENCE |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables | Microsoft.Pipeline |
| Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Truncate Staging | Microsoft.ExecuteSQLTask |
| SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables | STOCK:SEQUENCE |
| Execute SQL Task - Delete Transactions From Fact Tables | Microsoft.ExecuteSQLTask |
| SeqCont - Execute Insert Merges | STOCK:SEQUENCE |
| Execute SQL Task - spMergeDynamicsDiscountFacts | Microsoft.ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsPaymentFacts | Microsoft.ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsSalesDetailFacts | Microsoft.ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsTaxFacts | Microsoft.ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsTransactionHeaderFacts | Microsoft.ExecuteSQLTask |
| SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn | STOCK:SEQUENCE |
| Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - New | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - Old | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Update Step 2 - Set IsCurrent to Null for Negate Only Trans | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Update Step 3 - Insert Negating Transactions - Negate Only | Microsoft.ExecuteSQLTask |
| SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base | STOCK:SEQUENCE |
| Execute SQL Task -  Update Step 4 - Insert Updated Transaction Data | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Update Step 1 - Identify Records to Be Updated | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Update Step 2 - Set IsCurrent to Null | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Update Step 3 - Insert Negating Transactions | Microsoft.ExecuteSQLTask |
| SeqCont - Stage Sales Data | STOCK:SEQUENCE |
| SeqCont - Load Staging Tables | STOCK:SEQUENCE |
| Execute SQL Task - Exclude Trans Before Cutover Start Date | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Truncate Stage | Microsoft.ExecuteSQLTask |
| SeqCont - Clean Up Payment Table | STOCK:SEQUENCE |
| Execute SQL Task - Clean up $0 Payment Lines | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Clean up 1 Cent Variances | Microsoft.ExecuteSQLTask |
| SeqCont - Load Discounts and Tax Stage | STOCK:SEQUENCE |
| Data Flow Task - Load Discounts - New | Microsoft.Pipeline |
| Data Flow Task - UK and IE TAx | Microsoft.Pipeline |
| Data Flow Task - US and CA Tax | Microsoft.Pipeline |
| SeqCont - Load Header and Detail Stage | STOCK:SEQUENCE |
| Data Flow Task - Load Header | Microsoft.Pipeline |
| Data Flow Task - Load Sales Detail - Sound Chip | Microsoft.Pipeline |
| Data Flow Task - Load Sales Detail Discounts | Microsoft.Pipeline |
| DF - Header (1 store) | Microsoft.Pipeline |
| DF - Load Sales Detail - Sound Chip (1 store) | Microsoft.Pipeline |
| Execute SQL Task - Append Blank Sound Chip - New | Microsoft.ExecuteSQLTask |
| SeqCont - Load Payment Table | STOCK:SEQUENCE |
| Data Flow Task - Load Payments | Microsoft.Pipeline |
| SeqCont - Load Tax  Discount and Tender Reference Data | STOCK:SEQUENCE |
| SeqCont - Load Discount Ref Table | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| SeqCont - Load Tax Data from AW - Replaced by Dans ETL | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| SeqCont - Load Tender Exchange Ref Table | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| spMergeDynamicsTenderExchangeFacts | Microsoft.ExecuteSQLTask |
| SeqCont - Load Tender Facts  Reference Table | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| SeqCont - Validations and  Exception Routing | STOCK:SEQUENCE |
| Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | Microsoft.Pipeline |
| Execute SQL Task - Delete Exception Records From Staging Tables | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Update IsCurrent on Exception Table and Delete Old Records | Microsoft.ExecuteSQLTask |
| Sequence Container | STOCK:SEQUENCE |
| SeqCont -  Dynamics Import Validations - Daily | STOCK:SEQUENCE |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | Microsoft.Pipeline |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old | Microsoft.Pipeline |
| Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag | Microsoft.ExecuteSQLTask |
| Execute SQL Task - Truncate Staging | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | select  rt.transactionid as RetailTransactionId,  rt.DataAreaId, rt.receiptId as RetailReceiptId, cast (rt.businessDate as date) as TransDate from [dbo].[RetailTransactionTable] rt where 1=1 --and cast(rt.businessDate as date) > = '2024-01-15' and cast(rt.businessDate as date) > = ? group by  rt.transactionid,  rt.DataAreaId, rt.receiptId,  cast (rt.businessDate as date) |
|  | with Summary1 as ( select case when dsd.LineAction in (2,12,15,26) 	then df.SumDiscAmount*-1 	else df.SumDiscAmount end as Amount  	, case when dsd.LineAction in (2,12,15,26) 	then df.SumDiscAmount*-1 	else df.SumDiscAmount end as DiscountCost 	--, 'None' as DiscountOriginType -- Per Scoping Document "Will Always Be Set to None"  	, case when df.DiscountType = 'Header' then 'Manual' 			when df.Dis |
|  | select  	cast(WarehouseId as varchar (4)) as WarehouseId,  	PrimaryAddressCountryRegionId as CountryCode, 	cast (Entity as varchar (4)) as Entity  from erp.WarehouseMaster where entity = '2110'  and WarehouseType <> 'Transit' group by  	cast(WarehouseId as varchar (4)), 	PrimaryAddressCountryRegionId, 	cast (Entity as varchar (4)) |
|  | with TransactionGrouped as ( select  cast (dsd.VatTaxAmount as decimal (14,2)) as Amount ,row_number() over(partition by RetailTransactionId order by dsd.LineNum) as LineNum ,dsd.LineNum as SaleLineNum , null as TaxCode -- Unknown ,dsd.RetailTerminalId ,dsd.RetailTransactionId ,dsd.BABIntRetailOperatingUnitNumber ,dsd.BABIntRetailProcessed ,dsd.Entity ,dsd.RetailReceiptId ,dsd.InventLocationId  -- |
|  | with TransactionGrouped as ( select  row_number() over(partition by RetailTransactionId order by dsd.LineNum) as LineNum ,dsd.LineNum as SaleLineNum ,dsd.TransactionLineSeq  , null as TaxCode -- Unknown ,dsd.RetailTerminalId ,dsd.RetailTransactionId ,dsd.BABIntRetailOperatingUnitNumber ,dsd.BABIntRetailProcessed ,dsd.Entity ,dsd.RetailReceiptId ,dsd.Price ,dsd.LineAction  --from DynamicsSalesDetai |
|  | with StoreLookup as ( select WarehouseID as InventLocationId,  LocationCode,  	Entity,  	case when Entity = '1100' then 'US' 	when Entity = '1700' then 'CA' 	when Entity = '2110' then 'UK' 	else null  	end as Country from [ERP].[vwWarehouseIDToLocationCode] group by  WarehouseID,  LocationCode,  Entity    )  select  	sl.LocationCode, 	sl.Country,  	rs.WarehouseId as InventLocationID, 	 	rs.Operati |
|  | select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete 	,null as CustAccount 	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number  	, case when sd.country = 'IE' then 'UK' 		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, |
|  | select 			cast (s.style_code as  varchar (30)) as ItemId,  			cast (case when left(s.style_code,1) = '0'   					then '027500'	 				when left(s.style_code,1) =  '1' 					then '127500' 				when left(s.style_code,1) =  '4' 					then '427500' 				else null end  as varchar (30)) as BlankSoundChipItemId,  			cast (case when left(s.style_code,1) = '0'   					then '1100'	 				when left(s.style_code,1) =   |
|  | -- old Query  -- Replaced 5/12/2022  --with --GiftCardRanges as --( --select --s.Style_Code, --concat(left(GiftCardRangeStart,1),right(GiftCardRangeStart,11)) as GiftCardRangeStart, --concat(left(GiftCardRangeEnd,1),right(GiftCardRangeEnd,11)) as GiftCardRangeEnd --from kodiaktest.GiftCardMstrData.dbo.GiftCardRange gc --join kodiaktest.GiftCardMstrData.dbo.StyleGiftCardRangeXref x on gc.GiftCardRa |
|  | with StoreLookup as ( select WarehouseID as InventLocationId,  LocationCode,  	Entity,  	case when Entity = '1100' then 'US' 	when Entity = '1700' then 'CA' 	when Entity = '2110' then 'UK' 	else null  	end as Country from [ERP].[vwWarehouseIDToLocationCode] group by  WarehouseID,  LocationCode,  Entity    )  select  	sl.LocationCode, 	sl.Country,  	rs.WarehouseId as InventLocationID, 	 	rs.Operati |
|  | with DynamicsFeeMapping as ( select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union  select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union  select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union  select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union  select '000025' |
|  | with Summary1 as ( select CustAccount,  InventLocationId,  TransactionLineSeq,  LineNum,  --OriginalPrice, -- Replaced 1/19/2023 with logic below - This is when stores use price MARKDOWN to increase the price of the item  --case when Price > OriginalPrice then Price else OriginalPrice end  as OriginalPrice,  -- Replaced  with below 3/29/2023 case when sd.LineAction in (2,12) then OriginalPrice whe |
|  | with StoreLookup as ( select WarehouseID as InventLocationId,  LocationCode,  	Entity,  	case when Entity = '1100' then 'US' 	when Entity = '1700' then 'CA' 	when Entity = '2110' then 'UK' 	else null  	end as Country from [ERP].[vwWarehouseIDToLocationCode] group by  WarehouseID,  LocationCode,  Entity    )  select  	sl.LocationCode, 	sl.Country,  	rs.WarehouseId as InventLocationID, 	 	rs.Operati |
|  | select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete 	,null as CustAccount 	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number  	, case when sd.country = 'IE' then 'UK' 		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, |
|  | select 			cast (s.style_code as  varchar (30)) as ItemId,  			cast (case when left(s.style_code,1) = '0'   					then '027500'	 				when left(s.style_code,1) =  '1' 					then '127500' 				when left(s.style_code,1) =  '4' 					then '427500' 				else null end  as varchar (30)) as BlankSoundChipItemId,  			cast (case when left(s.style_code,1) = '0'   					then '1100'	 				when left(s.style_code,1) =   |
|  | -- old Query  -- Replaced 5/12/2022  --with --GiftCardRanges as --( --select --s.Style_Code, --concat(left(GiftCardRangeStart,1),right(GiftCardRangeStart,11)) as GiftCardRangeStart, --concat(left(GiftCardRangeEnd,1),right(GiftCardRangeEnd,11)) as GiftCardRangeEnd --from kodiaktest.GiftCardMstrData.dbo.GiftCardRange gc --join kodiaktest.GiftCardMstrData.dbo.StyleGiftCardRangeXref x on gc.GiftCardRa |
|  | with StoreLookup as ( select WarehouseID as InventLocationId,  LocationCode,  	Entity,  	case when Entity = '1100' then 'US' 	when Entity = '1700' then 'CA' 	when Entity = '2110' then 'UK' 	else null  	end as Country from [ERP].[vwWarehouseIDToLocationCode] group by  WarehouseID,  LocationCode,  Entity    )  select  	sl.LocationCode, 	sl.Country,  	rs.WarehouseId as InventLocationID, 	 	rs.Operati |
|  | with DynamicsFeeMapping as ( select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union  select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union  select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union  select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union  select '000025' |
|  | with  DynamicsDiscountFactsStageCTE as ( 	select RetailReceiptId, SaleLineNum, sum(Amount) as Amount 	from DynamicsDiscountFactsStage 	--where RetailReceiptId = '463385215' 	group by RetailReceiptId, SaleLineNum ) ,  TenderExchangePayments as ( select transaction_id, line_object, line_object_description, line_action, line_action_display_descr, tender_key, sum(gross_line_amount) as Amount from dw.d |
|  | with LO as (  select lo.line_object,  lo.line_object_description,  lo.line_object_type,  lot.object_type_display_descr from line_object  lo (nolock) join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type  ),   Summary1 as (   select  avh.transaction_date,  avl.transaction_id,  avl.line_id,  avl.line_sequence,  avd.applied_by_line_id, avd.pos_discount_amount, L2.* from trans |
|  | --With TaxLevel as (  --select  --th.transaction_id, --td.tax_level --from [dbo].[transaction_line] tl (nolock)  --join [dbo].[tax_detail] td  (nolock) on tl.transaction_id=td.transaction_id --	and td.line_id=tl.line_id --join [dbo].[transaction_header] th (nolock) on th.transaction_id=tl.transaction_id --where line_action <> '90' -- 90 = order delivered, not interested in fulfilment  --and datedi |
|  | select  th.transaction_id, th.cashier_no,  th.store_no,  th.register_no,  th.transaction_no,  th.transaction_date,  cast (th.transaction_date as date) as transaction_date_cast,  tl.line_sequence,  tl.line_id,  lo.line_object_description,  la.line_action_display_descr,  tl.line_object,  tl.line_action,  tl.gross_line_amount,  tl.pos_discount_amount,  tl.reference_no,  isnull(OC.DFLT_CRNCY_CODE,'USD |
|  | with TransTenderTotal as ( select tfd.transaction_id,  case when tender_key = '16' 	then sum(tender_amt*-1)  	else sum(tender_amt) 	end as tender_amt  from TenderFactsDynamics  tfd (nolock)  where tender_key <> -1 --and tfd.transaction_id = '447023677' group by tfd.transaction_id, tender_key  ),   TransTenderTotalSummary as  (   select Transaction_id,  sum(tender_amt) as TotalTenderAmount from Tra |
|  | select cast (i.ItemNumber as varchar (50)) ItemNumber, cast (i.Entity as varchar (4)) as Entity  from wms.ItemMaster i (nolock)  group by  cast (i.ItemNumber as varchar (50)),  cast (i.Entity as varchar (4)) UNION  select cast (i.ItemNumber as varchar (50)) ItemNumber, cast (i.Entity as varchar (4)) as Entity  from wms.ItemMasterXtra i WHERE LEFT(ItemNumber,2) = 'SV' group by  cast (i.ItemNumber a |
|  | with  DynamicsDiscountFactsStageCTE as ( 	select RetailReceiptId, SaleLineNum, sum(Amount) as Amount 	from DynamicsDiscountFactsStage 	--where RetailReceiptId = '463385215' 	group by RetailReceiptId, SaleLineNum ) ,   Sales as (  	select s.RetailTransactionId, 		s.entity,  		s.RetailReceiptId,  		s.TransDate,  	sum (s.OriginalPrice*abs(s.qty))-sum(s.DiscAmount) as SalesTotal  	from DynamicsSalesDe |
|  | with ReturnTransactions as (  select d.RetailTransactionId, d.RetailReceiptId, d.LineNum as SaleLineNum --from DynamicsSalesDetailFactsStage d -- Replaced on 12/12/2022 from DynamicsSalesDetailDiscountsFactsStage d (nolock)  where d.LineAction in (2,12,15,26) and DiscAmount <> 0.00 group by d.RetailTransactionId, d.RetailReceiptId, d.LineNum  )  select distinct d.RetailTransactionId, d.RetailRecei |
|  | with DiscountsInSalesLines as (  select  RetailReceiptId, sum(DiscAmount) as SalesLIneSumDiscAmount  from DynamicsSalesDetailDiscountsFactsStage group by retailreceiptid   ) ,   Summary1 as (   select RetailTransactionId, h.RetailReceiptId, DiscAmount, TotalDiscAmount, dsl.SalesLIneSumDiscAmount, (h.DiscAmount - dsl.SalesLIneSumDiscAmount) as VarianceValue from DynamicsTransactionHeaderFactsStage  |
|  | select RetailTransactionId, RetailReceiptId, ItemId, dsd.LineObject, lod.Line_Object_Description, 'Item Id or ItemId Mapping Missing' as Reason  --from DynamicsSalesDetailFactsStage dsd -- Replaced on 12/12/2022 from DynamicsSalesDetailDiscountsFactsStage dsd  join dw.dbo.line_object_dim lod on lod.Line_Object=dsd.LineObject where (ItemId is null  or  right(ItemId,10) = 'NoRefAvail' ) group by Ret |
|  | select RetailTransactionId, 		RetailReceiptId,  		ItemId,  		Entity  --from DynamicsSalesDetailFactsStage dsd -- Replaced on 12/12/2022 from DynamicsSalesDetailDiscountsFactsStage dsd (nolock)    group by RetailTransactionId, RetailReceiptId,  ItemId,  Entity  order by 1, 2 |
|  | select  	RetailTransactionId,  	RetailReceiptId, 	ItemId,  	dsd.price, 	dsd.LineObject,  	lod.Line_Object_Description,  	'Item Sold Price Is Negative' as Reason  --from DynamicsSalesDetailFactsStage dsd -- Replaced on 12/12/2022 from DynamicsSalesDetailDiscountsFactsStage dsd join dw.dbo.line_object_dim lod on lod.Line_Object=dsd.LineObject where dsd.LineAction not in (2,12,15,26) -- These are the |
|  | select  rt.transactionid as RetailTransactionId,  rt.DataAreaId, rt.receiptId as RetailReceiptId, cast (rt.businessDate as date) as TransDate from [dbo].[RetailTransactionTable] rt where 1=1 --and cast(rt.businessDate as date) > = '2024-01-15' and cast(rt.businessDate as date) > = ? group by  rt.transactionid,  rt.DataAreaId, rt.receiptId,  cast (rt.businessDate as date) |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[tmpDynamicsIntRetailTransaction] |
|  | [dbo].[tmpDynamicsRetailTransaction] |
|  | [dbo].[tmpDynamicsIntRetailTransaction] |
|  | [dbo].[tmpDynamicsRetailTransaction] |
|  | [dbo].[tmpDynamicsIntRetailTransaction] |
|  | [dbo].[tmpDynamicsRetailTransaction] |
|  | [dbo].[DynamicsDiscountFactsStage] |
|  | [dbo].[DynamicsTaxFactsStage] |
|  | [dbo].[DynamicsTaxFactsStage] |
|  | [dbo].[DynamicsTransactionHeaderFactsStage] |
|  | [dbo].[DynamicsSalesDetailFactsStage] |
|  | [dbo].[DynamicsSalesDetailDiscountsFactsStage] |
|  | [dbo].[DynamicsTransactionHeaderFactsStage] |
|  | [dbo].[DynamicsSalesDetailFactsStage] |
|  | [dbo].[DynamicsPaymentFactsStage] |
|  | [dbo].[DiscountFactsReferenceDynamicsStage] |
|  | [dbo].[TransactionTaxFactsDynamicsStage] |
|  | [dbo].[DynamicsTenderExchangeFactsStage] |
|  | [dbo].[TenderPercentageFactsDynamicsStage] |
|  | [dbo].[DynamicsSalesTransactionExceptions] |
|  | [dbo].[tmpDynamicsIntRetailTransaction] |
|  | [dbo].[tmpDynamicsRetailTransaction] |
|  | [dbo].[tmpDynamicsIntRetailTransaction] |
|  | [dbo].[tmpDynamicsRetailTransaction] |

