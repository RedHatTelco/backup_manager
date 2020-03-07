#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2017, Ansible by Red Hat, inc
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
import os

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text

def main():
    """ main entry point for module execution
    """
    argument_spec = dict(
        repo=dict(type='path', required=True),
        remote=dict(default='origin'),
        branch=dict(default='master')
    )

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    repo = module.params['repo']
    remote = module.params['remote']
    branch = module.params['branch']

    result = {'changed': False}

    if not os.path.exists(repo):
        module.fail_json(msg='repo %s does not exist' % repo)
    os.chdir(repo)

    _rc, _out, _err = module.run_command('git push %s %s --dryrun' % (remote, branch))

    if 'Everything up-to-date' not in _out:
        if not module.check_mode:
            _rc, _out, _err = module.run_command('git push %s %s' % (remote, branch))
            if _rc > 0:
                module.fail_json(msg=to_text(_err.strip()))
        result['changed'] = True

    module.exit_json(**result)

if __name__ == '__main__':
    main()
