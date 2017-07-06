import json

with(open('bintray.json', 'w')) as f:
    json.dump({
        'package': {
            'name': 'test-cli',
            'repo': 'pros-test',
            'subject': 'purdue-sigbots'
        },
        'version': {
            'name': open('version').read().strip(),
            'desc': subprocess.check_output(['git', 'log', '-1', '--format=%B']),
            'vcs_tag': open('version').read().strip(),
        },
        'files': [
            { 'includePattern': './(pros_cli-.*\\\\.zip)', 'uploadPattern': '$1' },
            { 'includePattern': './dist/(.*\\\\.whl)', 'uploadPattern': '$1' }
        ]
    }, f)