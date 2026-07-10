# dbo.vwDW_SSRSInternationalSubscriptions

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwDW_SSRSInternationalSubscriptions"]
    dbo_vwDW_WeekEnding(["dbo.vwDW_WeekEnding"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.vwDW_WeekEnding |

## View Code

```sql
CREATE VIEW [dbo].[vwDW_SSRSInternationalSubscriptions]
AS

/***********************************************************************************************
Object Name:	[vwDW_SSRSInternationalSubscriptions]

Author			Date			Comment
Gary Murrish	1/27/2015		Changed Germany Name to [Store].[Corporate].[Region].&[Franchisees-Build A Bear Deutschland GmbH]
Gary Murrish	5/30/2013		Changed currency for DE to ZUR from EUR
Gary Murrish	3/16/2012		Added Mexico to the reports
Gary Murrish    7/15/2011		Added Brazil and Kuwait to the reports
Gary Murrish	3/27/2011		Changed Germany name to [Store].[Corporate].[Region].&[Franchisees-DIE BÄRENMACHER HOLDING AG-DIE BÄRENMACHER HOLDING AG]
Gary Murrish	11/3/2010		ADDED CurrentFP and PreviousFP for the reports which run month
Gary Murrish	10/8/2010		Removed countries of NL,BE,TW,KR and RU per Karen's request.
Funmi Agbebi	1/20/2009		Added Region and Currency Specific Records 
Funmi Agbebi	12/19/2009		WeekEnding date now selected from vwDW_PreviousWeekEnding 
								(new view that calculates the PreviousWeek Ending date on the fly)
Funmi Agbebi	12/1/2009		original creation

Purpose:		View used for ssrs_subscriptions.  Stores different combinations of parameters for 
				Franchisee reports such as the FranchiseeOpsScorecard and FranchiseeStoreByStore reports.
				Sets Static/constant value for most parameters and determines the PreviousWeekEnding 
				date on the fly based on today's date
**********************************************************************************************/

--Select * from vwDW_SSRSInternationalSubscriptions where ReportID = 50 and Format = 'PDF' and Week like 'TwoWeeksAgo'

-- Select * from vwDW_SSRSInternationalSubscriptions where ReportID = 50 and Format = 'PDF' and Week like 'Current'

			--OpsScorecard at Company Level PDF Format

/* ----------------------------Generic Parameters for most report Subscriptions Begin---------------------------------------------------------- */

			--Franchisee Report at Company Level broken out by PDF Format


			SELECT 50 as ReportID
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (pdf) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'Previous' 

UNION
			SELECT 50 as ReportID
			,'TwoWeeksAgo' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (pdf) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'TwoWeeksAgo' 

UNION
			SELECT 50 as ReportID
			,'CurrentWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (pdf) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'Current' 

UNION
			SELECT 50 as ReportID
			,'CurrentPeriod' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName(pdf) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] like 'CurrentFP' 

UNION
			SELECT 50 as ReportID
			,'PreviousPeriod' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName(pdf) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] like 'PreviousFP' 

UNION
			SELECT 50 as ReportID
			,'CurrentFP' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,'[Date].[Fiscal].[Fiscal Period].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + RIGHT('0' + ltrim(rtrim(cast(d.fiscal_period as varchar(2)))),2) + ']' AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName(pdf) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] like 'Current' 

UNION
			SELECT 50 as ReportID
			,'PreviousFP' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,'[Date].[Fiscal].[Fiscal Period].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + RIGHT('0' + ltrim(rtrim(cast(d.fiscal_period as varchar(2)))),2) + ']' AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName(pdf) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] like 'PreviousFP' 

UNION
			SELECT 50 as ReportID
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (Excel) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'Previous' 

/* ----------------------------Generic Parameters for most report Subscriptions End---------------------------------------------------------- */

/* ----------------------------Parameters for FranchiseeStoreByStore Subscriptions Begin---------------------------------------------------------- */

UNION

			SELECT 51 as ReportID
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Week' as Breakout  
			,'EXCEL' as Format
			,'@ReportName (Excel) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'Previous' 


UNION

			SELECT 51 as ReportID
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod
			,d.actual_date as WeekEndingDate
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']'
				ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4)) 
				+ ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding
			, '[Store].[Corporate].[Company Level].&[Franchisees]' as GeographyMember
			,'[Currency].[Currency Code].[USD]' as Currency
			,'Week' as Breakout  
			,'PDF' as Format
			,'@ReportName (pdf) was executed at @ExecutionTime' as [Subject]
			FROM dbo.vwDW_WeekEnding d
 			where [Week] = 'Previous' 

/* ----------------------------Parameters for FranchiseeStoreByStore Subscriptions End---------------------------------------------------------- */

/* ----------------------------Parameters for FranchiseeOpsScorecard Subscriptions By Region and Local Currency in PDF format Begin---------------------------------------------------------- */

UNION 



			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - BAHRAIN]' AS GeographyMember
			,'[Currency].[Currency Code].[AED]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (BAHRAIN in AED) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION 



			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - UAE]' AS GeographyMember
			,'[Currency].[Currency Code].[AED]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (UAE in AED) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'			
/*			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB Stores Holding BV - BeNeLux-BAB Stores Holding BV - Belgium]' AS GeographyMember
			,'[Currency].[Currency Code].[EUR]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (BE in EUR) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BABW-AU-BABW-AU]' AS GeographyMember
			,'[Currency].[Currency Code].[AUD]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (AU in AUD) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB Stores Holding BV - BeNeLux-BAB Stores Holding BV - Netherlands]' AS GeographyMember
			,'[Currency].[Currency Code].[EUR]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (NL in EUR) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/
/*
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BearInMind Corp-BearInMind Corp - Taiwan]' AS GeographyMember
			,'[Currency].[Currency Code].[TWD]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (TW in TWD) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/

UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Central Dept Stores LTD-Central Dept Stores LTD - Thailand]' AS GeographyMember
			,'[Currency].[Currency Code].[THB]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (TH in THB) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose I/S - Denmark]' AS GeographyMember
			,'[Currency].[Currency Code].[DKK]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (DK in DKK) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose Norway A/S - Norway]' AS GeographyMember
			,'[Currency].[Currency Code].[NOK]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (NO in NOK) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose Sweden AB - Sweden]' AS GeographyMember
			,'[Currency].[Currency Code].[SEK]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (SW in SEK) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Build A Bear Deutschland GmbH]' AS GeographyMember
			,'[Currency].[Currency Code].[ZUR]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (DE in ZUR) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-FCI Retail Concepts PTE LTD-FCI Retail Concepts PTE LTD - Singapore]' AS GeographyMember
			,'[Currency].[Currency Code].[SGD]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (SG in SGD) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Hicel Co., Ltd. - Korea-Hicel Co., Ltd. - Korea]' AS GeographyMember
			,'[Currency].[Currency Code].[KRW]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (KR in KRW) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-INTENCITY ENTERTAINMENT (PTY) LTD-INTENCITY ENTERTAINMENT (PTY) LTD]' AS GeographyMember
			,'[Currency].[Currency Code].[ZAR]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (ZA in ZAR) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Make A Friend, Inc. - Japan-Make A Friend, Inc. - Japan]' AS GeographyMember
			,'[Currency].[Currency Code].[JPY]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (JP in JPY) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Traderus BS Limited-Traderus BS Limited - Russia]' AS GeographyMember
			,'[Currency].[Currency Code].[RUB]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (RU in RUB) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			

UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - KW]' AS GeographyMember
			,'[Currency].[Currency Code].[KWD]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (KW in KWD) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BBW Brasil Comercio e Representacoes S/A-BBW Brasil Comercio e Representacoes S/A]' AS GeographyMember
			,'[Currency].[Currency Code].[BRL]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (BZ in BRL) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Koates X Siempre-Koates X Siempre]' AS GeographyMember
			,'[Currency].[Currency Code].[MXN]' as Currency 
			,'Store' as Breakout
			,'PDF' as Format
			,'@ReportName (MX in MXN) (pdf) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
			
/* ----------------------------Parameters for FranchiseeOpsScorecard Subscriptions By Region and Local Currency in PDF format End---------------------------------------------------------- */

/* ----------------------------Parameters for FranchiseeOpsScorecard Subscriptions By Region and Local Currency in Excel format Begin---------------------------------------------------------- */
UNION 


			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - BAHRAIN]' AS GeographyMember
			,'[Currency].[Currency Code].[AED]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (BAHRAIN in AED) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION 


			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - UAE]' AS GeographyMember
			,'[Currency].[Currency Code].[AED]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (UAE in AED) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
			
/*			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB Stores Holding BV - BeNeLux-BAB Stores Holding BV - Belgium]' AS GeographyMember
			,'[Currency].[Currency Code].[EUR]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (BE in EUR) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BABW-AU-BABW-AU]' AS GeographyMember
			,'[Currency].[Currency Code].[AUD]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (AU in AUD) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB Stores Holding BV - BeNeLux-BAB Stores Holding BV - Netherlands]' AS GeographyMember
			,'[Currency].[Currency Code].[EUR]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (NL in EUR) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			
/*
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BearInMind Corp-BearInMind Corp - Taiwan]' AS GeographyMember
			,'[Currency].[Currency Code].[TWD]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (TW in TWD) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/

UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Central Dept Stores LTD-Central Dept Stores LTD - Thailand]' AS GeographyMember
			,'[Currency].[Currency Code].[THB]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (TH in THB) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose I/S - Denmark]' AS GeographyMember
			,'[Currency].[Currency Code].[DKK]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (DK in DKK) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose Norway A/S - Norway]' AS GeographyMember
			,'[Currency].[Currency Code].[NOK]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (NO in NOK)(Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose Sweden AB - Sweden]' AS GeographyMember
			,'[Currency].[Currency Code].[SEK]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (SW in SEK )(Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Build A Bear Deutschland GmbH]' AS GeographyMember
			,'[Currency].[Currency Code].[ZUR]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (DE in ZUR) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-FCI Retail Concepts PTE LTD-FCI Retail Concepts PTE LTD - Singapore]' AS GeographyMember
			,'[Currency].[Currency Code].[SGD]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (SG in SGD) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Hicel Co., Ltd. - Korea-Hicel Co., Ltd. - Korea]' AS GeographyMember
			,'[Currency].[Currency Code].[KRW]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (KR in KRW) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-INTENCITY ENTERTAINMENT (PTY) LTD-INTENCITY ENTERTAINMENT (PTY) LTD]' AS GeographyMember
			,'[Currency].[Currency Code].[ZAR]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (ZA in ZAR) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Make A Friend, Inc. - Japan-Make A Friend, Inc. - Japan]' AS GeographyMember
			,'[Currency].[Currency Code].[JPY]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (JP in JPY) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*			
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Traderus BS Limited-Traderus BS Limited - Russia]' AS GeographyMember
			,'[Currency].[Currency Code].[RUB]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (RU in RUB) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/

UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - KW]' AS GeographyMember
			,'[Currency].[Currency Code].[KWD]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (KW in KWD) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'

UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BBW Brasil Comercio e Representacoes S/A-BBW Brasil Comercio e Representacoes S/A]' AS GeographyMember
			,'[Currency].[Currency Code].[BRL]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (BZ in BRL) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 52 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Koates X Siempre-Koates X Siempre]' AS GeographyMember
			,'[Currency].[Currency Code].[MXN]' as Currency 
			,'Store' as Breakout
			,'EXCEL' as Format
			,'@ReportName (MX in MXN) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'			
			
-- Select * from [tmp_vwDW_SSRSInternationalSubscriptions] where ReportID = 52 and TimePeriod = 'PreviousWeek' order by Format

/* ----------------------------Parameters for FranchiseeOpsScorecard Subscriptions By Region and Local Currency in Excel format End---------------------------------------------------------- */

/* ----------------------------Parameters for FranchiseeStoreByStore Subscriptions By Region and Local Currency in Excel format Begins---------------------------------------------------------- */

--Select * from [tmp_vwDW_SSRSInternationalSubscriptions] where ReportID = 53 and format = 'Excel' and TimePeriod = 'PreviousWeek'  --storebystore


UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - BAHRAIN]' AS GeographyMember
			,'[Currency].[Currency Code].[AED]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (BAHRAIN in AED) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - UAE]' AS GeographyMember
			,'[Currency].[Currency Code].[AED]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (UAE in AED) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'			
/*			
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB Stores Holding BV - BeNeLux-BAB Stores Holding BV - Belgium]' AS GeographyMember
			,'[Currency].[Currency Code].[EUR]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (BE in EUR) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BABW-AU-BABW-AU]' AS GeographyMember
			,'[Currency].[Currency Code].[AUD]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (AU in AUD) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*			
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB Stores Holding BV - BeNeLux-BAB Stores Holding BV - Netherlands]' AS GeographyMember
			,'[Currency].[Currency Code].[EUR]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (NL in EUR) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			
/*
UNION
			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BearInMind Corp-BearInMind Corp - Taiwan]' AS GeographyMember
			,'[Currency].[Currency Code].[TWD]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (TW in TWD) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/

UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Central Dept Stores LTD-Central Dept Stores LTD - Thailand]' AS GeographyMember
			,'[Currency].[Currency Code].[THB]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (TH in THB) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose I/S - Denmark]' AS GeographyMember
			,'[Currency].[Currency Code].[DKK]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (DK in DKK) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose Norway A/S - Norway]' AS GeographyMember
			,'[Currency].[Currency Code].[NOK]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (NO in NOK) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Choose-Choose Sweden AB - Sweden]' AS GeographyMember
			,'[Currency].[Currency Code].[SEK]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (SW in SEK) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Build A Bear Deutschland GmbH]' AS GeographyMember
			,'[Currency].[Currency Code].[ZUR]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (DE in ZUR) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-FCI Retail Concepts PTE LTD-FCI Retail Concepts PTE LTD - Singapore]' AS GeographyMember
			,'[Currency].[Currency Code].[SGD]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (SG in SGD) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*			
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Hicel Co., Ltd. - Korea-Hicel Co., Ltd. - Korea]' AS GeographyMember
			,'[Currency].[Currency Code].[KRW]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (KR in KRW) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/			
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-INTENCITY ENTERTAINMENT (PTY) LTD-INTENCITY ENTERTAINMENT (PTY) LTD]' AS GeographyMember
			,'[Currency].[Currency Code].[ZAR]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (ZA in ZAR) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Make A Friend, Inc. - Japan-Make A Friend, Inc. - Japan]' AS GeographyMember
			,'[Currency].[Currency Code].[JPY]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (JP in JPY) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/*			
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Traderus BS Limited-Traderus BS Limited - Russia]' AS GeographyMember
			,'[Currency].[Currency Code].[RUB]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (RU in RUB) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
*/

UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BAB GULF FZE-BAB GULF FZE - KW]' AS GeographyMember
			,'[Currency].[Currency Code].[KWD]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (KW in KWD) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-BBW Brasil Comercio e Representacoes S/A-BBW Brasil Comercio e Representacoes S/A]' AS GeographyMember
			,'[Currency].[Currency Code].[BRL]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (BZ in BRL) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
UNION

			SELECT 53 as ReportID 
			,'PreviousWeek' as [TimePeriod]
			,d.week_of_period as WeekOfPeriod 
			,d.actual_date as WeekEndingDate 
			,CASE WHEN d.fiscal_week > 9 THEN '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' ' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' ELSE '[Date].[Fiscal].[Fiscal Week].&[' + cast(d.fiscal_year as varchar(4))  + ' 0' + ltrim(rtrim(cast(d.fiscal_week as varchar(2)))) + ']' END AS WeekEnding 
			,'[Store].[Corporate].[Region].&[Franchisees-Koates X Siempre-Koates X Siempre]' AS GeographyMember
			,'[Currency].[Currency Code].[MXN]' as Currency 
			,'Week' as Breakout
			,'EXCEL' as Format
			,'@ReportName (MX in MXN) (Excel) was executed at @ExecutionTime' as [Subject] 
			FROM dbo.vwDW_WeekEnding d  
			WHERE [Week] = 'Previous'
/* ----------------------------Parameters for FranchiseeStoreByStore Subscriptions By Region and Local Currency in Excel format Ends---------------------------------------------------------- */
/*
Select * from vwDW_SSRSInternationalSubscriptions where ReportID = 50 and TimePeriod = 'PreviousWeek'
Select * from vwDW_SSRSInternationalSubscriptions where ReportID = 51 and TimePeriod = 'PreviousWeek'
Select * from vwDW_SSRSInternationalSubscriptions where ReportID = 52 and TimePeriod = 'PreviousWeek'
Select * from vwDW_SSRSInternationalSubscriptions where ReportID = 53 and TimePeriod = 'PreviousWeek'
*/
```

