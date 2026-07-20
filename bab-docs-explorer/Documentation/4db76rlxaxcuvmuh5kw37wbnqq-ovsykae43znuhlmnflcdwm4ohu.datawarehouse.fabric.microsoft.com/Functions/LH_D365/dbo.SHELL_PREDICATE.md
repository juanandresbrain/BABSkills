# dbo.SHELL_PREDICATE

**Database:** LH_D365  
**Server:** 4db76rlxaxcuvmuh5kw37wbnqq-ovsykae43znuhlmnflcdwm4ohu.datawarehouse.fabric.microsoft.com  
**Function Type:** Inline Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.SHELL_PREDICATE"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

_No parameters._

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[SHELL_PREDICATE]() RETURNS TABLE WITH SCHEMABINDING RETURN SELECT 1 as policyResult WHERE 1 != 1
```

