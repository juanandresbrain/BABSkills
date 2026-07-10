# dbo.spEmailUltiProToActiveDirectoryOUupdatesStaged

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spEmailUltiProToActiveDirectoryOUupdatesStaged"]
    dbo_sp_send_dbmail(["dbo.sp_send_dbmail"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.sp_send_dbmail |

## Stored Procedure Code

```sql
CREATE proc [dbo].[spEmailUltiProToActiveDirectoryOUupdatesStaged] 
	@EmployeeID nvarchar(7),
	@EecLocation nvarchar(50),
	@EepNameFirst nvarchar(50),
	@EepNameLast nvarchar(50),
	@LocDesc nvarchar(50),
	@JbcJobCode nvarchar(50),
	@EecOrgLvl1Code nvarchar(50),
	@samaccountname nvarchar(50),
	@EmployeeADGroup nvarchar(50),
	@AD_Department nvarchar(50),
	@objectToMove nvarchar(255),
	@newAdsPath nvarchar(255),
	@displayName nvarchar(50)

--========================================================================================================================
--	2019-05-17	Dan Tweedie	- Created proc 
--								Runs with SSIS dataflow, accepting parameters to send email per employee staged for AD
--								exec spEmailUltiProToActiveDirectoryUpdatesStaged 
--									
--========================================================================================================================

as

set nocount on

declare 
	@provisionText varchar(20),
	@subj varchar(52),
	@recip varchar(1000),
	@cc varchar(100),
	@body nvarchar(max)


select @Subj = 'UltiPro to Active Directory Employee OU Update'
	--select @recip = 'ianw@buildabear.com'
	select @recip = 'ianw@buildabear.com;dant@buildabear.com;'
	select @ProvisionText = 'OU update'


select @body = 
'<font face =arial size = 2><B>UltiPro to Active Directory Employee department/OU change</B><br>' +
'The following employee OU was updated. <br> ' +
'</font>' +
	'<table border="1">' +
		'<tr><th><font face =arial size = 2>ProvisioningEvent</font></th>' +
			'<th><font face =arial size = 2>EmployeeID</font></th>' +
			'<th><font face =arial size = 2>Location</font></th>' +
			'<th><font face =arial size = 2>First Name</font></th>' +
			'<th><font face =arial size = 2>Last Name</font></th>' +
			'<th><font face =arial size = 2>Job Code</font></th>' +
			'<th><font face =arial size = 2>Previous OU container</font></th>' +
			'<th><font face =arial size = 2>New OU container</font></th>' +
			'<th><font face =arial size = 2>Display Name</font></th>' +
'<font face =arial size = 2>' +
    CAST ( ( SELECT td = @provisionText,'',
                    td = @EmployeeID, '',
					td = @EecLocation, '',
					td=  @EepNameFirst, '',
					td=  @EepNameLast, '',
					td=  @JbcJobCode,'',
                    td = @EmployeeADGroup, '',
                    td = @AD_Department, '',
					td = @displayName, ''
              FOR XML PATH('tr'), TYPE 
    ) AS NVARCHAR(MAX) ) +
    '</font></table></font></p></p>
    <br><br>' +
    '<br>
    <font face =arial size = 1><B>This report was run from SSIS as part of the UltiPro to Active Directory ETL. </B></font>
    <br>
    <br>
<font face =arial size = 1><i>The information in this message may be privileged, “confidential” and protected from disclosure and/or intended only for the addressee(s) named above.  If the reader of this message is not the intended recipient, or an employee or agent responsible for delivering this message to the intended recipient, you are hereby notified that any dissemination, distribution or copying of the communication is strictly prohibited.  If you have received this communication in error, please notify us immediately by replying to the message and deleting it from your computer.  Thank you beary much.</i></font>'



		exec msdb.dbo.sp_send_dbmail
			@profile_name = 'BIAdmin',
			@recipients = @recip,
			@body = @body,
			@subject = @subj,
			@body_format = 'HTML'


dbo,spGuestLoad_Pull_Mobile_Txt,-- =============================================================================================================
-- Name: spGuestLoad_Pull_Mobile_Txt
--
-- Description:	
--		pull raw Mobile data for crm guests
--
-- Input:
--		@etl_log_id			int	
--			Current load to process
--
-- Output: 
--		data will be loaded into dw.dbo.GuestLoad_Pull_Mobile_Txt
--
-- Dependencies: 
--
-- EXAMPLE:
--		exec dw.dbo.GuestLoad_Pull_Mobile_Txt -1
--
-- Revision History
--		Name:			Date:			Comments:
--		Dave Rice		7/19/2010		created
-- =============================================================================================================
CREATE PROCEDURE [dbo].[spGuestLoad_Pull_Mobile_Txt](@etl_log_id int)
AS
BEGIN
-- SET NOCOUNT ON added to prevent extra result sets from
-- interfering with SELECT statements.
SET NOCOUNT ON;

----exec dbo.GuestLoad_Pull_Mobile_Txt 14224
--select top 1 etl_log_id from dwstaging.dbo.load_rec_id_cntrl with (nolock)
--declare @etl_log_id int
--set @etl_log_id = 17552

truncate table GuestLoad_Pull_Mobile_Txt

insert into GuestLoad_Pull_Mobile_Txt (
	stg_id, stg_dta_set_cd, updt_src_sys_cd, mobile_txt_id, mobile_txt_nbr,
	cntry_abbrv, mobile_txt_stat_cd, src_updt_dt
)
-- crm
SELECT
	lric.stg_id,
	lric.stg_dta_set_cd,
	lric.stg_dta_set_cd as opt_in_src_sys_cd,
	IsNull(mtd.mobile_txt_id, -1) as mobile_txt_id,

	rgd.mobile_txt_nbr as mobile_txt_nbr,

	case when rad.DRVD_CNTRY_ABBRV = 'US' then 'USA'
		when rad.DRVD_CNTRY_ABBRV = 'CA' then 'CAN'
		when rad.DRVD_CNTRY_ABBRV = 'GB' then 'GBR'
		when rad.DRVD_CNTRY_ABBRV = 'FR' then 'FRA'
		else 'USA'
	end cntry_abbrv,

	rgd.drvd_mobile_txt_stat_cd mobile_txt_stat_cd,
	s.src_rec_crte_dt as src_updt_dt
FROM dwstaging.dbo.load_rec_id_cntrl lric with (nolock)
	join dwstaging.dbo.crm_stg s with (nolock)
	ON s.crm_stg_id = lric.stg_id
	join dw.dbo.raw_gst_dim rgd with (nolock)
	ON rgd.raw_gst_id = lric.raw_gst_id
	join dw.dbo.raw_addr_dim rad with (nolock)
	ON rad.raw_addr_id = lric.raw_addr_id
	left join dw.dbo.mobile_txt_dim mtd with (nolock)
	ON mtd.mobile_txt_nbr = rgd.mobile_txt_nbr
where 1=1
	AND lric.stg_dta_set_cd = 'CRM'
	AND lric.etl_log_id = @etl_log_id
	and rgd.mobile_txt_nbr is not null
END
```

