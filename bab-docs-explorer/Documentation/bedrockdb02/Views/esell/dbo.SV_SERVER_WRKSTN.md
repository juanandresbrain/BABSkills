# dbo.SV_SERVER_WRKSTN

**Database:** esell  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.SV_SERVER_WRKSTN"]
    dbo_ORG_CHN_WRKSTN(["dbo.ORG_CHN_WRKSTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ORG_CHN_WRKSTN |

## View Code

```sql
create view [dbo].[SV_SERVER_WRKSTN] AS
SELECT WRKSTN_NUM, ORG_CHN_NUM, BSNS_DAY_END_RNG_START_TIME, BSNS_DAY_END_RNG_END_TIME, ACTV, SRVR_WRKSTN_NUM =
	(SELECT a.WRKSTN_NUM 
	   FROM ORG_CHN_WRKSTN a 
	  WHERE a.PRNT_WRKSTN_ID = o.WRKSTN_ID
            AND o.WRKSTN_ID = a.WRKSTN_ID)
FROM ORG_CHN_WRKSTN o
```

