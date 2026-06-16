# SSIS Package: CustomerXML

**Project:** CustomerXMLExtract  
**Folder:** SSIS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        papamart_dw_conn(["papamart.dw [OLEDB]"])
        papamart_DWStaging_conn(["papamart.DWStaging [OLEDB]"])
        STL_SSIS_P_01_IntegrationStaging_conn(["STL-SSIS-P-01.IntegrationStaging [OLEDB]"])
    end
    subgraph ControlFlow
        CustomerXML_task["CustomerXML"]
        Stage_Date_task[/"Stage Date"/]
        CustomerXML_task --> Stage_Date_task
        TRUNCATE_STAGE_task["TRUNCATE STAGE"]
        Stage_Date_task --> TRUNCATE_STAGE_task
        xml_extract_task[/"xml extract"/]
        TRUNCATE_STAGE_task --> xml_extract_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| papamart.dw | OLEDB |
| papamart.DWStaging | OLEDB |
| STL-SSIS-P-01.IntegrationStaging | OLEDB |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| CustomerXML | Microsoft.Package |
| Stage Date | Microsoft.Pipeline |
| TRUNCATE STAGE | Microsoft.ExecuteSQLTask |
| xml extract | Microsoft.Pipeline |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | select p.EmailAddress, p.LastLoginTime, a2.text  from CustomerXMLExport_ProfileDataStage p join CustomerXMLExport_AttributeStage1 a1 on p.ProfileID = a1.profileID  join CustomerXMLExport_AttributeStage2 a2 on a1.AttributeID = a2.CustomAttributeID and a2.AttributeID = 'crmCustomerNumber' |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [dbo].[CustomerXMLExport] |
|  | [dbo].[CustomerXMLExport_AttributeStage1] |
|  | [dbo].[CustomerXMLExport_AttributeStage2] |
|  | [dbo].[CustomerXMLExport_ProfileDataStage] |

