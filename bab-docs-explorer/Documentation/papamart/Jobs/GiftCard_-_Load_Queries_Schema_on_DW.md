# Job: GiftCard - Load Queries Schema on DW

**Enabled:** Yes  
**Server:** papamart  
**Description:** Loads papamart DW.queries..giftcards_activated and giftcards_redeemed, loads 60 days by default, if need to load more just add the number after the proc name  

## Architecture Diagram

```mermaid
flowchart LR
    JOB["GiftCard - Load Queries Schema on DW"]
    JOB --> S1["Step 1: DW [TSQL]"]
```

## Steps

### Step 1: DW
**Subsystem:** TSQL  

```sql
exec spGiftcard_Extract_Activated_Redeemed
```

