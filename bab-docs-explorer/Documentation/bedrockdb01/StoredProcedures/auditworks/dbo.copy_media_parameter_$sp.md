# dbo.copy_media_parameter_$sp

**Database:** auditworks  
**Server:** bedrockdb01  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.copy_media_parameter_$sp"]
    code_description(["code_description"]) --> SP
    common_error_handling__sp(["common_error_handling_$sp"]) --> SP
    media_parameter_object(["media_parameter_object"]) --> SP
    media_parameter_rec_calc(["media_parameter_rec_calc"]) --> SP
    media_parameter_rec_group(["media_parameter_rec_group"]) --> SP
    media_parameter_rec_type(["media_parameter_rec_type"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| code_description |
| common_error_handling_$sp |
| media_parameter_object |
| media_parameter_rec_calc |
| media_parameter_rec_group |
| media_parameter_rec_type |

## Stored Procedure Code

```sql
CREATE proc [dbo].[copy_media_parameter_$sp] 
@old_media_parameter_set_no     smallint,
@new_media_parameter_set_no     smallint OUTPUT, --when called from F/E this argument will always be -1
@errmsg                         nvarchar(2000) OUTPUT,
@new_description				nvarchar(255) = NULL  --description of new Media Parameter Set to be created

AS

/* 
PROC NAME: copy_media_parameter_$sp (rel 4.00 and higher)
     DESC: Makes a copy of media parameter tables for a new media parameter set no.
           Called by F/E tm.

Unicode version

HISTORY: 
Date      Name       Def#    Desc
May18,16  Geoff   DAOM-297   Insert a new row into code_description for code_type 18.
Sep29,04  David    DV-1146   Only called by PB, so remove parameter @process_id and @user_name.
Jul09,04  ShuZ     DV-1071   Expand user_name to nvarchar(50)
Apr21,04  Maryam   DV-1071   Receive @process_id, @user_name and pass it to common_error_handling_$sp
Apr14,04  Sab	   DV-1068   Remove code for old media_parameter table
Oct03,03  Maryam     15869   Make sure the row does not exist in media_parameter before inserting
                             into it.
Jul22,03  Maryam     11627   Author
*/

DECLARE
  @errno			int,
  @message_id		int,
  @object_name		nvarchar(255),
  @operation_name	nvarchar(100),
  @process_name		nvarchar(100),
  @current_date		smalldatetime,
  @rows				int
  
  SELECT        
       @process_name = 'copy_media_parameter_$sp',
       @message_id   = 201068,
       @current_date = getdate()

  --DAOM-297 
  INSERT into code_description(
         code_type,
         code,
         code_display_descr,
         code_meaning_control,
         approval_status_date)
  SELECT 18,
         MIN(code) + 1 code,
         IsNull(@new_description, convert(nvarchar, MIN(code) + 1)),
         'U',
         @current_date
    FROM code_description c
   WHERE code_type = 18
   AND NOT EXISTS (SELECT 1
                   FROM code_description v
                   WHERE v.code_type = 18
                   AND v.code = c.code + 1)

  SELECT @errno = @@error
  IF @errno != 0 
    BEGIN
      SELECT @errmsg = 'Failed to create code_description entry for new code-type',
             @object_name = 'code_description',
             @operation_name = 'INSERT'
      GOTO error
    END

   SELECT @new_media_parameter_set_no = MAX(code)
   FROM code_description
   WHERE code_type = 18
   AND code_meaning_control = 'U'
   AND approval_status_date = @current_date
   SELECT @errno = @@error, @rows = @@rowcount
  
   IF @errno != 0 OR @rows = 0
    BEGIN
     SELECT @errmsg = 'Failed to determine new media parameter set code',
            @object_name = 'code_description',
            @operation_name = 'SELECT'
     GOTO error
  END

  INSERT media_parameter_object(
         media_parameter_set_no,
         line_object,
         rec_type,
         rec_group_line_object)
  SELECT @new_media_parameter_set_no,
         line_object,
         rec_type,
         rec_group_line_object
    FROM media_parameter_object
   WHERE media_parameter_set_no = @old_media_parameter_set_no 

  SELECT @errno = @@error
  IF @errno != 0 
    BEGIN
      SELECT @errmsg = 'Failed to insert into media_parameter_object',
             @object_name = 'media_parameter_object',
             @operation_name = 'INSERT'
      GOTO error
    END

  INSERT media_parameter_rec_calc(
         media_parameter_set_no,
         line_object,
         line_action,
         rec_side,
         rec_amount_type,
         rec_amount_subtype,
         rec_type,
         balancing_method,
         store_no_factor,
         register_no_factor,
         till_no_factor,
         cashier_no_factor,
         bank_no_factor,
         multiple_actual_handling_code,
         rec_group_line_object,
         contribution_sign,
         foreign_currency_id,
         convert_to_domestic,
         track_qty,
  short_tolerance_amount,
         short_tolerance_qty,
         short_tolerance_percent,
         unrec_tolerance_days,
         unrec_tolerance_amount)
  SELECT @new_media_parameter_set_no,
         line_object,
         line_action,
         rec_side,
         rec_amount_type,
         rec_amount_subtype,
         rec_type,
         balancing_method,
         store_no_factor,
         register_no_factor,
         till_no_factor,
         cashier_no_factor,
         bank_no_factor,
         multiple_actual_handling_code,
         rec_group_line_object,
         contribution_sign,
         foreign_currency_id,
         convert_to_domestic,
         track_qty,
         short_tolerance_amount,
         short_tolerance_qty,
         short_tolerance_percent,
         unrec_tolerance_days,
         unrec_tolerance_amount
    FROM media_parameter_rec_calc
   WHERE media_parameter_set_no = @old_media_parameter_set_no 

  SELECT @errno = @@error
  IF @errno != 0 
    BEGIN
      SELECT @errmsg = 'Failed to insert into media_parameter_rec_calc',
    @object_name = 'media_parameter_rec_calc',
             @operation_name = 'INSERT'
      GOTO error
    END

  INSERT media_parameter_rec_group(
         media_parameter_set_no,
         rec_type,
         rec_group_line_object,
         short_tolerance_amount,
         short_tolerance_qty,
         short_tolerance_percent,
         unrec_tolerance_days,
         unrec_tolerance_amount,
         rec_option,
         track_qty,
         foreign_currency_id,
         convert_to_domestic)
SELECT @new_media_parameter_set_no,
    rec_type,
         rec_group_line_object,
         short_tolerance_amount,
         short_tolerance_qty,
         short_tolerance_percent,
         unrec_tolerance_days,
         unrec_tolerance_amount,
         rec_option,
         track_qty,
         foreign_currency_id,
         convert_to_domestic
    FROM media_parameter_rec_group
   WHERE media_parameter_set_no = @old_media_parameter_set_no 

  SELECT @errno = @@error
  IF @errno != 0 
    BEGIN
      SELECT @errmsg = 'Failed to insert into media_parameter_rec_group',
             @object_name = 'media_parameter_rec_group',
             @operation_name = 'INSERT'
      GOTO error
    END
    
  INSERT media_parameter_rec_type(
         media_parameter_set_no,
         rec_type,
         balancing_method,
         multiple_actual_handling_code,
         dflt_short_tolerance_amount,
         dflt_short_tolerance_qty,
         dflt_short_tolerance_percent,
         dflt_unrec_tolerance_days,
         dflt_unrec_tolerance_amount,
         auto_populate_object)
  SELECT @new_media_parameter_set_no,
         rec_type,
         balancing_method,
         multiple_actual_handling_code,
         dflt_short_tolerance_amount,
         dflt_short_tolerance_qty,
         dflt_short_tolerance_percent,
         dflt_unrec_tolerance_days,
         dflt_unrec_tolerance_amount,
         auto_populate_object
    FROM media_parameter_rec_type
   WHERE media_parameter_set_no = @old_media_parameter_set_no 

  SELECT @errno = @@error
  IF @errno != 0 
    BEGIN
      SELECT @errmsg = 'Failed to insert into media_parameter_rec_type',
             @object_name = 'media_parameter_rec_type',
             @operation_name = 'INSERT'
      GOTO error
    END


RETURN

error:
 
	EXEC common_error_handling_$sp 0, @errno, @errmsg, 0, @message_id, 
	@process_name, @object_name, @operation_name
	
        RETURN
```

