def function_1(a: int, b:int) -> int:
    """
    Task:
    Buat fungsi untuk perkalian dua bilangan
    Conotoh:
    function_1 (3, 4) -> 12
    """
    # TODO: lengkapi fungsi ini
    return a*b
    pass  

def function_2(n: int) -> bool:
    """
    Buat fungsi untuk mengecek apakah angka geanap,
    Return jika True genap dan False jik ganjil
    """
    # TODO: lengkapi fungsi ini
    if n % 2 == 0:
        return True
    else:
        return False
    pass

def function_3(n: int) -> list:
    """
    Buat fungsi untuk mengembalikan semua faktor dari n,
    contoh 6 = [1, 2, 3, 6]
    """
    #TODO: lengkapi fungsi ini
    result = []
    for i in range(1 , n+1):
        if n % i == 0:
            result.append(i)
    return result       
    pass
    
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
    
