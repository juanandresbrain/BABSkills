# dbo.spCL_CleanupBadCharacters

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spCL_CleanupBadCharacters"]
    dbo_cust_liability(["dbo.cust_liability"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| dbo.cust_liability |

## Stored Procedure Code

```sql
--DROP PROC [dbo].[spCL_CleanupBadCharacters]
--GO

CREATE PROC [dbo].[spCL_CleanupBadCharacters]
-- =============================================================================================================
-- Name: [dbo].[spCL_CleanupBadCharacters]
--
-- Description:	Cleans up bad characters, such as commas in customer liability records that can cause issues 
--				when creating tab delimited files 
--
-- Output: N/A
--
-- Dependencies: 
--
-- Revision History
--		Name:			Date:			Comments:
--		Paul Beckman	12/15/2011		Created SP
--		Paul Beckman	02/18/2014		Updated to remove ' from first_name and last_name fields as the '
--										causes issues with redemptions from the web using Epicor DLLs
--		Paul Beckman	04/24/2014		Updated to remove & from first_name and last_name fields as the &
--										causes issues with redemptions from the web using Epicor DLLs
--
-- exec spCL_CleanupBadCharacters
-- =============================================================================================================
AS
SET NOCOUNT ON

--COMMA
UPDATE  auditworks.dbo.cust_liability
	SET     city = REPLACE(city, ',', '')
    WHERE   CHARINDEX(',', city) > 0

UPDATE  auditworks.dbo.cust_liability
    SET     address_1 = REPLACE(address_1, ',', '')
    WHERE   CHARINDEX(',', address_1) > 0

UPDATE  auditworks.dbo.cust_liability
    SET     address_2 = REPLACE(address_2, ',', '')
    WHERE   CHARINDEX(',', address_2) > 0

--SINGLE QUOTE
UPDATE  auditworks.dbo.cust_liability
	SET     first_name = REPLACE(first_name, '''', '')
    WHERE   CHARINDEX('''', first_name) > 0

UPDATE  auditworks.dbo.cust_liability
    SET     last_name = REPLACE(last_name, '''', '')
    WHERE   CHARINDEX('''', last_name) > 0

--AMPERSAND
UPDATE  auditworks.dbo.cust_liability
	SET     first_name = REPLACE(first_name, '&', '')
    WHERE   CHARINDEX('&', first_name) > 0

UPDATE  auditworks.dbo.cust_liability
    SET     last_name = REPLACE(last_name, '&', '')
    WHERE   CHARINDEX('&', last_name) > 0
```

