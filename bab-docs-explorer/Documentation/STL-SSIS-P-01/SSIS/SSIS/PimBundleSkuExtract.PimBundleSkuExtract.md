# SSIS Package: PimBundleSkuExtract

**Project:** PimBundleSkuExtract  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Connection Managers

| Name | Type | Server | Catalog | Connection (sanitized) |
|---|---|---|---|---|
| Archive | FILE |  |  |  |
| ArchiveClearance | FILE |  |  |  |
| ArchiveFeedonomics | FILE |  |  |  |
| IntegrationStaging | OLEDB | stl-ssis-p-01 | IntegrationStaging | Data Source=stl-ssis-p-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| IntegrationStagingProdCopyingOnly | OLEDB | stl-ssis-p-01 | IntegrationStaging | Data Source=stl-ssis-p-01; Initial Catalog=IntegrationStaging; Provider=SQLNCLI11.1; Integrated Security=SSPI; Auto Translate=False |
| MissingBundlesCsv | FLATFILE |  |  |  |
| PimCsv | FLATFILE |  |  |  |
| PimCsvUk | FLATFILE |  |  |  |
| PimCsvUkQty | FLATFILE |  |  |  |
| PimCsvUs | FLATFILE |  |  |  |
| PimCsvUsQty | FLATFILE |  |  |  |
| SMTP | SMTP |  |  |  |
| UK_GlobalE_BundlesCsv | FLATFILE |  |  |  |
| UK_GlobalE_ComponentCsv | FLATFILE |  |  |  |
| US_GlobalE_BundleCsv | FLATFILE |  |  |  |
| US_GlobalE_ComponentCsv | FLATFILE |  |  |  |
| UkClearancePriceCsv | FLATFILE |  |  |  |
| UkSalePriceCsv | FLATFILE |  |  |  |
| UsClearancePriceCsv | FLATFILE |  |  |  |
| UsSalePriceCsv | FLATFILE |  |  |  |
| XML FILE | FILE |  |  |  |
| XML FILE Clearance | FILE |  |  |  |

## Control Flow Tasks

| Task | Type |
|---|---|
| PimBundleSkuExtract | Package |
| Execute SQL Task  - Check Time | ExecuteSQLTask |
| Faux Control | ExecuteSQLTask |
| SeqCont - Bundle Sale Price Extract | SEQUENCE |
| Execute SQL Task - Truncate Stage | ExecuteSQLTask |
| SeqCont - Cleanse and Stage For Sale Pricebook XML generation  Data | SEQUENCE |
| Data Flow Task - Build Sale Bundle Fact Table - New Oct 4 2024 | Pipeline |
| Data Flow Task - Build Sale Bundle Fact Table - Old | Pipeline |
| Data Flow Task - Cleanse | Pipeline |
| SeqCont - Copy and Archive Files | SEQUENCE |
| FEL - Copy to SFTP and Archive | FOREACHLOOP |
| File System Task - Archive | FileSystemTask |
| File System Task - Copy to Feedonomics Directory | FileSystemTask |
| File System Task - Copy to SFTP Stage | FileSystemTask |
| SeqCont - Output Sale Pricebook XML Files | SEQUENCE |
| Data Flow Task - UK Sale File Generation | Pipeline |
| Data Flow Task - US Sale File Generation | Pipeline |
| SeqCont - Process Sale Price Files | SEQUENCE |
| FEL - Ingest and Archive Copy of Sale Price File - UK | FOREACHLOOP |
| Data Flow Task | Pipeline |
| File System Task - Copy File | FileSystemTask |
| FEL - Ingest and Archive Copy of Sale Price File - US | FOREACHLOOP |
| Data Flow Task | Pipeline |
| File System Task - Copy File | FileSystemTask |
| SeqCont - Clearance Price Extract | SEQUENCE |
| Execute SQL Task - Truncate Stage | ExecuteSQLTask |
| SeqCont - Cleanse and Stage for Clearance Pricebook Generation Data | SEQUENCE |
| Data Flow Task - Build Clearance Bundle Fact Table | Pipeline |
| Data Flow Task - Cleanse - Handle Duplicates | Pipeline |
| SeqCont - Copy and Archive Clerance Pricebook Files | SEQUENCE |
| FEL - Copy to SFTP and Archive | FOREACHLOOP |
| File System Task - Archive | FileSystemTask |
| File System Task - Copy to Feedonomics Directory | FileSystemTask |
| File System Task - Copy to SFTP Stage | FileSystemTask |
| SeqCont - Output Clearance Pricebook XML Files | SEQUENCE |
| Data Flow Task - UK Clearance File Generation | Pipeline |
| Data Flow Task - US Clearance File Generation | Pipeline |
| SeqCont - Process Clearance Price Files | SEQUENCE |
| FEL - Ingest and Archive Copy of Clearance File - UK | FOREACHLOOP |
| Data Flow Task | Pipeline |
| File System Task - Copy UK File | FileSystemTask |
| FEL - Ingest and Archive Copy of Clearance File - US | FOREACHLOOP |
| Data Flow Task | Pipeline |
| File System Task - Copy US File | FileSystemTask |
| SeqCont - Generate and Email Global E Report Documents | SEQUENCE |
| FEL - Archive Global E Files | FOREACHLOOP |
| File System Task - Archive Global E Files | FileSystemTask |
| Send Mail Task - Email Global E Filese to Web Team | SendMailTask |
| SeqCont - Generate Global E Files | SEQUENCE |
| Data Flow Task | Pipeline |
| SeqCont - Missing Bundles Stage | SEQUENCE |
| Data Flow Task | Pipeline |
| Execute SQL Task | ExecuteSQLTask |
| SeqCont - Process and Stage PIM  Bundle Files - Orig | SEQUENCE |
| Data Flow Task - Cleanse and Derive | Pipeline |
| Execute SQL Task - Truncate Stage | ExecuteSQLTask |
| FEL - Ingest and Archive PIM Bundle Files | FOREACHLOOP |
| Data Flow Task - File to Stage | Pipeline |
| Rename and Archive | FileSystemTask |
| spMergePimBundleSkuExtract | ExecuteSQLTask |
| SeqCont - Process and Stage PIM  Bundle Files - Seperate Files | SEQUENCE |
| Execute SQL Task - Truncate Stage | ExecuteSQLTask |
| SeqCont - Consolidate and Cleanse | SEQUENCE |
| Data Flow Task - Cleanse | Pipeline |
| Data Flow Task - Consolidate | Pipeline |
| Sequence Container | SEQUENCE |
| FEL - Ingest and Archive PIM Bundle File UK | FOREACHLOOP |
| Data Flow Task | Pipeline |
| Rename and Archive | FileSystemTask |
| FEL - Ingest and Archive PIM Bundle File US | FOREACHLOOP |
| Data Flow Task | Pipeline |
| Rename and Archive | FileSystemTask |
| spMergePimBundleSkuExtract | ExecuteSQLTask |
| SeqCont - Stage and Merge Bundle Pricing to PricebookFactBundles | SEQUENCE |
| Data Flow Task - BundleSkuExtract to PricebookFactBundlePreStage | Pipeline |
| Execute SQL Task - Truncate Stage | ExecuteSQLTask |
| spMergePricebookBundleSkuFact | ExecuteSQLTask |
| SeqCont - Test Assistance - Copy PROD Single Sku Pricebook Tables to Test | SEQUENCE |
| Data Flow Task - Single Sku Pricebook | Pipeline |
| Execute SQL Task | ExecuteSQLTask |
| SeqCont - Test Assitance - Copy PROD Bundle Pricebook Tables to TEst | SEQUENCE |
| Data Flow Task Bundle Pricebook | Pipeline |
| Execute SQL Task | ExecuteSQLTask |
| SeqCont - Upload XML Files To Feedonomics and Archive | SEQUENCE |
| FEL - Archive Feedonomics Files | FOREACHLOOP |
| File System Task - Archive File | FileSystemTask |
| WinSCP  - Upload Files to Feedonomics FTP | ExecuteProcess |
| Send Mail Task | SendMailTask |

## Control Flow Outline

```text
- Send Mail Task [SendMailTask]
- Execute SQL Task  - Check Time [ExecuteSQLTask]
- Faux Control [ExecuteSQLTask]
- SeqCont - Bundle Sale Price Extract [SEQUENCE]
  - Execute SQL Task - Truncate Stage [ExecuteSQLTask]
  - SeqCont - Cleanse and Stage For Sale Pricebook XML generation  Data [SEQUENCE]
    - Data Flow Task - Build Sale Bundle Fact Table - New Oct 4 2024 [Pipeline]
    - Data Flow Task - Build Sale Bundle Fact Table - Old [Pipeline]
    - Data Flow Task - Cleanse [Pipeline]
  - SeqCont - Copy and Archive Files [SEQUENCE]
    - FEL - Copy to SFTP and Archive [FOREACHLOOP]
      - File System Task - Archive [FileSystemTask]
      - File System Task - Copy to Feedonomics Directory [FileSystemTask]
      - File System Task - Copy to SFTP Stage [FileSystemTask]
  - SeqCont - Output Sale Pricebook XML Files [SEQUENCE]
    - Data Flow Task - UK Sale File Generation [Pipeline]
    - Data Flow Task - US Sale File Generation [Pipeline]
  - SeqCont - Process Sale Price Files [SEQUENCE]
    - FEL - Ingest and Archive Copy of Sale Price File - UK [FOREACHLOOP]
      - Data Flow Task [Pipeline]
      - File System Task - Copy File [FileSystemTask]
    - FEL - Ingest and Archive Copy of Sale Price File - US [FOREACHLOOP]
      - Data Flow Task [Pipeline]
      - File System Task - Copy File [FileSystemTask]
- SeqCont - Clearance Price Extract [SEQUENCE]
  - Execute SQL Task - Truncate Stage [ExecuteSQLTask]
  - SeqCont - Cleanse and Stage for Clearance Pricebook Generation Data [SEQUENCE]
    - Data Flow Task - Build Clearance Bundle Fact Table [Pipeline]
    - Data Flow Task - Cleanse - Handle Duplicates [Pipeline]
  - SeqCont - Copy and Archive Clerance Pricebook Files [SEQUENCE]
    - FEL - Copy to SFTP and Archive [FOREACHLOOP]
      - File System Task - Archive [FileSystemTask]
      - File System Task - Copy to Feedonomics Directory [FileSystemTask]
      - File System Task - Copy to SFTP Stage [FileSystemTask]
  - SeqCont - Output Clearance Pricebook XML Files [SEQUENCE]
    - Data Flow Task - UK Clearance File Generation [Pipeline]
    - Data Flow Task - US Clearance File Generation [Pipeline]
  - SeqCont - Process Clearance Price Files [SEQUENCE]
    - FEL - Ingest and Archive Copy of Clearance File - UK [FOREACHLOOP]
      - Data Flow Task [Pipeline]
      - File System Task - Copy UK File [FileSystemTask]
    - FEL - Ingest and Archive Copy of Clearance File - US [FOREACHLOOP]
      - Data Flow Task [Pipeline]
      - File System Task - Copy US File [FileSystemTask]
- SeqCont - Generate and Email Global E Report Documents [SEQUENCE]
  - FEL - Archive Global E Files [FOREACHLOOP]
    - File System Task - Archive Global E Files [FileSystemTask]
  - Send Mail Task - Email Global E Filese to Web Team [SendMailTask]
  - SeqCont - Generate Global E Files [SEQUENCE]
    - Data Flow Task [Pipeline]
- SeqCont - Missing Bundles Stage [SEQUENCE]
  - Data Flow Task [Pipeline]
  - Execute SQL Task [ExecuteSQLTask]
- SeqCont - Process and Stage PIM  Bundle Files - Orig [SEQUENCE]
  - Data Flow Task - Cleanse and Derive [Pipeline]
  - Execute SQL Task - Truncate Stage [ExecuteSQLTask]
  - FEL - Ingest and Archive PIM Bundle Files [FOREACHLOOP]
    - Data Flow Task - File to Stage [Pipeline]
    - Rename and Archive [FileSystemTask]
  - spMergePimBundleSkuExtract [ExecuteSQLTask]
- SeqCont - Process and Stage PIM  Bundle Files - Seperate Files [SEQUENCE]
  - Execute SQL Task - Truncate Stage [ExecuteSQLTask]
  - SeqCont - Consolidate and Cleanse [SEQUENCE]
    - Data Flow Task - Cleanse [Pipeline]
    - Data Flow Task - Consolidate [Pipeline]
  - Sequence Container [SEQUENCE]
    - FEL - Ingest and Archive PIM Bundle File UK [FOREACHLOOP]
      - Data Flow Task [Pipeline]
      - Rename and Archive [FileSystemTask]
    - FEL - Ingest and Archive PIM Bundle File US [FOREACHLOOP]
      - Data Flow Task [Pipeline]
      - Rename and Archive [FileSystemTask]
  - spMergePimBundleSkuExtract [ExecuteSQLTask]
- SeqCont - Stage and Merge Bundle Pricing to PricebookFactBundles [SEQUENCE]
  - Data Flow Task - BundleSkuExtract to PricebookFactBundlePreStage [Pipeline]
  - Execute SQL Task - Truncate Stage [ExecuteSQLTask]
  - spMergePricebookBundleSkuFact [ExecuteSQLTask]
- SeqCont - Test Assistance - Copy PROD Single Sku Pricebook Tables to Test [SEQUENCE]
  - Data Flow Task - Single Sku Pricebook [Pipeline]
  - Execute SQL Task [ExecuteSQLTask]
- SeqCont - Test Assitance - Copy PROD Bundle Pricebook Tables to TEst [SEQUENCE]
  - Data Flow Task Bundle Pricebook [Pipeline]
  - Execute SQL Task [ExecuteSQLTask]
- SeqCont - Upload XML Files To Feedonomics and Archive [SEQUENCE]
  - FEL - Archive Feedonomics Files [FOREACHLOOP]
    - File System Task - Archive File [FileSystemTask]
  - WinSCP  - Upload Files to Feedonomics FTP [ExecuteProcess]
```

