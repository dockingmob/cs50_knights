from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Can Either be a Knigth orKnave
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight),AKnave)),
    #Can not be both a Knight and a Knave
    Biconditional(AKnave, Not(And(AKnave, AKnight))),
    Biconditional(AKnight, And(AKnave, AKnight)),


)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Either A is a knight or knave and not both
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight),AKnave)),
    #Either B is a knight or knave and not both
    Or(And(BKnave, Not(BKnight)), And(Not(BKnave),BKnight)),
    # A says "We are both knaves"
    Biconditional(AKnight, And(AKnave, BKnave)),
    Biconditional(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Either A is a knight or knave and not both
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight),AKnave)),
    #Either B is a knight or knave and not both
    Or(And(BKnave, Not(BKnight)), And(Not(BKnave),BKnight)),
    # A saya "We are the same kind"
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),
    Biconditional(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    # B says "We are of different kinds"
    Biconditional(BKnight, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))),
    Biconditional(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave)))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Either A is a knight or knave and not both
    Or(And(AKnight, Not(AKnave)), And(Not(AKnight),AKnave)),
    #Either B is a knight or knave and not both
    Or(And(BKnave, Not(BKnight)), And(Not(BKnave),BKnight)),


)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
