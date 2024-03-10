from typing import List

class RowParagraph:
    def __init__(self):
        self.content = []
    
    def __repr__(self) -> str:
        return str(self.content)

class Image:
    def __init__(self, input: str):
        parameters = input[6:len(input) - 1:].split()
        self.dx = None
        self.dy = None
        for parameter in parameters:
            name, value = parameter.split("=")
            if name == "layout":
                self.layout = value
            elif name == "width":
                self.width = value
            elif name == "height":
                self.height = value
            elif name == "dx":
                self.dx = value
            elif name == "dy":
                self.dy = value
    
    def __repr__(self) -> str:
        return str(f"image: l={self.layout} w={self.width} h={self.height} dx={self.dx} dy={self.dy}")

#PARAGRAPH###############################################################
class Paragraph:
    def __init__(self, docWidth, rowHeight, symbolWidth, rowParagraphContent):
        self.width = docWidth
        self.defaulRowHeight = rowHeight
        self.symbolWidth = symbolWidth
        self.lines = List[Line]()

        for content in rowParagraphContent:
            while not self.getLastLine().canFit(content):
                self.addNewLine()
            self.getLastLine().add(content)

    def getLastLine(self):
        if len(self.lines) == 0:
            self.addNewLine()
        else:
            return self.lines[-1]
    
    def addNewLine(self):
        if len(self.lines) == 0:
            self.lines.append(Line(self.rowHeight, self.docWidth, self.symbolWidth))
        else:
            prevLine = self.getLastLine()
            prevLineFirstFragment = prevLine.fragments[0]
            newLine = Line(self.rowHeight, self.docWidth, self.symbolWidth)
            newLineCurrentFragment = Fragment(newLine, prevLineFirstFragment.width)
            for prevLineFragmentIndex in range(1, len(prevLine.fragments)):
                prevLineFragment = prevLine.fragments[prevLineFragmentIndex]
                shouldPrevLineFragmentSplitNewLine = prevLineFragment.getBottomY() > newLine.getY()
                if shouldPrevLineFragmentSplitNewLine:
                    newLine.fragments.append(newLineCurrentFragment)
                    
                else:
                    newLineCurrentFragment.width = prevLineFirstFragment.getX() - 1
        
#LINE###############################################################
class Line:
    def __init__(self, height, width, symbolWidth) -> None:
        self.height = height
        self.width = width
        self.symbolWidth = symbolWidth
        self.fragments = [Fragment(width)]
        self.lastUsedFragmentIndex = 0
    
    def canFit(self, paragraphContent):
        while self.lastUsedFragmentIndex < len(self.fragments):
            currentFragment = self.fragments[self.lastUsedFragmentIndex]
            if paragraphContent is str:
                if currentFragment.canFitText(paragraphContent, self.symbolWidth):
                    return True
            else:
                if currentFragment.canFitImage(paragraphContent):
                    return True
            self.lastUsedFragmentIndex += 1
        
        return False

#ELEMENT###############################################################
class Element:
    #types: 1 - text, 2 - image
    def __init__(self, parentFragment, type):
        self.parentFragment = parentFragment
        self.type = type

#FRAGMENT###############################################################
class Fragment:
    def __init__(self, parentLine, width):
        self.parentLine = parentLine
        self.width = width
    
    def canFitText(self, text, symbolWidth):
        if self.type == 2:
            return False
        requiredWidth = len(text) * symbolWidth
        if self.content:
            spaceWidth = symbolWidth
            usedWidth = len(self.content) * symbolWidth
            return self.width >= usedWidth + spaceWidth + requiredWidth
        else:
            return self.width > requiredWidth
        
    def canFitImage(self, image: Image):
        if image.layout == ""

def solve(inputLines: List[str]):
    docWidth, rowHeight, symbolWidth, rowParagraphs = parse(inputLines)    
  
    paragraphs = []
    for rowParagraph in rowParagraphs:
        paragraphs.append(Paragraph(docWidth, rowHeight, symbolWidth, rowParagraph.content))

    result = []
    for paragraph in paragraphs:
        result.extend(paragraph.getImages())
    return result

def findSuitablePosition(board, cursorX, currentLineY, currentLineHeight, elementWidth):
    freePixels = 0
    resultX, resultY = cursorX, currentLineY
    for i in range(cursorX, len(board[currentLineY])):
        if board[currentLineY][i] == None:
            freePixels += 1
        else:
            freePixels = 0
            resultX = i + 1
        if freePixels == elementWidth:
            return resultX, resultY
    
    return (0, currentLineY + currentLineHeight)


def parse(inputLines: List[str]) -> tuple[int, int, int, List[RowParagraph]]:    
    rowParagraphs = []
    file_line = inputLines[0]
    docWidth, rowHeight, symbolWidth = list(map(int, file_line.strip().split()))
    currentRowParagraph = RowParagraph()
    for index in range(1, len(inputLines)):
        file_line = inputLines[index].strip()
        if file_line == "":
            rowParagraphs.append(currentRowParagraph)
            currentRowParagraph = RowParagraph()
        else:
            lineParts = file_line.split("(")
            for part in lineParts:
                if part.startswith("image"):
                    image = Image(part)
                    currentRowParagraph.content.append(image)
                elif part.strip():
                    currentRowParagraph.content.append(part.strip())
    
    if currentRowParagraph.content:
        rowParagraphs.append(currentRowParagraph)

    return (docWidth, rowHeight, symbolWidth, rowParagraphs)

def main():
    reader = open('input.txt', 'r')
    allLines = reader.readlines()
    reader.close()

    results = solve(allLines)
    for result in results:
        print(f"{result[0]} {result[1]}")

if __name__ == '__main__':
    main()