import math
class CreateTable:
    def __init__(self, header, rows, intColumns):
        self.__header = header
        self.__rows = rows
        self.__intColumns = intColumns
        self.__dicHighs = {}
        self.tab = 4

        self.__width = 0

    def initDicHighs(self):
        for i in range(self.__intColumns):
            self.__dicHighs[i] = int(i)
        return True

    def getStrHighs(self):
        self.initDicHighs()
        for i in range(len(self.__rows)):
            for j in range(len(self.__rows[i])):
                if self.__dicHighs[j] < len(self.__rows[i][j]):
                    self.__dicHighs[j] = len(self.__rows[i][j])
        return


    def getBodyArray(self):
        content = []
        for row in self.__rows:
            colIndex = 0
            column = []
            for item in row:
                element = self.formattedElement(item, colIndex)
                column.append(element)
                colIndex +=1
            content.append(column)
        self.__width = self.getWidth(content[0])
        return content

    def getWidth(self, row):
        count = 0
        for col in row:
            count += len(col)
        return count


    def getHeaderArray(self):

        spaces = math.ceil(self.__width/2 - len(self.__header)/2)
        return ["%s%s%s"%(" "*spaces, self.__header, " "*spaces)]



    def formattedElement(self, item, colIndex):
        spaces = self.__dicHighs[colIndex]+ self.tab - len(str(item))
        return "|%s%s"%(item," "*spaces)


    def printTable(self):
        self.initDicHighs()
        self.getStrHighs()
        array = self.getBodyArray()
        header = self.getHeaderArray()

        print(header)

        for row in array:
            print("".join(row))

    def createTable(self):
        self.initDicHighs()
        self.getStrHighs()
        body = self.getBodyArray()
        header = self.getHeaderArray()

        lines = "%s\n"%("-"* len("".join(header)))

        content= "%s%s\n%s"%(lines,"".join(header),lines)
        for row in body:
            content += "%s|"% "".join(row)
            content += "\n%s"%lines
        return content
