import io
import os
import json
import argparse
import requests
from flask import Flask, send_file, render_template
from flask_caching import Cache


class DVR:
    def __init__(self, args):
        self.api_username = args.api_username
        self.api_password = args.api_password
        self.api_endpoint = args.api_endpoint
        self.api_params = args.api_params
        self.api_picture_channels = args.api_picture_channels

    def get_picture(self, channel):
        response = requests.get(f'{self.api_endpoint}/{channel}',
                                params=self.api_params,
                                auth=(self.api_username,self.api_password),
                                stream=True)
        return response.content


def argument_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--api_username', type=str, default=os.getenv('API_USERNAME'))
    arg_parser.add_argument('--api_password', type=str, default=os.getenv('API_PASSWORD'))
    arg_parser.add_argument('--api_endpoint', type=str, default=os.getenv('API_ENDPOINT'))
    arg_parser.add_argument('--api_params', type=str, default=os.getenv('API_PARAMS', '{}'))
    arg_parser.add_argument('--api_picture_channels', type=str, default=os.getenv('API_PICTURE_CHANNELS'))
    return arg_parser.parse_args()


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


def create_app(args):
    cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
    app = Flask(__name__)
    cache.init_app(app)
    dvr = DVR(args)

    @app.route('/')
    def home():
        body = '<a href="/view-all">View all</a><br>'
        for channel in args.api_picture_channels:
            body += f'<a class="channel" href="/{channel}">{channel}</a><br>'
        return body

    @app.route('/view-all')
    def index():
        return render_template('index.j2.html', channels=args.api_picture_channels)

    @app.route(f'/<path:channel>')
    @cache.cached(timeout=1)
    def channel(channel):
        if channel not in args.api_picture_channels:
            return 'Channel not found', 404
        picture = io.BytesIO(dvr.get_picture(channel))
        return send_file(picture, mimetype='image/jpeg')

    return app


def main():
    args = argument_parser()
    validate_args_type(args)
    app = create_app(args)
    app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    main()
