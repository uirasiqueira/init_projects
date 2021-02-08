from mysq import creat_cone, close_cone


def insere_usuario(conec, IdFunc, nome, endereço, cep):
    cursor = conec.cursor()
    dados = "INSERT INTO funcionarios(IdFunc, nome, endereço, cep) values (%s, %s, %s, %s)"
    val = (IdFunc, nome, endereço, cep)
    cursor.execute(dados, val)
    cursor.close()
    conec.commit()

def main():
    con = creat_cone("localhost", "root", "", "taxi")

    insere_usuario(con, "127323", "Gaara", "Aldeia da areia, 12", "34122")

    close_cone(con)


if __name__ == "__main__":
    main()


