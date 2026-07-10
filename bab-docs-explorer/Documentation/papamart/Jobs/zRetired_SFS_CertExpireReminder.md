# Job: zRetired_SFS_CertExpireReminder

**Enabled:** No  
**Server:** papamart  
**Description:** Direct Marketing sends email reminders to guests who have certificates that are 1 and 3 months from expiration. This job provides data for the email.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["zRetired_SFS_CertExpireReminder"]
    JOB --> S1["Step 1: create file [TSQL]"]
```

## Steps

### Step 1: create file
**Subsystem:** TSQL  

```sql
--Certs Expiration Reminder Data Pull
--Data used by reminder email sent by Ashley B
--There files are output.  One is data and one is header.  Only file used by Ashley is CertReminder3And5MonthYYYYMM.txt.
--Can delete files CertReminder3And5Month_HEADER and CertReminder3And5Month_DATA
--This script is in subversion in 
--C:\Databears\Server Objects\Papamart\Scripts--SFSCertExpirationReminderEmail.sql
--Date:				Name:				Change:
--2012-08-23		GaryD				Modify expiration date logic
--2012-10-06		GaryD				Add month 4 during Christmas season

---------------------------------------------
--7/17/2012 run
----------------------------------------------------

IF OBJECT_ID(N'tempdb.dbo.#tmpT1', N'U') IS NOT NULL
	DROP TABLE #tmpT1
	
        SELECT * 
          into #tmpT1
          FROM papamart.queries.dbo.SFS_EarnedCerts_Master with (nolock)
           WHERE cast(earneddate as datetime) between CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(GETDATE())-1),DATEADD(MONTH, -7, GETDATE())),101) and CONVERT(VARCHAR(25), DATEADD(ms, -3, DATEADD(mm, DATEDIFF(mm, 0, GETDATE()), 0)) , 101)
           AND redemption_date IS NULL
           AND email_stat_cd = 'VALID'
           and cast(expirationdate as datetime) >= getdate()

--select top 1000 * from #tmpT1

IF OBJECT_ID(N'tempdb.dbo.#tmpT2', N'U') IS NOT NULL
	DROP TABLE #tmpT2

select email_addr_txt
      ,sfsnumber
      ,firstname
      ,lastname
      ,case when country = 'USA' and state in ('PR', 'Puerto Rico','PUERTORICO') then 'PR'
            when country = 'USA' and state not in ('PR', 'Puerto Rico','PUERTORICO') then 'US'
            when country = 'CAN' and state in ('QC', 'Quebe','Quebec') then 'QC'
            when country = 'CAN' and state not in ('QC', 'Quebe','Quebec') then 'CA'
            when country = '' then 'US'
            else ISNULL(country, 'US') 
       end as cntry
      ,serialized
      ,earneddate
      ,expirationdate
  into #tmpT2
  from #tmpT1 t1
 where earneddate = (select min(earneddate)  --get earliest earned
                       from #tmpT1 s1
                      where t1.email_addr_txt = s1.email_addr_txt)

--select top 100 * from #tmpT2

IF OBJECT_ID(N'tempdb.dbo.#tmpT3', N'U') IS NOT NULL
	DROP TABLE #tmpT3

select email_addr_txt
      ,sfsnumber
      ,firstname
      ,lastname
      ,cntry
      ,serialized
      ,earneddate
      ,expirationdate
  into #tmpT3
  from #tmpT2 t2
 where serialized = (select min(serialized)  --get lowest number if multiples
                       from #tmpT2 s2
                      where t2.email_addr_txt = s2.email_addr_txt)

IF OBJECT_ID(N'tempdb.dbo.#tmpT4', N'U') IS NOT NULL
	DROP TABLE #tmpT4

select distinct email_addr_txt
      ,sfsnumber
      ,firstname
      ,lastname
      ,cntry
      ,serialized
      ,earneddate
      ,expirationdate
  into #tmpT4
  from #tmpT3
--539,667 rows in #tmpT4

