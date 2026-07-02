# SSIS Package: CRM_CustomerDimDeleteDE

**Project:** CRM_CustomerDimDeleteDE  
**Folder:** CRM  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        Archive_conn(["Archive [FILE]"])
        CRM_conn(["CRM [OLEDB]"])
        CRM_1_conn(["CRM 1 [OLEDB]"])
        CRMCustomerDimDelete_xlsx_conn(["CRMCustomerDimDelete.xlsx [Excel (KingswaySoft)]"])
        DW_conn(["DW [OLEDB]"])
        DW_1_conn(["DW 1 [OLEDB]"])
        DWStaging_conn(["DWStaging [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        SMTP_conn(["SMTP [SMTP]"])
    end
    subgraph ControlFlow
        CRM_CustomerDimDeleteDE_task["CRM_CustomerDimDeleteDE"]
        Sequence_Container_task["Sequence Container"]
        CRM_CustomerDimDeleteDE_task --> Sequence_Container_task
        delete_customers_no_longer_in_CRM_from_DE_table_task["delete customers no longer in CRM from DE table"]
        Sequence_Container_task --> delete_customers_no_longer_in_CRM_from_DE_table_task
        Send_Mail_Task_task["Send Mail Task"]
        delete_customers_no_longer_in_CRM_from_DE_table_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| Archive | FILE |
| CRM | OLEDB |
| CRM 1 | OLEDB |
| CRMCustomerDimDelete.xlsx | Excel (KingswaySoft) |
| DW | OLEDB |
| DW 1 | OLEDB |
| DWStaging | OLEDB |
| IntegrationStaging | OLEDB |
| SMTP | SMTP |

## Control Flow Tasks

| Task | Type |
|---|---|
| CRM_CustomerDimDeleteDE | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| delete customers no longer in CRM from DE table | Microsoft.ExecuteSQLTask |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

_None detected._

