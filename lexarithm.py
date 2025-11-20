# greek_isopsephy.py
"""
Greek Isopsephy Calculator – Full System + Step-by-Step Reduction
Features:
  • 27-letter alphabet (including Ϝ=6, Ϙ=90, ϡ=900)
  • Full lexarithm + inline digital reduction with successive =
  • Traditional Greek numeral output
"""

from typing import Dict, List, Tuple

# Full historical isopsephy table
ISOPSEPHY_TABLE: Dict[str, int] = {
    'Α':1, 'α':1, 'Ά':1,
    'Β':2, 'β':2,
    'Γ':3, 'γ':3,
    'Δ':4, 'δ':4,
    'Ε':5, 'ε':5, 'Έ':5,
    'Ϝ':6, 'ϝ':6, 'F':6, 'f':6, 'Ϛ':6, 'ϛ':6,   # Digamma / Stigma
    'Ζ':7, 'ζ':7,
    'Η':8, 'η':8, 'Ή':8,
    'Θ':9, 'θ':9,
    'Ι':10, 'ι':10, 'Ί':10, 'Ϊ':10,
    'Κ':20, 'κ':20,
    'Λ':30, 'λ':30,
    'Μ':40, 'μ':40,
    'Ν':50, 'ν':50,
    'Ξ':60, 'ξ':60,
    'Ο':70, 'ο':70, 'Ό':70,
    'Π':80, 'π':80,
    'Ϙ':90, 'ϙ':90, 'Q':90, 'q':90,            # Qoppa
    'Ρ':100, 'ρ':100,
    'Σ':200, 'σ':200, 'ς':200,
    'Τ':300, 'τ':300,
    'Υ':400, 'υ':400, 'Ύ':400, 'Ϋ':400,
    'Φ':500, 'φ':500,
    'Χ':600, 'χ':600,
    'Ψ':700, 'ψ':700,
    'Ω':800, 'ω':800, 'Ώ':800,
    'Ϡ':900, 'ϡ':900,                          # Sampi
}

def isopsephy_value(word: str) -> int:
    return sum(ISOPSEPHY_TABLE.get(ch.upper(), 0) for ch in word if ch.upper() in ISOPSEPHY_TABLE)

def isopsephy_breakdown(word: str) -> List[Tuple[str, int]]:
    return [(ch, ISOPSEPHY_TABLE[ch.upper()]) for ch in word if ch.upper() in ISOPSEPHY_TABLE]

def reduction_steps(n: int) -> str:
    """Return string like '888 = 8+8+8 = 24 = 2+4 = 6'"""
    if n <= 9:
        return str(n)
    
    steps = [str(n)]
    current = n
    
    while current > 9:
        digits = [int(d) for d in str(current)]
        step = "+".join(map(str, digits))
        current = sum(digits)
        steps.append(step)
        steps.append(str(current))
    
    return " = ".join(steps)

def to_greek_numeral(n: int) -> str:
    if n <= 0:
        return "0"
    thousands = {1:'͵α',2:'͵β',3:'͵γ',4:'͵δ',5:'͵ε',6:'͵ϝ',7:'͵ζ',8:'͵η',9:'͵θ'}
    units = {
        1:'α',2:'β',3:'γ',4:'δ',5:'ε',6:'ϝ',7:'ζ',8:'η',9:'θ',
        10:'ι',20:'κ',30:'λ',40:'μ',50:'ν',60:'ξ',70:'ο',80:'π',90:'ϙ',
        100:'ρ',200:'σ',300:'τ',400:'υ',500:'φ',600:'χ',700:'ψ',800:'ω',900:'ϡ'
    }
    s = ""
    if n >= 1000:
        s += thousands.get(n // 1000, "")
        n %= 1000
    for val in sorted(units.keys(), reverse=True):
        while n >= val:
            s += units[val]
            n -= val
    return s + (" " if len(s) > 1 else "")

def analyze(word: str) -> dict:
    letters = isopsephy_breakdown(word)
    total = sum(v for _, v in letters)
    breakdown = " + ".join(f"[{ch}={v}]" for ch, v in letters)
    full_chain = f"{breakdown} = {reduction_steps(total)}" if letters else "0"
    
    return {
        "word": word,
        "total": total,
        "chain": full_chain,
        "greek_numeral": to_greek_numeral(total)
    }

# CLI
def main():
    print("\nὙπολογιστήρας\n")

    while True:
        word = input("Εἰσάγετε την λέξιν (ἤ 'q'): ").strip()
        if word.lower() in {"quit", "exit", "q", ""}:
            print("\nΧαῖρε!\n")
            break

        data = analyze(word)

        if data["total"] == 0:
            print("No valid Greek letters found.\n")
            continue

        print(f"\n{data['word'].upper()} = {data['chain'].upper()}\n")
        # print(f"  → {data['greek_numeral']}\n")

if __name__ == "__main__":
    main()
