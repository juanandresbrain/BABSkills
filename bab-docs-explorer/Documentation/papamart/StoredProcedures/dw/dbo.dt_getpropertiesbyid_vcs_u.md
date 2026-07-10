# dbo.dt_getpropertiesbyid_vcs_u

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.dt_getpropertiesbyid_vcs_u"]
    dbo_dt_getpropertiesbyid_vcs(["dbo.dt_getpropertiesbyid_vcs"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.dt_getpropertiesbyid_vcs |

## Stored Procedure Code

```sql
create procedure dbo.dt_getpropertiesbyid_vcs_u
    @id       int,
    @property varchar(64),
    @value    nvarchar(255) = NULL OUT

as

    -- This procedure should no longer be called;  dt_getpropertiesbyid_vcsshould be called instead.
	-- Calls are forwarded to dt_getpropertiesbyid_vcs to maintain backward compatibility.
	set nocount on
    exec dbo.dt_getpropertiesbyid_vcs
		@id,
		@property,
		@value output


dbo,spGuestLoad_Remove_Previous_Run,-- =============================================================================================================
-- Name: spGuestLoad_Remove_Previous_Run
--
-- Description:	
--		Removes the previous unsuccessful load.  Loads can get hung up for many reasons, but rather than try to piece the
--		old state back together, it's better to clean things out, fix the problem and then reload.  it's one thing to remove
--		inserted rows, but to try to undo updates would have been prone to error.  You can ask, what is the harm in just reloading
--		the data?  As long as we aren't totally screwed up, meaning, we ended up associating the wrong folks to addresses, or things
--		got crisscrossed in a horrendous fashion, we should be ok.  Worst case, remove the tkf records or reload the guests.  we
--		should just end up with unused cleansed addresses.
--
--		so, just remove staging data and clear out the etl_prcs_cntrl table so that we can take another stab at it.
--
-- Input:
--
-- Output: 
--
-- Dependencies: 
--
-- EXAMPLE:
--		exec dw.dbo.spGuestLoad_Remove_Previous_Run 
--
-- Revision History
--		Name:			Date:			Comments:
--		Dave Rice		7/19/2010		created
-- =============================================================================================================
CREATE PROCEDURE [dbo].[spGuestLoad_Remove_Previous_Run]
AS
BEGIN

-- SET NOCOUNT ON added to prevent extra result sets from
-- interfering with SELECT statements.
SET NOCOUNT ON;

-- exec spGuestLoad_Remove_Previous_Run

-- ******
declare @etl_log_id int
set @etl_log_id = (select top 1 etl_log_id from dwstaging.dbo.etl_prcs_cntrl where etl_prcs_nm in ('ksk_stg_insert','CRM_STG_Insert') and stat_cd is null order by etl_log_id desc)

if isnull(@etl_log_id, -999) > 0
begin
	/*
	????
	select * from GST_SUM_FACT
	truncate table GST_SUM_FACT
	*/

	begin tran

	--declare @bad_address_count int
	--set @bad_address_count = (select count(*) from dw.dbo.raw_addr_dim where etl_log_id = @etl_log_id and clnsd_addr_id is null)

	--delete from dw.dbo.raw_addr_dim
	--
	--select count(*) From dw.dbo.raw_addr_dim where clnsd_Addr_id is null
	--select * from dw.dbo.raw_addr_dim where clnsd_Addr_id is null
	delete from dw.dbo.raw_addr_dim where clnsd_addr_id is null

	-- only remove clsnd_addr_dim if taking out an individual batch???
	-- had to say, hopefully the raw and clnsd addr stuff is solid, if there is doubt, then yes, pop them,
	-- but things will go far faster if we don't delete them

	--if @bad_address_count > 0
	--begin
	--	delete from dw.dbo.clnsd_addr_dim where clnsd_addr_id > -1 and etl_log_id = @etl_log_id
	--end

	--delete from dw.dbo.clnsd_addr_dim_hist where etl_log_id = @etl_log_id
	--delete from dw.dbo.clnsd_addr_dim_rjct where etl_log_id = @etl_log_id
	--
	--delete dw.[dbo].ADDR_SUM_FACT
	--from dw.[dbo].ADDR_SUM_FACT asf
	--	left join dw.dbo.clnsd_addr_dim cad
	--	on cad.clnsd_addr_id = asf.clnsd_addr_id
	--where cad.clnsd_addr_id is null
	--
	--delete from dw.dbo.clnsd_gst_dim where clnsd_gst_id >= 0 and etl_log_id = @etl_log_id
	--delete from dw.dbo.clnsd_gst_dim_hist where etl_log_id = @etl_log_id
	--delete from dw.dbo.clnsd_gst_dim_rjct where etl_log_id = @etl_log_id
	----delete from dw.dbo.clnsd_gst_email_addr_brdg where etl_log_id = @etl_log_id
	--
	----delete from dw.dbo.CURR_CLNSD_GST_DIM where etl_log_id = @etl_log_id
	--
	--delete from dw.dbo.EMAIL_ADDR_DIM where email_addr_id > -1 and etl_log_id = @etl_log_id
	--delete from dw.dbo.EMAIL_ADDR_DIM_HIST where etl_log_id = @etl_log_id
	--delete from dw.dbo.EMAIL_ADDR_DIM_RJCT where etl_log_id = @etl_log_id
	--delete from dw.dbo.EMAIL_ADDR_PRSNLZTN_ATTR_DIM where etl_log_id = @etl_log_id
	--delete from dw.dbo.EMAIL_ADDR_STAT_FACT where etl_log_id = @etl_log_id
	--
	---- only remove clsnd_addr_dim if taking out an individual batch???
	---- had to say, hopefully the raw and clnsd addr stuff is solid, if there is doubt, then yes, pop them,
	---- but things will go far faster if we don't delete them
	--if @bad_address_count > 0
	--begin
	--	delete from dw.dbo.raw_addr_dim where raw_addr_id > -1 and etl_log_id = @etl_log_id
	--end
	--
	--delete from dw.dbo.raw_addr_dim_rjct where etl_log_id = @etl_log_id
	--
	--delete from dw.dbo.raw_gst_dim where raw_gst_id > -1 and etl_log_id = @etl_log_id
	--delete from dw.dbo.raw_gst_dim_rjct where etl_log_id = @etl_log_id
	--
	--delete from dw.dbo.raw_rcpnt_dim where raw_rcpnt_id > -1 and etl_log_id = @etl_log_id
	--delete from dw.dbo.raw_rcpnt_dim_rjct where etl_log_id = @etl_log_id
	--
	--delete from dw.dbo.trn_ksk_fact where etl_log_id = @etl_log_id
	--delete from dw.dbo.TKF_CLNSD_GST_BRDG where etl_log_id = @etl_log_id
	--
	-- ******
	delete from dwstaging.dbo.crm_stg where etl_log_id = @etl_log_id
	delete from dwstaging.dbo.crm_stg_rjct where etl_log_id = @etl_log_id

	delete from dwstaging.dbo.ksk_regis_stg where etl_log_id = @etl_log_id
	delete from dwstaging.dbo.ksk_regis_stg_rjct where etl_log_id = @etl_log_id

	truncate table dwstaging.dbo.load_rec_id_cntrl
	truncate table dwstaging.dbo.load_rec_id_cntrl_tmp
	--delete from dwstaging.dbo.load_rec_id_cntrl where etl_log_id = @etl_log_id
	--delete from dwstaging.dbo.load_rec_id_cntrl_tmp where etl_log_id = @etl_log_id

	--delete from dwstaging.dbo.vldtn_prcs  -- do not delete this data!!!!
	--delete from dwstaging.dbo.vldtn_prcs_instnc where etl_log_id = @etl_log_id
	--delete from dwstaging.dbo.vldtn_prcs_instnc_dtl_miss_key where etl_log_id = @etl_log_id
	--delete from dwstaging.dbo.vldtn_prcs_instnc_dtl_prcs_spfc where etl_log_id = @etl_log_id
	--delete from dwstaging.dbo.vldtn_prcs_instnc_dtl_rec_cnt where etl_log_id = @etl_log_id
	--delete from dwstaging.dbo.vldtn_prcs_instnc_dtl_ref_intgrty where etl_log_id = @etl_log_id
	--delete from dwstaging.dbo.vldtn_prcs_instnc_dtl_trn_sum where etl_log_id = @etl_log_id

	-- these must be kept in sync
	delete from email_addr_dim
	from email_addr_dim ead
		left join EMAIL_ADDR_PRFRNCE_DIM eapd
		on eapd.email_addr_id = ead.email_addr_id
	where eapd.email_addr_id is null

	--delete from QASCleansing.dbo.matches_hist where etl_log_id = @etl_log_id

	delete from dwstaging.dbo.etl_prcs_cntrl where etl_log_id = @etl_log_id and etl_prcs_nm in ('ksk_stg_insert','CRM_STG_Insert') 

	commit tran
end

END
```

