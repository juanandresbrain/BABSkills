# dbo.convert_query_list_to_sql_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.convert_query_list_to_sql_$sp"]
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| common_error_handling_$sp |

## Stored Procedure Code

```sql
create proc dbo.convert_query_list_to_sql_$sp 
( @query_list varchar(8000), 
  @field_name varchar(100),
  @query_list_sql varchar(8000) OUTPUT
)
AS
/*
  Proc name: convert_query_list_to_sql_$sp
       Desc: Receives a comma delimited list of numbers or number-ranges (dash-delimited) along with the name of the field 
             that holds the number in question and converts it to an SQL statement clause suitable for use in the calling
             procedure's WHERE clause.
DECLARE

  HISTORY:
  Date     Name     Defect# 	Desc
  May20,14 Vicci    TFS-63835 	Author
*/
DECLARE
  @query_list_length smallint,
  @start_pstn smallint, 
  @dash_pstn smallint, 
  @comma_pstn smallint, 
  
  @sql_value_list varchar(8000), 
  @sql_value_range varchar(8000), 
  @from_value numeric(12,0), 
  @to_value numeric(12,0), 
  @from_value_string varchar(8000), 

  @errmsg            nvarchar(2000),
  @errmsg2			 nvarchar(2000),
  @errno             int,
  @message_id        int,
  @object_name       nvarchar(255),
  @operation_name    nvarchar(100),
  @process_name      nvarchar(100),
  @process_no        int;

SELECT @process_name = 'convert_query_list_to_sql_$sp',
       @process_no   = 302,
       @message_id   = 201068,
       @start_pstn   = 1, 
       @dash_pstn    = 0,
       @query_list   = REPLACE(@query_list, ' ', '');

IF @query_list = '' OR @query_list IS NULL
BEGIN
  SELECT @query_list_sql = '';
  RETURN;
END;

IF LTRIM(RTRIM(@field_name)) = '' OR @field_name IS NULL
  SELECT @field_name = '@field_name';

--Validate @query_list passed in
IF IsNumeric(REPLACE(REPLACE(REPLACE(@query_list, '-', 0), ',', 0), ' ', '')) = 0
BEGIN
  SELECT @errno = 201684, @message_id = 201684, @errmsg2 = '''' + @query_list + ''' is an nvalid number list argument:  it must be a comma delimited list of numbers or number-ranges (dash-delimited).'
  EXEC common_error_handling_$sp @process_no, @errno, @errmsg2, 0, @message_id, @process_name, @object_name, @operation_name, 0;
  RETURN;
END

BEGIN TRY;
SELECT @query_list_length = len(@query_list)

WHILE @start_pstn <= @query_list_length
BEGIN
  SELECT @dash_pstn = CHARINDEX('-', @query_list, @start_pstn)
  IF @dash_pstn > 0
  BEGIN
    SELECT @from_value_string = SUBSTRING(@query_list, @start_pstn, @dash_pstn - @start_pstn), 
           @comma_pstn = -1
    --SELECT @from_value_string from_cashier_string, @start_pstn start_pstn, @dash_pstn dash_pstn
    WHILE @comma_pstn <> 0
    BEGIN
      --SELECT @from_value_string from_cashier_string, @comma_pstn comma_pstn
      SELECT @comma_pstn = COALESCE(CHARINDEX(',', @from_value_string, 1), 0)
      IF @comma_pstn = 0 
      BEGIN
        SELECT @from_value = @from_value_string
        SELECT @start_pstn = @dash_pstn + 1
      END
      ELSE
      BEGIN
        SELECT @sql_value_list = CASE WHEN @sql_value_list IS NULL 
                                        THEN ' ' + @field_name + ' IN (' 
                                        ELSE @sql_value_list + ', ' 
                                   END + SUBSTRING(@from_value_string, 1, @comma_pstn - 1)
        SELECT @from_value_string = SUBSTRING(@from_value_string, @comma_pstn + 1, LEN(@from_value_string) - @comma_pstn)
      END
    END
    
    SELECT @comma_pstn = CHARINDEX(',', @query_list, @start_pstn) 
    IF @comma_pstn = 0 
    BEGIN
      SELECT @to_value = SUBSTRING(@query_list, @start_pstn, @query_list_length - @start_pstn + 1)
      SELECT @start_pstn = @query_list_length + 1
    END
    ELSE
    BEGIN  
      SELECT @to_value = SUBSTRING(@query_list, @start_pstn, @comma_pstn - @start_pstn)
      SELECT @start_pstn = @comma_pstn + 1
    END

    SELECT @sql_value_range = CASE WHEN @sql_value_range IS NULL THEN ' (' + @field_name + ' BETWEEN ' ELSE @sql_value_range + ' OR ' + @field_name + ' BETWEEN ' END + CONVERT(varchar, @from_value) + ' AND ' + CONVERT(varchar, @to_value)
  END  --IF @dash_pstn > 0
  ELSE
  BEGIN
--    SELECT @sql_value_list sql_cashier_list, @start_pstn start_pstn, @query_list_length cashier_list_length
    SELECT @sql_value_list = CASE WHEN @sql_value_list IS NULL 
          THEN ' ' + @field_name + ' IN (' 
                                    ELSE @sql_value_list + ', ' 
                               END + SUBSTRING(@query_list, @start_pstn, @query_list_length - @start_pstn + 1)
    SELECT @start_pstn = @query_list_length + 1
  END  --ELSE OF IF @dash_pstn > 0
END   --WHILE @start_pstn <= @query_list_length 
IF @sql_value_list IS NOT NULL 
  SELECT @sql_value_list = @sql_value_list + ')'
IF @sql_value_range IS NOT NULL 
  SELECT @sql_value_range = @sql_value_range + ')'
IF @sql_value_list IS NOT NULL AND @sql_value_range IS NOT NULL
  SELECT @query_list_sql = @sql_value_list + ' OR' + @sql_value_range
ELSE 
  SELECT @query_list_sql = COALESCE(@sql_value_list, '') + COALESCE(@sql_value_range, '')

--SELECT @query_list query_list, @query_list_sql query_list_sql

RETURN;
END TRY 

BEGIN CATCH
  SELECT @errno = ERROR_NUMBER();
  IF @errmsg2 IS NULL
  BEGIN
    SELECT @errmsg2 = @process_name + ':  ' + COALESCE(@errmsg, '') + ' Line: ' + CONVERT(varchar, ERROR_LINE()) + ', ' + ERROR_MESSAGE();
  END;
  SELECT @errmsg = @errmsg2;  
  EXEC common_error_handling_$sp @process_no, @errno, @errmsg2, 0, @message_id, @process_name, @object_name, @operation_name, 0;
  RETURN;
END CATCH;
```

