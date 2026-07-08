# dbo.find_text_in_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.find_text_in_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[find_text_in_$sp]
@StringToSearch varchar(100) 
as 

/*******************************************************
*Author: Ankur,2011
*Comments: Searches for Text in Stored Procedures.
*******************************************************/

set @StringToSearch = '%' +@StringToSearch + '%'
select distinct so.name
from sysobjects so (nolock)
inner join syscomments sc (nolock) on so.id = sc.id
and so.type = 'P'
and sc.text like @StringToSearch
order by so.name
```

