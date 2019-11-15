import pytz
from datetime import datetime, date, time
from decimal import Decimal


def trim(text, length=None, start=0):
    if not length: return text.strip()
    return text[start:start+length].strip()

def integer(text):
    return int(trim(text))

def parse_datetime(text, date_format, tz=pytz.utc):
    dt = datetime.strptime(text, date_format)
    if tz: dt = dt.replace(tzinfo=tz)
    return dt

def parse_date(text, date_format, tz=pytz.utc):
    return parse_datetime(text, date_format, tz).date()

def parse_time(text, date_format, tz=pytz.utc):
    return parse_datetime(text, date_format, tz).time()

def decimal(text):
    return Decimal(text)

def cents(text, decimal_digits=2):
    dec = decimal(text[:-decimal_digits] + "." + text[-decimal_digits:])
    return dec

def cents_signed(text, decimal_digits=2):
    sign = text[-1:]
    digits = text[:-1]
    dec = cents(digits, decimal_digits)
    if sign == '-': return dec * -1
    return dec

def sign(parser, field_name, sign="+"):
    if sign == '-':
        old = parser.get(field_name)
        parser.set(field_name, -1 * old)
    return sign



# Control Section: present in all records, no exceptions.
CONTROL_SECTION = [
    {
        "field_name"    :   "record_sequence_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9
    },
    {
        "field_name"    :   "record_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "record_length",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   3,
    },
]


FILE_HEADER = [
    {
        "field_name"    :   "file_title",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   8,
    },
    {
        "field_name"    :   "file_version",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   5,
    },
    {
        "field_name"    :   "file_creation_date",
        "parser"        :   lambda parser,text: parse_date(text, "%Y%m%d"),
        "length"        :   8,
    },
    {
        "field_name"    :   "file_creation_time",
        "parser"        :   lambda parser,text: parse_time(text, "%H%M%S"),
        "length"        :   6,
    },
    {
        "field_name"    :   "processing_date",
        "parser"        :   lambda parser,text: parse_date(text, "%Y%m%d"),
        "length"        :   8,
    },
    {
        "length"        :   5,
    },
    {
        "field_name"    :   "file_creator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   20,
    },
    {
        "field_name"    :   "disclaimer",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   30,
    },
    {
        "field_name"    :   "chain_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "field_name"    :   "merchant_acronym",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "principal_group",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "future_group",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "field_name"    :   "affiliate_group",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   7,
    },
    {
        "field_name"    :   "national_group",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   7,
    },
    {
        "field_name"    :   "regional_group",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "branch_group",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   5,
    },
    {
        "field_name"    :   "branch_group",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   5,
    },
    {
        "field_name"    :   "character_super_chain",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   10,
    },
    {
        "length"        :   42,
    },
]

FILE_TRAILER = [
    {
        "field_name"    :   "file_position_reference",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "record_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   8,
    },
    {
        "length"        :   5,
    },
    {
        "field_name"    :   "file_creator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   20,
    },
    {
        "field_name"    :   "disclaimer",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   30,
    },
    {
        "length"        :   110,
    },
]


# 070 - Merchant Account Number (MID)/Batch Header Record 1
BATCH_HEADER = [
    {
        "field_name"    :   "batch_settlement_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "merchant_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   16,
    },
    {
        "field_name"    :   "front_end_mid",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   16,
    },
    {
        "field_name"    :   "merchant_division",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "merchant_store",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "merchant_name",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   25,
    },
    {
        "field_name"    :   "merchant_country_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "batch_file_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "length"        :   105,
    },
]

