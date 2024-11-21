import io
import os
import json
import argparse
import requests
from flask import Flask, send_file, render_template

def validate_args_type(args):
    try:
        args.api_picture_channels = json.loads(args.api_picture_channels)
        assert isinstance(args.api_picture_channels, list)
    except:
        raise ValueError('API_PICTURE_CHANNELS must be a valid list.')

    try:
        args.api_params = json.loads(args.api_params)
        assert isinstance(args.api_params, dict)
    except:
        raise ValueError('API_PARAMS must be a valid dictionary.')

def argument_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--api_username', type=str, default=os.getenv('API_USERNAME'))
    arg_parser.add_argument('--api_password', type=str, default=os.getenv('API_PASSWORD'))
    arg_parser.add_argument('--api_endpoint', type=str, default=os.getenv('API_ENDPOINT'))
    arg_parser.add_argument('--api_params', type=str, default=os.getenv('API_PARAMS', '{}'))
    arg_parser.add_argument('--api_picture_channels', type=str, default=os.getenv('API_PICTURE_CHANNELS'))
    return arg_parser.parse_args()


def create_app(args):
    app = Flask(__name__)

    def get_dvr_picture(args, channel):
        response = requests.get(f'{args.api_endpoint}/{channel}',
                                params=args.api_params,
                                auth=(args.api_username,args.api_password),
                                stream=True)
        print(response)
        picture = io.BytesIO(response.content)
        return picture

    @app.route('/')
    def home():
        return 'DVR API'

    @app.route('/channels')
    def channels():
        body = '<a href="/view-all">View all</a><br>'
        for channel in args.api_picture_channels:
            body += f'<a class="channel" href="/{channel}">{channel}</a><br>'
        return body

    @app.route('/view-all')
    def index():
        return render_template('index.j2.html', channels=args.api_picture_channels)

    @app.route(f'/<path:channel>')
    def channel(channel):
        if channel not in args.api_picture_channels:
            return 'Channel not found', 404
        picture = get_dvr_picture(args, channel)
        return send_file(picture, mimetype='image/jpeg')

    return app

def main():
    args = argument_parser()
    validate_args_type(args)
    app = create_app(args)
    app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
