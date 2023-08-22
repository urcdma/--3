import ast
from typing import List, Tuple

class CodeAnalyzer:
    def __init__(self):
        self.comments = []

    def parse_code(self, code: str) -> None:
        """
        Parse the uploaded Python code using ast
        """
        self.tree = ast.parse(code)

    def generate_comments(self) -> None:
        """
        Generate comments for each line or block of code
        """
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                self.comments.append((node.lineno, f"Function {node.name} defined here"))
            elif isinstance(node, ast.If):
                self.comments.append((node.lineno, "If statement starts here"))
            elif isinstance(node, ast.For):
                self.comments.append((node.lineno, "For loop starts here"))
            elif isinstance(node, ast.While):
                self.comments.append((node.lineno, "While loop starts here"))
            elif isinstance(node, ast.Import):
                self.comments.append((node.lineno, "Import statement here"))
            elif isinstance(node, ast.Assign):
                self.comments.append((node.lineno, "Assignment statement here"))

    def display_code(self, code: str) -> List[Tuple[int, str, str]]:
        """
        Display the parsed code with comments
        """
        lines = code.split('\n')
        result = []
        for i, line in enumerate(lines, start=1):
            comment = next((c for n, c in self.comments if n == i), "")
            result.append((i, line, comment))
        return result
