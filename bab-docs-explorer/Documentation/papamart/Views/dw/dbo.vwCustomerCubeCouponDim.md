# dbo.vwCustomerCubeCouponDim

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    VIEW["dbo.vwCustomerCubeCouponDim"]
    coupon_dim(["coupon_dim"]) --> VIEW
```

## Table Dependencies

| Referenced Table |
|---|
| coupon_dim |

## View Code

```sql
CREATE view [dbo].[vwCustomerCubeCouponDim]
as

with 
CouponData as
	(
		select 
			c.coupon_key as CouponKey,
			isnull(c.coupon_desc,'n/a') as CouponDescription,
			isnull(c.event_name, 'n/a') as CouponEvent,
			isnull(c.category, 'n/a') as CouponCategory
		from coupon_dim c with (nolock)
	)
select 
	CouponKey,
	CouponDescription,
	CouponEvent,
	CouponCategory,
	dense_rank() over (order by CouponEvent) as CouponEventID,
	dense_rank() over (order by CouponEvent,CouponCategory) as CouponCategoryID
from CouponData



dbo,vwEMAIL_ADDR_DIM,/***********************************************************************************************
Object Name:	dbo.vwEMAIL_ADDR_DIM
Author:			Funmi Agbebi
Created Date:	3/6/2009
Purpose:		View used for reporting.  Primarily used by BO universes to 
				conveniently access all relevant pieces of EMAIL data and its status.
				Sourced from Kiosk and CRM .
				Joins EMAIL_ADDR_DIM to[EMAIL_ADDR_PRSNLZTN_ATTR_DIM] -- EMAIL_ADDR_STAT_FACT

**********************************************************************************************/

CREATE VIEW [dbo].[vwEMAIL_ADDR_DIM]
AS
SELECT e.[EMAIL_ADDR_ID]
      ,[EMAIL_ADDR_TXT]
      ,[OPT_IN_SRC_SYS_CD]
      ,[EMAIL_STAT_CD]
      ,[GLBL_OPT_IN_DT]
      ,[PERM_BOUNC_DT]
      ,[SRC_REC_UPDT_DT]
	  ,p.EMAIL_PRSNLZTN_ATTR_SEQ_NBR
      ,p.[EMAIL_FRST_NM]
      ,p.[EMAIL_LAST_NM]
      ,p.[EMAIL_BRTH_DT]
      ,p.[CNTRY_ABBRV]
      ,p.[INS_DT] pznInsDt
      ,p.[UPDT_DT] pzUpdtDt
      ,p.[BEG_EFF_DT] pzBegEffDt
      ,p.[END_EFF_DT] pzEndEffDt
      ,e.[INS_DT] vwEmailAddrDimInsDt
      ,e.[UPDT_DT] vwEmailUpdtDt
  FROM [dbo].[EMAIL_ADDR_DIM] e WITH (NOLOCK) left join 
	   [dbo].[EMAIL_ADDR_PRSNLZTN_ATTR_DIM] p  WITH (NOLOCK) ON
		e.[EMAIL_ADDR_ID] = p.[EMAIL_ADDR_ID]
```

