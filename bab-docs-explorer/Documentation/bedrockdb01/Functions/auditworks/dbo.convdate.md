# dbo.convdate

**Database:** auditworks  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** nvarchar(100)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.convdate"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @date | datetime | 8 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION dbo.convdate (@date datetime)
returns nvarchar(50)

AS
/* 
  Name : dbo.convdate
  Desc : Return a string date of this format YYYY-MM-DD HH:MI:SS2004-08-31 14:16:04
         which is used in logging to audit trail.
 
         
  HISTORY:   

  Date     Name       Defect#  Desc
  Jan06,11 Paul        105313  Use unicode datatypes
  Aug31,04 Maryam     DV-1120  Author
  
*/
BEGIN

  DECLARE
  @string nvarchar(50)

  SELECT @string = CONVERT(nvarchar,@date,120)

  RETURN @string
  
END
```

