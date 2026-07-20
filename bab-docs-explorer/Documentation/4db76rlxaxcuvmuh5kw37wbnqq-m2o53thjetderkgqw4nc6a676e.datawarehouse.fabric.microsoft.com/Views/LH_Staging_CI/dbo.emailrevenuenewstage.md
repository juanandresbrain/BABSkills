# dbo.emailrevenuenewstage

**Database:** LH_Staging_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.emailrevenuenewstage"]
    dbo_emailrevenuenewstage(["dbo.emailrevenuenewstage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.emailrevenuenewstage |

## View Code

```sql
;
CREATE   VIEW [dbo].[emailrevenuenewstage]
AS
    SELECT [JobID] COLLATE Latin1_General_CI_AS AS [JobID], [SubID] COLLATE Latin1_General_CI_AS AS [SubID], [ListID] COLLATE Latin1_General_CI_AS AS [ListID], [BatchID] COLLATE Latin1_General_CI_AS AS [BatchID], [EmailAddress] COLLATE Latin1_General_CI_AS AS [EmailAddress], [SubscriberKey] COLLATE Latin1_General_CI_AS AS [SubscriberKey], [INSERT_DATE] COLLATE Latin1_General_CI_AS AS [INSERT_DATE], [FrequencyCount24m] COLLATE Latin1_General_CI_AS AS [FrequencyCount24m], [RecencyCount24m] COLLATE Latin1_General_CI_AS AS [RecencyCount24m], [FrequencyCount1m] COLLATE Latin1_General_CI_AS AS [FrequencyCount1m], [FrequencyCount3m] COLLATE Latin1_General_CI_AS AS [FrequencyCount3m], [FrequencyCount6m] COLLATE Latin1_General_CI_AS AS [FrequencyCount6m], [FrequencyCount12m] COLLATE Latin1_General_CI_AS AS [FrequencyCount12m], [FrequencyCount18m] COLLATE Latin1_General_CI_AS AS [FrequencyCount18m], [FrequencyCountTTL] COLLATE Latin1_General_CI_AS AS [FrequencyCountTTL], [RecencyCount1m] COLLATE Latin1_General_CI_AS AS [RecencyCount1m], [RecencyCount3m] COLLATE Latin1_General_CI_AS AS [RecencyCount3m], [RecencyCount6m] COLLATE Latin1_General_CI_AS AS [RecencyCount6m], [RecencyCount12m] COLLATE Latin1_General_CI_AS AS [RecencyCount12m], [RecencyCountTTL] COLLATE Latin1_General_CI_AS AS [RecencyCountTTL], [LastTransactionDate] COLLATE Latin1_General_CI_AS AS [LastTransactionDate], [LastTransactionStore] COLLATE Latin1_General_CI_AS AS [LastTransactionStore], [MonetarySum1m] COLLATE Latin1_General_CI_AS AS [MonetarySum1m], [MonetarySum3m] COLLATE Latin1_General_CI_AS AS [MonetarySum3m], [MonetarySum6m] COLLATE Latin1_General_CI_AS AS [MonetarySum6m], [MonetarySum12m] COLLATE Latin1_General_CI_AS AS [MonetarySum12m], [MonetarySum18m] COLLATE Latin1_General_CI_AS AS [MonetarySum18m], [MonetarySum24m] COLLATE Latin1_General_CI_AS AS [MonetarySum24m], [MonetarySumTTL] COLLATE Latin1_General_CI_AS AS [MonetarySumTTL], [EventDate] COLLATE Latin1_General_CI_AS AS [EventDate], [EventType] COLLATE Latin1_General_CI_AS AS [EventType]
    FROM LH_Staging.[dbo].[emailrevenuenewstage]
```

