from flask import Flask, request
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def get_route():  # put application's code here

    with open('request_info.txt', 'a') as f:
        write_request_to_file(request.headers, request.args, request.get_data(as_text=True), method="GET")
    return "Success"

@app.post('/')
def post_route():  # put application's code here
    write_request_to_file(request.headers, request.args, request.get_data(as_text=True), method="POST")
    return "Success"


def write_request_to_file(headers, parameters, body, method="GET"):
    with open('request_info.txt', 'a') as f:
        f.write(f"Request at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"\n{'=' * 50}\n")
        f.write(f"Method: {method}\n")
        f.write("Headers:\n")
        for key, value in headers:
            f.write(f"{key}: {value}\n")
        f.write("\nParameters:\n")
        f.write(",".join([f"{key}={value}" for key, value in parameters.items()]) + "\n")
        f.write("\nBody:\n")
        f.write(body + "\n")


if __name__ == '__main__':
    app.run()
