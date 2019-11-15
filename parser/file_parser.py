from .emaf_parser import EMAFParser
from .constants import *


class EMAFFileParser(object):

    VERSION = "0.0.5"

    def __init__(
            self, 
            file, 
            callback_batch=None, 
            callback_transaction=None, 
            callback_summary=None, 
            callback_adjustment=None
        ):

        if callback_batch:          self.callback_batch = callback_batch
        if callback_transaction:    self.callback_transaction = callback_transaction
        if callback_summary:        self.callback_summary = callback_summary
        if callback_adjustment:     self.callback_adjustment = callback_adjustment
        self.parse(file)


    # use the following methods to utilize the parsed records
    @classmethod
    def callback_batch(cls, data):  # called when a batch record is parsed
        print("Override Batch Callback")

    @classmethod
    def callback_transaction(cls, data):  # called when a batch transaction record is parsed
        print("Override Batch Transaction Callback")

    @classmethod
    def callback_adjustment(cls, data):  # called when a batch adjustment record is parsed
        print("Override Batch Adjustment Callback")

    @classmethod
    def callback_summary(cls, data):  # called when a summary record is parsed
        print("Override Summary Callback")


    @classmethod
    def parse(cls, file):
        line = True
        while line:
            line = file.readline().strip()
            if not line: continue

            parser = EMAFParser(line)
            parsed = parser.get_parsed()
            record_type = parsed.get("record_type")

            if not record_type:
                print("can't seem to locate record type in this:")
                print(line)
                continue

            if record_type in FILE_HEADERS:
                FILE_SUMMARIES = {}
                continue


            if record_type in FILE_TRAILERS:
                # nothing to do here
                continue


            if record_type in BATCH_HEADERS:
                BATCH = parsed
                BATCH_TRANSACTIONS = {}
                BATCH_ADJUSTMENTS = {}
                continue


            if record_type in BATCH_TRAILERS:
                BATCH.update(parsed)
                cls.callback_batch(BATCH)

                for record_type in BATCH_TRANSACTIONS.keys():
                    for data in BATCH_TRANSACTIONS.get(record_type):
                        cls.callback_transaction(data)

                for record_type in BATCH_ADJUSTMENTS.keys():
                    for data in BATCH_ADJUSTMENTS.get(record_type):
                        cls.callback_adjustment(data)

                BATCH = None
                BATCH_TRANSACTIONS = {}
                BATCH_ADJUSTMENTS = {}
                continue


            if record_type in SUMMARY_HEADERS:
                # nothing to do here
                continue


            if record_type in SUMMARY_TRAILERS:
                for record_type in FILE_SUMMARIES.keys():
                    for data in FILE_SUMMARIES.get(record_type):
                        cls.callback_summary(data)
                FILE_SUMMARIES = {}
                continue


            if record_type in RECONCILIATION_DETAIL_RECORDS:
                # merge additional records into the parent:
                parent_code = cls.get_parent_code(record_type)
                if not BATCH_TRANSACTIONS.get(parent_code):
                    BATCH_TRANSACTIONS[parent_code] = []

                if record_type == parent_code:
                    # append record if it's parent
                    BATCH_TRANSACTIONS[parent_code].append(parsed)
                else:
                    # update parent record if it's child
                    l = len(BATCH_TRANSACTIONS[parent_code])
                    BATCH_TRANSACTIONS[parent_code][l-1].update(parsed)
                continue


            if record_type in RECONCILIATION_SUMMARY_RECORDS:
                parent_code = cls.get_parent_code(record_type)
                if not FILE_SUMMARIES.get(parent_code):
                    FILE_SUMMARIES[parent_code] = []

                FILE_SUMMARIES[parent_code].append(parsed)

                if record_type == parent_code:
                    FILE_SUMMARIES[parent_code].append(parsed)
                else:
                    l = len(FILE_SUMMARIES[parent_code])
                    FILE_SUMMARIES[parent_code][l-1].update(parsed)
                continue


            if record_type in ADJUSTMENT_DETAIL_RECORDS:
                parent_code = cls.get_parent_code(record_type)
                if not BATCH_ADJUSTMENTS.get(parent_code):
                    BATCH_ADJUSTMENTS[parent_code] = []

                if record_type == parent_code:
                    BATCH_ADJUSTMENTS[parent_code].append(parsed)
                else:
                    l = len(BATCH_ADJUSTMENTS[parent_code])
                    BATCH_ADJUSTMENTS[parent_code][l-1].update(parsed)
                continue

            print("!!! WARNING !!! RECORD IS NOT PARSED !!!")
            print(line)


    @classmethod
    def get_parent_code(cls, code):
        for n in MERGE_RECORDS:
            if code in n: return n[0]
        return code

