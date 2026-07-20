# dbo.gcstage_valuelink_activations

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.gcstage_valuelink_activations"]
    dbo_gcstage_valuelink_activations(["dbo.gcstage_valuelink_activations"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.gcstage_valuelink_activations |

## View Code

```sql
;
CREATE   VIEW [dbo].[gcstage_valuelink_activations]
AS
    SELECT [activationDate], [date_key], [store_key], [terminal_id], [terminal_transaction_number], [account_number] COLLATE Latin1_General_CI_AS AS [account_number], [transaction_amount], [reversal_flag] COLLATE Latin1_General_CI_AS AS [reversal_flag], [LineID], [merchant_id] COLLATE Latin1_General_CI_AS AS [merchant_id], [postedPhase], [gaRecID]
    FROM LH_Staging.[dbo].[gcstage_valuelink_activations]
```

