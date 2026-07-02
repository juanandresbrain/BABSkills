# SSIS Package: ERP_PO_Export_To_DBSchenker_OnDemand

**Project:** ERP_PurchaseOrderFromD365  
**Folder:** SSIS  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        me_01_conn(["me_01 [OLEDB]"])
    end
    subgraph ControlFlow
        ERP_PO_Export_To_DBSchenker_OnDemand_task["ERP_PO_Export_To_DBSchenker_OnDemand"]
        Stage_for_DB_Schenker_Sequence_task["Stage for DB Schenker Sequence"]
        ERP_PO_Export_To_DBSchenker_OnDemand_task --> Stage_for_DB_Schenker_Sequence_task
        Export_to_FTP_task["Export to FTP"]
        Stage_for_DB_Schenker_Sequence_task --> Export_to_FTP_task
        Stage_PO_to_Merch_task["Stage PO to Merch"]
        Export_to_FTP_task --> Stage_PO_to_Merch_task
        Truncate_DBS_Stage_task["Truncate DBS Stage"]
        Stage_PO_to_Merch_task --> Truncate_DBS_Stage_task
        Truncate_DBS_Stage_On_Merch_task["Truncate DBS Stage On Merch"]
        Truncate_DBS_Stage_task --> Truncate_DBS_Stage_On_Merch_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| IntegrationStaging | OLEDB |
| me_01 | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| ERP_PO_Export_To_DBSchenker_OnDemand | Microsoft.Package |
| Stage for DB Schenker Sequence | STOCK:SEQUENCE |
| Export to FTP | Microsoft.ExecuteSQLTask |
| Stage PO to Merch | Microsoft.Pipeline |
| Truncate DBS Stage | Microsoft.ExecuteSQLTask |
| Truncate DBS Stage On Merch | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | update ERP.PurchaseOrderHeader set Exported_DBS = getdate()  where Exported_DBS is NULL  and cast(PurchaseOrderNumber as nvarchar) = ? |
|  | update ERP.PurchaseOrderLines set Exported_DBS = getdate()  where Exported_DBS is NULL  and cast(PurchaseOrderNumber as nvarchar) = ?  and LineNumber = ? |

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[tmpHoldDBSchenkerPO_FromD365] |
|  | [ERP].[vwPurchaseOrderDBSchenker] |