## Architecture Diagram

```mermaid
flowchart TD
    n_Package_Execute_SQL_Task____Check_Time["Execute SQL Task  - Check Time"]
    n_Package_Faux_Control["Faux Control"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract["SeqCont - Bundle Sale Price Extract"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_Execute_SQL_Task___Truncate_Stage["Execute SQL Task - Truncate Stage"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data["SeqCont - Cleanse and Stage For Sale Pricebook XML generation  Data"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data_Data_Flow_Task___Build_Sale_Bundle_Fact_Table___New_Oct_4_2024["Data Flow Task - Build Sale Bundle Fact Table - New Oct 4 2024"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data_Data_Flow_Task___Build_Sale_Bundle_Fact_Table___Old["Data Flow Task - Build Sale Bundle Fact Table - Old"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data_Data_Flow_Task___Cleanse["Data Flow Task - Cleanse"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files["SeqCont - Copy and Archive Files"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files_FEL___Copy_to_SFTP_and_Archive["FEL - Copy to SFTP and Archive"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Archive["File System Task - Archive"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_Feedonomics_Directory["File System Task - Copy to Feedonomics Directory"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_SFTP_Stage["File System Task - Copy to SFTP Stage"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Output_Sale_Pricebook_XML_Files["SeqCont - Output Sale Pricebook XML Files"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Output_Sale_Pricebook_XML_Files_Data_Flow_Task___UK_Sale_File_Generation["Data Flow Task - UK Sale File Generation"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Output_Sale_Pricebook_XML_Files_Data_Flow_Task___US_Sale_File_Generation["Data Flow Task - US Sale File Generation"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files["SeqCont - Process Sale Price Files"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___UK["FEL - Ingest and Archive Copy of Sale Price File - UK"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___UK_Data_Flow_Task["Data Flow Task"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___UK_File_System_Task___Copy_File["File System Task - Copy File"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___US["FEL - Ingest and Archive Copy of Sale Price File - US"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___US_Data_Flow_Task["Data Flow Task"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___US_File_System_Task___Copy_File["File System Task - Copy File"]
    n_Package_SeqCont___Clearance_Price_Extract["SeqCont - Clearance Price Extract"]
    n_Package_SeqCont___Clearance_Price_Extract_Execute_SQL_Task___Truncate_Stage["Execute SQL Task - Truncate Stage"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data["SeqCont - Cleanse and Stage for Clearance Pricebook Generation Data"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data_Data_Flow_Task___Build_Clearance_Bundle_Fact_Table["Data Flow Task - Build Clearance Bundle Fact Table"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data_Data_Flow_Task___Cleanse___Handle_Duplicates["Data Flow Task - Cleanse - Handle Duplicates"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files["SeqCont - Copy and Archive Clerance Pricebook Files"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_FEL___Copy_to_SFTP_and_Archive["FEL - Copy to SFTP and Archive"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Archive["File System Task - Archive"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_Feedonomics_Directory["File System Task - Copy to Feedonomics Directory"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_SFTP_Stage["File System Task - Copy to SFTP Stage"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Output_Clearance_Pricebook_XML_Files["SeqCont - Output Clearance Pricebook XML Files"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Output_Clearance_Pricebook_XML_Files_Data_Flow_Task___UK_Clearance_File_Generation["Data Flow Task - UK Clearance File Generation"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Output_Clearance_Pricebook_XML_Files_Data_Flow_Task___US_Clearance_File_Generation["Data Flow Task - US Clearance File Generation"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files["SeqCont - Process Clearance Price Files"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___UK["FEL - Ingest and Archive Copy of Clearance File - UK"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___UK_Data_Flow_Task["Data Flow Task"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___UK_File_System_Task___Copy_UK_File["File System Task - Copy UK File"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___US["FEL - Ingest and Archive Copy of Clearance File - US"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___US_Data_Flow_Task["Data Flow Task"]
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___US_File_System_Task___Copy_US_File["File System Task - Copy US File"]
    n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents["SeqCont - Generate and Email Global E Report Documents"]
    n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_FEL___Archive_Global_E_Files["FEL - Archive Global E Files"]
    n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_FEL___Archive_Global_E_Files_File_System_Task___Archive_Global_E_Files["File System Task - Archive Global E Files"]
    n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_Send_Mail_Task___Email_Global_E_Filese_to_Web_Team["Send Mail Task - Email Global E Filese to Web Team"]
    n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_SeqCont___Generate_Global_E_Files["SeqCont - Generate Global E Files"]
    n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_SeqCont___Generate_Global_E_Files_Data_Flow_Task["Data Flow Task"]
    n_Package_SeqCont___Missing_Bundles_Stage["SeqCont - Missing Bundles Stage"]
    n_Package_SeqCont___Missing_Bundles_Stage_Data_Flow_Task["Data Flow Task"]
    n_Package_SeqCont___Missing_Bundles_Stage_Execute_SQL_Task["Execute SQL Task"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig["SeqCont - Process and Stage PIM  Bundle Files - Orig"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_Data_Flow_Task___Cleanse_and_Derive["Data Flow Task - Cleanse and Derive"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_Execute_SQL_Task___Truncate_Stage["Execute SQL Task - Truncate Stage"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_FEL___Ingest_and_Archive_PIM_Bundle_Files["FEL - Ingest and Archive PIM Bundle Files"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_FEL___Ingest_and_Archive_PIM_Bundle_Files_Data_Flow_Task___File_to_Stage["Data Flow Task - File to Stage"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_FEL___Ingest_and_Archive_PIM_Bundle_Files_Rename_and_Archive["Rename and Archive"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_spMergePimBundleSkuExtract["spMergePimBundleSkuExtract"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files["SeqCont - Process and Stage PIM  Bundle Files - Seperate Files"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Execute_SQL_Task___Truncate_Stage["Execute SQL Task - Truncate Stage"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_SeqCont___Consolidate_and_Cleanse["SeqCont - Consolidate and Cleanse"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_SeqCont___Consolidate_and_Cleanse_Data_Flow_Task___Cleanse["Data Flow Task - Cleanse"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_SeqCont___Consolidate_and_Cleanse_Data_Flow_Task___Consolidate["Data Flow Task - Consolidate"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container["Sequence Container"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_UK["FEL - Ingest and Archive PIM Bundle File UK"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_UK_Data_Flow_Task["Data Flow Task"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_UK_Rename_and_Archive["Rename and Archive"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_US["FEL - Ingest and Archive PIM Bundle File US"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_US_Data_Flow_Task["Data Flow Task"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_US_Rename_and_Archive["Rename and Archive"]
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_spMergePimBundleSkuExtract["spMergePimBundleSkuExtract"]
    n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles["SeqCont - Stage and Merge Bundle Pricing to PricebookFactBundles"]
    n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_Data_Flow_Task___BundleSkuExtract_to_PricebookFactBundlePreStage["Data Flow Task - BundleSkuExtract to PricebookFactBundlePreStage"]
    n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_Execute_SQL_Task___Truncate_Stage["Execute SQL Task - Truncate Stage"]
    n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_spMergePricebookBundleSkuFact["spMergePricebookBundleSkuFact"]
    n_Package_SeqCont___Test_Assistance___Copy_PROD_Single_Sku_Pricebook_Tables_to_Test["SeqCont - Test Assistance - Copy PROD Single Sku Pricebook Tables to Test"]
    n_Package_SeqCont___Test_Assistance___Copy_PROD_Single_Sku_Pricebook_Tables_to_Test_Data_Flow_Task___Single_Sku_Pricebook["Data Flow Task - Single Sku Pricebook"]
    n_Package_SeqCont___Test_Assistance___Copy_PROD_Single_Sku_Pricebook_Tables_to_Test_Execute_SQL_Task["Execute SQL Task"]
    n_Package_SeqCont___Test_Assitance___Copy_PROD_Bundle_Pricebook_Tables_to_TEst["SeqCont - Test Assitance - Copy PROD Bundle Pricebook Tables to TEst"]
    n_Package_SeqCont___Test_Assitance___Copy_PROD_Bundle_Pricebook_Tables_to_TEst_Data_Flow_Task_Bundle_Pricebook["Data Flow Task Bundle Pricebook"]
    n_Package_SeqCont___Test_Assitance___Copy_PROD_Bundle_Pricebook_Tables_to_TEst_Execute_SQL_Task["Execute SQL Task"]
    n_Package_SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive["SeqCont - Upload XML Files To Feedonomics and Archive"]
    n_Package_SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive_FEL___Archive_Feedonomics_Files["FEL - Archive Feedonomics Files"]
    n_Package_SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive_FEL___Archive_Feedonomics_Files_File_System_Task___Archive_File["File System Task - Archive File"]
    n_Package_SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive_WinSCP____Upload_Files_to_Feedonomics_FTP["WinSCP  - Upload Files to Feedonomics FTP"]
    n_Package_EventHandlers_OnError__Send_Mail_Task["Send Mail Task"]
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data_Data_Flow_Task___Cleanse --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data_Data_Flow_Task___Build_Sale_Bundle_Fact_Table___New_Oct_4_2024
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_SFTP_Stage --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_Feedonomics_Directory
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_Feedonomics_Directory --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Archive
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Output_Sale_Pricebook_XML_Files_Data_Flow_Task___US_Sale_File_Generation --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Output_Sale_Pricebook_XML_Files_Data_Flow_Task___UK_Sale_File_Generation
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___UK_Data_Flow_Task --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___UK_File_System_Task___Copy_File
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___US_Data_Flow_Task --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files_FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___US_File_System_Task___Copy_File
    n_Package_SeqCont___Bundle_Sale_Price_Extract_Execute_SQL_Task___Truncate_Stage --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Process_Sale_Price_Files --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Output_Sale_Pricebook_XML_Files
    n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Output_Sale_Pricebook_XML_Files --> n_Package_SeqCont___Bundle_Sale_Price_Extract_SeqCont___Copy_and_Archive_Files
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data_Data_Flow_Task___Cleanse___Handle_Duplicates --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data_Data_Flow_Task___Build_Clearance_Bundle_Fact_Table
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_SFTP_Stage --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_Feedonomics_Directory
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Copy_to_Feedonomics_Directory --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_FEL___Copy_to_SFTP_and_Archive_File_System_Task___Archive
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Output_Clearance_Pricebook_XML_Files_Data_Flow_Task___US_Clearance_File_Generation --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Output_Clearance_Pricebook_XML_Files_Data_Flow_Task___UK_Clearance_File_Generation
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___UK_Data_Flow_Task --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___UK_File_System_Task___Copy_UK_File
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___US_Data_Flow_Task --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files_FEL___Ingest_and_Archive_Copy_of_Clearance_File___US_File_System_Task___Copy_US_File
    n_Package_SeqCont___Clearance_Price_Extract_Execute_SQL_Task___Truncate_Stage --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Process_Clearance_Price_Files --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Output_Clearance_Pricebook_XML_Files
    n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Output_Clearance_Pricebook_XML_Files --> n_Package_SeqCont___Clearance_Price_Extract_SeqCont___Copy_and_Archive_Clerance_Pricebook_Files
    n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_SeqCont___Generate_Global_E_Files --> n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_Send_Mail_Task___Email_Global_E_Filese_to_Web_Team
    n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_Send_Mail_Task___Email_Global_E_Filese_to_Web_Team --> n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents_FEL___Archive_Global_E_Files
    n_Package_SeqCont___Missing_Bundles_Stage_Execute_SQL_Task --> n_Package_SeqCont___Missing_Bundles_Stage_Data_Flow_Task
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_FEL___Ingest_and_Archive_PIM_Bundle_Files_Data_Flow_Task___File_to_Stage --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_FEL___Ingest_and_Archive_PIM_Bundle_Files_Rename_and_Archive
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_Execute_SQL_Task___Truncate_Stage --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_FEL___Ingest_and_Archive_PIM_Bundle_Files
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_FEL___Ingest_and_Archive_PIM_Bundle_Files --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_Data_Flow_Task___Cleanse_and_Derive
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_Data_Flow_Task___Cleanse_and_Derive --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_spMergePimBundleSkuExtract
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_SeqCont___Consolidate_and_Cleanse_Data_Flow_Task___Consolidate --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_SeqCont___Consolidate_and_Cleanse_Data_Flow_Task___Cleanse
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_UK_Data_Flow_Task --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_UK_Rename_and_Archive
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_US_Data_Flow_Task --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container_FEL___Ingest_and_Archive_PIM_Bundle_File_US_Rename_and_Archive
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Execute_SQL_Task___Truncate_Stage --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_Sequence_Container --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_SeqCont___Consolidate_and_Cleanse
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_SeqCont___Consolidate_and_Cleanse --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_spMergePimBundleSkuExtract
    n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_Execute_SQL_Task___Truncate_Stage --> n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_Data_Flow_Task___BundleSkuExtract_to_PricebookFactBundlePreStage
    n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_Data_Flow_Task___BundleSkuExtract_to_PricebookFactBundlePreStage --> n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_spMergePricebookBundleSkuFact
    n_Package_SeqCont___Test_Assistance___Copy_PROD_Single_Sku_Pricebook_Tables_to_Test_Execute_SQL_Task --> n_Package_SeqCont___Test_Assistance___Copy_PROD_Single_Sku_Pricebook_Tables_to_Test_Data_Flow_Task___Single_Sku_Pricebook
    n_Package_SeqCont___Test_Assitance___Copy_PROD_Bundle_Pricebook_Tables_to_TEst_Execute_SQL_Task --> n_Package_SeqCont___Test_Assitance___Copy_PROD_Bundle_Pricebook_Tables_to_TEst_Data_Flow_Task_Bundle_Pricebook
    n_Package_SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive_WinSCP____Upload_Files_to_Feedonomics_FTP --> n_Package_SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive_FEL___Archive_Feedonomics_Files
    n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files --> n_Package_SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles
    n_Package_Faux_Control --> n_Package_SeqCont___Bundle_Sale_Price_Extract
    n_Package_SeqCont___Bundle_Sale_Price_Extract --> n_Package_SeqCont___Clearance_Price_Extract
    n_Package_SeqCont___Clearance_Price_Extract --> n_Package_SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive
    n_Package_SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive --> n_Package_Execute_SQL_Task____Check_Time
    n_Package_Execute_SQL_Task____Check_Time --> n_Package_SeqCont___Generate_and_Email_Global_E_Report_Documents
    n_Package_Faux_Control --> n_Package_SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files
```

