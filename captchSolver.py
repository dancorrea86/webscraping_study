from PIL import Image # import o MÓDULO Imagem da biblioteca PIL

im = Image.open("puppy.jpg", "r") # Importa a imagem 
pix_val = list(im.getdata()) # Retorna os dados da imagem com uma seguencia dos Pixels em RGB
print(pix_val) # Print a sequencia dos pixels