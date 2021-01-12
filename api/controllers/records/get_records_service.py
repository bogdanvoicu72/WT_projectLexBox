import json

from bson import ObjectId

from common.response_builder import ResponseBuilder


def build_result(document, user):
    return {
        "_id": str(document["_id"]),
        "data": document["record_date"],
        "docx": document["docx"],
        "files": document["filenames"],
        "user": user["firstName"] + " " + user["lastName"],
        "inspectorat": document["institutia_agent"],
        "status": document["status_dosar"]
    }


def get_records_service(request, records, users):
    try:
        records_lst = []
        cursor = records.find({})
        for document in cursor:
            user = users.find_one({"_id": ObjectId(document['uid'][0])})
            records_lst.append(build_result(document=document, user=user))

        return ResponseBuilder.success({"records": records_lst})
    except Exception as e:
        return ResponseBuilder.failure(str(e))
