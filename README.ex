# Overview

This is a shim charm meant for faciliating testing of the neutron-api
charm's subordinate interface. Use it if you want to test things like
overriding values in the neutron.conf. Or use it if you are writing a
neutron-api subordinate charm, and want a jumping off place. This
charm doesn't have any practical production uses as is.

# Usage

Deploy neutron-api, with accompanying services (TODO: add a minimum
viable use case.)

juju deploy /path/to/this/charm

juju relate neturon-api neutron-api-suboridinate-stub

# Configuration

The configuration options will be listed on the charm store, however If you're
making assumptions or opinionated decisions in the charm (like setting a default
administrator password), you should detail that here so the user knows how to
change it immediately, etc.

# Contact Information

Fee free to contact the charm's author if you have any questions:
pete.vandergiessen@canonical.com
freenode#petevg
https://github.com/petevg/neutron-api-subordinate-shim