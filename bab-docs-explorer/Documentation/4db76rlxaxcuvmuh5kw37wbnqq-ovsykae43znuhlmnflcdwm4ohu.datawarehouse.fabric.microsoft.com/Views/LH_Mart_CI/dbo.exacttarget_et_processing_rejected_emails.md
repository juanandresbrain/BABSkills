# dbo.exacttarget_et_processing_rejected_emails

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.exacttarget_et_processing_rejected_emails"]
    dbo_exacttarget_et_processing_rejected_emails(["dbo.exacttarget_et_processing_rejected_emails"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.exacttarget_et_processing_rejected_emails |

## View Code

```sql
; CREATE   VIEW exacttarget_et_processing_rejected_emails AS SELECT * FROM LH_Mart.dbo.exacttarget_et_processing_rejected_emails;
```

