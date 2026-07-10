# Job: GiftCard - Missing Upload Files

**Enabled:** Yes  
**Server:** papamart  
**Description:** No description available.  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["GiftCard - Missing Upload Files"]
    JOB --> S1["Step 1: step1 [TSQL]"]
```

## Steps

### Step 1: step1
**Subsystem:** TSQL  

```sql
exec spGiftCardMissingUploadFiles,dw
JMC_TO_DW_KILL_LONG_RUNNING_INSERT_MERGE,No description available.,1,find spid for jmc running longer than x, kill it,TSQL,declare @spid int

select @spid= r.session_id
FROM sys.dm_exec_requests AS r
     CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) AS st
     CROSS APPLY sys.dm_exec_query_plan(r.plan_handle) AS qp
WHERE 
	(
		st.TEXT like '%insert%jmc%'
		or
		st.TEXT like '%merge%jmc%'
	)
and datediff(mi,r.start_time, getdate()) >=30

declare @SQL varchar(100)
select @SQL = 'kill ' + cast(@spid as varchar)

exec (@SQL)
```

