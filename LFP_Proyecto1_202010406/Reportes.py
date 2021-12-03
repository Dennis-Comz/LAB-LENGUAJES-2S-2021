import os

class Reporte:
    def __init__(self, tokenList):
        if len(tokenList.getTokens()) != 0:
            print('NO VACIO')
            self.writeFile(tokenList.getTokens())
        else:
            print('vacio')
    def writeFile(self, tokens):
        html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css" integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,900;1,900&display=swap" rel="stylesheet">
    <title>Reporte Tokens</title>
</head>
<body>
    <nav>
        <h1>TOKENS</h1>
    </nav>
    <div>
        <h1>REPORTE DE TOKENS</h1>
        <table class="table table-bordered">
            <thead class="thead-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Token</th>
                <th scope="col">Lexema</th>
                <th scope="col">Fila</th>
                <th scope="col">Columna</th>
              </tr>
            </thead>
            <tbody>\n'''

        i = 1
        for token in tokens:
            if token.tipo != 8:
                html += "\t\t\t<tr>\n"
                html += '\t\t\t\t<th scope=\"row\">' + str(i) + "</th>\n"
                html += '\t\t\t\t<td>' + str(token.getTipo()) + "</td>\n"
                html += '\t\t\t\t<td>' + str(token.getLexema()) + "</td>\n"
                html += '\t\t\t\t<td>' + str(token.getFila()) + "</td>\n"
                html += '\t\t\t\t<td>' + str(token.getColumna()) + "</td>\n"
                html += "\t\t\t</tr>\n"
                i += 1
        html += '\n\t\t</tbody>\n\t</table>\n</div>\n'
        html += '''<div>
        <h1>REPORTE DE ERRORES</h1>
        <table class="table table-bordered">
            <thead class="thead-dark">
              <tr>
                <th scope="col">#</th>
                <th scope="col">Token</th>
                <th scope="col">Lexema</th>
                <th scope="col">Fila</th>
                <th scope="col">Columna</th>
              </tr>
            </thead>
            <tbody>\n'''
        i = 1
        for token in tokens:
            if token.tipo == 8:
                html += "\t\t\t<tr>"
                html += '\t\t\t\t<th scope=\"row\">' + str(i) + "</th>\n"
                html += '\t\t\t\t<td>' + str(token.getTipo()) + "</td>\n"
                html += '\t\t\t\t<td>' + str(token.getLexema()) + "</td>\n"
                html += '\t\t\t\t<td>' + str(token.getFila()) + "</td>\n"
                html += '\t\t\t\t<td>' + str(token.getColumna()) + "</td>\n"
                html += "\t\t\t</tr>"
                i += 1
        html += '\n\t\t</tbody>\n\t</table>\n</div>\n</body>\n</html>'
        
        file = open("ReporteTokens.html", 'w')
        file.write(html)
        file.close
        os.startfile('ReporteTokens.html')
        # print(html)