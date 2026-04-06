@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    # ERRO INTENCIONAL: trocar + por -
    return {"resultado": a - b}