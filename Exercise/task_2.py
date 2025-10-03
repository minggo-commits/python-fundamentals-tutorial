def function_4(n:int)-> list:
    """
    Task:
    Buat fungsi untuk menghasilkan
    deret Fibonacci sepanjang n
    Contoh (5) = [0, 1, 1, 2, 3]
    """
    #TODO: lengkapi fungsi dibawah ini
    
    results = []
    a, b = 0, 1
    for _ in range(n):
        results.append(a)
        a, b = b, a + b
    return results
    pass