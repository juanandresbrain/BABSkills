# dbo.tmp_franchiseefilesimporterrorsummary

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmp_franchiseefilesimporterrorsummary"]
    dbo_tmp_franchiseefilesimporterrorsummary(["dbo.tmp_franchiseefilesimporterrorsummary"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_franchiseefilesimporterrorsummary |

## View Code

```sql
; CREATE   VIEW [dbo].[tmp_franchiseefilesimporterrorsummary] AS SELECT [ID] COLLATE Latin1_General_CI_AS AS [ID], [ErrorDesc] COLLATE Latin1_General_CI_AS AS [ErrorDesc] FROM [dbo].[tmp_franchiseefilesimporterrorsummary]
```

