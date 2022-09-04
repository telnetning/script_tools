# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# pip3 install python-leetcode
import leetcode

# Get the next two values from your browser cookies
leetcode_session = ""
csrf_token = ""

# Experimental: Or CSRF token can be obtained automatically
# import leetcode.auth
# csrf_token = leetcode.auth.get_csrf_cookie(leetcode_session)

configuration = leetcode.Configuration()

configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_client = leetcode.ApiClient(configuration)
api_instance = leetcode.DefaultApi(api_client)

def get_submissions():
    # https://leetcode.com/api/submissions/?offset=0&limit=20&lastkey=
    # Authentication setting

    auth_settings = [
        "cookieCSRF",
        "cookieSession",
        "headerCSRF",
        "referer",
    ]  # noqa: E501

    path_params = {}
    query_params = {
        "offset": 0,
        "limit": 20
    }
    header_params = {}
    header_params["Accept"] = api_client.select_header_accept(
        ["application/json"]
    )

    (data) = api_client.call_api(
        "/api/submissions/",
        "GET",
        path_params,
        query_params,
        header_params,
        body = None,
        post_params = [],
        files = {},
        response_type="InlineResponse200",
        auth_settings=auth_settings,
        async_req=None,
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=None,
        collection_formats = {},
    )

    return data

if __name__ == '__main__':
    print(get_submissions())
