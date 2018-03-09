"""
Reactive functions for our shim -- most of our stuff just lives here.
"""

import subprocess

# Install python-apt, before we have import troubles
subprocess.check_call(['apt', 'install', '-y', 'python-apt'])

from charms.reactive import when, when_not, set_state


@when('neutron-plugin-api-subordinate.connected')
def configure_plugin(api_principle):
    """
    Send some data over the relation that should get written to the
    neutron.conf file.

    """
    plugin_config = {
        'neutron-api': {
            '/etc/neutron/neutron.conf': {
                'sections': {
                    'DEFAULT': [
                        ('foo', 'bar')
                    ],
                    'a_plugin': [
                        ('baz', 'qux')
                    ]
                }
            }
        }
    }

    api_principle.configure_plugin(
        neutron_plugin='ovs',
        core_plugin='neutron.plugins.ml2.plugin.Ml2Plugin',
        subordinate_configuration=plugin_config
    )
    # TODO prevent this from repeating, add config changed hook
