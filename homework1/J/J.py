from typing import List


class Paragraph:
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

def solve(inputLines: List[str]):    
    paragraphs = []
    file_line = inputLines[0]
    docWidth, rowHeight, symbolWidth = list(map(int, file_line.strip().split()))
    currentParagraph = Paragraph()
    for index in range(1, len(inputLines)):
        file_line = inputLines[index].strip()
        if file_line == "":
            paragraphs.append(currentParagraph)
            currentParagraph = Paragraph()
        else:
            lineParts = file_line.split("(")
            for part in lineParts:
                if part.startswith("image"):
                    image = Image(part)
                    currentParagraph.content.append(image)
                elif part.strip():
                    currentParagraph.content.append(part.strip())
    
    if currentParagraph.content:
        paragraphs.append(currentParagraph)

    print(paragraphs)

def main():
    reader = open('input.txt', 'r')
    allLines = reader.readlines()
    reader.close()

    solve(allLines)

if __name__ == '__main__':
    main()