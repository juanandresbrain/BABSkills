# dbo.vwDW_SSRSSubscriptionsWIP

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SSRSSubscriptionsWIP"]
    dbo_vwDW_WeekEnding(["dbo.vwDW_WeekEnding"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwDW_WeekEnding |

## View Code

```sql
/***********************************************************************************************
Object Name:	[vwDW_SSRSSubscriptions]

Author			Date			Comment

Funmi Agbebi	12/19/2009		WeekEnding date now selected from vwDW_PreviousWeekEnding 
								(new view that calculates the PreviousWeek Ending date on the fly)
								Records added for European subscriptions and Top 7 reports
Funmi Agbebi	12/1/2009		original creation


Purpose:		View used for ssrs_subscriptions.  Stores different combinations of parameters for 
				SSRS reports such as the OpsScorecard and StoreByStore reports.
				Sets Static/constant value for most parameters and determines the PreviousWeekEnding 
				date on the fly based on today's date
**********************************************************************************************/

CREATE VIEW [dbo].[vwDW_SSRSSubscriptionsWIP]
AS


/* ----------------------------OpsScorecard Subscriptions Begin---------------------------------------------------------- */

			--OpsScorecard at Company Level broken out by PDF Format

			SELECT 23 as ReportID
			,case when d.fiscal_week > 9 then '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				else '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' end as WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Company Level' as Breakout
			,'PDF' as Format
			,'OpsScorecard (Company Level) (USD) (pdf) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION
			
			--OpsScorecard by Bear Range PDF Format

			SELECT	23 as ReportID
			,case when d.fiscal_week > 9 then '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				else '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' end as WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Bear Range' as Breakout
			,'PDF' as Format
			,'OpsScorecard (Bear Range) (USD) (pdf) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 
UNION 

			--OpsScorecard by Region PDF Format

			SELECT	23 as ReportID
			,case when d.fiscal_week > 9 then '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				else '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' end as WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Region' as Breakout
			,'PDF' as Format
			,'OpsScorecard (Region) (USD) (pdf) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION
			--OpsScorecard by Bearitory PDF Format

			SELECT	23 as ReportID
			,case when d.fiscal_week > 9 then '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				else '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' end as WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Bearitory' as Breakout
			,'PDF' as Format
			,'OpsScorecard (Bearitory) (USD)(pdf) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION
		--OpsScorecard for North America by Bear Range in Excel Format

			SELECT	23 as ReportID
			,case when d.fiscal_week > 9 then '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				else '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' end as WeekEnding
			, '[Store].[Corporate].[Bear Range].&[Company-North America]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Bear Range' as Breakout
			,'EXCEL' as Format
			,'OpsScorecard (North America) (USD) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION

		--OpsScorecard for North America by Region in Excel Format

			SELECT	23 as ReportID
			,case when d.fiscal_week > 9 then '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				else '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' end as WeekEnding
			, '[Store].[Corporate].[Bear Range].&[Company-North America]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Region' as Breakout
			,'EXCEL' as Format
			,'OpsScorecard (NA Regions) (USD) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION
		--OpsScorecard for UK Region in GBP in Excel Format

			SELECT	23 as ReportID
			,case when d.fiscal_week > 9 then '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				else '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' end as WeekEnding
			, '[Store].[Corporate].[Region].&[Company-Europe-UK]' as GeographyMember
			,'[Destination Currency].[Currency Code].[GBP]' as Currency
			,'Region' as Breakout
			,'EXCEL' as Format
			,'OpsScorecard (UK Region) (GBP) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION

		--OpsScorecard for FR & IE Region in EUR in Excel Format

			SELECT	23 as ReportID
			,case when d.fiscal_week > 9 then '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				else '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' end as WeekEnding
			, '[Store].[Corporate].[Region].&[Company-Europe-France and Eire]' as GeographyMember
			,'[Destination Currency].[Currency Code].[EUR]' as Currency
			,'Region' as Breakout
			,'EXCEL' as Format
			,'OpsScorecard (FR & IE Region) (EUR) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 


/* ----------------------------OpsScorecard Subscriptions End---------------------------------------------------------- */

/* ----------------------------StoreByStore Subscriptons Begin---------------------------------------------------------- */

UNION

			--StoreByStore at Company Level by Week in PDF Format

			SELECT 24 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Week' as ReportingLevel
			,'PDF' as Format
			,'StoreByStore (Fiscal Week) (USD) (pdf) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION

			--StoreByStore at Company Level by Period in PDF Format

			SELECT 24 as ReportID 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Period' as ReportingLevel
			,'PDF' as Format
			,'StoreByStore (Fiscal Period) (USD) (pdf) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION
			--StoreByStore at Company Level by Quarter in PDF Format

			SELECT 24 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Quarter' as ReportingLevel
			,'PDF' as Format
			,'StoreByStore (Fiscal Quarter) (USD) (pdf) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION
			--StoreByStore at Company Level by Year in PDF Format

			SELECT 24 as ReportID 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Year' as ReportingLevel
			,'PDF' as Format
			,'StoreByStore (Fiscal Year) (pdf)(USD) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION

			--StoreByStore at Company Level by Week in Excel Format

			SELECT 	24 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Company]' as GeographyMember
			,'[Destination Currency].[Currency Code].[USD]' as Currency
			,'Week' as ReportingLevel
			,'EXCEL' as Format
			,'StoreByStore (Fiscal Week) (USD) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 


UNION
			--StoreByStore by Week for UK Region in GBP in Excel Format

			SELECT 	24 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Region].&[Company-Europe-UK]' as GeographyMember
			,'[Destination Currency].[Currency Code].[GBP]' as Currency
			,'Week' as ReportingLevel
			,'EXCEL' as Format
			,'StoreByStore (Fiscal Week) (UK Region) (GBP) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION
			--StoreByStore by Month for UK Region in GBP in Excel Format

			SELECT 	24 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Region].&[Company-Europe-UK]' as GeographyMember
			,'[Destination Currency].[Currency Code].[GBP]' as Currency
			,'Period' as ReportingLevel
			,'EXCEL' as Format
			,'StoreByStore (Fiscal Period) (UK Region) (GBP) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

UNION
			--StoreByStore by Week for FR & IE Region in EUR in Excel Format

			SELECT 	24 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Region].&[Company-Europe-France and Eire]' as GeographyMember
			,'[Destination Currency].[Currency Code].[EUR]' as Currency
			,'Week' as ReportingLevel
			,'EXCEL' as Format
			,'StoreByStore (Fiscal Week) (FR & IE Region) (EUR) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 


UNION
			--StoreByStore by Month for FR & IE Region in EUR in Excel Format

			SELECT 	24 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Region].&[Company-Europe-France and Eire]' as GeographyMember
			,'[Destination Currency].[Currency Code].[EUR]' as Currency
			,'Period' as ReportingLevel
			,'EXCEL' as Format
			,'StoreByStore (Fiscal Period) (FR & IE Region) (EUR) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 

/* ----------------------------StoreByStore Subscriptons End---------------------------------------------------------- */

/* ----------------------------Top7OpsScorecard Subscriptons Begin---------------------------------------------------------- */

			--Top7StoreByStore by Week for Top 7 UK Stores in GBP in Excel Format

UNION

		--Top7OpsScorecard for Top 7 UK Stores in GBP in Excel Format (Sunday schedule)

			SELECT	25 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Store Ranking].[Store Rank].&[Top 7 UK Stores]' as GeographyMember
			,'[Destination Currency].[Currency Code].[GBP]' as Currency
			,'Company Level' as Breakout
			,'EXCEL' as Format
			,'Top7OpsScorecard (Top 7 UK Stores) (GBP) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 


UNION
		--Top7OpsScorecard for Top 7 UK Stores in GBP in Excel Format (Mon - Sat Schedule)

			SELECT	25 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Store Ranking].[Store Rank].&[Top 7 UK Stores]' as GeographyMember
			,'[Destination Currency].[Currency Code].[GBP]' as Currency
			,'Company Level' as Breakout
			,'EXCEL' as Format
			,'Top7OpsScorecard (Top 7 UK Stores) (GBP) (Excel) was executed at @ExecutionTime' as [Subject]
			,'Current' as [Week]
			FROM dbo.vwDW_WeekEnding d
			where [Week] = 'Current'

/* ----------------------------Top7OpsScorecard Subscriptons End---------------------------------------------------------- */

/* ----------------------------Top7StoreByStore Subscriptons Begin---------------------------------------------------------- */
UNION

		--Top7StoreByStore for Top 7 UK Stores in GBP in Excel Format (Sunday schedule)

			SELECT 	26 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Store Ranking].[Store Rank].&[Top 7 UK Stores]' as GeographyMember
			,'[Destination Currency].[Currency Code].[GBP]' as Currency
			,'Week' as ReportingLevel
			,'EXCEL' as Format
			,'Top7StoreByStore (Fiscal Week) (Top 7 UK Stores) (GBP) (Excel) was executed at @ExecutionTime' as [Subject]
			,'TwoWeeksAgo' as [Week] -- 			,'Previous' as [Week]
			FROM dbo.vwDW_WeekEnding d 
 			where [Week] = 'TwoWeeksAgo' --  			where [Week] = 'Previous' 


UNION

		--Top7StoreByStore for Top 7 UK Stores in GBP in Excel Format (Mon - Sat schedule)

			SELECT 	26 as ReportID
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Store Ranking].[Store Rank].&[Top 7 UK Stores]' as GeographyMember
			,'[Destination Currency].[Currency Code].[GBP]' as Currency
			,'Week' as ReportingLevel
			,'EXCEL' as Format
			,'Top7StoreByStore (Fiscal Week) (Top 7 UK Stores) (GBP) (Excel) was executed at @ExecutionTime' as [Subject]
			,'Current' as [Week]
			FROM dbo.vwDW_WeekEnding d 
			where [Week] = 'Current'

/* ----------------------------Top7StoreByStore Subscriptons End---------------------------------------------------------- */

--select * from [dbo].[vwDW_SSRSSubscriptionsWIP] order by reportid, currency,format

--select * from [dbo].[vwDW_SSRSSubscriptions] order by reportid, currency,format

--OpsScorecard Excel Email Subscription


/*

Data Sources:
1) BAB SSAS

Connection String: (SSAS)
Data Source=babwscore01;Initial Catalog="BAB DW"

2) SRSUserDefaults 
Connection String: (SQL Server)
Data Source=BABWSCORE01;Initial Catalog=BABDWConfig


DonnaCr@buildabear.co.uk;RogerP@buildabear.co.uk;GaryR@buildabear.co.uk


Description:
OpsScorecard Europe Excel Email Subscription

Connection String: (SQL Server)
data source=PAPAMART; initial catalog=reportingservices_subscription

Query:
Select * from vwDW_SSRSSubscriptions where ReportID = 24 and Format = 'Excel' 
and Currency not like '%USD%'

Recipients:
To: BL-UK@buildabear.com
cc: funmia@buildabear.com;keithm@buildabear.com

*/
```

