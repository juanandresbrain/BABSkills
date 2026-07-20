# sys.sys_dw_schemas

**Database:** LH_Reporting  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-m2o53thjetderkgqw4nc6a676e.datawarehouse.fabric.microsoft.com  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["sys.sys_dw_schemas"]
    VIEW --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## View Code

```sql
CREATE   VIEW sys.sys_dw_schemas
AS
SELECT s.*, i.* 
FROM sys.schemas s
OUTER APPLY OpenRowSet(TABLE DW_SCHEMAS, s.schema_id) i
```

