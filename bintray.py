import json
import subprocess

o = {
        'package': {
            'name': 'test-cli',
            'repo': 'pros-test',
            'subject': 'purdue-sigbots'
        },
        'version': {
            'name': open('version').read().strip(),
            'desc': str(subprocess.check_output(['git', 'log', '-1', '--format=%B'])).strip(),
            'vcs_tag': open('version').read().strip(),
        },
        'files': [
            { 'includePattern': './(pros_cli-.*\\\\.zip)', 'uploadPattern': '$1' },
            { 'includePattern': './dist/(.*\\\\.whl)', 'uploadPattern': '$1' }
        ]
    }

with open('bintray.json', 'w') as f:
    json.dump(o, f)