# 071 - Merchant Account Number (MID)/Batch Header Record 2
# BATCH_HEADER_2 = [
#   {
#       "field_name"    :   "merchant_name",
#       "parser"        :   lambda parser,text: trim(text, 25),
#       "length"        :   25,
#   },
#   {
#       "field_name"    :   "merchant_city",
#       "parser"        :   lambda parser,text: trim(text, 15),
#       "length"        :   15,
#   },
#   {
#       "field_name"    :   "merchant_state",
#       "parser"        :   lambda parser,text: trim(text, 3),
#       "length"        :   3,
#   },
#   {
#       "field_name"    :   "merchant_zipcode",
#       "parser"        :   lambda parser,text: trim(text, 9),
#       "length"        :   9,
#   },
#   {
#       "field_name"    :   "merchant_country_code",
#       "parser"        :   lambda parser,text: trim(text, 3),
#       "length"        :   3,
#   },
#   {
#       "field_name"    :   "timezone",
#       "parser"        :   lambda parser,text: trim(text, 3),
#       "length"        :   3,
#   },
#   {
#       "field_name"    :   "basic_account_number",
#       "parser"        :   lambda parser,text: trim(text, 17),
#       "length"        :   17,
#   },
#   {
#       "field_name"    :   "basic_routing_number",
#       "parser"        :   lambda parser,text: trim(text, 9),
#       "length"        :   9,
#   },
#   {
#       "field_name"    :   "deposit_account_number",
#       "parser"        :   lambda parser,text: trim(text, 17),
#       "length"        :   17,
#   },
#   {
#       "field_name"    :   "deposit_routing_number",
#       "parser"        :   lambda parser,text: trim(text, 9),
#       "length"        :   9,
#   },
#   {
#       "field_name"    :   "fee_account_number",
#       "parser"        :   lambda parser,text: trim(text, 17),
#       "length"        :   17,
#   },
#   {
#       "field_name"    :   "fee_routing_number",
#       "parser"        :   lambda parser,text: trim(text, 9),
#       "length"        :   9,
#   },
#   {
#       "field_name"    :   "exception_account_number",
#       "parser"        :   lambda parser,text: trim(text, 17),
#       "length"        :   17,
#   },
#   {
#       "field_name"    :   "exception_routing_number",
#       "parser"        :   lambda parser,text: trim(text, 9),
#       "length"        :   9,
#   },
#   {
#       "length"        :   23,
#   },
# ]

# Merchant Account Number (MID)/Batch Header Record 3
# BATCH_HEADER_3 = [
#   {
#       "field_name"    :   "alternate_account_number",
#       "parser"        :   lambda parser,text: trim(text),
#       "length"        :   17,
#   },
#   {
#       "field_name"    :   "alternate_routing_number",
#       "parser"        :   lambda parser,text: trim(text),
#       "length"        :   9,
#   },
#   {
#       "length"        :   159,
#   },
# ]

BATCH_TRAILER = [
    {
        "field_name"    :   "file_position_reference",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "settlement_mid",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   16,
    },
    {
        "field_name"    :   "batch_file_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "field_name"    :   "authorized_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   8,
    },
    {
        "field_name"    :   "authorized_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "returns_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   8,
    },
    {
        "field_name"    :   "returns_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "cashback_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   8,
    },
    {
        "field_name"    :   "cashback_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "batch_net_amount",
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "logical_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   9,
    },
    {
        "length"        :   72,
    },
]


# 080 - Summary Section Header Record
SUMMARY_HEADER = [
    {
        "field_name"    :   "payment_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "length"        :   182,
    },
]

# 980 - Summary Section Trailer Record
SUMMARY_TRAILER = [
    {
        "field_name"    :   "payment_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "logical_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   9,
    },
]

# Skipping records 100-103 since they aren't coming through via the ftp feed


