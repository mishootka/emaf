from files import Directory
from parser import EMAFFileParser


class MyEMAFFileParser(EMAFFileParser):

    @classmethod
    def callback_batch(cls, data):  # called when a batch record is parsed
        print("Look mom, new batch!")

    @classmethod
    def callback_transaction(cls, data):  # called when a batch transaction record is parsed
        print("Look mom, new batch transaction!")

    @classmethod
    def callback_adjustment(cls, data):  # called when a batch adjustment record is parsed
        print("Look mom, new batch Adjustment!")

    @classmethod
    def callback_summary(cls, data):  # called when a summary record is parsed
        print("Look mom, new summary!")
        

if __name__ == "__main__":
    directory = Directory("./data")
    directory.each_file(MyEMAFFileParser.parse)

