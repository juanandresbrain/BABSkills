# dbo.fn_wbi_skins

**Database:** dw  
**Server:** papamart  
**Function Type:** Table-Valued Function  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.fn_wbi_skins"]
    dbo_tmp_wbi_rawdata_summary(["dbo.tmp_wbi_rawdata_summary"]) --> FUNC
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @abit_partyonly | bit | 1 | NO |

## Table Dependencies

| Referenced Table |
|---|
| dbo.tmp_wbi_rawdata_summary |

## Function Code

```sql
CREATE FUNCTION dbo.fn_wbi_skins
-- =============================================================================================================
-- Name: fn_wbi_skins
--
-- Description:	Used with nightly load process for Workbrain
--
-- Input: party only; if 0, then skins bought for parties are excluded	
--
-- Output: returns skins for each store, date, and 1/2 hour time increment 
--
-- Dependencies: Must be run from stored procedure xxxx
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Missey	9/7/2007		Created
--		Keith Missey	10/15/2007		Made "Skins" all upper case
--		Keith Missey	6/10/2009		remove dino and dolls from CASE statement
--		Keith Missey	8/26/2009		removed RZ from case statement and removed product division parameter
-- =============================================================================================================
    (
       @abit_partyonly bit = 0
    )
RETURNS @transoutput TABLE
    (
      SKDGRP_NAME varchar(40),
      INVTYP_ID smallint,
      RESDET_DATE char(10),
      RESDET_TIME char(8),
      RESDET_VOLUME money,
      INPUT_INVTYP_ID smallint,
      OLD_SKDGRP_NAME varchar(40),
      VOLTYPE_NAME varchar(200)
    )
AS BEGIN
  
            INSERT  @transoutput
                    SELECT  RTRIM(CAST(store_id AS char)) + '-BAB '
                            + CASE @abit_partyonly
                                WHEN 0 THEN 'SKINS'
                                WHEN 1 THEN 'PARTY SKINS'
                              END,
                            3,
                            CONVERT(varchar(10), actual_date, 101),
                            CONVERT(varchar(2), hour) + ':'
                            + CASE WHEN half_hour_id = 1 THEN '00:00'
                                   WHEN half_hour_id = 2 THEN '30:00'
                              END,
                            SUM(animalunits),
                            NULL,
                            NULL,
                            NULL
                    FROM    dbo.tmp_wbi_rawdata_summary
                    WHERE   partyflag = @abit_partyonly
                            AND animalunits > 0
                    GROUP BY store_id,
                            actual_date,
                            hour,
                            half_hour_id
    RETURN 
   END

dbo,fn_wbi_sales,SQL_TABLE_VALUED_FUNCTION,-- =============================================================================================================
-- Name: fn_wbi_sales
--
-- Description:	Used with nightly load process for Workbrain
--
-- Input: @abit_partyonly	if 0, then skins bought for parties are excluded
--
-- Output: returns sales for each store, date, and 1/2 hour time increment 
--
-- Dependencies: Must be run from stored procedure xxxx
--
-- Revision History
--		Name:			Date:			Comments:
--		Keith Missey	9/7/2007		Created
--		Keith Missey	6/10/2009		remove dino and dolls from CASE statement
--		Keith Missey	8/26/2009		removed RZ from case statement and removed product parameter 
-- =============================================================================================================
CREATE FUNCTION dbo.fn_wbi_sales
    (
      @abit_partyonly bit = 0
    )
RETURNS @transoutput TABLE
    (
      SKDGRP_NAME varchar(40),
      INVTYP_ID smallint,
      RESDET_DATE char(10),
      RESDET_TIME char(8),
      RESDET_VOLUME money,
      INPUT_INVTYP_ID smallint,
      OLD_SKDGRP_NAME varchar(40),
      VOLTYPE_NAME varchar(200)
    )
AS BEGIN
 
	
            INSERT  @transoutput
                    SELECT  RTRIM(CAST(store_id AS char)) + '-BAB '
                            + CASE @abit_partyonly
                                WHEN 0 THEN 'SALES'
                                WHEN 1 THEN 'PARTY SALES'
                              END,
                            3,
                            CONVERT(varchar(10), actual_date, 101),
                            CONVERT(varchar(2), hour) + ':'
                            + CASE WHEN half_hour_id = 1 THEN '00:00'
                                   WHEN half_hour_id = 2 THEN '30:00'
                              END,
                            SUM(gaapsales),
                            NULL,
                            NULL,
                            NULL
                    FROM    dbo.tmp_wbi_rawdata_summary
                    WHERE   partyflag = @abit_partyonly
                    GROUP BY store_id,
                            actual_date,
                            hour,
                            half_hour_id

    RETURN 
   END
```

