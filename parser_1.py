import sys
from pathlib import Path


JPEG_IMAGES = []
PNG_IMAGES = []
JPG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOC = []
DOCX_DOC = []
TXT_DOC = []
PDF_DOC = []
XLSX_DOC = []
PPTX_DOC = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
OTHER_FILES = []

REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOC,
    'DOCX': DOCX_DOC,
    'TXT': TXT_DOC,
    'PDF': PDF_DOC,
    'XLSX': XLSX_DOC,
    'PPTX': PPTX_DOC,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,

}

FOLSERS = []
EXTENSIONS = set()
UNKNOWN = set()

def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()

def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER_FILES'):
                FOLSERS.append(item)
                scan(item)
            continue
        extension = get_extension(item.name)
        full_name = folder / item.name

        if not extension:
            OTHER_FILES.append(full_name)
        else:
            try:
                ext_reg = REGISTER_EXTENSION[extension]
                ext_reg.append(full_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER_FILES.append(full_name)

if __name__ == '__main__':
     folder_process = sys.argv[1]
     scan(Path(folder_process))
     print(f'Images jpeg: {JPEG_IMAGES}')
     print(f'Images jpg: {JPG_IMAGES}')
     print(f'UNKNOWN jpg: {UNKNOWN}')
     print(f'EXTENSIONS jpg: {EXTENSIONS}')
     print(f'FOLSERS jpg: {FOLSERS}')
