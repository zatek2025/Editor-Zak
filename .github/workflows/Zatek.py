def interpretar_zak(codigo):
    variaveis = {}
    linhas = codigo.strip().split("\n")
    i = 0

    while i < len(linhas):
        linha = linhas[i].strip()

        if linha.startswith("diga "):
            msg = linha[5:].strip().strip('"')
            print(msg)

        elif linha.startswith("crie "):
            partes = linha.split("com")
            nome = partes[0].replace("crie", "").strip()
            valor = partes[1].strip().strip('"')
            # Tenta converter para número, senão deixa como string
            try:
                valor = int(valor)
            except:
                pass
            variaveis[nome] = valor

        elif linha.startswith("se "):
            condicao = linha[3:].split("então")[0].strip()
            nome_var, operador, valor = condicao.split()
            valor = int(valor)
            cond_ok = False

            if operador == "maior" and variaveis[nome_var] > valor:
                cond_ok = True
            elif operador == "menor" and variaveis[nome_var] < valor:
                cond_ok = True
            elif operador == "igual" and variaveis[nome_var] == valor:
                cond_ok = True

            bloco = []
            i += 1
            while not linhas[i].strip() == "fim":
                bloco.append(linhas[i])
                i += 1
            if cond_ok:
                interpretar_zak("\n".join(bloco))

        elif linha.startswith("repita "):
            partes = linha.split()
            vezes = int(partes[1])
            bloco = []
            i += 1
            while not linhas[i].strip() == "fim":
                bloco.append(linhas[i])
                i += 1
            for _ in range(vezes):
                interpretar_zak("\n".join(bloco))

        i += 1
