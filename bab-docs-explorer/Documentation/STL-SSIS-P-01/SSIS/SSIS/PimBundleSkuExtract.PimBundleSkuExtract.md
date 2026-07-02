# SSIS Package: PimBundleSkuExtract

**Project:** PimBundleSkuExtract  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Archive_conn(["Archive [FILE]"])
        ArchiveClearance_conn(["ArchiveClearance [FILE]"])
        ArchiveFeedonomics_conn(["ArchiveFeedonomics [FILE]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        IntegrationStagingProdCopyingOnly_conn(["IntegrationStagingProdCopyingOnly [OLEDB]"])
        MissingBundlesCsv_conn(["MissingBundlesCsv [FLATFILE]"])
        PimCsv_conn(["PimCsv [FLATFILE]"])
        PimCsvUk_conn(["PimCsvUk [FLATFILE]"])
        PimCsvUkQty_conn(["PimCsvUkQty [FLATFILE]"])
        PimCsvUs_conn(["PimCsvUs [FLATFILE]"])
        PimCsvUsQty_conn(["PimCsvUsQty [FLATFILE]"])
        SMTP_conn(["SMTP [SMTP]"])
        UkClearancePriceCsv_conn(["UkClearancePriceCsv [FLATFILE]"])
        UkSalePriceCsv_conn(["UkSalePriceCsv [FLATFILE]"])
        UK_GlobalE_BundlesCsv_conn(["UK_GlobalE_BundlesCsv [FLATFILE]"])
        UK_GlobalE_ComponentCsv_conn(["UK_GlobalE_ComponentCsv [FLATFILE]"])
        UsClearancePriceCsv_conn(["UsClearancePriceCsv [FLATFILE]"])
        UsSalePriceCsv_conn(["UsSalePriceCsv [FLATFILE]"])
        US_GlobalE_BundleCsv_conn(["US_GlobalE_BundleCsv [FLATFILE]"])
        US_GlobalE_ComponentCsv_conn(["US_GlobalE_ComponentCsv [FLATFILE]"])
        XML_FILE_conn(["XML FILE [FILE]"])
        XML_FILE_Clearance_conn(["XML FILE Clearance [FILE]"])
    end
    subgraph ControlFlow
        PimBundleSkuExtract_task["PimBundleSkuExtract"]
        Execute_SQL_Task____Check_Time_task["Execute SQL Task  - Check Time"]
        PimBundleSkuExtract_task --> Execute_SQL_Task____Check_Time_task
        Faux_Control_task["Faux Control"]
        Execute_SQL_Task____Check_Time_task --> Faux_Control_task
        SeqCont___Bundle_Sale_Price_Extract_task["SeqCont - Bundle Sale Price Extract"]
        Faux_Control_task --> SeqCont___Bundle_Sale_Price_Extract_task
        Execute_SQL_Task___Truncate_Stage_task["Execute SQL Task - Truncate Stage"]
        SeqCont___Bundle_Sale_Price_Extract_task --> Execute_SQL_Task___Truncate_Stage_task
        SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data_task["SeqCont - Cleanse and Stage For Sale Pricebook XML generation  Data"]
        Execute_SQL_Task___Truncate_Stage_task --> SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data_task
        Data_Flow_Task___Build_Sale_Bundle_Fact_Table___New_Oct_4_2024_task["Data Flow Task - Build Sale Bundle Fact Table - New Oct 4 2024"]
        SeqCont___Cleanse_and_Stage_For_Sale_Pricebook_XML_generation__Data_task --> Data_Flow_Task___Build_Sale_Bundle_Fact_Table___New_Oct_4_2024_task
        Data_Flow_Task___Build_Sale_Bundle_Fact_Table___Old_task["Data Flow Task - Build Sale Bundle Fact Table - Old"]
        Data_Flow_Task___Build_Sale_Bundle_Fact_Table___New_Oct_4_2024_task --> Data_Flow_Task___Build_Sale_Bundle_Fact_Table___Old_task
        Data_Flow_Task___Cleanse_task["Data Flow Task - Cleanse"]
        Data_Flow_Task___Build_Sale_Bundle_Fact_Table___Old_task --> Data_Flow_Task___Cleanse_task
        SeqCont___Copy_and_Archive_Files_task["SeqCont - Copy and Archive Files"]
        Data_Flow_Task___Cleanse_task --> SeqCont___Copy_and_Archive_Files_task
        FEL___Copy_to_SFTP_and_Archive_task["FEL - Copy to SFTP and Archive"]
        SeqCont___Copy_and_Archive_Files_task --> FEL___Copy_to_SFTP_and_Archive_task
        File_System_Task___Archive_task["File System Task - Archive"]
        FEL___Copy_to_SFTP_and_Archive_task --> File_System_Task___Archive_task
        File_System_Task___Copy_to_Feedonomics_Directory_task["File System Task - Copy to Feedonomics Directory"]
        File_System_Task___Archive_task --> File_System_Task___Copy_to_Feedonomics_Directory_task
        File_System_Task___Copy_to_SFTP_Stage_task["File System Task - Copy to SFTP Stage"]
        File_System_Task___Copy_to_Feedonomics_Directory_task --> File_System_Task___Copy_to_SFTP_Stage_task
        SeqCont___Output_Sale_Pricebook_XML_Files_task["SeqCont - Output Sale Pricebook XML Files"]
        File_System_Task___Copy_to_SFTP_Stage_task --> SeqCont___Output_Sale_Pricebook_XML_Files_task
        Data_Flow_Task___UK_Sale_File_Generation_task["Data Flow Task - UK Sale File Generation"]
        SeqCont___Output_Sale_Pricebook_XML_Files_task --> Data_Flow_Task___UK_Sale_File_Generation_task
        Data_Flow_Task___US_Sale_File_Generation_task["Data Flow Task - US Sale File Generation"]
        Data_Flow_Task___UK_Sale_File_Generation_task --> Data_Flow_Task___US_Sale_File_Generation_task
        SeqCont___Process_Sale_Price_Files_task["SeqCont - Process Sale Price Files"]
        Data_Flow_Task___US_Sale_File_Generation_task --> SeqCont___Process_Sale_Price_Files_task
        FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___UK_task["FEL - Ingest and Archive Copy of Sale Price File - UK"]
        SeqCont___Process_Sale_Price_Files_task --> FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___UK_task
        Data_Flow_Task_task["Data Flow Task"]
        FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___UK_task --> Data_Flow_Task_task
        File_System_Task___Copy_File_task["File System Task - Copy File"]
        Data_Flow_Task_task --> File_System_Task___Copy_File_task
        FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___US_task["FEL - Ingest and Archive Copy of Sale Price File - US"]
        File_System_Task___Copy_File_task --> FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___US_task
        Data_Flow_Task_task["Data Flow Task"]
        FEL___Ingest_and_Archive_Copy_of_Sale_Price_File___US_task --> Data_Flow_Task_task
        File_System_Task___Copy_File_task["File System Task - Copy File"]
        Data_Flow_Task_task --> File_System_Task___Copy_File_task
        SeqCont___Clearance_Price_Extract_task["SeqCont - Clearance Price Extract"]
        File_System_Task___Copy_File_task --> SeqCont___Clearance_Price_Extract_task
        Execute_SQL_Task___Truncate_Stage_task["Execute SQL Task - Truncate Stage"]
        SeqCont___Clearance_Price_Extract_task --> Execute_SQL_Task___Truncate_Stage_task
        SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data_task["SeqCont - Cleanse and Stage for Clearance Pricebook Generation Data"]
        Execute_SQL_Task___Truncate_Stage_task --> SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data_task
        Data_Flow_Task___Build_Clearance_Bundle_Fact_Table_task["Data Flow Task - Build Clearance Bundle Fact Table"]
        SeqCont___Cleanse_and_Stage_for_Clearance_Pricebook_Generation_Data_task --> Data_Flow_Task___Build_Clearance_Bundle_Fact_Table_task
        Data_Flow_Task___Cleanse___Handle_Duplicates_task["Data Flow Task - Cleanse - Handle Duplicates"]
        Data_Flow_Task___Build_Clearance_Bundle_Fact_Table_task --> Data_Flow_Task___Cleanse___Handle_Duplicates_task
        SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_task["SeqCont - Copy and Archive Clerance Pricebook Files"]
        Data_Flow_Task___Cleanse___Handle_Duplicates_task --> SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_task
        FEL___Copy_to_SFTP_and_Archive_task["FEL - Copy to SFTP and Archive"]
        SeqCont___Copy_and_Archive_Clerance_Pricebook_Files_task --> FEL___Copy_to_SFTP_and_Archive_task
        File_System_Task___Archive_task["File System Task - Archive"]
        FEL___Copy_to_SFTP_and_Archive_task --> File_System_Task___Archive_task
        File_System_Task___Copy_to_Feedonomics_Directory_task["File System Task - Copy to Feedonomics Directory"]
        File_System_Task___Archive_task --> File_System_Task___Copy_to_Feedonomics_Directory_task
        File_System_Task___Copy_to_SFTP_Stage_task["File System Task - Copy to SFTP Stage"]
        File_System_Task___Copy_to_Feedonomics_Directory_task --> File_System_Task___Copy_to_SFTP_Stage_task
        SeqCont___Output_Clearance_Pricebook_XML_Files_task["SeqCont - Output Clearance Pricebook XML Files"]
        File_System_Task___Copy_to_SFTP_Stage_task --> SeqCont___Output_Clearance_Pricebook_XML_Files_task
        Data_Flow_Task___UK_Clearance_File_Generation_task["Data Flow Task - UK Clearance File Generation"]
        SeqCont___Output_Clearance_Pricebook_XML_Files_task --> Data_Flow_Task___UK_Clearance_File_Generation_task
        Data_Flow_Task___US_Clearance_File_Generation_task["Data Flow Task - US Clearance File Generation"]
        Data_Flow_Task___UK_Clearance_File_Generation_task --> Data_Flow_Task___US_Clearance_File_Generation_task
        SeqCont___Process_Clearance_Price_Files_task["SeqCont - Process Clearance Price Files"]
        Data_Flow_Task___US_Clearance_File_Generation_task --> SeqCont___Process_Clearance_Price_Files_task
        FEL___Ingest_and_Archive_Copy_of_Clearance_File___UK_task["FEL - Ingest and Archive Copy of Clearance File - UK"]
        SeqCont___Process_Clearance_Price_Files_task --> FEL___Ingest_and_Archive_Copy_of_Clearance_File___UK_task
        Data_Flow_Task_task["Data Flow Task"]
        FEL___Ingest_and_Archive_Copy_of_Clearance_File___UK_task --> Data_Flow_Task_task
        File_System_Task___Copy_UK_File_task["File System Task - Copy UK File"]
        Data_Flow_Task_task --> File_System_Task___Copy_UK_File_task
        FEL___Ingest_and_Archive_Copy_of_Clearance_File___US_task["FEL - Ingest and Archive Copy of Clearance File - US"]
        File_System_Task___Copy_UK_File_task --> FEL___Ingest_and_Archive_Copy_of_Clearance_File___US_task
        Data_Flow_Task_task["Data Flow Task"]
        FEL___Ingest_and_Archive_Copy_of_Clearance_File___US_task --> Data_Flow_Task_task
        File_System_Task___Copy_US_File_task["File System Task - Copy US File"]
        Data_Flow_Task_task --> File_System_Task___Copy_US_File_task
        SeqCont___Generate_and_Email_Global_E_Report_Documents_task["SeqCont - Generate and Email Global E Report Documents"]
        File_System_Task___Copy_US_File_task --> SeqCont___Generate_and_Email_Global_E_Report_Documents_task
        FEL___Archive_Global_E_Files_task["FEL - Archive Global E Files"]
        SeqCont___Generate_and_Email_Global_E_Report_Documents_task --> FEL___Archive_Global_E_Files_task
        File_System_Task___Archive_Global_E_Files_task["File System Task - Archive Global E Files"]
        FEL___Archive_Global_E_Files_task --> File_System_Task___Archive_Global_E_Files_task
        Send_Mail_Task___Email_Global_E_Filese_to_Web_Team_task["Send Mail Task - Email Global E Filese to Web Team"]
        File_System_Task___Archive_Global_E_Files_task --> Send_Mail_Task___Email_Global_E_Filese_to_Web_Team_task
        SeqCont___Generate_Global_E_Files_task["SeqCont - Generate Global E Files"]
        Send_Mail_Task___Email_Global_E_Filese_to_Web_Team_task --> SeqCont___Generate_Global_E_Files_task
        Data_Flow_Task_task["Data Flow Task"]
        SeqCont___Generate_Global_E_Files_task --> Data_Flow_Task_task
        SeqCont___Missing_Bundles_Stage_task["SeqCont - Missing Bundles Stage"]
        Data_Flow_Task_task --> SeqCont___Missing_Bundles_Stage_task
        Data_Flow_Task_task["Data Flow Task"]
        SeqCont___Missing_Bundles_Stage_task --> Data_Flow_Task_task
        Execute_SQL_Task_task["Execute SQL Task"]
        Data_Flow_Task_task --> Execute_SQL_Task_task
        SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_task["SeqCont - Process and Stage PIM  Bundle Files - Orig"]
        Execute_SQL_Task_task --> SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_task
        Data_Flow_Task___Cleanse_and_Derive_task["Data Flow Task - Cleanse and Derive"]
        SeqCont___Process_and_Stage_PIM__Bundle_Files___Orig_task --> Data_Flow_Task___Cleanse_and_Derive_task
        Execute_SQL_Task___Truncate_Stage_task["Execute SQL Task - Truncate Stage"]
        Data_Flow_Task___Cleanse_and_Derive_task --> Execute_SQL_Task___Truncate_Stage_task
        FEL___Ingest_and_Archive_PIM_Bundle_Files_task["FEL - Ingest and Archive PIM Bundle Files"]
        Execute_SQL_Task___Truncate_Stage_task --> FEL___Ingest_and_Archive_PIM_Bundle_Files_task
        Data_Flow_Task___File_to_Stage_task["Data Flow Task - File to Stage"]
        FEL___Ingest_and_Archive_PIM_Bundle_Files_task --> Data_Flow_Task___File_to_Stage_task
        Rename_and_Archive_task["Rename and Archive"]
        Data_Flow_Task___File_to_Stage_task --> Rename_and_Archive_task
        spMergePimBundleSkuExtract_task["spMergePimBundleSkuExtract"]
        Rename_and_Archive_task --> spMergePimBundleSkuExtract_task
        SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_task["SeqCont - Process and Stage PIM  Bundle Files - Seperate Files"]
        spMergePimBundleSkuExtract_task --> SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_task
        Execute_SQL_Task___Truncate_Stage_task["Execute SQL Task - Truncate Stage"]
        SeqCont___Process_and_Stage_PIM__Bundle_Files___Seperate_Files_task --> Execute_SQL_Task___Truncate_Stage_task
        SeqCont___Consolidate_and_Cleanse_task["SeqCont - Consolidate and Cleanse"]
        Execute_SQL_Task___Truncate_Stage_task --> SeqCont___Consolidate_and_Cleanse_task
        Data_Flow_Task___Cleanse_task["Data Flow Task - Cleanse"]
        SeqCont___Consolidate_and_Cleanse_task --> Data_Flow_Task___Cleanse_task
        Data_Flow_Task___Consolidate_task["Data Flow Task - Consolidate"]
        Data_Flow_Task___Cleanse_task --> Data_Flow_Task___Consolidate_task
        Sequence_Container_task["Sequence Container"]
        Data_Flow_Task___Consolidate_task --> Sequence_Container_task
        FEL___Ingest_and_Archive_PIM_Bundle_File_UK_task["FEL - Ingest and Archive PIM Bundle File UK"]
        Sequence_Container_task --> FEL___Ingest_and_Archive_PIM_Bundle_File_UK_task
        Data_Flow_Task_task["Data Flow Task"]
        FEL___Ingest_and_Archive_PIM_Bundle_File_UK_task --> Data_Flow_Task_task
        Rename_and_Archive_task["Rename and Archive"]
        Data_Flow_Task_task --> Rename_and_Archive_task
        FEL___Ingest_and_Archive_PIM_Bundle_File_US_task["FEL - Ingest and Archive PIM Bundle File US"]
        Rename_and_Archive_task --> FEL___Ingest_and_Archive_PIM_Bundle_File_US_task
        Data_Flow_Task_task["Data Flow Task"]
        FEL___Ingest_and_Archive_PIM_Bundle_File_US_task --> Data_Flow_Task_task
        Rename_and_Archive_task["Rename and Archive"]
        Data_Flow_Task_task --> Rename_and_Archive_task
        spMergePimBundleSkuExtract_task["spMergePimBundleSkuExtract"]
        Rename_and_Archive_task --> spMergePimBundleSkuExtract_task
        SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_task["SeqCont - Stage and Merge Bundle Pricing to PricebookFactBundles"]
        spMergePimBundleSkuExtract_task --> SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_task
        Data_Flow_Task___BundleSkuExtract_to_PricebookFactBundlePreStage_task["Data Flow Task - BundleSkuExtract to PricebookFactBundlePreStage"]
        SeqCont___Stage_and_Merge_Bundle_Pricing_to_PricebookFactBundles_task --> Data_Flow_Task___BundleSkuExtract_to_PricebookFactBundlePreStage_task
        Execute_SQL_Task___Truncate_Stage_task["Execute SQL Task - Truncate Stage"]
        Data_Flow_Task___BundleSkuExtract_to_PricebookFactBundlePreStage_task --> Execute_SQL_Task___Truncate_Stage_task
        spMergePricebookBundleSkuFact_task["spMergePricebookBundleSkuFact"]
        Execute_SQL_Task___Truncate_Stage_task --> spMergePricebookBundleSkuFact_task
        SeqCont___Test_Assistance___Copy_PROD_Single_Sku_Pricebook_Tables_to_Test_task["SeqCont - Test Assistance - Copy PROD Single Sku Pricebook Tables to Test"]
        spMergePricebookBundleSkuFact_task --> SeqCont___Test_Assistance___Copy_PROD_Single_Sku_Pricebook_Tables_to_Test_task
        Data_Flow_Task___Single_Sku_Pricebook_task["Data Flow Task - Single Sku Pricebook"]
        SeqCont___Test_Assistance___Copy_PROD_Single_Sku_Pricebook_Tables_to_Test_task --> Data_Flow_Task___Single_Sku_Pricebook_task
        Execute_SQL_Task_task["Execute SQL Task"]
        Data_Flow_Task___Single_Sku_Pricebook_task --> Execute_SQL_Task_task
        SeqCont___Test_Assitance___Copy_PROD_Bundle_Pricebook_Tables_to_TEst_task["SeqCont - Test Assitance - Copy PROD Bundle Pricebook Tables to TEst"]
        Execute_SQL_Task_task --> SeqCont___Test_Assitance___Copy_PROD_Bundle_Pricebook_Tables_to_TEst_task
        Data_Flow_Task_Bundle_Pricebook_task["Data Flow Task Bundle Pricebook"]
        SeqCont___Test_Assitance___Copy_PROD_Bundle_Pricebook_Tables_to_TEst_task --> Data_Flow_Task_Bundle_Pricebook_task
        Execute_SQL_Task_task["Execute SQL Task"]
        Data_Flow_Task_Bundle_Pricebook_task --> Execute_SQL_Task_task
        SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive_task["SeqCont - Upload XML Files To Feedonomics and Archive"]
        Execute_SQL_Task_task --> SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive_task
        FEL___Archive_Feedonomics_Files_task["FEL - Archive Feedonomics Files"]
        SeqCont___Upload_XML_Files_To_Feedonomics_and_Archive_task --> FEL___Archive_Feedonomics_Files_task
        File_System_Task___Archive_File_task["File System Task - Archive File"]
        FEL___Archive_Feedonomics_Files_task --> File_System_Task___Archive_File_task
        WinSCP____Upload_Files_to_Feedonomics_FTP_task["WinSCP  - Upload Files to Feedonomics FTP"]
        File_System_Task___Archive_File_task --> WinSCP____Upload_Files_to_Feedonomics_FTP_task
        Send_Mail_Task_task["Send Mail Task"]
        WinSCP____Upload_Files_to_Feedonomics_FTP_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| Archive | FILE |
| ArchiveClearance | FILE |
| ArchiveFeedonomics | FILE |
| IntegrationStaging | OLEDB |
| IntegrationStagingProdCopyingOnly | OLEDB |
| MissingBundlesCsv | FLATFILE |
| PimCsv | FLATFILE |
| PimCsvUk | FLATFILE |
| PimCsvUkQty | FLATFILE |
| PimCsvUs | FLATFILE |
| PimCsvUsQty | FLATFILE |
| SMTP | SMTP |
| UkClearancePriceCsv | FLATFILE |
| UkSalePriceCsv | FLATFILE |
| UK_GlobalE_BundlesCsv | FLATFILE |
| UK_GlobalE_ComponentCsv | FLATFILE |
| UsClearancePriceCsv | FLATFILE |
| UsSalePriceCsv | FLATFILE |
| US_GlobalE_BundleCsv | FLATFILE |
| US_GlobalE_ComponentCsv | FLATFILE |
| XML FILE | FILE |
| XML FILE Clearance | FILE |

## Control Flow Tasks

| Task | Type |
|---|---|
| PimBundleSkuExtract | Microsoft.Package |
| Execute SQL Task  - Check Time | Microsoft.ExecuteSQLTask |
| Faux Control | Microsoft.ExecuteSQLTask |
| SeqCont - Bundle Sale Price Extract | STOCK:SEQUENCE |
| Execute SQL Task - Truncate Stage | Microsoft.ExecuteSQLTask |
| SeqCont - Cleanse and Stage For Sale Pricebook XML generation  Data | STOCK:SEQUENCE |
| Data Flow Task - Build Sale Bundle Fact Table - New Oct 4 2024 | Microsoft.Pipeline |
| Data Flow Task - Build Sale Bundle Fact Table - Old | Microsoft.Pipeline |
| Data Flow Task - Cleanse | Microsoft.Pipeline |
| SeqCont - Copy and Archive Files | STOCK:SEQUENCE |
| FEL - Copy to SFTP and Archive | STOCK:FOREACHLOOP |
| File System Task - Archive | Microsoft.FileSystemTask |
| File System Task - Copy to Feedonomics Directory | Microsoft.FileSystemTask |
| File System Task - Copy to SFTP Stage | Microsoft.FileSystemTask |
| SeqCont - Output Sale Pricebook XML Files | STOCK:SEQUENCE |
| Data Flow Task - UK Sale File Generation | Microsoft.Pipeline |
| Data Flow Task - US Sale File Generation | Microsoft.Pipeline |
| SeqCont - Process Sale Price Files | STOCK:SEQUENCE |
| FEL - Ingest and Archive Copy of Sale Price File - UK | STOCK:FOREACHLOOP |
| Data Flow Task | Microsoft.Pipeline |
| File System Task - Copy File | Microsoft.FileSystemTask |
| FEL - Ingest and Archive Copy of Sale Price File - US | STOCK:FOREACHLOOP |
| Data Flow Task | Microsoft.Pipeline |
| File System Task - Copy File | Microsoft.FileSystemTask |
| SeqCont - Clearance Price Extract | STOCK:SEQUENCE |
| Execute SQL Task - Truncate Stage | Microsoft.ExecuteSQLTask |
| SeqCont - Cleanse and Stage for Clearance Pricebook Generation Data | STOCK:SEQUENCE |
| Data Flow Task - Build Clearance Bundle Fact Table | Microsoft.Pipeline |
| Data Flow Task - Cleanse - Handle Duplicates | Microsoft.Pipeline |
| SeqCont - Copy and Archive Clerance Pricebook Files | STOCK:SEQUENCE |
| FEL - Copy to SFTP and Archive | STOCK:FOREACHLOOP |
| File System Task - Archive | Microsoft.FileSystemTask |
| File System Task - Copy to Feedonomics Directory | Microsoft.FileSystemTask |
| File System Task - Copy to SFTP Stage | Microsoft.FileSystemTask |
| SeqCont - Output Clearance Pricebook XML Files | STOCK:SEQUENCE |
| Data Flow Task - UK Clearance File Generation | Microsoft.Pipeline |
| Data Flow Task - US Clearance File Generation | Microsoft.Pipeline |
| SeqCont - Process Clearance Price Files | STOCK:SEQUENCE |
| FEL - Ingest and Archive Copy of Clearance File - UK | STOCK:FOREACHLOOP |
| Data Flow Task | Microsoft.Pipeline |
| File System Task - Copy UK File | Microsoft.FileSystemTask |
| FEL - Ingest and Archive Copy of Clearance File - US | STOCK:FOREACHLOOP |
| Data Flow Task | Microsoft.Pipeline |
| File System Task - Copy US File | Microsoft.FileSystemTask |
| SeqCont - Generate and Email Global E Report Documents | STOCK:SEQUENCE |
| FEL - Archive Global E Files | STOCK:FOREACHLOOP |
| File System Task - Archive Global E Files | Microsoft.FileSystemTask |
| Send Mail Task - Email Global E Filese to Web Team | Microsoft.SendMailTask |
| SeqCont - Generate Global E Files | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| SeqCont - Missing Bundles Stage | STOCK:SEQUENCE |
| Data Flow Task | Microsoft.Pipeline |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| SeqCont - Process and Stage PIM  Bundle Files - Orig | STOCK:SEQUENCE |
| Data Flow Task - Cleanse and Derive | Microsoft.Pipeline |
| Execute SQL Task - Truncate Stage | Microsoft.ExecuteSQLTask |
| FEL - Ingest and Archive PIM Bundle Files | STOCK:FOREACHLOOP |
| Data Flow Task - File to Stage | Microsoft.Pipeline |
| Rename and Archive | Microsoft.FileSystemTask |
| spMergePimBundleSkuExtract | Microsoft.ExecuteSQLTask |
| SeqCont - Process and Stage PIM  Bundle Files - Seperate Files | STOCK:SEQUENCE |
| Execute SQL Task - Truncate Stage | Microsoft.ExecuteSQLTask |
| SeqCont - Consolidate and Cleanse | STOCK:SEQUENCE |
| Data Flow Task - Cleanse | Microsoft.Pipeline |
| Data Flow Task - Consolidate | Microsoft.Pipeline |
| Sequence Container | STOCK:SEQUENCE |
| FEL - Ingest and Archive PIM Bundle File UK | STOCK:FOREACHLOOP |
| Data Flow Task | Microsoft.Pipeline |
| Rename and Archive | Microsoft.FileSystemTask |
| FEL - Ingest and Archive PIM Bundle File US | STOCK:FOREACHLOOP |
| Data Flow Task | Microsoft.Pipeline |
| Rename and Archive | Microsoft.FileSystemTask |
| spMergePimBundleSkuExtract | Microsoft.ExecuteSQLTask |
| SeqCont - Stage and Merge Bundle Pricing to PricebookFactBundles | STOCK:SEQUENCE |
| Data Flow Task - BundleSkuExtract to PricebookFactBundlePreStage | Microsoft.Pipeline |
| Execute SQL Task - Truncate Stage | Microsoft.ExecuteSQLTask |
| spMergePricebookBundleSkuFact | Microsoft.ExecuteSQLTask |
| SeqCont - Test Assistance - Copy PROD Single Sku Pricebook Tables to Test | STOCK:SEQUENCE |
| Data Flow Task - Single Sku Pricebook | Microsoft.Pipeline |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| SeqCont - Test Assitance - Copy PROD Bundle Pricebook Tables to TEst | STOCK:SEQUENCE |
| Data Flow Task Bundle Pricebook | Microsoft.Pipeline |
| Execute SQL Task | Microsoft.ExecuteSQLTask |
| SeqCont - Upload XML Files To Feedonomics and Archive | STOCK:SEQUENCE |
| FEL - Archive Feedonomics Files | STOCK:FOREACHLOOP |
| File System Task - Archive File | Microsoft.FileSystemTask |
| WinSCP  - Upload Files to Feedonomics FTP | Microsoft.ExecuteProcess |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | With ListBundles as  ( select  f.BundleSku ,BundleSkuCatalog from WEB.PricebookBundleSkuFact f where 1=1 --and f.BundleSku in ('29031_28917_28934') -- Testing Purposes Only  group by  f.BundleSku ,BundleSkuCatalog ),   BundlesWithSales as  ( select  e.BundleSku ,e.BundleSkuCatalog ,bpf.SaleReference from [dbo].[PimBundleSkuExtract] p (nolock) join ListBundles e on e.BundleSku = p.LocalProductCode  |
|  | With ListBundles as  ( select  f.BundleSku ,BundleSkuCatalog from WEB.PricebookBundleSkuFact f where 1=1 --and f.BundleSku in ('32498_32495_22920_22920','432498_432495_422920_422920','224099_24174_24175_28093') -- Testing Purposes Only  group by  f.BundleSku ,BundleSkuCatalog )  ,Summary1 as (  select  e.BundleSku ,e.BundleSkuCatalog ,p.ComponentProducts as ComponentProduct , bpf.SalePriceStartDat |
|  | select  case when s.catalog  = 'UK' and len(sku) < 6  		then concat ('4',right(DerivedStyleCode,5))  	else s.DerivedStyleCode end as StyleCode ,s.Retail as SalePrice ,s.Catalog ,s.reference as SaleReference ,s.DerivedStartDateTime as SalePriceStartDateTime ,s.DerivedEndDateTime as SalePriceEndDateTime from WEB.BundleSalePriceStage s where 1=1 group by  case when s.catalog  = 'UK' and len(sku) < 6  |
|  | select getdate() as DummyField |
|  | /* With SaleBundles as  ( select  f.BundleSku ,BundleSkuCatalog from [WEB].[BundleSalePriceFact] f where 1=1 and f.BundleSkuCatalog = 'UK' group by  f.BundleSku ,BundleSkuCatalog ) , Summary1 as ( select  e.BundleSku ,e.BundleSkuCatalog ,p.ComponentProducts as ComponentProduct ,bpf.SalePriceStartDateTime ,bpf.SalePriceEndDateTime ,bpf.SaleReference ,bpf.SalePrice , case when SalePrice is null then |
|  | select   --f.UnionSource f.BundleSku ,f.BundleSkuCatalog --,f.SalePriceStartDateTime --,CONVERT(VARCHAR(50), CAST(f.SalePriceStartDateTime AS DATETIMEOFFSET), 127) as SalePriceStartDateTime ,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f.SalePriceEndDateTime |
|  | select getdate() as DummyField |
|  | /*With SaleBundles as  ( select  f.BundleSku ,BundleSkuCatalog from [WEB].[BundleSalePriceFact] f where 1=1 and f.BundleSkuCatalog = 'US' group by  f.BundleSku ,BundleSkuCatalog ) , Summary1 as ( select  e.BundleSku ,e.BundleSkuCatalog ,p.ComponentProducts as ComponentProduct ,bpf.SalePriceStartDateTime ,bpf.SalePriceEndDateTime ,bpf.SaleReference ,bpf.SalePrice , case when SalePrice is null then  |
|  | select   --f.UnionSource f.BundleSku ,f.BundleSkuCatalog --,f.SalePriceStartDateTime --,CONVERT(VARCHAR(50), CAST(f.SalePriceStartDateTime AS DATETIMEOFFSET), 127) as SalePriceStartDateTime ,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f.SalePriceEndDate |
|  | With ListBundles as  ( select  f.BundleSku ,BundleSkuCatalog from WEB.PricebookBundleSkuFact f where 1=1 --and f.BundleSku in ('26808_26808_26808_26808','26907_26907_26907_26907','28389_28389_28389') -- Testing Purposes Only  group by  f.BundleSku ,BundleSkuCatalog )  ,Summary1 as (  select  e.BundleSku ,e.BundleSkuCatalog ,p.ComponentProducts as ComponentProduct ,bpf.ClearancePriceStartDateTime , |
|  | /*-- Exclude Duplicates Approach  With Duplicates as  ( select  s.DerivedStyleCode ,s.Catalog from [WEB].[BundleClearancePriceStage] s group by  DerivedStyleCode ,s.Catalog having count (*) > 1 )   select  case when s.catalog  = 'UK' and len(sku) < 6  		then concat ('4',right(s.DerivedStyleCode,5))  	else s.DerivedStyleCode end as StyleCode ,s.Retail as ClearancePrice ,s.Catalog ,s.reference as Cl |
|  | /* With ClearanceBundles as  ( select  f.BundleSku ,BundleSkuCatalog from [WEB].[BundleClearancePriceFact] f where 1=1 and f.BundleSkuCatalog = 'UK' group by  f.BundleSku ,BundleSkuCatalog ) , Summary1 as ( select  e.BundleSku ,e.BundleSkuCatalog ,p.ComponentProducts as ComponentProduct ,bpf.ClearancePriceStartDateTime ,bpf.ClearancePriceEndDateTime ,bpf.ClearanceReference ,bpf.ClearancePrice , ca |
|  | select getdate () as GetDate |
|  | select   --f.UnionSource f.BundleSku ,f.BundleSkuCatalog --,f.ClearancePriceStartDateTime --,CONVERT(VARCHAR(50), CAST(f.ClearancePriceStartDateTime AS DATETIMEOFFSET), 127) as SalePriceStartDateTime ,CONVERT (varchar,f.ClearancePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion  --,f.Sa |
|  | select getdate () as GetDate |
|  | /* With ClearanceBundles as  ( select  f.BundleSku ,BundleSkuCatalog from [WEB].[BundleClearancePriceFact] f where 1=1 and f.BundleSkuCatalog = 'US' group by  f.BundleSku ,BundleSkuCatalog ) , Summary1 as ( select  e.BundleSku ,e.BundleSkuCatalog ,p.ComponentProducts as ComponentProduct ,bpf.ClearancePriceStartDateTime ,bpf.ClearancePriceEndDateTime ,bpf.ClearanceReference ,bpf.ClearancePrice , ca |
|  | select   --f.UnionSource f.BundleSku ,f.BundleSkuCatalog --,f.ClearancePriceStartDateTime --,CONVERT(VARCHAR(50), CAST(f.ClearancePriceStartDateTime AS DATETIMEOFFSET), 127) as SalePriceStartDateTime ,CONVERT (varchar,f.ClearancePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as SalePriceStartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f |
|  | select  f.BundleSku as Sku ,cast (1 as int) as Quantity ,f.BundSkuSalePrice as Retail ,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127)  as StartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f.SalePriceEndDateTime ,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'GMT Standard Time' At Time Zone 'UTC',127) as EndDateTime  |
|  | -- Will need this to capture Quantity Information once multi qty component skus is enable  With Stage as   ( select  s.DerivedStyleCode ,s.Retail ,s.catalog ,s.DerivedStartDateTime ,s.DerivedEndDateTime ,s.Quantity from WEB.BundleSalePriceStage s where 1=1 and s.catalog  = 'UK' group by  s.DerivedStyleCode ,s.Retail ,s.catalog ,s.DerivedStartDateTime ,s.DerivedEndDateTime ,s.Quantity  )   select s |
|  | select  f.BundleSku as Sku ,cast (1 as int) as Quantity ,f.BundSkuSalePrice as Retail ,CONVERT (varchar,SalePriceStartDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as StartDateTime -- Per Bryce Ahrens on 8/26/2024 they require UTC conversion --,f.SalePriceEndDateTime ,CONVERT (varchar,SalePriceEndDateTime at Time Zone 'Central Standard Time' At Time Zone 'UTC',127) as EndDa |
|  | -- Will need this to capture Quantity Information once multi qty component skus is enable  With Stage as   ( select  s.DerivedStyleCode ,s.Retail ,s.catalog ,s.DerivedStartDateTime ,s.DerivedEndDateTime ,s.Quantity from WEB.BundleSalePriceStage s where 1=1 and s.catalog  = 'US' group by  s.DerivedStyleCode ,s.Retail ,s.catalog ,s.DerivedStartDateTime ,s.DerivedEndDateTime ,s.Quantity  )   select s |
|  | with ValidBundlesStage as ( select  s.PrimaryId, count (s.UsComponentProducts) as CountComponentProducts,  LEN(s.PrimaryId) - LEN(REPLACE(s.PrimaryId, '_', '')) + 1 as ExpectedSkuCount -- I do +1 as there is no leading underscore from PimBundleSkuExtractStage s where 1=1 and s.UsComponentProducts <> '' -- Filtering Out Any rows where the Ind Sku field is empty - and s.UsComponentProducts not like  |
|  | with ValidBundlesStage as  ( select  s.PrimaryId ,s.Catalog ,count (distinct s.ComponentProducts) as CountComponentProductsDistinct -- Renamed  as Part of JIRA BIB-1024  ,sum (case when s.ComponentQuantity <> 1 then 1*s.ComponentQuantity	else 1 end ) as CountComponentProducts -- Added as Part of JIRA BIB-1024  ,LEN(s.PrimaryId) - LEN(REPLACE(s.PrimaryId, '_', '')) + 1 as ExpectedSkuCount -- I do + |
|  | with DataStage as  ( select  us.PrimaryId ,us.USLocalProductCode as LocalProductCode ,us.KeyStory  ,us.GroupingType ,us.UsMSTAT as MSTAT ,us.UsComponentProducts as ComponentProducts ,us.UsDisplayName as DisplayName ,us.Catalog ,case when us.UsComponentQuantity = '' 	then 1 else us.UsComponentQuantity end as ComponentQuantity from [PimBundleSkuExtractStageUs] us where 1=1 and us.UsComponentProducts |
|  | with EligibleBundleStage as ( select  p.PrimaryId  ,p.CountComponentProducts ,pf.Catalog ,sum (case when pf.style_code is null then 0  		when pf.style_code is not null then 1 		end ) as PricebookFactRowCount from [dbo].[PimBundleSkuExtract] p (nolock)  join web.PricebookFact pf (nolock) on pf.style_code = p.ComponentProducts and pf.Catalog =  p.Catalog  where 1=1 --and  --( --	p.LocalProductCode = |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [WEB].[BundleSalePriceFact] |
|  | [WEB].[BundleSalePriceFact] |
|  | [WEB].[BundleSalePrice] |
|  | [WEB].[BundleSalePriceStage] |
|  | [WEB].[BundleSalePriceStage] |
|  | [WEB].[BundleClearancePriceFact] |
|  | [WEB].[BundleClearancePrice] |
|  | [WEB].[BundleClearancePriceStage] |
|  | [WEB].[BundleClearancePriceStage] |
|  | [dbo].[MissingBundleSkuStage] |
|  | [dbo].[PimBundleSkuExtractCleansed] |
|  | [dbo].[PimBundleSkuExtractStageFailed] |
|  | [dbo].[PimBundleSkuExtractStage] |
|  | [dbo].[PimBundleSkuExtractStageConsolidatedAndCleansed] |
|  | [dbo].[PimBundleSkuExtractStageConsolidated] |
|  | [dbo].[PimBundleSkuExtractStageUK] |
|  | [dbo].[PimBundleSkuExtractStageUs] |
|  | [WEB].[BundlePricebookFactPreStage] |
|  | [WEB].[PricebookFact] |
|  | [WEB].[PricebookFact] |
|  | [WEB].[PricebookBundleSkuFact] |
|  | [WEB].[PricebookBundleSkuFact] |

