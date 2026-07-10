# dbo.spMoveStyleSummaryReports

**Database:** reportingservices_subscription  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMoveStyleSummaryReports"]
    CurrentDateInformation(["CurrentDateInformation"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| CurrentDateInformation |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Gary Murrish
-- Create date: 10/11/2012
-- Description:	Push the Sunday Style Summary reports to the proper directories
-- =============================================
CREATE PROCEDURE [dbo].[spMoveStyleSummaryReports]
    @rootTargetDirectory AS VARCHAR(255)    = '\\sharebear1\groups\Planning\StyleSummaryReports',
    @sourceDirectory     AS VARCHAR(255)    = '\\babwscore01\D\Run SSRS Reports\Drop'
-- Don't put the trailing backslash on the directory names.
-- Remember all of these directories are relative to the SQL Server which is executing them
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @destinationDirectory VARCHAR(255)
	DECLARE @fiscalPeriod INTEGER
	DECLARE @fiscalYear INTEGER



	-- Get the Fiscal Period being reported on 
	SELECT @fiscalPeriod = FiscalPeriod, @fiscalYear = fiscalYear
	FROM
		CurrentDateInformation cdi


	SET @destinationDirectory = @rootTargetDirectory + '\' + cast(@fiscalYear AS VARCHAR)+ '\' + cast(@fiscalPeriod AS VARCHAR)


	DECLARE @cmd VARCHAR(255)

	-- Create the target directory
	SET @cmd = 'mkdir "' + @destinationDirectory + '"'
	EXEC master..xp_CMDShell @cmd

	-- Clear out the pdfs in the target root directory from last week
	SET @cmd = 'DEL "' + @rootTargetDirectory + '\*.pdf"'
	EXEC master..xp_CMDShell @cmd

	-- Copy this week's pdfs to the target directory
	SET @cmd = 'COPY /Y "' + @sourceDirectory + '\*.pdf" "' + @destinationDirectory + '\"'
	EXEC master..xp_CMDShell @cmd

	-- Copy this week's pdfs to the root directory
	SET @cmd = 'MOVE /Y "' + @sourceDirectory + '\*.pdf" "' + @rootTargetDirectory + '\"'
	EXEC master..xp_CMDShell @cmd

END
```

