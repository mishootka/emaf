from .constants import *

class EMAFParser(object):

    from .tokens import CONTROL_SECTION
    from .tokens import FILE_HEADER
    from .tokens import FILE_TRAILER
    from .tokens import BATCH_HEADER
    from .tokens import BATCH_TRAILER
    from .tokens import SUMMARY_HEADER
    from .tokens import SUMMARY_TRAILER
    from .tokens import CREDIT_RECONCILIATION_DETAIL_1
    from .tokens import CREDIT_RECONCILIATION_DETAIL_2
    from .tokens import CREDIT_RECONCILIATION_DETAIL_7
    from .tokens import CREDIT_RECONCILIATION_SUMMARY_1
    from .tokens import CREDIT_RECONCILIATION_SUMMARY_2
    from .tokens import CREDIT_RECONCILIATION_SUMMARY_4
    from .tokens import CREDIT_ADJUSTMENT_REVERSAL_1
    from .tokens import DEBIT_RECONCILIATION_DETAIL_1
    from .tokens import DEBIT_RECONCILIATION_DETAIL_2
    from .tokens import DEBIT_RECONCILIATION_SUMMARY_1
    from .tokens import DEBIT_RECONCILIATION_SUMMARY_2
    from .tokens import DEBIT_RECONCILIATION_SUMMARY_3
    from .tokens import DEBIT_ADJUSTMENT_REVERSAL_1

    VERSION = "0.0.5"

    __text = ""
    __position = 0
    __parsed = {}

    def __init__(self, text):
        self.__text = text
        self.parse()

    def __str__(self):
        return "EMAF Parser v{}".format(self.VERSION)

    def get(self, key, default=None):
        return self.__parsed.get(key, default)

    def set(self, key, value):
        self.__parsed[key] = value

    @classmethod
    def encrypt(cls, text):
        try:
            from rest.crypto import aes_encrypt
            return aes_encrypt(ENCRYPTION_KEY, text)
        except Exception as e:
            return text

    @classmethod
    def decrypt(cls, encrypted):
        try:
            from rest.crypto import aes_decrypt
            return aes_decrypt(ENCRYPTION_KEY, encrypted)
        except Exception as e:
            return encrypted

    def get_parsed(self):
        return self.__parsed

    def get_level(self):
        record_type = self.get("record_type")
        if record_type in FILE_HEADERS: return 0
        if record_type in FILE_TRAILERS: return 0
        if record_type in HIERARCHY_RECORDS: return 1
        return 2

    def parse_tokens(self, tokens):
        for token in tokens:
            length      = token.get("length")
            pos         = self.__position
            text        = self.__text[pos:pos+length]
            field_name  = token.get("field_name")
            fn          = token.get("parser")
            self.__position += length
            if not field_name: continue
            try:
                self.__parsed[field_name] = fn(self, text)
            except Exception as e:
                self.__parsed[field_name] = None

    # Parse Record Header:
    def parse_control_section(self):
        self.parse_tokens(self.CONTROL_SECTION)

    def print_me(self):
        parsed = self.get_parsed()
        prepend = "---" * self.get_level()
        print("{} {}:".format(prepend, self.get("record_type")))
        keys = parsed.keys()
        keys.sort()
        for k in keys:
            print("{} {}: '{}'".format(prepend, k, parsed.get(k)))
        print("{} {}.".format(prepend, self.get("record_type")))

    def parse(self):
        self.__position = 0
        self.__parsed = {}
        # This must be on top since it parses record_type:
        self.parse_control_section()

        record_type = self.get("record_type")

        # Pick token set based on the record_type:
        
        if record_type in FILE_HEADERS: self.parse_tokens(self.FILE_HEADER)

        if record_type == "070": self.parse_tokens(self.BATCH_HEADER)
        if record_type == "970": self.parse_tokens(self.BATCH_TRAILER)

        if record_type == "080": self.parse_tokens(self.SUMMARY_HEADER)
        if record_type == "980": self.parse_tokens(self.SUMMARY_TRAILER)

        if record_type == "300": self.parse_tokens(self.CREDIT_RECONCILIATION_DETAIL_1)
        if record_type == "301": self.parse_tokens(self.CREDIT_RECONCILIATION_DETAIL_2)
        if record_type == "306": self.parse_tokens(self.CREDIT_RECONCILIATION_DETAIL_7)
        if record_type == "500": self.parse_tokens(self.CREDIT_RECONCILIATION_SUMMARY_1)
        if record_type == "501": self.parse_tokens(self.CREDIT_RECONCILIATION_SUMMARY_2)
        if record_type == "503": self.parse_tokens(self.CREDIT_RECONCILIATION_SUMMARY_4)
        if record_type == "700": self.parse_tokens(self.CREDIT_ADJUSTMENT_REVERSAL_1)

        if record_type == "320": self.parse_tokens(self.DEBIT_RECONCILIATION_DETAIL_1)
        if record_type == "321": self.parse_tokens(self.DEBIT_RECONCILIATION_DETAIL_2)
        if record_type == "520": self.parse_tokens(self.DEBIT_RECONCILIATION_SUMMARY_1)
        if record_type == "521": self.parse_tokens(self.DEBIT_RECONCILIATION_SUMMARY_2)
        if record_type == "522": self.parse_tokens(self.DEBIT_RECONCILIATION_SUMMARY_3)
        if record_type == "720": self.parse_tokens(self.DEBIT_ADJUSTMENT_REVERSAL_1)

        if record_type in FILE_TRAILERS: self.parse_tokens(self.FILE_TRAILER)

        return self.get_parsed()



