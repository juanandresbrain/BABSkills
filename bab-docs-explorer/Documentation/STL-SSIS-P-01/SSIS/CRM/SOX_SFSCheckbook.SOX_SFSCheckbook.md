# SSIS Package: SOX_SFSCheckbook

**Project:** SOX_SFSCheckbook  
**Folder:** CRM  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        CRM_conn(["CRM [OLEDB]"])
        DW_conn(["DW [OLEDB]"])
        SOX_conn(["SOX [OLEDB]"])
    end
    subgraph ControlFlow
        SOX_SFSCheckbook_task["SOX_SFSCheckbook"]
        Sequence_Container_task["Sequence Container"]
        SOX_SFSCheckbook_task --> Sequence_Container_task
        Check_for_Fiscal_Start_Date_task["Check for Fiscal Start Date"]
        Sequence_Container_task --> Check_for_Fiscal_Start_Date_task
        Insert___Update_CRMRewardSummary_task["Insert & Update CRMRewardSummary"]
        Check_for_Fiscal_Start_Date_task --> Insert___Update_CRMRewardSummary_task
        Push_Data_from_CRM_to_Papamart_task["Push Data from CRM to Papamart"]
        Insert___Update_CRMRewardSummary_task --> Push_Data_from_CRM_to_Papamart_task
        STAGE_CRM_Data_to_CRM_Tables_task["STAGE CRM Data to CRM Tables"]
        Push_Data_from_CRM_to_Papamart_task --> STAGE_CRM_Data_to_CRM_Tables_task
        TRUNCATE_STAGE_task["TRUNCATE STAGE"]
        STAGE_CRM_Data_to_CRM_Tables_task --> TRUNCATE_STAGE_task
    end
```

## Connection Managers

| Name | Type |
|---|---|
| CRM | OLEDB |
| DW | OLEDB |
| SOX | OLEDB |

## Control Flow Tasks

| Task | Type |
|---|---|
| SOX_SFSCheckbook | Microsoft.Package |
| Sequence Container | STOCK:SEQUENCE |
| Check for Fiscal Start Date | Microsoft.ExecuteSQLTask |
| Insert & Update CRMRewardSummary | Microsoft.ExecuteSQLTask |
| Push Data from CRM to Papamart | Microsoft.Pipeline |
| STAGE CRM Data to CRM Tables | Microsoft.ExecuteSQLTask |
| TRUNCATE STAGE | Microsoft.ExecuteSQLTask |

## Data Flow: Sources

_None detected._

## Data Flow: Destinations

| Component | Destination |
|---|---|
|  | [dbo].[CRMPointExpiration] |
|  | [dbo].[CRMRewardTransaction] |
|  | [Staging].[CRMPointExpiration] |
|  | [Staging].[CRMRewardTransaction] |

