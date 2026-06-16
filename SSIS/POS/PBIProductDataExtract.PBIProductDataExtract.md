# SSIS Package: PBIProductDataExtract

**Project:** PBIProductDataExtract  
**Folder:** POS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        auditworks_conn(["auditworks [OLEDB]"])
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        me_01_conn(["me_01 [OLEDB]"])
        SMTP_EMAIL_conn(["SMTP_EMAIL [SMTP]"])
    end
    subgraph ControlFlow
        PBIProductDataExtract_task["PBIProductDataExtract"]
        Stage_Data___From_me_01_to_IntegrationStaging___PROD_task["Stage Data - From me_01 to IntegrationStaging - PROD"]
        PBIProductDataExtract_task --> Stage_Data___From_me_01_to_IntegrationStaging___PROD_task
        Pre_Stage_POS_Attributes_task["Pre Stage POS Attributes"]
        Stage_Data___From_me_01_to_IntegrationStaging___PROD_task --> Pre_Stage_POS_Attributes_task
        Stage_POS_Attributes_task[/"Stage POS Attributes"/]
        Pre_Stage_POS_Attributes_task --> Stage_POS_Attributes_task
        Truncate_Staging_task["Truncate Staging"]
        Stage_POS_Attributes_task --> Truncate_Staging_task
        Send_Email_onError_task["Send Email onError"]
        Truncate_Staging_task --> Send_Email_onError_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| auditworks | OLEDB |
| IntegrationStaging | OLEDB |
| me_01 | OLEDB |
| SMTP_EMAIL | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| PBIProductDataExtract | Microsoft.Package |
| Stage Data - From me_01 to IntegrationStaging - PROD | STOCK:SEQUENCE |
| Pre Stage POS Attributes | Microsoft.ExecuteSQLTask |
| Stage POS Attributes | Microsoft.Pipeline |
| Truncate Staging | Microsoft.ExecuteSQLTask |
| Send Email onError | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | select * from [POS].[ProductCatalogMasterAttributesStage] |
|  |  | select * from [dbo].[vwPBIBundledSKU] |

## Data Flow: Destinations

| Component | Destination Table |
|---|---|
|  | [POS].[PBIProductCatalogMasterAttributesStage] |
|  | [dbo].[vwPBIProductCatalogWithHierarchyStage] |