## Variables

| Namespace | Name | Expression-bound |
|---|---|---|
| System | Propagate | No |
| User | ArchiveClearancePriceFileNameAndPathUk | Yes |
| User | ArchiveClearancePriceFileNameAndPathUs | Yes |
| User | ArchiveFileNameAndPath | Yes |
| User | ArchiveFileNameAndPathUk | Yes |
| User | ArchiveFileNameAndPathUs | Yes |
| User | ArchiveFileNameAndPathUsBAK | Yes |
| User | ArchiveFolder | Yes |
| User | ArchiveFolderClearancePriceFile | Yes |
| User | ArchiveFolderSalePriceFile | Yes |
| User | ArchiveSalePriceFileNameAndPathUk | Yes |
| User | ArchiveSalePriceFileNameAndPathUs | Yes |
| User | DateTimeStamp | Yes |
| User | EndDate | Yes |
| User | EndDateAsDATE | Yes |
| User | FEL_ArchiveFilepath | Yes |
| User | FEL_BundleClearancePricebookName | No |
| User | FEL_BundleSalePricebookName | No |
| User | FEL_ClearancePriceFileNameUk | No |
| User | FEL_ClearancePriceFileNameUs | No |
| User | FEL_FeedonomicsFileName | No |
| User | FEL_GlobalE_FileName | No |
| User | FEL_GlobalE_SourceString | Yes |
| User | FEL_GlobaleE_ArchivePath | Yes |
| User | FEL_PimFileName | No |
| User | FEL_PimFileNameUk | No |
| User | FEL_PimFileNameUs | No |
| User | FEL_SalePriceFileNameUk | No |
| User | FEL_SalePriceFileNameUs | No |
| User | FeedonomicsStageDirectory | Yes |
| User | GetDate | Yes |
| User | GetDateAsDATE | Yes |
| User | GetDateTime | Yes |
| User | GlobalE_RootFolder | Yes |
| User | SFTPStageDirectory | Yes |
| User | StartDate | Yes |
| User | StartDateAsDATE | Yes |
| User | TimeCheck | No |
| User | UkClearancePriceBookOutputPath | Yes |
| User | UkSalePriceBookOutputPath | Yes |
| User | UsClearancePriceBookOutputPath | Yes |
| User | UsSalePriceBookOutputPath | Yes |

### Expression-bound variable values

#### User::ArchiveClearancePriceFileNameAndPathUk

**Expression:**

```sql
@[User::ArchiveFolderClearancePriceFile] +"BundleClearancePrice_UK_"+ @[User::GetDateAsDATE]+".csv"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Inbound\BundleClearancePrice\Archive\BundleClearancePrice_UK_2025-11-25.csv
```

#### User::ArchiveClearancePriceFileNameAndPathUs

**Expression:**

```sql
@[User::ArchiveFolderClearancePriceFile] +"BundleClearancePrice_US_"+ @[User::GetDateAsDATE]+".csv"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Inbound\BundleClearancePrice\Archive\BundleClearancePrice_US_2025-11-25.csv
```

#### User::ArchiveFileNameAndPath

**Expression:**

```sql
@[User::ArchiveFolder]+"PIMtoBABDW_"+ @[User::GetDateAsDATE]+".csv"
```

**Evaluated value:**

```sql
\\stl-sftp-p-01\ecommerce\to-bab\from-PIM\Prod\Archive\PIMtoBABDW_2025-11-25.csv
```

#### User::ArchiveFileNameAndPathUk

**Expression:**

```sql
@[User::ArchiveFolder]+"PIMtoBABDW_UK_"+ @[User::GetDateAsDATE]+".csv"
```

**Evaluated value:**

```sql
\\stl-sftp-p-01\ecommerce\to-bab\from-PIM\Prod\Archive\PIMtoBABDW_UK_2025-11-25.csv
```

#### User::ArchiveFileNameAndPathUs

**Expression:**

```sql
@[User::ArchiveFolder]+"PIMtoBABDW_US_"+  @[User::GetDateTime] +".csv"
```

**Evaluated value:**

```sql
\\stl-sftp-p-01\ecommerce\to-bab\from-PIM\Prod\Archive\PIMtoBABDW_US_2025-11-25-070936500.csv
```

#### User::ArchiveFileNameAndPathUsBAK

**Expression:**

```sql
@[User::ArchiveFolder]+"PIMtoBABDW_US_"+ @[User::GetDateAsDATE]+".csv"
```

**Evaluated value:**

```sql
\\stl-sftp-p-01\ecommerce\to-bab\from-PIM\Prod\Archive\PIMtoBABDW_US_2025-11-25.csv
```

#### User::ArchiveFolder

**Expression:**

```sql
@[$Package::PimOutputFilePath]+"Archive"+"\\"
```

**Evaluated value:**

```sql
\\stl-sftp-p-01\ecommerce\to-bab\from-PIM\Prod\Archive\
```

#### User::ArchiveFolderClearancePriceFile

**Expression:**

```sql
@[$Package::ClearancePriceFilePath] +"Archive"+"\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Inbound\BundleClearancePrice\Archive\
```

#### User::ArchiveFolderSalePriceFile

**Expression:**

```sql
@[$Package::SalePriceFilePath]+"Archive"+"\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Inbound\BundleSalePrice\Archive\
```

#### User::ArchiveSalePriceFileNameAndPathUk

**Expression:**

```sql
@[User::ArchiveFolderSalePriceFile]+"BundleSalePrice_UK_"+ @[User::GetDateAsDATE]+".csv"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Inbound\BundleSalePrice\Archive\BundleSalePrice_UK_2025-11-25.csv
```

#### User::ArchiveSalePriceFileNameAndPathUs

**Expression:**

```sql
@[User::ArchiveFolderSalePriceFile]+"BundleSalePrice_US_"+ @[User::GetDateAsDATE]+".csv"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Inbound\BundleSalePrice\Archive\BundleSalePrice_US_2025-11-25.csv
```

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
202511257936500
```

#### User::EndDate

**Expression:**

```sql
dateadd("dd", @[$Package::DaysToInclude], @[User::StartDate])
```

**Evaluated value:**

```sql
11/25/2025
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
2025-11-25
```

#### User::FEL_ArchiveFilepath

**Expression:**

```sql
@[$Package::PimOutputFilePath]+"Archive"+"\\"
```

**Evaluated value:**

```sql
\\stl-sftp-p-01\ecommerce\to-bab\from-PIM\Prod\Archive\
```

#### User::FEL_GlobalE_SourceString

**Expression:**

```sql
@[User::GlobalE_RootFolder]+ @[User::FEL_GlobalE_FileName]+".csv"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Pricebook\GlobalE\GlobalEFile.csv
```

#### User::FEL_GlobaleE_ArchivePath

**Expression:**

```sql
@[User::GlobalE_RootFolder]+"Archive"+ "\\"+@[User::FEL_GlobalE_FileName]+"_"+ @[User::DateTimeStamp]+".csv"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Pricebook\GlobalE\Archive\GlobalEFile_202511257936503.csv
```

#### User::FeedonomicsStageDirectory

**Expression:**

```sql
"\\\\"+ @[$Package::IntegrationStaging_ServerName]+"\\"+"IntegrationStaging"+"\\"+"WEB"+"\\"+"Outbound"+"\\"+"Feedonomics"+"\\"+"BundlePricebooks"+"\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Feedonomics\BundlePricebooks\
```

#### User::GetDate

**Expression:**

```sql
(DT_DATE)DATEDIFF("Day", (DT_DATE) 0, GETDATE())
```

**Evaluated value:**

```sql
11/25/2025
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
2025-11-25
```

#### User::GetDateTime

**Expression:**

