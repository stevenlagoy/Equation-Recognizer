"""
Reconstruct a mathematical expression from classified characters.
"""

def characters_to_expression(characters: list[str]) -> str:
    """Join ordered, classified characters into a plain-text expression.

    Args:
        characters: Recognized characters in left-to-right order.

    Returns:
        A plain-text mathematical expression, e.g. "2x+5=15".
    """
    return "".join(characters)

def expression_to_latex(expression: str) -> str:
    """Convert a plain-text expression into a LaTeX string.

    Starts with a simple symbol substitution; will need to handle
    spatial notation (exponents, fractions, roots) as an extension.
    """
    substitutions = {
        "times": r"\times",
        "div": r"\div",
        "leq": r"\leq",
        "geq": r"\geq",
        "lt": "<",
        "gt": ">",
    }
    latex = expression
    for token, replacement in substitutions.items():
        latex = latex.replace(token, replacement)
    return f"${latex}$"
