# SSIS Package: PromotionLocationsToSalesforceCore

**Project:** PromotionLocationsToSalesforceCore  
**Folder:** POS  

## Architecture Diagram

```mermaid
flowchart TD
    subgraph Connections
        IntegrationStaging_conn(["IntegrationStaging [OLEDB]"])
        LocationsCSV_conn(["LocationsCSV [FLATFILE]"])
        SMTP_EMAIL_conn(["SMTP_EMAIL [SMTP]"])
    end
    subgraph ControlFlow
        PromotionLocationsToSalesforceCore_task["PromotionLocationsToSalesforceCore"]
        Data_Flow_Task_task[/"Data Flow Task"/]
        PromotionLocationsToSalesforceCore_task --> Data_Flow_Task_task
        Send_Mail_Task_task["Send Mail Task"]
        Data_Flow_Task_task --> Send_Mail_Task_task
    end
```

## Connection Managers

| Connection Name | Type |
|---|---|
| IntegrationStaging | OLEDB |
| LocationsCSV | FLATFILE |
| SMTP_EMAIL | SMTP |

## Control Flow Tasks

| Task Name | Type |
|---|---|
| PromotionLocationsToSalesforceCore | Microsoft.Package |
| Data Flow Task | Microsoft.Pipeline |
| Send Mail Task | Microsoft.SendMailTask |

## Data Flow: Sources

| Component | Tables Referenced | SQL Preview |
|---|---|---|
|  |  | select  	Code as LocationCode, 	case  		when Code >=2000  			then Code 		else concat(cast('1' as varchar), right(Code,3)) 	end as LocationNumber, 	LocationName, 	LocationType, 	Country  from web.LocationStage |

## Data Flow: Destinations

_No OLE DB data flow destinations detected._

