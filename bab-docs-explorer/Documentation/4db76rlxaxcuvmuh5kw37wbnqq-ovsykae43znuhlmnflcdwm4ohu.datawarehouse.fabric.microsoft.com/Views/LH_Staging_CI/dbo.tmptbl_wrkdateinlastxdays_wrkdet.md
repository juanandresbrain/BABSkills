# dbo.tmptbl_wrkdateinlastxdays_wrkdet

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.tmptbl_wrkdateinlastxdays_wrkdet"]
    dbo_tmptbl_wrkdateinlastxdays_wrkdet(["dbo.tmptbl_wrkdateinlastxdays_wrkdet"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmptbl_wrkdateinlastxdays_wrkdet |

## View Code

```sql
; CREATE   VIEW [dbo].[tmptbl_wrkdateinlastxdays_wrkdet] AS SELECT [wrks_id], [wrkd_id] FROM [dbo].[tmptbl_wrkdateinlastxdays_wrkdet]
```

