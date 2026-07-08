# SSIS Package: SalesAuditToDynamicsStaging

**Project:** SalesAuditToDynamicsStaging  
**Folder:** WMS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| BronzeDataLake | OLEDB | azsynapsewkstt3osb-ondemand.sql.azuresynapse.net | sqlmdwprodeus | Data Source=azsynapsewkstt3osb-ondemand.sql.azuresynapse.net; Initial Catalog=sqlmdwprodeus; Provider=SQLNCLI11.1; Auto Translate=False |
| DWStaging | OLEDB | papamart | DWStaging | Data Source=papamart; Initial Catalog=DWStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| Dynamics | DynamicsAX |  |  |  |
| EJ | OLEDB | bedrockdb02 | EJ | Data Source=bedrockdb02; Initial Catalog=EJ; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| IntegrationStaging | OLEDB | stl-ssis-p-01 | IntegrationStaging | Data Source=stl-ssis-p-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| SMTP | SMTP |  |  |  |
| auditworks | OLEDB | bedrockdb01 | auditworks | Data Source=bedrockdb01; Initial Catalog=auditworks; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| dw | OLEDB | papamart | dw | Data Source=papamart; Initial Catalog=dw; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| me_01 | OLEDB | BEDROCKDB02 | me_01 | Data Source=BEDROCKDB02; Initial Catalog=me_01; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |

## Control Flow Tasks

| Task | Type |
|---|---|
| SalesAuditToDynamicsStaging | Package |
| Master Container | SEQUENCE |
| Merge and Update Sales Data | SEQUENCE |
| SeqCont -  Dynamics Import Validations - Daily | SEQUENCE |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | Pipeline |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old | Pipeline |
| Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag | ExecuteSQLTask |
| Execute SQL Task - Truncate Staging | ExecuteSQLTask |
| SeqCont - Execute Initial Transaction Insert Merges | SEQUENCE |
| Execute SQL Task - spMergeDynamicsDiscountFacts | ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsPaymentFacts | ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsSalesDetailFacts | ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsTaxFacts | ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsTransactionHeaderFacts | ExecuteSQLTask |
| SeqCont - Execute Transaction Updates Merge | SEQUENCE |
| SeqCont -  Dynamics Import Validations - Weekly | SEQUENCE |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables | Pipeline |
| Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag | ExecuteSQLTask |
| Execute SQL Task - Truncate Staging | ExecuteSQLTask |
| SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables | SEQUENCE |
| Execute SQL Task - Delete Transactions From Fact Tables | ExecuteSQLTask |
| SeqCont - Execute Insert Merges | SEQUENCE |
| Execute SQL Task - spMergeDynamicsDiscountFacts | ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsPaymentFacts | ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsSalesDetailFacts | ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsTaxFacts | ExecuteSQLTask |
| Execute SQL Task - spMergeDynamicsTransactionHeaderFacts | ExecuteSQLTask |
| SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn | SEQUENCE |
| Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - New | ExecuteSQLTask |
| Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - Old | ExecuteSQLTask |
| Execute SQL Task - Update Step 2 - Set IsCurrent to Null for Negate Only Trans | ExecuteSQLTask |
| Execute SQL Task - Update Step 3 - Insert Negating Transactions - Negate Only | ExecuteSQLTask |
| SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base | SEQUENCE |
| Execute SQL Task -  Update Step 4 - Insert Updated Transaction Data | ExecuteSQLTask |
| Execute SQL Task - Update Step 1 - Identify Records to Be Updated | ExecuteSQLTask |
| Execute SQL Task - Update Step 2 - Set IsCurrent to Null | ExecuteSQLTask |
| Execute SQL Task - Update Step 3 - Insert Negating Transactions | ExecuteSQLTask |
| SeqCont - Stage Sales Data | SEQUENCE |
| SeqCont - Load Staging Tables | SEQUENCE |
| Execute SQL Task - Exclude Trans Before Cutover Start Date | ExecuteSQLTask |
| Execute SQL Task - Truncate Stage | ExecuteSQLTask |
| SeqCont - Clean Up Payment Table | SEQUENCE |
| Execute SQL Task - Clean up $0 Payment Lines | ExecuteSQLTask |
| Execute SQL Task - Clean up 1 Cent Variances | ExecuteSQLTask |
| SeqCont - Load Discounts and Tax Stage | SEQUENCE |
| Data Flow Task - Load Discounts - New | Pipeline |
| Data Flow Task - UK and IE TAx | Pipeline |
| Data Flow Task - US and CA Tax | Pipeline |
| SeqCont - Load Header and Detail Stage | SEQUENCE |
| Data Flow Task - Load Header | Pipeline |
| Data Flow Task - Load Sales Detail - Sound Chip | Pipeline |
| Data Flow Task - Load Sales Detail Discounts | Pipeline |
| DF - Header (1 store) | Pipeline |
| DF - Load Sales Detail - Sound Chip (1 store) | Pipeline |
| Execute SQL Task - Append Blank Sound Chip - New | ExecuteSQLTask |
| SeqCont - Load Payment Table | SEQUENCE |
| Data Flow Task - Load Payments | Pipeline |
| SeqCont - Load Tax  Discount and Tender Reference Data | SEQUENCE |
| SeqCont - Load Discount Ref Table | SEQUENCE |
| Data Flow Task | Pipeline |
| Execute SQL Task | ExecuteSQLTask |
| SeqCont - Load Tax Data from AW - Replaced by Dans ETL | SEQUENCE |
| Data Flow Task | Pipeline |
| Execute SQL Task | ExecuteSQLTask |
| SeqCont - Load Tender Exchange Ref Table | SEQUENCE |
| Data Flow Task | Pipeline |
| Execute SQL Task | ExecuteSQLTask |
| spMergeDynamicsTenderExchangeFacts | ExecuteSQLTask |
| SeqCont - Load Tender Facts  Reference Table | SEQUENCE |
| Data Flow Task | Pipeline |
| Execute SQL Task | ExecuteSQLTask |
| SeqCont - Validations and  Exception Routing | SEQUENCE |
| Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | Pipeline |
| Execute SQL Task - Delete Exception Records From Staging Tables | ExecuteSQLTask |
| Execute SQL Task - Update IsCurrent on Exception Table and Delete Old Records | ExecuteSQLTask |
| Sequence Container | SEQUENCE |
| SeqCont -  Dynamics Import Validations - Daily | SEQUENCE |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | Pipeline |
| Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old | Pipeline |
| Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag | ExecuteSQLTask |
| Execute SQL Task - Truncate Staging | ExecuteSQLTask |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- Master Container [SEQUENCE]
  - Merge and Update Sales Data [SEQUENCE]
    - SeqCont -  Dynamics Import Validations - Daily [SEQUENCE]
      - Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake [Pipeline]
      - Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old [Pipeline]
      - Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag [ExecuteSQLTask]
      - Execute SQL Task - Truncate Staging [ExecuteSQLTask]
    - SeqCont - Execute Initial Transaction Insert Merges [SEQUENCE]
      - Execute SQL Task - spMergeDynamicsDiscountFacts [ExecuteSQLTask]
      - Execute SQL Task - spMergeDynamicsPaymentFacts [ExecuteSQLTask]
      - Execute SQL Task - spMergeDynamicsSalesDetailFacts [ExecuteSQLTask]
      - Execute SQL Task - spMergeDynamicsTaxFacts [ExecuteSQLTask]
      - Execute SQL Task - spMergeDynamicsTransactionHeaderFacts [ExecuteSQLTask]
    - SeqCont - Execute Transaction Updates Merge [SEQUENCE]
      - SeqCont -  Dynamics Import Validations - Weekly [SEQUENCE]
        - Data Flow Task - Load tmpDynamics ODATA Validation Tables [Pipeline]
        - Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag [ExecuteSQLTask]
        - Execute SQL Task - Truncate Staging [ExecuteSQLTask]
      - SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables [SEQUENCE]
        - Execute SQL Task - Delete Transactions From Fact Tables [ExecuteSQLTask]
        - SeqCont - Execute Insert Merges [SEQUENCE]
          - Execute SQL Task - spMergeDynamicsDiscountFacts [ExecuteSQLTask]
          - Execute SQL Task - spMergeDynamicsPaymentFacts [ExecuteSQLTask]
          - Execute SQL Task - spMergeDynamicsSalesDetailFacts [ExecuteSQLTask]
          - Execute SQL Task - spMergeDynamicsTaxFacts [ExecuteSQLTask]
          - Execute SQL Task - spMergeDynamicsTransactionHeaderFacts [ExecuteSQLTask]
      - SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn [SEQUENCE]
        - Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - New [ExecuteSQLTask]
        - Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - Old [ExecuteSQLTask]
        - Execute SQL Task - Update Step 2 - Set IsCurrent to Null for Negate Only Trans [ExecuteSQLTask]
        - Execute SQL Task - Update Step 3 - Insert Negating Transactions - Negate Only [ExecuteSQLTask]
      - SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base [SEQUENCE]
        - Execute SQL Task -  Update Step 4 - Insert Updated Transaction Data [ExecuteSQLTask]
        - Execute SQL Task - Update Step 1 - Identify Records to Be Updated [ExecuteSQLTask]
        - Execute SQL Task - Update Step 2 - Set IsCurrent to Null [ExecuteSQLTask]
        - Execute SQL Task - Update Step 3 - Insert Negating Transactions [ExecuteSQLTask]
  - SeqCont - Stage Sales Data [SEQUENCE]
    - SeqCont - Load Staging Tables [SEQUENCE]
      - Execute SQL Task - Exclude Trans Before Cutover Start Date [ExecuteSQLTask]
      - Execute SQL Task - Truncate Stage [ExecuteSQLTask]
      - SeqCont - Clean Up Payment Table [SEQUENCE]
        - Execute SQL Task - Clean up $0 Payment Lines [ExecuteSQLTask]
        - Execute SQL Task - Clean up 1 Cent Variances [ExecuteSQLTask]
      - SeqCont - Load Discounts and Tax Stage [SEQUENCE]
        - Data Flow Task - Load Discounts - New [Pipeline]
        - Data Flow Task - UK and IE TAx [Pipeline]
        - Data Flow Task - US and CA Tax [Pipeline]
      - SeqCont - Load Header and Detail Stage [SEQUENCE]
        - DF - Header (1 store) [Pipeline]
        - DF - Load Sales Detail - Sound Chip (1 store) [Pipeline]
        - Data Flow Task - Load Header [Pipeline]
        - Data Flow Task - Load Sales Detail - Sound Chip [Pipeline]
        - Data Flow Task - Load Sales Detail Discounts [Pipeline]
        - Execute SQL Task - Append Blank Sound Chip - New [ExecuteSQLTask]
      - SeqCont - Load Payment Table [SEQUENCE]
        - Data Flow Task - Load Payments [Pipeline]
    - SeqCont - Load Tax  Discount and Tender Reference Data [SEQUENCE]
      - SeqCont - Load Discount Ref Table [SEQUENCE]
        - Data Flow Task [Pipeline]
        - Execute SQL Task [ExecuteSQLTask]
      - SeqCont - Load Tax Data from AW - Replaced by Dans ETL [SEQUENCE]
        - Data Flow Task [Pipeline]
        - Execute SQL Task [ExecuteSQLTask]
      - SeqCont - Load Tender Exchange Ref Table [SEQUENCE]
        - Data Flow Task [Pipeline]
        - Execute SQL Task [ExecuteSQLTask]
        - spMergeDynamicsTenderExchangeFacts [ExecuteSQLTask]
      - SeqCont - Load Tender Facts  Reference Table [SEQUENCE]
        - Data Flow Task [Pipeline]
        - Execute SQL Task [ExecuteSQLTask]
    - SeqCont - Validations and  Exception Routing [SEQUENCE]
      - Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check [Pipeline]
      - Execute SQL Task - Delete Exception Records From Staging Tables [ExecuteSQLTask]
      - Execute SQL Task - Update IsCurrent on Exception Table and Delete Old Records [ExecuteSQLTask]
