from pathlib import Path
import shutil
import sys
import parser_1
from normalazi import normalize

def handle_media(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    file_name.replace(target_folder / normalize(file_name.name))

def handle_archive(file_name: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / normalize(file_name.name.replace(file_name.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(file_name.absolute(), str(folder_for_file.absolute())))
    except shutil.ReadError:
        folder_for_file.rmdir()
        return
    file_name.unlink()

def main(folder: Path):
    parser_1.scan(folder)
    for file in parser_1.JPEG_IMAGES:
        handle_media(file, folder / 'images' / 'JPEG')
    for file in parser_1.JPG_IMAGES:
        handle_media(file, folder / 'images' / 'JPG')
    for file in parser_1.PNG_IMAGES:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser_1.SVG_IMAGES:
        handle_media(file, folder / 'images' / 'SVG')

    for file in parser_1.AVI_VIDEO:
        handle_media(file, folder / 'video' / 'AVI')
    for file in parser_1.MP4_VIDEO:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser_1.MOV_VIDEO:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser_1.MKV_VIDEO:
        handle_media(file, folder / 'video' / 'MKV')

    for file in parser_1.DOC_DOC:
        handle_media(file, folder / 'documents' / 'DOC')
    for file in parser_1.DOCX_DOC:
        handle_media(file, folder / 'documents' / 'DOCX')
    for file in parser_1.TXT_DOC:
        handle_media(file, folder / 'documents' / 'TXT')
    for file in parser_1.PDF_DOC:
        handle_media(file, folder / 'documents' / 'PDF')
    for file in parser_1.XLSX_DOC:
        handle_media(file, folder / 'documents' / 'XLSX')
    for file in parser_1.PPTX_DOC:
        handle_media(file, folder / 'documents' / 'PPTX')

    for file in parser_1.MP3_AUDIO:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser_1.OGG_AUDIO:
        handle_media(file, folder / 'audio' / 'OGG')
    for file in parser_1.WAV_AUDIO:
        handle_media(file, folder / 'audio' / 'WAV')
    for file in parser_1.AMR_AUDIO:
        handle_media(file, folder / 'audio' / 'AMR')

    for file in parser_1.ZIP_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'ZIP')
    for file in parser_1.GZ_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'GZ')
    for file in parser_1.TAR_ARCHIVES:
        handle_archive(file, folder / 'archives' / 'TAR')

    for file in parser_1.OTHER_FILES:
        handle_media(file, folder / 'OTHER_FILES')

    for folder in parser_1.FOLSERS[::1]:
        try:
            folder.mkdir()
        except OSError:
            print(f'Error during remove folder {folder}')

if __name__ == '__main__':
    folder_process = Path(sys.argv[1])
    main(folder_process)