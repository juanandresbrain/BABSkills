# dbo.gcstage_activations

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.gcstage_activations"]
    dbo_gcstage_activations(["dbo.gcstage_activations"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.gcstage_activations |

## View Code

```sql
;
CREATE   VIEW [dbo].[gcstage_activations]
AS
    SELECT [recID], [store_key], [transaction_id], [date_key], [activated_amount], [discount_amount], [giftcard_no] COLLATE Latin1_General_CI_AS AS [giftcard_no], [currency_key], [MID] COLLATE Latin1_General_CI_AS AS [MID], [Source] COLLATE Latin1_General_CI_AS AS [Source], [VLVerified], [register_no], [transaction_no], [postedPhase], [vlLineID]
    FROM LH_Staging.[dbo].[gcstage_activations]
```

