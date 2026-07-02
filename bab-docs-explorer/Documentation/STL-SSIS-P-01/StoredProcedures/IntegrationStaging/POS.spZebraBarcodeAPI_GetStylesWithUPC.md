# POS.spZebraBarcodeAPI_GetStylesWithUPC

**Database:** IntegrationStaging  
**Server:** STL-SSIS-P-01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["POS.spZebraBarcodeAPI_GetStylesWithUPC"]
    dbo_ZebraLabelProductInfo(["dbo.ZebraLabelProductInfo"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.ZebraLabelProductInfo |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Brandon Hickey
-- Create date: 04/10/2023
-- Description:	Returns style information for Zebra Barcode Application
-- =============================================
CREATE PROCEDURE [POS].[spZebraBarcodeAPI_GetStylesWithUPC] 
	
	@JurisdictionID int,
	@styleCode nvarchar(20)
WITH EXECUTE AS 'dbo'
AS
BEGIN
	
	SET NOCOUNT ON;

    SELECT upc_number, short_desc, cost, local_desc
    FROM ZebraLabelProductInfo                
    where jurisdiction_id = @JurisdictionID
		and style_code = @styleCode

END
```

