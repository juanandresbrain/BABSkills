# dbo.crmcustomers3daysstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.crmcustomers3daysstage"]
    dbo_crmcustomers3daysstage(["dbo.crmcustomers3daysstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.crmcustomers3daysstage |

## View Code

```sql
; CREATE   VIEW [dbo].[crmcustomers3daysstage] AS SELECT [CustomerNumber] COLLATE Latin1_General_CI_AS AS [CustomerNumber], [firstTransaction], [lastTransaction] FROM [dbo].[crmcustomers3daysstage]
```