```sql
(DT_STR,4,1252) YEAR(GETDATE()) + "-" +
RIGHT("0" + (DT_STR,2,1252) MONTH(GETDATE()),2) + "-" +
RIGHT("0" + (DT_STR,2,1252) DAY(GETDATE()),2) + "-" +
RIGHT("0" + (DT_STR,2,1252) DATEPART("HOUR",GETDATE()),2) +
RIGHT("0" + (DT_STR,2,1252) DATEPART("MINUTE",GETDATE()),2) +
RIGHT("0" + (DT_STR,2,1252) DATEPART("SECOND",GETDATE()),2) +
RIGHT("00" + (DT_STR,3,1252) DATEPART("MILLISECOND",GETDATE()),3)
```

**Evaluated value:**

```sql
2025-11-25-070936503
```

#### User::GlobalE_RootFolder

**Expression:**

```sql
"\\\\"+ @[$Package::IntegrationStaging_ServerName]+"\\"+"IntegrationStaging"+"\\"+"WEB"+"\\"+"Outbound"+"\\"+"Pricebook"+"\\"+"GlobalE"+"\\"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Pricebook\GlobalE\
```

#### User::SFTPStageDirectory

**Expression:**

```sql
@[$Package::SftpStageDirectory]
```

**Evaluated value:**

```sql
\\stl-sftp-p-01\ecommerce\to-sfcc\pricebooks\
```

#### User::StartDate

**Expression:**

```sql
dateadd("dd", -@[$Package::DaysToGoBack] , @[User::GetDate] )
```

**Evaluated value:**

```sql
11/24/2025
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
2025-11-24
```

#### User::UkClearancePriceBookOutputPath

**Expression:**

```sql
@[$Package::ClearancePriceXmlOutputFilePathRootFolder]+@[User::DateTimeStamp]+"_clearance_pricebooks_gbp.xml"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Pricebook\BundleSkuClearance\202511257936503_clearance_pricebooks_gbp.xml
```

#### User::UkSalePriceBookOutputPath

**Expression:**

```sql
@[$Package::SalePriceXmlOutputFilePathRootFolder]+ @[User::DateTimeStamp]+"_promo_pricebooks_gbp.xml"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Pricebook\BundleSku\202511257936503_promo_pricebooks_gbp.xml
```

#### User::UsClearancePriceBookOutputPath

**Expression:**

```sql
@[$Package::ClearancePriceXmlOutputFilePathRootFolder] + @[User::DateTimeStamp]+"_clearance_pricebooks_usd.xml"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Pricebook\BundleSkuClearance\202511257936507_clearance_pricebooks_usd.xml
```

#### User::UsSalePriceBookOutputPath

**Expression:**

```sql
@[$Package::SalePriceXmlOutputFilePathRootFolder]+ @[User::DateTimeStamp]+"_promo_pricebooks_usd.xml"
```

**Evaluated value:**

```sql
\\stl-ssis-p-01\IntegrationStaging\WEB\Outbound\Pricebook\BundleSku\202511257936507_promo_pricebooks_usd.xml
```

## Execute SQL Tasks

### Execute SQL Task  - Check Time

**Path:** `Package\Execute SQL Task  - Check Time`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select 
case when 
	cast (GETDATE () as time) < '12:00'
then 'Pass' 
Else 'Fail'
end as TimeCheck
```

### Faux Control

**Path:** `Package\Faux Control`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
select getdate () as FauxYo
```

### Execute SQL Task - Truncate Stage

**Path:** `Package\SeqCont - Bundle Sale Price Extract\Execute SQL Task - Truncate Stage`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
TRUNCATE TABLE WEB.BundleSalePriceStage
TRUNCATE TABLE WEB.BundleSalePrice
TRUNCATE TABLE WEB.BundleSalePriceFact
```

### Execute SQL Task - Truncate Stage

**Path:** `Package\SeqCont - Clearance Price Extract\Execute SQL Task - Truncate Stage`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table [WEB].[BundleClearancePriceStage]
truncate table [WEB].[BundleClearancePrice]
truncate table [WEB].[BundleClearancePriceFact] 
```

### Execute SQL Task

**Path:** `Package\SeqCont - Missing Bundles Stage\Execute SQL Task`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table [MissingBundleSkuStage]
```

### Execute SQL Task - Truncate Stage

**Path:** `Package\SeqCont - Process and Stage PIM  Bundle Files - Orig\Execute SQL Task - Truncate Stage`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table PimBundleSkuExtractStage
truncate table PimBundleSkuExtractCleansed

```

### spMergePimBundleSkuExtract

**Path:** `Package\SeqCont - Process and Stage PIM  Bundle Files - Orig\spMergePimBundleSkuExtract`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
exec [spMergePimBundleSkuExtract] 
```

### Execute SQL Task - Truncate Stage

**Path:** `Package\SeqCont - Process and Stage PIM  Bundle Files - Seperate Files\Execute SQL Task - Truncate Stage`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table PimBundleSkuExtractStageUs
truncate table PimBundleSkuExtractStageUk
truncate table PimBundleSkuExtractStageConsolidated
truncate table PimBundleSkuExtractStageConsolidatedAndCleansed


```

### spMergePimBundleSkuExtract

**Path:** `Package\SeqCont - Process and Stage PIM  Bundle Files - Seperate Files\spMergePimBundleSkuExtract`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
exec [spMergePimBundleSkuExtract] 
```

### Execute SQL Task - Truncate Stage

**Path:** `Package\SeqCont - Stage and Merge Bundle Pricing to PricebookFactBundles\Execute SQL Task - Truncate Stage`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table web.BundlePricebookFactPreStage
```

### spMergePricebookBundleSkuFact

**Path:** `Package\SeqCont - Stage and Merge Bundle Pricing to PricebookFactBundles\spMergePricebookBundleSkuFact`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
exec [WEB].[spMergePricebookBundleSkuFact]
```

### Execute SQL Task

**Path:** `Package\SeqCont - Test Assistance - Copy PROD Single Sku Pricebook Tables to Test\Execute SQL Task`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table web.PricebookFact
```

### Execute SQL Task

**Path:** `Package\SeqCont - Test Assitance - Copy PROD Bundle Pricebook Tables to TEst\Execute SQL Task`  
**Connection:** IntegrationStaging (stl-ssis-p-01/IntegrationStaging)  

```sql
truncate table [WEB].[PricebookBundleSkuFact]
```

## Data Flow: Sources

| Component | Source Object | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Source - IntStaging - SQL Cmd |  | OLEDBSource | Data Flow Task - Build Sale Bundle Fact Table - New Oct 4 2024 | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - SQL Cmd |  | OLEDBSource | Data Flow Task - Build Sale Bundle Fact Table - Old | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - WebBundleSalePriceStage - SQL Cmd |  | OLEDBSource | Data Flow Task - Cleanse | IntegrationStaging | SqlCommand |
| OLE DB Source - Dummy Source |  | OLEDBSource | Data Flow Task - UK Sale File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - Component Products |  | OLEDBSource | Data Flow Task - UK Sale File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - Sql Cmd - Price Table |  | OLEDBSource | Data Flow Task - UK Sale File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - Dummy Source |  | OLEDBSource | Data Flow Task - US Sale File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - Component Skus |  | OLEDBSource | Data Flow Task - US Sale File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - Sql Cmd - Price Table |  | OLEDBSource | Data Flow Task - US Sale File Generation | IntegrationStaging | SqlCommand |
| Flat File Source - UkSalePriceCsv |  | FlatFileSource | Data Flow Task | UkSalePriceCsv |  |
| Flat File Source - UsSalePriceCsv |  | FlatFileSource | Data Flow Task | UsSalePriceCsv |  |
| OLE DB Source - IntStaging - SQL Cmd |  | OLEDBSource | Data Flow Task - Build Clearance Bundle Fact Table | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - SQL Cmd |  | OLEDBSource | Data Flow Task - Cleanse - Handle Duplicates | IntegrationStaging | SqlCommand |
| OLE DB Source |  | OLEDBSource | Data Flow Task - UK Clearance File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - Dummy Cmd |  | OLEDBSource | Data Flow Task - UK Clearance File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - Lines |  | OLEDBSource | Data Flow Task - UK Clearance File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - Dummy Cmd |  | OLEDBSource | Data Flow Task - US Clearance File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - Component Skus |  | OLEDBSource | Data Flow Task - US Clearance File Generation | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - Lines |  | OLEDBSource | Data Flow Task - US Clearance File Generation | IntegrationStaging | SqlCommand |
| Flat File Source - UkClearancePriceCsv |  | FlatFileSource | Data Flow Task | UkClearancePriceCsv |  |
| Flat File Source - UsClearancePriceCsv |  | FlatFileSource | Data Flow Task | UsClearancePriceCsv |  |
| OLE DB Source - IntStaging -  UK Bundle Return |  | OLEDBSource | Data Flow Task | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging -  UK Component Return |  | OLEDBSource | Data Flow Task | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging -  US Bundle Return |  | OLEDBSource | Data Flow Task | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging -  US Component Return |  | OLEDBSource | Data Flow Task | IntegrationStaging | SqlCommand |
| Flat File Source - Missing Bundles Csv |  | FlatFileSource | Data Flow Task | MissingBundlesCsv |  |
| OLE DB Source - IntStaging - PimBundleSkuExtract SQL Cmd |  | OLEDBSource | Data Flow Task - Cleanse and Derive | IntegrationStaging | SqlCommand |
| Flat File Source - PimCSv |  | FlatFileSource | Data Flow Task - File to Stage | PimCsv |  |
| OLE DB Source - IntStaging - SQL Cmd |  | OLEDBSource | Data Flow Task - Cleanse | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStaging - SQL Cmd |  | OLEDBSource | Data Flow Task - Consolidate | IntegrationStaging | SqlCommand |
| Flat File Source - PimCsvUkQty |  | FlatFileSource | Data Flow Task | PimCsvUkQty |  |
| Flat File Source - PimCsvUsQty |  | FlatFileSource | Data Flow Task | PimCsvUsQty |  |
| OLE DB Source - IntStaging - SqlCommand |  | OLEDBSource | Data Flow Task - BundleSkuExtract to PricebookFactBundlePreStage | IntegrationStaging | SqlCommand |
| OLE DB Source - IntStagingProdCopyingOnly |  | OLEDBSource | Data Flow Task - Single Sku Pricebook | IntegrationStagingProdCopyingOnly |  |
| OLE DB Source - int STaging prod only |  | OLEDBSource | Data Flow Task Bundle Pricebook | IntegrationStagingProdCopyingOnly |  |

#### OLE DB Source - IntStaging - SQL Cmd — SqlCommand

