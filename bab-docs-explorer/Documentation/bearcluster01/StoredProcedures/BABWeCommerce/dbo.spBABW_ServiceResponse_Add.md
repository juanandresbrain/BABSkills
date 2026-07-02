# dbo.spBABW_ServiceResponse_Add

**Database:** BABWeCommerce  
**Server:** bearcluster01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spBABW_ServiceResponse_Add"]
    dbo_babw_serviceResponse(["dbo.babw_serviceResponse"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.babw_serviceResponse |

## Stored Procedure Code

```sql
-- =============================================
-- Author:		Atkinson, Brad
-- Create date: 5/2/2011
-- Description:	The babw.services project uses this procedure to store
-- the request objects that are being used. The purpose of this
-- process is to assist with debugging.
-- =============================================
CREATE PROCEDURE [dbo].[spBABW_ServiceResponse_Add]
	@ServiceName varchar(50),
	@Value xml
AS
BEGIN
	insert into babw_serviceResponse (ServiceName, Value, CreatedDate) Values (@ServiceName, @Value, GETDATE());
	
	SELECT @@IDENTITY;
END
```

