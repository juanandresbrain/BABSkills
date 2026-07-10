# dbo.BankersRound

**Database:** DWStaging  
**Server:** papamart  
**Function Type:** Scalar Function  
**Returns:** decimal(17)  

## Architecture Diagram

```mermaid
flowchart LR
    FUNC["dbo.BankersRound"]
    FUNC --> NoRefs(["No dependencies detected"])
```

## Parameters

| Parameter | Data Type | Max Length | Is Output |
|---|---|---|---|
| @Val | decimal | 17 | NO |
| @Digits | int | 4 | NO |

## Table Dependencies

_No table dependencies detected._

## Function Code

```sql
Create Function dbo.BankersRound(@Val Decimal(32,16), @Digits Int)
Returns Decimal(32,16)
AS
Begin
    Return Case When Abs(@Val - Round(@Val, @Digits, 1)) * Power(10, @Digits+1) = 5 
                Then Round(@Val, @Digits, Case When Convert(int, Round(abs(@Val) * power(10,@Digits), 0, 1)) % 2 = 1 Then 0 Else 1 End)
                Else Round(@Val, @Digits)
                End
End
```