```sql
With ListBundles as 
(
select 
f.BundleSku
,BundleSkuCatalog
from WEB.PricebookBundleSkuFact f
where 1=1
--and f.BundleSku in ('29031_28917_28934') -- Testing Purposes Only 
group by 
f.BundleSku
,BundleSkuCatalog
), 

BundlesWithSales as 
(
select 
e.BundleSku
,e.BundleSkuCatalog
,bpf.SaleReference
from [dbo].[PimBundleSkuExtract] p (nolock) join ListBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
join WEB.BundleSalePrice bpf (nolock) on bpf.StyleCode = p.ComponentProducts  and bpf.Catalog = p.Catalog and bpf.Catalog = e.BundleSkuCatalog
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter
group by 
e.BundleSku
,e.BundleSkuCatalog
,bpf.SaleReference

) 
, 
Summary1 as (
select 
e.BundleSku
,e.BundleSkuCatalog
,p.ComponentProducts as ComponentProduct
,bpf.SalePriceStartDateTime
,bpf.SalePriceEndDateTime
,bws.SaleReference
,bpf.SalePrice
,p.ComponentQuantity 
,pf.CurrentPrice as ListCurrentPrice
,pf.SalePrice as ListSalePrice
from [dbo].[PimBundleSkuExtract] p (nolock) 
join ListBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
join BundlesWithSales bws on bws.BundleSku = e.BundleSku and bws.BundleSkuCatalog = e.BundleSkuCatalog
join web.PricebookFact pf (nolock) on pf.style_code = p.ComponentProducts  and pf.Catalog = p.catalog 
left join WEB.BundleSalePrice bpf (nolock) on bpf.StyleCode = p.ComponentProducts  and bpf.Catalog = p.Catalog and bpf.Catalog = e.BundleSkuCatalog and bpf.SaleReference = bws.SaleReference
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter

) 
, FinalSummary as (
select 
 s.BundleSku
,s.BundleSkuCatalog
--,s.ComponentProduct
,min(s.SalePriceStartDateTime) as SalePriceStartDateTime
,max (s.SalePriceEndDateTime) SalePriceEndDateTime
,s.SaleReference
--,s.SalePrice
--,s.ComponentQuantity
--,s.ListCurrentPrice
--,s.ListSalePrice
,sum(isnull	(s.SalePrice*ComponentQuantity, isnull(	s.ListSalePrice*ComponentQuantity,s.ListCurrentPrice*ComponentQuantity))) as Price
from Summary1 s
group by 
s.BundleSku
,s.BundleSkuCatalog
,s.SaleReference
)
-- analysis against current 
/*
Select 
s.BundleSku
,s.BundleSkuCatalog
,s.SalePriceStartDateTime
,s.SalePriceEndDateTime
,s.Price as BundSkuSalePrice
,f.BundleSkuPrice as BundleSkuListPrice
, bpf.*
from FinalSummary s
join web.PricebookBundleSkuFact f on f.BundleSku = s.BundleSku and f.BundleSkuCatalog = s.BundleSkuCatalog
left join web.BundleSalePriceFact bpf on bpf.BundleSku = s.BundleSku and bpf.BundleSkuCatalog = s.BundleSkuCatalog and bpf.SalePriceStartDateTime = s.SalePriceStartDateTime and bpf.SalePriceEndDateTime = s.SalePriceEndDateTime
where 1=1
and bpf.BundleSku is null 
*/


Select 
 null as UnionSource
,s.BundleSku
,s.BundleSkuCatalog
,s.SalePriceStartDateTime
,s.SalePriceEndDateTime
,s.Price as BundSkuSalePrice
,f.BundleSkuPrice as BundleSkuListPrice
from FinalSummary s
join web.PricebookBundleSkuFact f on f.BundleSku = s.BundleSku and f.BundleSkuCatalog = s.BundleSkuCatalog
order by 2 desc ,1, 4
```

#### OLE DB Source - IntStaging - SQL Cmd — SqlCommand

```sql
With ListBundles as 
(
select 
f.BundleSku
,BundleSkuCatalog
from WEB.PricebookBundleSkuFact f
where 1=1
--and f.BundleSku in ('32498_32495_22920_22920','432498_432495_422920_422920','224099_24174_24175_28093') -- Testing Purposes Only 
group by 
f.BundleSku
,BundleSkuCatalog
)

,Summary1 as (

select 
e.BundleSku
,e.BundleSkuCatalog
,p.ComponentProducts as ComponentProduct
, bpf.SalePriceStartDateTime
,bpf.SalePriceEndDateTime
,bpf.SaleReference
,bpf.SalePrice
, case when SalePrice is null then 'List'
	else 'Sale'
	end as ComponentProductPricetype
,p.ComponentQuantity -- Added 9/26/2024 as part of JIRA BIB-1024
from [dbo].[PimBundleSkuExtract] p (nolock) 
join ListBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
left join WEB.BundleSalePrice bpf (nolock) on bpf.StyleCode = p.ComponentProducts  and bpf.Catalog = p.Catalog and bpf.Catalog = e.BundleSkuCatalog
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter
--and e.BundleSku in ('230005_30004','25533_32320_21564_28679_21512') -- Testing Filter
) 

, BundlesWithSales as (
select  
s.BundleSku,
BundleSkuCatalog
from Summary1 s
where 1=1
and SalePrice is not null 
group by 
s.BundleSku,
BundleSkuCatalog
)

, ListPrices as (
select
e.BundleSku
,e.BundleSkuCatalog
,pf.style_code as ListPriceStyleCode
,pf.CurrentPrice as ListCurrentPrice
,pf.SalePrice as ListSalePrice
from [dbo].[PimBundleSkuExtract] p (nolock) 
join ListBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
join web.PricebookFact pf (nolock) on pf.style_code = p.ComponentProducts  and pf.Catalog = p.catalog 
join BundlesWithSales bs on bs.BundleSku = e.BundleSku and bs.BundleSkuCatalog = e.BundleSkuCatalog
where 1=1
group by
e.BundleSku
,e.BundleSkuCatalog
,pf.style_code 
,pf.CurrentPrice 
,pf.SalePrice 
) 




, PricingSummary as (
select 
s.BundleSku
,s.BundleSkuCatalog
,s.ComponentProduct
,s.SalePriceStartDateTime
,s.SalePriceEndDateTime
,s.SaleReference
,s.SalePrice
,s.ComponentProductPricetype
,lp.ListCurrentPrice
,lp.ListSalePrice
,s.ComponentQuantity -- Added 9/26/2024 as part of JIRA BIB-1024
, rank ()over (partition by s.BundleSku order by s.ComponentProduct) as Rank
, dense_rank ()over (partition by s.BundleSku order by s.ComponentProduct, s.SalePriceStartDateTime) as DenseRank
from Summary1  s
join ListPrices lp on lp.BundleSku = s.BundleSku and lp.BundleSkuCatalog= s.BundleSkuCatalog and lp.ListPriceStyleCode = s.ComponentProduct
--order by 2, 1, 3 , 4

) 

, MultiSaleBundle as (
select 
pc.BundleSku
,pc.BundleSkuCatalog
from PricingSummary pc 
where 1=1 
and pc.Rank <> pc.DenseRank
and pc.SalePrice is not null 
group by 
pc.BundleSku
,pc.BundleSkuCatalog
) 

, MultiSummary as (
select 
pc.*
,'Union1' as UnionSource
from PricingSummary pc
where 1=1
and pc.rank = pc.DenseRank
union all
select 
pc.*
,'Union2' as UnionSource
from PricingSummary pc
join MultiSaleBundle msb on msb.BundleSku = pc.BundleSku and msb.BundleSkuCatalog = pc.BundleSkuCatalog
where 1=1
and 
(pc.rank = pc.DenseRank and pc.ComponentProductPricetype = 'List') 
or 
--(pc.rank <> pc.DenseRank and pc.ComponentProductPricetype = 'Sale') 
(pc.rank = pc.DenseRank-1 and pc.ComponentProductPricetype = 'Sale') 
--union all
--select 
--pc.*
--,'Union3' as UnionSource
--from PricingSummary pc
--join MultiSaleBundle msb on msb.BundleSku = pc.BundleSku and msb.BundleSkuCatalog = pc.BundleSkuCatalog
--where 1=1
--and 
--(pc.rank = pc.DenseRank and pc.ComponentProductPricetype = 'List') 
--or 
----(pc.rank <> pc.DenseRank and pc.ComponentProductPricetype = 'Sale') 
--(pc.rank = pc.DenseRank-2 and pc.ComponentProductPricetype = 'Sale') 

) 
, FinalSummary as (
select 
m.UnionSource
,m.BundleSku
,m.BundleSkuCatalog
,min (m.SalePriceStartDateTime) as SalePriceStartDateTime
,max (m.SalePriceEndDateTime) as SalePriceEndDateTime
--,sum(isnull(m.SalePrice, isnull(m.ListSalePrice,m.ListCurrentPrice))) as Price -- Replaced  9/26/2024 as part of JIRA BIB-1024
,sum(isnull	(m.SalePrice*ComponentQuantity, isnull(	m.ListSalePrice*ComponentQuantity,m.ListCurrentPrice*ComponentQuantity))) as Price -- Replaced  9/26/2024 as part of JIRA BIB-1024
from MultiSummary m
where 1=1
group by 
m.UnionSource
,m.BundleSku
,m.BundleSkuCatalog
)

Select 
s.UnionSource
,s.BundleSku
,s.BundleSkuCatalog
,s.SalePriceStartDateTime
,s.SalePriceEndDateTime
,s.Price as BundSkuSalePrice
,f.BundleSkuPrice as BundleSkuListPrice
from FinalSummary s
join web.PricebookBundleSkuFact f on f.BundleSku = s.BundleSku and f.BundleSkuCatalog = s.BundleSkuCatalog
where 1=1
--and s.SalePriceStartDateTime is not null 
--and s.BundleSkuCatalog = 'US'
order by 3 desc ,2, 4
```

#### OLE DB Source - IntStaging - WebBundleSalePriceStage - SQL Cmd — SqlCommand

```sql
select 
case when s.catalog  = 'UK' and len(sku) < 6 
		then concat ('4',right(DerivedStyleCode,5)) 
	else s.DerivedStyleCode
end as StyleCode
,s.Retail as SalePrice
,s.Catalog
,s.reference as SaleReference
,s.DerivedStartDateTime as SalePriceStartDateTime
,s.DerivedEndDateTime as SalePriceEndDateTime
from WEB.BundleSalePriceStage s
where 1=1
group by 
case when s.catalog  = 'UK' and len(sku) < 6 
		then concat ('4',right(DerivedStyleCode,5)) 
	else s.DerivedStyleCode
end
,s.Retail
,s.Catalog
,s.reference 
,s.DerivedStartDateTime 
,s.DerivedEndDateTime 
order by 
3 desc, 
1
```

#### OLE DB Source - Dummy Source — SqlCommand

```sql
select getdate() as DummyField
```

#### OLE DB Source - IntStaging - Component Products — SqlCommand

```sql
/*
With SaleBundles as 
(
select 
f.BundleSku
,BundleSkuCatalog
from [WEB].[BundleSalePriceFact] f
where 1=1
and f.BundleSkuCatalog = 'UK'
group by 
f.BundleSku
,BundleSkuCatalog
)
, Summary1 as (
select 
e.BundleSku
,e.BundleSkuCatalog
,p.ComponentProducts as ComponentProduct
,bpf.SalePriceStartDateTime
,bpf.SalePriceEndDateTime
,bpf.SaleReference
,bpf.SalePrice
, case when SalePrice is null then 'List'
	else 'Sale'
	end as ComponentProductPricetype
from [dbo].[PimBundleSkuExtract] p (nolock) 
join SaleBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
left join [WEB].[BundleSalePrice] bpf (nolock) on bpf.StyleCode = p.ComponentProducts  and bpf.Catalog = p.Catalog and bpf.Catalog = e.BundleSkuCatalog
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter
)

select 
--s.BundleSku
cast(s.ComponentProduct as varchar (150)) as BundleSku
,s.BundleSkuCatalog
--,s.ClearancePriceStartDateTime
,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
--,s.ClearancePriceEndDateTime
,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
--,s.ClearanceReference
,s.SalePrice as BundleSkuSalePrice
--,s.ComponentProductPricetype
,null as XmlPricebookId
from Summary1 s 
where 1=1
and ComponentProductPricetype = 'Sale'

*/

-- Per Bryce on 8/27/2024 he needs all SKUs in the upload files his team is creating regardles if they belong a bundle 
-- never mentioned this before, poor requirements gathering on his part 
-- Keeping Code above in case it is needed in the future 

select 
 s.StyleCode as BundleSku
,s.Catalog as BundleSkuCatalog
--,s.SalePriceStartDateTime
,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
--,s.SalePriceEndDateTime
,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
,s.SalePrice as BundleSkuSalePrice
,null as XmlPricebookId
from [WEB].[BundleSalePrice] s
where 1=1
and s.catalog  = 'UK'
group by 
 s.StyleCode
,s.SalePrice
,s.Catalog
,s.SaleReference
,s.SalePriceStartDateTime
,s.SalePriceEndDateTime
order by 2 desc, 1
```

#### OLE DB Source - IntStaging - Sql Cmd - Price Table — SqlCommand