- Sequence Container [SEQUENCE]
  - SeqCont -  Dynamics Import Validations - Daily [SEQUENCE]
    - Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake [Pipeline]
    - Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old [Pipeline]
    - Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag [ExecuteSQLTask]
    - Execute SQL Task - Truncate Staging [ExecuteSQLTask]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Master_Container["Master Container"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data["Merge and Update Sales Data"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily["SeqCont -  Dynamics Import Validations - Daily"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake["Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old["Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag["Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Execute_SQL_Task___Truncate_Staging["Execute SQL Task - Truncate Staging"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Initial_Transaction_Insert_Merges["SeqCont - Execute Initial Transaction Insert Merges"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Initial_Transaction_Insert_Merges_Execute_SQL_Task___spMergeDynamicsDiscountFacts["Execute SQL Task - spMergeDynamicsDiscountFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Initial_Transaction_Insert_Merges_Execute_SQL_Task___spMergeDynamicsPaymentFacts["Execute SQL Task - spMergeDynamicsPaymentFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Initial_Transaction_Insert_Merges_Execute_SQL_Task___spMergeDynamicsSalesDetailFacts["Execute SQL Task - spMergeDynamicsSalesDetailFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Initial_Transaction_Insert_Merges_Execute_SQL_Task___spMergeDynamicsTaxFacts["Execute SQL Task - spMergeDynamicsTaxFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Initial_Transaction_Insert_Merges_Execute_SQL_Task___spMergeDynamicsTransactionHeaderFacts["Execute SQL Task - spMergeDynamicsTransactionHeaderFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge["SeqCont - Execute Transaction Updates Merge"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly["SeqCont -  Dynamics Import Validations - Weekly"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables["Data Flow Task - Load tmpDynamics ODATA Validation Tables"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly_Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag["Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly_Execute_SQL_Task___Truncate_Staging["Execute SQL Task - Truncate Staging"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables["SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_Execute_SQL_Task___Delete_Transactions_From_Fact_Tables["Execute SQL Task - Delete Transactions From Fact Tables"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_SeqCont___Execute_Insert_Merges["SeqCont - Execute Insert Merges"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_SeqCont___Execute_Insert_Merges_Execute_SQL_Task___spMergeDynamicsDiscountFacts["Execute SQL Task - spMergeDynamicsDiscountFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_SeqCont___Execute_Insert_Merges_Execute_SQL_Task___spMergeDynamicsPaymentFacts["Execute SQL Task - spMergeDynamicsPaymentFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_SeqCont___Execute_Insert_Merges_Execute_SQL_Task___spMergeDynamicsSalesDetailFacts["Execute SQL Task - spMergeDynamicsSalesDetailFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_SeqCont___Execute_Insert_Merges_Execute_SQL_Task___spMergeDynamicsTaxFacts["Execute SQL Task - spMergeDynamicsTaxFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_SeqCont___Execute_Insert_Merges_Execute_SQL_Task___spMergeDynamicsTransactionHeaderFacts["Execute SQL Task - spMergeDynamicsTransactionHeaderFacts"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn["SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___New["Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - New"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___Old["Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - Old"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_for_Negate_Only_Trans["Execute SQL Task - Update Step 2 - Set IsCurrent to Null for Negate Only Trans"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions___Negate_Only["Execute SQL Task - Update Step 3 - Insert Negating Transactions - Negate Only"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base["SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task____Update_Step_4___Insert_Updated_Transaction_Data["Execute SQL Task -  Update Step 4 - Insert Updated Transaction Data"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Updated["Execute SQL Task - Update Step 1 - Identify Records to Be Updated"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null["Execute SQL Task - Update Step 2 - Set IsCurrent to Null"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions["Execute SQL Task - Update Step 3 - Insert Negating Transactions"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data["SeqCont - Stage Sales Data"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables["SeqCont - Load Staging Tables"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_Execute_SQL_Task___Exclude_Trans_Before_Cutover_Start_Date["Execute SQL Task - Exclude Trans Before Cutover Start Date"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_Execute_SQL_Task___Truncate_Stage["Execute SQL Task - Truncate Stage"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Clean_Up_Payment_Table["SeqCont - Clean Up Payment Table"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Clean_Up_Payment_Table_Execute_SQL_Task___Clean_up__0_Payment_Lines["Execute SQL Task - Clean up $0 Payment Lines"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Clean_Up_Payment_Table_Execute_SQL_Task___Clean_up_1_Cent_Variances["Execute SQL Task - Clean up 1 Cent Variances"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Discounts_and_Tax_Stage["SeqCont - Load Discounts and Tax Stage"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Discounts_and_Tax_Stage_Data_Flow_Task___Load_Discounts___New["Data Flow Task - Load Discounts - New"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Discounts_and_Tax_Stage_Data_Flow_Task___UK_and_IE_TAx["Data Flow Task - UK and IE TAx"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Discounts_and_Tax_Stage_Data_Flow_Task___US_and_CA_Tax["Data Flow Task - US and CA Tax"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage["SeqCont - Load Header and Detail Stage"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Data_Flow_Task___Load_Header["Data Flow Task - Load Header"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Data_Flow_Task___Load_Sales_Detail___Sound_Chip["Data Flow Task - Load Sales Detail - Sound Chip"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Data_Flow_Task___Load_Sales_Detail_Discounts["Data Flow Task - Load Sales Detail Discounts"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_DF___Header__1_store_["DF - Header (1 store)"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_DF___Load_Sales_Detail___Sound_Chip__1_store_["DF - Load Sales Detail - Sound Chip (1 store)"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Execute_SQL_Task___Append_Blank_Sound_Chip___New["Execute SQL Task - Append Blank Sound Chip - New"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Payment_Table["SeqCont - Load Payment Table"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Payment_Table_Data_Flow_Task___Load_Payments["Data Flow Task - Load Payments"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data["SeqCont - Load Tax  Discount and Tender Reference Data"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Discount_Ref_Table["SeqCont - Load Discount Ref Table"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Discount_Ref_Table_Data_Flow_Task["Data Flow Task"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Discount_Ref_Table_Execute_SQL_Task["Execute SQL Task"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tax_Data_from_AW___Replaced_by_Dans_ETL["SeqCont - Load Tax Data from AW - Replaced by Dans ETL"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tax_Data_from_AW___Replaced_by_Dans_ETL_Data_Flow_Task["Data Flow Task"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tax_Data_from_AW___Replaced_by_Dans_ETL_Execute_SQL_Task["Execute SQL Task"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Exchange_Ref_Table["SeqCont - Load Tender Exchange Ref Table"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Exchange_Ref_Table_Data_Flow_Task["Data Flow Task"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Exchange_Ref_Table_Execute_SQL_Task["Execute SQL Task"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Exchange_Ref_Table_spMergeDynamicsTenderExchangeFacts["spMergeDynamicsTenderExchangeFacts"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Facts__Reference_Table["SeqCont - Load Tender Facts  Reference Table"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Facts__Reference_Table_Data_Flow_Task["Data Flow Task"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Facts__Reference_Table_Execute_SQL_Task["Execute SQL Task"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing["SeqCont - Validations and  Exception Routing"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing_Data_Flow_Task___Route_Exceptions_to_Review_Table___With_Item_in_Dynamics_Check["Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing_Execute_SQL_Task___Delete_Exception_Records_From_Staging_Tables["Execute SQL Task - Delete Exception Records From Staging Tables"]
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing_Execute_SQL_Task___Update_IsCurrent_on_Exception_Table_and_Delete_Old_Records["Execute SQL Task - Update IsCurrent on Exception Table and Delete Old Records"]
    n_Package_Sequence_Container["Sequence Container"]
    n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily["SeqCont -  Dynamics Import Validations - Daily"]
    n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake["Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake"]
    n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old["Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old"]
    n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag["Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag"]
    n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Execute_SQL_Task___Truncate_Staging["Execute SQL Task - Truncate Staging"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Execute_SQL_Task___Truncate_Staging --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily_Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly_Execute_SQL_Task___Truncate_Staging --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly_Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_Execute_SQL_Task___Delete_Transactions_From_Fact_Tables --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables_SeqCont___Execute_Insert_Merges
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Negated_Only___New --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_for_Negate_Only_Trans
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null_for_Negate_Only_Trans --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn_Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions___Negate_Only
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task___Update_Step_1___Identify_Records_to_Be_Updated --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task___Update_Step_2___Set_IsCurrent_to_Null --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task___Update_Step_3___Insert_Negating_Transactions --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base_Execute_SQL_Task____Update_Step_4___Insert_Updated_Transaction_Data
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont____Dynamics_Import_Validations___Weekly --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Excecute_Transactions_Update_Merge___Transactions_Stuck_in_Dynamics_Staging_Tables --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute_Transaction_Updates_Merge___Transactions_Exist_in_Base --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge_SeqCont___Execute__AW_Transaction_Deleted_Merge___Negate_Only_to_Dyn
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Initial_Transaction_Insert_Merges --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily
    n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont____Dynamics_Import_Validations___Daily --> n_Package_Master_Container_Merge_and_Update_Sales_Data_SeqCont___Execute_Transaction_Updates_Merge
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Clean_Up_Payment_Table_Execute_SQL_Task___Clean_up__0_Payment_Lines --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Clean_Up_Payment_Table_Execute_SQL_Task___Clean_up_1_Cent_Variances
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Discounts_and_Tax_Stage_Data_Flow_Task___UK_and_IE_TAx --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Discounts_and_Tax_Stage_Data_Flow_Task___US_and_CA_Tax
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Data_Flow_Task___Load_Sales_Detail___Sound_Chip --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Data_Flow_Task___Load_Sales_Detail_Discounts
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Data_Flow_Task___Load_Sales_Detail_Discounts --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Execute_SQL_Task___Append_Blank_Sound_Chip___New
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Data_Flow_Task___Load_Header --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage_Data_Flow_Task___Load_Sales_Detail___Sound_Chip
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Discounts_and_Tax_Stage
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_Execute_SQL_Task___Truncate_Stage --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Header_and_Detail_Stage
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Discounts_and_Tax_Stage --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Payment_Table
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Load_Payment_Table --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Clean_Up_Payment_Table
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_SeqCont___Clean_Up_Payment_Table --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables_Execute_SQL_Task___Exclude_Trans_Before_Cutover_Start_Date
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Discount_Ref_Table_Execute_SQL_Task --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Discount_Ref_Table_Data_Flow_Task
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tax_Data_from_AW___Replaced_by_Dans_ETL_Execute_SQL_Task --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tax_Data_from_AW___Replaced_by_Dans_ETL_Data_Flow_Task
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Exchange_Ref_Table_Execute_SQL_Task --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Exchange_Ref_Table_Data_Flow_Task
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Exchange_Ref_Table_Data_Flow_Task --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Exchange_Ref_Table_spMergeDynamicsTenderExchangeFacts
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Facts__Reference_Table_Execute_SQL_Task --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data_SeqCont___Load_Tender_Facts__Reference_Table_Data_Flow_Task
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing_Execute_SQL_Task___Update_IsCurrent_on_Exception_Table_and_Delete_Old_Records --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing_Data_Flow_Task___Route_Exceptions_to_Review_Table___With_Item_in_Dynamics_Check
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing_Data_Flow_Task___Route_Exceptions_to_Review_Table___With_Item_in_Dynamics_Check --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing_Execute_SQL_Task___Delete_Exception_Records_From_Staging_Tables
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Tax__Discount_and_Tender_Reference_Data --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables
    n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Load_Staging_Tables --> n_Package_Master_Container_SeqCont___Stage_Sales_Data_SeqCont___Validations_and__Exception_Routing
    n_Package_Master_Container_SeqCont___Stage_Sales_Data --> n_Package_Master_Container_Merge_and_Update_Sales_Data
    n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Execute_SQL_Task___Truncate_Staging --> n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old
    n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___Old --> n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake
    n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Data_Flow_Task___Load_tmpDynamics_ODATA_Validation_Tables___New_DataLake --> n_Package_Sequence_Container_SeqCont____Dynamics_Import_Validations___Daily_Execute_SQL_Task___Set_IsInDynamicsFlag_or_IsInDynamicsStagingFlag
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | DateTimeStamp | Yes |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | PreviousWeekDate | Yes |
| User | PreviousWeekDateAsDATE | Yes |
| User | SqlStringAwDiscountRefTable | Yes |
| User | SqlStringAwDiscountRefTableEligibleLines | Yes |
| User | SqlStringAwDiscountRefTableTargetTransactions | Yes |
| User | SqlStringAwDiscountRefTableV2 | Yes |
| User | SqlStringAwDiscountRefTableV3 | Yes |
| User | SqlStringAwDiscountRefTableV4 | Yes |
| User | SqlStringAwTenderExchangeDetails | Yes |
| User | SqlStringDwTenderPercentageRef | Yes |
| User | SqlStringDwTenderPercentageRefV2 | Yes |
| User | SqlStringDwTenderPercentageRefV3 | Yes |
| User | SqlStringEJTenderExchangeTargetTrans | Yes |
| User | SqlStringHeaderStageSourceV6 | Yes |
| User | SqlStringHeaderStageSourceV7 | Yes |
| User | SqlStringSalesDetailStageSourceFeeHandlingV7 | Yes |
| User | SqlStringSalesDetailStageSourceFeeHandlingV8 | Yes |
| User | SqlStringSalesDetailStageSourceFeeHandlingV9 | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | v7 | Yes |
| User | v9 | Yes |

### Expression-bound variable values

#### User::DateTimeStamp

**Expression:**

```sql
(DT_WSTR,4)DATEPART("yyyy",GetDate()) 
+ (DT_WSTR,4)DATEPART("mm",GetDate()) 
+ (DT_WSTR,4)DATEPART("dd",GetDate()) 
+ (DT_WSTR,4)DATEPART("hh",GetDate()) 
+ (DT_WSTR,4)DATEPART("mi",GetDate()) 
+ (DT_WSTR,4)DATEPART("ss",GetDate()) 
+ (DT_WSTR,4)DATEPART("ms",GetDate())
```

**Evaluated value:**

```sql
202651114252603
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
5/1/2026
```

#### User::EndDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::EndDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::EndDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::EndDate]),2)
```

**Evaluated value:**

```sql
2026-05-01
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
5/1/2026
```

#### User::GetDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::GetDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::GetDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::GetDate]),2)
```

**Evaluated value:**

```sql
2026-05-01
```

#### User::PreviousWeekDate

**Expression:**

```sql
dateadd("dd", -7 , @[User::GetDate] )
```

**Evaluated value:**

```sql
4/24/2026
```

#### User::PreviousWeekDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::PreviousWeekDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::PreviousWeekDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::PreviousWeekDate]),2)
```

**Evaluated value:**

```sql
2026-04-24
```

#### User::SqlStringAwDiscountRefTable

**Expression:**

```sql
"
with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType

from Summary1 s 
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 

line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr
order by 2"
```

**Evaluated value:**

```sql

with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= 7
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType

from Summary1 s 
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 

line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr
order by 2
```

#### User::SqlStringAwDiscountRefTableEligibleLines

**Expression:**

```sql
"select tdf.transaction_id, tdf.transaction_line_seq
from TransactionDetailFactsDynamics tdf (nolock) 
join date_dim dd (nolock) on dd.date_key=tdf.date_key
join line_object_dim lod (nolock) on lod.Line_Object_Key=tdf.line_object_key
where lod.Line_Object in (100, 102, 103, 104, 115,101,105,202,204,292,799,701,710,711,714,200,203,294, 400, 401, 402, 403, 404, 410, 1625,296) -- these are the LOs we are allowing to flow to Dynamics 
and DATEDIFF(dd,dd.actual_date, getdate()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"

group by tdf.transaction_id, tdf.transaction_line_seq
Order by tdf.transaction_id, tdf.transaction_line_seq
"
```

**Evaluated value:**

```sql
select tdf.transaction_id, tdf.transaction_line_seq
from TransactionDetailFactsDynamics tdf (nolock) 
join date_dim dd (nolock) on dd.date_key=tdf.date_key
join line_object_dim lod (nolock) on lod.Line_Object_Key=tdf.line_object_key
where lod.Line_Object in (100, 102, 103, 104, 115,101,105,202,204,292,799,701,710,711,714,200,203,294, 400, 401, 402, 403, 404, 410, 1625,296) -- these are the LOs we are allowing to flow to Dynamics 
and DATEDIFF(dd,dd.actual_date, getdate()) <= 7

group by tdf.transaction_id, tdf.transaction_line_seq
Order by tdf.transaction_id, tdf.transaction_line_seq

```

#### User::SqlStringAwDiscountRefTableTargetTransactions

**Expression:**

```sql
"
with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
--where avh.transaction_id in ('445530260','445532413','445533821','445521171','445864979','450547996','447974050','449683383','450693682','448460254','450734674','452093385','450734682','452100720','451992197','415185156','451995268','451490651','448377116','445504561','445564084','445526683','446870232','449182098','448060545','449214514','449175830','451287766','452237484','451062109','447355553','448911292','445550437','445550440','445644625','446714970','445777666','445783946','450279768','447945235','449150097','450054158','431233780','451317913','451493062','452026528','447920976','447979911','445493748','445495947','446943003','446942992','449671490','448397175','449473638','450102040','451314319','452081109','451792528','449004495','447845608')
where avh.transaction_id in ('445530627')
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
--where avh.av_transaction_id in ('445530260','445532413','445533821','445521171','445864979','450547996','447974050','449683383','450693682','448460254','450734674','452093385','450734682','452100720','451992197','415185156','451995268','451490651','448377116','445504561','445564084','445526683','446870232','449182098','448060545','449214514','449175830','451287766','452237484','451062109','447355553','448911292','445550437','445550440','445644625','446714970','445777666','445783946','450279768','447945235','449150097','450054158','431233780','451317913','451493062','452026528','447920976','447979911','445493748','445495947','446943003','446942992','449671490','448397175','449473638','450102040','451314319','452081109','451792528','449004495','447845608')
where avh.av_transaction_id in ('445530627')
and datediff(dd,avh.transaction_date,GETDATE()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType

from Summary1 s 
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 

line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr
order by 2"
```

**Evaluated value:**

```sql

with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
--where avh.transaction_id in ('445530260','445532413','445533821','445521171','445864979','450547996','447974050','449683383','450693682','448460254','450734674','452093385','450734682','452100720','451992197','415185156','451995268','451490651','448377116','445504561','445564084','445526683','446870232','449182098','448060545','449214514','449175830','451287766','452237484','451062109','447355553','448911292','445550437','445550440','445644625','446714970','445777666','445783946','450279768','447945235','449150097','450054158','431233780','451317913','451493062','452026528','447920976','447979911','445493748','445495947','446943003','446942992','449671490','448397175','449473638','450102040','451314319','452081109','451792528','449004495','447845608')
where avh.transaction_id in ('445530627')
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
--where avh.av_transaction_id in ('445530260','445532413','445533821','445521171','445864979','450547996','447974050','449683383','450693682','448460254','450734674','452093385','450734682','452100720','451992197','415185156','451995268','451490651','448377116','445504561','445564084','445526683','446870232','449182098','448060545','449214514','449175830','451287766','452237484','451062109','447355553','448911292','445550437','445550440','445644625','446714970','445777666','445783946','450279768','447945235','449150097','450054158','431233780','451317913','451493062','452026528','447920976','447979911','445493748','445495947','446943003','446942992','449671490','448397175','449473638','450102040','451314319','452081109','451792528','449004495','447845608')
where avh.av_transaction_id in ('445530627')
and datediff(dd,avh.transaction_date,GETDATE()) <= 7
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType

from Summary1 s 
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 

line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr
order by 2
```

#### User::SqlStringAwDiscountRefTableV2

**Expression:**

```sql
"
with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType,
line_action as LineAction

from Summary1 s 
where line_action not in (2,12,15,26) 
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr,
line_action
having sum(pos_discount_amount) >= 0 -- Added Jan 19 2023 If stores do a price markdown that increases the price this comes in as negative and skews calculations
order by transaction_id, line_sequence "
```

**Evaluated value:**

```sql

with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= 7
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType,
line_action as LineAction

from Summary1 s 
where line_action not in (2,12,15,26) 
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr,
line_action
having sum(pos_discount_amount) >= 0 -- Added Jan 19 2023 If stores do a price markdown that increases the price this comes in as negative and skews calculations
order by transaction_id, line_sequence 
```

#### User::SqlStringAwDiscountRefTableV3

**Expression:**

```sql
"
with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType,
line_action as LineAction

from Summary1 s 
--where line_action not in (2,12,15,26) -- 3/30/2023 We must consider return discount line actions -- Example Trans Id: 467484542
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr,
line_action
having sum(pos_discount_amount) >= 0 -- Added Jan 19 2023 If stores do a price markdown that increases the price this comes in as negative and skews calculations
order by transaction_id, line_sequence "
```

**Evaluated value:**

```sql

with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= 7
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType,
line_action as LineAction

from Summary1 s 
--where line_action not in (2,12,15,26) -- 3/30/2023 We must consider return discount line actions -- Example Trans Id: 467484542
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr,
line_action
having sum(pos_discount_amount) >= 0 -- Added Jan 19 2023 If stores do a price markdown that increases the price this comes in as negative and skews calculations
order by transaction_id, line_sequence 
```

#### User::SqlStringAwDiscountRefTableV4

**Expression:**

```sql
"
with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case
	when s.line_object = '1626' --1626 Subtotal Bear Bucks Discount - Per Joel Berger Should be a line level discount - Added 4/4/2023
		then 'Line'
	when left(line_object_description, 8) = 'Subtotal'
		then 'Header'
	else 'Line'
		end 
	as DiscountType,
line_action as LineAction

from Summary1 s 
--where line_action not in (2,12,15,26) -- 3/30/2023 We must consider return discount line actions -- Example Trans Id: 467484542
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr,
line_action
having sum(pos_discount_amount) >= 0 -- Added Jan 19 2023 If stores do a price markdown that increases the price this comes in as negative and skews calculations
order by transaction_id, line_sequence "
```

**Evaluated value:**

```sql

with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*,
avl.line_action
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= 7
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case
	when s.line_object = '1626' --1626 Subtotal Bear Bucks Discount - Per Joel Berger Should be a line level discount - Added 4/4/2023
		then 'Line'
	when left(line_object_description, 8) = 'Subtotal'
		then 'Header'
	else 'Line'
		end 
	as DiscountType,
line_action as LineAction

from Summary1 s 
--where line_action not in (2,12,15,26) -- 3/30/2023 We must consider return discount line actions -- Example Trans Id: 467484542
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr,
line_action
having sum(pos_discount_amount) >= 0 -- Added Jan 19 2023 If stores do a price markdown that increases the price this comes in as negative and skews calculations
order by transaction_id, line_sequence 
```

#### User::SqlStringAwTenderExchangeDetails

**Expression:**

```sql
"
select 
th.transaction_id,
th.cashier_no, 
th.store_no, 
th.register_no, 
th.transaction_no, 
th.transaction_date, 
cast (th.transaction_date as date) as transaction_date_cast, 
tl.line_sequence, 
tl.line_id, 
lo.line_object_description, 
la.line_action_display_descr, 
tl.line_object, 
tl.line_action, 
tl.gross_line_amount, 
tl.pos_discount_amount, 
tl.reference_no, 
isnull(OC.DFLT_CRNCY_CODE,'USD') as currency_code
from transaction_line tl (nolock) 
join transaction_header th (nolock) on th.transaction_id=tl.transaction_id
join line_object lo (nolock) on lo.line_object=tl.line_object
join line_action la (nolock) on la.line_action=tl.line_action
left join ORG_CHN OC (nolock) ON OC.ORG_CHN_NUM=th.store_no
where tl.line_action in ('2','12','23','26','27') -- Returned, Refunded,remitted in exchange, Cashed, Credited 
and tl.gross_line_amount <> 0
and tl.gross_line_amount - tl.pos_discount_amount <> 0
and DATEDIFF(dd,th.transaction_date, getdate()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
union 
select
th.av_transaction_id as transaction_id, 
th.cashier_no, 
th.store_no, 
th.register_no, 
th.transaction_no, 
th.transaction_date, 
cast (th.transaction_date as date) as transaction_date_cast, 
tl.line_sequence, 
tl.line_id, 
lo.line_object_description, 
la.line_action_display_descr, 
tl.line_object, 
tl.line_action, 
tl.gross_line_amount, 
tl.pos_discount_amount, 
tl.reference_no, 
isnull(OC.DFLT_CRNCY_CODE,'USD') as currency_code
from av_transaction_line tl (nolock) 
join av_transaction_header th (nolock) on th.av_transaction_id=tl.av_transaction_id
join line_object lo (nolock) on lo.line_object=tl.line_object
join line_action la (nolock) on la.line_action=tl.line_action
left join ORG_CHN OC (nolock) ON OC.ORG_CHN_NUM=th.store_no
where tl.line_action in ('2','12','23','26','27') -- Returned, Refunded,remitted in exchange, Cashed, Credited 
and tl.gross_line_amount <> 0
and tl.gross_line_amount - tl.pos_discount_amount <> 0
and DATEDIFF(dd,th.transaction_date, getdate()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
--Order by 1 
Order by store_no, register_no, transaction_no, cast (th.transaction_date as date)
"
```

**Evaluated value:**

```sql

select 
th.transaction_id,
th.cashier_no, 
th.store_no, 
th.register_no, 
th.transaction_no, 
th.transaction_date, 
cast (th.transaction_date as date) as transaction_date_cast, 
tl.line_sequence, 
tl.line_id, 
lo.line_object_description, 
la.line_action_display_descr, 
tl.line_object, 
tl.line_action, 
tl.gross_line_amount, 
tl.pos_discount_amount, 
tl.reference_no, 
isnull(OC.DFLT_CRNCY_CODE,'USD') as currency_code
from transaction_line tl (nolock) 
join transaction_header th (nolock) on th.transaction_id=tl.transaction_id
join line_object lo (nolock) on lo.line_object=tl.line_object
join line_action la (nolock) on la.line_action=tl.line_action
left join ORG_CHN OC (nolock) ON OC.ORG_CHN_NUM=th.store_no
where tl.line_action in ('2','12','23','26','27') -- Returned, Refunded,remitted in exchange, Cashed, Credited 
and tl.gross_line_amount <> 0
and tl.gross_line_amount - tl.pos_discount_amount <> 0
and DATEDIFF(dd,th.transaction_date, getdate()) <= 7
union 
select
th.av_transaction_id as transaction_id, 
th.cashier_no, 
th.store_no, 
th.register_no, 
th.transaction_no, 
th.transaction_date, 
cast (th.transaction_date as date) as transaction_date_cast, 
tl.line_sequence, 
tl.line_id, 
lo.line_object_description, 
la.line_action_display_descr, 
tl.line_object, 
tl.line_action, 
tl.gross_line_amount, 
tl.pos_discount_amount, 
tl.reference_no, 
isnull(OC.DFLT_CRNCY_CODE,'USD') as currency_code
from av_transaction_line tl (nolock) 
join av_transaction_header th (nolock) on th.av_transaction_id=tl.av_transaction_id
join line_object lo (nolock) on lo.line_object=tl.line_object
join line_action la (nolock) on la.line_action=tl.line_action
left join ORG_CHN OC (nolock) ON OC.ORG_CHN_NUM=th.store_no
where tl.line_action in ('2','12','23','26','27') -- Returned, Refunded,remitted in exchange, Cashed, Credited 
and tl.gross_line_amount <> 0
and tl.gross_line_amount - tl.pos_discount_amount <> 0
and DATEDIFF(dd,th.transaction_date, getdate()) <= 7
--Order by 1 
Order by store_no, register_no, transaction_no, cast (th.transaction_date as date)

```

#### User::SqlStringDwTenderPercentageRef

**Expression:**

```sql
"with TransTenderTotal as (
select tfd.transaction_id, 
case when tender_key = '16'
	then sum(tender_amt*-1) 
	else sum(tender_amt)
	end as tender_amt 
from TenderFactsDynamics  tfd (nolock) 
join date_dim dd (nolock) on dd.date_key = tfd.date_key
where tender_key <> -1
and DATEDIFF(dd,dd.actual_date,getdate()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by tfd.transaction_id, tender_key

), 

TransTenderTotalSummary as 
(


select Transaction_id, 
sum(tender_amt) as TotalTenderAmount
from TransTenderTotal
group by transaction_id
having sum(tender_amt) > 0 

) 

select tfd.transaction_id, 
tfd.tender_key, 
--tfd.tender_amt, 
case when  tfd.tender_key in ('16') then 
	tfd.tender_amt*-1/ts.TotalTenderAmount 
	else tfd.tender_amt/ts.TotalTenderAmount 
	end as TenderPercentage 
from TenderFactsDynamics TFD (nolock) 
join TransTenderTotalSummary TS on tfd.transaction_id=ts.transaction_id
	and tfd.tender_key <> - 1
order by 1, 2
"
```

**Evaluated value:**

```sql
with TransTenderTotal as (
select tfd.transaction_id, 
case when tender_key = '16'
	then sum(tender_amt*-1) 
	else sum(tender_amt)
	end as tender_amt 
from TenderFactsDynamics  tfd (nolock) 
join date_dim dd (nolock) on dd.date_key = tfd.date_key
where tender_key <> -1
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by tfd.transaction_id, tender_key

), 

TransTenderTotalSummary as 
(


select Transaction_id, 
sum(tender_amt) as TotalTenderAmount
from TransTenderTotal
group by transaction_id
having sum(tender_amt) > 0 

) 

select tfd.transaction_id, 
tfd.tender_key, 
--tfd.tender_amt, 
case when  tfd.tender_key in ('16') then 
	tfd.tender_amt*-1/ts.TotalTenderAmount 
	else tfd.tender_amt/ts.TotalTenderAmount 
	end as TenderPercentage 
from TenderFactsDynamics TFD (nolock) 
join TransTenderTotalSummary TS on tfd.transaction_id=ts.transaction_id
	and tfd.tender_key <> - 1
order by 1, 2

```

#### User::SqlStringDwTenderPercentageRefV2

**Expression:**

```sql
"with TransTenderTotal as (
select tfd.transaction_id, 
abs( sum(tender_amt)) as tender_amt 
from TenderFactsDynamics  tfd (nolock) 
join date_dim dd (nolock) on dd.date_key = tfd.date_key
where tender_key <> -1
and DATEDIFF(dd,dd.actual_date,getdate()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by tfd.transaction_id, tender_key

), 

TransTenderTotalSummary as 
(


select Transaction_id, 
abs (sum(tender_amt)) as TotalTenderAmount
from TransTenderTotal
group by transaction_id
having sum(tender_amt) > 0 

) 

select tfd.transaction_id, 
tfd.tender_key, 
abs(tfd.tender_amt/ts.TotalTenderAmount) as TenderPercentage 
from TenderFactsDynamics TFD (nolock) 
join TransTenderTotalSummary TS on tfd.transaction_id=ts.transaction_id
	and tfd.tender_key <> - 1
order by 1, 2
"
```

**Evaluated value:**

```sql
with TransTenderTotal as (
select tfd.transaction_id, 
abs( sum(tender_amt)) as tender_amt 
from TenderFactsDynamics  tfd (nolock) 
join date_dim dd (nolock) on dd.date_key = tfd.date_key
where tender_key <> -1
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by tfd.transaction_id, tender_key

), 

TransTenderTotalSummary as 
(


select Transaction_id, 
abs (sum(tender_amt)) as TotalTenderAmount
from TransTenderTotal
group by transaction_id
having sum(tender_amt) > 0 

) 

select tfd.transaction_id, 
tfd.tender_key, 
abs(tfd.tender_amt/ts.TotalTenderAmount) as TenderPercentage 
from TenderFactsDynamics TFD (nolock) 
join TransTenderTotalSummary TS on tfd.transaction_id=ts.transaction_id
	and tfd.tender_key <> - 1
order by 1, 2

```

#### User::SqlStringDwTenderPercentageRefV3

**Expression:**

```sql
"with TransTenderTotal as (
select tfd.transaction_id,  
abs(sum(tender_amt)) as tender_amt
from TenderFactsDynamics  tfd (nolock) 
join date_dim dd (nolock) on dd.date_key = tfd.date_key
where tender_key not in ('-1','408') -- Tax , Serialized Coupon 
and DATEDIFF(dd,dd.actual_date,getdate()) <= " +
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by tfd.transaction_id, tender_key

), 

TransTenderTotalSummary as 
(


select Transaction_id, 
abs (sum(tender_amt)) as TotalTenderAmount
from TransTenderTotal
group by transaction_id
having sum(tender_amt) > 0 

) 

select tfd.transaction_id, 
tfd.tender_key, 
abs(tfd.tender_amt/ts.TotalTenderAmount) as TenderPercentage 
from TenderFactsDynamics TFD (nolock) 
join TransTenderTotalSummary TS on tfd.transaction_id=ts.transaction_id
	and tfd.tender_key not in ('-1','408') -- Tax , Serialized Coupon 
order by 1, 2
"
```

**Evaluated value:**

```sql
with TransTenderTotal as (
select tfd.transaction_id,  
abs(sum(tender_amt)) as tender_amt
from TenderFactsDynamics  tfd (nolock) 
join date_dim dd (nolock) on dd.date_key = tfd.date_key
where tender_key not in ('-1','408') -- Tax , Serialized Coupon 
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by tfd.transaction_id, tender_key

), 

TransTenderTotalSummary as 
(


select Transaction_id, 
abs (sum(tender_amt)) as TotalTenderAmount
from TransTenderTotal
group by transaction_id
having sum(tender_amt) > 0 

) 

select tfd.transaction_id, 
tfd.tender_key, 
abs(tfd.tender_amt/ts.TotalTenderAmount) as TenderPercentage 
from TenderFactsDynamics TFD (nolock) 
join TransTenderTotalSummary TS on tfd.transaction_id=ts.transaction_id
	and tfd.tender_key not in ('-1','408') -- Tax , Serialized Coupon 
order by 1, 2

```

#### User::SqlStringEJTenderExchangeTargetTrans

**Expression:**

```sql
"
select STORENO as store_no_ej, 
TILLNO as register_no_ej,
TRANNO as transaction_no_ej, 
[DATETIME] as Transaction_Date_raw_ej,
cast([DATETIME] as date) as Transaction_Date_cast_ej
--, *
from [dbo].[Transactions] (nolock) 
where TRANTYPE = '15' -- TenderExchange 
and VOID <> 1
and DATEDIFF(dd,[datetime],getdate()) <= "+
(DT_WSTR, 4) @[$Package::DaysToGoBack]+"
--order by 4, 1, 3
group by STORENO,
TILLNO,
TRANNO, 
[DATETIME],
cast([DATETIME] as date) 
order by STORENO, TILLNO, TRANNO, cast([DATETIME] as date)
"
```

**Evaluated value:**

```sql

select STORENO as store_no_ej, 
TILLNO as register_no_ej,
TRANNO as transaction_no_ej, 
[DATETIME] as Transaction_Date_raw_ej,
cast([DATETIME] as date) as Transaction_Date_cast_ej
--, *
from [dbo].[Transactions] (nolock) 
where TRANTYPE = '15' -- TenderExchange 
and VOID <> 1
and DATEDIFF(dd,[datetime],getdate()) <= 7
--order by 4, 1, 3
group by STORENO,
TILLNO,
TRANNO, 
[DATETIME],
cast([DATETIME] as date) 
order by STORENO, TILLNO, TRANNO, cast([DATETIME] as date)

```

#### User::SqlStringHeaderStageSourceV6

**Expression:**

```sql
"
With RegSales as  (
select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete
	,null as CustAccount
	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.transaction_id as RetailReceiptId
	,tdf.cashier_id as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
	,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
	,cast(dd.actual_date  as date) TransDate 
	, 'Sales' as RetailTransactionType
	, null as BABIntRetailProcessed	
	, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
	, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
	, tdf.transaction_no as TransactionNumber
from TransactionDetailFactsDynamics TDF (nolock) 
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock) on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on tdf.date_key=dd.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header due to ES Orders and how that is handled in detail lines 
	left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tdf.transaction_id
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801') -- Added Varsity Locations on 1/25/2024
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,203,204,292,799,701,710,711,714)

	
		) -- Misc Fee and Donation lines 

	or ( lod.Line_Object in (200,203,296)

		) -- Shipping Fee Lines

	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+
 (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 

	cast (tdf.register_num  as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tdf.transaction_id
	,tdf.cashier_id
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	,isnull(ds.SumTransDiscounts,0.00)
	,isnull(ds.SumTransHeaderDiscounts,0.00)
	, tdf.transaction_no
), 

--union 
TenderExchange as (


select cast(tef.register_no as varchar) as RetailTerminalId_Incomplete
,null as CustAccount
,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
, case when sd.country = 'IE' then 'UK'
	else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
,tef.transaction_id as RetailReceiptId
,tef.cashier_no as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
,cast(dd.actual_date  as date) TransDate 
, 'Sales' as RetailTransactionType
, null as BABIntRetailProcessed	
--, 0.00 as DiscAmount
--, 0.00 as TotalDiscAmount
, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
, tef.transaction_no as TransactionNumber
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tef.transaction_id
where 1=1
and (tef.line_object in ('633','404')and line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13')  -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801') -- Added Varsity Locations on 1/25/2024
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+
 (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 
	cast (tef.register_no as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tef.transaction_id
	,tef.cashier_no
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	, tef.transaction_no 
	, isnull(ds.SumTransDiscounts,0.00) 
	, isnull(ds.SumTransHeaderDiscounts,0.00)
)

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te
order by 9, 3, 5"
```

**Evaluated value:**

```sql

With RegSales as  (
select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete
	,null as CustAccount
	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.transaction_id as RetailReceiptId
	,tdf.cashier_id as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
	,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
	,cast(dd.actual_date  as date) TransDate 
	, 'Sales' as RetailTransactionType
	, null as BABIntRetailProcessed	
	, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
	, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
	, tdf.transaction_no as TransactionNumber
from TransactionDetailFactsDynamics TDF (nolock) 
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock) on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on tdf.date_key=dd.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header due to ES Orders and how that is handled in detail lines 
	left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tdf.transaction_id
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801') -- Added Varsity Locations on 1/25/2024
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,203,204,292,799,701,710,711,714)

	
		) -- Misc Fee and Donation lines 

	or ( lod.Line_Object in (200,203,296)

		) -- Shipping Fee Lines

	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 

	cast (tdf.register_num  as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tdf.transaction_id
	,tdf.cashier_id
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	,isnull(ds.SumTransDiscounts,0.00)
	,isnull(ds.SumTransHeaderDiscounts,0.00)
	, tdf.transaction_no
), 

--union 
TenderExchange as (


select cast(tef.register_no as varchar) as RetailTerminalId_Incomplete
,null as CustAccount
,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
, case when sd.country = 'IE' then 'UK'
	else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
,tef.transaction_id as RetailReceiptId
,tef.cashier_no as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
,cast(dd.actual_date  as date) TransDate 
, 'Sales' as RetailTransactionType
, null as BABIntRetailProcessed	
--, 0.00 as DiscAmount
--, 0.00 as TotalDiscAmount
, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
, tef.transaction_no as TransactionNumber
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tef.transaction_id
where 1=1
and (tef.line_object in ('633','404')and line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13')  -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801') -- Added Varsity Locations on 1/25/2024
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 
	cast (tef.register_no as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tef.transaction_id
	,tef.cashier_no
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	, tef.transaction_no 
	, isnull(ds.SumTransDiscounts,0.00) 
	, isnull(ds.SumTransHeaderDiscounts,0.00)
)

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te
order by 9, 3, 5
```

#### User::SqlStringHeaderStageSourceV7

**Expression:**

```sql
"
With RegSales as  (
select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete
	,null as CustAccount
	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.transaction_id as RetailReceiptId
	,tdf.cashier_id as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
	,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
	,cast(dd.actual_date  as date) TransDate 
	, 'Sales' as RetailTransactionType
	, null as BABIntRetailProcessed	
	, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
	, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
	, tdf.transaction_no as TransactionNumber
from TransactionDetailFactsDynamics TDF (nolock) 
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock) on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on tdf.date_key=dd.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header due to ES Orders and how that is handled in detail lines 
	left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tdf.transaction_id
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','0630','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807','437','807','808','809','810','813','2086','558','811','812','0559','0560','0561','0562','0563','0564','0566','0567','0568','0569','0571','0572','0573','2085','2087','570','574','575','576','2088','477','0816','0817','0578','0576','0577','0579','0580','0581','0582','0583','0584','0585','0586','0587','0588','0589','0590','0591','2089','2090','2801') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,203,204,292,799,701,710,711,714)

	
		) -- Misc Fee and Donation lines 

	or ( 
		lod.Line_Object in (200,203,296)
			and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines

	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+
 (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 

	cast (tdf.register_num  as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tdf.transaction_id
	,tdf.cashier_id
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	,isnull(ds.SumTransDiscounts,0.00)
	,isnull(ds.SumTransHeaderDiscounts,0.00)
	, tdf.transaction_no
), 

--union 
TenderExchange as (


select cast(tef.register_no as varchar) as RetailTerminalId_Incomplete
,null as CustAccount
,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
, case when sd.country = 'IE' then 'UK'
	else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
,tef.transaction_id as RetailReceiptId
,tef.cashier_no as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
,cast(dd.actual_date  as date) TransDate 
, 'Sales' as RetailTransactionType
, null as BABIntRetailProcessed	
--, 0.00 as DiscAmount
--, 0.00 as TotalDiscAmount
, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
, tef.transaction_no as TransactionNumber
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tef.transaction_id
where 1=1
and (tef.line_object in ('633','404')and line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13')  -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','0630','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807','437','807','808','809','810','2086','558','811','812','813','0559','0560','0561','0562','0563','0564','0566','0567','0568','0569','0571','0572','0573','2085','2087','570','574','575','576','2088','477','0816','0817','0578','0576','0577','0579','0580','0581','0582','0583','0584','0585','0586','0587','0588','0589','0590','0591','2089','2090','2801') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+
 (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 
	cast (tef.register_no as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tef.transaction_id
	,tef.cashier_no
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	, tef.transaction_no 
	, isnull(ds.SumTransDiscounts,0.00) 
	, isnull(ds.SumTransHeaderDiscounts,0.00)
)

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te
order by 9, 3, 5"
```

**Evaluated value:**

```sql

With RegSales as  (
select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete
	,null as CustAccount
	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.transaction_id as RetailReceiptId
	,tdf.cashier_id as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
	,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
	,cast(dd.actual_date  as date) TransDate 
	, 'Sales' as RetailTransactionType
	, null as BABIntRetailProcessed	
	, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
	, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
	, tdf.transaction_no as TransactionNumber
from TransactionDetailFactsDynamics TDF (nolock) 
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock) on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on tdf.date_key=dd.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header due to ES Orders and how that is handled in detail lines 
	left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tdf.transaction_id
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','0630','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807','437','807','808','809','810','813','2086','558','811','812','0559','0560','0561','0562','0563','0564','0566','0567','0568','0569','0571','0572','0573','2085','2087','570','574','575','576','2088','477','0816','0817','0578','0576','0577','0579','0580','0581','0582','0583','0584','0585','0586','0587','0588','0589','0590','0591','2089','2090','2801') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,203,204,292,799,701,710,711,714)

	
		) -- Misc Fee and Donation lines 

	or ( 
		lod.Line_Object in (200,203,296)
			and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines

	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 

	cast (tdf.register_num  as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tdf.transaction_id
	,tdf.cashier_id
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	,isnull(ds.SumTransDiscounts,0.00)
	,isnull(ds.SumTransHeaderDiscounts,0.00)
	, tdf.transaction_no
), 

--union 
TenderExchange as (


select cast(tef.register_no as varchar) as RetailTerminalId_Incomplete
,null as CustAccount
,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
, case when sd.country = 'IE' then 'UK'
	else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
,tef.transaction_id as RetailReceiptId
,tef.cashier_no as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
,cast(dd.actual_date  as date) TransDate 
, 'Sales' as RetailTransactionType
, null as BABIntRetailProcessed	
--, 0.00 as DiscAmount
--, 0.00 as TotalDiscAmount
, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
, tef.transaction_no as TransactionNumber
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tef.transaction_id
where 1=1
and (tef.line_object in ('633','404')and line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13')  -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','0630','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807','437','807','808','809','810','2086','558','811','812','813','0559','0560','0561','0562','0563','0564','0566','0567','0568','0569','0571','0572','0573','2085','2087','570','574','575','576','2088','477','0816','0817','0578','0576','0577','0579','0580','0581','0582','0583','0584','0585','0586','0587','0588','0589','0590','0591','2089','2090','2801') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 
	cast (tef.register_no as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tef.transaction_id
	,tef.cashier_no
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	, tef.transaction_no 
	, isnull(ds.SumTransDiscounts,0.00) 
	, isnull(ds.SumTransHeaderDiscounts,0.00)
)

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te
order by 9, 3, 5
```

#### User::SqlStringSalesDetailStageSourceFeeHandlingV7

**Expression:**

```sql
"

with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



),

RegSales as (

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
			--else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when lod.Line_Object in ('204','205','292','296') -- Miscellaneous Fee, NSF Fee, Merchandise Contribution				
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
			when lod.Line_Object in ('403') and sd.store_id = '2013'
				then cast ('SV00015' as varchar) -- Dynamics Service Item: Web ECertificate
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292','296') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0584','0585','0591','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','0591','800','801','804','808','809','810','813') -- Added Varsity Locations on 1/25/2024
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( lod.Line_Object in (200,203,296)

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+ (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
),

TenderExchange as (

select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as OriginalPrice
		--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
		,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as Price,
	-1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, 'SV00014' as ItemId -- Hard Coded Per Joel Berger on Jan 11 2023
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where 1=1
and (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0584','0585','0591','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','0591','800','801','804','808','809','810','813') -- Added Varsity Locations on 1/25/2024
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+ (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

) 

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te

order by 12, 
2, 
3


"
```

**Evaluated value:**

```sql


with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



),

RegSales as (

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
			--else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when lod.Line_Object in ('204','205','292','296') -- Miscellaneous Fee, NSF Fee, Merchandise Contribution				
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
			when lod.Line_Object in ('403') and sd.store_id = '2013'
				then cast ('SV00015' as varchar) -- Dynamics Service Item: Web ECertificate
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292','296') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0584','0585','0591','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','0591','800','801','804','808','809','810','813') -- Added Varsity Locations on 1/25/2024
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( lod.Line_Object in (200,203,296)

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
),

TenderExchange as (

select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as OriginalPrice
		--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
		,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as Price,
	-1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, 'SV00014' as ItemId -- Hard Coded Per Joel Berger on Jan 11 2023
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where 1=1
and (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0584','0585','0591','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','0591','800','801','804','808','809','810','813') -- Added Varsity Locations on 1/25/2024
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

) 

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te

order by 12, 
2, 
3



```

#### User::SqlStringSalesDetailStageSourceFeeHandlingV8

**Expression:**

```sql
"

with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



),

RegSales as (

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
			--else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when lod.Line_Object in ('292') -- Merchandise Contribution aka Donation				
				then cast (isnull(dfm.DynamicsItemId,'SV091450') as varchar (50)) -- 2/5/2024: using Donation Service Item if no lookup found			
			when lod.Line_Object in ('204','205','296') -- Miscellaneous Fee, NSF Fee, CustomerService 			
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
			when lod.Line_Object in ('403') and sd.store_id = '2013'
				then cast ('SV00015' as varchar) -- Dynamics Service Item: Web ECertificate
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292','296') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0591','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807' ) -- Added Additional Varsity Locations on 02/08/2024 per Joel Berger direction 
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( 
		lod.Line_Object in (200,203,296)
		and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+ (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
),

TenderExchange as (

select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as OriginalPrice
		--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
		,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as Price,
	-1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, 'SV00014' as ItemId -- Hard Coded Per Joel Berger on Jan 11 2023
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where 1=1
and (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0591','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807' ) -- Added Additional Varsity Locations on 02/08/2024 per Joel Berger direction 
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+ (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

) 

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te

order by 12, 
2, 
3


"
```

**Evaluated value:**

```sql


with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



),

RegSales as (

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
			--else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when lod.Line_Object in ('292') -- Merchandise Contribution aka Donation				
				then cast (isnull(dfm.DynamicsItemId,'SV091450') as varchar (50)) -- 2/5/2024: using Donation Service Item if no lookup found			
			when lod.Line_Object in ('204','205','296') -- Miscellaneous Fee, NSF Fee, CustomerService 			
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
			when lod.Line_Object in ('403') and sd.store_id = '2013'
				then cast ('SV00015' as varchar) -- Dynamics Service Item: Web ECertificate
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292','296') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0591','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807' ) -- Added Additional Varsity Locations on 02/08/2024 per Joel Berger direction 
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( 
		lod.Line_Object in (200,203,296)
		and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
),

TenderExchange as (

select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as OriginalPrice
		--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
		,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as Price,
	-1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, 'SV00014' as ItemId -- Hard Coded Per Joel Berger on Jan 11 2023
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where 1=1
and (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0591','0605','0610','0615','0619','0620','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807' ) -- Added Additional Varsity Locations on 02/08/2024 per Joel Berger direction 
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

) 

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te

order by 12, 
2, 
3



```

#### User::SqlStringSalesDetailStageSourceFeeHandlingV9

**Expression:**

```sql
"

with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



),

RegSales as (

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
			--else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when tdf.reference_no in ('098088','480200','498033','498088') -- Known Bag fees in SubClass Code R-B-D-57-01-01 and Exist in Current FDD - Added 2/20/2024
			 then cast ('SV'+tdf.reference_no as varchar (50)) 
			when lod.Line_Object in ('292') -- Merchandise Contribution aka Donation				
				then cast (isnull(dfm.DynamicsItemId,'SV091450') as varchar (50)) -- 2/5/2024: using Donation Service Item if no lookup found			
			when lod.Line_Object in ('204','205','296') -- Miscellaneous Fee, NSF Fee, CustomerService 			
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
			when lod.Line_Object in ('403') and sd.store_id = '2013'
				then cast ('SV00015' as varchar) -- Dynamics Service Item: Web ECertificate
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292','296') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','0630','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807','437','807','808','809','810','2086','558','811','812','813','0559','0560','0561','0562','0563','0564','0566','0567','0568','0569','0571','0572','0573','2085','2087','570','574','575','576','2088','477','0816','0817','0578','0576','0577','0579','0580','0581','0582','0583','0584','0585','0586','0587','0588','0589','0590','0591','2089','2090','2801') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( 
		lod.Line_Object in (200,203,296)
		and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+ (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
),

TenderExchange as (

select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as OriginalPrice
		--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
		,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as Price,
	-1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, 'SV00014' as ItemId -- Hard Coded Per Joel Berger on Jan 11 2023
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where 1=1
and (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','0630','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','0584','0585','0591','800','801','802','803','804','805','806','807','437','807','808','809','810','2086','558','811','812','813','0559','0560','0561','0562','0563','0564','0566','0567','0568','0569','0571','0572','0573','2085','2087','570','574','575','576','2088','477','0816','0817','0578','0576','0577','0579','0580','0581','0582','0583','0584','0585','0586','0587','0588','0589','0590','0591','2089','2090','2801') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+ (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

) 

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te

order by 12, 
2, 
3


"
```

**Evaluated value:**

```sql


with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



),

RegSales as (

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
			--else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when tdf.reference_no in ('098088','480200','498033','498088') -- Known Bag fees in SubClass Code R-B-D-57-01-01 and Exist in Current FDD - Added 2/20/2024
			 then cast ('SV'+tdf.reference_no as varchar (50)) 
			when lod.Line_Object in ('292') -- Merchandise Contribution aka Donation				
				then cast (isnull(dfm.DynamicsItemId,'SV091450') as varchar (50)) -- 2/5/2024: using Donation Service Item if no lookup found			
			when lod.Line_Object in ('204','205','296') -- Miscellaneous Fee, NSF Fee, CustomerService 			
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
			when lod.Line_Object in ('403') and sd.store_id = '2013'
				then cast ('SV00015' as varchar) -- Dynamics Service Item: Web ECertificate
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292','296') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','0630','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','800','801','802','803','804','805','806','807','437','807','808','809','810','2086','558','811','812','813','0559','0560','0561','0562','0563','0564','0566','0567','0568','0569','0571','0572','0573','2085','2087','570','574','575','576','2088','477','0816','0817','0578','0576','0577','0579','0580','0581','0582','0583','0584','0585','0586','0587','0588','0589','0590','0591','2089','2090','2801') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( 
		lod.Line_Object in (200,203,296)
		and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
),

TenderExchange as (

select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as OriginalPrice
		--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
		,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as Price,
	-1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, 'SV00014' as ItemId -- Hard Coded Per Joel Berger on Jan 11 2023
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where 1=1
and (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('0001','0002','0102','0105','0167','0183','0212','0221','0278','0286','0415','0521','0534','0119','0130','0174','0177','0204','0205','0215','0358','0404','0439','0540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082','0003','0004','0012','0016','0020','0021','0030','0037','0038','0043','0053','0056','0062','0063','0065','0068','0076','0084','0085','0087','0093','0098','0101','0103','0109','0113','0122','0126','0129','0131','0133','0134','0137','0138','0139','0144','0149','0156','0157','0166','0185','0186','0190','0194','0195','0196','0202','0203','0208','0214','0224','0239','0251','0267','0277','0281','0313','0316','0321','0423','0425','0448','0535','0536','0603','0614','0011','0031','0041','0046','0049','0066','0071','0072','0082','0099','0110','0117','0118','0128','0158','0161','0169','0175','0181','0191','0192','0193','0198','0207','0210','0222','0226','0236','0237','0247','0248','0254','0256','0257','0260','0268','0275','0297','0298','0299','0307','0308','0309','0315','0318','0326','0328','0330','0331','0345','0350','0385','0393','0397','0398','0421','0424','0446','0454','0457','0520','0542','0607','0613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078','0006','0010','0014','0018','0022','0029','0032','0036','0040','0045','0051','0055','0059','0078','0083','0086','0089','0090','0091','0092','0094','0096','0106','0108','0116','0123','0125','0132','0141','0145','0148','0152','0160','0164','0168','0171','0178','0199','0201','0206','0213','0220','0223','0234','0244','0271','0273','0287','0290','0291','0300','0310','0317','0319','0324','0329','0335','0337','0349','0422','0447','0449','0453','0458','0468','0537','0541','0543','0549','0551','0621','0009','0015','0019','0023','0026','0034','0039','0042','0047','0054','0057','0064','0075','0077','0079','0080','0088','0100','0104','0107','0115','0120','0135','0142','0147','0151','0153','0154','0159','0162','0163','0170','0173','0176','0200','0216','0218','0230','0231','0233','0238','0243','0245','0249','0253','0258','0261','0264','0265','0274','0294','0295','0302','0312','0327','0332','0334','0354','0355','0356','0361','0363','0364','0366','0367','0368','0370','0371','0382','0384','0385','0402','0405','0407','0411','0414','0416','0417','0440','0441','0451','0452','0459','0476','0525','0526','0527','0528','0529','0530','0532','0533','0538','0539','0550','0552','0553','0554','0605','0610','0615','0619','0620','0630','2019','2079','2080','2013','2083','2084','0547','0478','0546','0548','0556','0555','0557','0584','0585','0591','800','801','802','803','804','805','806','807','437','807','808','809','810','2086','558','811','812','813','0559','0560','0561','0562','0563','0564','0566','0567','0568','0569','0571','0572','0573','2085','2087','570','574','575','576','2088','477','0816','0817','0578','0576','0577','0579','0580','0581','0582','0583','0584','0585','0586','0587','0588','0589','0590','0591','2089','2090','2801') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

) 

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te

order by 12, 
2, 
3



```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
4/24/2026
```

#### User::StartDateAsDATE

**Expression:**

```sql
(DT_WSTR, 4) datepart("year", @[User::StartDate])  + "-" +
right("0"+ (DT_WSTR, 2) datepart("mm", @[User::StartDate]),2)  + "-" +
right("0" +(DT_WSTR, 2) datepart("dd",  @[User::StartDate]),2)
```

**Evaluated value:**

```sql
2026-04-24
```

#### User::v7

**Expression:**

```sql
"
With RegSales as  (
select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete
	,null as CustAccount
	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.transaction_id as RetailReceiptId
	,tdf.cashier_id as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
	,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
	,cast(dd.actual_date  as date) TransDate 
	, 'Sales' as RetailTransactionType
	, null as BABIntRetailProcessed	
	, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
	, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
	, tdf.transaction_no as TransactionNumber
from TransactionDetailFactsDynamics TDF (nolock) 
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock) on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on tdf.date_key=dd.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header due to ES Orders and how that is handled in detail lines 
	left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tdf.transaction_id
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('2006') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,203,204,292,799,701,710,711,714)

	
		) -- Misc Fee and Donation lines 

	or ( 
		lod.Line_Object in (200,203,296)
			and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines

	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+
 (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 

	cast (tdf.register_num  as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tdf.transaction_id
	,tdf.cashier_id
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	,isnull(ds.SumTransDiscounts,0.00)
	,isnull(ds.SumTransHeaderDiscounts,0.00)
	, tdf.transaction_no
), 

--union 
TenderExchange as (


select cast(tef.register_no as varchar) as RetailTerminalId_Incomplete
,null as CustAccount
,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
, case when sd.country = 'IE' then 'UK'
	else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
,tef.transaction_id as RetailReceiptId
,tef.cashier_no as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
,cast(dd.actual_date  as date) TransDate 
, 'Sales' as RetailTransactionType
, null as BABIntRetailProcessed	
--, 0.00 as DiscAmount
--, 0.00 as TotalDiscAmount
, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
, tef.transaction_no as TransactionNumber
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tef.transaction_id
where 1=1
and (tef.line_object in ('633','404')and line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13')  -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('2006') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+
 (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 
	cast (tef.register_no as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tef.transaction_id
	,tef.cashier_no
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	, tef.transaction_no 
	, isnull(ds.SumTransDiscounts,0.00) 
	, isnull(ds.SumTransHeaderDiscounts,0.00)
)

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te
order by 9, 3, 5"
```

**Evaluated value:**

```sql

With RegSales as  (
select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete
	,null as CustAccount
	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.transaction_id as RetailReceiptId
	,tdf.cashier_id as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
	,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
	,cast(dd.actual_date  as date) TransDate 
	, 'Sales' as RetailTransactionType
	, null as BABIntRetailProcessed	
	, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
	, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
	, tdf.transaction_no as TransactionNumber
from TransactionDetailFactsDynamics TDF (nolock) 
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock) on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on tdf.date_key=dd.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header due to ES Orders and how that is handled in detail lines 
	left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tdf.transaction_id
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('2006') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,203,204,292,799,701,710,711,714)

	
		) -- Misc Fee and Donation lines 

	or ( 
		lod.Line_Object in (200,203,296)
			and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines

	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 

	cast (tdf.register_num  as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tdf.transaction_id
	,tdf.cashier_id
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	,isnull(ds.SumTransDiscounts,0.00)
	,isnull(ds.SumTransHeaderDiscounts,0.00)
	, tdf.transaction_no
), 

--union 
TenderExchange as (


select cast(tef.register_no as varchar) as RetailTerminalId_Incomplete
,null as CustAccount
,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
, case when sd.country = 'IE' then 'UK'
	else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
,tef.transaction_id as RetailReceiptId
,tef.cashier_no as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
,cast(dd.actual_date  as date) TransDate 
, 'Sales' as RetailTransactionType
, null as BABIntRetailProcessed	
--, 0.00 as DiscAmount
--, 0.00 as TotalDiscAmount
, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
, tef.transaction_no as TransactionNumber
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tef.transaction_id
where 1=1
and (tef.line_object in ('633','404')and line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13')  -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('2006') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 
	cast (tef.register_no as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tef.transaction_id
	,tef.cashier_no
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	, tef.transaction_no 
	, isnull(ds.SumTransDiscounts,0.00) 
	, isnull(ds.SumTransHeaderDiscounts,0.00)
)

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te
order by 9, 3, 5
```

#### User::v9

**Expression:**

```sql
"

with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



),

RegSales as (

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
			--else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when tdf.reference_no in ('098088','480200','498033','498088') -- Known Bag fees in SubClass Code R-B-D-57-01-01 and Exist in Current FDD - Added 2/20/2024
			 then cast ('SV'+tdf.reference_no as varchar (50)) 
			when lod.Line_Object in ('292') -- Merchandise Contribution aka Donation				
				then cast (isnull(dfm.DynamicsItemId,'SV091450') as varchar (50)) -- 2/5/2024: using Donation Service Item if no lookup found			
			when lod.Line_Object in ('204','205','296') -- Miscellaneous Fee, NSF Fee, CustomerService 			
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
			when lod.Line_Object in ('403') and sd.store_id = '2013'
				then cast ('SV00015' as varchar) -- Dynamics Service Item: Web ECertificate
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292','296') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('2006')-- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( 
		lod.Line_Object in (200,203,296)
		and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+ (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
),

TenderExchange as (

select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as OriginalPrice
		--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
		,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as Price,
	-1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, 'SV00014' as ItemId -- Hard Coded Per Joel Berger on Jan 11 2023
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where 1=1
and (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('2006') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and DATEDIFF(dd,dd.actual_date,getdate()) <= "+ (DT_WSTR, 4) @[$Package::DaysToGoBack]+"
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

) 

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te

order by 12, 
2, 
3


"
```

**Evaluated value:**

```sql


with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



),

RegSales as (

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
			--else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when tdf.reference_no in ('098088','480200','498033','498088') -- Known Bag fees in SubClass Code R-B-D-57-01-01 and Exist in Current FDD - Added 2/20/2024
			 then cast ('SV'+tdf.reference_no as varchar (50)) 
			when lod.Line_Object in ('292') -- Merchandise Contribution aka Donation				
				then cast (isnull(dfm.DynamicsItemId,'SV091450') as varchar (50)) -- 2/5/2024: using Donation Service Item if no lookup found			
			when lod.Line_Object in ('204','205','296') -- Miscellaneous Fee, NSF Fee, CustomerService 			
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
			when lod.Line_Object in ('403') and sd.store_id = '2013'
				then cast ('SV00015' as varchar) -- Dynamics Service Item: Web ECertificate
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292','296') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where 1=1
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('2006')-- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( 
		lod.Line_Object in (200,203,296)
		and 
		lad.Line_Action not in ('91','92','93','95','96','97','147','160') -- Known Enterprise Selling aka Endless Aisle Line Actions -- Added 02-05-2024

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
),

TenderExchange as (

select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as OriginalPrice
		--, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
		,  case when tef.line_action in  (2,12,15,26) -- Return Lines
		then sum(tef.gross_line_amount)*-1
		else sum(tef.gross_line_amount) end 
		as Price,
	-1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, 'SV00014' as ItemId -- Hard Coded Per Joel Berger on Jan 11 2023
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where 1=1
and (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13') -- Removed 2013 from exclusion on 9/22/2023
and sd.store_id in ('2006') -- Added Upcoming Stores 2089 to 2090 on Aug 14 2025
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

) 

-- Needed to not include any tender exchanges that may appear as returns in sales audit 
select *
from RegSales rs
where rs.RetailReceiptId not in (select distinct RetailReceiptId from TenderExchange) 
union 
select *
from TenderExchange te

order by 12, 
2, 
3



```

## Execute SQL Tasks

### Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont -  Dynamics Import Validations - Daily\Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
IF OBJECT_ID(N'tempdb..##UpdateSummary') IS NOT NULL DROP TABLE ##UpdateSummary;

with BaseSource as (
select r.TransactionNumber as RetailTransactionId, 
r.dataareaid as Entity,
r.RreceiptId as RetailReceiptId
from tmpDynamicsRetailTransaction r
group by r.TransactionNumber, r.dataAreaId, r.RreceiptId

) , 

StagingSource as (


select i.RetailTransactionId as RetailTransactionId_Staging, 
i.dataAreaId as Entity_Staging, 
i.RetailReceiptId as RetailReceiptId_Staging
from tmpDynamicsIntRetailTransaction i 
group by i.RetailTransactionId, i.dataAreaId, i.RetailReceiptId
) , 


Summary1 as (

Select b.*, 
s.*
from BaseSource b
full outer join StagingSource  s on b.RetailTransactionId=s.RetailTransactionId_Staging 
) , 

SummaryFinal as (


select  
case 
	when s.RetailTransactionId is null 
		then s.RetailTransactionId_Staging 
	when s.RetailTransactionId is not null 
		then s.RetailTransactionId
	else null end as RetailTransactionId,	
case
	when s.RetailReceiptId is null 
		then RetailReceiptId_Staging
	when s.RetailReceiptId is not null 
		then s.RetailReceiptId
	else null 
	end as RetailReceiptId, 
	case when s.RetailTransactionId is null 
		then 'IsInDynamicsStaging'
	when s.RetailTransactionId 
		is not null then 'IsInDynamics'
	else null end as StatusFlag
from Summary1 s
) ,

UpdateSummary as (

select distinct hf.RetailTransactionId, 
hf.Entity, 
sf.StatusFlag

from dw.dbo.DynamicsTransactionHeaderFacts hf
join SummaryFinal SF on SF.RetailTransactionId = hf.RetailTransactionId
where hf.BatchID is not null -- Indicates it's been exported via the Package API SSIS
--and hf.IsCurrent = 1 -- Indicates is the current transation sequence -- Removed Condition on 1/31/2023
and hf.IsInDynamics is null 

) 


select *
into ##UpdateSummary
from UpdateSummary
order by 3, 2, 1

update HF 
set hf.IsInDynamics = 1 
from dw.dbo.DynamicsTransactionHeaderFacts HF 
	join ##UpdateSummary s on s.RetailTransactionId=hf.RetailTransactionId
				and s.Entity=hf.Entity
				and s.StatusFlag = 'IsInDynamics'


update HF 
set hf.IsInDynamicsStaging = 1 
from dw.dbo.DynamicsTransactionHeaderFacts HF 
	join ##UpdateSummary s on s.RetailTransactionId=hf.RetailTransactionId
				and s.Entity=hf.Entity
				and s.StatusFlag = 'IsInDynamicsStaging'






```

### Execute SQL Task - Truncate Staging

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont -  Dynamics Import Validations - Daily\Execute SQL Task - Truncate Staging`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
truncate table dbo.tmpDynamicsRetailTransaction
truncate table dbo.tmpDynamicsIntRetailTransaction

```

### Execute SQL Task - spMergeDynamicsDiscountFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Initial Transaction Insert Merges\Execute SQL Task - spMergeDynamicsDiscountFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsDiscountFacts] 
```

### Execute SQL Task - spMergeDynamicsPaymentFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Initial Transaction Insert Merges\Execute SQL Task - spMergeDynamicsPaymentFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsPaymentFacts] 
```

### Execute SQL Task - spMergeDynamicsSalesDetailFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Initial Transaction Insert Merges\Execute SQL Task - spMergeDynamicsSalesDetailFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsSalesDetailFacts] 
```

### Execute SQL Task - spMergeDynamicsTaxFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Initial Transaction Insert Merges\Execute SQL Task - spMergeDynamicsTaxFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsTaxFacts] 
```

### Execute SQL Task - spMergeDynamicsTransactionHeaderFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Initial Transaction Insert Merges\Execute SQL Task - spMergeDynamicsTransactionHeaderFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsTransactionHeaderFacts] 
```

### Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont -  Dynamics Import Validations - Weekly\Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
IF OBJECT_ID(N'tempdb..##UpdateSummary') IS NOT NULL DROP TABLE ##UpdateSummary;

with BaseSource as (
select r.TransactionNumber as RetailTransactionId, 
r.dataareaid as Entity,
r.RreceiptId as RetailReceiptId
from tmpDynamicsRetailTransaction r
group by r.TransactionNumber, r.dataAreaId, r.RreceiptId

) , 

StagingSource as (


select i.RetailTransactionId as RetailTransactionId_Staging, 
i.dataAreaId as Entity_Staging, 
i.RetailReceiptId as RetailReceiptId_Staging
from tmpDynamicsIntRetailTransaction i 
group by i.RetailTransactionId, i.dataAreaId, i.RetailReceiptId
) , 


Summary1 as (

Select b.*, 
s.*
from BaseSource b
full outer join StagingSource  s on b.RetailTransactionId=s.RetailTransactionId_Staging 
) , 

SummaryFinal as (


select  
case 
 when s.RetailTransactionId is null 
  then s.RetailTransactionId_Staging 
 when s.RetailTransactionId is not null 
  then s.RetailTransactionId
 else null end as RetailTransactionId, 
case
 when s.RetailReceiptId is null 
  then RetailReceiptId_Staging
 when s.RetailReceiptId is not null 
  then s.RetailReceiptId
 else null 
 end as RetailReceiptId, 
 case when s.RetailTransactionId is null 
  then 'IsInDynamicsStaging'
 when s.RetailTransactionId 
  is not null then 'IsInDynamics'
 else null end as StatusFlag
from Summary1 s
) ,

UpdateSummary as (

select distinct hf.RetailTransactionId, 
hf.Entity, 
sf.StatusFlag

from dw.dbo.DynamicsTransactionHeaderFacts hf
join SummaryFinal SF on SF.RetailReceiptId = hf.RetailReceiptId
    and SF.RetailTransactionId = hf.RetailTransactionId
where hf.BatchID is not null -- Indicates it's been exported via the Package API SSIS
and hf.IsCurrent = 1 -- Indicates is the current transation sequence 
and hf.IsInDynamics is null 

) 


select *
into ##UpdateSummary
from UpdateSummary
order by 3, 2, 1

update HF 
set hf.IsInDynamics = 1 
from dw.dbo.DynamicsTransactionHeaderFacts HF 
 join ##UpdateSummary s on s.RetailTransactionId=hf.RetailTransactionId
    and s.Entity=hf.Entity
    and s.StatusFlag = 'IsInDynamics'


update HF 
set hf.IsInDynamicsStaging = 1 
from dw.dbo.DynamicsTransactionHeaderFacts HF 
 join ##UpdateSummary s on s.RetailTransactionId=hf.RetailTransactionId
    and s.Entity=hf.Entity
    and s.StatusFlag = 'IsInDynamicsStaging'






```

### Execute SQL Task - Truncate Staging

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont -  Dynamics Import Validations - Weekly\Execute SQL Task - Truncate Staging`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
truncate table dbo.tmpDynamicsRetailTransaction
truncate table dbo.tmpDynamicsIntRetailTransaction

```

### Execute SQL Task - Delete Transactions From Fact Tables

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables\Execute SQL Task - Delete Transactions From Fact Tables`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql


IF OBJECT_ID(N'tempdb..##DeleteFactRecords') IS NOT NULL DROP TABLE ##DeleteFactRecords


-- Create MaxID Temp Table 
IF OBJECT_ID(N'tempdb..##MaxID1') IS NOT NULL DROP TABLE ##MaxID1 
select hf.RetailReceiptId, 
max (hf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTransactionHeaderFacts' as TableName
into ##MaxID1 
from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
group by hf.RetailReceiptId 
union 
select Sdf.RetailReceiptId, 
max (Sdf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsSalesDetailFacts' as TableName
from dw.[dbo].[DynamicsSalesDetailFacts] SDF (nolock) 
group by Sdf.RetailReceiptId 
union
select df.RetailReceiptId, 
max (df.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsDiscountFacts' as TableName
FROM dw.dbo.[DynamicsDiscountFacts] df
group by df.RetailReceiptId
union 
select tf.RetailReceiptId, 
max (tf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTaxFacts' as TableName
FROM dw.dbo.[DynamicsTaxFacts] TF
group by tf.RetailReceiptId
union
select pf.RetailReceiptId, 
max (pf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsPaymentFacts' as TableName
FROM dw.dbo.[DynamicsPaymentFacts] PF
group by pf.RetailReceiptId

;

with UpdateTransactions as (

Select m.TableName, 
	hf.DynamicsTransactionHeaderFactsId as RecordId , 
	hf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	

from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=hf.RetailTransactionId
		and m.TableName = 'DynamicsTransactionHeaderFacts'
	join [DynamicsTransactionHeaderFactsStage] HFS on hfs.RetailReceiptId=hf.RetailReceiptId
where	HF.RetailTerminalId	<>	HFS.RetailTerminalId	or
		HF.InventLocationId	<>	HFS.InventLocationId	or
		HF.RetailStaffId	<>	HFS.RetailStaffId	or
		HF.BABIntRetailOperatingUnitNumber	<>	HFS.BABIntRetailOperatingUnitNumber	or
		HF.TransDate	<>	HFS.TransDate	or
		HF.RetailTransactionType	<>	HFS.RetailTransactionType
group by m.TableName, hf.DynamicsTransactionHeaderFactsId, hf.RetailReceiptId
	union 
Select m.TableName, 
	sdf.DynamicsSalesDetailFactsId as RecordId , 
	sdf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsSalesDetailFacts]  SDF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=sdf.RetailTransactionId
		and m.TableName = 'DynamicsSalesDetailFacts'
	--join [DynamicsSalesDetailFactsStage] SDS on SDS.RetailReceiptId=sdf.RetailReceiptId -- Replaced on 12/13/2022
	join [DynamicsSalesDetailDiscountsFactsStage] SDS (nolock) on SDS.RetailReceiptId=sdf.RetailReceiptId
		and sds.LineNum=sdf.LineNum
where 	
	SDF.InventLocationId	<>	SDS.InventLocationId	or
	SDF.OriginalPrice	<>	SDS.OriginalPrice	or
	SDF.Price	<>	SDS.Price	or
	SDF.Qty	<>	SDS.Qty	or	
	SDF.BABIntRetailOperatingUnitNumber	<>	SDS.BABIntRetailOperatingUnitNumber	or
	SDF.RetailTerminalId	<>	SDS.RetailTerminalId	or
	SDF.TransDate	<>	SDS.TransDate	or
	SDF.ItemId	<>	SDS.ItemId	or
	SDF.LineDscAmount	<>	SDS.LineDscAmount	or
	SDF.DiscAmount	<>	SDS.DiscAmount
group by m.TableName, sdf.DynamicsSalesDetailFactsId, sdf.RetailReceiptId
	union 
Select m.TableName, 
	df.DynamicsDiscountFactsId as RecordId , 
	df.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsDiscountFacts]  DF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=df.RetailTransactionId
		and m.TableName = 'DynamicsDiscountFacts'
	join [DynamicsDiscountFactsStage] DFS on df.RetailReceiptId=dfs.RetailReceiptId
		and df.SaleLineNum=dfs.SaleLineNum
		--and df.LineNum=dfs.LineNum -- Replaced 12/13/2022 with join below 
		and df.BabRetailDiscountTransUniqueLineNum=dfs.DiscountTransUniqueLineNum		
where 
	DF.Amount	<>	DFS.Amount	or
	DF.DiscountCost	<>	DFS.DiscountCost	or
	DF.DiscountOriginType	<>	DFS.DiscountOriginType	or
	DF.RetailTerminalId	<>	DFS.RetailTerminalId	or	
	DF.BABIntRetailOperatingUnitNumber	<>	DFS.BABIntRetailOperatingUnitNumber	or	
	--DF.[Percentage]	<>	DFS.[Percentage]	or  -- Omitted 12/13/2022 we no longer populate this field 
	DF.RetailStoreId	<>	DFS.RetailStoreId	or	
	DF.CustomerDiscountType	<>	DFS.CustomerDiscountType
group by m.TableName, df.DynamicsDiscountFactsId, df.RetailReceiptId
	union 
Select m.TableName, 
	tf.DynamicsTaxFactsId as RecordId , 
	tf.RetailReceiptId,
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsTaxFacts] TF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=tf.RetailTransactionId
		and m.TableName = 'DynamicsTaxFacts'
	join [DynamicsTaxFactsStage] TFS on tf.RetailReceiptId=tfs.RetailReceiptId
		and tf.LineNum=tfs.LineNum
where 
	TF.Amount	<>	TFS.Amount	or
	TF.RetailTerminalId	<>	TFS.RetailTerminalId	or
	TF.BABIntRetailOperatingUnitNumber	<>	TFS.BABIntRetailOperatingUnitNumber	or
	tf.TaxCode <> tfs.TaxCode
group by m.TableName, tf.DynamicsTaxFactsId, tf.RetailReceiptId
	union 

Select m.TableName, 
	pf.DynamicsPaymentFactsId as RecordId , 
	pf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsPaymentFacts] PF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=Pf.RetailTransactionId
		and m.TableName = 'DynamicsPaymentFacts'
	join [DynamicsPaymentFactsStage] pFS on Pf.RetailReceiptId=Pfs.RetailReceiptId
		and pf.LineNum=pfs.LineNum
where 	
	PF.AmountCur	<>	PFS.AmountCur	or
	PF.AmountMst	<>	PFS.AmountMst	or
	PF.RetailAmountTendered	<>	PFS.RetailAmountTendered	or	
	PF.RetailTenderTypeId	<>	PFS.RetailTenderTypeId	or
	PF.RetailTerminalId	<>	PFS.RetailTerminalId	or
	PF.BABIntRetailOperatingUnitNumber	<>	PFS.BABIntRetailOperatingUnitNumber	or
	PF.TransDate	<>	PFS.TransDate	or	
	PF.ChangeLine	<>	PFS.ChangeLine	or	
	PF.CurrencyCode	<>	PFS.CurrencyCode	

group by m.TableName, pf.DynamicsPaymentFactsId, pf.RetailReceiptId	
) , 

UpdatedSummary  as (

select distinct RetailReceiptId
from UpdateTransactions

) , 

SummaryFinal as (


select 
	m.TableName, 
	hf.DynamicsTransactionHeaderFactsId as RecordId , 
	hf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
--into ##tc 
from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=hf.RetailTransactionId
		and m.TableName = 'DynamicsTransactionHeaderFacts'
	join Updatedsummary u on u.RetailReceiptId=hf.RetailReceiptId
	union 
select 
	m.TableName, 
	sf.DynamicsSalesDetailFactsId as RecordId , 
	sf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsSalesDetailFacts]  SF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=sf.RetailTransactionId
		and m.TableName = 'DynamicsSalesDetailFacts'
	join Updatedsummary u on u.RetailReceiptId=sf.RetailReceiptId
	union
Select 
	m.TableName, 
	df.DynamicsDiscountFactsId as RecordId , 
	df.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsDiscountFacts]  DF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=df.RetailTransactionId
		and m.TableName = 'DynamicsDiscountFacts'
	join Updatedsummary u on u.RetailReceiptId=df.RetailReceiptId
	union 
Select
	m.TableName, 
	tf.DynamicsTaxFactsId as RecordId , 
	tf.RetailReceiptId,
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsTaxFacts] TF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=tf.RetailTransactionId
		and m.TableName = 'DynamicsTaxFacts'
	join Updatedsummary u on u.RetailReceiptId=tf.RetailReceiptId
	union 
Select 
	m.TableName, 
	pf.DynamicsPaymentFactsId as RecordId , 
	pf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsPaymentFacts] PF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=Pf.RetailTransactionId
		and m.TableName = 'DynamicsPaymentFacts'
	join Updatedsummary u on u.RetailReceiptId=pf.RetailReceiptId



	), 

ExistsInDynamicsStaging as (
	select RetailTransactionId, RetailReceiptId, Entity 
	from dw.dbo.DynamicsTransactionHeaderFacts
	where IsInDynamics is null -- Does NOT Exist in Dynamics Base Tables
	and IsInDynamicsStaging = 1 -- Does Exist in Dynamics Staging Tables
	and IsCurrent = 1 -- May Not need this but leaving for now 
	and DATEDIFF(dd,TransDate,Getdate()) <= 60
	group by RetailTransactionId, RetailReceiptId, Entity 


)


select distinct sf.RetailReceiptId
into ##DeleteFactRecords
from SummaryFinal sf 
join ExistsInDynamicsStaging E on sf.RetailReceiptId=e.RetailReceiptId 

-- Perform Deletes on Fact Records 
delete from dw.[dbo].[DynamicsTransactionHeaderFacts] 
where RetailReceiptId in (select distinct RetailReceiptId from ##DeleteFactRecords)

delete from dw.[dbo].[DynamicsSalesDetailFacts]
where RetailReceiptId in (select distinct RetailReceiptId from ##DeleteFactRecords)

delete from dw.[dbo].[DynamicsDiscountFacts]
where RetailReceiptId in (select distinct RetailReceiptId from ##DeleteFactRecords)

delete from dw.[dbo].[DynamicsTaxFacts]
where RetailReceiptId in (select distinct RetailReceiptId from ##DeleteFactRecords)

delete from dw.[dbo].[DynamicsPaymentFacts]
where RetailReceiptId in (select distinct RetailReceiptId from ##DeleteFactRecords)
	
```

### Execute SQL Task - spMergeDynamicsDiscountFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables\SeqCont - Execute Insert Merges\Execute SQL Task - spMergeDynamicsDiscountFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsDiscountFacts] 
```

### Execute SQL Task - spMergeDynamicsPaymentFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables\SeqCont - Execute Insert Merges\Execute SQL Task - spMergeDynamicsPaymentFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsPaymentFacts] 
```

### Execute SQL Task - spMergeDynamicsSalesDetailFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables\SeqCont - Execute Insert Merges\Execute SQL Task - spMergeDynamicsSalesDetailFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsSalesDetailFacts] 
```

### Execute SQL Task - spMergeDynamicsTaxFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables\SeqCont - Execute Insert Merges\Execute SQL Task - spMergeDynamicsTaxFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsTaxFacts] 
```

### Execute SQL Task - spMergeDynamicsTransactionHeaderFacts

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Excecute Transactions Update Merge - Transactions Stuck in Dynamics Staging Tables\SeqCont - Execute Insert Merges\Execute SQL Task - spMergeDynamicsTransactionHeaderFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec [dbo].[spMergeDynamicsTransactionHeaderFacts] 
```

### Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - New

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn\Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - New`  
**Connection:** dw (papamart/dw)  

```sql
use dw; 
-- Create MaxID Temp Table 
IF OBJECT_ID(N'tempdb..##MaxId2') IS NOT NULL DROP TABLE ##MaxId2
select hf.RetailReceiptId, 
max (hf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTransactionHeaderFacts' as TableName
into ##MaxId2 
from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
group by hf.RetailReceiptId 
union 
select Sdf.RetailReceiptId, 
max (Sdf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsSalesDetailFacts' as TableName
from dw.[dbo].[DynamicsSalesDetailFacts] SDF (nolock) 
group by Sdf.RetailReceiptId 
union
select df.RetailReceiptId, 
max (df.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsDiscountFacts' as TableName
FROM dw.dbo.[DynamicsDiscountFacts] df (nolock)
group by df.RetailReceiptId
union 
select tf.RetailReceiptId, 
max (tf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTaxFacts' as TableName
FROM dw.dbo.[DynamicsTaxFacts] TF (nolock)
group by tf.RetailReceiptId
union
select pf.RetailReceiptId, 
max (pf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsPaymentFacts' as TableName
FROM dw.dbo.[DynamicsPaymentFacts] PF (nolock)
group by pf.RetailReceiptId

;

IF OBJECT_ID(N'tempdb..#CurrentFiscalPeriod') IS NOT NULL 
DROP TABLE #CurrentFiscalPeriod
select 
cast (min(actual_date) as date)  as FirstDateOfCurrentPeriod, 
cast (max(actual_date) as date)  as LastDateOfCurrentPeriod 
into #CurrentFiscalPeriod
from date_dim dd (nolock) 
where dd.period_id  = (select period_id from date_dim  where actual_date = cast (getdate() as date)) 

IF OBJECT_ID(N'tempdb..#StoreLookup') IS NOT NULL 
DROP TABLE #StoreLookup
select WarehouseID as InventLocationId, 
LocationCode, 
	Entity, 
	case when Entity = '1100' then 'US'
	when Entity = '1700' then 'CA'
	when Entity = '2110' then 'UK'
	else null 
	end as Country
into #StoreLookup
from [stl-ssis-p-01].IntegrationStaging.[ERP].[vwWarehouseIDToLocationCode]
group by  WarehouseID, 
LocationCode, 
Entity 

IF OBJECT_ID(N'tempdb..#InventLocation') IS NOT NULL 
DROP TABLE #InventLocation
select 
	sl.LocationCode,
	sl.Country, 
	rs.WarehouseId as InventLocationID, 	
	rs.OperatingUnitNumber,
	rs.WarehouseLegalEntity as Entity	
into #InventLocation
from [stl-ssis-p-01].IntegrationStaging.[WMS].[RetailStore] RS 
join #StoreLookup SL on sl.Entity=rs.WarehouseLegalEntity and sl.InventLocationId=rs.warehouseid
where sl.Country is not null 

-- Added Jul 31 2025
-- Sometimes the Sales Audit Staff will mistakenly prearchive transactions before the end of the period
-- This could cause a false negate only flag 
IF OBJECT_ID(N'tempdb..#PreArchivedTransactions') IS NOT NULL 
DROP TABLE #PreArchivedTransactions
select distinct th.av_transaction_id as transaction_id
into #PreArchivedTransactions
from bedrockdb01.auditworks.dbo.av_transaction_header th
where 1=1
and th.transaction_void_flag = '0'
and th.transaction_date  >= (select FirstDateOfCurrentPeriod from #CurrentFiscalPeriod)


IF OBJECT_ID(N'tempdb..#DeletedTransactions') IS NOT NULL 
DROP TABLE #DeletedTransactions
--CurrentPeriod
select hf.RetailTransactionId
into #DeletedTransactions
from  DynamicsTransactionHeaderFacts hf (nolock) 
left join bedrockdb01.auditworks.dbo.transaction_header th on hf.RetailReceiptId=th.transaction_id 								
join #InventLocation IL on il.InventLocationID=hf.InventLocationId and il.Entity=hf.Entity
where  1=1 
and hf.IsCurrent = 1
and hf.BatchID is not null  -- Pushed to Dynamics Sales API
and
	( 
		th.transaction_id is null  -- Transaction Id No Longer Exists in Sales Audit 
			or 
		th.store_no <> il.LocationCode  -- Sales Audit Team Changed The Selling Store in Sales Audit  -- Added 4/24/2023
			or
		--th.transaction_void_flag = '1' -- Added 01/25/2024  -- Replaced on 1/29/2024
		th.transaction_void_flag <> '0' -- Added 01/29/2024 - We need to  closer match the dw load when only includes transactions to pull with th.transaction_void_flag = 0
	)
and hf.TransDate >= (select FirstDateOfCurrentPeriod from #CurrentFiscalPeriod)  -- Noticed Sales Audit has some very old transactions stuck in the current period tables, this is to ensure we only consider current fiscal period 
-- Added Jul 31 2025
and hf.RetailReceiptId not in (select distinct transaction_id from #PreArchivedTransactions)


-- Previous Period(s) -- Use for Ad Hoc Use 
/*
union 

select hf.RetailTransactionId
--into #DeletedTransactions
from  DynamicsTransactionHeaderFacts hf (nolock) 
left join bedrockdb01.auditworks.dbo.av_transaction_header th on hf.RetailReceiptId=th.av_transaction_id 								
join #InventLocation IL on il.InventLocationID=hf.InventLocationId and il.Entity=hf.Entity
where  1=1 
and hf.IsCurrent = 1
and hf.BatchID is not null  -- Pushed to Dynamics Sales API
and hf.TransDate between '11-26-2023' and '12-30-2023' -- Specify Targeted Date Range
and th.transaction_date between '11-26-2023' and '12-30-2023'  -- Specify Targeted Date Range
and
	( 
		th.av_transaction_id is null  -- Transaction Id No Longer Exists in Sales Audit 
			or 
		th.store_no <> il.LocationCode  -- Sales Audit Team Changed The Selling Store in Sales Audit  -- Added 4/24/2023
			or
		--th.transaction_void_flag = '1' -- Added 01/25/2024  -- Replaced on 1/29/2024
		th.transaction_void_flag <> '0' -- Added 01/29/2024 - We need to  closer match the dw load when only includes transactions to pull with th.transaction_void_flag = 0
	)
*/


IF OBJECT_ID(N'tempdb..#SummaryFinal') IS NOT NULL 
DROP TABLE #SummaryFinal
Select 
	m.TableName, 
	hf.DynamicsTransactionHeaderFactsId as RecordId , 
	hf.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
into #SummaryFinal
from #DeletedTransactions dt
join DynamicsTransactionHeaderFacts HF (nolock) on hf.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId
	and m.TableName = 'DynamicsTransactionHeaderFacts'
group by m.TableName, hf.DynamicsTransactionHeaderFactsId, hf.RetailReceiptId
	union 
Select m.TableName, 
	sdf.DynamicsSalesDetailFactsId as RecordId , 
	sdf.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 
from #DeletedTransactions dt
join DynamicsSalesDetailFacts SDF (nolock) 	on sdf.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId	
	and m.TableName = 'DynamicsSalesDetailFacts'
group by m.TableName, sdf.DynamicsSalesDetailFactsId, sdf.RetailReceiptId
	union 
Select m.TableName, 
	df.DynamicsDiscountFactsId as RecordId , 
	df.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from #DeletedTransactions dt
join DynamicsDiscountFacts  DF (nolock) on df.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId		
	and m.TableName = 'DynamicsDiscountFacts'
	union 
Select m.TableName, 
	tf.DynamicsTaxFactsId as RecordId , 
	tf.RetailReceiptId,
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from #DeletedTransactions dt
join DynamicsTaxFacts TF (nolock)  on tf.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId	
	and m.TableName = 'DynamicsTaxFacts'
group by m.TableName, tf.DynamicsTaxFactsId, tf.RetailReceiptId	
	union 
Select m.TableName, 
	pf.DynamicsPaymentFactsId as RecordId , 
	pf.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 
from #DeletedTransactions dt
join DynamicsPaymentFacts PF (nolock) on pf.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId	
	and m.TableName = 'DynamicsPaymentFacts'


-- Insert Into Negate Only Log
Insert Into dw.dbo.[DynamicsTransactionNegateOnlyLog] (TableName,RecordId,RetailReceiptId,UpdateProcessed,InsertDate,UpdateDate)
select sf.TableName, 
sf.RecordId, 
sf.RetailReceiptId, 
sf.UpdateProcessed, 
sf.InsertDate, 
sf.UpdateDate
from #SummaryFinal sf 



```

### Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - Old

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn\Execute SQL Task - Update Step 1 - Identify Records to Be Negated Only - Old`  
**Connection:** dw (papamart/dw)  

```sql
--set nocount on 

-- Create MaxID Temp Table 
IF OBJECT_ID(N'tempdb..##MaxId2') IS NOT NULL DROP TABLE ##MaxId2
select hf.RetailReceiptId, 
max (hf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTransactionHeaderFacts' as TableName
into ##MaxId2 
from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
group by hf.RetailReceiptId 
union 
select Sdf.RetailReceiptId, 
max (Sdf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsSalesDetailFacts' as TableName
from dw.[dbo].[DynamicsSalesDetailFacts] SDF (nolock) 
group by Sdf.RetailReceiptId 
union
select df.RetailReceiptId, 
max (df.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsDiscountFacts' as TableName
FROM dw.dbo.[DynamicsDiscountFacts] df
group by df.RetailReceiptId
union 
select tf.RetailReceiptId, 
max (tf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTaxFacts' as TableName
FROM dw.dbo.[DynamicsTaxFacts] TF
group by tf.RetailReceiptId
union
select pf.RetailReceiptId, 
max (pf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsPaymentFacts' as TableName
FROM dw.dbo.[DynamicsPaymentFacts] PF
group by pf.RetailReceiptId

;

With CurrentFiscalPeriod As  
(
	select 
	cast (min(actual_date) as date)  as FirstDateOfCurrentPeriod, 
	cast (max(actual_date) as date)  as LastDateOfCurrentPeriod 
	from date_dim dd (nolock) 
	where dd.period_id  = (select period_id from date_dim  where actual_date = cast (getdate() as date)) 
), 


StoreLookup as (
select WarehouseID as InventLocationId, 
LocationCode, 
	Entity, 
	case when Entity = '1100' then 'US'
	when Entity = '1700' then 'CA'
	when Entity = '2110' then 'UK'
	else null 
	end as Country
from [stl-ssis-p-01].IntegrationStaging.[ERP].[vwWarehouseIDToLocationCode]
group by  WarehouseID, 
LocationCode, 
Entity 


), -- Added 4/24/2023  --Sales Audit Team Changed The Selling Store in Sales Audit

InventLocation as (

select 
	sl.LocationCode,
	sl.Country, 
	rs.WarehouseId as InventLocationID, 	
	rs.OperatingUnitNumber,
	rs.WarehouseLegalEntity as Entity	
from [stl-ssis-p-01].IntegrationStaging.[WMS].[RetailStore] RS 
join StoreLookup SL on sl.Entity=rs.WarehouseLegalEntity and sl.InventLocationId=rs.warehouseid
where sl.Country is not null 
) , -- Added 4/24/2023  --Sales Audit Team Changed The Selling Store in Sales Audit



DeletedTransactions as (

select hf.RetailTransactionId
from  DynamicsTransactionHeaderFacts hf (nolock) 
left join bedrockdb01.auditworks.dbo.transaction_header th on hf.RetailReceiptId=th.transaction_id 								
join InventLocation IL on il.InventLocationID=hf.InventLocationId and il.Entity=hf.Entity
where  1=1 
and hf.IsCurrent = 1
and hf.BatchID is not null  -- Pushed to Dynamics Sales API
and
	( 
		th.transaction_id is null  -- Transaction Id No Longer Exists in Sales Audit 
		or 
		th.store_no <> il.LocationCode  -- Sales Audit Team Changed The Selling Store in Sales Audit  -- Added 4/24/2023
	)
and hf.TransDate >= (select FirstDateOfCurrentPeriod from CurrentFiscalPeriod)  -- Noticed Sales Audit has some very old transactions stuck in the current period tables, this is to ensure we only consider current fiscal period 
	), 


SummaryFinal as (

Select 
	m.TableName, 
	hf.DynamicsTransactionHeaderFactsId as RecordId , 
	hf.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from DeletedTransactions dt
join DynamicsTransactionHeaderFacts HF (nolock) on hf.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId
	and m.TableName = 'DynamicsTransactionHeaderFacts'
group by m.TableName, hf.DynamicsTransactionHeaderFactsId, hf.RetailReceiptId
	union 
Select m.TableName, 
	sdf.DynamicsSalesDetailFactsId as RecordId , 
	sdf.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 
from DeletedTransactions dt
join DynamicsSalesDetailFacts SDF (nolock) 	on sdf.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId	
	and m.TableName = 'DynamicsSalesDetailFacts'
group by m.TableName, sdf.DynamicsSalesDetailFactsId, sdf.RetailReceiptId
	union 
Select m.TableName, 
	df.DynamicsDiscountFactsId as RecordId , 
	df.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from DeletedTransactions dt
join DynamicsDiscountFacts  DF (nolock) on df.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId		
	and m.TableName = 'DynamicsDiscountFacts'
	union 
Select m.TableName, 
	tf.DynamicsTaxFactsId as RecordId , 
	tf.RetailReceiptId,
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from DeletedTransactions dt
join DynamicsTaxFacts TF (nolock)  on tf.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId	
	and m.TableName = 'DynamicsTaxFacts'
group by m.TableName, tf.DynamicsTaxFactsId, tf.RetailReceiptId	
	union 
Select m.TableName, 
	pf.DynamicsPaymentFactsId as RecordId , 
	pf.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 
from DeletedTransactions dt
join DynamicsPaymentFacts PF (nolock) on pf.RetailTransactionId=dt.RetailTransactionId
join ##MaxId2 m on m.MaxRetailTransactionId=dt.RetailTransactionId	
	and m.TableName = 'DynamicsPaymentFacts'
)

Insert Into dw.dbo.[DynamicsTransactionNegateOnlyLog] (TableName,RecordId,RetailReceiptId,UpdateProcessed,InsertDate,UpdateDate)
select sf.TableName, 
sf.RecordId, 
sf.RetailReceiptId, 
sf.UpdateProcessed, 
sf.InsertDate, 
sf.UpdateDate
from SummaryFinal sf 



```

### Execute SQL Task - Update Step 2 - Set IsCurrent to Null for Negate Only Trans

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn\Execute SQL Task - Update Step 2 - Set IsCurrent to Null for Negate Only Trans`  
**Connection:** dw (papamart/dw)  

```sql
-- Update existing records IsCurrent value to null 


-- Header
Update  H
Set H.IsCurrent= null
--select *
from dw.[dbo].[DynamicsTransactionHeaderFacts] H
	join dw.dbo.[DynamicsTransactionNegateOnlyLog] L on l.RecordId=H.DynamicsTransactionHeaderFactsId 
											and l.TableName = 'DynamicsTransactionHeaderFacts'
											and l.UpdateProcessed is null 
-- Sales Detail 

Update  SD
Set SD.IsCurrent= null
--select *
from dw.[dbo].[DynamicsSalesDetailFacts] SD
	join dw.dbo.[DynamicsTransactionNegateOnlyLog] L on l.RecordId=sd.DynamicsSalesDetailFactsId
											and l.TableName = 'DynamicsSalesDetailFacts'
											and l.UpdateProcessed is null 

-- Discounts 
Update  D
Set D.IsCurrent= null
--select *
from dw.[dbo].[DynamicsDiscountFacts] D
	join dw.dbo.[DynamicsTransactionNegateOnlyLog] L on l.RecordId=d.DynamicsDiscountFactsId
											and l.TableName = 'DynamicsDiscountFacts'
											and l.UpdateProcessed is null 

-- Payments
Update  P
Set P.IsCurrent= null
--select *
from dw.[dbo].[DynamicsPaymentFacts]  P
	join dw.dbo.[DynamicsTransactionNegateOnlyLog] L on l.RecordId=p.DynamicsPaymentFactsId
											and l.TableName = 'DynamicsPaymentFacts'
											and l.UpdateProcessed is null 

-- Tax 
Update  T
Set T.IsCurrent= null
--select *
from dw.[dbo].[DynamicsTaxFacts]   T
	join dw.dbo.[DynamicsTransactionNegateOnlyLog] L on l.RecordId=t.DynamicsTaxFactsId
											and l.TableName = 'DynamicsTaxFacts'
											and l.UpdateProcessed is null 




												

```

### Execute SQL Task - Update Step 3 - Insert Negating Transactions - Negate Only

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Execute  AW Transaction Deleted Merge - Negate Only to Dyn\Execute SQL Task - Update Step 3 - Insert Negating Transactions - Negate Only`  
**Connection:** dw (papamart/dw)  

```sql
-- Insert Negating Transactions 

-- Header 


INSERT INTO dw.[dbo].[DynamicsTransactionHeaderFacts] (RetailTerminalId,CustAccount,InventLocationId,RetailReceiptId,RetailStaffId,RetailTransactionId,BABIntRetailOperatingUnitNumber,TransDate,RetailTransactionType,BABIntRetailProcessed,Entity,DiscAmount,TotalDiscAmount,IsNegatedCurrent,InsertDate,TransactionNumber)
select 
h.RetailTerminalId, 
h.CustAccount, 
h.InventLocationId, 
h.RetailReceiptId, 
h.RetailStaffId, 
SUBSTRING(RetailTransactionId,0, CHARINDEX('_' ,h.RetailTransactionId)+1)+ cast(cast (right(h.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
h.BABIntRetailOperatingUnitNumber, 
h.TransDate, 
h.RetailTransactionType, 
h.BABIntRetailProcessed, 
h.Entity, 
h.DiscAmount*-1 as DiscAmount,
h.TotalDiscAmount*-1 as TotalDiscAmount ,
'1' as IsNegatedCurrent, 
getdate() as InsertDate, 
h.TransactionNumber

from dw.[dbo].[DynamicsTransactionHeaderFacts] H
	join dw.dbo.[DynamicsTransactionNegateOnlyLog]  L on l.RecordId=H.DynamicsTransactionHeaderFactsId 
											and l.TableName = 'DynamicsTransactionHeaderFacts'
											and l.UpdateProcessed is null 
											and H.BatchID is not null -- Added 1/23/2024 as we did for the Update DataFlow


-- Sales Detail 
INSERT INTO  dw.[dbo].[DynamicsSalesDetailFacts] (CustAccount,InventLocationId,LineNum,OriginalPrice,Price,Qty,RetailReceiptId,RetailTransactionId,BABIntRetailOperatingUnitNumber,RetailTerminalId,TransDate,ItemId,LineDscAmount,DiscAmount,GiftCardNumber,BABIntRetailProcessed,VatTaxAmount,CurrencyCode,Entity,PeriodicPercentageDiscount,TotalDiscAmount,TotalDiscPct,IsNegatedCurrent,InsertDate)
select 
sd.CustAccount, 
sd.InventLocationId, 
sd.LineNum, 
sd.OriginalPrice*-1 as OriginalPrice, 
sd.Price*-1 as Price, 
sd.Qty*-1 as Qty, 
sd.RetailReceiptId, 
SUBSTRING(sd.RetailTransactionId,0, CHARINDEX('_' ,sd.RetailTransactionId)+1)+ cast(cast (right(sd.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
sd.BABIntRetailOperatingUnitNumber, 
sd.RetailTerminalId, 
sd.TransDate, 
sd.ItemId, 
sd.LineDscAmount*-1 as LineDscAmount, -- Per Elizabeth W these values need to be negative on the negating transaction
sd.DiscAmount*-1 as DiscAmount, -- Per Elizabeth W these values need to be negative on the negating transaction
sd.GiftCardNumber, 
sd.BABIntRetailProcessed, 
sd.VatTaxAmount*-1 as VatTaxAmount, 
sd.CurrencyCode, 
sd.Entity, 
sd.PeriodicPercentageDiscount as PeriodicPercentageDiscount , --3/29/2023 -- Per Joel Berger this field can NEVER be negative 
sd.TotalDiscAmount*-1 as TotalDiscAmount, 
sd.TotalDiscPct as TotalDiscPct , --3/29/2023 -- Per Joel Berger this field can NEVER be negative 
'1' as IsNegatedCurrent, 
getdate() as InsertDate 

from dw.[dbo].[DynamicsSalesDetailFacts] SD
join dw.dbo.[DynamicsTransactionNegateOnlyLog]  L on l.RecordId=sd.DynamicsSalesDetailFactsId
											and l.TableName = 'DynamicsSalesDetailFacts'
											and l.UpdateProcessed is null 
											and sd.BatchID is not null -- Added 1/23/2024 as we did for the Update DataFlow



-- Discounts 
--INSERT INTO  dw.[dbo].[DynamicsDiscountFacts]  (Amount,DiscountCost,DiscountOriginType,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,LineNum,[Percentage],RetailStoreId,SaleLineNum,CustomerDiscountType,BABIntRetailProcessed,Entity,RetailReceiptId,IsNegatedCurrent,InsertDate)
INSERT INTO  dw.[dbo].[DynamicsDiscountFacts]  (Amount,DiscountCost,DiscountOriginType,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,LineNum,RetailStoreId,SaleLineNum,CustomerDiscountType,BABIntRetailProcessed,Entity,RetailReceiptId,BabRetailDiscountTransUniqueLineNum,ManualDiscountType,PeriodicDiscountOfferId,IsNegatedCurrent,InsertDate)
select 
d.Amount*-1 as Amount, 
d.DiscountCost*-1 as DiscountCost, 
d.DiscountOriginType, 
d.RetailTerminalId, 
SUBSTRING(d.RetailTransactionId,0, CHARINDEX('_' ,d.RetailTransactionId)+1)+ cast(cast (right(d.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
d.BABIntRetailOperatingUnitNumber, 
d.LineNum,  
--d.[Percentage], -- Remarked out on 12/13/2022 we no longer populate this field 
d.RetailStoreId, 
d.SaleLineNum, 
d.CustomerDiscountType, 
d.BABIntRetailProcessed, 
d.Entity, 
d.RetailReceiptId, 
d.BabRetailDiscountTransUniqueLineNum, -- Added 12/13/2022
d.ManualDiscountType, -- Added 12/13/2022
d.PeriodicDiscountOfferId, -- Added 12/13/2022
'1' as IsNegatedCurrent, 
getdate() as InsertDate 

from dw.[dbo].[DynamicsDiscountFacts] D
	join dw.dbo.[DynamicsTransactionNegateOnlyLog]  L on l.RecordId=d.DynamicsDiscountFactsId
											and l.TableName = 'DynamicsDiscountFacts'
											and l.UpdateProcessed is null 
											and D.BatchID is not null -- Added 1/23/2024 as we did for the Update DataFlow


-- Tax 

INSERT INTO  dw.[dbo].[DynamicsTaxFacts] (Amount,LineNum,TaxCode,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,BABIntRetailProcessed,Entity,RetailReceiptId,IsNegatedCurrent,InsertDate)
select
t.Amount*-1 as Amount, 
t.LineNum, 
t.TaxCode, 
t.RetailTerminalId, 
SUBSTRING(t.RetailTransactionId,0, CHARINDEX('_' ,t.RetailTransactionId)+1)+ cast(cast (right(t.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
t.BABIntRetailOperatingUnitNumber, 
t.BABIntRetailProcessed, 
t.Entity, 
t.RetailReceiptId, 
'1' as IsNegatedCurrent, 
getdate() as InsertDate 
from dw.[dbo].[DynamicsTaxFacts]   T
	join dw.dbo.[DynamicsTransactionNegateOnlyLog]  L on l.RecordId=t.DynamicsTaxFactsId
											and l.TableName = 'DynamicsTaxFacts'
											and l.UpdateProcessed is null 
											and T.BatchID is not null -- Added 1/23/2024 as we did for the Update DataFlow

-- Payments 
INSERT INTO  dw.[dbo].[DynamicsPaymentFacts]  (AmountCur,AmountMst,RetailAmountTendered,RetailCardTypeId,RetailReceiptId,LineNum,RetailTransactionId,RetailTenderTypeId,RetailTerminalId,BABIntRetailOperatingUnitNumber,TransDate,AccountNum,RetailCardNum,ChangeLine,PaymentAuthorization,CurrencyCode,BABIntRetailProcessed,Entity,IsNegatedCurrent,InsertDate)
select 
p.AmountCur*-1 as AmountCur, 
p.AmountMst*-1 as AmountMst, 
p.RetailAmountTendered*-1 as RetailAmountTendered, 
p.RetailCardTypeId, 
p.RetailReceiptId, 
p.LineNum, 
SUBSTRING(p.RetailTransactionId,0, CHARINDEX('_' ,p.RetailTransactionId)+1)+ cast(cast (right(p.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
p.RetailTenderTypeId, 
p.RetailTerminalId, 
p.BABIntRetailOperatingUnitNumber, 
p.TransDate, 
p.AccountNum, 
p.RetailCardNum, 
p.ChangeLine, 
p.PaymentAuthorization, 
p.CurrencyCode, 
p.BABIntRetailProcessed, 
p.Entity, 
'1' as IsNegatedCurrent, 
getdate () as InsertDate
from dw.[dbo].[DynamicsPaymentFacts]  P
	join dw.dbo.[DynamicsTransactionNegateOnlyLog]  L on l.RecordId=p.DynamicsPaymentFactsId
											and l.TableName = 'DynamicsPaymentFacts'
											and l.UpdateProcessed is null 
											and P.BatchID is not null -- Added 1/23/2024 as we did for the Update DataFlow




```

### Execute SQL Task -  Update Step 4 - Insert Updated Transaction Data

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base\Execute SQL Task -  Update Step 4 - Insert Updated Transaction Data`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
-- Create MaxID Temp Table 
IF OBJECT_ID(N'tempdb..##MaxID2') IS NOT NULL DROP TABLE ##MaxID2
select hf.RetailReceiptId, 
max (hf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTransactionHeaderFacts' as TableName
into ##MaxID2
from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
group by hf.RetailReceiptId 
union 
select Sdf.RetailReceiptId, 
max (Sdf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsSalesDetailFacts' as TableName
from dw.[dbo].[DynamicsSalesDetailFacts] SDF (nolock) 
group by Sdf.RetailReceiptId 
union
select df.RetailReceiptId, 
max (df.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsDiscountFacts' as TableName
FROM dw.dbo.[DynamicsDiscountFacts] df
group by df.RetailReceiptId
union 
select tf.RetailReceiptId, 
max (tf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTaxFacts' as TableName
FROM dw.dbo.[DynamicsTaxFacts] TF
group by tf.RetailReceiptId
union
select pf.RetailReceiptId, 
max (pf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsPaymentFacts' as TableName
FROM dw.dbo.[DynamicsPaymentFacts] PF
group by pf.RetailReceiptId

; 

-- Insert Updated Data into Fact Tables
-- Header Data 
insert into dw.[dbo].[DynamicsTransactionHeaderFacts] (RetailTerminalId,CustAccount,InventLocationId,RetailReceiptId,RetailStaffId,RetailTransactionId,BABIntRetailOperatingUnitNumber,TransDate,RetailTransactionType,BABIntRetailProcessed,Entity,DiscAmount,TotalDiscAmount,IsCurrent,InsertDate,TransactionNumber)
select hf.RetailTerminalId, 
hf.CustAccount, 
hf.InventLocationId, 
hf.RetailReceiptId, 
hf.RetailStaffId, 
SUBSTRING(m.MaxRetailTransactionId,0, CHARINDEX('_' ,m.MaxRetailTransactionId)+1)+ cast(cast (right(m.MaxRetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
hf.BABIntRetailOperatingUnitNumber, 
hf.TransDate, 
hf.RetailTransactionType, 
hf.BABIntRetailProcessed, 
hf.Entity,
hf.DiscAmount,
hf.TotalDiscAmount,
'1' as isCurrent, 
getdate() as InsertDate, 
hf.TransactionNumber
from DynamicsTransactionHeaderFactsStage HF 
join dw.dbo.DynamicsTransactionUpdateLog l on l.retailreceiptid=hf.RetailReceiptId
											and l.UpdateProcessed is null 
											and l.TableName = 'DynamicsTransactionHeaderFacts'
join ##MaxID2 m on m.RetailReceiptId=l.retailreceiptid
				and m.TableName = 'DynamicsTransactionHeaderFacts'

-- Sales Detail Data 
INSERT INTO dw.[dbo].[DynamicsSalesDetailFacts] (CustAccount,InventLocationId,LineNum,OriginalPrice,Price,Qty,RetailReceiptId,RetailTransactionId,BABIntRetailOperatingUnitNumber,RetailTerminalId,TransDate,ItemId,LineDscAmount,DiscAmount,GiftCardNumber,BABIntRetailProcessed,VatTaxAmount,CurrencyCode,Entity,PeriodicPercentageDiscount,TotalDiscAmount,TotalDiscPct,IsCurrent,InsertDate)
select 
sd.CustAccount, 
sd.InventLocationId, 
sd.LineNum, 
sd.OriginalPrice as OriginalPrice, 
sd.Price as Price, 
sd.Qty as Qty, 
sd.RetailReceiptId, 
SUBSTRING(m.MaxRetailTransactionId,0, CHARINDEX('_' ,m.MaxRetailTransactionId)+1)+ cast(cast (right(m.MaxRetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
sd.BABIntRetailOperatingUnitNumber, 
sd.RetailTerminalId, 
sd.TransDate, 
sd.ItemId, 
sd.LineDscAmount as LineDscAmount, 
sd.DiscAmount as DiscAmount, 
sd.GiftCardNumber, 
sd.BABIntRetailProcessed, 
sd.VatTaxAmount as VatTaxAmount, 
sd.CurrencyCode, 
sd.Entity, 
sd.PeriodicPercentageDiscount, 
sd.TotalDiscAmount, 
sd.TotalDiscPct,
'1' as isCurrent, 
getdate() as InsertDate 

--from [dbo].[DynamicsSalesDetailFactsStage] SD -- Replaced 12/13/2022
from [dbo].[DynamicsSalesDetailDiscountsFactsStage] SD
join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.retailreceiptid=sd.RetailReceiptId
											and l.UpdateProcessed is null 
											and l.TableName = 'DynamicsSalesDetailFacts'
join ##MaxID2 m on m.RetailReceiptId=l.retailreceiptid
				and m.TableName = 'DynamicsSalesDetailFacts'
group by sd.CustAccount, sd.InventLocationId, sd.LineNum, sd.OriginalPrice, sd.Price, sd.Qty, sd.RetailReceiptId, m.MaxRetailTransactionId, sd.BABIntRetailOperatingUnitNumber, sd.RetailTerminalId, sd.TransDate, sd.ItemId, sd.LineDscAmount, sd.DiscAmount, sd.GiftCardNumber, sd.BABIntRetailProcessed, sd.VatTaxAmount, sd.CurrencyCode, sd.Entity, sd.PeriodicPercentageDiscount,sd.TotalDiscAmount,sd.TotalDiscPct
order by m.MaxRetailTransactionId, sd.LineNum

-- Discount Data 
--INSERT INTO  dw.[dbo].[DynamicsDiscountFacts]  (Amount,DiscountCost,DiscountOriginType,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,LineNum,[Percentage],RetailStoreId,SaleLineNum,CustomerDiscountType,BABIntRetailProcessed,Entity,RetailReceiptId,IsCurrent,InsertDate) -- Replaced 12/13/2022
INSERT INTO  dw.[dbo].[DynamicsDiscountFacts]  (Amount,DiscountCost,DiscountOriginType,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,LineNum,RetailStoreId,SaleLineNum,CustomerDiscountType,BABIntRetailProcessed,Entity,RetailReceiptId,BabRetailDiscountTransUniqueLineNum,ManualDiscountType,PeriodicDiscountOfferId,IsCurrent,InsertDate)
select 
d.Amount as Amount, 
d.DiscountCost as DiscountCost, 
d.DiscountOriginType, 
d.RetailTerminalId, 
SUBSTRING(m.MaxRetailTransactionId,0, CHARINDEX('_' ,m.MaxRetailTransactionId)+1)+ cast(cast (right(m.MaxRetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
d.BABIntRetailOperatingUnitNumber, 
d.LineNum,  
--d.[Percentage], -- Removed 12/13/2022, we no longer populate this field 
d.RetailStoreId, 
d.SaleLineNum, 
d.CustomerDiscountType, 
d.BABIntRetailProcessed, 
d.Entity, 
d.RetailReceiptId, 
d.DiscountTransUniqueLineNum,
d.ManualDiscountType,
d.PeriodicDiscountOfferId,
'1' as isCurrent,  
getdate() as InsertDate 

from [dbo].[DynamicsDiscountFactsStage] D
join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.retailreceiptid=d.RetailReceiptId
											and l.UpdateProcessed is null 
											and l.TableName = 'DynamicsDiscountFacts'
join ##MaxID2 m on m.RetailReceiptId=d.retailreceiptid
				and m.TableName = 'DynamicsDiscountFacts'
group by d.Amount, d.DiscountCost, d.DiscountOriginType, d.RetailTerminalId, m.MaxRetailTransactionId, d.BABIntRetailOperatingUnitNumber, d.LineNum, d.Percentage, d.RetailStoreId, d.SaleLineNum, d.CustomerDiscountType, d.BABIntRetailProcessed, d.Entity, d.RetailReceiptId, d.DiscountTransUniqueLineNum,d.ManualDiscountType,d.PeriodicDiscountOfferId
											
-- Tax Data 
INSERT INTO  dw.[dbo].[DynamicsTaxFacts] (Amount,LineNum,TaxCode,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,BABIntRetailProcessed,Entity,RetailReceiptId,IsCurrent,InsertDate)
select
t.Amount as Amount, 
t.LineNum, 
t.TaxCode, 
t.RetailTerminalId, 
SUBSTRING(m.MaxRetailTransactionId,0, CHARINDEX('_' ,M.MaxRetailTransactionId)+1)+ cast(cast (right(m.MaxRetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
t.BABIntRetailOperatingUnitNumber, 
t.BABIntRetailProcessed, 
t.Entity, 
t.RetailReceiptId, 
'1' as isCurrent, 
getdate() as InsertDate 
from [dbo].[DynamicsTaxFactsStage]   T
join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.retailreceiptid=t.RetailReceiptId
											and l.UpdateProcessed is null 
											and l.TableName = 'DynamicsTaxFacts'											
join ##MaxID2 m on m.RetailReceiptId=t.retailreceiptid
				and m.TableName = 'DynamicsTaxFacts'
group by t.Amount, t.LineNum, t.TaxCode, t.RetailTerminalId, m.MaxRetailTransactionId, t.BABIntRetailOperatingUnitNumber, t.BABIntRetailProcessed, t.Entity, t.RetailReceiptId
order by m.MaxRetailTransactionId, t.LineNum

-- Payment Data 
INSERT INTO  dw.[dbo].[DynamicsPaymentFacts]  (AmountCur,AmountMst,RetailAmountTendered,RetailCardTypeId,RetailReceiptId,LineNum,RetailTransactionId,RetailTenderTypeId,RetailTerminalId,BABIntRetailOperatingUnitNumber,TransDate,AccountNum,RetailCardNum,ChangeLine,PaymentAuthorization,CurrencyCode,BABIntRetailProcessed,Entity,IsCurrent,InsertDate)
select 
p.AmountCur as AmountCur, 
p.AmountMst as AmountMst, 
p.RetailAmountTendered as RetailAmountTendered, 
p.RetailCardTypeId, 
p.RetailReceiptId, 
p.LineNum, 
SUBSTRING(m.MaxRetailTransactionId,0, CHARINDEX('_' ,M.MaxRetailTransactionId)+1)+ cast(cast (right(m.MaxRetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
p.RetailTenderTypeId, 
p.RetailTerminalId, 
p.BABIntRetailOperatingUnitNumber, 
p.TransDate, 
p.AccountNum, 
p.RetailCardNum, 
p.ChangeLine, 
p.PaymentAuthorization, 
p.CurrencyCode, 
p.BABIntRetailProcessed, 
p.Entity, 
'1' as isCurrent, 
getdate () as InsertDate
from [dbo].[DynamicsPaymentFactsStage]  P
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.retailreceiptid=p.RetailReceiptId
											and l.UpdateProcessed is null 
											and l.TableName = 'DynamicsPaymentFacts'
join ##MaxID2 m on m.RetailReceiptId=p.retailreceiptid
				and m.TableName = 'DynamicsPaymentFacts'
group by p.AmountCur, p.AmountMst, p.RetailAmountTendered, p.RetailCardTypeId, p.RetailReceiptId, p.LineNum, M.MaxRetailTransactionId, p.RetailTenderTypeId, p.RetailTerminalId, p.BABIntRetailOperatingUnitNumber, p.TransDate, p.AccountNum, p.RetailCardNum, p.ChangeLine, p.PaymentAuthorization, p.CurrencyCode, p.BABIntRetailProcessed, p.Entity


```

### Execute SQL Task - Update Step 1 - Identify Records to Be Updated

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base\Execute SQL Task - Update Step 1 - Identify Records to Be Updated`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
-- Had to change the##MaxID1 m CTE to a Temp Table Load for Performance reasons 

--with##MaxID1 m as (

--select hf.RetailReceiptId, 
--max (hf.RetailTransactionId) as MaxRetailTransactionId, 
--'DynamicsTransactionHeaderFacts' as TableName
--from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
--group by hf.RetailReceiptId 
--union 
--select Sdf.RetailReceiptId, 
--max (Sdf.RetailTransactionId) as MaxRetailTransactionId, 
--'DynamicsSalesDetailFacts' as TableName
--from dw.[dbo].[DynamicsSalesDetailFacts] SDF (nolock) 
--group by Sdf.RetailReceiptId 
--union
--select df.RetailReceiptId, 
--max (df.RetailTransactionId) as MaxRetailTransactionId, 
--'DynamicsDiscountFacts' as TableName
--FROM dw.dbo.[DynamicsDiscountFacts] df
--group by df.RetailReceiptId
--union 
--select tf.RetailReceiptId, 
--max (tf.RetailTransactionId) as MaxRetailTransactionId, 
--'DynamicsTaxFacts' as TableName
--FROM dw.dbo.[DynamicsTaxFacts] TF
--group by tf.RetailReceiptId
--union
--select pf.RetailReceiptId, 
--max (pf.RetailTransactionId) as MaxRetailTransactionId, 
--'DynamicsPaymentFacts' as TableName
--FROM dw.dbo.[DynamicsPaymentFacts] PF
--group by pf.RetailReceiptId


--), 

-- Create MaxID Temp Table 
IF OBJECT_ID(N'tempdb..##MaxID1') IS NOT NULL DROP TABLE ##MaxID1 
select hf.RetailReceiptId, 
max (hf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTransactionHeaderFacts' as TableName
into ##MaxID1 
from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
group by hf.RetailReceiptId 
union 
select Sdf.RetailReceiptId, 
max (Sdf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsSalesDetailFacts' as TableName
from dw.[dbo].[DynamicsSalesDetailFacts] SDF (nolock) 
group by Sdf.RetailReceiptId 
union
select df.RetailReceiptId, 
max (df.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsDiscountFacts' as TableName
FROM dw.dbo.[DynamicsDiscountFacts] df
group by df.RetailReceiptId
union 
select tf.RetailReceiptId, 
max (tf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsTaxFacts' as TableName
FROM dw.dbo.[DynamicsTaxFacts] TF
group by tf.RetailReceiptId
union
select pf.RetailReceiptId, 
max (pf.RetailTransactionId) as MaxRetailTransactionId, 
'DynamicsPaymentFacts' as TableName
FROM dw.dbo.[DynamicsPaymentFacts] PF
group by pf.RetailReceiptId

;

IF OBJECT_ID(N'tempdb..#UpdateTransactions') IS NOT NULL DROP TABLE #UpdateTransactions
--with UpdateTransactions as (

Select m.TableName, 
	hf.DynamicsTransactionHeaderFactsId as RecordId , 
	hf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
into #UpdateTransactions
from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=hf.RetailTransactionId
		and m.TableName = 'DynamicsTransactionHeaderFacts'
	join [DynamicsTransactionHeaderFactsStage] HFS on hfs.RetailReceiptId=hf.RetailReceiptId
where	HF.RetailTerminalId	<>	HFS.RetailTerminalId	or
		HF.InventLocationId	<>	HFS.InventLocationId	or
		HF.RetailStaffId	<>	HFS.RetailStaffId	or
		HF.BABIntRetailOperatingUnitNumber	<>	HFS.BABIntRetailOperatingUnitNumber	or
		HF.TransDate	<>	HFS.TransDate	or
		HF.RetailTransactionType	<>	HFS.RetailTransactionType
group by m.TableName, hf.DynamicsTransactionHeaderFactsId, hf.RetailReceiptId
	union 
Select m.TableName, 
	sdf.DynamicsSalesDetailFactsId as RecordId , 
	sdf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsSalesDetailFacts]  SDF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=sdf.RetailTransactionId
		and m.TableName = 'DynamicsSalesDetailFacts'
	--join [DynamicsSalesDetailFactsStage] SDS on SDS.RetailReceiptId=sdf.RetailReceiptId -- Replaced 12/13/2022
	join [DynamicsSalesDetailDiscountsFactsStage] SDS on SDS.RetailReceiptId=sdf.RetailReceiptId
		and sds.LineNum=sdf.LineNum
where 	
	SDF.InventLocationId	<>	SDS.InventLocationId	or
	SDF.OriginalPrice	<>	SDS.OriginalPrice	or
	SDF.Price	<>	SDS.Price	or
	SDF.Qty	<>	SDS.Qty	or	
	SDF.BABIntRetailOperatingUnitNumber	<>	SDS.BABIntRetailOperatingUnitNumber	or
	SDF.RetailTerminalId	<>	SDS.RetailTerminalId	or
	SDF.TransDate	<>	SDS.TransDate	or
	SDF.ItemId	<>	SDS.ItemId	or
	SDF.LineDscAmount	<>	SDS.LineDscAmount	or
	SDF.DiscAmount	<>	SDS.DiscAmount or 
	SDF.TotalDiscAmount <> SDS.TotalDiscAmount or
	SDF.TotalDiscPct <> SDS.TotalDiscPct
group by m.TableName, sdf.DynamicsSalesDetailFactsId, sdf.RetailReceiptId
	union 
Select m.TableName, 
	df.DynamicsDiscountFactsId as RecordId , 
	df.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsDiscountFacts]  DF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=df.RetailTransactionId
		and m.TableName = 'DynamicsDiscountFacts'
	join [DynamicsDiscountFactsStage] DFS on df.RetailReceiptId=dfs.RetailReceiptId
		and df.SaleLineNum=dfs.SaleLineNum
		--and df.LineNum=dfs.LineNum -- Replaced with join below on 12/13/2022
		and df.BabRetailDiscountTransUniqueLineNum = dfs.DiscountTransUniqueLineNum
		
where 
	DF.Amount	<>	DFS.Amount	or
	DF.DiscountCost	<>	DFS.DiscountCost	or
	DF.DiscountOriginType	<>	DFS.DiscountOriginType	or
	DF.RetailTerminalId	<>	DFS.RetailTerminalId	or	
	DF.BABIntRetailOperatingUnitNumber	<>	DFS.BABIntRetailOperatingUnitNumber	or	
	--DF.[Percentage]	<>	DFS.[Percentage]	or -- Omitted 12/13/2022 as we are no longer populating this field 
	DF.RetailStoreId	<>	DFS.RetailStoreId	or	
	DF.CustomerDiscountType	<>	DFS.CustomerDiscountType
group by m.TableName, df.DynamicsDiscountFactsId, df.RetailReceiptId
	union 
Select m.TableName, 
	tf.DynamicsTaxFactsId as RecordId , 
	tf.RetailReceiptId,
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsTaxFacts] TF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=tf.RetailTransactionId
		and m.TableName = 'DynamicsTaxFacts'
	join [DynamicsTaxFactsStage] TFS on tf.RetailReceiptId=tfs.RetailReceiptId
		and tf.LineNum=tfs.LineNum
where 
	TF.Amount	<>	TFS.Amount	or
	TF.RetailTerminalId	<>	TFS.RetailTerminalId	or
	TF.BABIntRetailOperatingUnitNumber	<>	TFS.BABIntRetailOperatingUnitNumber	
group by m.TableName, tf.DynamicsTaxFactsId, tf.RetailReceiptId
	union 

Select m.TableName, 
	pf.DynamicsPaymentFactsId as RecordId , 
	pf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsPaymentFacts] PF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=Pf.RetailTransactionId
		and m.TableName = 'DynamicsPaymentFacts'
	join [DynamicsPaymentFactsStage] pFS on Pf.RetailReceiptId=Pfs.RetailReceiptId
		and pf.LineNum=pfs.LineNum
where 	
	PF.AmountCur	<>	PFS.AmountCur	or
	PF.AmountMst	<>	PFS.AmountMst	or
	PF.RetailAmountTendered	<>	PFS.RetailAmountTendered	or	
	PF.RetailTenderTypeId	<>	PFS.RetailTenderTypeId	or
	PF.RetailTerminalId	<>	PFS.RetailTerminalId	or
	PF.BABIntRetailOperatingUnitNumber	<>	PFS.BABIntRetailOperatingUnitNumber	or
	PF.TransDate	<>	PFS.TransDate	or	
	PF.ChangeLine	<>	PFS.ChangeLine	or	
	PF.CurrencyCode	<>	PFS.CurrencyCode	

group by m.TableName, pf.DynamicsPaymentFactsId, pf.RetailReceiptId	
--) , 

IF OBJECT_ID(N'tempdb..#UpdatedSummary') IS NOT NULL DROP TABLE #UpdatedSummary

--UpdatedSummary  as (

select distinct RetailReceiptId
into #UpdatedSummary
from #UpdateTransactions

--) , 

IF OBJECT_ID(N'tempdb..#SummaryFinal') IS NOT NULL DROP TABLE #SummaryFinal
--SummaryFinal as (

select 
	m.TableName, 
	hf.DynamicsTransactionHeaderFactsId as RecordId , 
	hf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
into #SummaryFinal
from dw.[dbo].[DynamicsTransactionHeaderFacts]  HF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=hf.RetailTransactionId
		and m.TableName = 'DynamicsTransactionHeaderFacts'
	join #Updatedsummary u on u.RetailReceiptId=hf.RetailReceiptId
	union 
select 
	m.TableName, 
	sf.DynamicsSalesDetailFactsId as RecordId , 
	sf.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsSalesDetailFacts]  SF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=sf.RetailTransactionId
		and m.TableName = 'DynamicsSalesDetailFacts'
	join #Updatedsummary u on u.RetailReceiptId=sf.RetailReceiptId
	union
Select 
	m.TableName, 
	df.DynamicsDiscountFactsId as RecordId , 
	df.RetailReceiptId, 
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsDiscountFacts]  DF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=df.RetailTransactionId
		and m.TableName = 'DynamicsDiscountFacts'
	join #Updatedsummary u on u.RetailReceiptId=df.RetailReceiptId
	union 
Select
	m.TableName, 
	tf.DynamicsTaxFactsId as RecordId , 
	tf.RetailReceiptId,
	null as UpdateProcesed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsTaxFacts] TF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=tf.RetailTransactionId
		and m.TableName = 'DynamicsTaxFacts'
	join #Updatedsummary u on u.RetailReceiptId=tf.RetailReceiptId
	union 
Select 
	m.TableName, 
	pf.DynamicsPaymentFactsId as RecordId , 
	pf.RetailReceiptId, 
	null as UpdateProcessed, 
	getdate() as InsertDate, 
	null as UpdateDate 	
from dw.[dbo].[DynamicsPaymentFacts] PF (nolock) 
	join ##MaxID1 m on m.MaxRetailTransactionId=Pf.RetailTransactionId
		and m.TableName = 'DynamicsPaymentFacts'
	join #Updatedsummary u on u.RetailReceiptId=pf.RetailReceiptId



--), 

IF OBJECT_ID(N'tempdb..#ExistsInDynamics') IS NOT NULL DROP TABLE #ExistsInDynamics
--ExistsInDynamics as (
	select RetailTransactionId, RetailReceiptId, Entity 
	into #ExistsInDynamics
	from dw.dbo.DynamicsTransactionHeaderFacts
	where 1=1
	and IsInDynamics = 1  -- Should Be A Prod Flag
	and IsCurrent = 1 -- Should Be A Prod Flag
	--and DATEDIFF(dd,TransDate,Getdate()) <= 61 -- Should Be A Prod Flag
	--and InventLocationId = '1016' -- Use these filters and below when wanting to do a targeted transaction set 
	--and TransDate between '01-29-2023' and '02-25-2023'-- Use these filters and below when wanting to do a targeted transaction set 
	group by RetailTransactionId, RetailReceiptId, Entity 
--)

Insert Into dw.dbo.[DynamicsTransactionUpdateLog] (TableName,RecordId,RetailReceiptId,UpdateProcessed,InsertDate,UpdateDate)
select sf.TableName, 
sf.RecordId, 
sf.RetailReceiptId, 
sf.UpdateProcesed, 
sf.InsertDate, 
sf.UpdateDate
from #SummaryFinal sf 
join #ExistsInDynamics E on sf.RetailReceiptId=e.RetailReceiptId 
--where sf.RetailReceiptId in ('468706731') -- Testing Specific Transactions 
order by 3,1 
	
```

### Execute SQL Task - Update Step 2 - Set IsCurrent to Null

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base\Execute SQL Task - Update Step 2 - Set IsCurrent to Null`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
-- Update existing records IsCurrent value to null 


-- Header
Update  H
Set H.IsCurrent= null
--select *
from dw.[dbo].[DynamicsTransactionHeaderFacts] H
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=H.DynamicsTransactionHeaderFactsId 
											and l.TableName = 'DynamicsTransactionHeaderFacts'
											and l.UpdateProcessed is null 
-- Sales Detail 

Update  SD
Set SD.IsCurrent= null
--select *
from dw.[dbo].[DynamicsSalesDetailFacts] SD
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=sd.DynamicsSalesDetailFactsId
											and l.TableName = 'DynamicsSalesDetailFacts'
											and l.UpdateProcessed is null 

-- Discounts 
Update  D
Set D.IsCurrent= null
--select *
from dw.[dbo].[DynamicsDiscountFacts] D
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=d.DynamicsDiscountFactsId
											and l.TableName = 'DynamicsDiscountFacts'
											and l.UpdateProcessed is null 

-- Payments
Update  P
Set P.IsCurrent= null
--select *
from dw.[dbo].[DynamicsPaymentFacts]  P
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=p.DynamicsPaymentFactsId
											and l.TableName = 'DynamicsPaymentFacts'
											and l.UpdateProcessed is null 

-- Tax 
Update  T
Set T.IsCurrent= null
--select *
from dw.[dbo].[DynamicsTaxFacts]   T
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=t.DynamicsTaxFactsId
											and l.TableName = 'DynamicsTaxFacts'
											and l.UpdateProcessed is null 




												

```

### Execute SQL Task - Update Step 3 - Insert Negating Transactions

**Path:** `Package\Master Container\Merge and Update Sales Data\SeqCont - Execute Transaction Updates Merge\SeqCont - Execute Transaction Updates Merge - Transactions Exist in Base\Execute SQL Task - Update Step 3 - Insert Negating Transactions`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
-- Insert Negating Transactions 

-- Header 


INSERT INTO dw.[dbo].[DynamicsTransactionHeaderFacts] (RetailTerminalId,CustAccount,InventLocationId,RetailReceiptId,RetailStaffId,RetailTransactionId,BABIntRetailOperatingUnitNumber,TransDate,RetailTransactionType,BABIntRetailProcessed,Entity,DiscAmount,TotalDiscAmount,IsNegatedCurrent,InsertDate,TransactionNumber)
select 
h.RetailTerminalId, 
h.CustAccount, 
h.InventLocationId, 
h.RetailReceiptId, 
h.RetailStaffId, 
SUBSTRING(RetailTransactionId,0, CHARINDEX('_' ,h.RetailTransactionId)+1)+ cast(cast (right(h.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
h.BABIntRetailOperatingUnitNumber, 
h.TransDate, 
h.RetailTransactionType, 
h.BABIntRetailProcessed, 
h.Entity, 
h.DiscAmount*-1 as DiscAmount,
h.TotalDiscAmount*-1 as TotalDiscAmount ,
'1' as IsNegatedCurrent, 
getdate() as InsertDate, 
h.TransactionNumber

from dw.[dbo].[DynamicsTransactionHeaderFacts] H
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=H.DynamicsTransactionHeaderFactsId 
											and l.TableName = 'DynamicsTransactionHeaderFacts'
											and l.UpdateProcessed is null 
											and H.BatchID is not null -- Added 01/23/2023 -- Found that sometimes the original transaction merge is inserting a record when it should't which is resulting in negating a line that was never sent 



-- Sales Detail 
INSERT INTO  dw.[dbo].[DynamicsSalesDetailFacts] (CustAccount,InventLocationId,LineNum,OriginalPrice,Price,Qty,RetailReceiptId,RetailTransactionId,BABIntRetailOperatingUnitNumber,RetailTerminalId,TransDate,ItemId,LineDscAmount,DiscAmount,GiftCardNumber,BABIntRetailProcessed,VatTaxAmount,CurrencyCode,Entity,PeriodicPercentageDiscount,TotalDiscAmount,TotalDiscPct,IsNegatedCurrent,InsertDate)
select 
sd.CustAccount, 
sd.InventLocationId, 
sd.LineNum, 
sd.OriginalPrice*-1 as OriginalPrice, 
sd.Price*-1 as Price, 
sd.Qty*-1 as Qty, 
sd.RetailReceiptId, 
SUBSTRING(sd.RetailTransactionId,0, CHARINDEX('_' ,sd.RetailTransactionId)+1)+ cast(cast (right(sd.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
sd.BABIntRetailOperatingUnitNumber, 
sd.RetailTerminalId, 
sd.TransDate, 
sd.ItemId, 
sd.LineDscAmount*-1 as LineDscAmount, -- Per Elizabeth W these values need to be negative on the negating transaction
sd.DiscAmount*-1 as DiscAmount, -- Per Elizabeth W these values need to be negative on the negating transaction
sd.GiftCardNumber, 
sd.BABIntRetailProcessed, 
sd.VatTaxAmount*-1 as VatTaxAmount, 
sd.CurrencyCode, 
sd.Entity, 
sd.PeriodicPercentageDiscount as PeriodicPercentageDiscount , --3/29/2023 -- Per Joel Berger this field can NEVER be negative 
sd.TotalDiscAmount*-1 as TotalDiscAmount, 
sd.TotalDiscPct as TotalDiscPct , --3/29/2023 -- Per Joel Berger this field can NEVER be negative 
'1' as IsNegatedCurrent, 
getdate() as InsertDate 

from dw.[dbo].[DynamicsSalesDetailFacts] SD
join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=sd.DynamicsSalesDetailFactsId
											and l.TableName = 'DynamicsSalesDetailFacts'
											and l.UpdateProcessed is null 
											and SD.BatchID is not null -- Added 01/23/2023 -- Found that sometimes the original transaction merge is inserting a record when it should't which is resulting in negating a line that was never sent 



-- Discounts 
--INSERT INTO  dw.[dbo].[DynamicsDiscountFacts]  (Amount,DiscountCost,DiscountOriginType,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,LineNum,[Percentage],RetailStoreId,SaleLineNum,CustomerDiscountType,BABIntRetailProcessed,Entity,RetailReceiptId,IsNegatedCurrent,InsertDate)
INSERT INTO  dw.[dbo].[DynamicsDiscountFacts]  (Amount,DiscountCost,DiscountOriginType,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,LineNum,RetailStoreId,SaleLineNum,CustomerDiscountType,BABIntRetailProcessed,Entity,RetailReceiptId,BabRetailDiscountTransUniqueLineNum,ManualDiscountType,PeriodicDiscountOfferId,IsNegatedCurrent,InsertDate)
select 
d.Amount*-1 as Amount, 
d.DiscountCost*-1 as DiscountCost, 
d.DiscountOriginType, 
d.RetailTerminalId, 
SUBSTRING(d.RetailTransactionId,0, CHARINDEX('_' ,d.RetailTransactionId)+1)+ cast(cast (right(d.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
d.BABIntRetailOperatingUnitNumber, 
d.LineNum,  
--d.[Percentage], -- Remarked out on 12/13/2022 we no longer populate this field 
d.RetailStoreId, 
d.SaleLineNum, 
d.CustomerDiscountType, 
d.BABIntRetailProcessed, 
d.Entity, 
d.RetailReceiptId, 
d.BabRetailDiscountTransUniqueLineNum, -- Added 12/13/2022
d.ManualDiscountType, -- Added 12/13/2022
d.PeriodicDiscountOfferId, -- Added 12/13/2022
'1' as IsNegatedCurrent, 
getdate() as InsertDate 

from dw.[dbo].[DynamicsDiscountFacts] D
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=d.DynamicsDiscountFactsId
											and l.TableName = 'DynamicsDiscountFacts'
											and l.UpdateProcessed is null 
											and D.BatchID is not null -- Added 01/23/2023 -- Found that sometimes the original transaction merge is inserting a record when it should't which is resulting in negating a line that was never sent 


-- Tax 

INSERT INTO  dw.[dbo].[DynamicsTaxFacts] (Amount,LineNum,TaxCode,RetailTerminalId,RetailTransactionId,BABIntRetailOperatingUnitNumber,BABIntRetailProcessed,Entity,RetailReceiptId,IsNegatedCurrent,InsertDate)
select
t.Amount*-1 as Amount, 
t.LineNum, 
t.TaxCode, 
t.RetailTerminalId, 
SUBSTRING(t.RetailTransactionId,0, CHARINDEX('_' ,t.RetailTransactionId)+1)+ cast(cast (right(t.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
t.BABIntRetailOperatingUnitNumber, 
t.BABIntRetailProcessed, 
t.Entity, 
t.RetailReceiptId, 
'1' as IsNegatedCurrent, 
getdate() as InsertDate 
from dw.[dbo].[DynamicsTaxFacts]   T
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=t.DynamicsTaxFactsId
											and l.TableName = 'DynamicsTaxFacts'
											and l.UpdateProcessed is null 
											and T.BatchID is not null -- Added 01/23/2023 -- Found that sometimes the original transaction merge is inserting a record when it should't which is resulting in negating a line that was never sent 

-- Payments 
INSERT INTO  dw.[dbo].[DynamicsPaymentFacts]  (AmountCur,AmountMst,RetailAmountTendered,RetailCardTypeId,RetailReceiptId,LineNum,RetailTransactionId,RetailTenderTypeId,RetailTerminalId,BABIntRetailOperatingUnitNumber,TransDate,AccountNum,RetailCardNum,ChangeLine,PaymentAuthorization,CurrencyCode,BABIntRetailProcessed,Entity,IsNegatedCurrent,InsertDate)
select 
p.AmountCur*-1 as AmountCur, 
p.AmountMst*-1 as AmountMst, 
p.RetailAmountTendered*-1 as RetailAmountTendered, 
p.RetailCardTypeId, 
p.RetailReceiptId, 
p.LineNum, 
SUBSTRING(p.RetailTransactionId,0, CHARINDEX('_' ,p.RetailTransactionId)+1)+ cast(cast (right(p.RetailTransactionId,1) as int) + 1 as varchar) as RetailTransactionId, 
p.RetailTenderTypeId, 
p.RetailTerminalId, 
p.BABIntRetailOperatingUnitNumber, 
p.TransDate, 
p.AccountNum, 
p.RetailCardNum, 
p.ChangeLine, 
p.PaymentAuthorization, 
p.CurrencyCode, 
p.BABIntRetailProcessed, 
p.Entity, 
'1' as IsNegatedCurrent, 
getdate () as InsertDate
from dw.[dbo].[DynamicsPaymentFacts]  P
	join dw.[dbo].[DynamicsTransactionUpdateLog] L on l.RecordId=p.DynamicsPaymentFactsId
											and l.TableName = 'DynamicsPaymentFacts'
											and l.UpdateProcessed is null 
											and P.BatchID is not null -- Added 01/23/2023 -- Found that sometimes the original transaction merge is inserting a record when it should't which is resulting in negating a line that was never sent 




```

### Execute SQL Task - Exclude Trans Before Cutover Start Date

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Staging Tables\Execute SQL Task - Exclude Trans Before Cutover Start Date`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql

-- Identify Transactions To Exclude 
-- This should only be necessary as we are onboarding stores to retail inventory 

IF OBJECT_ID(N'tempdb..##ExcludedTrans') IS NOT NULL
Drop Table ##ExcludedTrans

select distinct  h.RetailTransactionId, h.TransDate, h.InventLocationId
into ##ExcludedTrans
from DynamicsTransactionHeaderFactsStage h

where 1=1
and (
	InventLocationId in ('1001','1002','1102','1105','1167','1183','1212','1221','1278','1286','1415','1521','1534') -- Stores in This Pilot Group
	and 
	TransDate < '04-02-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Pilot Group 1 

or 
	(
	InventLocationId in ('1119','1130','1174','1177','1204','1205','1215','1358','1404','1439','1540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082')-- Stores in This Pilot Group
	and 
	TransDate < '04-30-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Pilot Group 2 
or 
	(
	InventLocationId in ('1003','1004','1012','1016','1020','1021','1030','1037','1038','1043','1053','1056','1062','1063','1065','1068','1076','1084','1085','1087','1093','1098','1101','1103','1109','1113','1122','1126','1129','1131','1133','1134','1137','1138','1139','1144','1149','1156','1157','1166','1185','1186','1190','1194','1195','1196','1202','1203','1208','1214','1224','1239','1251','1267','1277','1281','1313','1316','1321','1423','1425','1448','1535','1536','1603','1614')-- Stores in This Pilot Group 3
	and 
	TransDate < '05-28-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Pilot Group 3
or 
	(
	InventLocationId in ('1011','1031','1041','1046','1049','1066','1071','1072','1082','1099','1110','1117','1118','1128','1158','1161','1169','1175','1181','1191','1192','1193','1198','1207','1210','1222','1226','1236','1237','1247','1248','1254','1256','1257','1260','1268','1275','1297','1298','1299','1307','1308','1309','1315','1318','1326','1328','1330','1331','1345','1350','1393','1397','1398','1421','1424','1446','1454','1457','1520','1542','1607','1613','2003','2006','2016','2017','2018','2033','2034','2035','2036','2037','2042','2043','2052','2054','2058','2077','2078')-- Stores in This Pilot Group 4
	and 
	TransDate < '07-02-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Pilot Group 4
or 
	(
	InventLocationId in ('1006','1010','1014','1018','1022','1029','1032','1036','1040','1045','1051','1055','1059','1078','1083','1086','1089','1090','1091','1092','1094','1096','1106','1108','1116','1123','1125','1132','1141','1145','1148','1152','1160','1164','1168','1171','1178','1199','1201','1206','1213','1220','1223','1234','1244','1271','1273','1287','1290','1291','1300','1310','1317','1319','1324','1329','1335','1337','1349','1422','1447','1449','1453','1458','1468','1537','1541','1543','1549','1551','1621')-- Stores in This Pilot Group 5
	and 
	TransDate < '7-30-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Pilot Group 5
or 
	(
	InventLocationId in ('1009','1015','1019','1023','1026','1034','1039','1042','1047','1054','1057','1064','1075','1077','1079','1080','1088','1100','1104','1107','1115','1120','1135','1142','1147','1151','1153','1154','1159','1162','1163','1170','1173','1176','1200','1216','1218','1230','1231','1233','1238','1243','1245','1249','1253','1258','1261','1264','1265','1274','1294','1295','1302','1312','1327','1332','1334','1354','1355','1356','1361','1363','1364','1366','1367','1368','1370','1371','1382','1384','1385','1402','1405','1407','1411','1414','1416','1417','1440','1441','1451','1452','1459','1476','1525','1526','1527','1528','1529','1530','1532','1533','1538','1539','1550','1552','1553','1554','1605','1610','1615','1619','1620','2019','2079','2080','2013')-- Stores in This Pilot Group 6
	and 
	TransDate < '08-27-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Pilot Group 6
or 
	(
	InventLocationId in ('1478','1546','1548')-- Stores in This Pilot Group
	and 
	TransDate < '11-22-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Joel Berger Request on 11/29/2023
or 
	(
	InventLocationId in ('1547')-- Stores in This Pilot Group
	and 
	TransDate < '11-21-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Joel Berger Request on 11/29/2023
or 
	(
	InventLocationId in ('2084')-- Stores in This Pilot Group
	and 
	TransDate < '11-20-2023' -- Pilot Group Sales Transaction Go Live Fiscal Date
	) -- Joel Berger Request on 11/29/2023

--or 
--	(
--	InventLocationId in ()-- Stores in This Pilot Group
--	and 
--	TransDate < '' -- Pilot Group Sales Transaction Go Live Fiscal Date
--	) -- Group 7?

group by h.RetailTransactionId, h.TransDate, h.InventLocationId

-- Validation\Testing 
/*
select *
from ##ExcludedTrans e
where e.InventLocationId in ('1001','1002','1102','1105','1167','1183','1212','1221','1278','1286','1415','1521','1534')  -- Pilot Group 1 
--where e.InventLocationId in ('1119','1122','1130','1174','1177','1204','1205','1215','1358','1404','1439','1540','2001','2010','2020','2022','2023','2024','2026','2028','2029','2045','2047','2048','2051','2062','2063','2069','2081','2082') -- Pilot Group 2 
order by e.TransDate
*/



-- Perform Delete 
 

delete from [dbo].[DynamicsTransactionHeaderFactsStage] 
where RetailTransactionId in (select distinct RetailTransactionId from ##ExcludedTrans)

delete from [dbo].[DynamicsSalesDetailFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from ##ExcludedTrans)

delete from [dbo].[DynamicsSalesDetailDiscountsFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from ##ExcludedTrans)

delete from [dbo].[DynamicsDiscountFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from ##ExcludedTrans)

delete from [dbo].[DynamicsTaxFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from ##ExcludedTrans)

delete from [dbo].[DynamicsPaymentFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from ##ExcludedTrans)

```

### Execute SQL Task - Truncate Stage

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Staging Tables\Execute SQL Task - Truncate Stage`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
truncate table DynamicsTransactionHeaderFactsStage
truncate table DynamicsSalesDetailFactsStage
truncate table DynamicsSalesDetailDiscountsFactsStage
truncate table DynamicsDiscountFactsStage
truncate table DynamicsPaymentFactsStage
truncate table DynamicsTaxFactsStage

```

### Execute SQL Task - Clean up $0 Payment Lines

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Staging Tables\SeqCont - Clean Up Payment Table\Execute SQL Task - Clean up $0 Payment Lines`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
-- Identify 0.00 Payment lines that are not cash nor giftcards 
With ZeroDollarPaymentLines as (

select distinct RetailTransactionId
from  [dbo].DynamicsPaymentFactsStage
where amountcur = 0.00
and RetailTenderTypeId  not in ('600','633') -- Exclude Cash and Gift Card Tender types as those can be $0 applied 

)

Update [dbo].DynamicsPaymentFactsStage  
set RetailCardTypeId = null, RetailTenderTypeId = 600 -- Cash Tender 
from ZeroDollarPaymentLines Z
join dbo.DynamicsPaymentFactsStage  P on z.RetailTransactionId=p.RetailTransactionId
where p.RetailTenderTypeId not in ('600','633') -- Exclude Cash and Gift Card Tender types as those can be $0 applied 

```

### Execute SQL Task - Clean up 1 Cent Variances

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Staging Tables\SeqCont - Clean Up Payment Table\Execute SQL Task - Clean up 1 Cent Variances`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
---- This Script will be used to Validate Gross Amount is matching Tender Amount 
--IF OBJECT_ID(N'dbo.TmpOrdersTie', N'U') IS NOT NULL  
--DROP TABLE [dbo].[TmpOrdersTie];

with Sales as (
	--select s.RetailTransactionId, entity, RetailReceiptId, TransDate, sum(s.Price*s.Qty) as SalesTotal
	select s.RetailTransactionId, entity, RetailReceiptId, TransDate, 
	--sum ((s.OriginalPrice*s.Qty)-s.LineDscAmount) as SalesTotal -- Old 
	sum (s.OriginalPrice*abs(s.qty))-sum(s.DiscAmount) as SalesTotal 
	--from DynamicsSalesDetailFactsStage s (nolock) 	
	from DynamicsSalesDetailDiscountsFactsStage s (nolock) 	
	group by s.RetailTransactionId, entity, RetailReceiptId, TransDate
), 

Tax as (
select 
	RetailTransactionId, 
	entity, 
	cast (dbo.bankersround(sum(Amount),2) as decimal (14,2))as TaxAmount
	from DynamicsTaxFactsStage (nolock) 
	group by RetailTransactionId, entity

),

Tenders as (
select 
	p.RetailTransactionId, sum(p.AmountCur) as PaymentTotal
	from DynamicsPaymentFactsStage p (nolock) 
	group by p.RetailTransactionId
) , 

Summary1 as (
select 
	s.*, 
	isnull(tx.TaxAmount,0.00) as TaxTotal, 
	isnull(t.PaymentTotal,0.00) as PaymentTotal
	from Sales s 
	left join Tenders t on s.RetailTransactionId=t.RetailTransactionId
	left join Tax tx on tx.RetailTransactionId=s.RetailTransactionId

), 

Summary2 as (

select 
	RetailTransactionId, 
	Entity, 
	RetailReceiptId,
	TransDate,
	cast(SalesTotal+TaxTotal as decimal (14,2)) as GrossAmount,
	cast (PaymentTotal as decimal (14,2)) as PaymentTotal 
	from Summary1
), 

Summary3 as (
select 
	RetailTransactionId, 
	RetailReceiptId,
	TransDate,
	Entity,
	GrossAmount, 
	PaymentTotal, 
	PaymentTotal-GrossAmount as Variance
	from Summary2 
	
	
) , 

TransPaymentsToUpdate as (


select RetailTransactionId, Variance
from Summary3
where GrossAmount <> PaymentTotal -- 
and abs(variance) = .01
)

/* -- Troubleshooting 
select * from TransPaymentsToUpdate

*/

update  DynamicsPaymentFactsStage
Set AmountCur = AmountCur + (t.Variance*-1), 
AmountMst = AmountMst + (t.Variance*-1),
RetailAmountTendered = RetailAmountTendered + (t.Variance*-1)
 -- Times -1 is necessary to properly account for negative variances
From TransPaymentsToUpdate T
join DynamicsPaymentFactsStage P on t.RetailTransactionId=p.RetailTransactionId
	and p.LineNum = 1 -- There were always be at least one payment line 



```

### Execute SQL Task - Append Blank Sound Chip - New

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Staging Tables\SeqCont - Load Header and Detail Stage\Execute SQL Task - Append Blank Sound Chip - New`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
with MaxLineNumber as (
select 
	RetailTransactionId,
	max (LineNum)  as MaxLineNum, 
	max (TransactionLineSeq) as MaxTransactionLineSeq
from [dbo].[DynamicsSalesDetailDiscountsFactsStage] (nolock) 
--where BlankSoundChipItemId is not null 
group by 
	RetailTransactionId 
	

), 

HearMeTransactions as (
select 
CustAccount, 
InventLocationId, 
sum(Qty) as Quantity,
RetailReceiptId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
RetailTerminalId, 
TransDate, 
GiftCardNumber, 
BABIntRetailProcessed, 
CurrencyCode, 
Entity, 
--LineObject, 
--LineAction, 
BlankSoundChipItemId  
from [dbo].[DynamicsSalesDetailDiscountsFactsStage] (nolock) 
where BlankSoundChipItemId is not null 
group by
CustAccount, 
InventLocationId, 
RetailReceiptId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
RetailTerminalId, 
TransDate, 
GiftCardNumber, 
BABIntRetailProcessed, 
CurrencyCode, 
Entity, 
--LineObject, 
--LineAction, 
BlankSoundChipItemId  




), 

Summary1 as (
select h.CustAccount, 
h.InventLocationId, 
m.MaxTransactionLineSeq+100 as TransactionLineSeq, 
m.MaxLineNum+1 as LineNum, 
0.00 as OriginalPrice, 
0.00 as Price, 
h.Quantity as Qty, 
h.RetailReceiptId, 
h.RetailTransactionId, 
h.BABIntRetailOperatingUnitNumber, 
h.RetailTerminalId, 
h.TransDate, 
h.BlankSoundChipItemId as ItemId, 
0.00 as LineDscAmount, 
0.00 as DiscAmount, 
h.GiftCardNumber, 
h.BABIntRetailProcessed, 
0.00 as VatTaxAmount, 
h.CurrencyCode, 
h.Entity, 
null as LineObject, 
null as LineAction, 
h.BlankSoundChipItemId, 
0.00 as PeriodicPercentageDiscount, 
0.00 as TotalDiscAmount, 
0.00 as TotalDiscPct
from HearMeTransactions H 
join MaxLineNumber m on m.RetailTransactionId=h.RetailTransactionId					
)


insert into DynamicsSalesDetailDiscountsFactsStage
select *
from Summary1 s
where s.Qty <> 0 -- Do they want a net 0 line ? 





```

### Execute SQL Task

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Tax  Discount and Tender Reference Data\SeqCont - Load Discount Ref Table\Execute SQL Task`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
truncate table [DiscountFactsReferenceDynamicsStage]
```

### Execute SQL Task

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Tax  Discount and Tender Reference Data\SeqCont - Load Tax Data from AW - Replaced by Dans ETL\Execute SQL Task`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
truncate table TransactionTaxFactsDynamicsStage 
```

### Execute SQL Task

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Tax  Discount and Tender Reference Data\SeqCont - Load Tender Exchange Ref Table\Execute SQL Task`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
Truncate Table DynamicsTenderExchangeFactsStage
```

### spMergeDynamicsTenderExchangeFacts

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Tax  Discount and Tender Reference Data\SeqCont - Load Tender Exchange Ref Table\spMergeDynamicsTenderExchangeFacts`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
exec spMergeDynamicsTenderExchangeFacts
```

### Execute SQL Task

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Load Tax  Discount and Tender Reference Data\SeqCont - Load Tender Facts  Reference Table\Execute SQL Task`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
truncate table [TenderPercentageFactsDynamicsStage]
```

### Execute SQL Task - Delete Exception Records From Staging Tables

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Validations and  Exception Routing\Execute SQL Task - Delete Exception Records From Staging Tables`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
delete from [dbo].[DynamicsTransactionHeaderFactsStage] 
where RetailTransactionId in (select distinct RetailTransactionId from [DynamicsSalesTransactionExceptions] where iscurrent = 1)

delete from [dbo].[DynamicsSalesDetailFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from [DynamicsSalesTransactionExceptions] where iscurrent = 1)

delete from [dbo].[DynamicsSalesDetailDiscountsFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from [DynamicsSalesTransactionExceptions] where iscurrent = 1)

delete from [dbo].[DynamicsDiscountFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from [DynamicsSalesTransactionExceptions] where iscurrent = 1)

delete from [dbo].[DynamicsTaxFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from [DynamicsSalesTransactionExceptions] where iscurrent = 1)

delete from [dbo].[DynamicsPaymentFactsStage]
where RetailTransactionId in (select distinct RetailTransactionId from [DynamicsSalesTransactionExceptions] where iscurrent = 1)
```

### Execute SQL Task - Update IsCurrent on Exception Table and Delete Old Records

**Path:** `Package\Master Container\SeqCont - Stage Sales Data\SeqCont - Validations and  Exception Routing\Execute SQL Task - Update IsCurrent on Exception Table and Delete Old Records`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
-- Delete Old Entries
delete 
from [DynamicsSalesTransactionExceptions] 
where DATEDIFF(dd,InsertDate,getdate()) >= 75

-- Delete Entries where Transaction now exists in Fact Table 
delete
from DynamicsSalesTransactionExceptions 
where RetailReceiptId in 
	(
		select distinct RetailReceiptId
		from dw.dbo.DynamicsTransactionHeaderFacts
		where RetailReceiptId in (select distinct RetailReceiptId from DynamicsSalesTransactionExceptions)
	)
	   
-- Clear Current Exceptions Flag 
update [DynamicsSalesTransactionExceptions] 
set IsCurrent = null 
where IsCurrent is not null 
```

### Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag

**Path:** `Package\Sequence Container\SeqCont -  Dynamics Import Validations - Daily\Execute SQL Task - Set IsInDynamicsFlag or IsInDynamicsStagingFlag`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
IF OBJECT_ID(N'tempdb..##UpdateSummary') IS NOT NULL DROP TABLE ##UpdateSummary;

with BaseSource as (
select r.TransactionNumber as RetailTransactionId, 
r.dataareaid as Entity,
r.RreceiptId as RetailReceiptId
from tmpDynamicsRetailTransaction r
group by r.TransactionNumber, r.dataAreaId, r.RreceiptId

) , 

StagingSource as (


select i.RetailTransactionId as RetailTransactionId_Staging, 
i.dataAreaId as Entity_Staging, 
i.RetailReceiptId as RetailReceiptId_Staging
from tmpDynamicsIntRetailTransaction i 
group by i.RetailTransactionId, i.dataAreaId, i.RetailReceiptId
) , 


Summary1 as (

Select b.*, 
s.*
from BaseSource b
full outer join StagingSource  s on b.RetailTransactionId=s.RetailTransactionId_Staging 
) , 

SummaryFinal as (


select  
case 
 when s.RetailTransactionId is null 
  then s.RetailTransactionId_Staging 
 when s.RetailTransactionId is not null 
  then s.RetailTransactionId
 else null end as RetailTransactionId, 
case
 when s.RetailReceiptId is null 
  then RetailReceiptId_Staging
 when s.RetailReceiptId is not null 
  then s.RetailReceiptId
 else null 
 end as RetailReceiptId, 
 case when s.RetailTransactionId is null 
  then 'IsInDynamicsStaging'
 when s.RetailTransactionId 
  is not null then 'IsInDynamics'
 else null end as StatusFlag
from Summary1 s
) ,

UpdateSummary as (

select distinct hf.RetailTransactionId, 
hf.Entity, 
sf.StatusFlag

from dw.dbo.DynamicsTransactionHeaderFacts hf
join SummaryFinal SF on SF.RetailTransactionId = hf.RetailTransactionId
where hf.BatchID is not null -- Indicates it's been exported via the Package API SSIS
--and hf.IsCurrent = 1 -- Indicates is the current transation sequence -- Removed Condition on 1/31/2023
and hf.IsInDynamics is null 

) 


select *
into ##UpdateSummary
from UpdateSummary
order by 3, 2, 1

update HF 
set hf.IsInDynamics = 1 
from dw.dbo.DynamicsTransactionHeaderFacts HF 
 join ##UpdateSummary s on s.RetailTransactionId=hf.RetailTransactionId
    and s.Entity=hf.Entity
    and s.StatusFlag = 'IsInDynamics'


update HF 
set hf.IsInDynamicsStaging = 1 
from dw.dbo.DynamicsTransactionHeaderFacts HF 
 join ##UpdateSummary s on s.RetailTransactionId=hf.RetailTransactionId
    and s.Entity=hf.Entity
    and s.StatusFlag = 'IsInDynamicsStaging'






```

### Execute SQL Task - Truncate Staging

**Path:** `Package\Sequence Container\SeqCont -  Dynamics Import Validations - Daily\Execute SQL Task - Truncate Staging`  
**Connection:** DWStaging (papamart/DWStaging)  

```sql
truncate table dbo.tmpDynamicsRetailTransaction
truncate table dbo.tmpDynamicsIntRetailTransaction

```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Source - BronzeDataLake - RetailTransaction Base Table |  | OLEDBSource | Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | BronzeDataLake | SqlCommand |
| OLE DB Source - DWStaging |  | OLEDBSource | Data Flow Task - Load Discounts - New | DWStaging | SqlCommand |
| OLE DB Source - DynamicsSalesDetailFactsStage |  | OLEDBSource | Data Flow Task - UK and IE TAx | DWStaging | SqlCommand |
| OLE DB Source - US and CA Tax - DynamicsSalesDetailFactsStage |  | OLEDBSource | Data Flow Task - US and CA Tax | DWStaging | SqlCommand |
| OLE DB Source - DW |  | OLEDBSource | Data Flow Task - Load Header | dw | SqlCommand |
| OLE DB Source - DW |  | OLEDBSource | Data Flow Task - Load Sales Detail - Sound Chip | dw | SqlCommand |
| OLE DB Source - DW Staging |  | OLEDBSource | Data Flow Task - Load Sales Detail Discounts | DWStaging | SqlCommand |
| OLE DB Source - DW |  | OLEDBSource | DF - Header (1 store) | dw | SqlCommand |
| OLE DB Source - DW |  | OLEDBSource | DF - Load Sales Detail - Sound Chip (1 store) | dw | SqlCommand |
| OLE DB Source - DynamicsSalesDetailFactsStage New |  | OLEDBSource | Data Flow Task - Load Payments | DWStaging | SqlCommand |
| OLE DB Source - AW - Sorted |  | OLEDBSource | Data Flow Task | auditworks | SqlCommand |
| OLE DB Source - DW - Eligible Lines - Sorted |  | OLEDBSource | Data Flow Task | dw |  |
| OLE DB Source  - AW - Tax Line Data |  | OLEDBSource | Data Flow Task | auditworks | SqlCommand |
| OLE DB Source - auditworks - Tender Exchange Details -  Sorted |  | OLEDBSource | Data Flow Task | auditworks | SqlCommand |
| OLE DB Source - EJ - Identify Tender Exchange Transactions - Sorted |  | OLEDBSource | Data Flow Task | EJ |  |
| OLE DB Source - DW |  | OLEDBSource | Data Flow Task | dw | SqlCommand |
| OLE DB Source -  Line and Payment Variance |  | OLEDBSource | Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | DWStaging | SqlCommand |
| OLE DB Source - Discount is Not Positive and Transaction Is Not A Return |  | OLEDBSource | Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | DWStaging | SqlCommand |
| OLE DB Source - Header and Line Discounts Mismatch |  | OLEDBSource | Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | DWStaging | SqlCommand |
| OLE DB Source - Invalid ItemId values |  | OLEDBSource | Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | DWStaging | SqlCommand |
| OLE DB Source - Item Does Not Exist in Dynamics |  | OLEDBSource | Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | DWStaging | SqlCommand |
| OLE DB Source - Sold Price is Negative |  | OLEDBSource | Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | DWStaging | SqlCommand |
| OLE DB Source - BronzeDataLake - RetailTransaction Base Table |  | OLEDBSource | Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | BronzeDataLake | SqlCommand |

#### OLE DB Source - BronzeDataLake - RetailTransaction Base Table — SqlCommand

```sql
select 
rt.transactionid as RetailTransactionId, 
rt.DataAreaId,
rt.receiptId as RetailReceiptId,
cast (rt.businessDate as date) as TransDate
from [dbo].[RetailTransactionTable] rt
where 1=1
--and cast(rt.businessDate as date) > = '2024-01-15'
and cast(rt.businessDate as date) > = ?
group by 
rt.transactionid, 
rt.DataAreaId,
rt.receiptId, 
cast (rt.businessDate as date)
```

#### OLE DB Source - DWStaging — SqlCommand

```sql
with Summary1 as (
select
case when dsd.LineAction in (2,12,15,26)
	then df.SumDiscAmount*-1
	else df.SumDiscAmount end as Amount 
	, case when dsd.LineAction in (2,12,15,26)
	then df.SumDiscAmount*-1
	else df.SumDiscAmount end as DiscountCost
	--, 'None' as DiscountOriginType -- Per Scoping Document "Will Always Be Set to None" 
	, case when df.DiscountType = 'Header' then 'Manual'
			when df.DiscountType = 'Line' then 'Periodic'
			end 
			 as DiscountOriginType
	, RetailTerminalId 
	, RetailTransactionId 
	, BABIntRetailOperatingUnitNumber 
	--, row_number() over(partition by dsd.RetailTransactionId order by dsd.LineNum ) as LineNum -- Line Number For File 
	, case when df.DiscountType = 'Header' then '1'
			when df.DiscountType = 'Line' then '2'
			end as LineNum
	--, Cast (abs(discamount/originalprice*100) as decimal (14,2)) as 'Percentage' -- Removed on 12/12/2022
	, dsd.InventLocationId as RetailStoreId 
	, dsd.LineNum as SalesLineNum  -- The Transaction Line Number we maintain in our table 
	,'None' as CustomerDiscountType -- Per Scoping Document "Will Always Be Set to None" 
	,BABIntRetailProcessed
	,Entity -- BAB Internal Field Only 
	,dsd.RetailReceiptId -- BAB Internal Feed Only 
	--, dpl.DiscountsPerLine as DiscountTransUniqueLineNum
	, row_number() over(partition by dsd.RetailTransactionId order by dsd.LineNum ) as DiscountTransUniqueLineNum -- Line Number For File 
	, case when df.DiscountType = 'Header' then 'TotalDiscountAmount'
			when df.DiscountType = 'Line' then 'None'
			end 
			as ManualDiscountType
	--, case when df.DiscountType = 'Header' then ''
	--		when df.DiscountType = 'Line' then 'Discount' -- Per ElizabethW this is to be changed from Discounts to Discount (dropping the s) 
	--		end 
	--		as  PeriodicDiscountOfferId  -- Replaced 2/28/2023 - See JIRA BIB-514
		, case when dsd.GiftCardNumber is null then 'MerchDis'
			when dsd.GiftCardNumber is not null then 'GiftCardDis' 
			end 
			as  PeriodicDiscountOfferId  -- Replaced Code above on  2/28/2023 - See JIRA BIB-514
from [DynamicsSalesDetailDiscountsFactsStage] DSD 
join [dbo].[DiscountFactsReferenceDynamicsStage] df on dsd.RetailReceiptId=df.transaction_id
													and dsd.TransactionLineSeq=df.line_sequence
--join [dbo].[vwDynamicsDiscountsPerLine] dpl on dpl.transaction_id=dsd.RetailReceiptId
--													and dpl.line_sequence = dsd.TransactionLineSeq
where dsd.discamount <> '0.00'  and dsd.OriginalPrice <> '0.00'-- We only want to send discounts when there is actually a discount 
--and RetailTransactionId = '1001-1001Int-20221206-463434431' -- Just For Testing 
--and dsd.retailreceiptid = '467484542'
) 

select Amount, 
DiscountCost, 
DiscountOriginType, 
RetailTerminalId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
row_number() over(partition by RetailTransactionId, SalesLineNum order by SalesLineNum ) as LineNum , -- Line Number per JIRA BIB -515 TASK 
RetailStoreId, 
SalesLineNum, 
CustomerDiscountType, 
BABIntRetailProcessed, 
Entity, 
RetailReceiptId, 
DiscountTransUniqueLineNum, 
ManualDiscountType, 
PeriodicDiscountOfferId
--into #TC 
from Summary1 
order by  5, 9,7


--select RetailReceiptId, SalesLineNum, count(linenum)
--from #TC
--where PeriodicDiscountOfferId = 'GiftCardDis'
--group by RetailReceiptId, SalesLineNum
--order by 3 desc
```

#### OLE DB Source - DynamicsSalesDetailFactsStage — SqlCommand

```sql
with TransactionGrouped as (
select 
cast (dsd.VatTaxAmount as decimal (14,2)) as Amount
,row_number() over(partition by RetailTransactionId order by dsd.LineNum) as LineNum
,dsd.LineNum as SaleLineNum
, null as TaxCode -- Unknown
,dsd.RetailTerminalId
,dsd.RetailTransactionId
,dsd.BABIntRetailOperatingUnitNumber
,dsd.BABIntRetailProcessed
,dsd.Entity
,dsd.RetailReceiptId
,dsd.InventLocationId

--from DynamicsSalesDetailFactsStage dsd -- Replaced on 12/9/2022
from DynamicsSalesDetailDiscountsFactsStage dsd
--join dw.dbo.TenderFactsDynamics tendf on tendf.transaction_id=dsd.RetailReceiptId and tendf.tender_key = -1
--join dw.dbo.tender_dim tendd on tendd.tender_key=tendf.tender_key
where dsd.Entity = '2110' -- UK VAT Tax is Captured Differently
--and dsd.VatTaxAmount <> 0 -- Only want Taxed Items , remarked out on 5/19/22 as we arent doing this for US 
group by dsd.VatTaxAmount
,dsd.RetailTerminalId
,dsd.RetailTransactionId
,dsd.BABIntRetailOperatingUnitNumber
,dsd.BABIntRetailProcessed
,dsd.Entity
,dsd.RetailReceiptId
,dsd.LineNum 
,dsd.InventLocationId
) 



select  cast (Amount as decimal (14,2)) as Amount, 
LineNum, 
SaleLineNum,
--cast ('Exempt' as varchar) as TaxCode, -- Per Project Meeting on 5/18/22 this needs to be hard coded to Exempt not null 
null as TaxCode, -- Per E-mail on 6/3/2022 this is to be specific to UK or Ireland, will lookup and derive in dataflow 
RetailTerminalId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
BABIntRetailProcessed, 
Entity, 
RetailReceiptId, 
InventLocationId

from TransactionGrouped tg
```

#### OLE DB Source - US and CA Tax - DynamicsSalesDetailFactsStage — SqlCommand

```sql
with TransactionGrouped as (
select 
row_number() over(partition by RetailTransactionId order by dsd.LineNum) as LineNum
,dsd.LineNum as SaleLineNum
,dsd.TransactionLineSeq 
, null as TaxCode -- Unknown
,dsd.RetailTerminalId
,dsd.RetailTransactionId
,dsd.BABIntRetailOperatingUnitNumber
,dsd.BABIntRetailProcessed
,dsd.Entity
,dsd.RetailReceiptId
,dsd.Price
,dsd.LineAction 
--from DynamicsSalesDetailFactsStage dsd -- Replaced on 12/9/2022
from DynamicsSalesDetailDiscountsFactsStage dsd
where dsd.Entity <> '2110' -- UK VAT Tax is Captured Differently
--and RetailTransactionId in ('1063-1063Int-20220402-449077715') -- Testing Purposes Only 
--and  dsd.RetailReceiptId = '445900300' -- Testing Purposes 
group by dsd.RetailTerminalId
,dsd.RetailTransactionId
,dsd.BABIntRetailOperatingUnitNumber
,dsd.BABIntRetailProcessed
,dsd.Entity
,dsd.RetailReceiptId
,dsd.LineNum 
,dsd.Price
,dsd.TransactionLineSeq
,dsd.LineAction 
), 

TaxDetail as (


select cast( transaction_id as varchar) as RetailReceiptId, 
line_sequence, 
cast (dbo.BankersRound(tax_amount_expected ,2)as decimal (14,2)) as TaxAmount,
case when tax_amount_expected = 0.000
	then 0.0000
	else combined_rate end as TaxRate
--from TransactionTaxFactsDynamicsStage -- Table I was loading until Dan Loaded new DW table , Replaced on 4/5/2022
from DW.dbo.TransactionTaxDynamicsStage -- Loaded by Dan's ETL 
where line_object <> '106' -- ES Lines


), Summary1 as (

select  
case when tg.LineAction in ('2','12') -- 2 = returned, 12 = Refunded 
	then isnull(td.TaxAmount,0.00)*-1
	else isnull(td.TaxAmount,0.00)
	end 
	as Amount ,
--case when tg.LineAction = '2' --returned
--	then ((td.TaxRate*tg.Price)*-1) /100
--	else (td.TaxRate*tg.Price)/100
--	end 
--	as Amount , -- This would be using the tax rate & the item price to get the tax, not ideal 
tg.LineNum, 
tg.SaleLineNum,
tg.TaxCode, 
tg.RetailTerminalId, 
tg.RetailTransactionId, 
tg.BABIntRetailOperatingUnitNumber, 
tg.BABIntRetailProcessed, 
tg.Entity, 
tg.RetailReceiptId
--,td.TaxRate
--, tg.Price
from TransactionGrouped TG
left join TaxDetail TD on tg.RetailReceiptId=td.RetailReceiptId
	and tg.TransactionLineSeq=td.line_sequence


), 
Summary2 as (

Select 
cast (dbo.BankersRound(isnull(Amount,0.00),2)as decimal (14,2)) as Amount,
LineNum, 
SaleLineNum, 
TaxCode, 
RetailTerminalId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
BABIntRetailProcessed, 
Entity, 
RetailReceiptId
--, isnull(TaxRate,0.00) as TaxRate 

from Summary1
)

select Sum(Amount) as Amount,
LineNum, 
SaleLineNum, 
--cast ('Exempt' as varchar) as TaxCode, -- Per Project Meeting on 5/18/22 this needs to be hard coded to Exempt not null , replaced 12/9/2022
cast ('INT' as varchar) as TaxCode,
RetailTerminalId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
BABIntRetailProcessed, 
Entity, 
RetailReceiptId

from Summary2
group by LineNum, 
SaleLineNum, 
TaxCode, 
RetailTerminalId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
BABIntRetailProcessed, 
Entity, 
RetailReceiptId
```

#### OLE DB Source - DW — SqlCommand

```sql
select 	cast (tdf.register_num  as varchar) as RetailTerminalId_Incomplete
	,null as CustAccount
	,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.transaction_id as RetailReceiptId
	,tdf.cashier_id as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
	,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
	,cast(dd.actual_date  as date) TransDate 
	, 'Sales' as RetailTransactionType
	, null as BABIntRetailProcessed	
	, isnull(ds.SumTransDiscounts,0.00) as DiscAmount
	, isnull(ds.SumTransHeaderDiscounts,0.00) as TotalDiscAmount
from TransactionDetailFactsDynamics TDF (nolock) 
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock) on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on tdf.date_key=dd.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header due to ES Orders and how that is handled in detail lines 
	left join dwstaging.[dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=tdf.transaction_id
where sd.store_id not in ('13','2013')
and sd.store_id in ('0001','0016','0026','0064','0066','0094','0104','0105','0125','0138','0156','0168','0175','0200','0239','0244','0256','0257','0295','0337','0345','0404','0415','0521','2006','2036','2063') -- Pilot Stores List Modified 9/01/2022
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,203,204,292,799,701,710,711,714)

	
		) -- Misc Fee and Donation lines 

	or ( lod.Line_Object in (200)

		) -- Shipping Fee Lines

	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
--and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
and tdf.transaction_id in ('445577369','446173433','448697587','445620771')
group by 

	cast (tdf.register_num  as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tdf.transaction_id
	,tdf.cashier_id
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)
	,isnull(ds.SumTransDiscounts,0.00)
	,isnull(ds.SumTransHeaderDiscounts,0.00)
union 
select cast(tef.register_no as varchar) as RetailTerminalId_Incomplete
,null as CustAccount
,right('0000'+cast(sd.store_id as varchar),4) as LocationCode  -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
, case when sd.country = 'IE' then 'UK'
	else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
,tef.transaction_id
,tef.cashier_no as RetailStaffId -- Cashier ID is the POS transaction cashier number, we dont need to look up to the cashier dim 
, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete --Updated Feb 11 After Feedback from BHS
,right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber 
,cast(dd.actual_date  as date) TransDate 
, 'Sales' as RetailTransactionType
, null as BABIntRetailProcessed	
, 0.00 as DiscAmount
, 0.00 as TotalDiscAmount
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where (tef.line_object in ('633','404')and line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13','2013')
and sd.store_id in ('0001','0016','0026','0064','0066','0094','0104','0105','0125','0138','0156','0168','0175','0200','0239','0244','0256','0257','0295','0337','0345','0404','0415','0521','2006','2036','2063') -- Pilot Stores List Modified 9/01/2022
and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
and tef.transaction_id in ('445577369','446173433','448697587','445620771')
group by 
	cast (tef.register_no as varchar)
	,right('0000'+cast(sd.store_id as varchar),4)
	,sd.country 
	,tef.transaction_id
	,tef.cashier_no
	,'-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar)
	,right('0000'+cast(sd.store_id as varchar),4) 
	,cast(dd.actual_date  as date)

order by 9, 3, 5
```

#### OLE DB Source - DW — SqlCommand

```sql
with DynamicsFeeMapping as (
select '000014' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000015' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000016' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000017' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '000025' as 'SKU' , cast ('SV000025' as varchar (30))  as 'DynamicsItemId' union 
select '000032' as 'SKU' , cast ('SV000032' as varchar (30))  as 'DynamicsItemId' union 
select '018079' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '018084' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '022610' as 'SKU' , cast ('SV022610' as varchar (30))  as 'DynamicsItemId' union 
select '028144' as 'SKU' , cast ('SV028144' as varchar (30))  as 'DynamicsItemId' union 
select '080731' as 'SKU' , cast ('SV080731' as varchar (30))  as 'DynamicsItemId' union 
select '091450' as 'SKU' , cast ('SV091450' as varchar (30))  as 'DynamicsItemId' union 
select '098041' as 'SKU' , cast ('SV098041' as varchar (30))  as 'DynamicsItemId' union 
select '098044' as 'SKU' , cast ('SV098044' as varchar (30))  as 'DynamicsItemId' union 
select '098075' as 'SKU' , cast ('SV098075' as varchar (30))  as 'DynamicsItemId' union 
select '098088' as 'SKU' , cast ('SV098088' as varchar (30))  as 'DynamicsItemId' union 
select '198075' as 'SKU' , cast ('SV198075' as varchar (30))  as 'DynamicsItemId' union 
select '400003' as 'SKU' , cast ('SV400003' as varchar (30))  as 'DynamicsItemId' union 
select '480200' as 'SKU' , cast ('SV480200' as varchar (30))  as 'DynamicsItemId' union 
select '491450' as 'SKU' , cast ('SV491450' as varchar (30))  as 'DynamicsItemId' union 
select '491451' as 'SKU' , cast ('SV491451' as varchar (30))  as 'DynamicsItemId' union 
select '498033' as 'SKU' , cast ('SV498033' as varchar (30))  as 'DynamicsItemId' union 
select '498041' as 'SKU' , cast ('SV498041' as varchar (30))  as 'DynamicsItemId' union 
select '498088' as 'SKU' , cast ('SV498088' as varchar (30))  as 'DynamicsItemId' union
select '000024'	as 'SKU' , cast ('SV000024' as varchar (30))  as 'DynamicsItemId' union 
select '000026'	as 'SKU' , cast ('SV000026' as varchar (30))  as 'DynamicsItemId' union 
select '000027'	as 'SKU' , cast ('SV000027' as varchar (30))  as 'DynamicsItemId' union 
select '000029'	as 'SKU' , cast ('SV000029' as varchar (30))  as 'DynamicsItemId' union 
select '000035'	as 'SKU' , cast ('SV000035' as varchar (30))  as 'DynamicsItemId' union 
select '000042'	as 'SKU' , cast ('SV000042' as varchar (30))  as 'DynamicsItemId' union 
select '000044'	as 'SKU' , cast ('SV000044' as varchar (30))  as 'DynamicsItemId' union 
select '000077'	as 'SKU' , cast ('SV000077' as varchar (30))  as 'DynamicsItemId' union 
select '000078'	as 'SKU' , cast ('SV000078' as varchar (30))  as 'DynamicsItemId' union 
select '000081'	as 'SKU' , cast ('SV000081' as varchar (30))  as 'DynamicsItemId' union 
select '000082'	as 'SKU' , cast ('SV000082' as varchar (30))  as 'DynamicsItemId' union 
select '080726'	as 'SKU' , cast ('SV080726' as varchar (30))  as 'DynamicsItemId' union 
select '080727'	as 'SKU' , cast ('SV080727' as varchar (30))  as 'DynamicsItemId' union 
select '080728'	as 'SKU' , cast ('SV080728' as varchar (30))  as 'DynamicsItemId' union 
select '080729'	as 'SKU' , cast ('SV080729' as varchar (30))  as 'DynamicsItemId' union 
select '080730'	as 'SKU' , cast ('SV080730' as varchar (30))  as 'DynamicsItemId' union 
select '080733'	as 'SKU' , cast ('SV080733' as varchar (30))  as 'DynamicsItemId' union 
select '080736'	as 'SKU' , cast ('SV080736' as varchar (30))  as 'DynamicsItemId' union 
select '080738'	as 'SKU' , cast ('SV080738' as varchar (30))  as 'DynamicsItemId' union 
select '080741'	as 'SKU' , cast ('SV080741' as varchar (30))  as 'DynamicsItemId' union 
select '098042'	as 'SKU' , cast ('SV098042' as varchar (30))  as 'DynamicsItemId' union 
select '098043'	as 'SKU' , cast ('SV098043' as varchar (30))  as 'DynamicsItemId' union 
select '480731'	as 'SKU' , cast ('SV480731' as varchar (30))  as 'DynamicsItemId' 



)

select  

	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tdf.[transaction_line_seq] 
	, row_number() over(partition by tdf.transaction_id order by tdf.transaction_line_seq ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast( abs(tdf.unit_gross_amount)*-1 as decimal (14,2))
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast( tdf.unit_gross_amount as decimal (14,2))
			when pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))
			when pd.product_key in ('-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding or Paid Out cost incurred 
				then cast( tdf.unit_gross_amount/tdf.units*-1 as decimal (14,2))			
			else cast(tdf.unit_gross_amount/tdf.units as decimal (14,2))
		end as OriginalPrice -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit.
	, case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation 
				then cast(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2))  
			when  pd.product_key <> '-16' and lad.Line_Action in (2,12) -- Returned/Refunded Items 
				then  cast(((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units)*-1 as decimal (14,2)) 
			when pd.product_key in ( '-799','-701','-710','-711','-714') and lad.Line_Action in (15) -- Nickel Rounding cost or Paid Out incurred 
				then cast(abs(tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))*-1 as decimal (14,2)) 
			else cast((tdf.unit_gross_amount-(tdf.unit_disc_amount-tdf.upsell_disc_allocated))/tdf.units as decimal (14,2)) 
		end as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	,case	when pd.product_key = '-16' and lad.Line_Action in (2,12) -- Merchandise Contribution aka Donation, Returned/Refunded 
				then cast (-1 as int) -- Hardcoding Donation Items to Qty 1 
			when pd.product_key = '-16' and lad.Line_Action not in (2,12) -- Merchandise Contribution aka Donation
				then cast (1 as int) -- Hardcoding Donation Items to Qty 1
			else cast(tdf.units as int) 
		end as Qty -- Modified on 5/3/2022 as we found not only 0 qty for some donations but also multiple quantities which was throwing off Dynamics gross vs payment amount 
	, tdf.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tdf.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tdf.register_num as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, case	when lod.Line_Object in ('204','205','292') -- Miscellaneous Fee, NSF Fee, Merchandise Contribution				
				then cast (isnull(dfm.DynamicsItemId,'SV00010') as varchar (50)) -- 5/2/2022: using MiscFee Service Item if no lookup found
			when lod.Line_Object in ('202') -- EmbroideryFees
				then cast ('SV022610' as varchar) -- Dynamics Service Item: Embroidery 
			when lod.Line_Object in ('200','203') -- Shipping Fees
				then cast ('SV00001' as varchar) -- Dynamics Service Item: Shipping 
			when lod.Line_Object in ('799') -- NickelRounding
				then cast ('SV00011' as varchar) -- Dynamics Service Item: Nickel Rounding
			when lod.Line_Object in (701,710,711,714)
				then cast ('SV00012' as varchar) -- Dynamics Service Item: Paid In and Paid Out
		else cast(pd.style_code as varchar) end  as ItemId -- special mapping for fees and donations before Elizabeth Details
	, cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) as LineDiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when pd.product_key = '-16' -- Merchandise Contribution aka Donation
		then cast(abs(tdf.unit_disc_amount-tdf.upsell_disc_allocated) as decimal (14,2)) -- We are handling Donations as a single unit and in theory they should not have discounts 
		else  cast(abs((tdf.unit_disc_amount-tdf.upsell_disc_allocated)/tdf.units) as decimal (14,2)) -- 5/3/2022:  Per Josh Miller of BHS this is to be calculated as per unit 
		end as DiscAmount -- In our DW we map discounted gift card tenders to tdf.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, case when lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625) then tdf.reference_no
		else null end as GiftCardNumber
	, null as BABIntRetailProcessed
	, tdf.vat_tax_amount as VatTaxAmount -- We will need this later for the Tax Files as there is no tax line objects in our extracted AW data for UK transactions 
	, cd.currency_code as CurrencyCode -- We Will need this later for the payments 
	, lod.Line_Object as LineObject -- BAB Internal Use 
	, lad.Line_Action as LineAction -- BAB Internal Use 
from TransactionDetailFactsDynamics (nolock) tdf
	join TransactionFactsDynamics TF (nolock) on tf.transaction_id=tdf.transaction_id
	left join line_object_dim lod (nolock) on tdf.line_object_key=lod.Line_Object_Key
	left join Line_Action_Dim lad (nolock)  on tdf.line_action_key=lad.Line_Action_Key
	join date_dim dd (nolock) on dd.date_key=tdf.date_key
	join product_dim pd (nolock) on tdf.product_key=pd.product_key
	left join DynamicsFeeMapping DFM on DFM.SKU=tdf.reference_no
		and lod.Line_Object in ('202','204','205','292') 
	join store_dim sd (nolock) on sd.store_key=tf.store_key -- Want to Join to Header for Location information due to how ES orders at handled in details
	join currency_dim cd (nolock) on cd.currency_key=tdf.currency_key
where sd.store_id not in ('13','2013')
and sd.store_id in ('0001','0016','0026','0064','0066','0094','0104','0105','0125','0138','0156','0168','0175','0200','0239','0244','0256','0257','0295','0337','0345','0404','0415','0521','2006','2036','2063') -- Pilot Stores List Modified 9/01/2022
and	(
		( 
			lod.Line_Object IN (100, 102, 103, 104, 115) 
			--AND RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01')  -- These are bag fees, probably do not want to exclude - 3/25/2022
		)-- Merchandise Transaction Lines
	or (
			lod.line_object in (101,105,202,204,292,799,701,710,711,714)
			
		) -- Misc Fee and Donation lines  
	or ( lod.Line_Object in (200,203)

		) -- Shipping Fee Lines
	or 
		(	
			lod.Line_Object IN (294, 400, 401, 402, 403, 404, 410, 1625)
		)-- Gift Card Transaction  Lines 
	--or
	--	(
	--		lod.line_object = 106  -- This is Order Merchandise 
	--			--and (lad.line_action in (90,142,99) -- These are Order Delivered, Delivery Returned, Order Pickedup 
	--			and (lad.line_action in (7,8) -- These are  Ordered, Order Cancelled 
	--		--and RIGHT(pd.subclass_code, 8) NOT IN ('57-01-01') -- These Are Bag Fees - Probably do not want to exclude 3/25/2022
	--	) -- ES Order Fulfillment  Lines 

	--	)-- Removed ES Order Lines on 3/28/2022 after discussion with DanT - ES Orders are fulfiled by the web, so Ben's process would generate SO for those lines
	)	
and not exists (select es.transaction_id from dw.dbo.tmpESRef_  es where es.transaction_id=tdf.transaction_id)
--and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
and tdf.transaction_id in ('445577369','446173433','448697587','445620771')
union 
select 
	 null as CustAccount
	, right('0000'+cast(sd.store_id as varchar),4) as LocationCode -- We will use this to lookup the InventLocationID field ie the Dynamics Store Number 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end as Country -- This is for us to perform a lookup to entity for the Dynamics store number, Ireland stores are in UK entity in Dynamics 
	,tef.line_sequence as [transaction_line_seq] 
	, row_number() over(partition by tef.transaction_id order by tef.line_sequence ) as LineNum -- Our approach is to derive our own line number using a windowing function
	, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as OriginalPrice 
	, sum(tef.gross_line_amount-tef.pos_discount_amount)*-1 as Price -- 5/3/2022: Per Josh Miller of BHS this is to be calculated as per unit. Previous Note: In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, -1 as  Qty -- **NEED TO THINK ON THIS **
	, tef.transaction_id as RetailReceiptId 	
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) as RetailTransactionId_Incomplete -- Updated on Feb 11 after feedback from BHS
	, right('0000'+cast(sd.store_id as varchar),4) as BABIntRetailOperatingUnitNumber  
	,'-'+ cast(tef.register_no as varchar) as RetailTerminalId_Incomplete -- Need Leading Dynamics Store Number
	, cast(dd.actual_date  as date) TransDate
	, null as ItemId -- Likely will need to be a lookup 
	, 0.00 as LineDiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, 0.00 DiscAmount -- In our DW we map discounted gift card tenders to tef.unit_disc_amount and  upsell_disc_allocated, we must subtract the upsell_disc_allocated to properly capture the discount for Dynamics
	, cast (tef.reference_no as varchar(80)) as GiftCardNumber
	, null as BABIntRetailProcessed
	, 0.00 as VatTaxAmount -- Gift Cards Are not Taxed , its a store of value 
	, cast(tef.currency_code as varchar(3)) as CurrencyCode -- We Will need this later for the payments 
	, tef.Line_Object as LineObject -- BAB Internal Use 
	, tef.Line_Action as LineAction -- BAB Internal Use 
from DynamicsTenderExchangeFacts TEF (nolock) 
join store_dim sd (nolock) on sd.store_key=tef.store_key
join date_dim dd (nolock) on tef.date_key=dd.date_key
where (tef.line_object in ('633','404')and tef.line_action in ('2','26')) -- These are the returned objects and actions 
and sd.store_id not in ('13','2013')
and sd.store_id in ('0001','0016','0026','0064','0066','0094','0104','0105','0125','0138','0156','0168','0175','0200','0239','0244','0256','0257','0295','0337','0345','0404','0415','0521','2006','2036','2063') -- Pilot Stores List Modified 9/01/2022
--and DATEDIFF(dd,dd.actual_date,getdate()) <= 7
and tef.transaction_id in ('445577369','446173433','448697587','445620771')
group by 
	 right('0000'+cast(sd.store_id as varchar),4) 
	, case when sd.country = 'IE' 
			then 'UK'
		else sd.country end
	,tef.line_sequence 
	, tef.transaction_id 
	, '-' + convert(varchar,dd.actual_date, 112) + '-' + cast(tef.transaction_id as varchar) 
	, right('0000'+cast(sd.store_id as varchar),4) 
	,'-'+ cast(tef.register_no as varchar) 
	, cast(dd.actual_date  as date) 	
	, cast (tef.reference_no as varchar(80))	
	, cast(tef.currency_code as varchar(3)) 
	, tef.Line_Object 
	, tef.Line_Action 

--order by 12, 
--2, 
--3

order by 9
```

#### OLE DB Source - DW Staging — SqlCommand

```sql
with Summary1 as (
select
CustAccount, 
InventLocationId, 
TransactionLineSeq, 
LineNum, 
--OriginalPrice, -- Replaced 1/19/2023 with logic below - This is when stores use price MARKDOWN to increase the price of the item 
--case when Price > OriginalPrice then Price else OriginalPrice end  as OriginalPrice,  -- Replaced  with below 3/29/2023
case when sd.LineAction in (2,12) then OriginalPrice when Price > OriginalPrice then Price else OriginalPrice end  as OriginalPrice,

--Price, 
--OriginalPrice as Price,  -- Per Updated FDD Both Price and Original Price are sourced from Original Price 
--case when Price > OriginalPrice then Price else OriginalPrice end  as Price,  -- Replaced 1/19/2023 with logic below - This is when stores use price MARKDOWN to increase the price of the item -- Replaced  with below 3/29/2023
case when sd.LineAction in (2,12) then OriginalPrice when Price > OriginalPrice then Price else OriginalPrice end  as Price,
Qty, 
RetailReceiptId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
RetailTerminalId, 
TransDate, 
ItemId, 
--LineDscAmount, 
cast (abs(isnull(df.SumDiscAmount,0.00)) as numeric (14,2)) as LineDscAmount,  -- Per  Updated FDD LineDscAmount online should be Linve Level Discount Only 
--case when ds.SumTransHeaderDiscounts = 0.00	then 0.00	else sd.DiscAmount end as DiscAmount,
isnull(dfh.SumDiscAmount,0.00) as DiscAmount,
GiftCardNumber, 
BABIntRetailProcessed, 
VatTaxAmount, 
CurrencyCode, 
Entity, 
LineObject, 
sd.LineAction, 
BlankSoundChipItemId,
--ds.SumTransDiscounts, 
--ds.SumTransHeaderDiscounts, 
--ds.SumTransLineDiscounts, 
--dpl.DiscountsPerLine, 
--df.SumDiscAmount as DiscountAmount, 
--df.line_object_description,
cast (
	case when sd.OriginalPrice = 0.00
		then 0.0000
		else 
		abs(
			isnull(	df.SumDiscAmount/sd.OriginalPrice,0.00)
			) 
		end 
			as numeric (14,3)
	 ) 
as PeriodicPercentageDiscount, -- Per FDD Line Discount Amount / Original Price 
--cast (sd.DiscAmount-isnull(df.SumDiscAmount,0.00) as numeric (14,2)) as TotalDiscAmount, -- Aka Partial Header Discount -- Replaced with below 
--cast ((sd.DiscAmount*sd.Qty)-isnull(df.SumDiscAmount,0.00) as numeric (14,2)) as TotalDiscAmount, -- Aka Partial Header Discount -- Added Qty Multiplication on 3/23/2023
isnull(dfh.SumDiscAmount,0.00) as TotalDiscAmount,
cast (case when ds.SumTransHeaderDiscounts = 0.00
	then 0.000
	else 
	abs(
		 --((sd.DiscAmount-isnull(df.SumDiscAmount,0.00)) / ds.SumTransHeaderDiscounts ) -- Replaced with below 
		 --((sd.DiscAmount*sd.Qty-isnull(df.SumDiscAmount,0.00)) / ds.SumTransHeaderDiscounts ) -- Added Qty Multiplication on 3/24/2023
		 ((sd.DiscAmount*sd.Qty-isnull(df.SumDiscAmount,0.00)) / ds.SumTransHeaderDiscountsAbsolute ) -- Replaced above on 3/30/203 -- Due REturn Discounts we have to calcuate the absolute value of discounts 
		)
	end 
	as numeric (14,3) )
as TotalDiscPct
from [dbo].[DynamicsSalesDetailFactsStage] (nolock) sd
--left join [dbo].[DiscountFactsReferenceDynamicsStage] df on sd.RetailReceiptId=df.transaction_id
left join [dbo].[vwDiscountFactsReferenceDynamicsHeader] df on sd.RetailReceiptId=df.transaction_id
										and sd.TransactionLineSeq=df.line_sequence
										and df.DiscountType = 'Line'
--left join [dbo].[DiscountFactsReferenceDynamicsStage] dfh on sd.RetailReceiptId=dfh.transaction_id
left join [dbo].[vwDiscountFactsReferenceDynamicsHeader] dfh on sd.RetailReceiptId=dfh.transaction_id
										and sd.TransactionLineSeq=dfh.line_sequence
										and dfh.DiscountType = 'Header'
left join [dbo].[vwDynamicsDiscountsSum] ds on ds.transaction_id=sd.RetailReceiptId
--left join [dbo].[vwDynamicsDiscountsPerLine] dpl on dpl.transaction_id=sd.RetailReceiptId
--	and dpl.line_sequence = sd.TransactionLineSeq
--where sd.RetailReceiptId in ('467139167')  -- Thi is a sale and looks good 
--where sd.RetailReceiptId in ('467484542') -- This a return and sale combo  and looks good 
--where sd.RetailReceiptId in ('467384373') -- This a return only  and looks good 
--where sd.RetailReceiptID in ('467296686') -- This is a return only and looks good 
--where sd.RetailReceiptId in ('467158032')
--where sd.RetailReceiptId = '467543204' 
--where sd.RetailReceiptId = '470373911' -- Duplicate Sales LIne 2 example
--where ds.SumTransHeaderDiscounts <> 0.00
--order by sd.Entity, sd.RetailTransactionId, sd.LineNum
), 

Summary2  as 
(


select 
CustAccount, 
InventLocationId, 
TransactionLineSeq, 
LineNum, 
OriginalPrice, 
Price, 
Qty, 
RetailReceiptId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
RetailTerminalId, 
TransDate, 
ItemId, 
LineDscAmount, 
--case when LineAction in (2,12,15,26)	then (LineDscAmount + DiscAmount)	else (LineDscAmount + DiscAmount) 	end as DiscAmount, 
 (LineDscAmount + DiscAmount) 	 as DiscAmount, 
GiftCardNumber, 
BABIntRetailProcessed, 
VatTaxAmount, 
CurrencyCode, 
Entity, 
LineObject, 
LineAction, 
BlankSoundChipItemId, 
cast (
	case when OriginalPrice = 0.00
		then 0.0000
		else 
		abs(
			isnull(	LineDscAmount/(OriginalPrice*Qty),0.00)
			) 
		end 
			as numeric (14,3)
	 ) 
as PeriodicPercentageDiscount, -- Per FDD Line Discount Amount / Original Price 
case when LineAction in (2,12,15,26) then TotalDiscAmount*-1 else TotalDiscAmount end as TotalDiscAmount, 
TotalDiscPct

from Summary1

)

--select * 
--from Summary2


select CustAccount, 
InventLocationId, 
TransactionLineSeq, 
LineNum, 
OriginalPrice, 
Price, 
--Qty, 
case when LineAction not in (2,12,15,26) -- If its not a return it should be negatve 
	then abs(qty)*-1
	else abs(qty)  -- If it is a return it should be positive 
	end as Qty,
RetailReceiptId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
RetailTerminalId, 
TransDate, 
--ItemId, 
cast (replace(ItemId, ' ','') as varchar (50)) as ItemId, -- Replaced Above on 2/12/2024 to remove any spaces from the Item Id field
--case when LineAction in (2,12,15,26) then 0.00	else sum(LineDscAmount) end as LineDscAmount, -- Per FDD Updates Effective Jan 17 2023
--sum(LineDscAmount) as LineDscAmount, -- 3/30/2023 - We now included return discounts 
case when LineAction in (2,12,15,26)
	then sum(LineDscAmount*-1)
	else sum(LineDscAmount)
	end as LIneDscAmount,
--case when LineAction in (2,12,15,26)then 0.00	else DiscAmount end as DiscAmount, 
case when LineAction in (2,12,15,26)
	then DiscAmount*-1
	else 
	DiscAmount 
End as DiscAmount, 
GiftCardNumber, 
BABIntRetailProcessed, 
VatTaxAmount, 
CurrencyCode, 
Entity, 
LineObject, 
LineAction, 
BlankSoundChipItemId, 
sum(PeriodicPercentageDiscount) as PeriodicPercentageDiscount,
sum(TotalDiscAmount) as TotalDiscAmount, 
sum (TotalDiscPct) as TotalDiscPct  

from Summary2
--where RetailReceiptId = '465678056'
--where LineAction  in (2,12,15,26) -- Known Return Line Lactions
group by 
CustAccount, 
InventLocationId, 
TransactionLineSeq, 
LineNum, 
OriginalPrice, 
Price, 
Qty, 
RetailReceiptId, 
RetailTransactionId, 
BABIntRetailOperatingUnitNumber, 
RetailTerminalId, 
TransDate, 
--ItemId, 
cast (replace(ItemId, ' ','') as varchar (50)) , -- Replaced Above on 2/12/2024 to remove any spaces from the Item Id field
--LineDscAmount, 
DiscAmount, 
GiftCardNumber, 
BABIntRetailProcessed, 
VatTaxAmount, 
CurrencyCode, 
Entity, 
LineObject, 
LineAction, 
BlankSoundChipItemId,
--PeriodicPercentageDiscount,
TotalDiscAmount
--TotalDiscPct

order by 9,4
```

#### OLE DB Source - DynamicsSalesDetailFactsStage New — SqlCommand

```sql
with

DynamicsDiscountFactsStageCTE as (
	select RetailReceiptId, SaleLineNum, sum(Amount) as Amount
	from DynamicsDiscountFactsStage
	--where RetailReceiptId = '463385215'
	group by RetailReceiptId, SaleLineNum
) ,

TenderExchangePayments as (
select transaction_id, line_object, line_object_description, line_action, line_action_display_descr, tender_key, sum(gross_line_amount) as Amount
from dw.dbo.DynamicsTenderExchangeFacts tef
--where tef.line_action not in (2,12,15,26) -- We are basically saying exclude the rows that were returns\credit lines that were included in the sales detail 
where tef.line_action not in (2,15,26) -- Removed 12 on 3/7/2023
group by transaction_id, line_object,line_object_description, line_action, line_action_display_descr, tender_key

) , 

TransactionGrouped as (
select 
	--	case when dsd.LineAction in (2,12,15,26) -- Return Lines
	--			and (dfs.Amount < 0 or dfs.Amount is null )
	--		 then ((dsd.OriginalPrice*abs(dsd.qty))-isnull(dfs.Amount,0.00))*-1
	--		when dsd.LineAction in (2,12,15,26) -- Return Lines
	--			and dfs.Amount >  0
	--		then ((dsd.OriginalPrice*abs(dsd.qty))-dsd.DiscAmount)*-1
	--	else  (dsd.OriginalPrice*abs(dsd.qty))-(dsd.DiscAmount*abs(dsd.qty))
	--end as Price 
	--(dsd.OriginalPrice*abs(dsd.qty))-(dsd.DiscAmount*abs(dsd.qty)) as Price -- Replaced above on Jan 18 2023
	(dsd.OriginalPrice*abs(dsd.qty))-(dsd.DiscAmount) as Price -- Replaced above on March 30 2023
	, dtfs.Amount as TaxAmount
	, tendf.TenderPercentage
	,cast (tt.CardTypeId as varchar (10)) as RetailCardTypeId
	,dsd.RetailReceiptId	
	,dsd.RetailTransactionId
	,cast(tt.PaymentMethodNumber as varchar (18)) as RetailTenderTypeId	
	, dsd.RetailTerminalId
	, dsd.BABIntRetailOperatingUnitNumber
	, dsd.TransDate
	, null as AccountNum
	, null as RetailCardNum
	, 'No' as ChangeLine -- What is this? 
	, null as PaymentAuthorization 
	,dsd.currencycode as CurrencyCode
	,dsd.BABIntRetailProcessed
	,dsd.Entity
from DynamicsSalesDetailDiscountsFactsStage dsd
left join [TenderPercentageFactsDynamicsStage] tendf on tendf.transaction_id=dsd.RetailReceiptId and tendf.tender_key <> -1
left join dw.dbo.tender_dim tendd on tendd.tender_key=tendf.tender_key
left join TenderExchangePayments TEP on tep.transaction_id =dsd.RetailReceiptId
left join DynamicsTendersCardTypes tt on tt.TenderCode=tendd.tender_code
left join dw.dbo.TransactionFactsDynamics  TFD (Nolock) on tfd.transaction_id=dsd.RetailReceiptId
left join DynamicsTaxFactsStage DTFS on dtfs.RetailReceiptId = dsd.RetailReceiptId
						and dtfs.LineNum = dsd.LineNum
left join DynamicsDiscountFactsStageCTE dfs on dfs.RetailReceiptId=dsd.RetailReceiptId
											and dfs.SaleLineNum=dsd.linenum
--where dsd.RetailReceiptId = '465517334' -- Testing Purposes 
where tep.transaction_id is null 
union all
select 
	  --dsd.Price as Price -- 
	  	 case when dsd.LineAction in (2,12,15,26) -- Return Lines
	 then (dsd.OriginalPrice - dsd.DiscAmount)
	 else dsd.Price end as Price -- Replaced above on April 3 2023
	, dtfs.Amount as TaxAmount
	, null as TenderPercentage
	,cast (tt.CardTypeId as varchar (10)) as RetailCardTypeId
	,dsd.RetailReceiptId	
	,dsd.RetailTransactionId
	,cast(tt.PaymentMethodNumber as varchar (18)) as RetailTenderTypeId	
	, dsd.RetailTerminalId
	, dsd.BABIntRetailOperatingUnitNumber
	, dsd.TransDate
	, null as AccountNum
	, null as RetailCardNum
	, 'No' as ChangeLine -- What is this? 
	, null as PaymentAuthorization 
	,dsd.currencycode as CurrencyCode
	,dsd.BABIntRetailProcessed
	,dsd.Entity
	
from DynamicsSalesDetailDiscountsFactsStage dsd
join TenderExchangePayments TEP on tep.transaction_id =dsd.RetailReceiptId
--left join [TenderPercentageFactsDynamicsStage] tendf on tendf.transaction_id=dsd.RetailReceiptId and tendf.tender_key <> -1 -- Remarked out on 3/7/2023 we do not need this lookup for the tender exchange transactions
join dw.dbo.tender_dim tendd on tendd.tender_key=tep.tender_key
left join DynamicsTendersCardTypes tt on tt.TenderCode=tendd.tender_code
left join dw.dbo.TransactionFactsDynamics  TFD (Nolock) on tfd.transaction_id=dsd.RetailReceiptId
left join DynamicsTaxFactsStage DTFS on dtfs.RetailReceiptId = dsd.RetailReceiptId
						and dtfs.LineNum = dsd.LineNum
left join DynamicsDiscountFactsStageCTE dfs on dfs.RetailReceiptId=dsd.RetailReceiptId
											and dfs.SaleLineNum=dsd.linenum
--where dsd.RetailReceiptId = '465517334' -- Testing Purposes 


) 

, 
Summary1 as (

select sum (Price) as SumPrice ,
sum(TaxAmount) as SumTax,
TenderPercentage, 
RetailCardTypeId, 
RetailReceiptId, 
row_number() over(partition by RetailTransactionId order by RetailTenderTypeId) as LineNum,
RetailTransactionId, 
RetailTenderTypeId, 
RetailTerminalId, 
BABIntRetailOperatingUnitNumber, 
TransDate, 
AccountNum, 
RetailCardNum, 
ChangeLine, 
PaymentAuthorization, 
CurrencyCode, 
BABIntRetailProcessed, 
Entity

from TransactionGrouped
group by 
TenderPercentage, 
RetailCardTypeId, 
RetailReceiptId, 
RetailTransactionId, 
RetailTenderTypeId, 
RetailTerminalId, 
BABIntRetailOperatingUnitNumber, 
TransDate, 
AccountNum, 
RetailCardNum, 
ChangeLine, 
PaymentAuthorization, 
CurrencyCode, 
BABIntRetailProcessed, 
Entity
) 



select  
cast (dbo.BankersRound(	(isnull(SumPrice,0.00)+isnull(SumTax,0.00))*(isnull(TenderPercentage,1)),2) as decimal (14,2)) as AmountCur, 
cast (dbo.BankersRound(	(isnull(SumPrice,0.00)+isnull(SumTax,0.00))*(isnull(TenderPercentage,1)),2) as decimal (14,2)) as AmountMst,
cast (dbo.BankersRound(	(isnull(SumPrice,0.00)+isnull(SumTax,0.00))*(isnull(TenderPercentage,1)),2) as decimal (14,2)) as RetailAmountTendered,
RetailCardTypeId, 
RetailReceiptId, 
LineNum, 
RetailTransactionId, 
isnull(RetailTenderTypeId,600) as RetailTenderTypeId,  -- Cash 
RetailTerminalId, 
BABIntRetailOperatingUnitNumber, 
TransDate, 
AccountNum, 
RetailCardNum, 
ChangeLine, 
PaymentAuthorization, 
CurrencyCode, 
BABIntRetailProcessed, 
Entity

from Summary1
--where RetailReceiptId = '465816584'
--where RetailReceiptId in ('465517334','465974008','465816584')
order by RetailReceiptId, LIneNum
```

#### OLE DB Source - AW - Sorted — SqlCommand

```sql
with LO as (

select lo.line_object, 
lo.line_object_description, 
lo.line_object_type, 
lot.object_type_display_descr
from line_object  lo (nolock)
join line_object_type lot (nolock) on lo.line_object_type=lot.line_object_type

), 

Summary1 as (


select 
avh.transaction_date, 
avl.transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from transaction_line avl (nolock)
join transaction_header avh  (nolock) on avh.transaction_id=avl.transaction_id
join [dbo].[discount_detail] avd (nolock) on  avd.transaction_id=avl.transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
union 
select 
avh.transaction_date, 
avl.av_transaction_id as transaction_id, 
avl.line_id, 
avl.line_sequence, 
avd.applied_by_line_id,
avd.pos_discount_amount,
L2.*
from av_transaction_line avl (nolock)
join av_transaction_header avh  (nolock) on avh.av_transaction_id=avl.av_transaction_id
join [dbo].[av_discount_detail] avd (nolock) on  avd.av_transaction_id=avl.av_transaction_id
	and avd.line_id=avl.line_id
join LO L on L.line_object=avl.line_object
join LO L2 on L2.line_object=avd.pos_discount_type
where datediff(dd,avh.transaction_date,GETDATE()) <= 60
) 


select transaction_date, 
transaction_id, 
line_id, 
line_sequence, 
sum(pos_discount_amount) as SumDiscAmount, 
line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr, 
case when left(line_object_description, 8) = 'Subtotal'
	then 'Header'
	else 'Line'
	end 
	as DiscountType

from Summary1 s 
group by 
transaction_date, 
transaction_id, 
line_id, 
line_sequence, 

line_object, 
line_object_description, 
line_object_type, 
object_type_display_descr
order by 2
```

#### OLE DB Source  - AW - Tax Line Data — SqlCommand

```sql
--With TaxLevel as (

--select 
--th.transaction_id,
--td.tax_level
--from [dbo].[transaction_line] tl (nolock) 
--join [dbo].[tax_detail] td  (nolock) on tl.transaction_id=td.transaction_id
--	and td.line_id=tl.line_id
--join [dbo].[transaction_header] th (nolock) on th.transaction_id=tl.transaction_id
--where line_action <> '90' -- 90 = order delivered, not interested in fulfilment 
--and datediff(dd,th.transaction_date,getdate()) <= 60
--and td.line_object_type = '5'-- SalesTax 
----and  tl.transaction_id = '449382903'
--group by th.transaction_id,
--td.tax_level
--union 
--select 
--th.av_transaction_id as transaction_id,
--td.tax_level
----into #tc
--from [dbo].[av_transaction_line] tl (nolock) 
--join [dbo].[av_tax_detail] td  (nolock) on tl.av_transaction_id=td.av_transaction_id
--	and td.line_id=tl.line_id
--join [dbo].[av_transaction_header] th (nolock) on th.av_transaction_id=tl.av_transaction_id
--where line_action <> '90' -- 90 = order delivered, not interested in fulfilment 
--and datediff(dd,th.transaction_date,getdate()) <= 60
--and td.line_object_type = '5'-- SalesTax 
----and  tl.av_transaction_id = '449382903'
--group by th.av_transaction_id,
--td.tax_level

--)

select tl.transaction_id,
tl.line_id, 
tl.line_sequence, 
tl.line_object_type, 
tl.line_object,
tl.line_action, 
tl.gross_line_amount, 
tl.pos_discount_amount,
td.taxable_amount, 
td.nontaxable_amount, 
td.combined_rate,
td.tax_amount_expected,
th.transaction_date,
td.tax_level
--into #tc
from [dbo].[transaction_header] th (nolock) 
join [dbo].[transaction_line] tl (nolock) on th.transaction_id=tl.transaction_id
join [dbo].[tax_detail] td  (nolock) on tl.transaction_id=td.transaction_id
	and td.line_id=tl.line_id
--join TaxLevel txl on txl.transaction_id=tl.transaction_id and txl.tax_level=td.tax_level
where line_action <> '90' -- 90 = order delivered, not interested in fulfilment 
and datediff(dd,th.transaction_date,getdate()) <= 60
--and  tl.transaction_id = '449382903'
union 
select tl.av_transaction_id as transaction_id,
tl.line_id, 
tl.line_sequence, 
tl.line_object_type, 
tl.line_object,
tl.line_action, 
tl.gross_line_amount, 
tl.pos_discount_amount,
td.taxable_amount, 
td.nontaxable_amount, 
td.combined_rate,
td.tax_amount_expected, 
tl.transaction_date, 
td.tax_level
from [dbo].[av_transaction_header] th (nolock) 
join [dbo].[av_transaction_line] tl (nolock) on th.av_transaction_id=tl.av_transaction_id
join [dbo].[av_tax_detail] td  (nolock) on tl.av_transaction_id=td.av_transaction_id
	and td.line_id=tl.line_id
--join TaxLevel txl on txl.transaction_id=tl.av_transaction_id and txl.tax_level=td.tax_level
where line_action <> '90' -- 90 = order delivered, not interested in fulfilment 
and datediff(dd,th.transaction_date,getdate()) <= 60 
--and tl.av_transaction_id = '449382903'
order by 3, td.tax_level
```

#### OLE DB Source - auditworks - Tender Exchange Details -  Sorted — SqlCommand

```sql
select 
th.transaction_id,
th.cashier_no, 
th.store_no, 
th.register_no, 
th.transaction_no, 
th.transaction_date, 
cast (th.transaction_date as date) as transaction_date_cast, 
tl.line_sequence, 
tl.line_id, 
lo.line_object_description, 
la.line_action_display_descr, 
tl.line_object, 
tl.line_action, 
tl.gross_line_amount, 
tl.pos_discount_amount, 
tl.reference_no, 
isnull(OC.DFLT_CRNCY_CODE,'USD') as currency_code
from transaction_line tl (nolock) 
join transaction_header th (nolock) on th.transaction_id=tl.transaction_id
join line_object lo (nolock) on lo.line_object=tl.line_object
join line_action la (nolock) on la.line_action=tl.line_action
left join ORG_CHN OC (nolock) ON OC.ORG_CHN_NUM=th.store_no
where tl.line_action in ('2','12','23','26','27') -- Returned, Refunded,remitted in exchange, Cashed, Credited 
and tl.gross_line_amount <> 0
and tl.gross_line_amount - tl.pos_discount_amount <> 0
and DATEDIFF(dd,th.transaction_date, getdate()) <= 30 -- Need to Parameterize 
--and tl.transaction_id in ('464618130','464913484','464006163') -- Just for Testing 
union 
select
th.av_transaction_id as transaction_id, 
th.cashier_no, 
th.store_no, 
th.register_no, 
th.transaction_no, 
th.transaction_date, 
cast (th.transaction_date as date) as transaction_date_cast, 
tl.line_sequence, 
tl.line_id, 
lo.line_object_description, 
la.line_action_display_descr, 
tl.line_object, 
tl.line_action, 
tl.gross_line_amount, 
tl.pos_discount_amount, 
tl.reference_no, 
isnull(OC.DFLT_CRNCY_CODE,'USD') as currency_code
from av_transaction_line tl (nolock) 
join av_transaction_header th (nolock) on th.av_transaction_id=tl.av_transaction_id
join line_object lo (nolock) on lo.line_object=tl.line_object
join line_action la (nolock) on la.line_action=tl.line_action
left join ORG_CHN OC (nolock) ON OC.ORG_CHN_NUM=th.store_no
where tl.line_action in ('2','12','23','26','27') -- Returned, Refunded,remitted in exchange, Cashed, Credited 
and tl.gross_line_amount <> 0
and tl.gross_line_amount - tl.pos_discount_amount <> 0
and DATEDIFF(dd,th.transaction_date, getdate()) <= 30 -- Need to Parameterize 
and tl.gross_line_amount <> 0
--and tl.av_transaction_id in ('464618130','464913484','464006163') -- Just For Testing
```

#### OLE DB Source - DW — SqlCommand

```sql
with TransTenderTotal as (
select tfd.transaction_id, 
case when tender_key = '16'
	then sum(tender_amt*-1) 
	else sum(tender_amt)
	end as tender_amt 
from TenderFactsDynamics  tfd (nolock) 
where tender_key <> -1
--and tfd.transaction_id = '447023677'
group by tfd.transaction_id, tender_key

), 

TransTenderTotalSummary as 
(


select Transaction_id, 
sum(tender_amt) as TotalTenderAmount
from TransTenderTotal
group by transaction_id
having sum(tender_amt) > 0 

) 

select tfd.transaction_id, 
tfd.tender_key, 
--tfd.tender_amt, 
case when  tfd.tender_key in ('16') then 
	tfd.tender_amt*-1/ts.TotalTenderAmount 
	else tfd.tender_amt/ts.TotalTenderAmount 
	end as TenderPercentage 
from TenderFactsDynamics TFD (nolock) 
join TransTenderTotalSummary TS on tfd.transaction_id=ts.transaction_id
	and tfd.tender_key <> - 1
order by 1, 2
```

#### OLE DB Source -  Line and Payment Variance — SqlCommand

```sql
with 
DynamicsDiscountFactsStageCTE as (
	select RetailReceiptId, SaleLineNum, sum(Amount) as Amount
	from DynamicsDiscountFactsStage
	--where RetailReceiptId = '463385215'
	group by RetailReceiptId, SaleLineNum
) ,


Sales as (

	select s.RetailTransactionId,
		s.entity, 
		s.RetailReceiptId, 
		s.TransDate, 
	sum (s.OriginalPrice*abs(s.qty))-sum(s.DiscAmount) as SalesTotal 
	from DynamicsSalesDetailDiscountsFactsStage s (nolock) 
	left join DynamicsDiscountFactsStageCTE dfs on dfs.RetailReceiptId=s.RetailReceiptId
											and dfs.SaleLineNum=s.linenum
	--where s.RetailReceiptId = '452290277'
	group by s.RetailTransactionId, 
	s.entity, 
	s.RetailReceiptId, 
	s.TransDate
), 

Tax as (
select 
	RetailTransactionId, 
	entity, 
	cast ( dbo.bankersround(sum(Amount),2) as decimal (14,2))as TaxAmount
	from DynamicsTaxFactsStage
	group by RetailTransactionId, entity

),

Tenders as (
select 
	p.RetailTransactionId, sum(p.AmountCur) as PaymentTotal
	from DynamicsPaymentFactsStage p
	group by p.RetailTransactionId
) , 

Summary1 as (
select 
	s.*, 
	isnull(tx.TaxAmount,0.00) as TaxTotal, 
	isnull(t.PaymentTotal,0.00) as PaymentTotal
	from Sales s 
	left join Tenders t on s.RetailTransactionId=t.RetailTransactionId
	left join Tax tx on tx.RetailTransactionId=s.RetailTransactionId

), 

Summary2 as (

select 
	RetailTransactionId, 
	Entity, 
	RetailReceiptId,
	TransDate,
	cast(SalesTotal+TaxTotal as decimal (14,2)) as GrossAmount,
	cast (PaymentTotal as decimal (14,2)) as PaymentTotal 
	from Summary1
), 

Summary3 as (
select 
	RetailTransactionId, 
	RetailReceiptId,
	TransDate,
	Entity,
	GrossAmount, 
	PaymentTotal, 
	PaymentTotal-GrossAmount as Variance
	from Summary2 
	
	
) 


select distinct RetailTransactionId, RetailReceiptId, 'Sales and Payment Variance' as Reason, cast (abs(Variance) as numeric (14,2)) as VarianceValue
from Summary3
where Variance <> 0.00
group by RetailTransactionId, RetailReceiptId, Variance 

-- Troubleshooting below 


--select *
--from Summary3
--where Variance <> 0.00
----and abs(Variance) <> 0.01
----where RetailTransactionId = '1001-1001Int-20230102-465517334'
```

#### OLE DB Source - Discount is Not Positive and Transaction Is Not A Return — SqlCommand

```sql
with ReturnTransactions as (

select d.RetailTransactionId, d.RetailReceiptId, d.LineNum as SaleLineNum
--from DynamicsSalesDetailFactsStage d -- Replaced on 12/12/2022
from DynamicsSalesDetailDiscountsFactsStage d (nolock) 
where d.LineAction in (2,12,15,26)
and DiscAmount <> 0.00
group by d.RetailTransactionId, d.RetailReceiptId, d.LineNum

)

select distinct d.RetailTransactionId, d.RetailReceiptId, 'Discount Not Positive' as Reason
from DynamicsDiscountFactsStage d
left join ReturnTransactions RT on rt.RetailTransactionId=d.RetailTransactionId and rt.SaleLineNum=rt.SaleLineNum
where d.Amount < 0 
and rt.RetailTransactionId is null 
group by d.RetailTransactionId, d.RetailReceiptId
```

#### OLE DB Source - Header and Line Discounts Mismatch — SqlCommand

```sql
with DiscountsInSalesLines as (

select  RetailReceiptId, sum(DiscAmount) as SalesLIneSumDiscAmount 
from DynamicsSalesDetailDiscountsFactsStage
group by retailreceiptid 

) , 

Summary1 as (


select RetailTransactionId, h.RetailReceiptId, DiscAmount, TotalDiscAmount, dsl.SalesLIneSumDiscAmount, (h.DiscAmount - dsl.SalesLIneSumDiscAmount) as VarianceValue
from DynamicsTransactionHeaderFactsStage h
join DiscountsInSalesLines dsl on dsl.retailreceiptid=h.RetailReceiptId
where h.DiscAmount <> dsl.SalesLIneSumDiscAmount
group by RetailTransactionId, h.RetailReceiptId, DiscAmount, TotalDiscAmount, dsl.SalesLIneSumDiscAmount
) 

select RetailTransactionId, 
'Header and Line Discounts Mismatch' as Reason, 
RetailReceiptId,
cast (abs(VarianceValue) as numeric (14,2)) as VarianceValue
from Summary1 s
group by RetailTransactionId, 
RetailReceiptId , 
VarianceValue
order by 1
```

#### OLE DB Source - Invalid ItemId values — SqlCommand

```sql
select RetailTransactionId, RetailReceiptId, ItemId, dsd.LineObject, lod.Line_Object_Description, 'Item Id or ItemId Mapping Missing' as Reason 
--from DynamicsSalesDetailFactsStage dsd -- Replaced on 12/12/2022
from DynamicsSalesDetailDiscountsFactsStage dsd

join dw.dbo.line_object_dim lod on lod.Line_Object=dsd.LineObject
where (ItemId is null  or 
right(ItemId,10) = 'NoRefAvail' )
group by RetailTransactionId,RetailReceiptId, ItemId, dsd.LineObject, lod.Line_Object_Description
order by 1, 2
```

#### OLE DB Source - Item Does Not Exist in Dynamics — SqlCommand

```sql
select RetailTransactionId,
		RetailReceiptId, 
		ItemId, 
		Entity 
--from DynamicsSalesDetailFactsStage dsd -- Replaced on 12/12/2022
from DynamicsSalesDetailDiscountsFactsStage dsd (nolock) 


group by RetailTransactionId,
RetailReceiptId, 
ItemId, 
Entity 
order by 1, 2
```

#### OLE DB Source - Sold Price is Negative — SqlCommand

```sql
select 
	RetailTransactionId, 
	RetailReceiptId,
	ItemId, 
	dsd.price,
	dsd.LineObject, 
	lod.Line_Object_Description, 
	'Item Sold Price Is Negative' as Reason 
--from DynamicsSalesDetailFactsStage dsd -- Replaced on 12/12/2022
from DynamicsSalesDetailDiscountsFactsStage dsd
join dw.dbo.line_object_dim lod on lod.Line_Object=dsd.LineObject
where dsd.LineAction not in (2,12,15,26) -- These are the known Return Line Actions
	and (
		qty > 0  -- When an item is sold the quantity is negative thus when returned it is positive 
		and 
		Price < 0 -- When an item is sold the price is positive thus when returned it is negatve 
		)
--where (price < 0 and Qty > 0) -- Replaced 1/18/2023
group by RetailTransactionId,RetailReceiptId, ItemId, dsd.LineObject, lod.Line_Object_Description, dsd.price 
order by 1, 2
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Destination - DWStaging - tmpDynamicsIntRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsIntRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsIntRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables | DWStaging |  |
| OLE DB Destination - DWStaging - DynamicsDiscountFactsStage |  | OLEDBDestination | Data Flow Task - Load Discounts - New | DWStaging |  |
| OLE DB Destination - DWStaging - DynamicsTaxFactsStage |  | OLEDBDestination | Data Flow Task - UK and IE TAx | DWStaging |  |
| OLE DB Destination - DWStaging - DynamicsTaxFactsStage |  | OLEDBDestination | Data Flow Task - US and CA Tax | DWStaging |  |
| OLE DB Destination - DW Staging - DynamicsTransactionHeaderFactsStage |  | OLEDBDestination | Data Flow Task - Load Header | DWStaging |  |
| OLE DB Destination - DW Staging -  DynamicsSalesDetailFactsStage |  | OLEDBDestination | Data Flow Task - Load Sales Detail - Sound Chip | DWStaging |  |
| OLE DB Destination - DWStaging - DynamicsSalesDetailDiscountsFactsStage |  | OLEDBDestination | Data Flow Task - Load Sales Detail Discounts | DWStaging |  |
| OLE DB Destination - DW Staging - DynamicsTransactionHeaderFactsStage |  | OLEDBDestination | DF - Header (1 store) | DWStaging |  |
| OLE DB Destination - DW Staging -  DynamicsSalesDetailFactsStage |  | OLEDBDestination | DF - Load Sales Detail - Sound Chip (1 store) | DWStaging |  |
| OLE DB Destination - DW Staging - DynamicsPaymentFactsStage |  | OLEDBDestination | Data Flow Task - Load Payments | DWStaging |  |
| OLE DB Destination - DWStaging - DiscountFactsReferenceDynamicsStage |  | OLEDBDestination | Data Flow Task | DWStaging |  |
| OLE DB Destination - DWStaging - TransactionTaxFactsDynamicsStage |  | OLEDBDestination | Data Flow Task | DWStaging |  |
| OLE DB Destination - DWstaging - DynamicsTenderExchangeFactsStage |  | OLEDBDestination | Data Flow Task | DWStaging |  |
| OLE DB Destination - DWStaging - TenderPercentageFactsDynamicsStage |  | OLEDBDestination | Data Flow Task | DWStaging |  |
| OLE DB Destination - DWStaging - DynamicsSalesTransactionExceptions |  | OLEDBDestination | Data Flow Task - Route Exceptions to Review Table - With Item in Dynamics Check | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsIntRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables - New DataLake | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsIntRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old | DWStaging |  |
| OLE DB Destination - DWStaging - tmpDynamicsRetailTransaction |  | OLEDBDestination | Data Flow Task - Load tmpDynamics ODATA Validation Tables - Old | DWStaging |  |
