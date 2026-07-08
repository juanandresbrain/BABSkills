# dbo.Find_Text_In_$SP

**Database:** foundation  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Find_Text_In_$SP"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE Find_Text_In_$SP
@StringToSearch varchar(100) 
as 
set @StringToSearch = '%' +@StringToSearch + '%'
select distinct so.name
from sysobjects so (nolock)
inner join syscomments sc (nolock) on so.id = sc.id
and so.type = 'P'
and sc.text like @StringToSearch
order by so.name
```