# 300 - Credit Reconciliation Detail Transaction Record 1
CREDIT_RECONCILIATION_DETAIL_1 = [
    {
        "field_name"    :   "transaction_date",
        "parser"        :   lambda parser,text: parse_date(text, "%m%d%Y"),
        "length"        :   8,
    },
    {
        "field_name"    :   "transaction_time",
        "parser"        :   lambda parser,text: parse_time(text, "%H%M"),
        "length"        :   4,
    },
    {
        "field_name"    :   "transaction_sequence",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "transaction_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "length"        :   2,
    },
    {
        "field_name"    :   "authorization_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "field_name"    :   "pos_entry_mode",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    # TODO: mask this!
    {
        "field_name"    :   "pan",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   19,
    },
    {
        "field_name"    :   "expiration_date",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "old_authorized_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "cashback_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "mcc_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "card_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "card_product",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "length"        :   6,
    },
    {
        "field_name"    :   "merchant_reference_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "batch_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "field_name"    :   "convenience_fee",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "network_reference_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   24,
    },

    {
        "length"        :   25,
    },
]


# 301 - Credit Reconciliation Detail Transaction Record 2
CREDIT_RECONCILIATION_DETAIL_2 = [
    {
        "field_name"    :   "authorization_source",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "mail_phone_indicator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "cat_indicator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "avs_response_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "cvv2_response_indicator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "registration_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "terminal_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "employee_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "currency_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "aci",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "original_interchange_indicator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "interchange_code",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "interchange_amount", # DDDDDCCCCCCCCC-
        "parser"        :   lambda parser,text: cents_signed(text, 9),
        "length"        :   15,
    },
    {
        "field_name"    :   "surcharge_reason",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "surcharge_amount", # DDDDDDCC-
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   9,
    },
    # TODO: can be pasred additionally:
    {
        "field_name"    :   "network_response",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   24,
    },
    {
        "field_name"    :   "token",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   19,
    },
    {
        "field_name"    :   "token_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "field_name"    :   "emv_indicator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "token_exp_date",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "token_pan_last_4",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "token_level",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "token_requester",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   11,
    },
    {
        "length"        :   42,
    },
]


# Skipping records since they seems to not coming through via the ftp feed:
# 302 - Credit Reconciliation Detail Transaction Record 3 - DCC/MCP Information
# 303 - Credit Reconciliation Detail Transaction Record 4 - Risk Holds and Releases
# 307 - Credit Reconciliation Detail - eComm\Lowell Platform Customer ID Detail - Record 1
# 308 - Credit Reconciliation Detail - eComm\Lowell Platform Customer ID Detail - Record 2

# Credit Reconciliation Detail Transaction Record 7 - Customer Discretionary Data
CREDIT_RECONCILIATION_DETAIL_7 = [
    {
        "field_name"    :   "customer_field_1",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   35,
    },
    {
        "field_name"    :   "customer_field_2",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   20,
    },
    {
        "field_name"    :   "customer_field_3",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   20,
    },
    {
        "length"        :   110,
    },
]

# 500 - Credit Reconciliation Summary Level Record 1
CREDIT_RECONCILIATION_SUMMARY_1 = [
    {
        "field_name"    :   "reconciliation_level",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "submission_date",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "total_records_indicator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "file_submission_time",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "file_date",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "summary_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "division_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "store_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "mid",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   16,
    },
    {
        "field_name"    :   "net_sales_amount", # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "rejected_amount",  # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "net_settled_amount",   # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "net_non_settled_amount",   # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "interchange_fees",     # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "chargeback_amount",    # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "other_adjustments",    # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "net_deposit_amount",   # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "convenience_fee",  # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "length"        :   23,
    },
]

# 501 - Credit Reconciliation Summary Level Record 2
CREDIT_RECONCILIATION_SUMMARY_2 = [
    {
        "field_name"    :   "basic_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "basic_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "deposit_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "deposit_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "fee_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "fee_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "exception_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "exception_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "alternate_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "alternate_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "length"        :   55,
    },
]

# Skipping records since they seems to not coming through via the ftp feed:
# 502 - Credit Reconciliation Summary Level Record 3

# 503 - Credit Reconciliation Summary Level Record 4
CREDIT_RECONCILIATION_SUMMARY_4 = [
    {
        "field_name"    :   "reconciliation_level",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "division_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "store_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "mid",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   16,
    },
    {
        "field_name"    :   "network_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "net_sales_amount", # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "settlement_support_indicator", # S,N
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "network_fees", # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "length"        :   12,
    },
    {
        "field_name"    :   "tax_exempt_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "network_discount", # Currently, this applies only to Voyager/Wright Express.
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "chargeback_amount",
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   15,
    },
    {
        "field_name"    :   "currency_conversion",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "convenience_fee",
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "length"        :   53,
    },
]


# Skipping records since they seems to not coming through via the ftp feed:
# 120 - Debit POS Auth Detail Transaction Reporting Record 1
# 121 - Debit POS Auth Detail Transaction Reporting Record 2
# 122 - Debit POS Detail Authorization Detail - eComm\Lowell Platform Customer ID - Record 1
# 123 - Debit POS Detail Authorization Detail - eComm\Lowell Platform Customer ID - Record 2


# 320 - Debit POS Reconciliation Detail Transaction Record 1
DEBIT_RECONCILIATION_DETAIL_1 = [
    {
        "field_name"    :   "transaction_date",
        "parser"        :   lambda parser,text: parse_date(text, "%m%d%Y"),
        "length"        :   8,
    },
    {
        "field_name"    :   "transaction_time",
        "parser"        :   lambda parser,text: parse_time(text, "%H%M%S"),
        "length"        :   6,
    },
    {
        "field_name"    :   "transaction_sequence",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "transaction_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    # TODO: mask this!
    {
        "field_name"    :   "pan",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   19,
    },
    {
        "field_name"    :   "expiration_date",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "authorization_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "cashback_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "transaction_disposition",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "response_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "pos_entry_mode",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "terminal_location",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   44,
    },
    {
        "field_name"    :   "mcc_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "network_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "institution_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "cardholder_id_method",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "from_account",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "terminal_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   15,
    },
    {
        "field_name"    :   "pinless_ind",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "surcharge_amount",
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "draft_locator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   11,
    },
]

# 321 - Debit POS Reconciliation Detail Transaction Record 2
DEBIT_RECONCILIATION_DETAIL_2 = [
    {
        "field_name"    :   "authorization_source",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "pos_condition",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "registration_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "employee_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "currency_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "business_date",
        "parser"        :   lambda parser,text: parse_date(text, "%m%d%Y"),
        "length"        :   8,
    },
    {
        "field_name"    :   "interchange_code",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "interchange_amount",   # DDDDDCCCCCCCCC-
        "parser"        :   lambda parser,text: cents_signed(text, 9),
        "length"        :   15,
    },
    {
        "length"        :   8,
    },
    {
        "field_name"    :   "token",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   19,
    },
    {
        "field_name"    :   "token_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "field_name"    :   "customer_field_1",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   35,
    },
    {
        "field_name"    :   "customer_field_2",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   20,
    },
    {
        "field_name"    :   "customer_field_3",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   20,
    },
    {
        "field_name"    :   "emv_indicator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "token_requester",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "token_level",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "token_pan_last_4",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "token_exp_date",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "length"        :   3,
    },
]

# Skipping records since they seems to not coming through via the ftp feed:
# 322 - Debit POS Reconciliation Detail - eComm\Lowell Platform Customer ID - Record 1
# 323 - Debit POS Reconciliation Detail - eComm\Lowell Platform Customer ID - Record 2

# 520 - Debit POS Reconciliation Summary Level Record 1
DEBIT_RECONCILIATION_SUMMARY_1 = [
    {
        "field_name"    :   "reconciliation_level",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "submission_date",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "total_records_indicator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "file_submission_time",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "file_date",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "summary_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "division_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "store_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "mid",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   16,
    },
    {
        "field_name"    :   "purchase_sales_amount",    # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "return_amount",    # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "cashback_amount",  # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "net_sales_amount", # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "chargeback_amount",    # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "net_deposit_amount",   # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "interchange_fees",     # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "net_deposit_after_interchange",    # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "sales_surcharge_amount",   # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "return_surcharge_amount",  # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "length"        :   17,
    },
]

# 521 - Debit POS Reconciliation Summary Level Record 2
DEBIT_RECONCILIATION_SUMMARY_2 = [
    {
        "field_name"    :   "basic_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "basic_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "deposit_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "deposit_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "fee_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "fee_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "exception_account_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   17,
    },
    {
        "field_name"    :   "exception_routing_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "length"        :   81,
    },
]


# 522 - Debit POS Reconciliation Summary Level Record 3
DEBIT_RECONCILIATION_SUMMARY_3 = [
    {
        "field_name"    :   "reconciliation_level",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   1,
    },
    {
        "field_name"    :   "division_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "store_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "mid",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   16,
    },
    {
        "field_name"    :   "network_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "sale_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   7,
    },
    {
        "field_name"    :   "sales_amount", # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "return_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   7,
    },
    {
        "field_name"    :   "return_amount",    # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "cashback_amount",  # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "net_sales_amount", # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "network_fees_1",   # DDDDDDDDDCCCC
        "parser"        :   lambda parser,text: cents(text, 4),
        "length"        :   13,
    },
    {
        "field_name"    :   "network_fees_2",   # DDDDDDDDDCCCC
        "parser"        :   lambda parser,text: cents(text, 4),
        "length"        :   13,
    },
    {
        "field_name"    :   "adjustment_amount",    # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   13,
    },
    {
        "field_name"    :   "sales_surcharge_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   7,
    },
    {
        "field_name"    :   "sales_surcharge_amount",   # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },
    {
        "field_name"    :   "return_surcharge_count",
        "parser"        :   lambda parser,text: integer(text),
        "length"        :   7,
    },
    {
        "field_name"    :   "return_surcharge_amount",  # DDDDDDDDDDCC
        "parser"        :   lambda parser,text: cents(text),
        "length"        :   11,
    },

    {
        "field_name"    :   "network_fees_1_sign",  # +/-
        "parser"        :   lambda parser,text: sign(parser, "network_fees_1", trim(text)),
        "length"        :   1,
    },
    {
        "field_name"    :   "network_fees_2_sign",  # +/-
        "parser"        :   lambda parser,text: sign(parser, "network_fees_2", trim(text)),
        "length"        :   1,
    },
]

# 700 - Credit Adjustment/Reversal Detail Level Record 1
CREDIT_ADJUSTMENT_REVERSAL_1 = [
    {
        "field_name"    :   "transaction_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "original_transaction_reference",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   23,
    },
    {
        "field_name"    :   "original_transaction_date",
        "parser"        :   lambda parser,text: parse_date(text, "%m%d%Y"),
        "length"        :   8,
    },
    {
        "field_name"    :   "original_transaction_time",
        "parser"        :   lambda parser,text: parse_time(text, "%H%M%S"),
        "length"        :   6,
    },

    {
        "field_name"    :   "pan",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   19,
    },
    {
        "field_name"    :   "original_amount",
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "adjustment_date",
        "parser"        :   lambda parser,text: parse_date(text, "%m%d%Y"),
        "length"        :   8,
    },
    {
        "field_name"    :   "adjustment_time",
        "parser"        :   lambda parser,text: parse_time(text, "%H%M%S"),
        "length"        :   6,
    },
    {
        "field_name"    :   "adjustment_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "adjustment_amount",
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "adjustment_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "error_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "network_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
]

# 720 - Debit POS Adjustment Detail Level Record 1
DEBIT_ADJUSTMENT_REVERSAL_1 = [
    {
        "field_name"    :   "adjustment_record_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "originator",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "receiver",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   4,
    },
    {
        "field_name"    :   "transaction_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "original_transaction_date",
        "parser"        :   lambda parser,text: parse_date(text, "%m%d%Y"),
        "length"        :   8,
    },
    {
        "field_name"    :   "original_transaction_time",
        "parser"        :   lambda parser,text: parse_time(text, "%H%M%S"),
        "length"        :   6,
    },

    {
        "field_name"    :   "pan",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   19,
    },
    {
        "field_name"    :   "original_amount",
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "adjustment_transaction_disposition",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   2,
    },
    {
        "field_name"    :   "adjustment_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "adjustment_date",
        "parser"        :   lambda parser,text: parse_date(text, "%m%d%Y"),
        "length"        :   8,
    },
    {
        "field_name"    :   "adjustment_time",
        "parser"        :   lambda parser,text: parse_time(text, "%H%M%S"),
        "length"        :   6,
    },
    {
        "field_name"    :   "adjustment_type",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "adjustment_action",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "adjustment_amount",
        "parser"        :   lambda parser,text: cents_signed(text),
        "length"        :   12,
    },
    {
        "field_name"    :   "adjustment_settlement_date",
        "parser"        :   lambda parser,text: parse_date(text, "%m%d%Y"),
        "length"        :   8,
    },
    {
        "field_name"    :   "adjustment_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "error_code",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   3,
    },
    {
        "field_name"    :   "terminal_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   15,
    },
    {
        "field_name"    :   "terminal_sequence_number",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "field_name"    :   "employee_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   9,
    },
    {
        "field_name"    :   "token",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   19,
    },
    {
        "field_name"    :   "token_id",
        "parser"        :   lambda parser,text: trim(text),
        "length"        :   6,
    },
    {
        "length"        :   12,
    },
]
