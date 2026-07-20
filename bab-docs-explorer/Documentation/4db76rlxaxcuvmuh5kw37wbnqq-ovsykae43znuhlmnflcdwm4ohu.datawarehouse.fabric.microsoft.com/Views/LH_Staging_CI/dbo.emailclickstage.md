# dbo.emailclickstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailclickstage"]
    dbo_emailclickstage(["dbo.emailclickstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailclickstage |

## View Code

```sql
; CREATE   VIEW [dbo].[emailclickstage] AS SELECT [ClientID], [SendID], [SubscriberKey] COLLATE Latin1_General_CI_AS AS [SubscriberKey], [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [ClickDate], [clickCount] FROM [dbo].[emailclickstage]
```

