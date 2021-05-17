import datetime

class Formats:

    def dataTime_dataToView(self, value):
        return datetime.datetime.strptime(str(value), "%Y/%m/%d %H:%M:%S")