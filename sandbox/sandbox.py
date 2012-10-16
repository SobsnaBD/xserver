"""
"""

def record_suspicious_submission(msg, code_str):
    """
    Record a suspicious submission:

    TODO: upload to edx-studentcode-suspicious bucket on S3.  For now, just
    logging to avoids need for more config changes (S3 credentials, python
    requirements).
    """
    log.warning('Suspicious code: {0}, {1}'.format(msg, code_str))

def sandbox_cmd_list():
    """
    Return a command to use to run a python script in a sandboxed env.

    NOTE: this is kind of ugly--we should really have all copy-to-tmp dir and
    run logic here too, but then we'd have to duplicate it for testing in the
    content repo.
    """
    return ['sudo', '-u', 'sandbox', '/usr/bin/python-sandbox']
