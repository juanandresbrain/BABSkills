# dbo.syspublications

**Database:** CRDM_Distributor  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.syspublications"]
    IHpublications(["IHpublications"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| IHpublications |

## View Code

```sql
create view syspublications (description, name, pubid, repl_freq, status, sync_method, snapshot_jobid, 
        			independent_agent, immediate_sync, enabled_for_internet, allow_push, allow_pull, allow_anonymous, immediate_sync_ready, 
				allow_sync_tran, autogen_sync_procs, retention, allow_queued_tran, snapshot_in_defaultfolder, alt_snapshot_folder, 
				pre_snapshot_script, post_snapshot_script, compress_snapshot, ftp_address, ftp_port, ftp_subdirectory, ftp_login, 
				ftp_password, allow_dts, allow_subscription_copy, centralized_conflicts, conflict_retention, conflict_policy, queue_type, 
				ad_guidname, backward_comp_level, allow_initialize_from_backup, min_autonosync_lsn, replicate_ddl, options, originator_id) AS 
		   SELECT ihpub.description, 
				ihpub.name, 
				ihpub.pubid, 
				ihpub.repl_freq, 
				ihpub.status, 
				ihpub.sync_method, 
				ihpub.snapshot_jobid, 
				ihpub.independent_agent, 
				ihpub.immediate_sync, 
				ihpub.enabled_for_internet, 
				ihpub.allow_push, 
				ihpub.allow_pull, 
				ihpub.allow_anonymous, 
				ihpub.immediate_sync_ready, 
				ihpub.allow_sync_tran, 
				ihpub.autogen_sync_procs, 
				ihpub.retention, 
				ihpub.allow_queued_tran, 
				ihpub.snapshot_in_defaultfolder, 
				ihpub.alt_snapshot_folder, 
				ihpub.pre_snapshot_script, 
				ihpub.post_snapshot_script, 
				ihpub.compress_snapshot, 
				ihpub.ftp_address, 
				ihpub.ftp_port, 
				ihpub.ftp_subdirectory, 
				ihpub.ftp_login, 
				ihpub.ftp_password, 
				ihpub.allow_dts, 
				ihpub.allow_subscription_copy, 
				ihpub.centralized_conflicts, 
				ihpub.conflict_retention, 
				ihpub.conflict_policy, 
				ihpub.queue_type,
				ihpub.ad_guidname, 
				ihpub.backward_comp_level, 
				ihpub.allow_initialize_from_backup, 
				ihpub.min_autonosync_lsn, 
				ihpub.replicate_ddl,
				ihpub.options,
				ihpub.originator_id
		 FROM   IHpublications ihpub
```

