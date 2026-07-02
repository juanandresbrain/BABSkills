# dbo.spForgetMeNewRequestEmail

**Database:** BABWForgetMe_Restore  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spForgetMeNewRequestEmail"]
    dbo_ActionRequest(["dbo.ActionRequest"]) --> SP
    dbo_ActionStatus(["dbo.ActionStatus"]) --> SP
    dbo_ApplicationDim(["dbo.ApplicationDim"]) --> SP
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
    dbo_vwCurrentForgetMeStatus(["dbo.vwCurrentForgetMeStatus"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ActionRequest |
| dbo.ActionStatus |
| dbo.ApplicationDim |
| dbo.sp_send_dbmail |
| dbo.vwCurrentForgetMeStatus |

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[spForgetMeNewRequestEmail]  

-- Name: spForgetNewMeRequestEmail
--
-- Description:	Emails user using ForgetMe application  
-- l
-- Output: email
-- 
-- Available actions: 
--
-- Dependency: 
--		
--
-- Revision History
--		Name:			Date:			Comments:
--		Ben Barud		2019/12/13		Creation


--SELECT @recipients = 'benb@buildabear.com; blaken@buildabear.com; gregd@buildabear.com',
--SELECT @recipients = 'benb@buildabear.com',
--SELECT @recipients = 'nigelt@buildabear.com; nigelt@buildabear.com',
--SELECT @recipients = 'nigelt@buildabear.com; benb@buildabear.com; heatherv@buildabear.com; blaken@buildabear.com',
--SELECT @recipients = 'benb@buildabear.com',

AS
BEGIN

SET NOCOUNT ON  

DECLARE @recipients NVARCHAR(2000),
		@copy_recipients NVARCHAR(2000),
		@subject NVARCHAR(1000),
		@MessageTxt NVARCHAR(2000),
		@forgetMeUri NVARCHAR(100)

select @recipients = COALESCE(@recipients + '; ','') + a.TeamEmailAddress
from (select distinct TeamEmailAddress
        from ApplicationDim) a
--SELECT @recipients = 'blaken@buildabear.com'
SET @copy_recipients = 'gregd@buildabear.com; blaken@buildabear.com'
SET @subject = 'New ForgetMe Requests'
SET @MessageTxt = 'There are new ForgetMe requests'
SET @forgetMeUri = 'https://intranet.buildabear.com/ForgetMe2?page=my-systems'

Declare @Body varchar(8000),
		@Body1 varchar(max),
		@Xml varchar(max),
		@TableTail varchar(max)
			  
Set @Body1 = '';		 
		 
SET NOCOUNT ON
		
Set @TableTail = '</table><br><br><br>This email has been generated from STL-SQL-P-02.BABWForgetMe.dbo.spForgetMeNewRequestEmail</body></html>';		 

		
If (0 < (Select Count(*) FROM [BABWForgetMe].[dbo].[ActionStatus] A		
			LEFT OUTER JOIN  [BABWForgetMe].[dbo].[ActionRequest] D ON D.ActionRequestID = A.ActionRequestID 
			where CompletionDate IS NULL
			AND (SELECT DATEDIFF(d, getutcdate(), DATEADD(DAY, 30, ValidationDate))) = 29))
			 
		BEGIN
		SET @Xml = CAST((SELECT LEFT([EmailAddress], 3) + '*****@' 
	   + SUBSTRING([EmailAddress], CHARINDEX('@',[EmailAddress])+1,(LEN([EmailAddress]) - CHARINDEX('@',[EmailAddress])+1))

		 AS 'td','',
		[InsertDate] AS 'td' ,'',
		[ActionRequestName] as 'td'  
		FROM 
		(SELECT *  
		FROM [STL-SQL-P-02].BABWForgetMe.dbo.vwCurrentForgetMeStatus where CompletionDate IS NULL
		AND (SELECT DATEDIFF(d, getutcdate(), DATEADD(DAY, 30, ValidationDate))) = 29) tab
		FOR XML PATH('tr'), ELEMENTS ) AS NVARCHAR(MAX));

		SET @Body1 ='<html><body><H3>
		New ForgetMe Requests </H3>
		<tr>There are new ForgetMe requests.  Please login to the ForgetMe app and make your required updates by ' + CAST(CAST(DATEADD(DAY, 15, GETDATE()) AS DATE) AS VARCHAR(10)) + '.</tr> <br><br>
		<a href="' + @forgetMeUri + '">https://intranet.buildabear.com/ForgetMe2</a> <br><br>
		<tr>This is system generated report. Please do not reply.</tr><br><br>
		<table border = 1> 
		<tr bgcolor="#C0C0C0">
		<th> EmailAddress </th> 
		<th>InsertDate </th> 
		<th> ActionRequestName </th> 
		</tr>'
		
		SET @Body1 = @Body1 + @Xml
		SELECT @Body =  @Body1+ @TableTail
		
		EXEC msdb.dbo.sp_send_dbmail @recipients = @recipients, @copy_recipients = @copy_recipients, @subject = @subject, @body = @Body, @body_format = 'HTML'
		
	END
END
```