```sql
select 
 --f.UnionSource
f.BundleSku
,f.BundleSkuCatalog
--,f.SalePriceStartDateTime
--,CONVERT(VARCHAR(50), CAST(f.SalePriceStartDateTime AS DATETIMEOFFSET), 127) as SalePriceStartDateTime
,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f.SalePriceEndDateTime
--,f.SalePriceEndDateTime
--,CONVERT(VARCHAR(50), CAST(f.SalePriceEndDateTime AS DATETIMEOFFSET), 127) as SalePriceEndDateTime
,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
,f.BundSkuSalePrice
--,f.BundleSkuListPrice
--,f.InsertDate
--,f.UpdateDate
,null as XmlPricebookId
 from  WEB.BundleSalePriceFact f
 where 1=1
 and f.BundleSkuCatalog = 'UK'
```

#### OLE DB Source - IntStaging - Component Skus — SqlCommand

```sql
/*With SaleBundles as 
(
select 
f.BundleSku
,BundleSkuCatalog
from [WEB].[BundleSalePriceFact] f
where 1=1
and f.BundleSkuCatalog = 'US'
group by 
f.BundleSku
,BundleSkuCatalog
)
, Summary1 as (
select 
e.BundleSku
,e.BundleSkuCatalog
,p.ComponentProducts as ComponentProduct
,bpf.SalePriceStartDateTime
,bpf.SalePriceEndDateTime
,bpf.SaleReference
,bpf.SalePrice
, case when SalePrice is null then 'List'
	else 'Sale'
	end as ComponentProductPricetype
from [dbo].[PimBundleSkuExtract] p (nolock) 
join SaleBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
left join [WEB].[BundleSalePrice] bpf (nolock) on bpf.StyleCode = p.ComponentProducts  and bpf.Catalog = p.Catalog and bpf.Catalog = e.BundleSkuCatalog
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter
)

select 
--s.BundleSku
cast(s.ComponentProduct as varchar (150)) as BundleSku
,s.BundleSkuCatalog
--,s.ClearancePriceStartDateTime
,CONVERT (varchar,s.SalePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
--,s.ClearancePriceEndDateTime
,CONVERT (varchar,s.SalePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
--,s.ClearanceReference
,s.SalePrice as BundleSkuSalePrice
--,s.ComponentProductPricetype
,null as XmlPricebookId
from Summary1 s 
where 1=1
and ComponentProductPricetype = 'Sale'

*/
-- Per Bryce on 8/27/2024 he needs all SKUs in the upload files his team is creating regardles if they belong a bundle 
-- never mentioned this before, poor requirements gathering on his part 
-- Keeping Code above in case it is needed in the future 

select 
 s.StyleCode as BundleSku
,s.Catalog as BundleSkuCatalog
--,s.SalePriceStartDateTime
,CONVERT (varchar,s.SalePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
--,s.SalePriceEndDateTime
,CONVERT (varchar,s.SalePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
,s.SalePrice as BundleSkuSalePrice
,null as XmlPricebookId
from [WEB].[BundleSalePrice] s
where 1=1
and s.catalog  = 'US'
group by 
 s.StyleCode
,s.SalePrice
,s.Catalog
,s.SaleReference
,s.SalePriceStartDateTime
,s.SalePriceEndDateTime
order by 2 desc, 1
```

#### OLE DB Source - IntStaging - Sql Cmd - Price Table — SqlCommand

```sql
select 
 --f.UnionSource
f.BundleSku
,f.BundleSkuCatalog
--,f.SalePriceStartDateTime
--,CONVERT(VARCHAR(50), CAST(f.SalePriceStartDateTime AS DATETIMEOFFSET), 127) as SalePriceStartDateTime
,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f.SalePriceEndDateTime
--,CONVERT(VARCHAR(50), CAST(f.SalePriceEndDateTime AS DATETIMEOFFSET), 127) as SalePriceEndDateTime
,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
,f.BundSkuSalePrice
--,f.BundleSkuListPrice
--,f.InsertDate
--,f.UpdateDate
,null as XmlPricebookId
 from  WEB.BundleSalePriceFact f
 where 1=1
 and f.BundleSkuCatalog = 'US'
```

#### OLE DB Source - IntStaging - SQL Cmd — SqlCommand

```sql
With ListBundles as 
(
select 
f.BundleSku
,BundleSkuCatalog
from WEB.PricebookBundleSkuFact f
where 1=1
--and f.BundleSku in ('26808_26808_26808_26808','26907_26907_26907_26907','28389_28389_28389') -- Testing Purposes Only 
group by 
f.BundleSku
,BundleSkuCatalog
)

,Summary1 as (

select 
e.BundleSku
,e.BundleSkuCatalog
,p.ComponentProducts as ComponentProduct
,bpf.ClearancePriceStartDateTime
,bpf.ClearancePriceEndDateTime
,bpf.ClearanceReference
,bpf.ClearancePrice
, case when ClearancePrice is null then 'List'
	else 'Clearance'
	end as ComponentProductPricetype
,p.ComponentQuantity -- Added 9/26/2024 as part of JIRA BIB-1024
from [dbo].[PimBundleSkuExtract] p (nolock) 
join ListBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
left join [WEB].[BundleClearancePrice] bpf (nolock) on bpf.StyleCode = p.ComponentProducts  and bpf.Catalog = p.Catalog and bpf.Catalog = e.BundleSkuCatalog
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter
--and e.BundleSku in ('28750_16869_28706_30028') -- Testing Filter
) 
, 
BundlesWithClearance as (
select  
s.BundleSku,
BundleSkuCatalog
from Summary1 s
where 1=1
and s.ClearancePrice is not null 
group by 
s.BundleSku,
BundleSkuCatalog

) 

, ListPrices as (
select
e.BundleSku
,e.BundleSkuCatalog
,pf.style_code as ListPriceStyleCode
,pf.CurrentPrice as ListCurrentPrice
,pf.SalePrice as ListSalePrice
from [dbo].[PimBundleSkuExtract] p (nolock) 
join ListBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
join web.PricebookFact pf (nolock) on pf.style_code = p.ComponentProducts  and pf.Catalog = p.catalog 
join BundlesWithClearance bs on bs.BundleSku = e.BundleSku and bs.BundleSkuCatalog = e.BundleSkuCatalog
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter
) 

, PricingSummary as (
select 
s.BundleSku
,s.BundleSkuCatalog
,s.ComponentProduct
,s.ClearancePriceStartDateTime
,s.ClearancePriceEndDateTime
,s.ClearanceReference
,s.ClearancePrice
,s.ComponentProductPricetype
,lp.ListCurrentPrice
,lp.ListSalePrice
,s.ComponentQuantity -- Added 9/26/2024 as part of JIRA BIB-1024
, rank ()over (partition by s.BundleSku order by s.ComponentProduct) as Rank
, dense_rank ()over (partition by s.BundleSku order by s.ComponentProduct, s.ClearancePriceStartDateTime) as DenseRank
from Summary1  s
join ListPrices lp on lp.BundleSku = s.BundleSku and lp.BundleSkuCatalog= s.BundleSkuCatalog and lp.ListPriceStyleCode = s.ComponentProduct
--order by 2, 1, 3 , 4

) 

,FinalSummary as (
Select 
m.BundleSku
,m.BundleSkuCatalog
,min (m.ClearancePriceStartDateTime) as ClearancePriceStartDateTime
,max (m.ClearancePriceEndDateTime) as ClearancePriceEndDateTime
--,sum(isnull(m.ClearancePrice, isnull(m.ListSalePrice,m.ListCurrentPrice))) as Price -- Replaced  9/26/2024 as part of JIRA BIB-1024
,sum(isnull	(m.ClearancePrice*ComponentQuantity, isnull(	m.ListSalePrice*ComponentQuantity,m.ListCurrentPrice*ComponentQuantity))) as Price -- 9/26/2024 as part of JIRA BIB-1024
from PricingSummary m
group by 
m.BundleSku
,m.BundleSkuCatalog
)

Select 
s.BundleSku
,s.BundleSkuCatalog
,s.ClearancePriceStartDateTime
,s.ClearancePriceEndDateTime
,s.Price as BundleSkuClearancePrice
,f.BundleSkuPrice as BundleSkuListPrice
from FinalSummary s
join web.PricebookBundleSkuFact f on f.BundleSku = s.BundleSku and f.BundleSkuCatalog = s.BundleSkuCatalog
where 1=1
--and s.SalePriceStartDateTime is not null 
--and s.BundleSkuCatalog = 'US'
order by 3 desc ,2, 4
```

#### OLE DB Source - IntStaging - SQL Cmd — SqlCommand

```sql
/*-- Exclude Duplicates Approach 
With Duplicates as 
(
select 
s.DerivedStyleCode
,s.Catalog
from [WEB].[BundleClearancePriceStage] s
group by 
DerivedStyleCode
,s.Catalog
having count (*) > 1
) 

select 
case when s.catalog  = 'UK' and len(sku) < 6 
		then concat ('4',right(s.DerivedStyleCode,5)) 
	else s.DerivedStyleCode
end as StyleCode
,s.Retail as ClearancePrice
,s.Catalog
,s.reference as ClearanceReference
,s.DerivedStartDateTime as ClearancePriceStartDateTime
,s.DerivedEndDateTime as ClearancePriceEndDateTime
from [WEB].[BundleClearancePriceStage] s
left join Duplicates d on d.DerivedStyleCode = s.DerivedStyleCode and d.Catalog = s.Catalog
where 1=1
and d.DerivedStyleCode is null -- 
order by 
3 desc, 
1
*/


-- Take Min Price , Min Start Date and Max Date Approach 

select 
case when s.catalog  = 'UK' and len(sku) < 6 
		then concat ('4',right(s.DerivedStyleCode,5)) 
	else s.DerivedStyleCode
end as StyleCode
,min(s.Retail) as ClearancePrice
,s.Catalog
,s.reference as ClearanceReference
,min(s.DerivedStartDateTime) as ClearancePriceStartDateTime
,max(s.DerivedEndDateTime) as ClearancePriceEndDateTime
from [WEB].[BundleClearancePriceStage] s
where 1=1
group by 
case when s.catalog  = 'UK' and len(sku) < 6 
		then concat ('4',right(s.DerivedStyleCode,5)) 
	else s.DerivedStyleCode
end 
,s.Catalog
,s.reference
```

#### OLE DB Source — SqlCommand

```sql
/*
With ClearanceBundles as 
(
select 
f.BundleSku
,BundleSkuCatalog
from [WEB].[BundleClearancePriceFact] f
where 1=1
and f.BundleSkuCatalog = 'UK'
group by 
f.BundleSku
,BundleSkuCatalog
)
, Summary1 as (
select 
e.BundleSku
,e.BundleSkuCatalog
,p.ComponentProducts as ComponentProduct
,bpf.ClearancePriceStartDateTime
,bpf.ClearancePriceEndDateTime
,bpf.ClearanceReference
,bpf.ClearancePrice
, case when ClearancePrice is null then 'List'
	else 'Clearance'
	end as ComponentProductPricetype
from [dbo].[PimBundleSkuExtract] p (nolock) 
join ClearanceBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
left join [WEB].[BundleClearancePrice] bpf (nolock) on bpf.StyleCode = p.ComponentProducts  and bpf.Catalog = p.Catalog and bpf.Catalog = e.BundleSkuCatalog
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter
)

select 
--s.BundleSku
cast(s.ComponentProduct as varchar (150)) as BundleSku
,s.BundleSkuCatalog
--,s.ClearancePriceStartDateTime
,CONVERT (varchar,s.ClearancePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
--,s.ClearancePriceEndDateTime
,CONVERT (varchar,s.ClearancePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
--,s.ClearanceReference
,s.ClearancePrice as BundleSkuClearancePrice
--,s.ComponentProductPricetype
,null as XmlPricebookId
from Summary1 s 
where 1=1
and ComponentProductPricetype = 'Clearance'

*/

-- Per Bryce on 8/27/2024 he needs all SKUs in the upload files his team is creating regardles if they belong a bundle 
-- never mentioned this before, poor requirements gathering on his part 
-- Keeping Code above in case it is needed in the future 

select 
 s.StyleCode as BundleSku
,s.Catalog as BundleSkuCatalog
--,s.SalePriceStartDateTime
,CONVERT (varchar,s.ClearancePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
--,s.SalePriceEndDateTime
,CONVERT (varchar,s.ClearancePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
,s.ClearancePrice as BundleSkuClearancePrice
,null as XmlPricebookId
from [WEB].[BundleClearancePrice] s
where 1=1
and s.catalog  = 'UK'
group by 
 s.StyleCode
,s.ClearancePrice
,s.Catalog
,s.ClearancePriceStartDateTime
,s.ClearancePriceEndDateTime
order by 2 desc, 1
```

