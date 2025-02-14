def potencia(x, y):
    if y < 0:
        p = 0 - y
    else:
        p = y
    z = 1.0
    while p != 0:
        z = z * x
        p = p - 1
    if y < 0:
        z = 1 / z
    return z

# Casos de teste
def test_potencia():
    # Caminho 1
    assert potencia(2.0, 0.0) == 1.0, "Teste 1 falhou"
    
    # Caminho 2
    assert potencia(2.0, 0.0) == 1.0, "Teste 2 falhou"
    
    # Caminho 3
    assert potencia(2.0, -2.0) == 0.25, "Teste 3 falhou"
    
    # Caminho 4
    assert potencia(2.0, 3.0) == 8.0, "Teste 4 falhou"

    print("Todos os testes passaram!")

test_potencia()