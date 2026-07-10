# dbo.vwPayroll_Week_Facts

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwPayroll_Week_Facts"]
    dbo_payroll_week_facts(["dbo.payroll_week_facts"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.payroll_week_facts |

## View Code

```sql
CREATE   VIEW dbo.vwPayroll_Week_Facts
AS

SELECT *
FROM payroll.dbo.payroll_week_facts






dbo,vwDW_SFSGstsWIP,/***********************************************************************************************
Object Name:	[vwDW_SFSGsts]

Author			Date			Comment
Funmi Agbebi	12/7/2009		Added Repeat_SFSGstID field. 
Funmi Agbebi	11/4/2009		Added VALID_CRM_MBRSHP_DT field. Included case statements to nullify all CRM_MBRSHP_DT earlier than 6/1/2008
Funmi Agbebi	3/6/2009		original creation

Purpose:		View used for reporting.  Primarily used by the used the 'SFS Guest Facts' and 
				'SFS Guest With Email Facts' measure groups of the SSAS papa mart cube to identify
				 new vs repeat sfs guests and sfs gsts with email.
				Joins transaction_detail_facts to vwCRM_TRN_SUM_FACT, vwDW_store and date_dim
**********************************************************************************************/
CREATE VIEW [dbo].[vwDW_SFSGstsWIP]
AS
/***********************************
vwDW_Transactions_original
************************************/
SELECT top 30 temp.*

	FROM
	(
		SELECT tdf.date_key
			,trans_date_dim.fiscal_year
			,trans_date_dim.fiscal_quarter
			,trans_date_dim.fiscal_period
			,trans_date_dim.fiscal_week
			,tdf.store_key
			,tdf.transaction_id
			,1 as all_trans_cnt  -- (FA 7/21/2009)
			,tdf.sfs_trans_cnt   -- (FA 7/21/2009)
			,tdf.SFSGstID
			,tdf.CRM_MBRSHP_DT
			,tdf.VALID_CRM_MBRSHP_DT
			,tdf.SFS_GstVisitType
			,tdf.New_SFSGstID
			,tdf.Repeat_SFSGstID
			,tdf.SFSValidEmail
			,tdf.SFSValidEmail_GstID 
			,tdf.NewSFSValidEmail_GstID
		FROM
			(SELECT tdf1.date_key
					,tdf1.store_key
					,tdf1.transaction_id
					,max(cts.sfs_trans_cnt) sfs_trans_cnt  -- (FA 7/21/2009)
					,cts.SFSGstID
					,cts.CRM_MBRSHP_DT
					,cts.VALID_CRM_MBRSHP_DT
					,cts.SFS_GstVisitType
					,cts.New_SFSGstID
					,cts.Repeat_SFSGstID
					,cts.SFSValidEmail
					,cts.SFSValidEmail_GstID 
					,cts.NewSFSValidEmail_GstID
			FROM transaction_detail_facts tdf1 WITH (NOLOCK)
			--SMF BEGIN 20080118
			left join (select top 100 Percent [TDF_TRN_ID] AS transaction_id
							, str_id AS store_key
							, [DT_ID] AS date_key
							, 1 AS sfs_trans_cnt   -- (FA 7/21/2009)
							,CLNSD_GST_ID as SFSGstID
							,CRM_MBRSHP_DT
							,VALID_CRM_MBRSHP_DT
							,SFS_GstVisitType
							,New_SFSGstID
							,Repeat_SFSGstID
							,SFSValidEmail
							,SFSValidEmail_GstID 
							,NewSFSValidEmail_GstID
							from dw.dbo.[vwDW_CRM_TRN_SUM_FACT] WITH (NOLOCK)
							group by tdf_trn_id
								, str_id
								, dt_id
								,CLNSD_GST_ID
								,CRM_MBRSHP_DT
								,VALID_CRM_MBRSHP_DT
								,SFS_GstVisitType
								,New_SFSGstID
								,Repeat_SFSGstID
								,SFSValidEmail 
								,SFSValidEmail_GstID 
								,NewSFSValidEmail_GstID
								order by dt_id) cts
				on cts.transaction_id = tdf1.transaction_id
					and cts.store_key = tdf1.store_key
					and cts.date_key  = tdf1.date_Key
			--SMF END 20080118
			WHERE	tdf1.transaction_line_seq > 0
		AND tdf1.date_Key <= (SELECT date_key FROM date_dim WHERE actual_date = DATEADD(d, -1, CAST(CONVERT(varchar(10),GETDATE(),101) AS smalldatetime)))
			GROUP BY tdf1.date_key
					,tdf1.store_key
					,tdf1.transaction_id
					,cts.SFSGstID
					,cts.CRM_MBRSHP_DT
					,cts.VALID_CRM_MBRSHP_DT
					,cts.SFS_GstVisitType
					,cts.New_SFSGstID
					,cts.Repeat_SFSGstID
					,cts.SFSValidEmail
					,cts.SFSValidEmail_GstID 
					,cts.NewSFSValidEmail_GstID
			) tdf

		INNER JOIN vwDW_Store s  WITH (NOLOCK) ON s.store_key = tdf.store_key
		INNER JOIN date_dim trans_date_dim  WITH (NOLOCK) ON trans_date_dim.date_key = tdf.date_key
	) temp
  
 WHERE   ( date_key > 2555) -- ( date_key > 3280 and date_key < 4621 ) --FY 2007 - FP 07 2009
```

