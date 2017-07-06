import json

with(open('bintray.json', 'rw')) as f:
    json.dump({
        'package': {
            'name': 'test-cli',
            'repo': 'pros-test',
            'subject': 'purdue-sigbots'
        },
        'version': {
            'name': open('version').read().strip()
        }
    })