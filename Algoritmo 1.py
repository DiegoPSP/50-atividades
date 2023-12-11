def criar_lista_html(elementos):
    # Inicializa a string HTML com a tag de lista não ordenada
    html = "<ul>\n"

    # Adiciona cada elemento à lista HTML
    for elemento in elementos:
        html += f"  <li>{elemento}</li>\n"

    # Fecha a tag de lista não ordenada
    html += "</ul>"

    return html

# Exemplo de uso
elementos = ["Item 1", "Item 2", "Item 3", "Item 4"]
html_resultante = criar_lista_html(elementos)

# Imprime o HTML resultante
print(html_resultante)
