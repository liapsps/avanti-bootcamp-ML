import os
import xml.etree.ElementTree as ET

xml_path = "archive/annotations.xml"

images_folder = "archive/images"

tree = ET.parse(xml_path)
root = tree.getroot()

xml_images = [img.attrib['name'].split('/')[-1] for img in root.findall(".//image")]

missing = []
for name in xml_images:
    img_path = os.path.join(images_folder, name)
    if not os.path.exists(img_path):
        missing.append(name)

print(f"Total de imagens referenciadas no XML: {len(xml_images)}")
if missing:
    print(f"{len(missing)} imagem(ns) estão faltando:")
    for m in missing:
        print(f" - {m}")
else:
    print("Todas as imagens do XML existem na pasta de imagens.")

extensions_xml = set()
for name in xml_images:
    base_name, ext = os.path.splitext(name)
    extensions_xml.add(ext.lower())

print(f'Extensões encontradas nas imagens no XML: {extensions_xml}')

extensions_folder = set()
for archive in os.listdir(images_folder):
    if os.path.isfile(os.path.join(images_folder, archive)):
        base_name, ext = os.path.splitext(archive)
        extensions_folder.add(ext.lower())

print(f'Extensões encontradas na pasta de imagens: {extensions_folder}')