from corsheaders.signals import check_request_enabled


def cors_allow_admin_to_everyone(sender, request, **kwargs):
    return request.path.startswith('/admin/')


check_request_enabled.connect(cors_allow_admin_to_everyone)