#### OLE DB Source - Dummy Cmd — SqlCommand

```sql
select getdate () as GetDate
```

#### OLE DB Source - IntStaging - Lines — SqlCommand

```sql
select 
 --f.UnionSource
f.BundleSku
,f.BundleSkuCatalog
--,f.ClearancePriceStartDateTime
--,CONVERT(VARCHAR(50), CAST(f.ClearancePriceStartDateTime AS DATETIMEOFFSET), 127) as SalePriceStartDateTime
,CONVERT (varchar,f.ClearancePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
--,f.SalePriceEndDateTime
--,CONVERT(VARCHAR(50), CAST(f.ClearancePriceEndDateTime AS DATETIMEOFFSET), 127) as SalePriceEndDateTime
,CONVERT (varchar,f.ClearancePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
,f.BundleSkuClearancePrice
--,f.BundleSkuListPrice
--,f.InsertDate
--,f.UpdateDate
,null  as XmlPricebookId
 from  [WEB].[BundleClearancePriceFact] f
 where 1=1
 and f.BundleSkuCatalog = 'UK'
```

#### OLE DB Source - IntStaging - Component Skus — SqlCommand

```sql
/*
With ClearanceBundles as 
(
select 
f.BundleSku
,BundleSkuCatalog
from [WEB].[BundleClearancePriceFact] f
where 1=1
and f.BundleSkuCatalog = 'US'
group by 
f.BundleSku
,BundleSkuCatalog
)
, Summary1 as (
select 
e.BundleSku
,e.BundleSkuCatalog
,p.ComponentProducts as ComponentProduct
,bpf.ClearancePriceStartDateTime
,bpf.ClearancePriceEndDateTime
,bpf.ClearanceReference
,bpf.ClearancePrice
, case when ClearancePrice is null then 'List'
	else 'Clearance'
	end as ComponentProductPricetype
from [dbo].[PimBundleSkuExtract] p (nolock) 
join ClearanceBundles e on e.BundleSku = p.LocalProductCode and e.BundleSkuCatalog = p.catalog 
left join [WEB].[BundleClearancePrice] bpf (nolock) on bpf.StyleCode = p.ComponentProducts  and bpf.Catalog = p.Catalog and bpf.Catalog = e.BundleSkuCatalog
where 1=1
and p.GroupingType = 'Bundle' -- Mandatory Filter
)

select 
--s.BundleSku
cast(s.ComponentProduct as varchar (150)) as BundleSku
,s.BundleSkuCatalog
--,s.ClearancePriceStartDateTime
,CONVERT (varchar,s.ClearancePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
--,s.ClearancePriceEndDateTime
,CONVERT (varchar,s.ClearancePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
--,s.ClearanceReference
,s.ClearancePrice as BundleSkuClearancePrice
--,s.ComponentProductPricetype
,null as XmlPricebookId
from Summary1 s 
where 1=1
and ComponentProductPricetype = 'Clearance'
*/

-- Per Bryce on 8/27/2024 he needs all SKUs in the upload files his team is creating regardles if they belong a bundle 
-- never mentioned this before, poor requirements gathering on his part 
-- Keeping Code above in case it is needed in the future 

select 
 s.StyleCode as BundleSku
,s.Catalog as BundleSkuCatalog
--,s.SalePriceStartDateTime
,CONVERT (varchar,s.ClearancePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
--,s.SalePriceEndDateTime
,CONVERT (varchar,s.ClearancePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
,s.ClearancePrice as BundleSkuClearancePrice
,null as XmlPricebookId
from [WEB].[BundleClearancePrice] s
where 1=1
and s.catalog  = 'US'
group by 
 s.StyleCode
,s.ClearancePrice
,s.Catalog
,s.ClearancePriceStartDateTime
,s.ClearancePriceEndDateTime
order by 2 desc, 1
```

#### OLE DB Source - IntStaging - Lines — SqlCommand

```sql
select 
 --f.UnionSource
f.BundleSku
,f.BundleSkuCatalog
--,f.ClearancePriceStartDateTime
--,CONVERT(VARCHAR(50), CAST(f.ClearancePriceStartDateTime AS DATETIMEOFFSET), 127) as SalePriceStartDateTime
,CONVERT (varchar,f.ClearancePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
--,f.ClearancePriceEndDateTime
--,CONVERT(VARCHAR(50), CAST(f.ClearancePriceEndDateTime AS DATETIMEOFFSET), 127) as SalePriceEndDateTime
,CONVERT (varchar,f.ClearancePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceEndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion
,f.BundleSkuClearancePrice
--,f.BundleSkuListPrice
--,f.InsertDate
--,f.UpdateDate
,null as XmlPricebookId
 from  [WEB].[BundleClearancePriceFact] f
 where 1=1
 and f.BundleSkuCatalog = 'US'
```

#### OLE DB Source - IntStaging -  UK Bundle Return — SqlCommand

```sql
select 
f.BundleSku as Sku
,cast (1 as int) as Quantity
,f.BundSkuSalePrice as Retail
,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127)  as StartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f.SalePriceEndDateTime
,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as EndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
,'' as Reference 
 from  WEB.BundleSalePriceFact f
 where 1=1
 and f.BundleSkuCatalog = 'UK'
```

#### OLE DB Source - IntStaging -  UK Component Return — SqlCommand

```sql
-- Will need this to capture Quantity Information once multi qty component skus is enable 
With Stage as 

(
select 
s.DerivedStyleCode
,s.Retail
,s.catalog
,s.DerivedStartDateTime
,s.DerivedEndDateTime
,s.Quantity
from WEB.BundleSalePriceStage s
where 1=1
and s.catalog  = 'UK'
group by 
s.DerivedStyleCode
,s.Retail
,s.catalog
,s.DerivedStartDateTime
,s.DerivedEndDateTime
,s.Quantity

)


select
s.StyleCode as Sku
--,cast (st.Quantity as int) as Quantity -- Hardcoding Quantity until I have the qty requirement added 
,cast (1 as int) as Quantity 
,s.SalePrice as Retail
,s.Catalog
,s.SaleReference
--,s.SalePriceStartDateTime as StartDateTime
,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as StartDateTime
--,s.SalePriceEndDateTime as EndDateTime
,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as EndDateTime
,s.SaleReference as Reference 
from [WEB].[BundleSalePrice] s
join Stage st on st.DerivedStyleCode = s.StyleCode 
	and st.Catalog = s.Catalog 
	and st.Retail = s.SalePrice 
	and st.DerivedStartDateTime = s.SalePriceStartDateTime 
	and st.DerivedEndDateTime = s.SalePriceEndDateTime
where 1=1
and s.catalog  = 'UK'
group by 
s.StyleCode
--,cast (st.Quantity as int) -- Hardcoding Quantity until I have the qty requirement added 
,s.SalePrice
,s.Catalog
,s.SaleReference
,s.SalePriceStartDateTime
,s.SalePriceEndDateTime
,s.SaleReference
order by 1
```

#### OLE DB Source - IntStaging -  US Bundle Return — SqlCommand

```sql
select 
f.BundleSku as Sku
,cast (1 as int) as Quantity
,f.BundSkuSalePrice as Retail
,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as StartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f.SalePriceEndDateTime
,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as EndDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion 
,'' as Reference 
 from  WEB.BundleSalePriceFact f
 where 1=1
 and f.BundleSkuCatalog = 'US'
```

#### OLE DB Source - IntStaging -  US Component Return — SqlCommand

```sql
-- Will need this to capture Quantity Information once multi qty component skus is enable 
With Stage as 

(
select 
s.DerivedStyleCode
,s.Retail
,s.catalog
,s.DerivedStartDateTime
,s.DerivedEndDateTime
,s.Quantity
from WEB.BundleSalePriceStage s
where 1=1
and s.catalog  = 'US'
group by 
s.DerivedStyleCode
,s.Retail
,s.catalog
,s.DerivedStartDateTime
,s.DerivedEndDateTime
,s.Quantity

)


select
s.StyleCode as Sku
--,cast (st.Quantity as int) as Quantity -- Hardcoding Quantity until I have the qty requirement added 
,cast (1 as int) as Quantity 
,s.SalePrice as Retail
,s.Catalog
,s.SaleReference
--,s.SalePriceStartDateTime as StartDateTime
,CONVERT (varchar,s.SalePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as StartDateTime
--,s.SalePriceEndDateTime as EndDateTime
,CONVERT (varchar,s.SalePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as EndDateTime
,s.SaleReference as Reference 
from [WEB].[BundleSalePrice] s
join Stage st on st.DerivedStyleCode = s.StyleCode 
	and st.Catalog = s.Catalog 
	and st.Retail = s.SalePrice 
	and st.DerivedStartDateTime = s.SalePriceStartDateTime 
	and st.DerivedEndDateTime = s.SalePriceEndDateTime
where 1=1
and s.catalog  = 'US'
group by 
s.StyleCode
--,cast (st.Quantity as int) -- Hardcoding Quantity until I have the qty requirement added 
,s.SalePrice
,s.Catalog
,s.SaleReference
,s.SalePriceStartDateTime
,s.SalePriceEndDateTime
,s.SaleReference
order by 1
```

#### OLE DB Source - IntStaging - PimBundleSkuExtract SQL Cmd — SqlCommand

```sql
with ValidBundlesStage as (
select 
s.PrimaryId,
count (s.UsComponentProducts) as CountComponentProducts, 
LEN(s.PrimaryId) - LEN(REPLACE(s.PrimaryId, '_', '')) + 1 as ExpectedSkuCount -- I do +1 as there is no leading underscore
from PimBundleSkuExtractStage s
where 1=1
and s.UsComponentProducts <> '' -- Filtering Out Any rows where the Ind Sku field is empty -
and s.UsComponentProducts not like '%[_]%' -- We will not Allow Any Records where the Ind Sku Field is a bundled SKU 
group by 
s.PrimaryId

) , 

ValidBundles as 
(
select 
vb.PrimaryId, 
vb.CountComponentProducts, 
vb.ExpectedSkuCount

from ValidBundlesStage vb
where 1=1
and vb.CountComponentProducts = vb.ExpectedSkuCount -- Balanced Bundle Rows Only 
group by 
vb.PrimaryId, 
vb.CountComponentProducts, 
vb.ExpectedSkuCount


) , 

Summary1 as (

select
s.PrimaryId, 
s.UsLocalProductCode, 
s.KeyStory, 
s.GroupingType, 
s.UkMSTAT, 
s.UsMSTAT, 
s.UkLocalProductCode, 
s.UsComponentProducts, 
s.UsDisplayName, 
s.UkComponentProducts, 
s.UkDisplayName,
case when len(s.UsComponentProducts) = 5
		then concat('0',s.UsComponentProducts) 
	when len(s.UsComponentProducts) = 6
			then s.UsComponentProducts
		end as DerivedUsStyleCode, 
--case when len(s.UsComponentProducts) = 5
--		then concat('4',s.UsComponentProducts) 
--	when len(s.UsComponentProducts) = 6
--		then concat(left (UkLocalProductCode,1), right (s.UsComponentProducts,5))
--		end as DerivedUkStyleCode	-- Replaced on 7/31/2024 -- May be flawed 
case when len(s.UkComponentProducts) = 5
		then concat('4',s.UkComponentProducts) 
	when len(s.UkComponentProducts) = 6
		then s.UkComponentProducts
		end as DerivedUkStyleCode	-- Replaced above on 7/31/2024 
from PimBundleSkuExtractStage s
join ValidBundles vbs on vbs.Primaryid = s.PrimaryId
where 1=1
--and len(s.UsComponentProducts) =  6

) 

select 
--s.UkMSTAT, 
--s.UsMSTAT, 
s.PrimaryId, 
s.KeyStory, 
s.GroupingType, 
s.UsLocalProductCode, 
s.UsComponentProducts, 
cast (s.DerivedUsStyleCode as varchar (12)) as DerivedUsStyleCode , 
s.UsDisplayName, 
s.UkLocalProductCode, 
s.UkComponentProducts, 
cast (s.DerivedUkStyleCode as varchar (12)) as DerivedUkStyleCode , 
s.UkDisplayName, 
--vb.PrimaryId, 
vb.CountComponentProducts
--,vb.ExpectedSkuCount

from Summary1 s 
join ValidBundles vb on vb.PrimaryId = s.PrimaryId
where 1=1
order by 
s.PrimaryId, 
s.UsComponentProducts
```

