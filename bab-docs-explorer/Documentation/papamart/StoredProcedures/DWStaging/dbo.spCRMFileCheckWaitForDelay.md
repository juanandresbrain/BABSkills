# dbo.spCRMFileCheckWaitForDelay

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCRMFileCheckWaitForDelay"]
    tmpTransactionFileCheck(["tmpTransactionFileCheck"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| tmpTransactionFileCheck |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spCRMFileCheckWaitForDelay]

as 

set nocount on;

with 
FileTypes as
	(
		select 'CIM_header.txt' as FileType
		UNION
		select 'CIM_detail.txt' as FileType
		UNION
		select 'CIM_tender.txt' as FileType
		--UNION
		--select 'CUST.dat' as FileType
		--UNION
		--select 'Attr.dat' as FileType
	),
MaxFiles as
	(
		select 
			ft.FileType,
			Max(fc.FullFileName) as MaxFile
		from FileTypes ft
		left join tmpTransactionFileCheck fc 
							on ft.FileType = case when ft.FileType in ('CIM_header.txt','CIM_detail.txt', 'CIM_tender.txt') 
														then substring(fc.FullFileName, 1,14)
														else substring(fc.FullFilename, 1,8)
												 end
		group by ft.FileType
	),
FileStats as
	(
		select 
				ft.FileType, 
				mf.MaxFile as FullFileName,
				fc.FileDateTime,
				isnull(fc.FileProcessed,0) FileProcessed, 
				getdate() as CurrentDateTime,
				case 
					when isnull(fc.FileProcessed,0) = 1
						and datediff(mi, fc.FileDateTime, getdate()) >= 52
					then 1
					else 0
				end as ProcessedAgeOK,
				case when isnull(fc.FileProcessed,0) = 1
					then datediff(mi, fc.FileDateTime, getdate()) 
					else 0
				end as ProcessedAge,
				case 
					when isnull(fc.FileProcessed,0) = 0 
						 OR datediff(dd, fc.FileDateTime, getdate()) <> 0
						then 52
					when isnull(fc.FileProcessed,0) = 1
						and datediff(mi, fc.FileDateTime, getdate()) < 52
						and datediff(dd, fc.FileDateTime, getdate()) = 0
						then 52 - datediff(mi, fc.FileDateTime, getdate()) 
					else 0
					end as WaitMinutes
		from FileTypes ft 
		left join MaxFiles mf on ft.FileType = mf.FileType
		left join tmpTransactionFileCheck fc 
							on ft.FileType = case when ft.FileType in ('CIM_header.txt','CIM_detail.txt', 'CIM_tender.txt') 
														then substring(fc.FullFileName, 1,14)
														else substring(fc.FullFilename, 1,8)
												 end
							and mf.MaxFile = fc.FullFileName 
	) 
select 
	FileType, 
	isnull(FullFileName, 'no file found') as FullFileName,
	case when datediff(dd, FileDateTime, getdate()) = 0 then 'YES' else 'NO' end as FileStaged,
	case when datediff(dd, FileDateTime, getdate()) = 0 and FileProcessed = 1 then 'YES' else 'NO' end as FileProcessed,
	WaitMinutes 
into #TMP
from FileStats 


declare 
	@WaitMin varchar(10),
	@WaitFor varchar(10),
	@SQL varchar(100)

select @WaitMin = max(WaitMinutes) from #TMP
select @WaitFor = '00:' + @WaitMin + ':00'
select @SQL = 'Waitfor Delay ''' + @Waitfor + ''''
exec(@SQL)


select cast(count(*) as int) as UnprocessedCount from #TMP where FileProcessed = 'NO'
```

