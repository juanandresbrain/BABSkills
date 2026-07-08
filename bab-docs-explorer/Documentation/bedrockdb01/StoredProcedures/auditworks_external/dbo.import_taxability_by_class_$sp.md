# dbo.import_taxability_by_class_$sp

**Database:** auditworks_external  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.import_taxability_by_class_$sp"]
    ORG_CHN(["ORG_CHN"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    import_taxability_by_class(["import_taxability_by_class"]) --> SP
    parameter_general(["parameter_general"]) --> SP
    store_audit_status(["store_audit_status"]) --> SP
    taxability_by_class(["taxability_by_class"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| ORG_CHN |
| common_error_handling_$sp |
| import_taxability_by_class |
| parameter_general |
| store_audit_status |
| taxability_by_class |

## Stored Procedure Code

```sql
create proc [dbo].[import_taxability_by_class_$sp] AS

/* Version: 1.00 Date: 1998/04/14 */
/* Author: Vicci de Takacsy */
/* Description: This program posts updates to taxability exceptions by class.
		received from a client or 3rd party to the AW taxability_by_class
		table based on the I'nsert U'pdate D'elete R'eplacement_file entry_type.

History:
Date	 Name		Def#	Action
Sep07,11 Vicci        129626    Avoid multiple non-expired entries following attempt to delete non-existent entry when prior expired entry exists.
                                Avoid overlapping effective-dates when the taxability by class import is aborted.
Sep06,06  Tim           76719 Null Concatenation Fix.
May25,04 David          DV-1071 Use ORG_CHN table as new the Store table.
Mar18,03 Phu            5425    Remove @errmsg from parameter list to standardize import
May16,02 Henry		1-CD0IX Add R3.5 standardized common error handling
Jun27,01 Maryam         8090 	Modified based on release 3 import layout.
Feb26,01 Phu            7371 	Change double quotes to single quotes for MS SQL compatibility

*/

DECLARE
  @errmsg		nvarchar(255),
  @errno		int,
  @sales_date		smalldatetime,
  @entry_type		char,
  @store_no		int,
  @tax_jurisdiction	nchar(5),
  @tax_level		tinyint,
  @class_code		int,
  @tax_rate_code	tinyint,   
  @effective_from_date	smalldatetime,
  @effective_until_date	smalldatetime,
  @max_effective_from_date  smalldatetime,
  @max_date		smalldatetime,
  @min_date		smalldatetime,
  @upc_lookup_division	tinyint,
  @rows			int,
  @cursor_open		int,
-- used for common error handling.
  @process_no		smallint,
  @log_flag		tinyint,
  @object_name		nvarchar(255),
  @process_name		nvarchar(100),
  @operation_name	nvarchar(100),
  @message_id		int,
  @message_id2		int,
  @memo1 		nvarchar(50)

SET CONCAT_NULL_YIELDS_NULL OFF

SELECT @cursor_open = 0,
       @process_name = 'import_taxability_by_class_$sp',
       @message_id = 201068,
       @log_flag = 1,  -- called from smartload
       @process_no = 7 -- standard import

  SELECT @sales_date = MAX(sales_date)
    FROM store_audit_status 
   WHERE store_audit_status IN (400, 500)
     AND sales_date > (SELECT last_date_closed
                       FROM parameter_general)
  SELECT @errno = @@error
  IF @errno !=0 
    BEGIN
      SELECT @errmsg='Failed to select from store_audit_status',
	     @object_name = 'import_ntfm',
	     @operation_name = 'SELECT'
      GOTO error
    END
                         
  IF @sales_date IS NULL --
   BEGIN
      SELECT @sales_date = last_date_closed
        FROM parameter_general
      
      SELECT @errno = @@error
      IF @errno !=0 
        BEGIN
          SELECT @errmsg='Failed to select last_date_closed',
		 @object_name = 'parameter_general',
		 @operation_name = 'SELECT'
          GOTO error
        END
    END

  SELECT @sales_date = DATEADD(dd, 1, @sales_date) 

  UPDATE import_taxability_by_class
     SET effective_from_date = @sales_date
   WHERE effective_from_date IS NULL --
    AND UPPER(entry_type) IN ('I', 'U', 'R')

  SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to set effective_from_date.',
	     @object_name = 'import_taxability_by_class',
	     @operation_name = 'UPDATE'
      GOTO error
    END

  UPDATE import_taxability_by_class
     SET tax_jurisdiction = s.TAX_JRSDCTN_CODE
    FROM import_taxability_by_class bcp, ORG_CHN s 
   WHERE bcp.store_no = s.ORG_CHN_NUM
     AND UPPER(bcp.entry_subtype) = 'S'

  SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to set tax-jurisdiction for import_taxability_by_class rows of subtype S',
	     @object_name = 'import_taxability_by_class',
	     @operation_name = 'UPDATE'
      GOTO error
    END

  IF EXISTS(SELECT entry_type
              FROM import_taxability_by_class
             WHERE UPPER(entry_type) = 'R')
    TRUNCATE table taxability_by_class

  SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to truncate taxability_by_class table in preparation for replacement',
	     @object_name = 'taxability_by_class',
	     @operation_name = 'TRUNCATE'
      GOTO error
    END

  
  DECLARE tax_class_crsr CURSOR
  FOR
SELECT  entry_type,
	  store_no,
	  tax_jurisdiction,
	  class_code,
	  tax_level,
	  tax_rate_code,
	  effective_from_date,
	  upc_lookup_division
  FROM	  import_taxability_by_class
 ORDER BY effective_from_date   
	
  OPEN tax_class_crsr

  SELECT @errno = @@error
  IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to open cursor tax_class_crsr.',
	     @object_name = 'tax_class_crsr',
	     @operation_name = 'OPEN'
      GOTO error
    END

  SELECT @cursor_open = 1

  WHILE 1=1
  BEGIN

  FETCH tax_class_crsr INTO
	@entry_type,
	@store_no,
        @tax_jurisdiction,
        @class_code,
        @tax_level,
        @tax_rate_code,
        @effective_from_date,
        @upc_lookup_division

  IF @@fetch_status <> 0
    BREAK

  IF UPPER(@entry_type) NOT IN ('I', 'R', 'D', 'U')
    BEGIN
      SELECT @errmsg = 'Invalid entry_type in tax_class data file. Please verify the |1 table.',
	     @errno = 201064,
	     @message_id2 = 201064,
	     @object_name = 'tax_class_crsr',
	     @memo1 = 'tax_class_crsr',
	     @operation_name = 'SELECT'

      EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id2, 
		@process_name, @object_name, @operation_name, @log_flag, NULL, NULL,NULL, NULL, @memo1

      SELECT @errno = 0
    END

  IF UPPER(@entry_type) = 'D'
  BEGIN
    SELECT @max_effective_from_date = MAX(effective_from_date)
      FROM taxability_by_class
     WHERE tax_jurisdiction = @tax_jurisdiction 
       AND class_code = @class_code
       AND tax_level = @tax_level
       AND upc_lookup_division = @upc_lookup_division
       AND effective_from_date < @effective_from_date
    SELECT @errno = @@error
    IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to select effective_from_date of the row before that being deleted.',
	     @object_name = 'taxability_by_class',
	     @operation_name = 'SELECT'
      GOTO error
    END

    SELECT @effective_until_date = effective_until_date
      FROM taxability_by_class
     WHERE tax_jurisdiction = @tax_jurisdiction 
       AND class_code = @class_code
       AND tax_level = @tax_level
       AND upc_lookup_division = @upc_lookup_division
       AND (effective_from_date = @effective_from_date OR @effective_from_date IS NULL)  --note:  import table allows null effective_from_date meaning all effective dates
    SELECT @errno = @@error, @rows = @@rowcount
    IF @errno != 0
    BEGIN
      SELECT @errmsg = 'Failed to select effective_until_date of the row being deleted.',
      	     @object_name = 'taxability_by_class',
      	     @operation_name = 'SELECT'
      GOTO error
    END

    IF @rows > 0 --i.e. row to be deleted exists
    BEGIN
      BEGIN TRANSACTION
      
      DELETE taxability_by_class
       WHERE tax_jurisdiction = @tax_jurisdiction 
         AND class_code = @class_code
         AND tax_level = @tax_level
         AND (effective_from_date = @effective_from_date OR @effective_from_date IS NULL)
         AND upc_lookup_division = @upc_lookup_division
      SELECT @errno = @@error
      IF @errno != 0
      BEGIN
        SELECT @errmsg = 'Failed to DELETE from taxability_by_class.',
               @object_name = 'taxability_by_class',
               @operation_name = 'DELETE'
        GOTO error
      END

      IF @max_effective_from_date IS NOT NULL AND @rows = 1 --note:  @rows > 1 means all effective dates have already been deleted
      BEGIN
        UPDATE taxability_by_class
           SET effective_until_date = @effective_until_date
         WHERE tax_jurisdiction = @tax_jurisdiction 
           AND class_code = @class_code
           AND tax_level = @tax_level
           AND effective_from_date = @max_effective_from_date
           AND upc_lookup_division = @upc_lookup_division
        SELECT @errno = @@error
        IF @errno != 0
        BEGIN
          SELECT @errmsg = 'Failed to set effective_until_date of the row before that being deleted.',
		 @object_name = 'taxability_by_class',
		 @operation_name = 'UPDATE'
          GOTO error
        END
      END --IF @max_effective_from_date IS NOT NULL AND @rows = 1
      
      COMMIT TRANSACTION 
    END -- IF @rows > 0 --i.e. row(s) to be deleted exists
  END --IF @entry_type = 'D'

  IF UPPER(@entry_type) IN ('I', 'U', 'R')
    BEGIN
      
      UPDATE taxability_by_class
         SET tax_rate_code = @tax_rate_code
       WHERE tax_jurisdiction = @tax_jurisdiction 
         AND class_code = @class_code
         AND tax_level = @tax_level
         AND effective_from_date = @effective_from_date
         AND upc_lookup_division = @upc_lookup_division       
      SELECT @rows = @@rowcount,
             @errno = @@error
      IF @errno != 0
        BEGIN
          SELECT @errmsg = 'Failed to UPDATE taxability_by_class from import_taxability_by_class',
		 @object_name = 'taxability_by_class',
		 @operation_name = 'UPDATE'
          GOTO error
        END
  
      IF @rows = 0 
        BEGIN 
          SELECT @max_date = MAX(effective_from_date)
            FROM taxability_by_class
           WHERE tax_jurisdiction = @tax_jurisdiction
             AND class_code = @class_code
             AND tax_level = @tax_level
             AND upc_lookup_division = @upc_lookup_division
             AND effective_from_date < @effective_from_date
          SELECT @errno = @@error
          IF @errno != 0
            BEGIN
              SELECT @errmsg = 'Failed to select effective_from_date of the row before that being inserted.',
		     @object_name = 'taxability_by_class',
		     @operation_name = 'SELECT'
              GOTO error
            END

          SELECT @min_date = MIN(effective_from_date)
            FROM taxability_by_class
           WHERE tax_jurisdiction = @tax_jurisdiction
             AND class_code = @class_code
             AND tax_level = @tax_level
             AND upc_lookup_division = @upc_lookup_division
             AND effective_from_date > @effective_from_date
          SELECT @errno = @@error
          IF @errno != 0
            BEGIN
              SELECT @errmsg = 'Failed to select effective_from_date of the row after that being inserted.',
		     @object_name = 'taxability_by_class',
		     @operation_name = 'SELECT'
              GOTO error
            END

      BEGIN TRANSACTION 

          INSERT taxability_by_class (
                 tax_jurisdiction,
                 class_code,
                 upc_lookup_division,
                 tax_level,
                 tax_rate_code,
                 effective_from_date)
          VALUES (@tax_jurisdiction,
                 @class_code,
                 @upc_lookup_division,
                 @tax_level,
                 @tax_rate_code,
                 @effective_from_date)        

          SELECT @errno = @@error
          IF @errno != 0
            BEGIN
              SELECT @errmsg = 'Unable to INSERT imported exceptions for store_no = ' +
                                convert(nvarchar, @store_no) +', tax_jurisdiciton = ' + @tax_jurisdiction +
                                ', class_code = ' + convert(nvarchar, @class_code) + ', tax_level = ' + convert(nvarchar, @tax_level)+
                                ', tax_rate_code = ' + convert(nvarchar,@tax_rate_code) +  ', upc_lookup_division = ' + convert(nvarchar,@upc_lookup_division) + ', effective_from_date = '
                                + CONVERT(nvarchar(11), @effective_from_date)+' into the taxability_by_class table ',
		     @object_name = 'taxability_by_class',
		     @operation_name = 'INSERT'
              GOTO error
            END

            
          UPDATE taxability_by_class
             SET effective_until_date = DATEADD(dd, -1, @effective_from_date)
           WHERE tax_jurisdiction = @tax_jurisdiction 
             AND class_code = @class_code
             AND tax_level = @tax_level
             AND effective_from_date = @max_date
             AND upc_lookup_division = @upc_lookup_division       
          SELECT @errno = @@error
          IF @errno != 0
            BEGIN
              SELECT @errmsg = 'Failed to UPDATE effective_until_date of the row before that being inserted',
		     @object_name = 'taxability_by_class',
		     @operation_name = 'UPDATE'
              GOTO error
            END
            
          UPDATE taxability_by_class
             SET effective_until_date = DATEADD(dd, -1, @min_date)
           WHERE tax_jurisdiction = @tax_jurisdiction 
             AND class_code = @class_code
             AND tax_level = @tax_level
             AND effective_from_date = @effective_from_date
             AND upc_lookup_division = @upc_lookup_division
       
        SELECT @errno = @@error
        IF @errno != 0
          BEGIN
            SELECT @errmsg = 'Failed to UPDATE effective_until_date of the row being inserted.',
		   @object_name = 'taxability_by_class',
		   @operation_name = 'UPDATE'
            GOTO error
          END
        
        COMMIT TRANSACTION
      END -- IF @rows = 0 
    END --IF @entry_type IN ('I', 'U', 'R')
  END /* WHILE 1=1 */

CLOSE tax_class_crsr
SELECT @errno = @@error
IF @errno != 0
  BEGIN
    SELECT @errmsg = 'Failed to CLOSE cursor tax_class_crsr.',
           @object_name = 'tax_class_crsr',
	   @operation_name = 'CLOSE'
    GOTO error
  END

DEALLOCATE tax_class_crsr
    
RETURN

error:   /* Common error handler. */

	IF @cursor_open = 1
	  BEGIN
	   CLOSE tax_class_crsr
	   DEALLOCATE tax_class_crsr
	  END

	EXEC common_error_handling_$sp @process_no, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name, @log_flag

	RETURN
```

