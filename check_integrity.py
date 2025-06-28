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