import os

from config import FILE_INPUT_PREFIX
from config import FILE_INPUT_NAMES
from config import APPL_FILE_STORAGE


def create_directory(path):
    try:
        os.makedirs(path)
    except Exception as e:
        return e.__str__()

    return True


def upload(path, file, prefix):
    with open(path + "/" + prefix + str(file), "wb+") as f:
        f.write(file.read())


def upload_files(files, id):
    """
        Main function which upload files from form
        TODO: Filetype validation
        TODO: Change user unique folder creation method (rn is using csrf_token name)
        TODO: Database filename+path saving
    :param files: A list of files from HTML inputs
    :param id: csrf_token value
    :return: A dict with filenames
    """
    storage_root_path = os.getcwd() + "/" + APPL_FILE_STORAGE

    if not os.path.isdir(storage_root_path):
        create_directory(storage_root_path)

    create_directory(storage_root_path + "/" + id)
    current_user_files_path = storage_root_path + "/" + id

    filenames = {"carte_de_identitate": [], "imagine_proces_verbal": [], "imagine_chitanta_plata": [], "imagine_orice_alta_imagine": []}

    for file in files:
        # file extension
        filetype = str(files[file]).split(".")[-1]

        if str(file).__contains__(FILE_INPUT_NAMES["carte_de_identitate"]):
            filenames["carte_de_identitate"].append(id + "/" + str(files["carte_de_identitate"]))
            upload(path=current_user_files_path, file=files["carte_de_identitate"], prefix=FILE_INPUT_PREFIX["carte_de_identitate"])

        if str(file).__contains__(FILE_INPUT_NAMES["imagine_proces_verbal"]):
            filenames["imagine_proces_verbal"].append(id + "/" + str(files["imagine_proces_verbal"]))
            upload(path=current_user_files_path, file=files["imagine_proces_verbal"], prefix=FILE_INPUT_PREFIX["imagine_proces_verbal"])

        if str(file).__contains__(FILE_INPUT_NAMES["imagine_chitanta_plata"]):
            filenames["imagine_chitanta_plata"].append(id + "/" + str(files["imagine_chitanta_plata"]))
            upload(path=current_user_files_path, file=files["imagine_chitanta_plata"], prefix=FILE_INPUT_PREFIX["imagine_chitanta_plata"])

        if str(file).__contains__(FILE_INPUT_NAMES["imagine_orice_alta_imagine"]):
            count = 1
            for other_file in files.getlist("imagine_orice_alta_imagine"):
                filenames["imagine_orice_alta_imagine"].append(id + "/" + str(other_file))
                upload(path=current_user_files_path, file=other_file, prefix=FILE_INPUT_PREFIX["imagine_orice_alta_imagine"] + "_" + str(count) + "_")

    return filenames


if __name__ == '__main__':
    pass