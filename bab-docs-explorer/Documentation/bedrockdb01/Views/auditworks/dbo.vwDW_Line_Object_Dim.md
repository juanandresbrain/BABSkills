# dbo.vwDW_Line_Object_Dim

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_Line_Object_Dim"]
    dbo_line_object(["dbo.line_object"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.line_object |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_Line_Object_Dim]
AS
SELECT cast([line_object] as int) as line_object
	  ,cast([line_object_type] as int) as line_object_type
      ,cast(substring([line_object_description], 1, 50) as varchar(50)) as line_object_description
  FROM [auditworks].[dbo].[line_object] with (nolock)





dbo,register,-- don't drop to avoid losing customized view

create view dbo.register as
SELECT	store_no = OCW.ORG_CHN_NUM,
	register_no = OCW.WRKSTN_NUM,
	register_name = OCW.CMPTR_NAME,
	register_function = CASE WHEN OCW.WRKSTN_ID = OCW.PRNT_WRKSTN_ID OR OCW.PRNT_WRKSTN_ID IS NULL THEN 9000 ELSE 1 END,
	register_poll_id = OCW.PLNG_IDNTFR, -- numeric max 4 digits
	resource_id = NULL, --no longer in use
	reg_pre_midnight_time = OCW.BSNS_DAY_END_RNG_START_TIME,
	reg_post_midnight_time = OCW.BSNS_DAY_END_RNG_END_TIME,
	OCW.WRKSTN_ID, -- = PRNT_WRKSTN_ID for server reg
	OCW.PRNT_WRKSTN_ID, -- WRKSTN_ID of parent server reg
	OCW.ACTV
 FROM ORG_CHN_WRKSTN OCW
```

