# internal.decrypt_lob_data

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  
**Function Type:** Scalar Function  
**Returns:** varbinary  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["internal.decrypt_lob_data"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @key_name | nvarchar | 510 | NO |
| @KEY | varbinary | 8000 | NO |
| @IV | varbinary | 8000 | NO |
| @lob | varbinary | -1 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql





CREATE FUNCTION [internal].[decrypt_lob_data]
( 
    @key_name nvarchar(255), 
    @KEY varbinary(8000),
    @IV varbinary(8000),
    @lob varbinary(max) 
)
RETURNS varbinary(max)
WITH EXECUTE AS 'AllSchemaOwner'
AS
BEGIN
    DECLARE @decrypted_binary varbinary(MAX)
    SET @decrypted_binary = (SELECT [internal].[decrypt_binarydata](@key_name, @KEY,@IV, @lob))
    RETURN @decrypted_binary
END
```
