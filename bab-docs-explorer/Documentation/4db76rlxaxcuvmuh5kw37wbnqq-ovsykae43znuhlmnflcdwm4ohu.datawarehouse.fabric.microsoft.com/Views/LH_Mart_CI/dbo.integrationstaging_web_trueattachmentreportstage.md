# dbo.integrationstaging_web_trueattachmentreportstage

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.integrationstaging_web_trueattachmentreportstage"]
    dbo_integrationstaging_web_trueattachmentreportstage(["dbo.integrationstaging_web_trueattachmentreportstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.integrationstaging_web_trueattachmentreportstage |

## View Code

```sql
; CREATE   VIEW integrationstaging_web_trueattachmentreportstage AS SELECT * FROM LH_Mart.dbo.integrationstaging_web_trueattachmentreportstage;
```

