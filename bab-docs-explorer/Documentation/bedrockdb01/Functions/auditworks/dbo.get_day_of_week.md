# dbo.get_day_of_week

**Database:** auditworks  
**Server:** bedrockdb01  
**Function Type:** Scalar Function  
**Returns:** tinyint(1)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.get_day_of_week"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @t_date | smalldatetime | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
CREATE FUNCTION [dbo].[get_day_of_week] (@t_date	smalldatetime)
returns tinyint

AS

/* 
  Name : dbo.get_day_of_week
  Desc : Returns a number that corresponds to the day of the week as per specs provided by TAG.
         Sunday = 0, Monday = 1, ..., Saturday = 6.
         Cannot use datepart(dw, @t_date) because it depends on the value 
         set by SET DATEFIRST, which sets the first day of the week.

  HISTORY:   

  Date     Name       Defect# Desc
  May21,04 David      DV-1333 Author
  
*/

BEGIN

DECLARE

@day_of_week	tinyint,
@date_string	char(6),
@week_string	char(42)


SELECT @date_string = UPPER ((DATENAME (dw, @t_date))),
       @week_string = 'SUNDAYMONDAYTUESDAWEDNESTHURSDFRIDAYSATURD' 

SELECT @day_of_week = ABS ((CHARINDEX (@date_string, @week_string)) - 1)/6


RETURN @day_of_week


END
```

