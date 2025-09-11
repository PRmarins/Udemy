import os

def encontrar_exercicios_por_tags(diretorio_base, tags_buscadas):
    """
    Procura por arquivos Python (.py) em subpastas que contenham as tags especificadas.

    Args:
        diretorio_base (str): O caminho da pasta mãe a ser pesquisada.
        tags_buscadas (list): Uma lista de tags a serem procuradas.
    """
    exercicios_encontrados = []
    
    # Converte as tags buscadas para minúsculas para uma busca case-insensitive
    tags_buscadas = [tag.lower() for tag in tags_buscadas]
    
    print(f"Buscando exercícios com as tags: {', '.join(tags_buscadas)}\n")

    # Itera sobre todos os arquivos e diretórios dentro do diretório base
    for raiz, _, arquivos in os.walk(diretorio_base):
        for arquivo in arquivos:
            # Verifica se o arquivo é um arquivo Python
            if arquivo.endswith(".py"):
                caminho_completo = os.path.join(raiz, arquivo)
                
                try:
                    # Abre o arquivo para ler a primeira linha
                    with open(caminho_completo, 'r', encoding='utf-8') as f:
                        primeira_linha = f.readline().strip()
                        
                        # Verifica se a primeira linha é um comentário de tags
                        if primeira_linha.startswith("# tags:"):
                            # Extrai as tags do arquivo
                            tags_do_arquivo = [tag.strip().lower() for tag in primeira_linha[len("# tags:"):].split(',')]
                            
                            # Verifica se todas as tags buscadas estão no arquivo
                            if all(tag in tags_do_arquivo for tag in tags_buscadas):
                                exercicios_encontrados.append(caminho_completo)
                                
                except Exception as e:
                    print(f"Erro ao ler o arquivo {caminho_completo}: {e}")

    return exercicios_encontrados

if __name__ == "__main__":
    # Define o diretório base como o diretório onde o script está sendo executado
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    # Solicita ao usuário as tags a serem buscadas
    tags_input = input("Digite as tags que você quer buscar (separadas por vírgula): ")
    
    # Divide a entrada do usuário em uma lista de tags e remove espaços extras
    tags_usuario = [tag.strip() for tag in tags_input.split(',')]

    # Encontra os exercícios
    resultados = encontrar_exercicios_por_tags(diretorio_atual, tags_usuario)

    # Exibe os resultados
    if resultados:
        print("---")
        print("Exercícios encontrados:")
        for exercicio in resultados:
            print(f"- {exercicio}")
    else:
        print("---")
        print("Nenhum exercício encontrado com as tags especificadas.")