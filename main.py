import PyPDF2
import os

merger = PyPDF2.PdfMerger()

listar_arquivos = os.listdir("MesclarPDF/arquivos")
listar_arquivos.sort()
print(listar_arquivos)

for arquivo in listar_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"MesclarPDF/arquivos/{arquivo}")

caminho_final_pdf = os.path.join("MesclarPDF_RPA", "Final.pdf")
merger.write(caminho_final_pdf)
merger.close