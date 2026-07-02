# SSIS Package: concurETL_download

**Project:** concurETL_download  
**Folder:** HR  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        ASNCorrections_conn(["ASNCorrections [FLATFILE]"])
        CRM_conn(["CRM [ADO.NET:SQL]"])
        Dynamics_AX_Connection_Manager_conn(["Dynamics AX Connection Manager [DynamicsAX]"])
        ESPStaging_conn(["ESPStaging [OLEDB]"])
        Flat_File_Connection_Manager_conn(["Flat File Connection Manager [FLATFILE]"])
        Flat_File_Connection_Manager_1_conn(["Flat File Connection Manager 1 [FLATFILE]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
        ProductInventory_conn(["ProductInventory [FLATFILE]"])
        SendLog_conn(["SendLog [FLATFILE]"])
        SendLogPIPE_csv_conn(["SendLogPIPE.csv [FILE]"])
        SMTP_conn(["SMTP [SMTP]"])
        STL_SSIS_P_01_IntegrationStaging_conn(["STL-SSIS-P-01.IntegrationStaging [OLEDB]"])
        tcp_eco_bab_test_database_windows_net_1433_ecobabtest_USER_conn(["tcp:eco-bab-test.database.windows.net,1433.ecobabtest.USER [ADO.NET:System.Data.SqlClient.SqlConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089]"])
    end
    subgraph ControlFlow
        concurETL_download_task["concurETL_download"]
        retreive_and_decrypt_task["retreive and decrypt"]
        concurETL_download_task --> retreive_and_decrypt_task
        delete_prev_sae_task["delete prev sae"]
        retreive_and_decrypt_task --> delete_prev_sae_task
        delete_prev_sae_sorted_task["delete prev sae sorted"]
        delete_prev_sae_task --> delete_prev_sae_sorted_task
        SFTP_AWS_retrieve_task["SFTP AWS retrieve"]
        delete_prev_sae_sorted_task --> SFTP_AWS_retrieve_task
        SFTP_retrieve__legacy__task["SFTP retrieve (legacy)"]
        SFTP_AWS_retrieve_task --> SFTP_retrieve__legacy__task
        Send_Mail_Task_task["Send Mail Task"]
        SFTP_retrieve__legacy__task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| ASNCorrections | FLATFILE |
| CRM | ADO.NET:SQL |
| Dynamics AX Connection Manager | DynamicsAX |
| ESPStaging | OLEDB |
| Flat File Connection Manager | FLATFILE |
| Flat File Connection Manager 1 | FLATFILE |
| IntegrationStaging | OLEDB |
| papamart.DWStaging | OLEDB |
| ProductInventory | FLATFILE |
| SendLog | FLATFILE |
| SendLogPIPE.csv | FILE |
| SMTP | SMTP |
| STL-SSIS-P-01.IntegrationStaging | OLEDB |
| tcp:eco-bab-test.database.windows.net,1433.ecobabtest.USER | ADO.NET:System.Data.SqlClient.SqlConnection, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089 |

## Control Flow Tasks

| Task | Type |
|---|---|
| concurETL_download | Microsoft.Package |
| retreive and decrypt | STOCK:SEQUENCE |
| delete prev sae | Microsoft.FileSystemTask |
| delete prev sae sorted | Microsoft.FileSystemTask |
| SFTP AWS retrieve | Microsoft.ExecuteSQLTask |
| SFTP retrieve (legacy) | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

