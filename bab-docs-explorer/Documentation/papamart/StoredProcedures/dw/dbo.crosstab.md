# dbo.crosstab

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.crosstab"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE crosstab 
@select varchar(8000),
@sumfunc varchar(100), 
@pivot varchar(100), 
@table varchar(100) 
AS

DECLARE @sql varchar(8000), @delim varchar(1)
SET NOCOUNT ON
SET ANSI_WARNINGS OFF

EXEC ('SELECT ' + @pivot + ' AS pivot INTO ##pivot FROM ' + @table + ' WHERE 1=2')
EXEC ('INSERT INTO ##pivot SELECT DISTINCT ' + @pivot + ' FROM ' + @table + ' WHERE ' 
+ @pivot + ' Is Not Null')

SELECT @sql='',  @sumfunc=stuff(@sumfunc, len(@sumfunc), 1, ' END)' )

SELECT @delim=CASE Sign( CharIndex('char', data_type)+CharIndex('date', data_type) ) 
WHEN 0 THEN '' ELSE '''' END 
FROM tempdb.information_schema.columns 
WHERE table_name='##pivot' AND column_name='pivot'

SELECT @sql=@sql + '''' + convert(varchar(100), pivot) + ''' = ' + 
stuff(@sumfunc,charindex( '(', @sumfunc )+1, 0, ' CASE ' + @pivot + ' WHEN ' 
+ @delim + convert(varchar(100), pivot) + @delim + ' THEN ' ) + ', ' FROM ##pivot

DROP TABLE ##pivot

SELECT @sql=left(@sql, len(@sql)-1)
SELECT @select=stuff(@select, charindex(' FROM ', @select)+1, 0, ', ' + @sql + ' ')

EXEC (@select)
SET ANSI_WARNINGS ON
```

