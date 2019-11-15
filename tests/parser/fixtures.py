from decimal import Decimal
# from datetime import datetime, date, time
import datetime



PARSER_TEST_DATA = [
    # File open 010:
    (
        # source:
        "000000001010200MAF FILE03.002019111505144520191114     MERCHANT SERVICES   PROPRIETARY AND CONFIDENTIAL  0J412L",
        # result:
        {
            'affiliate_group': '',
            'branch_group': '',
            'chain_code': '0J412L',
            'character_super_chain': '',
            'disclaimer': 'PROPRIETARY AND CONFIDENTIAL',
            'file_creation_date': datetime.date(2019, 11, 15),
            'file_creation_time': datetime.time(5, 14, 45),
            'file_creator': 'MERCHANT SERVICES',
            'file_title': 'MAF FILE',
            'file_version': '03.00',
            'future_group': '',
            'merchant_acronym': '',
            'national_group': '',
            'principal_group': '',
            'processing_date': datetime.date(2019, 11, 14),
            'record_length': 200,
            'record_sequence_number': '000000001',
            'record_type': '010',
            'regional_group': ''
        }
    ),

    # File close 910:
    (
        # source:
        "000000001020200MAF FILE03.002019111505202220191114     MERCHANT SERVICES   PROPRIETARY AND CONFIDENTIAL  02540OCZBN",
        # result:
        {
            'affiliate_group': '',
            'branch_group': '',
            'chain_code': '02540O',
            'character_super_chain': '',
            'disclaimer': 'PROPRIETARY AND CONFIDENTIAL',
            'file_creation_date': datetime.date(2019, 11, 15),
            'file_creation_time': datetime.time(5, 20, 22),
            'file_creator': 'MERCHANT SERVICES',
            'file_title': 'MAF FILE',
            'file_version': '03.00',
            'future_group': '',
            'merchant_acronym': 'CZBN',
            'national_group': '',
            'principal_group': '',
            'processing_date': datetime.date(2019, 11, 14),
            'record_length': 200,
            'record_sequence_number': '000000001',
            'record_type': '020',
            'regional_group': ''
        }
    ),

    # Batch open 070:
    (
        # source:
        "000000002070200025429XXXXXXX1255 2XXXXXX1255        000000001HUSTLER 8009140109 CMI   840000001",
        # result:
        {
            'batch_file_number': '000001',
            'batch_settlement_type': '02',
            'front_end_mid': '2XXXXXX1255',
            'merchant_account_number': '5429XXXXXXX1255',
            'merchant_country_code': '840',
            'merchant_division': '',
            'merchant_name': 'HUSTLER 8009140109 CMI',
            'merchant_store': '000000001',
            'record_length': 200,
            'record_sequence_number': '000000002',
            'record_type': '070'
        }
    ),

    # Batch close 970:
    (
        # source:
        "000000367970200END OF MID  5429XXXXXXX7371 000025000000060000042930000000000000000000000000000000000000000000000429300+000000012",
        # result:
        {
            'authorized_amount': Decimal('4293.00'),
            'authorized_count': 6,
            'batch_file_number': '000025',
            'batch_net_amount': Decimal('4293.00'),
            'cashback_amount': Decimal('0.00'),
            'cashback_count': 0,
            'file_position_reference': 'END OF MID',
            'logical_count': 12,
            'record_length': 200,
            'record_sequence_number': '000000367',
            'record_type': '970',
            'returns_amount': Decimal('0.00'),
            'returns_count': 0,
            'settlement_mid': '5429XXXXXXX7371'
        }
    ),

    # Summary open 080:
    (
        # source:
        "000000860080200DBT",
        # result:
        {
            'payment_type': 'DBT',
            'record_length': 200,
            'record_sequence_number': '000000860',
            'record_type': '080'
        }
    ),

    # Summary close 980:
    (
        # source:
        "000000061980200CRT000000024",
        # result:
        {
            'logical_count': 24,
            'payment_type': 'CRT',
            'record_length': 200,
            'record_sequence_number': '000000061',
            'record_type': '980'
        }
    ),


    # Transaction record 300:
    (
        # source:
        "00000001730020011132019182600001962605   08973E05 XXXXXXXXXXXX1362   09230000010519900000000000000000000004829MCRDMEB      0057560000407001 0000000000002305379318100068982165",
        # result:
        {
            'amount': Decimal('1051.99'),
            'authorization_code': '08973E',
            'batch_number': '07001',
            'card_product': 'MEB',
            'card_type': 'MCRD',
            'cashback_amount': Decimal('0.00'),
            'convenience_fee': Decimal('0.00'),
            'expiration_date': '0923',
            'mcc_code': '4829',
            'merchant_reference_number': '00575600004',
            'network_reference_number': '02305379318100068982165',
            'old_authorized_amount': Decimal('0.00'),
            'pan': 'XXXXXXXXXXXX1362',
            'pos_entry_mode': '05',
            'record_length': 200,
            'record_sequence_number': '000000017',
            'record_type': '300',
            'transaction_date': datetime.date(2019, 11, 13),
            'transaction_sequence': '000019626',
            'transaction_time': datetime.time(18, 26),
            'transaction_type': '05'
        }
    ),

    # Transaction record 301:
    (
        # source:
        "0000000183012005   Z  0056         550000000840  0700034625300029560000000- m 00001284+MEBESYGEP1113                                    Y",
        # result:
        {
            'aci': '',
            'authorization_source': '5',
            'avs_response_code': 'Z',
            'cat_indicator': '',
            'currency_code': '840',
            'cvv2_response_indicator': '',
            'employee_id': '550000000',
            'emv_indicator': 'Y',
            'interchange_amount': Decimal('-29.560000000'),
            'interchange_code': 346253,
            'mail_phone_indicator': '',
            'network_response': 'MEBESYGEP1113',
            'original_interchange_indicator': '07',
            'record_length': 200,
            'record_sequence_number': '000000018',
            'record_type': '301',
            'registration_number': '0056',
            'surcharge_amount': Decimal('12.84'),
            'surcharge_reason': 'm',
            'terminal_number': '',
            'token': '',
            'token_exp_date': '',
            'token_id': '',
            'token_level': '',
            'token_pan_last_4': '',
            'token_requester': ''
        }
    ),

    # Transaction record 306:
    (
        # source:
        "000000292306200L38164012404",
        # result:
        {
            'customer_field_1': 'L38164012404',
            'record_length': 200,
            'record_sequence_number': '000000292',
            'record_type': '306'
        }
    ),

    # Transaction record 320:
    (
        # source:
        "0000000153202001113201922230900001963410 XXXXXXXXXXXX1813   0323000003091950000030919500000000000300005 1000 W REDONDO BEACH BLVD  GARDENA        CA4829INLKINT11DE 029804571255604N00000000000498600011",
        # result:
        {
            'amount': Decimal('3091.95'),
            'authorization_amount': Decimal('3091.95'),
            'cardholder_id_method': '1',
            'cashback_amount': Decimal('0.00'),
            'draft_locator': '00498600011',
            'expiration_date': '0323',
            'from_account': 'DE',
            'institution_id': 'INT1',
            'mcc_code': '4829',
            'network_id': 'INLK',
            'pan': 'XXXXXXXXXXXX1813',
            'pinless_ind': 'N',
            'pos_entry_mode': '05',
            'record_length': 200,
            'record_sequence_number': '000000015',
            'record_type': '320',
            'response_code': '000',
            'surcharge_amount': Decimal('0.00'),
            'terminal_id': '029804571255604',
            'terminal_location': '1000 W REDONDO BEACH BLVD  GARDENA        CA',
            'transaction_date': datetime.date(2019, 11, 13),
            'transaction_disposition': '3',
            'transaction_sequence': '000019634',
            'transaction_time': datetime.time(22, 23, 9),
            'transaction_type': '10'
        }
    ),

    # Transaction record 321:
    (
        # source:
        "000000016321200 00 00860200000008401114201900003017600001770000000-                                                                                                            Y",
        # result:
        {
            'authorization_source': '',
            'business_date': datetime.date(2019, 11, 14),
            'currency_code': '840',
            'customer_field_1': '',
            'customer_field_2': '',
            'customer_field_3': '',
            'employee_id': '020000000',
            'emv_indicator': 'Y',
            'interchange_amount': Decimal('-1.770000000'),
            'interchange_code': 30176,
            'pos_condition': '00',
            'record_length': 200,
            'record_sequence_number': '000000016',
            'record_type': '321',
            'registration_number': '0086',
            'token': '',
            'token_exp_date': '',
            'token_id': '',
            'token_level': '',
            'token_pan_last_4': '',
            'token_requester': ''
        }
    ),

    # Summary record 500:
    (
        # source:
        "000000049500200M1114 10371114POS   0000000505429XXXXXXX8100 000000244950+000000000000+000000244950+000000000000+000000000000+000000000000+000000000000+000000244950+000000000000+",
        # result:
        {
            'chargeback_amount': Decimal('0.00'),
            'convenience_fee': Decimal('0.00'),
            'division_code': '',
            'file_date': '1114',
            'file_submission_time': '1037',
            'interchange_fees': Decimal('0.00'),
            'mid': '5429XXXXXXX8100',
            'net_deposit_amount': Decimal('2449.50'),
            'net_non_settled_amount': Decimal('0.00'),
            'net_sales_amount': Decimal('2449.50'),
            'net_settled_amount': Decimal('2449.50'),
            'other_adjustments': Decimal('0.00'),
            'reconciliation_level': 'M',
            'record_length': 200,
            'record_sequence_number': '000000049',
            'record_type': '500',
            'rejected_amount': Decimal('0.00'),
            'store_number': '000000050',
            'submission_date': '1114',
            'summary_type': 'POS',
            'total_records_indicator': ''
        }
    ),

    # Summary record 501:
    (
        # source:
        "000000051501200XXXXXX9963       XXXXX0120XXXXXX2919       XXXXX9834                          XXXXXX2919       XXXXX9834",
        # result:
        {
            'alternate_account_number': '',
            'alternate_routing_number': '',
            'basic_account_number': 'XXXXXX9963',
            'basic_routing_number': 'XXXXX0120',
            'deposit_account_number': 'XXXXXX2919',
            'deposit_routing_number': 'XXXXX9834',
            'exception_account_number': 'XXXXXX2919',
            'exception_routing_number': 'XXXXX9834',
            'fee_account_number': '',
            'fee_routing_number': '',
            'record_length': 200,
            'record_sequence_number': '000000051',
            'record_type': '501'
        }
    ),

    # Summary record 503:
    (
        # source:
        "000000052503200M   0000000505429XXXXXXX8100 VISA000000244950+S0000000000000-000000000000000000000000000000000000000000000000-000000000000000000000-",
        # result:
        {
            'chargeback_amount': Decimal('0.00'),
            'convenience_fee': Decimal('0.00'),
            'currency_conversion': Decimal('-0.00'),
            'division_code': '',
            'mid': '5429XXXXXXX8100',
            'net_sales_amount': Decimal('2449.50'),
            'network_discount': Decimal('0.00'),
            'network_fees': Decimal('0.00'),
            'network_id': 'VISA',
            'reconciliation_level': 'M',
            'record_length': 200,
            'record_sequence_number': '000000052',
            'record_type': '503',
            'settlement_support_indicator': 'S',
            'store_number': '000000050',
            'tax_exempt_amount': Decimal('0.00')
        }
    ),

    # Summary record 520:
    (
        # source:
        "000000095520200M1114 09171114POS   0000000485429XXXXXXX8084 000001484375+00000000000+00000000000000001484375+00000000000+000001484375+00000000000+000000000000+00000000000+00000000000+",
        # result:
        {
            'cashback_amount': Decimal('0.00'),
            'chargeback_amount': Decimal('0.00'),
            'division_code': '',
            'file_date': '1114',
            'file_submission_time': '0917',
            'interchange_fees': Decimal('0.00'),
            'mid': '5429XXXXXXX8084',
            'net_deposit_after_interchange': Decimal('0.00'),
            'net_deposit_amount': Decimal('14843.75'),
            'net_sales_amount': Decimal('14843.75'),
            'purchase_sales_amount': Decimal('14843.75'),
            'reconciliation_level': 'M',
            'record_length': 200,
            'record_sequence_number': '000000095',
            'record_type': '520',
            'return_amount': Decimal('0.00'),
            'return_surcharge_amount': Decimal('0.00'),
            'sales_surcharge_amount': Decimal('0.00'),
            'store_number': '000000048',
            'submission_date': '1114',
            'summary_type': 'POS',
            'total_records_indicator': ''
        }
    ),

    # Summary record 521:
    (
        # source:
        "000000097521200XXXXXX9963       XXXXX0120XXXXXX2919       XXXXX9834                          XXXXXX2919       XXXXX9834",
        # result:
        {
            'basic_account_number': 'XXXXXX9963',
            'basic_routing_number': 'XXXXX0120',
            'deposit_account_number': 'XXXXXX2919',
            'deposit_routing_number': 'XXXXX9834',
            'exception_account_number': 'XXXXXX2919',
            'exception_routing_number': 'XXXXX9834',
            'fee_account_number': '',
            'fee_routing_number': '',
            'record_length': 200,
            'record_sequence_number': '000000097',
            'record_type': '521'
        }
    ),

    # Summary record 522:
    (
        # source:
        "000000098522200M   00000004854292XXXXXX8084 INTR0000014000001437435000000000000000000000000000000000001437435+00000000000000000000000000000000000000-000000000000000000000000000000000000--",
        # result:
        {
            'adjustment_amount': Decimal('-0.00'),
            'cashback_amount': Decimal('0.00'),
            'division_code': '',
            'mid': '54292XXXXXX8084',
            'net_sales_amount': Decimal('14374.35'),
            'network_fees_1': Decimal('-0.0000'),
            'network_fees_1_sign': '-',
            'network_fees_2': Decimal('-0.0000'),
            'network_fees_2_sign': '-',
            'network_id': 'INTR',
            'reconciliation_level': 'M',
            'record_length': 200,
            'record_sequence_number': '000000098',
            'record_type': '522',
            'return_amount': Decimal('0.00'),
            'return_count': 0,
            'return_surcharge_amount': Decimal('0.00'),
            'return_surcharge_count': 0,
            'sale_count': 14,
            'sales_amount': Decimal('14374.35'),
            'sales_surcharge_amount': Decimal('0.00'),
            'sales_surcharge_count': 0,
            'store_number': '000000048'
        }
    ),

    # Adjustment record 720:
    (
        # source:
        "00000012872020002CZBNINT155 10172019092934XXXXXXXXXXXX5244   00000000000+0300001923554811112019164041REQ11200000180000+11142019121000029807318092743006502110000000",
        # result:
        {
            'adjustment_action': '112',
            'adjustment_amount': Decimal('1800.00'),
            'adjustment_code': '121',
            'adjustment_date': datetime.date(2019, 11, 11),
            'adjustment_number': '000019235548',
            'adjustment_record_type': '02',
            'adjustment_settlement_date': datetime.date(2019, 11, 14),
            'adjustment_time': datetime.time(16, 40, 41),
            'adjustment_transaction_disposition': '03',
            'adjustment_type': 'REQ',
            'employee_id': '110000000',
            'error_code': '000',
            'original_amount': Decimal('0.00'),
            'original_transaction_date': datetime.date(2019, 10, 17),
            'original_transaction_time': datetime.time(9, 29, 34),
            'originator': 'CZBN',
            'pan': 'XXXXXXXXXXXX5244',
            'receiver': 'INT1',
            'record_length': 200,
            'record_sequence_number': '000000128',
            'record_type': '720',
            'terminal_id': '029807318092743',
            'terminal_sequence_number': '006502',
            'token': '',
            'token_id': '',
            'transaction_type': '55'
        }
    ),

]
