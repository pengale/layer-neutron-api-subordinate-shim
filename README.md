# Overview

This is a shim charm meant for faciliating testing of the neutron-api
charm's subordinate interface. Use it if you want to test things like
overriding values in the neutron.conf.

# Usage

Deploy neutron-api, with accompanying services. Set the plugin legacy
mode to false. Then deploy this charm.

juju deploy some-minimal-neutron-api-bundle.yaml
juju config neutron-api manage-neutron-plugin-legacy-mode=false

juju deploy /path/to/this/charm
juju relate neturon-api neutron-api-suboridinate-stub

# Contact Information

Fee free to contact the charm's author if you have any questions:
pete.vandergiessen@canonical.com
freenode#petevg
https://github.com/petevg/neutron-api-subordinate-shim