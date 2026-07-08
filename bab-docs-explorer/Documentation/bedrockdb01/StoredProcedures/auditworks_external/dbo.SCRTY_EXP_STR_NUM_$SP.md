# dbo.SCRTY_EXP_STR_NUM_$SP

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.SCRTY_EXP_STR_NUM_$SP"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
create proc [dbo].[SCRTY_EXP_STR_NUM_$SP] 
@tableName nvarchar(100), @activeGroups nvarchar(3000)
AS

/* 
 Procedure : SCRTY_EXP_STR_NUM_$SP
 Descr: This procedure will populate the table @tableName with a list of stores belonging to the active groups.
	Called by Foundation n-tier upon user authentication under the SA application.

HISTORY:  
Date     Name           Def# Desc
Jul06,12 Vicci        136606 Provide audit-group as well to support new audit workflow feature with summaries by group 
Oct31,05 Tim         DV-1320 Parentheses around parameter list removed - errors occurred when called from C#.
Aug01,05 Sab/Paul    DV-1295 Alias dbo when referencing the @tableName, added join to ORG_CHN_HRCHY_LVL_GRP
May30,05 Sab         DV-1254 Author
*/

DECLARE 
  @Count		int,
  @Cnt			int,
  @string		nvarchar(2000)

/* Check to see if the table @tableName exists */
SET @string = N'select @Count = count(*) from sysobjects where name = ''' + @tableName + ''''
EXEC sp_executesql @string,N'@Count int OUT', @Count OUT

/* IF @Count = 1, then the table exists */
IF @Count = 1
 BEGIN
   SET @string = N'truncate table dbo.' + @tableName
   EXEC sp_executesql @string
 END
ELSE
 BEGIN
   SET @string = N'create table dbo.' + @tableName + ' ( ORG_CHN_NUM INT not null, HRCHY_LVL_GRP_ID binary(16) null )'
   EXEC sp_executesql @string
   SET @string = N'create unique clustered index ' + @tableName + '_x0 ON dbo.' + @tableName + ' (ORG_CHN_NUM)'
   EXEC sp_executesql @string
 END

IF LEN(@activeGroups) > 0
BEGIN
  SET @string = N'insert into dbo.' + @tableName + ' (ORG_CHN_NUM, HRCHY_LVL_GRP_ID) ' +
		N'select a.ORG_CHN_NUM, max(b.HRCHY_LVL_GRP_ID) from ORG_CHN_HRCHY_LVL_GRP_A a, ORG_CHN_HRCHY_LVL_GRP b ' +
		N'where a.HRCHY_LVL_GRP_ID = b.HRCHY_LVL_GRP_ID and b.HRCHY_LVL_GRP_IDNTY IN (' + @activeGroups + ') 
                GROUP BY a.ORG_CHN_NUM '

  EXEC sp_executesql @string
END

RETURN
```

