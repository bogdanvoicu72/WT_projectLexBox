APPL_NAME = "LexBox"
APPL_FILE_STORAGE = "STORAGE/"

REST_API_URL = "http://127.0.0.1:5000/hello"
MONGODB_CONNECTION_STRING = "mongodb+srv://lexbox_user31:1JAaZTd6HYIdh0YM@cluster0.sl0s8.mongodb.net/lexbox?retryWrites=true&w=majority"

# Name of fields in HTML for file inputs
# Used later in file check&validation
FILE_INPUT_NAMES = {"carte_de_identitate": "carte_de_identitate", "imagine_proces_verbal": "imagine_proces_verbal",
                    "imagine_chitanta_plata": "imagine_chitanta_plata", "imagine_orice_alta_imagine": "imagine_orice_alta_imagine"}
FILE_INPUT_PREFIX = {"carte_de_identitate": "CI_", "imagine_proces_verbal": "PV_", "imagine_chitanta_plata": "CP_", "imagine_orice_alta_imagine": "AI_"}
