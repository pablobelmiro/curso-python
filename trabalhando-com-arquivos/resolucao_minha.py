from pathlib import Path
import shutil
import random

root_path = Path(__file__).parent
archive_path = root_path / 'arquivo_desafios'
sort_path = root_path / 'sort_path'
bkp_path = root_path / 'bkp_path'


if not sort_path.exists():
    sort_path.mkdir()

if not bkp_path.exists():
    bkp_path.mkdir()


for archive in archive_path.glob('**/*'):
    if archive.is_file():
        sort_path_ext = sort_path / archive.suffix.replace('.', '')
        if not sort_path_ext.exists():
            sort_path_ext.mkdir()

        shutil.move(archive, sort_path_ext / archive.name)


seed_value = 10000
random.seed(seed_value)
bkp_name = f"backup_{seed_value}"
shutil.make_archive(bkp_path / bkp_name, 'zip', sort_path)
