
# EMAF Record Type Identifiers

FILE_HEADER_CREDIT              = "010"
FILE_HEADER_DEBIT               = "020"
FILE_TRAILER_CREDIT             = "910"
FILE_TRAILER_DEBIT              = "920"

FILE_HEADERS = [
    FILE_HEADER_CREDIT,
    FILE_HEADER_DEBIT,
]
FILE_TRAILERS = [
    FILE_TRAILER_CREDIT,
    FILE_TRAILER_DEBIT,
]

FILE_RECORDS                        = FILE_HEADERS + FILE_TRAILERS
BATCH_HEADERS                       = ["070"]
BATCH_TRAILERS                      = ["970"] 
SUMMARY_HEADERS                     = ["080"]
SUMMARY_TRAILERS                    = ["980"] 
RECONCILIATION_DETAIL_RECORDS       = ["300","301","306","320","321"]
RECONCILIATION_SUMMARY_RECORDS      = ["500","501","503","520","521","522"]
ADJUSTMENT_DETAIL_RECORDS           = ["700","720","721"]

# This is used to merge records into one
# from right into the leftmost (index 0)
# e.g. 301 and 306 will be merged into 
# the preceding "300" record:
MERGE_RECORDS = [
    ["010","910"],
    ["020","920"],
    ["070","970"],
    ["080","980"],
    ["300","301","306"],
    ["320","321"],
    ["500","501","503"],
    ["520","521","522"],
    ["720","721"],
]

LEVELS = [
    ["010","020"],
    ["070","080"],
]

