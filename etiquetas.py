import pandas as pd

df = pd.read_csv('teste.csv', sep=';', encoding='cp1252')

counter = 1

html = ''

etiqueta = '''
                    <div>
                        <div style="width:70mm; height:1.5mm;"></div>
                        <table allign="center" cellpadding="0" cellspacing="0"  style="border-collapse: collapse;">
                            <tr>
                                <td style="width:22.5mm; height:10.5mm"></td>
                                    <td style="width:6mm; height:8.5mm; text-align:left;vertical-align:top;line-height:8.5mm;">
                                    <div style="width:6mm; height:8.5mm;">
                                        <p class="currency">R$</p>
                                    </div>
                                </td>
                                <td style="width:41.5mm; height:8.5mm; ">
                                    <div style="width:41.5mm; height:8.5mm; ">
                                        <p class="price">$price</p>
                                    </div>
                                </td>
                            </tr>
                        </table>
                        <div class="container_description" style="width:70mm; height:18mm;">
                            <div class="container_description">
                                <div class="description">$description</div>
                            </div>
                        </td>
                    </div>
'''

with open('etiquetas.html', 'r') as f:
    html = f.read();

with open('saida.html', 'w') as f:
    for index, row in df.iterrows():
        html = html.replace('$tag', etiqueta, 1)
        html = html.replace('$description', row['Descrição'],1)
        html = html.replace('$price', row['Preço'],1)
        counter = counter + 1
        if counter == 24:
            break
    html = html.replace('$tag', '')
    f.write(html)

print('Dones')
