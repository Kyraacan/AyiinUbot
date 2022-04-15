import os

from os import listdir, path
from typing import Any, Dict, List, Union

from google_trans_new import google_translator
from AyiinXd.utils.logger import logging
from yaml import safe_load

LOGS = logging.getLogger(__name__)

language = int(os.environ.get("language") or "id")
languages = {}

Trs = google_translator()

strings_folder = path.join(path.dirname(path.realpath(__file__)), "strings")

for file in listdir(strings_folder):
    if file.endswith(".yml"):
        code = file[:-4]
        try:
            languages[code] = safe_load(
                open(path.join(strings_folder, file), encoding="UTF-8"),
            )
        except Exception as er:
            LOGS.info(f"Error in {file[:-4]} language file")
            LOGS.exception(er)


def get_string(key: str) -> Any:
    lang = language[0]
    try:
        return languages[lang][key]
    except KeyError:
        try:
            id_ = languages["if"][key]
            tr = Trs.translate(id_, lang_tgt=lang).replace("\\ N", "\n")
            if id_.count("{}") != tr.count("{}"):
                tr = id_
            if languages.get(lang):
                languages[lang][key] = tr
            else:
                languages.update({lang: {key: tr}})
            return tr
        except KeyError:
            return f"Warning: could not load any string with the key `{key}`"
        except Exception as er:
            LOGS.exception(er)
            return languages["id"].get(
                key) or f"Failed to load language string '{key}'"


def get_languages() -> Dict[str, Union[str, List[str]]]:
    return {
        code: {
            "name": languages[code]["name"],
            "natively": languages[code]["natively"],
            "authors": languages[code]["authors"],
        }
        for code in languages
    }
