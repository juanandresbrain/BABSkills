# dbo.add_to_masked_string_$sp

**Database:** me_01  
**Server:** bedrockdb02  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.add_to_masked_string_$sp"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table references detected._

## Stored Procedure Code

```sql
CREATE PROCEDURE [dbo].[add_to_masked_string_$sp] 
   @mask NVARCHAR(20), 
   @old_no NVARCHAR(20),
   @increment INT,
   @new_no NVARCHAR(20) OUTPUT
AS
/*
Proc name: 	add_to_masked_string_$sp
Description: Given a mask, an old number and an increment it will add the increment
   to the old number and store it in a new number.

HISTORY: 
Date            Name       Desc
July 27, 2010   Yan Ding   Defect 109993 failed to generate store xfer # with alphanumeric mask 
*/
BEGIN
   DECLARE @carry   INT,
           @i       INT,
           @digit   INT,
           @err_no  INT,
           @c       NCHAR(1),
           @m       NCHAR(1),
           @err_msg NVARCHAR(255)
   
   SET @i = LEN(@old_no)
   
   -- 1. verify if @old_no matches @mask
   IF LEN(@mask) <> LEN(@old_no)
      BEGIN
         SET @err_no = 1
         SET @err_msg = N'Can''t increase the last generated document number ' + @old_no + 
             N' because it doesn''t match the mask ' + @mask
         GOTO ErrHandler
      END
   
   WHILE @i > 0
      BEGIN
         SET @c = SUBSTRING(@old_no, @i, 1)
         SET @m = SUBSTRING(@mask, @i, 1)
         
         IF UNICODE(N'A') <= UNICODE(@c) AND UNICODE(@c) <= UNICODE(N'Z')
            BEGIN
               IF @m <> N'A' AND @m <> N'C'
                  BEGIN
                     SET @err_no = 1
                     SET @err_msg = N'Can''t increase the last generated document number ' + @old_no + 
                         N' because it doesn''t match the mask ' + @mask
                     GOTO ErrHandler
                  END
            END
         ELSE IF UNICODE(N'0') <= UNICODE(@c) and UNICODE(@c) <= UNICODE(N'9')
            BEGIN
               IF @m <> N'A' AND @m <> N'Z' AND @m <> N'9'
                  BEGIN
                     SET @err_no = 1
                     SET @err_msg = N'Can''t increase the last generated document number ' + @old_no + 
                         N' because it doesn''t match the mask ' + @mask
                     GOTO ErrHandler
                  END
            END
         ELSE
            BEGIN
               SET @err_no = 2
               SET @err_msg = N'Can''t increase the last generated document number ' + @old_no + 
                  N' because it contains the non-alphanumeric character ' + @c
               GOTO ErrHandler
            END
         
         SET @i = @i - 1
      END
   
   -- 2. Increment the @old_no to get @new_no
   SET @new_no = @old_no
   SET @carry = @increment
   SET @i = LEN(@new_no)
   
   WHILE @i > 0 AND @carry > 0
      BEGIN
         SET @c = SUBSTRING(@new_no, @i, 1)
         
         IF UNICODE(N'A') <= UNICODE(@c) AND UNICODE(@c) <= UNICODE(N'Z')
            BEGIN
               SET @digit = UNICODE(@c) - UNICODE(N'A') + @carry
               SET @carry = @digit / 26
               SET @digit = @digit % 26
               SET @c = nchar(@digit + UNICODE(N'A'))
            END
         ELSE IF UNICODE(N'0') <= UNICODE(@c) and UNICODE(@c) <= UNICODE(N'9')
            BEGIN
               SET @digit = UNICODE(@c) - UNICODE(N'0') + @carry
               SET @carry = @digit / 10
               SET @digit = @digit % 10
               SET @c = NCHAR(@digit + UNICODE(N'0'))
            END
         
         SET @new_no = STUFF(@new_no, @i, 1, @c)
         
         SET @i = @i - 1
      END
   
   IF @carry > 0
      BEGIN
         SET @err_no = 3
         SET @err_msg = N'Can''t increase the last generated document number ' + @old_no + 
             N' by ' + CONVERT(NVARCHAR(2), @increment) + N' because an overflow occured'
         GOTO ErrHandler
      END
   
   RETURN
   
   ErrHandler:
      SET @new_no = NULL
      SET @err_no = ISNULL(@err_no, 0)
      
      RAISERROR (N'Message: %s   err_no: %d', 16, 1, @err_msg, @err_no)
END
```