/*QC checks
--check the system expiration dates and earned dates
select distinct cast(expirationdate as datetime)
from #tmpT4
order by cast(expirationdate as datetime)

select cast(expirationdate as datetime), count(*)
from #tmpT4
group by cast(expirationdate as datetime)
order by cast(expirationdate as datetime)

select distinct expirationdate
from #tmpT4
order by expirationdate

*/

---update earned and expire dates to be consistent
--some dates are MM/DD/YYYY and others are YYYY/MM/DD.  
update  #tmpT4
set expirationdate = '2012/10/31'
where expirationdate = '10/31/2012'

/*QC checks
select top 100 * from #tmpT4 where sfsnumber = '708134439'
select top 100 * from #tmpT4 where datediff(month, '8/31/2012', expirationdate ) = 0--5
select top 100 * from #tmpT4 where datediff(month, '2012/03/31', earneddate ) = 0--3
select top 100 * from #tmpT4
select min(earneddate) from #tmpT4
*/

IF OBJECT_ID(N'queries.dbo.TMP_CertReminder', N'U') IS NOT NULL
	DROP TABLE queries.dbo.TMP_CertReminder

select  
	email_addr_txt 'email_address'
	,sfsnumber 'sfs_number'
	,firstname 'first_name'
    ,lastname 'last_name'
    ,cntry
    ,serialized 'sfscert'
    ,right('00' + cast(month(earneddate) as varchar(2)), 2) + '/' + right('00' + cast(day(earneddate) as varchar(2)), 2) +  '/'  + cast(year(earneddate) as char(4)) as 'earndate' 
    ,right('00' + cast(month(expirationdate) as varchar(2)), 2) +  '/' + right('00' + cast(day(expirationdate) as varchar(2)), 2) +  '/'  + cast(year(expirationdate) as char(4)) as 'systemexpdate'
    ,
    CASE
		WHEN cast(expirationdate as datetime) < '2012/09/01' 
		THEN
			right('00' + cast(month(    (  CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,1,DATEADD(month, -1, expirationdate)))),DATEADD(mm,1,DATEADD(month, -1, expirationdate))),101)  )  ) as varchar(2)), 2) 
			+  '/'  + right('00' + cast(day(     (   CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,1,DATEADD(month, -1, expirationdate)))),DATEADD(mm,1,DATEADD(month, -1, expirationdate))),101)   )    ) as varchar(2)), 2) 
			+  '/'  + cast(year(        (   CONVERT(VARCHAR(25),DATEADD(dd,-(DAY(DATEADD(mm,1,DATEADD(month, -1, expirationdate)))),DATEADD(mm,1,DATEADD(month, -1, expirationdate))),101)    )      ) as char(4)) 
		ELSE
			right('00' + cast(month(expirationdate) as varchar(2)) , 2)
			+  '/'  + '15'
			+  '/'  + cast(year(expirationdate) as char(4))
	END as 'exp_date'
    ,case
		when datediff(month, earneddate, getdate()) = 3 then 3
		when datediff(month, earneddate, getdate()) = 4 then 4
		when datediff(month, earneddate, getdate()) = 5 then 5
	else 99
	end as 'monthsold'
	into queries.dbo.TMP_CertReminder
from #tmpT4
where datediff(month, earneddate, getdate()) in (3, 4, 5)
---169,403 rows in TMP_CertReminder

/*QC checks
select top 1000 * from queries.dbo.TMP_CertReminder

select monthsold, count(*) GuestCount
from dbo.TMP_CertReminder with (nolock) 
group by monthsold
*/

--select top 1000 * from queries.dbo.TMP_CertReminder return


/*QC checks
select top 100 * 
from TMP_CertReminder
where sfsnumber = '707794180' 

select top 100 *
from queries.dbo.SFS_EarnedCerts_Master with (nolock)
where sfsnumber = '707794180'
*/

-------------Get column headings for inclusion in file
    DECLARE @cmd varchar(1000),
        @filename varchar(100),
		@filename_header varchar(100),
        --@path varchar(200),
        @filedate varchar(20),
        @selectstmnt varchar(5000),
        @bcpsql varchar(500),
		@columnheaders varchar(4000), 
		@tablename varchar(128)

