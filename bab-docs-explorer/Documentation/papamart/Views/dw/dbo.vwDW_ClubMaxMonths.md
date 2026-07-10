# dbo.vwDW_ClubMaxMonths

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_ClubMaxMonths"]
    date_dim(["date_dim"]) --> VIEW
    transaction_detail_facts(["transaction_detail_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| date_dim |
| transaction_detail_facts |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_ClubMaxMonths]
AS
SELECT BearitorySet, StoreSet, fiscal_year, fiscal_period, first_dom_date_key, FiscalMonthMember, BearRange
	FROM
	(
		SELECT TOP 12
			'NONEMPTY(DESCENDANTS([Store].[Corporate].[Bear Range].[North America], [Store].[Corporate].[Bearitory]), [Measures].[GAAP Sales v. Plan YTD])' AS BearitorySet
			,'NONEMPTY(DESCENDANTS([Store].[Corporate].[Bear Range].[North America], [Store].[Corporate].[Store]), [Measures].[GAAP Sales v. Plan YTD])' AS StoreSet
			,d.fiscal_year
			,d.fiscal_period
			,CAST(MIN(d.date_key) AS varchar) AS first_dom_date_key
			,'[Date].[Fiscal].[Fiscal Period].&[' + CAST(d.fiscal_year AS varchar) + ' ' + RIGHT('0' + CAST(d.fiscal_period AS varchar), 2) + ']' AS FiscalMonthMember
			,'North America' AS BearRange
		FROM date_dim d
	--	INNER JOIN
	--		(
	--			SELECT 'North America' AS BearRange
	--			UNION
	--			SELECT 'UK' AS BearRange
	--		) br ON 1 = 1
		WHERE d.date_key <= (SELECT MAX(date_key) FROM transaction_detail_facts t)
		GROUP BY d.fiscal_year, d.fiscal_period
		ORDER BY d.fiscal_year DESC, d.fiscal_period DESC
	) t

	UNION

	SELECT BearitorySet, StoreSet, fiscal_year, fiscal_period, first_dom_date_key, FiscalMonthMember, BearRange
	FROM
	(
		SELECT TOP 12
			'NONEMPTY(DESCENDANTS([Store].[Corporate].[Bear Range].[UK], [Store].[Corporate].[Bearitory]), [Measures].[GAAP Sales v. Plan YTD])' AS BearitorySet
			,'NONEMPTY(DESCENDANTS([Store].[Corporate].[Bear Range].[UK], [Store].[Corporate].[Store]), [Measures].[GAAP Sales v. Plan YTD])' AS StoreSet
			,d.fiscal_year
			,d.fiscal_period
			,CAST(MIN(d.date_key) AS varchar) AS first_dom_date_key
			,'[Date].[Fiscal].[Fiscal Period].&[' + CAST(d.fiscal_year AS varchar) + ' ' + RIGHT('0' + CAST(d.fiscal_period AS varchar), 2) + ']' AS FiscalMonthMember
			,'UK' AS BearRange
		FROM date_dim d
		WHERE d.date_key <= (SELECT MAX(date_key) FROM transaction_detail_facts t)
		GROUP BY d.fiscal_year, d.fiscal_period
		ORDER BY d.fiscal_year DESC, d.fiscal_period DESC
	) t
```

