# dbo.spAuditWebCart_Populate_AWT_Log

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spAuditWebCart_Populate_AWT_Log"]
    dbo_WCAudit_AWT_Log(["dbo.WCAudit_AWT_Log"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.WCAudit_AWT_Log |

## Stored Procedure Code

```sql
--Papamart.dw

CREATE        PROC spAuditWebCart_Populate_AWT_Log
(
@BeginDate datetime
,@EndDate datetime
,@bFilterDates bit
)
AS

-- CLEAN UP =============================================================================================
IF (Object_ID('queries.dbo.WCAudit_AWT_Log') IS NOT NULL) DROP TABLE queries.dbo.WCAudit_AWT_Log

--EVERY AW Transaction (Unique by AW.Transaction Number which is equivelent to SJ.AWTransID)
CREATE TABLE queries.dbo.WCAudit_AWT_Log(
	iStoreID int
	,AWT_Date datetime
	,sBatchID varchar(50)
	,iAWTransID int
	,Original_OrderNumber varchar(50) 
	,mAmount money
	,iUnits int
	,bSentToAW bit
	)
create index ix_AWT_Log_Original_OrderNumber on queries.dbo.WCAudit_AWT_Log(Original_OrderNumber)

INSERT queries.dbo.WCAudit_AWT_Log(
	iStoreID 
	,AWT_Date 
	,sBatchID 
	,iAWTransID
	,Original_OrderNumber 
	,mAmount 
	,iUnits
	,bSentToAW
	)
SELECT a.iStoreID, a.AWT_Date, a.sBatchID, a.iAWTransID, a.Original_OrderNumber, a.mAmount, a.iUnits, a.bSentToAW
FROM 
OPENROWSET ( 'SQLOLEDB', 'BearWebDB' ; 'CommerceServer' ; 'A1g3r#1' , 
'SELECT lt.iStoreID
	,cast(convert(varchar(30),b.dTimeStamp,101) as datetime) as AWT_Date
	, b.sBatchID
	, iAWTransID
	, sOrderNumber as Original_OrderNumber
	, mAmount
	, iUnits
	, bSentToAW
	--, sDevComments, sCreatedBy 
FROM WebCart_Commerce.dbo.NSBTranslate_batch b with(nolock)
	join WebCart_Commerce.dbo.NSBTranslate_LogTrans lt with(nolock) 
	on b.sBatchID=lt.sBatchID
--where bSentToAW=1
 	--and b.dTimeStamp between ''12/8/05'' and ''12/9/05''
	--and iStoreID = 13
	--and len(sOrderNumber) < 20 --poor technique but it eliminates GC_K while it is only one on CC WS
	--and len(sOrderNumber) > 0 --poor technique but it eliminates GC_K while it is only one on CC WS
order by iStoreID
	, cast(convert(varchar(30),b.dTimeStamp,101) as datetime)
	, b.sBatchID
	, iAWTransID
	, sOrderNumber
'
) a

--select 'AWT Log INSERT' as DataSet, @@Rowcount as rowsAdded, count(*) as Level1_AWT_Log_Total from queries.dbo.WCAudit_AWT_Log


--============================================================================================
--REMOVE UNWANTED RECORDS
if(@bFilterDates = 1) begin
	delete from queries.dbo.WCAudit_AWT_Log 
	where (AWT_Date >= Dateadd(day,1,@EndDate)
		or AWT_Date < @BeginDate)
		--and len(sOrderNumber) < 20 --poor technique but it eliminates GC_K while it is only one on CC WS
		--and len(sOrderNumber) > 0 --poor technique but it eliminates GC_K while it is only one on CC WS
end

-- SELECT * FROM queries.dbo.WCAudit_AWT_Log
```

