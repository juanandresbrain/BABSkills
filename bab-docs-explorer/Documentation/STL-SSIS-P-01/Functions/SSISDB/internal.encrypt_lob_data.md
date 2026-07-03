# internal.encrypt_lob_data

**Database:** SSISDB  
**Server:** STL-SSIS-P-01  
**Function Type:** Scalar Function  
**Returns:** varbinary  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["internal.encrypt_lob_data"]
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
CREATE FUNCTION [internal].[encrypt_lob_data]
( 
    @key_name nvarchar(255), 
    @KEY varbinary(8000),
    @IV varbinary(8000),
    @lob varbinary(max) 
)
RETURNS varbinary(max)
AS
BEGIN
    DECLARE @encrypted_binary varbinary(MAX)
    SET @encrypted_binary = (SELECT [internal].[encrypt_binarydata](@key_name, @KEY,@IV, @lob))
    RETURN @encrypted_binary
END

internal,get_database_principals,
CREATE FUNCTION [internal].[get_database_principals]()
RETURNS @ret TABLE
(
    [name] sysname NOT NULL,
    [principal_id] int NOT NULL,
    [type] char(1) NOT NULL,
    [type_desc] nvarchar(60) NULL,
    [default_schema_name] sysname NULL,
    [create_date] datetime NOT NULL,
    [modify_date] datetime NOT NULL,
    [owning_principal_id] int NULL,
    [sid] varbinary(85) NULL,
    [is_fixed_role] bit NOT NULL
)
AS
BEGIN
    INSERT INTO @ret
    SELECT
        [name],
        [principal_id],
        [type],
        [type_desc],
        [default_schema_name],
        [create_date],
        [modify_date],
        [owning_principal_id],
        [sid],
        [is_fixed_role]
     FROM [sys].[database_principals]
     RETURN
END
```
