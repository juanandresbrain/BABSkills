# dbo.Sl_Sr_JobFlag

**Database:** fn_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.Sl_Sr_JobFlag"]
    dbo_Sr_JobFlag(["dbo.Sr_JobFlag"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.Sr_JobFlag |

## View Code

```sql
CREATE VIEW [dbo].[Sl_Sr_JobFlag] (job_flag,job_flag_label_1,job_flag_label_2)
AS SELECT job_flag,job_flag_label_1,job_flag_label_2
FROM fn_01.dbo.Sr_JobFlag
```

