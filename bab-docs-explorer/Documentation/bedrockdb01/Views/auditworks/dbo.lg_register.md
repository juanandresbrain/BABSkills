# dbo.lg_register

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.lg_register"]
    ORG_CHN_WRKSTN(["ORG_CHN_WRKSTN"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_CHN_WRKSTN |

## View Code

```sql
create view dbo.lg_register 
AS

SELECT
	store_no = ORG_CHN_NUM,
	register_no = WRKSTN_NUM,
	register_name = CMPTR_NAME,
	resource_id = 0,
	ACTV
 FROM ORG_CHN_WRKSTN
```