#### OLE DB Source - IntStaging - SQL Cmd — SqlCommand

```sql
with ValidBundlesStage as 
(
select 
s.PrimaryId
,s.Catalog
,count (distinct s.ComponentProducts) as CountComponentProductsDistinct -- Renamed  as Part of JIRA BIB-1024 
,sum (case when s.ComponentQuantity <> 1 then 1*s.ComponentQuantity	else 1 end ) as CountComponentProducts -- Added as Part of JIRA BIB-1024 
,LEN(s.PrimaryId) - LEN(REPLACE(s.PrimaryId, '_', '')) + 1 as ExpectedSkuCount -- I do +1 as there is no leading underscore
from [PimBundleSkuExtractStageConsolidated] s
where 1=1
group by 
s.PrimaryId
,s.Catalog

) ,


ValidBundles as (
select 
vb.PrimaryId
,vb.Catalog
,vb.CountComponentProducts
,vb.ExpectedSkuCount
,vb.CountComponentProductsDistinct
from ValidBundlesStage vb
where 1=1
and vb.CountComponentProducts = vb.ExpectedSkuCount -- Balanced Bundle Rows Only 
group by 
vb.PrimaryId 
,vb.Catalog
,vb.CountComponentProducts
,vb.ExpectedSkuCount
,vb.CountComponentProductsDistinct
) , 

Summary1 as 

(


select 
 s.PrimaryId
,s.LocalProductCode
,s.KeyStory
,s.GroupingType
,s.MSTAT
,s.ComponentProducts
,s.DisplayName
,s.Catalog
,s.ComponentQuantity

from PimBundleSkuExtractStageConsolidated s
join ValidBundles vbs on vbs.Primaryid = s.PrimaryId and vbs.Catalog=s.Catalog
where 1=1

) 

select 
s.PrimaryId
,s.LocalProductCode
,s.KeyStory
,s.GroupingType
,s.MSTAT
,s.ComponentProducts
,s.DisplayName
,s.Catalog
--,vb.CountComponentProducts
,vb.CountComponentProductsDistinct as CountComponentProducts -- Replaced Above on 9/26/2024 as related to JIRA BIB 1024
,s.ComponentQuantity
From Summary1 s
join ValidBundles vb on vb.PrimaryId = s.PrimaryId and vb.Catalog = s.Catalog
where 1=1
```

#### OLE DB Source - IntStaging - SQL Cmd — SqlCommand

```sql
with DataStage as 
(
select 
us.PrimaryId
,us.USLocalProductCode as LocalProductCode
,us.KeyStory 
,us.GroupingType
,us.UsMSTAT as MSTAT
,us.UsComponentProducts as ComponentProducts
,us.UsDisplayName as DisplayName
,us.Catalog
,case when us.UsComponentQuantity = ''
	then 1
else us.UsComponentQuantity end as ComponentQuantity
from [PimBundleSkuExtractStageUs] us
where 1=1
and us.UsComponentProducts <> ''
and us.UsComponentProducts not like '%[_]%'
union 
select 
uk.PrimaryId
,uk.UkLocalProductCode as LocalProductCode
,uk.KeyStory 
,uk.GroupingType
,uk.UkMSTAT as MSTAT
,uk.UkComponentProducts as ComponentProducts
,uk.UkDisplayName as DisplayName
,uk.Catalog
,case when uk.UkComponentQuantity = ''
	then 1
else uk.UkComponentQuantity end as ComponentQuantity
from [PimBundleSkuExtractStageUk] uk
where 1=1
and uk.UkComponentProducts <> ''
and uk.UkComponentProducts not like '%[_]%'

)

select
PrimaryId
,LocalProductCode
,KeyStory
,GroupingType
,MSTAT
,ComponentProducts
,DisplayName
,Catalog
,cast (ComponentQuantity as int) as ComponentQuantity
from DataStage
order by 1
```

#### OLE DB Source - IntStaging - SqlCommand — SqlCommand

```sql
with EligibleBundleStage as (
select 
p.PrimaryId 
,p.CountComponentProducts
,pf.Catalog
,sum (case when pf.style_code is null then 0 
		when pf.style_code is not null then 1
		end ) as PricebookFactRowCount
from [dbo].[PimBundleSkuExtract] p (nolock) 
join web.PricebookFact pf (nolock) on pf.style_code = p.ComponentProducts and pf.Catalog =  p.Catalog 
where 1=1
--and 
--(
--	p.LocalProductCode = '32498_32495_22920_22920' -- Example of new qty bundle 
-- or
-- p.LocalProductCode = '225448_25681_25626' -- non qty bundle, do not break 
--or 
-- p.localproductcode = '21991_28442_28212_28198_28443_27970_28445_27025' -- Example of an incomplete bundle , we do not have pricebook entries for all records

-- ) -- Testing Purposes 
group by 
p.primaryid, 
p.CountComponentProducts,
pf.Catalog


), 

EligibleBundles as 
(

select
eb.PrimaryId, 
eb.Catalog

from EligibleBundleStage eb 
where 1=1
and eb.PricebookFactRowCount = eb.CountComponentProducts
group by 
eb.PrimaryId, 
eb.Catalog

), 

Summary1 as 
(

select
p.PrimaryId as BundleSku, 
p.KeyStory, 
p.GroupingType, 
p.LocalProductCode as BundleLocalProductCode, 
p.ComponentProducts as BundleComponentProducts, 
p.DisplayName as BundleDisplayName, 
p.CountComponentProducts,
pf.style_code as PriceBookStyleCode, 
pf.CurrentPrice, 
pf.OriginalPrice, 
pf.SalePrice, 
pf.Catalog as PriceBookCatalog, 
p.ComponentQuantity
from [dbo].[PimBundleSkuExtract] p (nolock) 
join EligibleBundles e on e.PrimaryId = p.PrimaryId and e.Catalog = p.catalog 
join web.PricebookFact pf (nolock) on pf.style_code = p.ComponentProducts  and pf.Catalog = p.catalog 
	
)

Select 
--s.BundleSku, 
case when s.BundleLocalProductCode = ''
		then s.BundleSku 
	else s.BundleLocalProductCode 
end as BundleSku,   -- Bryce Ahrens Advised that they will Need the Local Product Code for the Bundle Sku , in addition had to work through when local product code may be empty
s.KeyStory, 
s.GroupingType, 
s.BundleLocalProductCode, 
s.BundleComponentProducts, 
s.BundleDisplayName, 
s.CountComponentProducts, 
s.PriceBookStyleCode, 
s.CurrentPrice as PriceBookCurrentPrice, 
s.OriginalPrice as PriceBookOriginalPrice, 
s.SalePrice as PriceBookSalePrice, 
s.PriceBookCatalog, 
s.ComponentQuantity
from Summary1 s
where 1=1
group by 
case when s.BundleLocalProductCode = ''
		then s.BundleSku 
	else s.BundleLocalProductCode 
end ,   -- Bryce Ahrens Advised that they will Need the Local Product Code for the Bundle Sku , in addition had to work through when local product code may be empty
s.KeyStory, 
s.GroupingType, 
s.BundleLocalProductCode, 
s.BundleComponentProducts, 
s.BundleDisplayName, 
s.CountComponentProducts, 
s.PriceBookStyleCode, 
s.CurrentPrice , 
s.OriginalPrice , 
s.SalePrice, 
s.PriceBookCatalog,
s.ComponentQuantity
order by 1
```

## Data Flow: Destinations

| Component | Target Table | Type | Data Flow Task | Connection | SQL Kind |
|---|---|---|---|---|---|
| OLE DB Destination - IntStaging - WEB-BundleSalePriceFact |  | OLEDBDestination | Data Flow Task - Build Sale Bundle Fact Table - New Oct 4 2024 | IntegrationStaging |  |
| OLE DB Destination - IntStaging - WEB-BundleSalePriceFact |  | OLEDBDestination | Data Flow Task - Build Sale Bundle Fact Table - Old | IntegrationStaging |  |
| OLE DB Destination - IntStaging - WebBundleSalePrice |  | OLEDBDestination | Data Flow Task - Cleanse | IntegrationStaging |  |
| OLE DB Destination - WebBundleSalePriceStage |  | OLEDBDestination | Data Flow Task | IntegrationStaging |  |
| OLE DB Destination - WebBundleSalePriceStage |  | OLEDBDestination | Data Flow Task | IntegrationStaging |  |
| OLE DB Destination - IntStaging - WebBundleClearancePriceFact |  | OLEDBDestination | Data Flow Task - Build Clearance Bundle Fact Table | IntegrationStaging |  |
| OLE DB Destination - IntStaging - WebBundleClearancePrice |  | OLEDBDestination | Data Flow Task - Cleanse - Handle Duplicates | IntegrationStaging |  |
| OLE DB Destination - IntStaging - WebBundleClearancePriceStage |  | OLEDBDestination | Data Flow Task | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Data Flow Task | IntegrationStaging |  |
| Flat File Destination - UK_GlobalE_BundlesCsv |  | FlatFileDestination | Data Flow Task | UK_GlobalE_BundlesCsv |  |
| Flat File Destination - UK_GlobalE_ComponentCsv |  | FlatFileDestination | Data Flow Task | UK_GlobalE_ComponentCsv |  |
| Flat File Destination - US_GlobalE_BundleCsv |  | FlatFileDestination | Data Flow Task | US_GlobalE_BundleCsv |  |
| Flat File Destination - US_GlobalE_ComponentCsv |  | FlatFileDestination | Data Flow Task | US_GlobalE_ComponentCsv |  |
| OLE DB Destination |  | OLEDBDestination | Data Flow Task | IntegrationStaging |  |
| OLE DB Destination - IntStaging - PimBundleSkuExtractCleansed |  | OLEDBDestination | Data Flow Task - Cleanse and Derive | IntegrationStaging |  |
| OLE DB Destination |  | OLEDBDestination | Data Flow Task - File to Stage | IntegrationStaging |  |
| OLE DB Destination - IntStaging - PimBundleSkuExtractStage |  | OLEDBDestination | Data Flow Task - File to Stage | IntegrationStaging |  |
| OLE DB Destination - IntStaging - PimBundleSkuExtractStageConsolidatedAndCleansed |  | OLEDBDestination | Data Flow Task - Cleanse | IntegrationStaging |  |
| OLE DB Destination - IntStaging - PimBundleSkuExtractStageConsolidated |  | OLEDBDestination | Data Flow Task - Consolidate | IntegrationStaging |  |
| OLE DB Destination - IntStaging - PimBundleSkuExtractStageUK |  | OLEDBDestination | Data Flow Task | IntegrationStaging |  |
| OLE DB Destination - PimBundleSkuExtractStageUs |  | OLEDBDestination | Data Flow Task | IntegrationStaging |  |
| OLE DB Destination - IntStaging - Web-BundlePricebookFactPreStage |  | OLEDBDestination | Data Flow Task - BundleSkuExtract to PricebookFactBundlePreStage | IntegrationStaging |  |
| OLE DB Destination - IntStaging - WebPricebookFact |  | OLEDBDestination | Data Flow Task - Single Sku Pricebook | IntegrationStaging |  |
| OLE DB Destination - IntStaging - Dev |  | OLEDBDestination | Data Flow Task Bundle Pricebook | IntegrationStaging |  |
