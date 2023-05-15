def fail_response(message) -> dict:
    return {
        "status": False,
        "message": message
    }


def success_response(responses, message) -> dict:
    return {
        "status": True,
        "message": message,
        "data": responses
    }
