# dbo.sp_MSdistribution_cleanup

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.sp_MSdistribution_cleanup"]
    dbo_sp_MSdistribution_delete(["dbo.sp_MSdistribution_delete"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_MSdistribution_delete |

## Stored Procedure Code

```sql
CREATE PROCEDURE sp_MSdistribution_cleanup
    @min_distretention int = 0,
    @max_distretention int = 24,
    @no_applock bit = 0
as
	SET DEADLOCK_PRIORITY LOW 
    declare @retcode int
    declare @agent_name nvarchar(255)
    declare @agent_type nvarchar(100)
    declare @message nvarchar(255)
	declare @cutoff_time datetime

     -- Check for invalid parameter values 
    if @min_distretention < 0 or @max_distretention < 0
    begin
        RAISERROR(14106, 16, -1)
        return (1)
    end

    declare @lockresource nvarchar(255),
            @acquiredapplicationlock bit

    -- 1) Acquire no-sync subscription setup lock up-front to prevent
    -- the cleanup task from interfering any no-sync subscription setup 
    -- task that may be in progress.
    
    -- WARNING: Before calling sp_MSdistribution_cleanup from another
    -- stored procedure or replication agent with @no_applock = 0,
    -- consider that the application lock acquired by 
    -- sp_MSdistribution_cleanup is owned by the current session and it may
    -- not be released properly by the time sp_MSdistribution_cleanup exits
    -- if the batch is aborted. It is ok for the distribution cleanup 
    -- job to call this procedure directly because SQLServerAgent makes a new
    -- connection every time a job runs.
    
    select @acquiredapplicationlock = 0

    if @no_applock = 0
    begin
        select @lockresource = db_name() + N'_nosync'
        exec @retcode = sys.sp_getapplock @Resource = @lockresource,
                                          @LockMode = 'Shared',
                                          @LockOwner = 'Session',
                                          @LockTimeout = -1,
                                          @DbPrincipal = 'db_owner' 
        -- No timeout! No-sync setup process should never take long and the 
        -- Transaction-owned lock acquired by the no-sync setup process has 
        -- to be released in the event of a catastrophic failure.  

        if @retcode < 0 or @@error <> 0 begin select @retcode = 1 goto FAIL end
        select @retcode = 0, @acquiredapplicationlock = 1
    end

	-- Update statistics on tables with norecompute flag
    -- to both update the statistics periodically and 
    -- to ensure that they are not updated too frequently
    -- since this slows performance.
    --
    -- Update statistics can only be performed when not in
    -- a transaction so predicate by transaction level check
    -- to avoid error.
    --
    if @@trancount = 0
    begin
        UPDATE STATISTICS MSrepl_commands WITH NORECOMPUTE
        UPDATE STATISTICS MSrepl_transactions WITH NORECOMPUTE
    end

	-- The call to sp_MSsubscription_cleanup has been moved to sp_expired_subscription_cleanup 
	-- that runs once every 24 hours by default (Expired subscription cleanup job).  We would still 
	-- need to calculate the cutoff_time here since this will be used to cleanup expired entries 
	-- from MSRepl_Commands and MSRepl_Transactions tables.
    select @cutoff_time = dateadd(hour, -@max_distretention, getdate())

    -- Remove transactions and commands
    exec @retcode = dbo.sp_MSdistribution_delete @min_distretention, 
		-- used to cleanup trans for anon publications.
		@cutoff_time
    if @retcode <> 0
        goto FAIL

    -- Update statistics on cleaned tables with norecompute flag
    -- to both update the statistics periodically and 
    -- to ensure that they are not updated too frequently
    -- since this slows performance.
    --
    -- Update statistics can only be performed when not in
    -- a transaction so predicate by transaction level check
    -- to avoid error.
    --
    if @@trancount = 0
    begin
        UPDATE STATISTICS MSrepl_commands WITH NORECOMPUTE
        UPDATE STATISTICS MSrepl_transactions WITH NORECOMPUTE
    end

    if @acquiredapplicationlock = 1
    begin
        exec sys.sp_releaseapplock @Resource = @lockresource,
                                   @LockOwner = 'Session',
                                   @DbPrincipal = N'db_owner'
    end
    select @acquiredapplicationlock = 0
    return(0)

FAIL:
    if @acquiredapplicationlock = 1
    begin
        exec sys.sp_releaseapplock @Resource = @lockresource,
                                   @LockOwner = 'Session',
                                   @DbPrincipal = N'db_owner'
    end
    -- Raise the Agent Failure error
    set @agent_type  = formatmessage(20543)
    SELECT @agent_name = db_name() + @agent_type
    set @message  = formatmessage(20552)
    exec sys.sp_MSrepl_raiserror @agent_type, @agent_name, 5, @message
    return (1)
```

