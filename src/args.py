import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--logLevel',
                    default='info',
                    help='Provide logging level. Example --logLevel debug, default=warning')
parser.add_argument('--apiKey',
                    required=True,
                    help='Provide Telegram Bot API key')
parser.add_argument('--heartbeatUrl',
                    required=True,
                    help='Provide URL for heartbeat')
parser.add_argument('--chat',
                    required=True,
                    help='Provide Chat_id for notification')

args = parser.parse_args()
