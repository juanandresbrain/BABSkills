# dbo.spRPT_EmployeeSales

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spRPT_EmployeeSales"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spRPT_EmployeeSales] --2006, 10
@Fiscal_Year int
,@Fiscal_Period int
AS

DECLARE @SQL nvarchar(2000)

SET @SQL = N'SELECT
  dbo.store_dim.store_id,
  dbo.store_dim.store_name,
  dbo.date_dim.fiscal_year,
  dbo.date_dim.fiscal_period,
  sum(dbo.Transaction_Summary_Facts.GAAP_Sale)
FROM
  dbo.store_dim,
  dbo.date_dim,
  dbo.Transaction_Summary_Facts (nolock)
WHERE
  ( dbo.Transaction_Summary_Facts.store_key=dbo.store_dim.store_key  )
  AND  ( dbo.Transaction_Summary_Facts.date_key=dbo.date_dim.date_key  )
  AND  ( dbo.Transaction_Summary_Facts.transaction_id IN 
		(
		SELECT dbo.discount_facts.transaction_id
		FROM
		  dbo.discount_facts (nolock),
		  dbo.date_dim,
		  dbo.Line_Object_Dim
		WHERE
		  ( dbo.date_dim.date_key=dbo.discount_facts.date_key  )
		  AND ( dbo.discount_facts.line_object_key=dbo.Line_Object_Dim.Line_Object_Key  )
		  AND ( dbo.date_dim.fiscal_period  = '+ CAST(@Fiscal_Period as varchar(2)) + ')
		  AND ( dbo.date_dim.fiscal_year  = '+ CAST(@Fiscal_Year as varchar(4))+')
		  AND  dbo.Line_Object_Dim.Line_Object  IN  (1700, 1900)
		) 
       )
GROUP BY
  dbo.store_dim.store_id,
  dbo.store_dim.store_name,
  dbo.date_dim.fiscal_year,
  dbo.date_dim.fiscal_period'

--select @SQL
exec sp_executesql @SQL
```

