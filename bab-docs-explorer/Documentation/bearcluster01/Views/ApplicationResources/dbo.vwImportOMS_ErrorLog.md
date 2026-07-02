# dbo.vwImportOMS_ErrorLog

**Database:** ApplicationResources  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwImportOMS_ErrorLog"]
    dbo_ServiceLoggingGeneralUsage(["dbo.ServiceLoggingGeneralUsage"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ServiceLoggingGeneralUsage |

## View Code

```sql
CREATE view [dbo].[vwImportOMS_ErrorLog]

as
------------------------------------------------------------------------------------------------------------------------------------
--Dan Tweedie - 2017-09-14 - Returns OrderNumber, ErrorMessage, LogDateTime for orders which errored during xml extract to stage
------------------------------------------------------------------------------------------------------------------------------------

--select 
--	cast(substring(FunctionName,charindex('ImportOMSOrders|',FunctionName)+16,10) as varchar(10)) as OrderNumber, 
--	Message as ErrorMessage,
--	max(LogCreatedDate) as LogDateTime
--from ServiceLoggingGeneralUsage with (nolock)
--where left(FunctionName,16) = 'ImportOMSOrders|'
--group by 
--	substring(FunctionName,charindex('ImportOMSOrders|',FunctionName)+16,10), 
--	Message



--GO



WITH 
	ErrorLog as
		(
			select 
				cast(substring(FunctionName,charindex('ImportOMSOrders|',FunctionName)+16,10) as varchar(10)) as OrderNumber, 
				Message as ErrorMessage,
				--max(LogCreatedDate) as LogDateTime
				LogCreatedDate as LogDateTime
			from ServiceLoggingGeneralUsage with (nolock)
			where left(FunctionName,16) = 'ImportOMSOrders|'
			--group by 
			--	substring(FunctionName,charindex('UpdateShippedOrders|',FunctionName)+20,10), 
			--	Message
		),
	Attempts as
		(
			select 
				OrderNumber, 
				count(*) Attempts
			from ErrorLog
			where datediff(dd, LogDateTime, getdate()) = 0
			group by OrderNumber
		),
	MaxLog as
		(
			select e.OrderNumber, max(e.LogDateTime) LogDateTime, a.Attempts
			from ErrorLog e
			join Attempts a on a.OrderNumber = e.OrderNumber
			where datediff(dd, LogDateTime, getdate()) = 0
			group by e.OrderNumber, a.Attempts
		)
	select 
		ml.OrderNumber,
		ml.LogDateTime,
		el.ErrorMessage,
		ml.Attempts
	from MaxLog ml
	join ErrorLog el on ml.OrderNumber = el.OrderNumber and ml.LogDateTime = el.LogDateTime
```

