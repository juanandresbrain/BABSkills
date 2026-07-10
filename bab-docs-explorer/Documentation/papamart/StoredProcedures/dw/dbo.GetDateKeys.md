# dbo.GetDateKeys

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.GetDateKeys"]
    date_dim(["date_dim"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[GetDateKeys]

	@Year as int,
	@Month as int = NULL,
	@Week as int = NULL

AS
BEGIN

	SELECT min(date_key) as min_date_key, max(date_key) as max_date_key
		,'WHERE date_key >= ' + CAST(MIN(date_key) as varchar) + ' AND date_key <= ' + CAST(MAX(date_key) as varchar) AS the_where
		,'WHERE aaa >= ''' + CONVERT(varchar, min(actual_date), 101) + ''' AND aaa <= ''' + CONVERT(varchar, max(actual_date), 101) + '''' AS the_date_where
		,min(actual_date) as min_date
		,max(actual_date) as max_date
	FROM date_dim
	WHERE fiscal_year = @Year
		AND fiscal_period = ISNULL(@Month, fiscal_period)
		AND fiscal_week = ISNULL(@Week, fiscal_week)

END
```

