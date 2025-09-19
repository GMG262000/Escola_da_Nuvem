# Variavel que armazena insulina Humana
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

print("Sequecias pré-pró-insulina: ")
print(preproInsulin)
print("Comprimento da sequencia: ", len(preproInsulin), "caracteres\n")

lsInsulina = "malwmrllpllallalwgpdpaaa"
bInsulina = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulina = "giveqcctsicslyqlenycn"
cInsulina = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulina = bInsulina + aInsulina 
print("Sequencia LS: ", lsInsulina, "tamanho", len(lsInsulina))
print("///*********************///")
print("Sequencia A: ", aInsulina, "tamanho", len(aInsulina))
print("///*********************///")
print("Sequencia B: ", bInsulina, "tamanho", len(bInsulina))
print("///*********************///")
print("Sequencia C: ", cInsulina, "tamanho", len(cInsulina))
print("///*********************///", "\n")

print("Sequencia da insulina (B + A): ")
print(insulina)
print("Comprimento da insulina:", len(insulina), "caracteres\n")