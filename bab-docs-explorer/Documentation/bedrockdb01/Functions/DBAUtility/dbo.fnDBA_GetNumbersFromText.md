# dbo.fnDBA_GetNumbersFromText

**Database:** DBAUtility  
**Server:** bedrockdb01  
**Function Type:** Inline Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fnDBA_GetNumbersFromText"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @String | varchar | 2000 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
create function [dbo].[fnDBA_GetNumbersFromText](@String varchar(2000))
--From http://stackoverflow.com/questions/9629880/extract-numbers-from-a-text-in-sql-server
returns table as return
(
  with C as
  (
    select cast(substring(S.Value, S1.Pos, S2.L) as int) as Number,
           stuff(s.Value, 1, S1.Pos + S2.L, '') as Value
    from (select @String+' ') as S(Value)
      cross apply (select patindex('%[0-9]%', S.Value)) as S1(Pos)
      cross apply (select patindex('%[^0-9]%', stuff(S.Value, 1, S1.Pos, ''))) as S2(L)
    union all
    select cast(substring(S.Value, S1.Pos, S2.L) as int),
           stuff(S.Value, 1, S1.Pos + S2.L, '')
    from C as S
      cross apply (select patindex('%[0-9]%', S.Value)) as S1(Pos)
      cross apply (select patindex('%[^0-9]%', stuff(S.Value, 1, S1.Pos, ''))) as S2(L)
    where patindex('%[0-9]%', S.Value) > 0
  )
  select Number
  from C
)
```

