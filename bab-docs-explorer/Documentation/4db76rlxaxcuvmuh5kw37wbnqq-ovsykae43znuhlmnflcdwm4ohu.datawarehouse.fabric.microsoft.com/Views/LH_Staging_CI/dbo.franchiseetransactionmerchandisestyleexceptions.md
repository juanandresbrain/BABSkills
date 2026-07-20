# dbo.franchiseetransactionmerchandisestyleexceptions

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.franchiseetransactionmerchandisestyleexceptions"]
    dbo_franchiseetransactionmerchandisestyleexceptions(["dbo.franchiseetransactionmerchandisestyleexceptions"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.franchiseetransactionmerchandisestyleexceptions |

## View Code

```sql
; CREATE   VIEW [dbo].[franchiseetransactionmerchandisestyleexceptions] AS SELECT [style_code] COLLATE Latin1_General_CI_AS AS [style_code], [style_desc] COLLATE Latin1_General_CI_AS AS [style_desc] FROM [dbo].[franchiseetransactionmerchandisestyleexceptions]
```

