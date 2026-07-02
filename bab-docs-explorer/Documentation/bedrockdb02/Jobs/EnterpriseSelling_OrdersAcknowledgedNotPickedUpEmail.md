# Job: EnterpriseSelling_OrdersAcknowledgedNotPickedUpEmail

**Enabled:** Yes  
**Server:** bedrockdb02  
**Description:** Sends email to BSRFollowup@buildabear.com with list of orders not picked up after 7 days of being acknowledged in Enterprise Selling system

## Architecture Diagram

```mermaid
flowchart LR
    JOB["EnterpriseSelling_OrdersAcknowledgedNotPickedUpEmail"]
    JOB --> Run_spEsellEmailAckOrdersNotPickedUp_1["Step 1: Run spEsellEmailAckOrdersNotPickedUp [TSQL]"]`n```

## Steps

### Step 1: Run spEsellEmailAckOrdersNotPickedUp
**Subsystem:** TSQL  

```sql
exec spEsellEmailAckOrdersNotPickedUp
```


