# dbo.spFranchiseeImportCreateIndexes

**Database:** DWStaging  
**Server:** papamart  

## Architecture Diagram

```mermaid
flowchart LR
    SP["dbo.spFranchiseeImportCreateIndexes"]
    SP --> NoRefs(["No dependencies detected"])
```

## Table Dependencies

_No table dependencies detected._

## Stored Procedure Code

```sql
CREATE proc [dbo].[spFranchiseeImportCreateIndexes] as

set nocount on

--DROP INDEXES
if exists (select * from sys.indexes where name = 'nci_TransactionIDGiftCardAmount' and object_id = OBJECT_ID('FranchiseeTransactionGiftCardIMPORT')) begin drop INDEX nci_TransactionIDGiftCardAmount ON dbo.FranchiseeTransactionGiftCardIMPORT end
if exists (select * from sys.indexes where name = 'nci_TransactionID' and object_id = OBJECT_ID('FranchiseeTransactionHeaderIMPORT')) begin drop INDEX nci_TransactionID ON dbo.FranchiseeTransactionHeaderIMPORT end
if exists (select * from sys.indexes where name = 'nci_TransactionDate' and object_id = OBJECT_ID('FranchiseeTransactionHeaderIMPORT')) begin drop INDEX nci_TransactionDate ON dbo.FranchiseeTransactionHeaderIMPORT end
if exists (select * from sys.indexes where name = 'nci_TransactionIDGrossSales' and object_id = OBJECT_ID('FranchiseeTransactionMerchandiseIMPORT')) begin drop INDEX nci_TransactionIDGrossSales ON dbo.FranchiseeTransactionMerchandiseIMPORT end
if exists (select * from sys.indexes where name = 'nci_TransactionIDAmount' and object_id = OBJECT_ID('FranchiseeTransactionPaymentIMPORT')) begin drop INDEX nci_TransactionIDAmount ON dbo.FranchiseeTransactionPaymentIMPORT end
if exists (select * from sys.indexes where name = 'nci_TransactionIDGiftCardAmount' and object_id = OBJECT_ID('FranchiseeTransactionGiftCardIMPORT')) begin drop INDEX nci_TransactionIDGiftCardAmount ON dbo.FranchiseeTransactionGiftCardIMPORT end
-----------------

--CREATE INDEXEX
CREATE NONCLUSTERED INDEX [nci_TransactionIDGiftCardAmount] ON [dbo].[FranchiseeTransactionGiftCardIMPORT]
(
	[TransactionID] ASC
)
INCLUDE ( 	[GiftCardAmount]) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

---------

CREATE NONCLUSTERED INDEX [nci_TransactionID] ON [dbo].[FranchiseeTransactionHeaderIMPORT]
(
	[TransactionID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

--------

CREATE NONCLUSTERED INDEX [nci_TransactionDate] ON [dbo].[FranchiseeTransactionHeaderIMPORT]
(
	[TransactionDateTime] ASC,
	[InsertDate] ASC
)
INCLUDE ( 	[TransactionID],
	[Franchisee]) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]


-------

CREATE NONCLUSTERED INDEX [nci_TransactionIDGrossSales] ON [dbo].[FranchiseeTransactionMerchandiseIMPORT]
(
	[TransactionID] ASC
)
INCLUDE ( 	[GrossSales]) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]

--------

CREATE NONCLUSTERED INDEX [nci_TransactionIDAmount] ON [dbo].[FranchiseeTransactionPaymentIMPORT]
(
	[TransactionID] ASC
)
INCLUDE ( 	[Amount]) WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
```

