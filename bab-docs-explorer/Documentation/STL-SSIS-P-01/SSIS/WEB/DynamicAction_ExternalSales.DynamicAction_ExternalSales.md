# SSIS Package: DynamicAction_ExternalSales

**Project:** DynamicAction_ExternalSales  
**Folder:** WEB  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        buildabear_externalsales_uk_conn(["buildabear_externalsales_uk [FLATFILE]"])
        buildabear_externalsales_us_conn(["buildabear_externalsales_us [FLATFILE]"])
        DW_conn(["DW [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        DynamicAction_ExternalSales_task["DynamicAction_ExternalSales"]
        Sequence_Container_task["Sequence Container"]
        DynamicAction_ExternalSales_task --> Sequence_Container_task
        DataFlow___Output_Files_task["DataFlow - Output Files"]
        Sequence_Container_task --> DataFlow___Output_Files_task
        Foreach_Loop_Container_task["Foreach Loop Container"]
        DataFlow___Output_Files_task --> Foreach_Loop_Container_task
        ___Do_Nothing____task["-- Do Nothing --"]
        Foreach_Loop_Container_task --> ___Do_Nothing____task
        Archive_File___UK_task["Archive File - UK"]
        ___Do_Nothing____task --> Archive_File___UK_task
        Archive_File___US_task["Archive File - US"]
        Archive_File___UK_task --> Archive_File___US_task
        FTP_UK_task["FTP UK"]
        Archive_File___US_task --> FTP_UK_task
        FTP_US_task["FTP US"]
        FTP_UK_task --> FTP_US_task
        Send_Mail_Task_task["Send Mail Task"]
        FTP_US_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| buildabear_externalsales_uk | FLATFILE |
| buildabear_externalsales_us | FLATFILE |
| DW | OLEDB |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| DynamicAction_ExternalSales | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| DataFlow - Output Files | Microsoft.Pipeline |
| Foreach Loop Container | STOCK:FOREACHLOOP |
| -- Do Nothing -- | Microsoft.ExecuteSQLTask |
| Archive File - UK | Microsoft.FileSystemTask |
| Archive File - US | Microsoft.FileSystemTask |
| FTP UK | Microsoft.ExecuteProcess |
| FTP US | Microsoft.ExecuteProcess |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | SQL Preview |
|---|---|
|  | with  ExcludeES as 	( 		--table is loaded during the morning load into transaction_facts, vis spdw_build_transaction_facts 		select transaction_id 		from tmpESRef  		group by transaction_id 	) select  	cast(pd.style_code as varchar(6)) as SKU, 	right((cast('0000' as varchar) + cast(sd.store_id as varchar)),4) as StockLocationID, 	sum(cast(tdf.units as int)) as ExternalUnitsSold, 	case when sd.stor |
|  | select style_code, catalog from web.pricebookfact |

## Data Flow: Destinations

_None detected._

