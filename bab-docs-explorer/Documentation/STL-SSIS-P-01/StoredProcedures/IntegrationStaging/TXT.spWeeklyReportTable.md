# TXT.spWeeklyReportTable

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["TXT.spWeeklyReportTable"]
    txt_PrdDates(["txt.PrdDates"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| txt.PrdDates |

## Stored Procedure Code

```sql
CREATE proc [TXT].[spWeeklyReportTable]
as 
-- =====================================================================================================
-- Name: TXT.spWeeklyReportTable
--
-- Description:	Creates table TXT.WeeklyReport; JIRA BIB-897
--
-- Revision History
--		Name:			Date:			Comments:
--		Lizzy Timm		07/10/2024		Created proc
-- =====================================================================================================
set nocount on 

SET NOCOUNT ON


-- Compare current year to year in table headers
DECLARE @year varchar(5)
	,@inputString NVARCHAR(50)


SELECT DISTINCT @year = fiscal_year FROM txt.PrdDates;

SELECT DISTINCT @inputString = ISNULL(COLUMN_NAME,'')
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 1=1
    AND TABLE_NAME LIKE 'WeeklyReport'
	AND COLUMN_NAME LIKE 'BOP OH Cost:Total  ( Period %01 )'
	AND TABLE_SCHEMA = 'TXT';


-- Find the starting position of "Period "
DECLARE @startPosition INT = CHARINDEX('Period ', @inputString) + LEN('Period ');

-- Extract the year "2024" which is the first 4 characters after "Period "
DECLARE @tableYear NVARCHAR(4) = SUBSTRING(@inputString, @startPosition + 1, 4);

-- If years do not match, drop the table and recreate it
IF(@year <> @tableYear)  
BEGIN

IF OBJECT_ID('TXT.WeeklyReport', 'U') IS NOT NULL DROP TABLE TXT.WeeklyReport;
-- Note: variables are broken up into fours due to length limitations
	DECLARE  @sql NVARCHAR(MAX)
		, @columnsA NVARCHAR(MAX)
		, @columnsB NVARCHAR(MAX)
		, @columnsC NVARCHAR(MAX)
		, @columnsD NVARCHAR(MAX)
		, @SQLPart1 NVARCHAR(MAX)
		, @SQLPart2 NVARCHAR(MAX)
		, @SQLPart3 NVARCHAR(MAX)
		, @SQLPart4 NVARCHAR(MAX)


	DECLARE @baseColumnsA TABLE (ColumnName NVARCHAR(2000))
	DECLARE @baseColumnsB TABLE (ColumnName NVARCHAR(2000))
	DECLARE @baseColumnsC TABLE (ColumnName NVARCHAR(2000))
	DECLARE @baseColumnsD TABLE (ColumnName NVARCHAR(2000))

-- Populate table variables with column names
	INSERT INTO @baseColumnsA (ColumnName) VALUES 
	('[Concept Code] nvarchar(2000)'),
	('[Chain Label] nvarchar(2000)'),
	('[Department Label] nvarchar(2000)'),
	('[Class Label] nvarchar(2000)'),
	('[Sub-Class Label] nvarchar(2000)'),
	('[Style Custom Property Value (KEY STORY)] nvarchar(2000)'),
	('[Style Attribute Set Code O (MERCHANDISE STATUS)] nvarchar(2000)'),
	('[Style Code] varchar(512)'),
	('[Style Short Desc] nvarchar(100)'),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[BOP OH Cost:Total  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[BOP OH Retail:Total te  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '01 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '02 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '03 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '04 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '05 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '06 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '07 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '08 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '09 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '10 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '11 )]' ,' int')),
	(CONCAT('[BOP OH Units:Total  ( Period ', @year, '12 )]' ,' int')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[EOP OH Cost:Total  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[EOP OH Retail:Total TE  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '01 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '02 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '03 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '04 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '05 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '06 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '07 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '08 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '09 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '10 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '11 )]' ,' int')),
	(CONCAT('[EOP OH Units:Total  ( Period ', @year, '12 )]' ,' int'))

	INSERT INTO @baseColumnsB (ColumnName) VALUES 
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[Net Receipts Cost  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[Net Receipts Retail TE  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '01 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '02 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '03 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '04 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '05 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '06 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '07 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '08 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '09 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '10 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '11 )]' ,' int')),
	(CONCAT('[Net Receipts Units  ( Period ', @year, '12 )]' ,' int')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[Net Sales Cost  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[Net Sales Retail TE  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '01 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '02 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '03 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '04 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '05 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '06 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '07 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '08 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '09 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '10 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '11 )]' ,' int')),
	(CONCAT('[Net Sales Units  ( Period ', @year, '12 )]' ,' int')),
	(CONCAT('[On Order Cost  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '09 )]' ,' decimal'))

	INSERT INTO @baseColumnsC (ColumnName) VALUES 
	(CONCAT('[On Order Cost  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[On Order Cost  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[On Order Retail TE  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[On Order Units  ( Period ', @year, '01 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '02 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '03 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '04 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '05 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '06 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '07 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '08 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '09 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '10 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '11 )]' ,' int')),
	(CONCAT('[On Order Units  ( Period ', @year, '12 )]' ,' int')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '01 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '02 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '03 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '04 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '05 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '06 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '07 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '08 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '09 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '10 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '11 )]' ,' numeric')),
	(CONCAT('[Perm Md Retail TE  ( Period ', @year, '12 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '01 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '02 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '03 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '04 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '05 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '06 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '07 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '08 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '09 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '10 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '11 )]' ,' numeric')),
	(CONCAT('[Perm Mdc Retail TE  ( Period ', @year, '12 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '01 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '02 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '03 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '04 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '05 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '06 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '07 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '08 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '09 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '10 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '11 )]' ,' numeric')),
	(CONCAT('[Perm Mu Retail TE  ( Period ', @year, '12 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '01 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '02 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '03 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '04 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '05 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '06 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '07 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '08 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '09 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '10 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '11 )]' ,' numeric')),
	(CONCAT('[Perm Muc Retail TE  ( Period ', @year, '12 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '01 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '02 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '03 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '04 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '05 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '06 )]' ,' numeric'))

	INSERT INTO @baseColumnsD (ColumnName) VALUES 
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '07 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '08 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '09 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '10 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '11 )]' ,' numeric')),
	(CONCAT('[Promo Pc Total Retail TE  ( Period ', @year, '12 )]' ,' numeric')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '01 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '02 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '03 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '04 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '05 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '06 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '07 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '08 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '09 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '10 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '11 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Retail TE  ( Period ', @year, '12 )]' ,' decimal')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '01 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '02 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '03 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '04 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '05 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '06 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '07 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '08 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '09 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '10 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '11 )]' ,' int')),
	(CONCAT('[Shrink Actual Units  ( Period ', @year, '12 )]' ,' int'))

-- Convert table variable values into strings with values seperated by commas
	SELECT @columnsA = STUFF((
		SELECT ', ' + ColumnName 
		FROM @baseColumnsA
		FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '')

	SELECT @columnsB = STUFF((
		SELECT ', ' + ColumnName 
		FROM @baseColumnsB
		FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '')

	SELECT @columnsC = STUFF((
		SELECT ', ' + ColumnName 
		FROM @baseColumnsC
		FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '')

	SELECT @columnsD = STUFF((
		SELECT ', ' + ColumnName 
		FROM @baseColumnsD
		FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, '')

-- Set SQL commands
	SET @SQLPart1 = 'CREATE TABLE TXT.WeeklyReport (' + @columnsA + ');'
	SET @SQLPart2 = 'ALTER TABLE TXT.WeeklyReport ADD ' + @ColumnsB + ';'
	SET @SQLPart3 = 'ALTER TABLE TXT.WeeklyReport ADD ' + @ColumnsC + ';'
	SET @SQLPart4 = 'ALTER TABLE TXT.WeeklyReport ADD ' + @ColumnsD + ';'

-- Execute SQL commands
	EXEC sp_executesql @SQLPart1
	EXEC sp_executesql @SQLPart2
	EXEC sp_executesql @SQLPart3
	EXEC sp_executesql @SQLPart4
END




WEB,spEmailPartyWebOrderShippedSummary,CREATE proc [WEB].[spEmailPartyWebOrderShippedSummary]

as 

------------------------------------------------------------------
--	Dan Tweedie	2018-01-08	Created proc, runs from SSIS (agent job WEB - PartyBooking Daily Reports)
--	Lizzy Timm	2024-06-20	Updated proc to remove columns made redundant by modifying the Girl Scout Transfer Orders integration; Jira BIB-851
------------------------------------------------------------------
set nocount on 

if (
		select count(*) 
		from WEB.PartyTransferOrdersShipped
		where datediff(dd, ShipDate, getdate()-1) = 0
	) > 0
begin

	declare @subj varchar(52),
			@text nvarchar(max),
			@recip varchar(1000),
			@cc varchar(100)


	select 
		@Subj = 'Party Web Orders Shipped',
		@recip = 'DistroBears@buildabear.com',
		--@recip = 'lizzyt@buildabear.com',
		@text = 
		'<font face =arial size = 2><B>Party Web Orders Shipped Summary</B><br>' +
	'The items below were shipped from the Web for scheduled Parties.<br>' +
	'</font>' +
		'<table cellpadding=10 border=1>' +
			'<tr bgcolor=#4b6c9e>
				<th><font face =arial size = 2 color=White>PartyID</font></th>' +
				'<th><font face =arial size = 2 color=White>PartyDate</font></th>' +
				'<th><font face =arial size = 2 color=White>Store</font></th>' +
				'<th><font face =arial size = 2 color=White>Style</font></th>' +
				'<th><font face =arial size = 2 color=White>Description</font></th>' +
				'<th><font face =arial size = 2 color=White>Qty</font></th>' +
				'<th><font face =arial size = 2 color=White>ShipDate</font></th>' +
				'<th><font face =arial size = 2 color=White>ShipMethod</font></th>' +
				'<th><font face =arial size = 2 color=White>Tracking</font></th>' +
				--'<th><font face =arial size = 2 color=White>WebOrder</font></th>' +
				'<th><font face =arial size = 2 color=White>TransferNumber</font></th>' + 
				'<th><font face =arial size = 2 color=White>TransferUnitsSent</font></th>' +
				--'<th><font face =arial size = 2 color=White>TransferUnitsReceived</font></th>' +
				'</tr>' +
	'<font face =arial size = 2>' +
		CAST ( ( SELECT td = PartyID,'',
						td = PartyDate, '',
						td = StoreNumber, '',
						td = Style, '',
						td = SKUDescription, '',
						td = QtyShipped, '',
						td = ShipDate, '',
						td = ShipMethod, '',
						td = isnull(TrackingNumber,'n/a'), '',
						--td = WebOrderNumber, '',
						td = isnull(TransferNumber, 'unknown'), '',
						td = isnull(TransferUnitsSent,0), ''--,
						--td = isnull(TransferUnitsReceived,0), ''
				  from WEB.PartyTransferOrdersShipped
				  where datediff(dd, ShipDate, getdate()-1) = 0
				  order by PartyDate, StoreNumber, Style, ShipMethod, TrackingNumber
				  FOR XML PATH('tr'), TYPE 
		) AS NVARCHAR(MAX) ) +
		'</font></table></font></p></p>
		<br><br>' +
		'<br>
		<font face =arial size = 1><B>This report was run from stl-ssis-p-01.IntegrationStaging.WEB.spEmailPartyWebOrderShippedSummary.</B></font>
		<br>
		<br>
	<font face =arial size = 1><i>The information in this message may be privileged, “confidential” and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'

	exec msdb.dbo.sp_send_dbmail
			@profile_name = 'BIAdmin',
			@recipients = @recip,
			@body = @text,
			@subject = @subj,
			@body_format = 'HTML'

end
```

