# eMAF Parser
Worldpay/Vantiv Merchant Activity File parser.

## Supported record types
- Merchant Account Number (MID)/Batch Records (070, 970)
- Summary Section Records (080, 980)
- Credit Reconciliation Detail Transaction Records (300, 301, 306)
- Credit Reconciliation Summary Level Records (500, 501, 503)
- Credit Adjustment/Reversal Detail Level Record (700)
- Debit POS Reconciliation Detail Transaction Records (320, 321)
- Debit POS Reconciliation Summary Level Record (520, 521, 522)
- Debit POS Adjustment Detail Level Record (720)


## Usage
Refer to parse_directory.py file for usage.

For tests run:
make test


