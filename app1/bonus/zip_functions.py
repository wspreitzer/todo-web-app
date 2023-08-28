import zipfile as zf
import pathlib as pl


def make_archive(filepaths, dest_dir):
    with zf.ZipFile(pl.Path(dest_dir, "compressed.zip"), "w") as archive:
        for filepath in filepaths:
            filepath = pl.Path(filepath)
            archive.write(filepath, arcname=filepath.name)


def extract_archive(archivepath, dest_dir):
    with zf.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    make_archive(filepaths=["bonus1.py", "bonus15.py"], dest_dir="dest")
    extract_archive(pl.Path("dest", "compressed.zip"), pl.Path("dest"))
