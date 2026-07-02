# dbo.spMerchandisingUpdateKodiakBearDatatblSourceDest_CN

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spMerchandisingUpdateKodiakBearDatatblSourceDest_CN"]
    dbo_tblSourceDest_CN(["dbo.tblSourceDest_CN"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.tblSourceDest_CN |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Keith Lee
-- Create date: 7/7/2016
-- Description:	A temporary proc that updates kodiak.BearData.dbo.tblSourceDest_CN until Development gets rectype 13 working
-- =============================================
CREATE PROCEDURE spMerchandisingUpdateKodiakBearDatatblSourceDest_CN 
AS
BEGIN

	SET NOCOUNT ON;


declare @dow varchar(10)

set @dow = (SELECT upper(DATENAME(dw,GETDATE())))

update kodiak.BearData.dbo.tblSourceDest_CN
set iShipDay = (select case when @dow = 'WEDNESDAY' 
						then 3
					   when @dow = 'MONDAY'
					   then 1
					   end)
where iDestID = 3002



END
```

