# dbo.giftcard_ftp_status

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.giftcard_ftp_status"]
    dbo_giftcard_ftp_status(["dbo.giftcard_ftp_status"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.giftcard_ftp_status |

## View Code

```sql
; CREATE   VIEW [dbo].[giftcard_ftp_status] AS     SELECT [GroupCode] COLLATE Latin1_General_CI_AS AS [GroupCode], [pulled_date], [period_start_date], [sequence_number], [ptd_pulled_date], [mposx_pulled_date], [dact_pulled_date], [hdsk_pulled_date], [wg_dact_pulled_date], [wg_hdsk_pulled_date], [ErrorFlag], [ErrorMessage] COLLATE Latin1_General_CI_AS AS [ErrorMessage], [InsertDate], [UpdateDate]     FROM [dbo].[giftcard_ftp_status]
```

