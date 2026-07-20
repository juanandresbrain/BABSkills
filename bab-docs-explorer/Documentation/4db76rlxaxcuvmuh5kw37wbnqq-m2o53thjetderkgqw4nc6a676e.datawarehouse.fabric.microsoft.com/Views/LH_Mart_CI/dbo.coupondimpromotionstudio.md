# dbo.coupondimpromotionstudio

**Database:** LH_Mart_CI  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.coupondimpromotionstudio"]
    dbo_coupondimpromotionstudio(["dbo.coupondimpromotionstudio"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.coupondimpromotionstudio |

## View Code

```sql
;

CREATE VIEW dbo.coupondimpromotionstudio AS SELECT coupon_key, Retail_Pro COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS Retail_Pro, coupon_desc COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS coupon_desc, start_date, stop_date, qty_distributed, event_id, event_name COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS event_name, category_id, category COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS category, INS_DT, UPDT_DT, ETL_LOG_ID, ETL_EVNT_ID, dmDiscountID, categoryTypeID COLLATE Latin1_General_100_CI_AS_KS_WS_SC_UTF8   AS categoryTypeID FROM LH_Mart.dbo.coupondimpromotionstudio;
```

