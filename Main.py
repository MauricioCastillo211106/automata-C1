class AFD:
    def __init__(self):
        # Define los estados del AFD
        self.states = ["q0", "q1", "q2"]
        
        # Define el estado inicial
        self.initial_state = "q0"
        
        # Define los estados finales
        self.final_states = ["q2"]
        
        # Define las transiciones del AFD
        self.transitions = {
            ("q0", "0"): "q1",
            ("q1", "0"): "q1",
            ("q1", "1"): "q1",
            ("q1", "0"): "q2",
            ("q2", "0"): "q2",
            ("q2", "1"): "q2",
        }
        
    def accepts(self, word):
        # Establece el estado actual como el estado inicial
        current_state = self.initial_state
        
        # Recorre cada símbolo de la palabra
        for symbol in word:
            # Obtiene el estado de destino mediante la transición
            current_state = self.transitions.get((current_state, symbol))
            
            # Si no hay transición, la palabra no es aceptada
            if current_state is None:
                return False
        
        # Si el estado actual es un estado final, la palabra es aceptada
        if current_state in self.final_states:
            return True
        else:
            return False

# Crea el AFD
afd = AFD()

# Prueba el AFD con algunas palabras
print(afd.accepts("0"))  # imprime False
print(afd.accepts("00"))  # imprime True
print(afd.accepts("01"))  # imprime False
print(afd.accepts("010"))  # imprime True
print(afd.accepts("0101"))  # imprime False