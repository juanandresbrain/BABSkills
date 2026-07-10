# dbo.Generate_Seq

**Database:** dw  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.Generate_Seq"]
    generate_number(["generate_number"]) --> SP
```

## Table Dependencies

| Referenced Table |
|---|
| generate_number |

## Stored Procedure Code

```sql
CREATE   PROCEDURE dbo.Generate_Seq  @Name varchar(20)
as

Declare @old_seq  int
Declare @Seq_no int
 
Begin Tran SEQ

select @old_Seq = last_number from generate_number where description = @name

if (@old_Seq is null)
begin
            insert into Generate_number values (@name,1)
            select @Seq_no = 1
end

else

begin
            update Generate_number set Last_number = last_number+1
            where Description = @name
            Select @Seq_no = last_number from generate_number where description = @name
end
COMMIT  Tran SEQ 
Return @Seq_no
```