--CREATE TABLE CONTAINING COLUMN HEADERS FOR FILE EXPORT
SET @columnheaders = ''
SET @tablename='TMP_CertReminder'

SELECT @columnheaders = @columnheaders + c.name + char(9) 
 FROM syscolumns c INNER JOIN sysobjects o ON o.id = c.id
 WHERE o.name = @tablename
 ORDER BY colid

SELECT @columnheaders = Substring(@columnheaders, 1, Datalength(@columnheaders) - 1)


if (Object_ID('queries.dbo.TMP_CertReminder_HEADER') IS NOT NULL) DROP TABLE queries.dbo.TMP_CertReminder_HEADER

SELECT @columnheaders AS columnheader
INTO queries.dbo.TMP_CertReminder_HEADER


--create directory to put files
declare @MD varchar(500), @Path varchar(500),@yyyy varchar(4), @mm varchar(2)
,@DELh varchar(500), @DELd varchar(500) 

SET @yyyy = YEAR(GETDATE())
SET @mm = RIGHT('00' + CAST(month(getdate()) AS VARCHAR(2)) , 2)

SET @Path = '\\sharebear1\Shared\Direct Marketing\Sharepoint Site\SFS PROGRAM\CERTIFICATES\Cert_Reminder_Email\' + @yyyy + @mm + '\'

--select @Path

SET @MD = ' mkdir ' + '"\\sharebear1\Shared\Direct Marketing\Sharepoint Site\SFS PROGRAM\CERTIFICATES\Cert_Reminder_Email\' + @yyyy + @mm + '"' 

--select @MD
EXEC xp_cmdshell @MD, no_output



    --SET @path = '\\sharebear1\Shared\Direct Marketing\Sharepoint Site\SFS PROGRAM\CERTIFICATES\Cert_Reminder_Email\201207\'
	SET @filedate = CONVERT(VARCHAR(20), GETDATE(), 112)
    SET @filename = 'CertReminder3And5Month_DATA.txt'
	SET @filename_header = 'CertReminder3And5Month_HEADER.txt'

--CREATE FILE CONTAINING EMAILS USING BCP COMMAND
    SET @selectstmnt = 'SELECT * FROM queries.dbo.TMP_CertReminder'
    SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename 
        + '" -t "\t" -T -c'
    EXEC master..xp_cmdshell @bcpsql--, no_output

    SET @selectstmnt = 'SELECT * FROM queries.dbo.TMP_CertReminder_HEADER'
    SET @bcpsql = 'bcp "' + @selectstmnt + '" queryout "' + @path + @filename_header
        + '" -t "\t" -T -c'
    EXEC master..xp_cmdshell @bcpsql--, no_output

    SET @cmd = 'copy "' + @path + @filename_header + '" + "' + @path + @filename + '"'
            + ' "' + @path + 'CertReminder3And5Month_' + @filedate + '.txt"' 

--select @cmd

    EXEC master..xp_cmdshell @cmd, no_output


---clean up the header and data file
SET @DELh = ' del ' + '"' + @Path + 'CertReminder3And5Month_HEADER.txt' + '"'
--select @DELh
EXEC xp_cmdshell @DELh, no_output

SET @DELd = ' del ' + '"' + @Path + 'CertReminder3And5Month_DATA.txt' + '"'
--select @DELd
EXEC xp_cmdshell @DELd, no_output


---send an email to let Direct Marketing know the file is waiting


declare @bodytext varchar(4000)
--,@Path varchar(500)

SET @Path = '\\sharebear1\Shared\Direct Marketing\Sharepoint Site\SFS PROGRAM\CERTIFICATES\Cert_Reminder_Email\'

set @bodytext = 'The latest certificate expiration reminder file has been created and is located in "' + @Path +  + @yyyy + @mm + '\' +  '".'
+ char(13)
+ char(13)
+ ' This email was produced by the ' + @@servername + ' job "SFS_CertExpireReminder"'

EXEC msdb.dbo.sp_send_dbmail
    @recipients = 'EdinP@buildabear.com',
    @body = @bodytext,
    @subject = 'SFS 3, 4 &5 Month Reminder' ;
```

