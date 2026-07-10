# dbo.spSCSyncPayroll

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spSCSyncPayroll"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
/******************************************************************************
**
**	Name:		spSCDWRunCubeBuild
**
**	Description: 	Returns results for the Trend Report.
**
**
**	Parameters:	none
**
** 	Returns:	result set
**
**	Examples:	EXEC spSCSyncPayroll
**			

******************************************************************************/

CREATE   PROCEDURE  [dbo].[spSCSyncPayroll]

AS
SET NOCOUNT ON

Exec BABWSCORE01.Master..xp_cmdshell 'dtexec /sq "Sync Payroll" /ser BABWSCORE01'
```

