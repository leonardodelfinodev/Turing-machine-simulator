# MdT = ( S, s0, F, A, β, δ )
# S -> finite, non-empty, set of states
# s0 -> initial state (s0 ∈ S)
# F -> set of accepting final states
# A -> finite, non-empty set of the tape alphabet "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^-{|}"
# β -> blank symbol
# δ -> transition function: δ : (S x A) -> S x A x {<, >, #}
class TuringMachine(object):

    def __init__(self, instructions):
        self.instructions = instructions
